#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -f /opt/gridscripts/ivory/pipeline-properties/rtbi.properties -p rtbi -b 6 -t40 -s KILLED,FAILED,TIMEDOUT -c uh1 -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -f /opt/gridscripts/ivory/pipeline-properties/rtbi.properties -p rtbi -b 6 -t40 -s KILLED,FAILED,TIMEDOUT -c uh1 -r')

Colo2="Krypton"

print '<h3><u>%s</u></h3>'%Colo2

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
