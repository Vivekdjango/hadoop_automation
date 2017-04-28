#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -f /opt/gridscripts/ivory/pipeline-properties/dcp_pipelines.properties -p dcp -b 72 -t60 -s KILLED,FAILED,TIMEDOUT -c gold -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -f /opt/gridscripts/ivory/pipeline-properties/dcp_pipelines.properties -p dcp -b 72 -t60 -s KILLED,FAILED,TIMEDOUT -c gold -r')

Colo1="GOLD-BOX"

print '<h3><u>%s</u></h3>'%Colo1

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
