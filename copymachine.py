#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import shutil
import re
import urllib2

texto = open("Clasicos.xspf", "r")          #Name of vlc playlist
regex = re.compile(r'(\/home.*)</location>')

for line in texto:
	link= regex.findall(line)
	for text in link:
		text = urllib2.unquote(text)
		text = str.replace(text, "&#39;", "'")
		text = str.replace(text, "&amp;", "&")
		shutil.copy(text, "/home/lauchalunar/besttest")  #Place to put music files