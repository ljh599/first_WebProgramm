from flask import Flask, render_template, request
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)

app.config['MySQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'data'
app.config['MYSQL_DATABSE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def home():
    return "<h1>hello</h1>"

@app.route("/demo_mysql", methods = ["GET"])
def demo_sql():
        cursor.execute("SELECT name, content from charts")
        rst = cursor.fetchall()
        return render_template("table.html", data = rst)


@app.route("/demo_mysql_message", methods = ["POST"])
def demo_sql_message():
        User = request.form.get('user')
        Content = request.form.get('content')
        sql = "INSERT INTO charts (name, content) VALUES (%s, %s);"
        newdata = (User, Content)
        cursor.execute(sql, newdata)
        cursor.execute("SELECT name, content from charts")
        rst = cursor.fetchall()
        #for (name, content) in cursor:
                #print("Name: %s, Content: %s" %(name, content))
        return render_template("table.html", data = rst)

app.run(port=3508)