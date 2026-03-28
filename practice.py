count = 0
attacks = {}

with open("logs/sample_auth.log", "r") as f:
    for line in f:
        if "Failed" in line:
            count = count + 1
            ip = line.split("from")[1].split()[0]
            if ip in attacks:
                attacks[ip] = attacks[ip] + 1
            else:
                attacks[ip] = 1


print(f"Failed login attempts found: {count}")
print()
print("Attacks by IP:")
for ip, attempts in attacks.items():
    print(f" {ip} {attempts} attempts")