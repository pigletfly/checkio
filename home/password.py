#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
def checkio(data):
    if len(data) < 10:
    	return False
    else:
    	lower = upper = digit = False
    	for i in data:
    		if i in string.ascii_lowercase:
    			lower = True
    		if i in string.ascii_uppercase:
    			upper = True
    		if i in string.digits:
    			digit = True
    	return lower and upper and digit






if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
