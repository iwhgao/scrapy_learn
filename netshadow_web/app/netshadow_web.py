#!/usr/bin/python
# -*- coding:utf8 -*-

from flask import *

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'some_secret'


@app.errorhandler(404)
def page_not_found(error):
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	return render_template('404.html'), 404


@app.route("/validate_login", methods=['POST', 'GET'])
def validate_login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin@163.com':
			error = 'Invalid username'
			return redirect(url_for('login'))
		elif request.form['password'] != 'admin':
			error = 'Invalid password'
			return redirect(url_for('login'))
		else:
			session['logged_in'] = True
			return redirect(url_for('index'))


@app.route("/login", methods=['POST', 'GET'])
def login():
	# 如果已经登录则直接跳转到主页
	if session.get('logged_in'):
		return redirect(url_for('index'))

	return render_template('login.html')


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('login'))


@app.route("/")
@app.route("/index")
def index():
	if not session.get('logged_in'):
		return redirect(url_for('login'))

	return render_template('index.html')


@app.route("/showdata")
def show_data():
	if not session.get('logged_in'):
		return redirect(url_for('login'))

	import MySQLdb
	conn = MySQLdb.connect(host='localhost', user='root', passwd='')
	conn.select_db('opensns');
	cursor = conn.cursor()
	cursor.execute("select * from ocenter_config limit 20")
	data = cursor.fetchone()
	cursor.close()
	conn.close()
	print data

if __name__ == "__main__":
	app.run(debug=True)
