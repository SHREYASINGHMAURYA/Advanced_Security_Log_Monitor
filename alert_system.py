import requests

def send_alert(ip, ip_info, event):
    token = 'Your Bot Token'
    chat_id = 'Your chat Id'
    
    message = (
        f"⚠️ Security Alert Detected!\n"
        f"IP: {ip}\n"
        f"Location: {ip_info}\n"
        f"Tactic: {event['Tactic']}\n"
        f"Technique: {event['Technique']}\n"
        f"MITRE ID: {event['MITRE ID']}"
    )
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': message}
    
    try:
        response = requests.post(url, data=payload, verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not send alert: {e}")