f1 = open('DPBase_run.py~', 'r')
f2 = open('DPBase_run.py~', 'w')
for line in f1:
    f2.write(line.replace('print l.strip()', 'print l.strip() + <br />'))
f1.close()
f2.close()
