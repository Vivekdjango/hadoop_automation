#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
<host>', username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/mkhoj/ops/lib/nrpe/check_s3_feeds.py|grep MISSING')

print "GOLD-BOX"

for l in stdout :
    print l.strip() + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
<host>', username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/mkhoj/ops/lib/nrpe/check_s3_feeds.py|grep MISSING')

print "Krypton"

for l in stdout :
    print l.strip() + '<br />'

for l in stderr:
    print l.strip()

ssh.close();
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
<host>', username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/mkhoj/ops/lib/nrpe/check_s3_feeds.py|grep MISSING')

print "UJ1"

for l in stdout :
    print l.strip() + '<br />'

for l in stderr:
    print l.strip()

ssh.close();

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
<host>', username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/mkhoj/ops/lib/nrpe/check_s3_feeds.py|grep MISSING')

print "LHR1"

for l in stdout :
    print l.strip() + '<br />'

for l in stderr:
    print l.strip()

ssh.close();

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
<host>', username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('/opt/mkhoj/ops/lib/nrpe/check_s3_feeds.py|grep MISSING')

print "HKG1"

for l in stdout :
    print l.strip() + '<br />'

for l in stderr:
    print l.strip()

ssh.close()

