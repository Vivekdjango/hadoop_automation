#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s killed,failed,timedout,suspended    -f /opt/gridscripts/ivory/localdc/conf/lda_pipelines.properties -b 48 -t 15 -c lhr1 -p lda -j replication -k richmedia,download  -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s killed,failed,timedout,suspended    -f /opt/gridscripts/ivory/localdc/conf/lda_pipelines.properties -b 48 -t 15 -c lhr1 -p lda -j replication -k richmedia,download -r')

Colo4="LHR1"


print '<h3><u>%s</u></h3>'%Colo4

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
