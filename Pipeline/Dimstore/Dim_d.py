#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect('glgw4006.grid.uh1.inmobi.com', username='vivek.sinha', password='Password@123')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p dimstore -f /opt/gridscripts/ivory/pipeline-properties/dimstore_pipelines.properties -b 24 -t40 -s KILLED,FAILED,TIMEDOUT -c gold -d')

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
ssh.connect('krgw4001.grid.uh1.inmobi.com', username='vivek.sinha', password='Password@123')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p dimstore -f /opt/gridscripts/ivory/pipeline-properties/dimstore_pipelines.properties -b 24 -t40 -s KILLED,FAILED,TIMEDOUT -c uh1 -d')

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
ssh.connect('tzgw4001.grid.uj1.inmobi.com', username='vivek.sinha', password='Password@123')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p dimstore -f /opt/gridscripts/ivory/pipeline-properties/dimstore_pipelines.properties -b 24 -t40 -s KILLED,FAILED,TIMEDOUT -c uj1 -d')

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
ssh.connect('ergw4001.grid.lhr1.inmobi.com', username='vivek.sinha', password='Password@123')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p dimstore -f /opt/gridscripts/ivory/pipeline-properties/dimstore_pipelines.properties -b 24 -t40 -s KILLED,FAILED,TIMEDOUT -c lhr1 -d')

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
ssh.connect('opgw4001.grid.hkg1.inmobi.com', username='vivek.sinha', password='Password@123')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p dimstore -f /opt/gridscripts/ivory/pipeline-properties/dimstore_pipelines.properties -b 24 -t40 -s KILLED,FAILED,TIMEDOUT -c hkg1 -d')

Colo5="HKG1"

print '<h3><u>%s</u></h3>'%Colo5

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close()

