import time

#router_ip_address = 123
#router_username = 123
#router_password = 123

def basicinfo(router_ip_address):
    router_ip_address = '192.168.2.2' #input("Enter Router IP Address: ")
    router_username = 'admin' #input("Enter Router Router username")
    router_password = 'Tcft65rdx' #("Enter router password")


    print(f"""router info
    {router_ip_address}
    {router_username}
    {router_password}
    """)
    time.sleep(2)

    return router_ip_address
    return router_username
    return router_password


basicinfo(router_ip_address)
