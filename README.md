# Advanced_Security_Log_Monitor
This project is an advanced log monitoring and threat detection system built for cybersecurity operations. It continuously analyzes system logs to identify suspicious activities using predefined rules and MITRE ATT&CK framework mappings. Upon detecting threats, it can automatically respond by blocking malicious IP addresses and sending real-time alerts via a Telegram bot.

🔧 Features
Identifies security threats by analyzing log patterns

Correlates detections with MITRE ATT&CK tactics and techniques

Sends real-time security alerts through Telegram notifications

Automatically blocks malicious IP addresses using iptables

Offers a live web dashboard for monitoring and visualizing detections

🛠️ Installation
Clone the repository: git clone https://github.com/PrathamBhanushali30/Advanced_log_monitoring.git

cd Advanced-Security-Log-Monitor

Install dependencies: pip install -r requirements.txt*


▶️ Usage
Run the detection engine: python detection_engine.py

Start the dashboard server: python dashboard/app.py

📡 Alerts & Actions
Alerts are sent via Telegram using the Telegram Bot API.

Detected malicious IPs are automatically blocked using iptables.


📌 Requirements
Python 3.8+

Linux (for iptables functionality)

Telegram Bot API token & chat ID


📚 License
This project is for educational and cybersecurity awareness purposes.
