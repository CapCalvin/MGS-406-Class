from flask import Flask, url_for, redirect, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def hello_world():
	return render_template("home.htm")



@app.route("/enternew")
def enternew():
	return render_template("Employee.htm")

@app.route("/addrec", methods = ['POST','GET'])
def addrec():
	if request.method == "POST":
		EMPID = request.form['EMPID']
		EMPname = request.form['EMPname']
		EMPgender = request.form['EMPgender']
		EMPphone = request.form['EMPphone']
		EMPBdate = request.form['EMPBate']



		with sql.connect("database.db") as conn:
			cur = conn.cursor()
			cmd = "INSERT INTO employee (EMPID,EMPname,EMPgender,EMPphone,EMPBdate) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(EMPID,EMPname,EMPgender,EMPphone,EMPBdate)
			cur.execute(cmd)
			conn.commit()
		
			msg = "Record successfully added"
		return render_template("output.htm", msg=msg)

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from employee")
   
   rows = cur.fetchall(); 
   return render_template("list.htm",rows = rows)

if __name__ =="__main__":
	app.run() 
