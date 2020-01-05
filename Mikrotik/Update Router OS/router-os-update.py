def file_to_write():

    filename = input("please enter the name of the file you would like to write to")
    filename = filename + '.txt'

    print(f"Full file name is: {filename}")

    file1 = open(file, 'a')

    file1.write(f'/ip pool add name="{dhcp_pool_name}" ranges={dhcp_pool_ip_address_range} comment="{dhcp_pool_comment}" \n')

    file1.write(f'/ systemscheduler')


    file1.write(f'add interval = 30d00: 00:00name = "Package upgrade" on - event = \')
    file1.write(f'"system package update install" policy = \')
    file1.write(f'ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon \')
    file1.write(f'start - time = 12:00: 00')

    file1.close()

    


