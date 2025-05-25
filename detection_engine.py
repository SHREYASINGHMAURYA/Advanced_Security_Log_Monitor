import json
import re
import os
import datetime
from threat_intel import get_ip_info
from alert_system import send_alert
from firewall_block import block_ip

# Load MITRE mapping
with open("mitre_mapping.json", "r") as f:
    mitre_mapping = json.load(f)

# Load detection rules
with open("logs/detections.json", "r") as f:
    detection_rules = json.load(f)

# Read log file
log_file_path = "logs/auth.log"
if not os.path.exists(log_file_path):
    print(f"[ERROR] Log file not found: {log_file_path}")
    exit(1)

with open(log_file_path, "r") as file:
    log_lines = file.readlines()

# Initialize detection log file
log_path = "logs/detection_log.json"
if os.path.exists(log_path):
    with open(log_path, "r") as f:
        detection_log = json.load(f)
else:
    detection_log = []

# Detection logic
for line in log_lines:
    for rule in detection_rules:
        pattern = rule["Pattern"]
        if re.search(pattern, line):
            # Extract IP address
            ip_match = re.search(r"(\d{1,3}(?:\.\d{1,3}){3})", line)
            if ip_match:
                ip = ip_match.group(1)
            else:
                ip = "Unknown"

            # Fetch IP details
            ip_info = get_ip_info(ip)

            # Send alert to Telegram
            send_alert(ip, ip_info, rule)

            # Block the IP using iptables
            if ip != "Unknown":
                block_ip(ip)

            # Log the detection
            log_entry = {
                "time": str(datetime.datetime.now()),
                "ip": ip,
                "ip_info": ip_info,
                "event": rule
            }

            detection_log.append(log_entry)

            print(f"[DETECTED] {rule['Technique']} - IP: {ip}")

# Write updated detection log
with open(log_path, "w") as f:
    json.dump(detection_log, f, indent=4)

print(f"[DONE] Detection process completed. Total detections: {len(detection_log)}")