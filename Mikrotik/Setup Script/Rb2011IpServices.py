def IpServices(filename):

    #default settings
    telnet = 'yes'
    ftp = 'yes'
    www = 'yes'
    api = 'yes'
    apissl = 'yes'
    ssh = 'no'
    winbox = 'no'
    wwwssl = 'yes'

    print(f"""
    Default settings are as follows

    Telnet disabled                 {telnet}
    FTP disabled                    {ftp}
    HTTP Web Interface disabled     {www}
    API Interface disabled          {api}
    API=SSL disabled                {apissl}
    SSH disabled                    {ssh}
    Winbox Access disabled          {winbox}
    WWW-SSL Access disabled         {wwwssl}
    """)

    response = str(input("Are the default values correct? (yes/no) :"))

    if response == 'no':
        print("will now enter correct values")
        loop = True
        while loop:

            print("Disable Telnet access yes/no:")
            telnet = input("yes or no: ")
            print("Disable FTP Access: ")
            ftp = input("yes or no: ")
            print("Disable WWW Access: ")
            www = input("yes or no: ")
            print("Disable API Access:")
            api = input("yes or no: ")
            print("Disable API SSL Access:")
            apissl = input("yes or no: ")
            print("Disable SSL Access:")
            ssh = input("yes or no: ")
            print("Diable Winbox Access:")
            winbox = input("yes or no: ")
            print("Diable WWW SSL Access:")
            wwwssl = input("yes or no: ")

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

    write_to_file(filename,telnet,ftp,www,api,apissl,ssh,winbox,wwwssl)











def write_to_file(filename,telnet,ftp,www,api,apissl,ssh,winbox,wwwssl):
        file = filename

        #file = file + '.txt'

        print(f"Full file name is: {file}")

        file1 = open(file, 'a')

        file1.write(f'\n')
        file1.write(f'/ip service set telnet disabled={telnet}\n')
        file1.write(f'/ip service set ftp disabled={ftp}\n')
        file1.write(f'/ip service set www disabled={www}\n')
        file1.write(f'/ip service set api disabled={api}\n')
        file1.write(f'/ip service set api-ssl disabled={apissl}\n')
        file1.write(f'/ip service set ssh disabled={ssh}\n')
        file1.write(f'/ip service set winbox disabled={winbox}\n')
        file1.write(f'/ip service set www-ssl disabled={wwwssl}\n')

        file1.close()