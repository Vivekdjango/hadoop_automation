#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s killed,failed,timedout,suspended    -f /usr/local/data-perf-ci-deployment/monitor/perfci.monitor.properties -b 48 -t 15 -c uj1 -p perfci -j hourly   -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s killed,failed,timedout,suspended    -f /usr/local/data-perf-ci-deployment/monitor/perfci.monitor.properties -b 48 -t 15 -c uj1 -p perfci -j hourly   -r'

Colo3="UJ1"


print '<h3><u>%s</u></h3>'%Colo3

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
