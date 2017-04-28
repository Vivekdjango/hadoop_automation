#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 90 -c gold -p lda -j enhancer,promoter   -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 90 -c gold -p lda -j enhancer,promoter   -r')

Colo1="GOLD-BOX"


print '<h3><u>%s</u></h3>'%Colo1

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 90 -c uh1 -p lda -j enhancer,promoter   -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 90 -c uh1 -p lda -j enhancer,promoter   -r')

Colo2="Krypton"


print '<h3><u>%s</u></h3>'%Colo2

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 90 -c uj1 -p lda -j enhancer,promoter   -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 90 -c uj1 -p lda -j enhancer,promoter   -r')

Colo3="UJ1"


print '<h3><u>%s</u></h3>'%Colo3

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
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
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 90 -c hkg1 -p lda -j enhancer,promoter   -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -q -s running    -f /usr/local/grid_lda_deploy/monitor/lda.monitor.properties -b 25 -t 90 -c hkg1 -p lda -j enhancer,promoter   -r')

Colo5="HKG1"


print '<h3><u>%s</u></h3>'%Colo5

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close()

