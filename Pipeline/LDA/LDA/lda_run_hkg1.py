#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s killed,failed,timedout,suspended    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 15 -c hkg1 -p lda -j minutely,rcconversion,enhancer,dpbase   -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s killed,failed,timedout,suspended    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 15 -c hkg1 -p lda -j minutely,rcconversion,enhancer,dpbase   -r')

Colo5="HKG1"


print '<h3><u>%s</u></h3>'%Colo5

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close()

