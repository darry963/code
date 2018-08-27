#!/usr/bin/env python
#-*- coding:utf-8 -*-

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()#待爬取库集合，二次去重
        self.old_urls = set()#已爬取库

#一次去重，加入待爬取url库
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
#单条提取url，等待加入待爬取url库
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

#判断待爬取url库中有无数据
    def has_new_url(self):
        return len(self.new_urls) != 0

#提取未爬取url，并返回
    def get_new_url(self):
        new_url = self.new_urls.pop()
        '''取出一个未爬取url，并删除未爬取库中原数据,赋值给new_url'''
        self.old_urls.add(new_url)#将取出new_url加入到已爬取库中
        return new_url