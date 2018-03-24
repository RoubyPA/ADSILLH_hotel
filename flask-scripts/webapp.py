import sys
# import json
import time
import psycopg2
from flask import *
from pymongo import MongoClient

################################################################################
## NE PAS MODIFIER LES LIGNES SUIVANTE
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
        if session['user'] != 'prouby':
                print ("[del_in_collection] access demy for user: "+ session['user'])
                return app.send_static_file("error_access_deny.html")
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
        if session['user'] != 'prouby':
                print ("[del_in_collection] access demy for user: "+ session['user'])
                return app.send_static_file("error_access_deny.html")

        title = request.form['title']
        page = del_in_collection(title)
        return page

def del_in_collection(title):
        if session['user'] != 'prouby':
                print ("[del_in_collection] access demy for user: "+ session['user'])
                return app.send_static_file("error_access_deny.html")

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
        if session['user'] != 'prouby':
                print ("[add_in_collection] access demy for user: "+ session['user'])
                return app.send_static_file("error_access_deny.html")

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
                client = MongoClient("mongodb://localhost")
                db = client['prouby']
                coll = db['hotel']

                coll.insert(post)
                return "<p>"+str(post)+"</p>"
        except Execption as e:
                return str(e)

@app.route("/chambre", methods=['POST'])
def chambre():
        id = request.form['id']
        cmd = {'id': str(id)}
        try:
                client = MongoClient("mongodb://localhost")
                db = client['prouby']
                coll = db['hotel']

                ret = coll.find_one(cmd)
                return "</p>" + str(ret) + "</p>"
        except Execption as e:
                return str(e)

@app.route("/chambre/list")
def get_list_chambre():
        try:
                client = MongoClient("mongodb://localhost")
                db = client['prouby']
                coll = db['hotel']

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
        # try:
        print('Trying to connect to the database')
        conn = psycopg2.connect("host=localhost dbname=prouby user=prouby password=xxx")
        print('Connection OK !')
        cur = conn.cursor()
        print('Trying to execute command: ' + command)
        cur.execute(command)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
        # except Exception as e:
        #         return form_client(error=str(e))

################################################################################
## Admin page
################################################################################
@app.route("/admin/chambre/add")
def form_add():
        if session['user'] == 'prouby':
                return app.send_static_file("form_add.html")
        print ("[add_room] access demy for user:"+ session['user'])
        return app.send_static_file("error_access_deny.html")

@app.route("/admin/chambre/del")
def form_del():
        if session['user'] == 'prouby':
                return app.send_static_file("form_del_by_title.html")
        print ("[del_room] access demy for user: "+ session['user'])
        return app.send_static_file("error_access_deny.html")

@app.route("/admin/client/list")
def form_client(error=None):
        if session['user'] == 'prouby':
                command = 'select email from hotel.clients;'
                data = sql_to_rows(command)
                return render_template("form_client.html", rows=data, hasError=error)
        print ("[del_room] access demy for user: "+ session['user'])
        return app.send_static_file("error_access_deny.html")

@app.route("/admin/client/show", methods=['POST'])
def display_client():
        if session['user'] != 'prouby':
                return app.send_static_file("error_access_deny.html")

        data = request.form['mail']
        command = 'select * from hotel.clients where email=\'' + data + '\';'
        rows = sql_to_rows(command)
        page = '<p>'
        for client in rows:
                page += str(client) + '<br>'

        if page == '<p>':
                return form_client(error="No data")
        page += '</p>'
        return page

################################################################################
## User page
################################################################################
@app.route("/")
def index():
        return app.send_static_file("index.html") # TODO create template

@app.route("/reservation/")
def select_date ():
        if 'user' not in session:
                return form_login()

        return render_template("form_select_date.html")


@app.route("/reservation/validation", methods=['POST'])
def reservation_validation ():
        if 'user' not in session:
                return form_login()

        session['chambre'] = str(request.form['chambre'])

        data = "<ul>"
        data += "<li>User = "+ session['nom'] +" "+ session['prenom'] +"</li>"
        data += "<li>Début = " + session['debut'] + "</li>"
        data += "<li>Fin = " + session['fin'] + "</li>"
        data += "<li>Chambre = " + session['chambre'] + "</li>"
        data += "</ul>"

        return "<h1>Validation</h1>" + data

@app.route("/reservation/select/chambre", methods=['POST'])
def form_reservation(error=None):
        # if user not connected
        if session['user'] == "" or 'user' not in session:
                return form_login()

        session['debut'] = request.form['debut']
        session['fin'] = request.form['fin']

        command = 'SELECT * FROM hotel.disponibilite '
        command += 'WHERE libredu <= \''+session['debut']+'\' '
        command += '  AND au >= \''+session['fin']+'\' '
        command += 'ORDER BY etage, libredu, au, numero;'

        data = sql_to_rows(command)
        if data == []:
                return "<h1>Pas de disponibilité</h1>"

        return render_template("form_reservation.html", rows=data)

################################################################################
## Login
################################################################################
@app.route("/login")
def form_login():
        return app.send_static_file("form_login.html")

@app.route("/login/connect", methods=['POST'])
def login():
        if request.form['user'] == "prouby" and request.form['password'] == "passw0rd":
                session['user'] = request.form['user']
                session['nom'] = "Rouby"
                session['prenom'] = "Pierre-Antoine"
                return "<h1>Welcome administrator !</h1>"

        # Possible SQL injection
        command = 'SELECT nom,prenom,address FROM hotel.clients '
        command += 'WHERE password = \''+request.form['password']+'\' '
        command += '  AND email = \''+request.form['user']+'\' '
        command += ';'

        data = sql_to_rows(command)
        if data != "":
                session['user'] = request.form['user']
                session['nom'] = str(data[0][0])
                session['prenom'] = str(data[0][1])
        else:
                return "<h1>Cannot login !</h1>"

        ## TODO create template
        return "<h1>Login with user : "+session['nom']+" "+session['prenom']+"</h1><h2><a href=\"/reservation\">Réservation</a><h2>"

@app.route("/login/whoami")
def whoami():
        return "<h1>Login : "+ session['user'] +"</h1>"

@app.route("/login/disconnect")
def disconnect():
        session['user'] = ""
        return "<h1>Diconnected</h1>"

################################################################################
## Useless
################################################################################
# @app.route("/hello/<name>")
# def hello_name(name):
# 	data= "<b>Hello "+name+"</b>. Nous sommes le " + time.strftime("%d/%m/%Y")
# 	return data

################################################################################
## NE SURTOUT PAS MODIFIER
################################################################################
if __name__ == "__main__":
        app.run(debug=True)
