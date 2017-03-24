# -*- coding: UTF-8 -*-

import xlrd
import os
import json
import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf8')

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

def read_xlsx(xlsx_path):
    workbook = xlrd.open_workbook(xlsx_path)
    sheets = workbook.sheets()

    map_sheet = {}
    for sheet in sheets:
        list_keys = []
        list_row = []
        for i in range(sheet.nrows):
            if i is 0:
                for col in range(sheet.ncols):
                    cell = sheet.cell(i, col)
                    value = cell.value
                    list_keys.append(value)
            else:
                map_value = {}
                for col in range(sheet.ncols):
                    cell = sheet.cell(i, col)
                    value = cell.value
                    map_value[list_keys[col]] = int(value) if isinstance(value, float) else value
                list_row.append(map_value)
        map_sheet[sheet.name] = list_row

    json_path = "".join((os.path.splitext(xlsx_path)[0], ".json"))
    with open(json_path, "w") as fp:
        json.dump(map_sheet, fp, ensure_ascii=False)

        
now_date = datetime.date.today()
yesterday = now_date - datetime.timedelta(days=1)
year = now_date.strftime("%Y")

xlsx_path = PATH("2017-03-22.xlsx")
read_xlsx(xlsx_path)

