import random
import string
import paramiko
import time


def router_info(
        router_ip_address,
        router_username,
        router_password):
    print("would you like to push this config to a router")

    response = str(input("do you want to push config to router? (yes/no) :"))

    if response == 'yes':

        loop = True
        while loop:

            print(f"""
            Router Values
            IP Address: {router_ip_address}
            Router Username: {router_username}
            Router Password: {router_password}
            """)

            response = str(input("Is the information entered correct? (yes/no) :"))


            while response.lower() not in ['yes', 'no']:
                response = str(input("please enter proper response: "))

            if response.lower() == 'no':

                router_ip_address = input("please enter your ip address of your router: ")
                router_username = input("please enter your SSH uesrname: ")
                router_password = input("Please enter your SSH password: ")
                print(f"""
                Router Details Entered
                IP Address: {router_ip_address}
                Username: {router_username}
                password: {router_password}
                """)

                continue

            if response.lower() == 'yes':
                print("Will continue to next seciont")
                break

        print("sending config to router")
        ssh(router_ip_address)

        current_config(
            dhcp_pool_name,
            dhcp_pool_ip_address_range,
            dhcp_pool_comment,
            ipsec_password,
            L2TP_profile_name,
            L2TP_un,
            L2TP_pw,
            router_ip_address,
            router_username,
            router_password,
        )

    else:
        current_config(
            dhcp_pool_name,
            dhcp_pool_ip_address_range,
            dhcp_pool_comment,
            ipsec_password,
            L2TP_profile_name,
            L2TP_un,
            L2TP_pw,
            router_ip_address,
            router_username,
            router_password,
        )


def ssh(router_ip_address):
    try:
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        session.connect(router_ip_address, username=router_username, password=router_password)
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


def current_config(
dhcp_pool_name,
dhcp_pool_ip_address_range,
dhcp_pool_comment,
ipsec_password,
L2TP_profile_name,
L2TP_un,
L2TP_pw,
router_ip_address,
router_username,
router_password,):
    print(f"""
                            ***This is the current config***
                 DHCP Information - Option 1                                    L2TP Settings - Option 2
         - DHCP Pool Name:{dhcp_pool_name}                          - IPSEC Password:{ipsec_password}
         - DHCP IP Address Range:{dhcp_pool_ip_address_range}\t\t   - L2TP Profile Name:{L2TP_profile_name}
         - DHCP Pool Comment:{dhcp_pool_comment}

                User Credentials - Option 3                                     Router Details - Option 4
         - L2tp username:{L2TP_un}                                  - IP Address:{router_ip_address}
         - L2TP Password:{L2TP_pw}                                  - Username:{router_username}
                                                                    - Password:{router_password}
         
            
            Options
            1 - Edit DHCP Options
            2 - Edit L2TP Settings  
            3 - Edit User Crednetials
            4 - Edit Router Details
            5 - Write to File
            6 - Write to Router
            7 - Exit
    """)
    menu_input()

def menu_input():

    response = str(input("Enter what option you would like to select ('1'-'7') :"))

    while response.lower() not in ['1', '2', '3', '4', '5', '6', '7',]:
        response = str(input("please enter proper response: "))

    if response.lower() == '1':
        print("this is option 1")

    elif response.lower() == '2':
        print("this is option 2")

    elif response.lower() == '3':
        print("this is option 3")

    elif response.lower() == '4':
        print("this is option 4")


    elif response.lower() == '5':
        print("open write to file options")

        write_to_file()


    elif response.lower() == '6':
        print("open router send to pgm")
        router_info(
        router_ip_address,
        router_username,
        router_password
        )

    else:
        exit(1000000)




# default dhcp values
dhcp_pool_name = "l2tp-dhcp-pool-1"
dhcp_pool_ip_address_range = "10.10.1.1-10.10.1.200"
dhcp_pool_comment = "l2tp-pool"

#default L2TP settings
ipsec_password = "password"
L2TP_profile_name = "L2TP_profile"

#default user credentials
L2TP_un = "L2TP_user"
L2TP_pw = "L2TP_password"

#default router credentials
router_ip_address = "192.168.2.3"
router_username = "admin-test"
router_password = "12345678"

def write_to_file():
    file = input("please enter the file name you want to save this configuration to: ")

    file = file + '.txt'

    print(f"Full file name is: {file}")

    file1 = open(file, 'a')

    file1.write(f'/ip firewall filter add action=accept chain=input dst-port=500,4500,1701 in-interface=ether1 protocol=udp comment="L2TP - Layer 2 UDP Rules"\n')

    file1.write(f'/ip pool add name="{dhcp_pool_name}" ranges={dhcp_pool_ip_address_range} comment="{dhcp_pool_comment}" \n')

    file1.write(f"/interface l2tp-server server set enable=yes\n")

    file1.write(f"/interface l2tp-server server set ipsec-secret={ipsec_password}\n")

    file1.write(f'/ppp profile add dns-server=10.0.1.10 local-address=10.10.0.1 name={L2TP_profile_name} remote-address="{dhcp_pool_name}"\n')

    file1.write(f'/ppp secret add name={L2TP_un} password={L2TP_pw} profile={L2TP_profile_name} service=l2tp\n')

    file1.close()

    current_config(
        dhcp_pool_name,
        dhcp_pool_ip_address_range,
        dhcp_pool_comment,
        ipsec_password,
        L2TP_profile_name,
        L2TP_un,
        L2TP_pw,
        router_ip_address,
        router_username,
        router_password,

    )

current_config(
dhcp_pool_name,
dhcp_pool_ip_address_range,
dhcp_pool_comment,
ipsec_password,
L2TP_profile_name,
L2TP_un,
L2TP_pw,
router_ip_address,
router_username,
router_password,
)

menu_input()