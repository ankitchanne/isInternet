import urllib2, os, time, webbrowser

def checkConn():
	try:
		response = urllib2.urlopen('http://www.google.com')
		return True
	except urllib2.URLError, e:
		return False
while(checkConn() is False):
	checkConn()

webbrowser.get().open('file://'+os.path.realpath('play_ping.html'))
