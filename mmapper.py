import subprocess
import sys

def nmap_scan(address):
    command = ["nmap", "-p-", "-T4", address]
    subprocess.run(command)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nmap_scan.py [address1] [address2] ...")
        sys.exit(1)

    addresses = sys.argv[1:]
    for address in addresses:
        print("Scanning {}...".format(address))
        nmap_scan(address)
        print("Scan completed for {}\n".format(address))