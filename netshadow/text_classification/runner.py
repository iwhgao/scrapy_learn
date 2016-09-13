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
import sys
import tgrocery
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


def print_usage():
	print "Usage runner.py <command:train|predict> <file_path>"
	print "Example: python runner.py train"
	print "Example: python runner.py predict ./sample/test.txt"
	sys.exit()


if __name__ == '__main__':

	if len(sys.argv) < 2:
		print_usage()
	elif sys.argv[1] == "predict" and len(sys.argv) != 3:
		print_usage()

	cmd = sys.argv[1]
	conn, cur = get_conn_cur()
	data = get_all_articles(cur)
	data = list(data)[1:800]
	data = [(x[0], x[1].encode('utf8')) for x in data]

	if cmd == "train":
		gry = tgrocery.Grocery('model_pickle')
		gry.train(data)
		gry.save()

		new_gry = tgrocery.Grocery('model_pickle')
		new_gry.load()

		test_res = new_gry.test(data)
		print test_res.accuracy_overall
		print test_res.accuracy_labels
		print test_res.show_result()
	elif cmd == "predict":
		new_gry = tgrocery.Grocery('model_pickle')
		new_gry.load()

		line = " ".join(open(sys.argv[2], "r").readlines())
		print new_gry.predict(line)

	close_conn(conn)
