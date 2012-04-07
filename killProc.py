"""
script to kill gyachi and/or other processes
usage: python killproc.py <optional arguments>
The optional arguments are process names delimited by spaces
If no arguments are given, gyachi will be killed
"""

import sys
from subprocess import call  

def killProc(process = "gyachi"):
	call("pkill %s"%process, shell=True)  
	print "Killed %s"%process

def main():
#	print len(sys.argv)
	if len(sys.argv) > 1:
		for process in sys.argv[1:]:
			killProc(process)
	else:
		killProc()

if __name__ == "__main__":
	main()
