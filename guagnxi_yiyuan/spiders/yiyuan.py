# !/usr/bin/env python
# -*- coding:utf-8 -*-
import os,re
import urllib.request

import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector

from guagnxi_yiyuan.items import GuagnxiYiyuanItem


class YiyuanSpider(scrapy.Spider):
    name = "yiyuan"
    # allowed_domains = ["yyk.99.com.cn"]
    # start_urls = [
    #     "http://yyk.99.com.cn/guangxi/",
    # ]

    def __init__(self):
        # 图片链接server域名
        #self.server_img = 'http://n.1whour.com/'
        # 章节链接server域名
        #self.server_link = 'http://comic.kukudm.com'
        self.allowed_domains = ['yyk.99.com.cn']
        self.start_urls = ['http://yyk.99.com.cn/guangxi/']
        #self.start_urls = ['http://yyk.99.com.cn/chengzhong/71714/jianjie.html']
        # 匹配图片地址的正则表达式
        #self.pattern_img = re.compile(r'\+"(.+)\'><span')

    # 从start_requests发送请求
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse1)

    # 获取所有医院
    def parse1(self, response):
        #print(response.xpath('//div[@class="tablist"]/ul/li/a[1]/@href').extract())
        #print(response.xpath('//div[@class="tablist"]/ul/li/a[1]/@title').extract())
        urls = response.xpath('//div[@class="tablist"]/ul/li/a[1]/@href').extract()
        for url in urls:
            #print(url)
            url_jianjie = url + "jianjie.html"
            yield scrapy.Request(url=url_jianjie, callback=self.parse__jianjie)


    #解析医院的详细信息
    def parse__jianjie(self, response):
        # 医院名称
        "/html/body/div[5]/div[3]/div[1]/div[2]/div[2]/ul/li[1]/span"
        name = response.xpath('normalize-space(/html/body/div[5]/div[3]/div[1]/div[2]/div[2]/ul/li[1]/span/text())').extract()
        # 所在地区
        "/html/body/div[5]/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a/u"
        area = response.xpath('normalize-space(/html/body/div[5]/div[3]/div[2]/div[2]/table/tr[1]/td[4]/a/u/text())').extract()
        # 院长姓名
        director = response.xpath('normalize-space(//div[@class="leftpad10 hpbasicinfo"]/table/tr[2]/td[2]/text())').extract()
        # 建院年份
        year_founded = response.xpath('normalize-space(//div[@class="leftpad10 hpbasicinfo"]/table/tr[2]/td[4]/text())').extract()
        # 医院类型
        nature = response.xpath('normalize-space(//div[@class="leftpad10 hpbasicinfo"]/table/tr[2]/td[6]/text())').extract()
        # 医院等级
        level = response.xpath('normalize-space(//div[@class="leftpad10 hpbasicinfo"]/table/tr[3]/td[2]/text())').extract()
        #联系电话
        "/html/body/div[5]/div[3]/div[1]/div[2]/div[2]/ul/li[4]/span[1]"
        contact_number = response.xpath('normalize-space(/html/body/div[5]/div[3]/div[1]/div[2]/div[2]/ul/li[4]/span[1]/text())').extract()
        # 联系地址
        "/html/body/div[5]/div[3]/div[1]/div[2]/div[2]/ul/li[5]/span"
        contact_address = response.xpath('normalize-space(/html/body/div[5]/div[3]/div[1]/div[2]/div[2]/ul/li[5]/span/text())').extract()
        # 科室数量
        department_number = response.xpath('normalize-space(//div[@class="leftpad10 hpbasicinfo"]/table/tr[3]/td[4]/a/u/text())').extract()
        # 医护人员
        medical_staff = response.xpath('normalize-space(//div[@class="leftpad10 hpbasicinfo"]/table/tr[3]/td[6]/a/u/text())').extract()
        # 临床数量
        beds = response.xpath('normalize-space(//div[@class="leftpad10 hpbasicinfo"]/table/tr[4]/td[2]/text())').extract()
        # 年门诊量
        year_quantity = response.xpath('normalize-space(//div[@class="leftpad10 hpbasicinfo"]/table/tr[4]/td[4]/text())').extract()
        # 是否医保
        is_medicare = response.xpath('normalize-space(//div[@class="leftpad10 hpbasicinfo"]/table/tr[4]/td[6]/text())').extract()
        # 先进设备
        advanced_equipment = response.xpath('normalize-space(//div[@class="mainleft"]/div[3]/div[@class="hpcontent"]/text())').extract()
        # 先进设备
        "/html/body/div[5]/div[3]/div[3]/div[2]/p[1]"
        advanced_equipment_ps = response.xpath('normalize-space(//div[@class="mainleft"]/div[3]/div[@class="hpcontent"]/p/text())').extract()
        for p in advanced_equipment_ps:
            advanced_equipment += p
        # 医院简介
        about_content = response.xpath('normalize-space(//div[@class="mainleft"]/div[4]/div[@class="hpcontent"]/text())').extract()
        about_ps = response.xpath('normalize-space(//div[@class="mainleft"]/div[4]/div[@class="hpcontent"]/p/text())').extract()
        for p in about_ps:
            about_content += p

        # 所获荣誉
        "/html/body/div[5]/div[3]/div[5]/div[2]"
        award = response.xpath('normalize-space(/html/body/div[5]/div[3]/div[5]/div[2]/text())').extract()

        item = GuagnxiYiyuanItem()
        #踩了这个坑，item在scrapy框架里是单例，所以上一次的结果还留在field_list里。
        item.field_list.clear()
        item['url'] = response.url
        #item.field_list.append(response.url)
        item['name'] = name
        item.field_list.append(name)
        item['area'] = area
        item.field_list.append(area)
        item['director'] = director
        item.field_list.append(director)
        item['year_founded'] = year_founded
        item.field_list.append(year_founded)
        item['nature'] = nature
        item.field_list.append(nature)
        item['level'] = level
        item.field_list.append(level)
        item['contact_number'] = contact_number
        item.field_list.append(contact_number)
        item['contact_address'] = contact_address
        item.field_list.append(contact_address)
        item['department_number'] = department_number
        item.field_list.append(department_number)
        item['medical_staff'] = medical_staff
        item.field_list.append(medical_staff)
        item['beds'] = beds
        item.field_list.append(beds)
        item['year_quantity'] = year_quantity
        item.field_list.append(year_quantity)
        item['is_medicare'] = is_medicare
        item.field_list.append(is_medicare)
        item['advanced_equipment'] = advanced_equipment
        item.field_list.append(advanced_equipment)
        item['about'] = about_content
        item.field_list.append(about_content)
        item['award'] = award
        item.field_list.append(award)


        yield item
