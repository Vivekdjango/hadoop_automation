#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jenhancer -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c gold -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jenhancer -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c gold -r')

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

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jenhancer -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c uh1 -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jenhancer -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c uh1 -r')

Colo2="Krypton"

print '<h3><u>%s</u></h3>'%Colo2

for l in stdout :
    print l.strip() = '<br />'

for l in stderr:
    print l.strip()

ssh.close();
print ('<br />')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jenhancer -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c uj1 -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jenhancer -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c uj1 -r')

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

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jenhancer -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c lhr1 -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jenhancer -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c lhr1 -r')

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

stdin, stdout, stderr = ssh.exec_command('/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jenhancer -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c hkg1 -d;/opt/gridscripts/gridopstools/bin/lda-monitor.sh -p cbp -jenhancer -b 12 -t15 -s KILLED,FAILED,TIMEDOUT -c hkg1 -r')

Colo5="HKG1"

print '<h3><u>%s</u></h3>'%Colo5

for l in stdout :
    print l.strip() + '<br />' + '<br />'

for l in stderr:
    print l.strip()

ssh.close()

