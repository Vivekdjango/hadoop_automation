#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s killed,failed,timedout,suspended    -f /opt/gridscripts/ivory/localdc/conf/lda_pipelines.properties -b 48 -t 15 -c hkg1 -p yoda -j summary,inventory,rm -k hourly -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s killed,failed,timedout,suspended    -f /opt/gridscripts/ivory/localdc/conf/lda_pipelines.properties -b 48 -t 15 -c hkg1 -p yoda -j summary,inventory,rm -k hourly -r')

Colo5="HKG1"

print '<h3><u>%s</u></h3>'%Colo5

for l in stdout :
    print l.strip()

for l in stderr:
    print l.strip()

ssh.close()

