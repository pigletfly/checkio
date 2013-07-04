#!/usr/bin/python
# -*- coding: utf-8 -*-
def checkio(data):
	return [i for i in data if data.count(i)>=2]



if __name__ == "__main__":
	print checkio([1, 2, 3, 1, 3]) 
	print checkio([1, 2, 3, 4, 5]) 
	print checkio([5, 5, 5, 5, 5])
	print checkio([10, 9, 10, 10, 9, 8])