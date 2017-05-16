# -*- coding:utf-8 -*-

import MySQLdb
import configparser
import os
import xlrd
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

# connect database
dbc = configparser.ConfigParser()
dbc.read(PATH('../db.ini'))
conn = MySQLdb.connect(host=dbc.get("db", 'db_host'), user=dbc.get("db", 'db_user'), passwd=dbc.get("db", 'db_pass'), db=dbc.get("db", 'db_database'), port=int(dbc.get("db", 'db_port')), charset='utf8')
cur = conn.cursor(MySQLdb.cursors.DictCursor)

# read xls file
work_book = xlrd.open_workbook(filename=PATH('wechat.xls'))
sheets = work_book.sheets()
for sheet in sheets:
    for row in range(sheet.nrows):
        values = []
        for col in range(sheet.ncols):
            value = sheet.cell(row, col).value
            value = str(int(value)) if isinstance(value, float) or isinstance(value, int) else value
            values.append(value)
        # remove repeated record
        wechatname = values[1]
        cur.execute("SELECT count(*) as count FROM `iqilu_wechat` WHERE `wechatname`='%s'" % wechatname)
        count = cur.fetchone()['count']
        if not count:
            print "INSERT %s" % values[0]
            cur.execute("INSERT INTO `iqilu_wechat` (`wid`, `wechat`, `wechatname`, `catid`, `status`) "
                        "VALUES (NULL, '%s', '%s', '%s', '%s');" % tuple(values))

conn.commit()
cur.close()
conn.close()
