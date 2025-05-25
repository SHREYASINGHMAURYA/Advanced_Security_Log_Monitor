import requests

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            return {
                "City": data.get("city"),
                "Region": data.get("region"),
                "Country": data.get("country"),
                "Org": data.get("org")
            }
        else:
            return {"Error": "Could not retrieve info"}
    except Exception as e:
        return {"Error": str(e)}