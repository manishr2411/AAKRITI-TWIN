import serial
import json
from pathlib import Path
from src.utils.cloud_sender import send_packet_to_firebase

COM_PORT = "COM12"   # change if needed
BAUD_RATE = 115200

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LIVE_SCAN_FILE = DATA_DIR / "live_scan.json"
SNAPSHOT_FILE = DATA_DIR / "latest_snapshot.json"
OBJECT_FILE = DATA_DIR / "sample_objects.json"

DATA_DIR.mkdir(exist_ok=True)

if not LIVE_SCAN_FILE.exists():
    LIVE_SCAN_FILE.write_text("[]", encoding="utf-8")

if not SNAPSHOT_FILE.exists():
    SNAPSHOT_FILE.write_text('{"scan_points": [], "objects": []}', encoding="utf-8")


def safe_load_json(file_path, default):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def safe_write_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def update_snapshot(scan_points):
    objects = safe_load_json(OBJECT_FILE, [])
    snapshot = {
        "scan_points": scan_points,
        "objects": objects
    }
    safe_write_json(SNAPSHOT_FILE, snapshot)


def normalize_packet(raw):
    required = {"scan_id", "timestamp", "angle_deg", "distance_cm"}
    if not required.issubset(raw.keys()):
        return None

    try:
        packet = {
            "scan_id": int(raw["scan_id"]),
            "timestamp": int(raw["timestamp"]),
            "angle_deg": float(raw["angle_deg"]),
            "distance_cm": float(raw["distance_cm"]),
        }
    except Exception:
        return None

    if packet["distance_cm"] == -1:
        return None

    return packet


def main():
    print(f"[INFO] Opening {COM_PORT} at {BAUD_RATE} baud")
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)

    current_scan_id = None
    current_sweep = []

    print("[INFO] Collector started. Press Ctrl+C to stop.")

    try:
        while True:
            line = ser.readline().decode("utf-8", errors="ignore").strip()

            if not line:
                continue

            try:
                raw = json.loads(line)
            except json.JSONDecodeError:
                print(f"[WARN] Bad JSON skipped: {line}")
                continue

            packet = normalize_packet(raw)
            if packet is None:
                continue

            packet_scan_id = packet["scan_id"]

            if current_scan_id is None:
                current_scan_id = packet_scan_id

            if packet_scan_id != current_scan_id:
                safe_write_json(LIVE_SCAN_FILE, current_sweep)
                update_snapshot(current_sweep)
                print(f"[INFO] Saved scan_id={current_scan_id} with {len(current_sweep)} points")
                current_scan_id = packet_scan_id
                current_sweep = []

            current_sweep.append(packet)

            safe_write_json(LIVE_SCAN_FILE, current_sweep)
            update_snapshot(current_sweep)

            try:
                r1, r2 = send_packet_to_firebase(packet)
                print(f"[FIREBASE] latest={r1.status_code}, history={r2.status_code}")
            except Exception as e:
                    print(f"[FIREBASE ERROR] {e}")
            print(packet)

    except KeyboardInterrupt:
        print("\n[INFO] Stopping collector...")
        if current_sweep:
            safe_write_json(LIVE_SCAN_FILE, current_sweep)
            update_snapshot(current_sweep)

    finally:
        if ser.is_open:
            ser.close()
        print("[INFO] Serial closed.")


if __name__ == "__main__":
    main()