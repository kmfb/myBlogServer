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

@app.route('/api/v1/articles')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM blog.posts')
    rv = cur.fetchall()
    return jsonify(rv)

@app.route('/api/v1/article/<id>')
def delete_task(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM blog.posts \
        WHERE id = {}".format(id))
    rv = cur.fetchall()
    return jsonify(rv[0])

if __name__ == '__main__':
    config = {
        'host': '0.0.0.0',
        'port': 5000,
        'debug': True,
    }
    app.run(**config)




