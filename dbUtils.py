#!/usr/local/bin/python
# Connect to MariaDB Platform
import mysql.connector #mariadb

try:
	#連線DB
	conn = mysql.connector.connect(
		user="root-test",
		password="test1234",
		host="localhost",
		port=3306,
		database="shopping"
	)
	#建立執行SQL指令用之cursor, 設定傳回dictionary型態的查詢結果 [{'欄位名':值, ...}, ...]
	cursor=conn.cursor(dictionary=True)
except mysql.connector.Error as e: # mariadb.Error as e:
	print(e)
	print("Error connecting to DB")
	exit(1)


def add(data):
	sql="insert into 表格 (欄位,...) VALUES (%s,%s,...)"
	#param=('值',...)
	cursor.execute(sql,param)
	conn.commit()
	return
	
def delete(id):
	sql="delete from 表格 where 條件"
	cursor.execute(sql,(id,))
	conn.commit()
	return

def update(id,data):
	sql="update 表格 set 欄位=值,... where 條件"
	#param=('值',...)
	cursor.execute(sql,param)
	conn.commit()
	return
	
def getList():
	sql="select 欄位,... from 表格 where 條件;"
	#param=('值',...)
	cursor.execute(sql,param)
	return cursor.fetchall()

def getM_List():
	sql="select l_name name, l_price price from list where 1=1;"
	#param=('值',...)
	cursor.execute(sql)
	return cursor.fetchall()

def addtocar(name, price):
	SQL="INSERT INTO car(c_name, c_price) VALUES (%s,%s)"
	cursor.execute(SQL,(name, price,))
	conn.commit()
	return

def getC_List():
	sql="select c_name name, c_price price, c_count count from car where 1=1;"
	#param=('值',...)
	cursor.execute(sql)
	return cursor.fetchall()

def delC_List(name):
	sql="DELETE FROM car WHERE c_name=%s"
	cursor.execute(sql,(name,))
	return