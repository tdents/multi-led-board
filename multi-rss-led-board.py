#!/usr/bin/python
import time
import threading
from lxml import etree
from urllib import urlopen
from subprocess import Popen, PIPE

def on(devpath):
	devicepowerlevel=devpath + "/power/level"
	file = open(devicepowerlevel, "w")
	file.write("on")
	file.close()

def off(devpath):
	devicepowerlevel=devpath + "/power/level"
	file = open(devicepowerlevel, "w")
	file.write("auto")
	file.close()

def ledwhile():
		print 'Thread started'
		light = 1
		delay = 1
		global state;
		while not exitapp:
			print state[1],state[2]
			if state[1] == 1:
				on(ch1devpath)
			if state[2] == 1:
				on(ch2devpath)
			if state[3] == 1:
				on(ch3devpath)
			if state[4] == 1:
				on(ch4devpath)
			time.sleep(light)
                        if state[1] == 1:
                                off(ch1devpath)
                        if state[2] == 1:
                                off(ch2devpath)
                        if state[3] == 1:
                                off(ch3devpath)
                        if state[4] == 1:
                                off(ch4devpath)
			time.sleep(delay)
			
def chkRSS(service,url):
    count = 0
    context = etree.iterparse(urlopen(url))
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        if elem.tag == "title":
		if text != service:
	    		print elem.tag + " => " + text
			count += 1
    return count

def chkState():
	global state
	if chkRSS('ServiceMalware','http://cerberus.intr/index.php/rss/87c0eaf68eba52a2fdfb0d98ce0ef016') > 0:
		print 'Malware LED ON'
		state[malwarech] = 1
	else:
		print 'Malware LED OFF'
		state[malwarech] = 0
		off(ch2devpath)


	if chkRSS('ServiceRebootRequest','http://cerberus.intr/index.php/rss/d9420f78bf2ce4ebe46b511f1f80cc6d') > 0:
		print 'Reboot request LED ON'
		state[rebootch] = 1
	else:
		print 'Reboot request LED OFF'
		state[rebootch] = 0
		off(ch1devpath)
	state[2] = 0
	state[3] = 0

#Config 4 channel version (hard values)
ch1dev = '09da:0006'
ch2dev = '09da:0006'
ch3dev = '09da:0006'
ch4dev = '09da:0006'
#Channel bind
#event = channel_number
#Ex: rebootrequest = 1
rebootch = 1
malwarech = 2

#Don't touch
exitapp = False

ch1ids = ch1dev.split(":")
ch2ids = ch2dev.split(":")
ch3ids = ch3dev.split(":")
ch4ids = ch4dev.split(":")
    
out, err = Popen('udevadm trigger -v -a idVendor='+ch1ids[0]+' -a idProduct=' + ch1ids[1] + '', shell=True, stdout=PIPE).communicate()
ch1devpath = str(out)
ch1devpath = ch1devpath.rstrip('\n')
out, err = Popen('udevadm trigger -v -a idVendor='+ch2ids[0]+' -a idProduct=' + ch2ids[1] + '', shell=True, stdout=PIPE).communicate()
ch2devpath = str(out)
ch2devpath = ch2devpath.rstrip('\n')
out, err = Popen('udevadm trigger -v -a idVendor='+ch3ids[0]+' -a idProduct=' + ch3ids[1] + '', shell=True, stdout=PIPE).communicate()
ch3devpath = str(out)
ch3devpath = ch3devpath.rstrip('\n')
out, err = Popen('udevadm trigger -v -a idVendor='+ch4ids[0]+' -a idProduct=' + ch4ids[1] + '', shell=True, stdout=PIPE).communicate()
ch4devpath = str(out)
ch4devpath = ch4devpath.rstrip('\n')

global state
state = [1,2,3,4,5]
state[1] = 0
state[2] = 0
state[3] = 0
state[4] = 0

t1 = threading.Thread(target=ledwhile)
t1.start()

while 1:
	chkState()
	time.sleep(30)
