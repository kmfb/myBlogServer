from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '7798984'
app.config['MYSQL_DB'] = 'blog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
CORS(app)

def postValues(form):
    title = form.get('title', None)
    summery = form.get('summery', None)
    content = form.get('content', None)
    tags = form.get('tags', None)
    date = form.get('date', None)
    p_type = form.get('type', None)
    return title, summery, content, tags, date, p_type

@app.route('/api/v1/articles')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM blog.posts')
    rv = cur.fetchall()
    return jsonify(rv)

@app.route('/api/v1/article/<id>')
def get_task(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM blog.posts \
        WHERE id = {}".format(id))
    rv = cur.fetchall()
    return jsonify(rv[0])

@app.route('/api/v1/article', methods=['POST'])
def add_task():
    form = request.get_json()
    title, summery, content, tags, date, p_type =  postValues(form)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO blog.posts(title, summery, content, tags, date, type) \
    values('{}', '{}', '{}', '{}', '{}', '{}')".format(title, summery, content, tags, date, p_type))
    mysql.connection.commit()
    if form != None:
        result = 'success'
    else:
        result = 'fault'
    return jsonify({'result': result})

@app.route('/api/v1/user', methods=['POST'])
def get_user():
    form = request.get_json()
    username = form.get('username', None)
    password = form.get('password', None)
   
    cur = mysql.connection.cursor()
    rv = cur.execute("SELECT * FROM blog.users \
        WHERE username = '{}' AND password = '{}'".format(username, password))
    if rv != 0:
        res = {
            'code': 200
        }
    else:
        res = {
            'code': 403
        }
    return jsonify({'data': res})





if __name__ == '__main__':
    config = {
        'host': '0.0.0.0',
        'port': 5000,
        'debug': True,
    }
    app.run(**config)




