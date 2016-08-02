########################################################################
# IMPORTS
########################################################################

import sys
import datetime
import subprocess

########################################################################
# Global variables
########################################################################

tags = sys.argv[1]
min_date = datetime.datetime.strptime(sys.argv[2], '%d-%m-%Y')
max_date = datetime.datetime.strptime(sys.argv[3], '%d-%m-%Y')

########################################################################
# Main Run
########################################################################
sp = []

for i in range(0,(max_date - min_date).days):
	date_min = (min_date + datetime.timedelta(days=i)).strftime("%d-%m-%Y")
	date_max = (min_date + datetime.timedelta(days=i+1)).strftime("%d-%m-%Y")
	cmd_line = "python -c \"import getphotos; getphotos.get_biased_photos(\'{arg1}\',\'{arg2}\',\'{arg3}\')\"".format(arg1=tags,arg2=date_min,arg3=date_max)
	print cmd_line
	p = subprocess.Popen(cmd_line, shell=True)
	sp.append(p)

exit_codes = [p.wait() for p in sp]
x=0
for exit_code in exit_codes:
	x=x+1
	print "Procccess " ,x," finished with exit code: " ,exit_code

########################################################################
