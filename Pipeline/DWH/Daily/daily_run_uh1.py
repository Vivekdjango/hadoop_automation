#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s killed,failed,timedout,suspended -f /usr/local/data-dwh-deployment/monitor/dwh.monitor.properties -b 48 -t 15 -c uh1 -p dwh -j daily -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s killed,failed,timedout,suspended -f /usr/local/data-dwh-deployment/monitor/dwh.monitor.properties -b 48 -t 15 -c uh1 -p dwh -j daily -r')

Colo2="Krypton"

print '<h3><u>%s</u></h3>'%Colo2

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
