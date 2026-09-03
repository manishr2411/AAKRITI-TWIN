import requests

DB_URL = "https://aakriti-twin-default-rtdb.asia-southeast1.firebasedatabase.app"


def push_latest(packet):
    return requests.put(f"{DB_URL}/scan/latest.json", json=packet, timeout=5)


def push_history(packet):
    return requests.post(f"{DB_URL}/scan/history.json", json=packet, timeout=5)


def send_packet_to_firebase(packet):
    """
    Send one packet to Firebase:
    - latest = overwrite current latest packet
    - history = append packet with auto key
    """
    r1 = push_latest(packet)
    r2 = push_history(packet)
    return r1, r2