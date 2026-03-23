from collections import defaultdict

failed_attempts = defaultdict(int)

with open("logs.txt", "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-3]
            failed_attempts[ip] += 1

print("\n--- Suspicious Activity Report ---")

for ip, count in failed_attempts.items():
    if count > 3:
        print(f" Possible brute force attack from {ip} ({count} attempts)")

print("\n--- End of Report ---")

