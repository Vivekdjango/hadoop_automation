#!/usr/bin/python
#Vivek Sinha
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
soup = BeautifulSoup(test)
data = soup.find('pre')
lines = soup.pre.string.splitlines()
for line in csv.reader(lines, skipinitialspace=True):
        for a in line:
                new = a.split('/')
                k = new[1].split('_')
                if new[0]=='gold' and k[3]=='DP-RichMediaSummary':
                        subprocess.call('/var/www/cgi-bin/Rich_gold_d.py',shell='True')
                elif new[0]=='uh1' and k[3]=='DP-RichMediaSummary':
                        subprocess.call('/var/www/cgi-bin/Rich_uh1_d.py',shell='True')
                elif new[0]=='uj1' and k[3]=='DP-RichMediaSummary':
                        subprocess.call('/var/www/cgi-bin/Rich_uj1_d.py',shell='True')
                elif new[0]=='hkg1' and k[3]=='DP-RichMediaSummary':
                        subprocess.call('/var/www/cgi-bin/Rich_hkg1_d.py',shell='True')
                elif new[0]=='lhr1' and k[3]=='DP-RichMediaSummary':
                        subprocess.call('/var/www/cgi-bin/Rich_lhr1_d.py',shell='True')


