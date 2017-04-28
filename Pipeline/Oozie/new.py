#!/usr/bin/python
#Vivek Sinha
print "Content-Type: text/html"
print

import urllib2
import paramiko
import cgi, cgitb
from bs4 import BeautifulSoup
form = cgi.FieldStorage() 
Username = form.getvalue('Username')
Password = form.getvalue('Password')

html = open("/var/www/html/noc_final/index.html",'r')
s = html.read()
header = "Content-Type: text/html; charset=UTF-8\n\n"
output = header + s.format
print (output)













#s = urllib2.Request('http://localhost/noc_final/index.html')
#r = urllib2.urlopen(s)

print r

#url = '/var/www/html/noc_final/index.html'
#url = 'https://www.hotstar.com'
#s = urllib.urlopen(url)
#test = s.read()
#soup = BeautifulSoup(test)

#print soup







#print "Location:http://localhost/noc_final/index.html\r\n"

#URL = 'http://localhost/noc_final/index.html'

#s = open(URL)
#print s

#f = open('/var/www/html/noc_final/index.html', 'r')
#myhtml = f.read()
#f.close()
#print myhtml




#"<div id="main"> <?php include '/var/www/html/noc_final/index.html';?> </div>"

#print """
#<form method="post" action="/var/www/html/noc_final/index.html" style="padding-top:5px; margin-top:5px">
      
#<div class="login_boxed style=width: 40px;margin-left: 13px;height: 30px">

#</form>

#"""
