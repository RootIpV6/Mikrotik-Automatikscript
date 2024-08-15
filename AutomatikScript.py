# Define IP address information
ip_range = "192.168.1.0/24"
gateway = "192.168.1.1"
dns1 = "8.8.8.8"
dns2 = "8.8.4.4"
interface = "ether1"


# Create MikroTik script
mikrotik_script = f"""
/ip address
add address={gateway}/24 interface={interface}
/ip dhcp-server network
add address={ip_range} gateway={gateway} dns-server={dns1},{dns2}
/ip pool
add name=dhcp_pool ranges={ip_range}
/ip dhcp-server
add address-pool=dhcp_pool interface={interface} lease-time=10m name=dhcp1
"""

# Write the script to a file
with open("mikrotik_script.rsc", "w") as file:
    file.write(mikrotik_script)

print("MikroTik scripti oluşturuldu.")
