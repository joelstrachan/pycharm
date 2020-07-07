/system script
add comment=script-tsit-update-firmware dont-require-permissions=no name=\
    script-tsit-update-firmware owner=admin-tsit policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="g\
    lobal Var1\r\
    \n:global Var2\r\
    \n:set Var1 \"\$[/system package get system version]\"\r\
    \n:set Var2 \"\$[/system routerboard get current-firmware]\"\r\
    \n:if (\$Var1>\$Var2) do={/system routerboard upgrade;\r\
    \n/system reboot;\r\
    \n}"