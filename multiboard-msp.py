#!/usr/bin/python
# coding=utf8
import time
import threading
from lxml import etree
from urllib import urlopen
from subprocess import Popen, PIPE

def sendcmd(channel,state):
	device="/dev/led-monitor"
	file = open(device, "w")
	command=str(channel) + ',' + str(state) + '\n'
	file.write(command)
	file.close()

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

rebootch = 2
vdserrorch = 3

def chkState():
	global state
#	if chkRSS('ServiceMalware','http://cerberus.intr/index.php/rss/87c0eaf68eba52a2fdfb0d98ce0ef016') > 0:
#		print 'Malware LED ON'
#		state[malwarech] = 1
#	else:
#		print 'Malware LED OFF'
#		state[malwarech] = 0
#		off(ch2devpath)


	if chkRSS('ServiceRebootRequest','http://cerberus.intr/index.php/rss/d9420f78bf2ce4ebe46b511f1f80cc6d') > 0:
		print 'Запрошена перезагрузка из панели'
		sendcmd(rebootch,1)
	else:
		print 'Запросов на перезагрузку нет'
		sendcmd(rebootch,0)

        if chkRSS('ServiceVDSErrors','http://cerberus.intr/index.php/rss/2bc47a20c129e7b67fd954bae20178ac') > 0:
                print 'Обнаружена ошибка в ходе выполнения задачи'
		sendcmd(vdserrorch,1)
        else:
                print 'Ошибок не обнаружено'
		sendcmd(vdserrorch,0)

while 1:
	print time.strftime("%H:%M:%S") + '-----------------------------'
	chkState()
	print '-------------------------------------'
	time.sleep(30)
