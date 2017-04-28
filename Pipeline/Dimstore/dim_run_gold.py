#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect('glgw4006.grid.uh1.inmobi.com', username='vivek.sinha', password='Password@123')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p dimstore -f /opt/gridscripts/ivory/pipeline-properties/dimstore_pipelines.properties -b 24 -t40 -s KILLED,FAILED,TIMEDOUT -c gold -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p dimstore -f /opt/gridscripts/ivory/pipeline-properties/dimstore_pipelines.properties -b 24 -t40 -s KILLED,FAILED,TIMEDOUT -c gold -r')

Colo1="GOLD-BOX"

print '<h3><u>%s</u></h3>'%Colo1

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
