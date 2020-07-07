/system script
add comment=script-tsit-update-routeros dont-require-permissions=no name=\
    script-tsit-update-routeros owner=admin-tsit policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    system package update check-for-updates\r\
    \n/system package update install"