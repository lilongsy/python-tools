#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 切分文件 '''

line_num = 10 #每个文件行数
file_name = "weixin.txt" #文件名

with open(file_name) as f:
    lines = f.readlines()
    i = 1 #当前行数
    j = 1 #文件名
    for l in lines:
        with open(str(j) + u".txt", 'a') as f1:
            if(i % (line_num + 1) == 0):
                f1.write(l.strip()) #去掉末尾换行符
                j += 1
            else:
                f1.write(l)
        i += 1
