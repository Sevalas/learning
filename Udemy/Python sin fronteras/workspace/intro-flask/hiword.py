from flask import Flask, request, url_for, redirect, abort, render_template
from mysql import connector
from mysql.connector import cursor
app = Flask(__name__)
udemyDb = connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='udemy'
)

udemyCursor = udemyDb.cursor(dictionary=True)

@app.route('/')
def index():
    return 'Hi world'
# METHODS(REST): GET, POST, PUT, DELETE, PATCH
@app.route('/post/<int:post_id>', methods=['GET','POST'])
def lala(post_id):
    return str(request.method)+' post id is: '+str(post_id);

@app.route('/lele', methods=['POST','GET'])
def lele():
    udemyCursor.execute('select * from Usuario')
    usuarios = udemyCursor.fetchall()
    # abort(500)
    # return redirect(url_for('lala', post_id=3))
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    # return render_template('lele.html')
    return render_template('lele.html', usuarios=usuarios)

@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hi world!')

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = "insert into Usuario (username,email,edad) values (%s,%s,%s)"
        udemyCursor.execute(sql,(username,email,edad))
        udemyDb.commit()

        return redirect(url_for('lele'))
    return render_template('crear.html')