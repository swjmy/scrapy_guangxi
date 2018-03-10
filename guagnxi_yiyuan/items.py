# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuagnxiYiyuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field() #url

    name = scrapy.Field() #医院名称
    area = scrapy.Field() #所在地区
    director = scrapy.Field() #院长姓名
    year_founded = scrapy.Field() #建院年份
    nature = scrapy.Field() #医院性质
    level = scrapy.Field() #医院等级
    contact_number = scrapy.Field() #联系电话
    contact_address = scrapy.Field() #联系地址
    department_number = scrapy.Field()#科室数量
    medical_staff = scrapy.Field()#医护人员
    beds = scrapy.Field()#临床数量
    year_quantity = scrapy.Field()#年门诊量
    is_medicare = scrapy.Field()#是否医保
    advanced_equipment = scrapy.Field()#先进设备
    about = scrapy.Field()#医院简介
    award = scrapy.Field()#所获荣誉
    field_list = []

    pass
