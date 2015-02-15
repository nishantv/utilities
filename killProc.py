"""
script to kill gyachi and/or other processes
usage: python killproc.py <optional arguments>
The optional arguments are process names delimited by spaces
If no arguments are given, gyachi will be killed
"""

import sys, platform
from subprocess import call  



def killProcWin(process = "gyachi"):
	for process in sys.argv[1:]:
		call("taskkill /IM %s.exe /F"%process, shell=True)  
		#print "Killed %s"%process
	

def main():
#	print len(sys.argv)
	if len(sys.argv) > 1:
		if platform.system() == 'Windows':
			print '\nDetected platform %s %s\n'%(platform.system(), \
			platform.release())
			killProcWin(sys.argv)



if __name__ == "__main__":
	main()
