"""
SSH ANALYSER
"""

import requests

def get_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
        data = response.json()
        if data["status"] == "success":
            return f"{data['city']}, {data['country']}"
        else:
            return "Unknown location"
    except:
        return "Location unavailable"


count = 0
attacks = {}
successful = {}

with open("logs/sample_auth.log", "r", encoding="utf-8") as f:
    for line in f:
        if "Failed" in line:
            count = count + 1
            ip = line.split("from")[1].split()[0]
            if ip in attacks:
                attacks[ip] = attacks[ip] + 1
            else:
                attacks[ip] = 1
        if "Accepted" in line:
            ip = line.split("from")[1].split()[0]
            user = line.split("for")[1].split()[0]
            if ip in successful:
                successful[ip] = successful[ip] + 1
            else:
                successful[ip] = 1


print(f"Failed login attempts found: {count}")
print()
print("Attacks by IP:")
for ip, attempts in attacks.items():
    location = get_location(ip)
    if ip in successful:
        print(f" {ip} {location} {attempts} (also successful)")
    else:
        print(f" {ip} {location} {attempts} attempts")

print()
print("Successful logins:")
for ip, count in successful.items():
    print(f" {ip} {count} successful logins")

