import subprocess
import argparse
import re
import sys


#Parsing and Validating Command Line Arguments
def get_arguments():
    parser = argparse.ArgumentParser(description="Change your MAC address.")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="mac_address", required=True, help="New MAC address")
    args = parser.parse_args()


    # Validate the MAC address format
    if not re.match(r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$", args.mac_address):
        parser.error("Invalid MAC address format. Please use the format XX:XX:XX:XX:XX:XX.")
    return args


#Changing the MAC Address
def change_mac(interface, mac_address):
    try:
        print(f"[+] Changing MAC address for {interface} to {mac_address}")
        subprocess.check_call(["sudo", "ifconfig", interface, "down"])
        subprocess.check_call(["sudo", "ifconfig", interface, "hw", "ether", mac_address])
        subprocess.check_call(["sudo", "ifconfig", interface, "up"])
    except subprocess.CalledProcessError:
        print("[!] Failed to change MAC address.")
        sys.exit(1)

#Retrieving the Current MAC Address
def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface], text=True)
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("[!] Could not read MAC address.")
    except subprocess.CalledProcessError:
        print(f"[!] Could not execute ifconfig for {interface}.")
        sys.exit(1)

#Main Function to Execute MAC Address Change
def main():
    args = get_arguments()
    current_mac = get_current_mac(args.interface)
    print(f"Current MAC: {current_mac}")

    change_mac(args.interface, args.mac_address)

    updated_mac = get_current_mac(args.interface)
    if updated_mac == args.mac_address:
        print(f"[+] MAC address was successfully changed to {updated_mac}")
    else:
        print("[!] MAC address did not get changed.")

if __name__ == "__main__":
    main()
