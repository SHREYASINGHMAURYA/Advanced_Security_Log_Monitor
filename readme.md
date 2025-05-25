# 📊 Advanced Security Log Monitor
This project is an advanced log monitoring and detection system designed for cybersecurity threat detection and response. It monitors logs, detects suspicious activities based on predefined rules and MITRE ATT&CK mappings, and takes automated actions like blocking IPs and sending real-time alerts to a Telegram bot.

# 🚀 Features
Detects security incidents based on log patterns

Maps detections to MITRE ATT&CK tactics and techniques

Sends instant security alerts via Telegram

Automatically blocks malicious IPs using iptables

Provides a real-time web dashboard to view detections

# 🛠️ Installation
Clone the repository:

git clone https://github.com/PrathamBhanushali30/Advanced_log_monitoring.git

cd Advanced-Security-Log-Monitor


Install dependencies:

pip install -r requirements.txt


# ▶️ Usage

Run the detection engine:

python detection_engine.py


Start the dashboard server:

python dashboard/app.py


# 📡 Alerts & Actions
Alerts are sent via Telegram using the Telegram Bot API.

Detected malicious IPs are automatically blocked using iptables.

# 📌 Requirements
Python 3.8+

Linux (for iptables functionality)

Telegram Bot API token & chat ID

# 📚 License
This project is for educational and cybersecurity awareness purposes.
