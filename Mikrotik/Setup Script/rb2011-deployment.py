import time
import rb2011basicinfo
#import rb2011createfile
#import Rb2011IpServices
#import rb2011ssh

router_ip_address = 123

rb2011basicinfo.basicinfo(router_ip_address)

print(f""" post basic info
{rb2011basicinfo.router_ip_address}
{rb2011basicinfo.router_username}
{rb2011basicinfo.router_password}""")
time.sleep(5)

#rb2011createfile.createfile(123)

#print(rb2011createfile.filename)

#Rb2011IpServices.IpServices(rb2011createfile.filename)

#print(f"""
#{rb2011basicinfo.router_ip_address}
#{rb2011basicinfo.router_username}
#{rb2011basicinfo.router_password}""")
#time.sleep(5)

#rb2011ssh.ssh(router_ip_address,router_username,router_password,file)