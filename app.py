from flask import Flask, render_template, request, session, redirect
from functools import wraps
from dbUtils import getList, getM_List, addtocar, getC_List, delC_List

# creates a Flask application, specify a static folder on /
app = Flask(__name__, static_folder='static',static_url_path='/')
#set a secret key to hash cookies
app.config['SECRET_KEY'] = '123TyU%^&'
#edit by user B
#define a function wrapper to check login session
def login_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		loginID = session.get('loginID')
		if not loginID:
			return redirect('/loginPage.html')
		return f(*args, **kwargs)
	return wrapper


@app.route("/") 
def hello(): 
	data=getM_List()
	return render_template('mainlist.html',data=data)

@app.route("/add/<string:name>/<int:price>")
def add(name, price):
	addtocar(name, price)
	data=getM_List()
	return render_template('mainlist.html',data=data)

@app.route("/car")
def car():
	data=getC_List()
	return render_template('car.html',data=data)

@app.route("/delete/<string:name>")
def delete(name):
	delC_List(name)
	data=getC_List()
	return render_template('car.html',data=data)

@app.route("/test/<string:name>/<int:id>")
#取得網址作為參數
def useParam(name,id):
	return f"got name={name}, id={id} "

@app.route("/edit")
#使用server side render: template 樣板
def h1():
	dat={
		"name": "大牛",
		"content":"內容說明文字"
	}
	#editform.html 存在於 templates目錄下, 將dat 作為參數送進 editform.html, 名稱為 data
	return render_template('editform.html', data=dat)

@app.route("/update", methods=['get','post'])
def upd():
	name=request.form['name']
	cnt=request.form['content']
	#sql
	html=f"update====> nnn={name},cnt={cnt}"
	return html

@app.route("/list")
#使用server side render: template 樣板
def h2():
	dat=[
		{
			"name": "大牛",
			"p":"超愛吃瓜"
		},
		{
			"name": "小李",
			"p":"怕榴槤"
		},
		{
			"name": "",
			"p":"ttttt"
		},
		{
			"name": "老謝",
			"p":"來者不拒"
		}
	]
	return render_template('list.html', data=dat)

@app.route('/input', methods=['GET', 'POST'])
def userInput():
	if request.method == 'POST':
		form =request.form
	else:
		form= request.args

	txt = form['txt']  # pass the form field name as key
	note =form['note']
	select = form['sel']
	msg=f"method: {request.method} txt:{txt} note:{note} sel: {select}"
	return msg

@app.route("/listJob")
#使用server side render: template 樣板
def gl():
	dat=getList()
	return render_template('todolist.html', data=dat)

#handles login request
@app.route('/login', methods=['POST'])
def login():
	form =request.form
	id = form['ID']
	pwd =form['PWD']
	#validate id/pwd
	if id=='123' and pwd=='456':
		session['loginID']=id
		return redirect("/")
	else:
		session['loginID']=False
		return redirect("/loginForm")
