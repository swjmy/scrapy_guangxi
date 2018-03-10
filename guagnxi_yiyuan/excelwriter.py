# encoding: utf-8
import xlsxwriter,xlrd
import sys,os.path
from datetime import datetime
from datetime import timedelta
import time
import json,re,os

from guagnxi_yiyuan.items import GuagnxiYiyuanItem

# reload(sys)
# sys.setdefaultencoding('utf-8')

class WorkBook():
    pass

def writeItems(self, items):
    print("write...")
    excel_name = "F:\\home\\workspace\\scrap_guangxi\\data\\guangxi.xlsx"
    workbook = xlsxwriter.Workbook(excel_name)  # 创建一个excel文件
    worksheet = workbook.add_worksheet()  # 创建一个工作表对象
    worksheet.set_column(0, 60, 22)  # 设定列的宽度为22像素
    # border：边框，align:对齐方式，bg_color：背景颜色，font_size：字体大小，bold：字体加粗
    top = workbook.add_format({'border': 1, 'align': 'center', 'bg_color': 'cccccc', 'font_size': 13, 'bold': True})
    green = workbook.add_format({'border': 1, 'align': 'center', 'bg_color': 'green', 'font_size': 12})
    yellow = workbook.add_format({'border': 1, 'bg_color': 'yellow', 'font_size': 12})
    red = workbook.add_format({'border': 1, 'align': 'center', 'bg_color': 'red', 'font_size': 12})
    blank = workbook.add_format({'border': 1})

    n = 0
    for item in items:
        i = 1
        for value in item.field_list:

            worksheet.write(n, i, value, blank)
            i += 1
        n += 1

    self.workbook.close()