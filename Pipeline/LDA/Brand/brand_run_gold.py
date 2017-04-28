#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/data-brand-ci-deployment/monitor/brandci.monitor.properties -b 48 -t 240 -c gold -p brandci -j hourly   -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/data-brand-ci-deployment/monitor/brandci.monitor.properties -b 48 -t 240 -c gold -p brandci -j hourly   -r')

Colo1="GOLD-BOX"


print '<h3><u>%s</u></h3>'%Colo1

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
