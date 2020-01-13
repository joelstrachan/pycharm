import random
import string
import paramiko
import time

def ssh(router_ip_address,router_username,router_password,file):
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