#!/usr/bin/python
# -*- coding: utf-8 -*-
def checkio(data):
	data.sort()
	print data
	if len(data) %2 ==0:
		return (data[len(data)/2-1]+data[len(data) /2 ])/2.0
	else:
		return data[(len(data)+1)/2-1]


if __name__ == "__main__":
	print checkio([1, 2, 3, 4, 5])
	print checkio([3, 1, 2, 5, 3])
	print checkio([1, 300, 2, 200, 1]) 
	print checkio([3, 6, 20, 99, 10, 15]) 
