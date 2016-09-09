#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
@version: v1.0.0
@author: deangao 
@license: Apache Licence 
@contact: gaowenhui2012@gmail.com
@site: www.iwhgao.com
@file: runner.py
@time: 2016/9/9 9:28
"""

import os
import tgrocey
import MySQLdb
from ConfigParser import ConfigParser


def get_config():
	"""读取数据库配置文件"""
	cfp = ConfigParser()
	cfp.read("./db.ini")
	return cfp


def get_conn_cur():
	"""获取数据库连接"""

	cfp = get_config()
	host = cfp.get("db_settings", "HOST")
	user = cfp.get("db_settings", "USER")
	pwd = cfp.get("db_settings", "PWD")
	db = cfp.get("db_settings", "DB")

	try:
		conn = MySQLdb.connect(host=host, user=user, passwd=pwd, db=db, port=3306, charset='utf8')
		cur = conn.cursor()
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return None, None
	return conn, cur


def get_all_articles(cur):
	"""获取所有文章"""

	cur.execute("SELECT field, content FROM qq_article WHERE length(trim(content))>10;")
	data = cur.fetchall()
	return data


def close_conn(conn):
	conn.close()


if __name__ == '__main__':
	conn, cur = get_conn_cur()
	data = get_all_articles(cur)
	close_conn(conn)
