import os

def block_ip(ip):
    print(f"[BLOCKING] Blocking IP: {ip}")
    # os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
    os.system(f"netsh advfirewall firewall add rule name=\"Block {ip}\" dir=in action=block remoteip={ip}")