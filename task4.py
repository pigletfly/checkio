#!/usr/bin/python
# -*- coding: utf-8 -*-
def checkio(data):
	balance,withdraw = data
	left = balance
	for draw in withdraw:
		if draw > balance:
			continue
		if draw % 5 !=0:
			continue
		left = balance - draw - 1
	return left


if __name__ == "__main_":
	print checkio([120, [10, 20, 30]]) 
	print checkio([120, [200, 10]]) 
	print checkio([120,[3, 10]]) 
	print checkio([120, [200 , 119]]) 
	print checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]])