#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import paramiko
import cgi, cgitb
form = cgi.FieldStorage() 
oozie_value = form.getvalue('oozie_value')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh.connect(<host>, username='<username>', password='<password>')

stdin, stdout, stderr = ssh.exec_command('source /etc/grid.aliases;oozie job -info %s'%oozie_value)

print "Krypton-BOX"

for l in stdout :
    print l.strip() + '<br />'

for l in stderr:
    print l.strip()

ssh.close();

