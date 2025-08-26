import re

with open("strings.txt", "r") as f:
    data = f.read()

ips = re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", data)
domains = re.findall(r"\b(?:[a-zA-Z0-9-]+\.)+[a-z]{2,}\b", data)
urls = re.findall(r"https?://[^\s'\"]+", data)
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w{2,}\b", data)
hashes = re.findall(r"\b[a-fA-F0-9]{32,64}\b", data)

print("IPs:", ips)
print("Domains:", domains)
print("URLs:", urls)
print("Emails:", emails)
print("Hashes:", hashes)
