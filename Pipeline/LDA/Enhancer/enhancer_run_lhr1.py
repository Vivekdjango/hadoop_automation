#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 90 -c lhr1 -p lda -j enhancer,promoter   -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 90 -c lhr1 -p lda -j enhancer,promoter   -r')

Colo4="LHR1"


print '<h3><u>%s</u></h3>'%Colo4

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')