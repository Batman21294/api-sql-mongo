import pymysql
from flask import Flask, request,jsonify

db = pymysql.connect(host="localhost",user="root",password="Snape@1993")
cursor = db.cursor()
cursor.execute("use apisqlcrud")
cursor.execute("create table if not exists apisqlcrud.sql_crud (emp_name varchar(30))")
db.commit()
cursor.fetchall()

app = Flask(__name__)

@app.route('/insert',methods=['POST'])
def insertrecord():
    if request.method=='POST':
        a = request.json["val"]
        cursor.execute("insert into apisqlcrud.sql_crud values (%s)",a)
        db.commit()
        return "inserted in table"


@app.route('/update',methods=['POST'])
def updaterecord():
    if request.method=='POST':
        b = request.json["to_be_updated_with"]
        d = request.json["id"]
        cursor.execute("update apisqlcrud.sql_crud set emp_name = %s where id = %s", (b,d))
        db.commit()
        return "updated the table"
if __name__=="__main__":
    app.run()