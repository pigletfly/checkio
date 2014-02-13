#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
def report_hook(count, block_size, total_size):

    """

    @count:        已经下载的数据块

    @block_size:    数据块大小

    @total_size:    文件大小

    """
    print ('%0f%%' %(100.0 * count * block_size/ total_size))

url = 'http://www.sina.com.cn'
local = 'sina.html'
urllib.urlretrieve(url, local, report_hook)