#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
def checkio(data):
	pattern = re.compile('\s+')
	return re.sub(pattern,' ',data) 

if __name__ == '__main__':
	print checkio('I  like       python')