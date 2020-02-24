#!/usr/bin/python3

# encoding = utf-8

import requests as req
import NewGuShi.NewFile as nfile # 调用文件操作工具
import os
url = "https://so.gushiwen.org/guwen/book_46653FD803893E4FB25B762406C1F882.aspx"
gus = req.get(url)
content = gus.text
bookname = content[content.find("<title>")+7:content.find("</title>")].strip() # 获取书本名称并去除空格
# nfile.mkdir("/home/ihpd/"+bookname) # 创建文件夹 并以书本名称命名
content = content[content.find("bookcont"):] #获取书本列表

a = 1
name = content[content.find("/guwen/bookv"):content.find("</a>")] # 获取书本第一篇张的字符串

'''
while a==1:
    if content.find(name):

        name = name[name.find('.aspx') + 7:] #获取篇幅标题 4
        href = content[content.find("/guwen/bookv"):] # 获取篇幅链接信息 5
        href = href[:href.find(".aspx")+5] #获取篇幅连接 6
        #使用带参数的方法 传入 name 和 href 写入文件
        print(name)
        print(href)
        content = content[content.find(name):] # 删除已获取的篇幅信息 1
        name = content[content.find("/guwen/bookv"):] # 找到下一篇幅的信息 2
        name = name[:name.find('</a>')] # 截取篇幅标题信息 3
    else:
        break 

'''
