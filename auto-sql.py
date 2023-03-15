import subprocess
import os

target = input("Enter the target domain: ")

# Subfinder
print("Running Subfinder...")
subfinder_command = f"subfinder -d {target} -o subdomains.txt"
subprocess.run(subfinder_command, shell=True)

# HTTPX
print("Running HTTPX...")
httpx_command = f"httpx -l subdomains.txt -o httpx_output.txt"
subprocess.run(httpx_command, shell=True)

# Waybackurls
print("Running Waybackurls...")
waybackurls_command = f"cat httpx_output.txt | waybackurls > waybackurls_output.txt"
subprocess.run(waybackurls_command, shell=True)

# GF SQLi
print("Running GF SQLi...")
gf_sqli_command = f"cat waybackurls_output.txt | gf sqli > gf_sqli_output.txt"
subprocess.run(gf_sqli_command, shell=True)

# SQLMap
print("Running SQLMap...")
with open("gf_sqli_output.txt", "r") as file:
    vulnerable_urls = file.readlines()

for url in vulnerable_urls:
    url = url.strip()
    print(f"Testing URL: {url}")
    sqlmap_command = f"sqlmap -u {url} --random-agent --batch"
    subprocess.run(sqlmap_command, shell=True)

print("Finished!")
