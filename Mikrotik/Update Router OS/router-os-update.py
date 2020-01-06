import random
import string
import paramiko
import time

def settings():

    router_ip_address = input("please enter the ip address of the router: ")
    router_username = input(please enter username to access router: )
    router_password = input(please enter password to access router: )

    print(f"""details entered are as follows""")

def file_create():

    filename = input("please enter the name of the file you would like to write to: ")
    filename = filename + '.txt'

    print(f"Full file name is: {filename}")

    file1 = open(filename, 'a')

    file1.write(f'/ systemscheduler')
    file1.write('\n')
    file1.write(f'add interval=30d00:00:00 name="Package upgrade" on-event=\\')
    file1.write('\n\t')
    file1.write(f'"system package update install" policy = \\')
    file1.write('\n\t')
    file1.write(f'ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon \\')
    file1.write('\n\t')
    file1.write(f'start - time = 12:00: 00')

    file1.close()




def ssh(router_ip_address):
    try:
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        session.connect(router_ip_address, username=router_username, password=router_password)
        selected_cmd_file = open(filename, 'r')
        selected_cmd_file.seek(0)
        for each_line in selected_cmd_file.readlines():
            connection = session.exec_command(each_line + '\n')
            time.sleep(1)

        selected_cmd_file.close()
        session.close()
        print("======================Configuration Done======================")
    except paramiko.AuthenticationException:
        print("* invalid username or password \n Please check the configuration.")

settings()

file_create()