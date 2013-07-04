#!/usr/bin/python
# -*- coding: utf-8 -*-
def checkio(data):
	a,b = data
	return bin(a^b).count('1')

if __name__ == "__main__":

	print checkio([117, 17])
	print checkio([1, 2]) 
	print checkio([16, 15]) 