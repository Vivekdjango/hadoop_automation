#!/usr/bin/python
print "Content-Type: text/html"
print ""
from bs4 import BeautifulSoup
import subprocess
import urllib2
import csv
import cgi, cgitb
cgitb.enable()

URL = 'http://gsmon.grid.lhr1.inmobi.com/pipeline.status.html'
s = urllib2.urlopen(URL)
test = s.read()
soup = BeautifulSoup(test,"lxml")
data = soup.find('pre')
new = data.get_text()
lines = new.splitlines()
for line in csv.reader(lines, skipinitialspace=True):
		for a in line:
			new = a.split('/')
       		    	print new[0],new[1],new[3]
