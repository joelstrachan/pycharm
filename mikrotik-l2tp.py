import random
import string
import paramiko
import time


def ssh(ip):
    try:
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        session.connect(ip, username=un, password=pw)
        selected_cmd_file = open(file, 'r')
        selected_cmd_file.seek(0)
        for each_line in selected_cmd_file.readlines():
            connection = session.exec_command(each_line + '\n')
            time.sleep(1)

        selected_cmd_file.close()
        session.close()
        print("======================Configuration Done======================")
    except paramiko.AuthenticationException:
        print("* invalid username or password \n Please check the configuration.")


file = input("please enter the file name you want to save this configuration to: ")

file = file + '.txt'

print(f"Full file name is: {file}")

file1 = open(file, 'a')

print("-" * 20)
print("DHCP Configuration")
print("-" * 20)

# default values
dhcp_pool_name = "l2tp-dhcp-pool-1"
dhcp_pool_ip_address_range = "10.10.1.1-10.10.1.200"
dhcp_pool_comment = "l2tp-pool"

print("default values for L2TP DHCP Pool Are as follows")

print(f"""
Default DHCP Values
Pool Name: {dhcp_pool_name}
IP Address Range: {dhcp_pool_ip_address_range}
DHCP Pool Comment: {dhcp_pool_comment}
""")

response = str(input("Are the default values correct? (yes/no) :"))

# while response.lower() not in ['yes', 'no']:
#    response = str(input("please enter proper response: "))

if response == 'no':
    print("will now enter correct values")
    loop = True
    while loop:

        print("Enter name for DHCP Pool:")
        dhcp_pool_name = input("EG: l2tp dhcp pool: ")
        print("Enter pool ip address range: ")
        dhcp_pool_ip_address_range = input("EG: 192.168.1.100-192.168.1.200: ")
        print("Enter DHCP Pool Comment: ")
        dhcp_pool_comment = input("This is the DHCP pool for l2tp Pool: ")

        print(f"""
        DHCP Inforamtion entered
        Pool Name: {dhcp_pool_name}
        IP Address Range: {dhcp_pool_ip_address_range}
        DHCP Pool Comment: {dhcp_pool_comment}
        """)

        response = str(input("Is the information entered correct? (yes/no) :"))

        while response.lower() not in ['yes', 'no']:
            response = str(input("please enter proper response: "))

        if response.lower() == 'no':
            continue

        if response.lower() == 'yes':
            print("Will continue to next seciont")
            break
else:
    print("will now continue to next section")

    print("-" * 20)
    print("L2TP Secret")
    print("-" * 20)

loop = True
while loop:

    ipsec_password = input("Enter IPSec Password: ")

    print(f"""
    DHCP Inforamtion entered
    L2TP Secret: {ipsec_password}
    """)

    response = str(input("Is the information entered correct? (yes/no) :"))

    while response.lower() not in ['yes', 'no']:
        response = str(input("please enter proper response: "))

    if response.lower() == 'no':
        continue

    if response.lower() == 'yes':
        print("Will continue to next seciont")
        break

loop = True
while loop:

    print("-" * 20)
    print("L2TP Profile Information")
    print("-" * 20)

    profile_name = input("Please enter Profile name:")

    secret_username = input("Enter secret User name: ")
    secret_password = input("Enter secret password: ")

    print(f"""
    L2TP Profile Information Entered
    L2TP Profile Name Entered: {profile_name}
    Username Entered: {secret_username}
    Password Entered: {secret_password}
    """)

    response = str(input("Is the information entered correct? (yes/no) :"))

    while response.lower() not in ['yes', 'no']:
        response = str(input("please enter proper response: "))

    if response.lower() == 'no':
        continue

    if response.lower() == 'yes':
        print("Will continue to next seciont")
        break

# add filter rules to router
file1.write(
    f'/ip firewall filter add action=accept chain=input dst-port=500,4500,1701 in-interface=ether1 protocol=udp comment="L2TP - Layer 2 UDP Rules"\n')

file1.write(
    f'/ip pool add name="{dhcp_pool_name}" ranges={dhcp_pool_ip_address_range} comment="{dhcp_pool_comment}" \n')

file1.write(f"/interface l2tp-server server set enable=yes\n")

file1.write(f"/interface l2tp-server server set use-ipsec=yes\n")

file1.write(f"/interface l2tp-server server set ipsec-secret={ipsec_password}\n")

file1.write(
    f'/ppp profile add dns-server=10.0.1.10 local-address=10.10.0.1 name={profile_name} remote-address="{dhcp_pool_name}"\n')

file1.write(f'/ppp secret add name={secret_username} password={secret_password} profile={profile_name} service=l2tp\n')

file1.close()

print("would you like to push this config to a router")

response = str(input("do you want to push config to router? (yes/no) :"))

if response == 'yes':

    loop = True
    while loop:

        print("-" * 20)
        print("Mikrotik L2TP Script")
        print("End router details")
        print("-" * 20)

        ip = input("please enter your ip address of your router: ")
        un = input("please enter your SSH uesrname: ")
        pw = input("Please enter your SSH password: ")
        print(f"""
        Router Details Entered
        IP Address: {ip}
        Username: {un}
        password: {pw}
        """)

        response = str(input("Is the information entered correct? (yes/no) :"))

        while response.lower() not in ['yes', 'no']:
            response = str(input("please enter proper response: "))

        if response.lower() == 'no':
            continue

        if response.lower() == 'yes':
            print("Will continue to next seciont")
            break

    print("sending config to router")
    ssh(ip)

else:
    print("end of router l2tp config")



