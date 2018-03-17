import sys
# import json
import time
import psycopg2
from flask import *
from pymongo import MongoClient

################################################################################
## NE PAS MODIFIER LA LIGNE SUIVANTE
################################################################################
app = Flask(__name__)
app.secret_key = 'yoloswagg'.encode('utf8')

################################################################################
## NoSQL
################################################################################
def nosql_connection():
        "Connect to mongo db server and set session['mongo']"
        if 'mongo' not in session:
                client = MongoClient("mongodb://localhost")
                db = client['prouby']
                coll = db['hotel']
                session['mongo'] = coll
        return coll

@app.route("/test_nosql")
def nosql_test():
        try:
                # nosql_connection()
                # coll = session['mongo']
                client = MongoClient("mongodb://localhost")
                db = client['prouby']
                coll = db['hotel']
                ret = "<p>"
                for post in coll.find():
                        ret += str(post)
                        ret += "</br>"
                        ret += "</p>"
                return ret
        except Execption as e:
                return str(e)

@app.route("/add", methods=['POST'])
def add_after_form():
        id = request.form['id']
        name = request.form['name']
        num = request.form['num']
        description = request.form['description']
        floor = request.form['floor']
        size = request.form['size']
        tags = request.form['tags']
        bed = request.form['bed']
        bathroom = request.form['bathroom']
        page = add_in_collection(id, name, num, floor, description,
                                 size, tags, bed, bathroom)
        return page

@app.route("/del", methods=['POST'])
def del_after_form():
        title = request.form['title']
        page = del_in_collection(title)
        return page

def del_in_collection(title):
        cmd = {'title': str(title)}
        try:
            client = MongoClient("mongodb://mongodb.emi.u-bordeaux.fr:27017")
            db = client['prouby']
            coll = db['hotel']
            ret = coll.remove(cmd)
            return str(ret)
        except Execption as e:
            return str(e)

def add_in_collection(id, name, num, floor, description, size, tags, bed, bathroom):
        post = [{
                "id": str(id),
                "chambre_name": str(name),
                "number": str(num),
                "floor": str(floor),
                "description": str(description),
                "size": str(size),
                "tags": str(tags),
                "bed": str(bed),
                "bathroom": str(bathroom),
                "comment": ["FIRST !"],
                "like": 0
        }]
        try:
                client = MongoClient("mongodb://mongodb.emi.u-bordeaux.fr:27017")
                db = client['prouby']
                coll = db['testcollection']

                coll.insert(post)
                return "<p>"+str(post)+"</p>"
        except Execption as e:
                return str(e)

@app.route("/chambre", methods=['POST'])
def chambre():
        id = request.form['id']
        cmd = {'id': str(id)}
        try:
                client = MongoClient("mongodb://mongodb.emi.u-bordeaux.fr:27017")
                db = client['prouby']
                coll = db['testcollection']

                ret = coll.find_one(cmd)
                return "</p>" + str(ret) + "</p>"
        except Execption as e:
                return str(e)

@app.route("/list_chambre_test")
def get_list_chambre():
        try:
                client = MongoClient("mongodb://mongodb.emi.u-bordeaux.fr:27017")
                db = client['prouby']
                coll = db['testcollection']

                ret = "{"
                for post in coll.find():
                        if ret != "{":
                                ret += ","
                                ret += str(post)
                                ret += "}"
                                return ret
        except Execption as e:
                return str(e)

################################################################################
## ProsgreSql
################################################################################
def sql_to_rows(command):
        print('Trying to connect to the database')
        try:
                conn = psycopg2.connect("host=dbserver dbname=prouby user=prouby")
                cur = conn.cursor()
                print('Trying to execute command: ' + command)
                try:
                        cur.execute(command)
                        rows = cur.fetchall()
                        cur.close()
                        conn.close()
                        return rows
                except Exception as e:
                        return form_client(error=str(e))
        except Exception as e:
                return form_client(error=str(e))

@app.route("/client", methods=['POST'])
def display_client():
        data = request.form['mail']
        # Try to connect to an existing database
        print('Trying to connect to the database')
        command = 'select * from HotelBis.Client where mail=\'' + data + '\';'
        rows = sql_to_rows(command)
        page = '<p>'
        for client in rows:
                page += str(client[0]) + ' : ' + str(client[1]) + ' : '
                page += str(client[2]) + ' : ' + str(client[3]) + '<br />'

        if page == '<p>':
                return form_client(error="No data")
        page += '</p>'
        return page

################################################################################
## User form
################################################################################
@app.route("/form")
def form():
        return app.send_static_file("form.html")

@app.route("/form_add")
def form_add():
        if 'user' in session:
                if session['user'] == 'admin':
                        return app.send_static_file("form_add.html")
        return '<h1>Access deny !</h1>'

@app.route("/form_del")
def form_del():
        return app.send_static_file("form_del_by_title.html")

@app.route("/after_form", methods=['POST'])
def after_form():
        data = "<h1>Bonjour " + request.form['prenom'] + "</h1>"
        return data

@app.route("/form_client")
def form_client(error=None):
        command = 'select mail from HotelBis.Client;'
        data = sql_to_rows(command)
        return render_template("form_client.html", rows=data, hasError=error)

@app.route("/form_reservation")
def tmp_form_reservation(error=None):
        # data = get_list_chambre()
        return render_template("tmp_reservation_chambre.html")

@app.route("/reservation")
def form_reservation(error=None):
        command = 'select mail from HotelBis.Client;'
        data = sql_to_rows(command)
        return render_template("form_reservation.html", rows=data)

################################################################################
## Login
################################################################################
@app.route("/form_login")
def form_login():
        return app.send_static_file("form_login.html")

@app.route("/login", methods=['POST'])
def login_admin():
        if request.form['user'] == 'admin':
                session['user'] = request.form['user']
                session['password'] = 'admin'
        elif request.form['user'] == request.form['password']:
                session['user'] = request.form['user']
        else:
                return "<h1>Cannot login !</h1>"
        return "<h1>Login with user : "+ session['user'] +"</h1>"

@app.route("/whoami")
def whoami():
        return "<h1>Login : "+ session['user'] +"</h1>"
################################################################################
## Useless
################################################################################
@app.route("/")
def hello():
        data = "<b>Hello world!</b><br>Python "+str(sys.version)
        return data

@app.route("/hello/<name>")
def hello_name(name):
	data= "<b>Hello "+name+"</b>. Nous sommes le " + time.strftime("%d/%m/%Y")
	return data

################################################################################
## NE SURTOUT PAS MODIFIER
################################################################################
if __name__ == "__main__":
        app.run(debug=True)
