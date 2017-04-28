#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jrcconversion -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -d -c uj1;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jrcconversion -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c uj1 -r')


Colo3="UJ1"

print '<h3><u>%s</u></h3>'%Colo3

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')

