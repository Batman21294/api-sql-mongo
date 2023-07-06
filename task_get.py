from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)
@app.route("/testfunc")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile_no")
    email = request.args.get("email")
    return "this is my first function for get {} {} {}".format(get_name,mobile_number,email)
@app.route("/querydb")
def query_db():
    try:
        db_name = request.args.get("db")
        db = pymysql.connect(host="localhost", user="root", password="Snape@1993",database=db_name)
        cursor = db.cursor()
        tablename = request.args.get("table")
        cursor.execute("select * from {}.{}".format(db_name,tablename))
        data = cursor.fetchall()
        db.close()
    except Exception as e:
        return jsonify(e)
    return jsonify(data)


if __name__=="__main__":
    app.run(port=5001)