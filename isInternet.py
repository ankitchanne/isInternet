import urllib2
import os
import time
def checkConn():
	try:
		response = urllib2.urlopen('http://www.google.com')
		return True
	except urllib2.URLError, e:
		return False
while(checkConn() is False):
	checkConn()

print 'Connected'
os.system('start ping.wav')
time.sleep(3)
os.system('TASKKILL /IM wmplayer.exe')	