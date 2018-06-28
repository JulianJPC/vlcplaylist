#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import shutil
import re
import os
import urllib2

varText = raw_input("Introducir nombre lista vlc: ") 	#Name of vlc playlist

texto = open(varText, "r")          
regex = re.compile(r'(\/home.*)</location>')			#only works linux

for line in texto:
	link= regex.findall(line)
	for text in link:
		text = urllib2.unquote(text)
		text = str.replace(text, "&#39;", "'")
		text = str.replace(text, "&amp;", "&")
		shutil.copy(text, os.path.dirname(os.path.realpath(__file__)))  #Place the files in the same directory of this file