# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlsxwriter


class GuagnxiYiyuanPipeline(object):

    row_n = 0
    items = []

    def process_item(self, item, spider):

        self.items.append(item.field_list.copy())
        #item['field_list'] = []
        self.row_n += 1
        print(self.row_n)
        print("item.field_list:",item.field_list.__len__())
        if self.row_n == 2222:
            #print("items:",self.items)
            self.writeItems(self.items)
        return item
        #print ("item:",item)
        #self.workbook.writeItem(item)
        #print ("url:",item['url'])
        #print("name:",item['name'],", area:",item['area'])


    def writeItems(self, items):
        print("write...")
        print("items.size:",items.__len__())
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

        worksheet.write(0, 0, "医院名称", blank)
        worksheet.write(0, 1, "所在地区", blank)
        worksheet.write(0, 2, "院长姓名", blank)
        worksheet.write(0, 3, "建院年份", blank)
        worksheet.write(0, 4, "医院类型", blank)
        worksheet.write(0, 5, "医院等级", blank)
        worksheet.write(0, 6, "联系电话", blank)
        worksheet.write(0, 7, "联系地址", blank)
        worksheet.write(0, 8, "科室数量", blank)
        worksheet.write(0, 9, "医护人员", blank)
        worksheet.write(0, 10, "临床数量", blank)
        worksheet.write(0, 11, "年门诊量", blank)
        worksheet.write(0, 12, "是否医保", blank)
        worksheet.write(0, 13, "先进设备", blank)
        worksheet.write(0, 14, "医院简介", blank)
        worksheet.write(0, 15, "所获荣誉", blank)


        n = 0
        for item in items:
            n += 1
            print("------n:",n,"------")
            i = 0
            for value in item:
                print("i:",i)
                #print(value)
                worksheet.write(n, i, value[0], blank)
                i += 1


        workbook.close()