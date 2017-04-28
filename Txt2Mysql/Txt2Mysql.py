# -*- coding:utf-8 -*-

import MySQLdb
import configparser
import os
import sys

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

dbc = configparser.ConfigParser()
dbc.read(PATH('db.ini'))
conn = MySQLdb.connect(host=dbc.get("db", 'db_host'), user=dbc.get("db", 'db_user'), passwd=dbc.get("db", 'db_pass'), db=dbc.get("db", 'db_database'), port=int(dbc.get("db", 'db_port')), charset='utf8')
cur = conn.cursor(MySQLdb.cursors.DictCursor)

with open(PATH('keywords.txt')) as f:
    lines = f.readlines()
    for l in lines:
        key = l.strip()
        # remove repeated record
        cur.execute("SELECT count(*) as count FROM `iqilu_keywords` WHERE `keyword`='%s'" % key)
        count = cur.fetchone()['count']
        if not count:
            print "INSERT %s" % key
            cur.execute("INSERT INTO `iqilu_keywords` (`id`, `catid`, `keyword`) VALUES (NULL, 1, '%s');" % key)

conn.commit()
cur.close()
conn.close()
