#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect('opgw4001.grid.hkg1.inmobi.com', username='vivek.sinha', password='Password@123')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p dimstore -f /opt/gridscripts/ivory/pipeline-properties/dimstore_pipelines.properties -b 24 -t40 -s KILLED,FAILED,TIMEDOUT -c hkg1 -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p dimstore -f /opt/gridscripts/ivory/pipeline-properties/dimstore_pipelines.properties -b 24 -t40 -s KILLED,FAILED,TIMEDOUT -c hkg1 -r')

Colo5="HKG1"

print '<h3><u>%s</u></h3>'%Colo5

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close()

