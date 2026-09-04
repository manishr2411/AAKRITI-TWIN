import serial
import requests
import math
import time
import json

# Replace with the COM port used by your ESP32
SERIAL_PORT = "COM_PORT"
BAUD_RATE = 115200

DB_URL = "https://aakriti-twin-default-rtdb.asia-southeast1.firebasedatabase.app"


def make_packet(data):
    angle = float(data["angle_deg"])
    distance = float(data["distance_cm"])

    rad = math.radians(angle)
    x = round(distance * math.cos(rad), 2)
    y = round(distance * math.sin(rad), 2)

    return {
        "scan_id": data.get("scan_id"),
        "arduino_timestamp": data.get("timestamp"),
        "angle": angle,
        "distance_cm": distance,
        "x": x,
        "y": y,
        "label": "unknown",
        "timestamp": int(time.time())
    }


def push_latest(packet):
    return requests.put(
        f"{DB_URL}/scan/latest.json",
        json=packet,
        timeout=5
    )


def push_history(packet):
    return requests.post(
        f"{DB_URL}/scan/history.json",
        json=packet,
        timeout=5
    )


print("Opening serial port...")
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)

print("Reading serial and uploading to Firebase...")

while True:
    line = ser.readline().decode(errors="ignore").strip()

    if not line:
        continue

    print("RAW:", line)

    try:
        data = json.loads(line)
    except json.JSONDecodeError:
        print("Skipped: invalid JSON")
        continue

    if "angle_deg" not in data or "distance_cm" not in data:
        print("Skipped: required keys not found")
        continue

    if float(data["distance_cm"]) < 0:
        print("Skipped: invalid distance")
        continue

    packet = make_packet(data)

    try:
        r1 = push_latest(packet)
        r2 = push_history(packet)

        print(
            "latest:",
            r1.status_code,
            "history:",
            r2.status_code
        )

    except Exception as e:
        print("Upload error:", e)
