import rb2011basicinfo
import rb2011createfile
import Rb2011IpServices
import rb2011ssh

rb2011basicinfo.basicinfo()

rb2011createfile.createfile(123)

print(rb2011createfile.filename)

Rb2011IpServices.IpServices(rb2011createfile.filename)

rb2011ssh.ssh(router_ip_address,router_username,router_password,file)