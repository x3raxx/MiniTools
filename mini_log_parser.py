import re

with open("sample_logs.txt", 'r') as f:
    content = f.read()

email = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
ip_add = r"Deny connection attempt SRC=(\d+\.\d+\.\d+\.\d+) DST=(\d+\.\d+\.\d+\.\d+)"
malware = r"[\\/][a-zA-Z0-9_.+-]+\.exe"
invalid_user = r"Invalid user (\w+) from (\d+\.\d+\.\d+\.\d+)"

emails = re.findall(email, content)
print("\n📧 Extracted Emails:")
for line in emails:
    print(line)
print("Total Emails:", len(emails))

ip_adds = re.findall(ip_add, content)
print("\n🌐 Extracted IP Pairs (SRC, DST):")
for line in ip_adds:
    print("SRC:", line[0], "-> DST:", line[1])
print("Total IP Pairs:", len(ip_adds))

malwares = re.findall(malware, content)
print("\n🦠 Extracted Malware Paths:")
for line in malwares:
    print(line)
print("Total Malware Paths:", len(malwares))

invalid_users = re.findall(invalid_user, content)
print("\n🚫 Invalid User Logins:")
for line in invalid_users:
    print("User:", line[0], "| IP:", line[1])
print("Total Invalid Users:", len(invalid_users))
