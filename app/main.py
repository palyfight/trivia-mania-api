from flask import Flask, request, jsonify, Response
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import simplejson as json
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{}:{}@172.18.0.2:3306/trivia'.format("root", "root")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
triviadb = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	# if missing data, return error
	username = request.form.get('username')
	email = request.form.get('email')
	password = bcrypt.generate_password_hash(request.form.get('password'))
	save_to_db(username, email, password)
	# if save to db worked, send email ????
	#send_email(email)
	# if email sent successfully, return 200 ???
	#return request.form
	return Response('', status=200, mimetype='application/json')

def save_to_db(username, email, password):
	user = User(username=username, email=email, password=password)
	triviadb.session.add(user)
	app.logger.info(triviadb.session.commit())
	app.logger.info('Created user %s', username)

def send_email(email):
	# if email is not real email, return error
	app.logger.info('Sent registration email to %s', email)

class User(triviadb.Model):
    id = triviadb.Column(triviadb.Integer, primary_key=True)
    username = triviadb.Column(triviadb.String(255), unique=True, nullable=False)
    email = triviadb.Column(triviadb.String(255), unique=True, nullable=False)
    password = triviadb.Column(triviadb.String(255), unique=False, nullable=False)
    totalscore = triviadb.Column(triviadb.Integer, unique=False, nullable=True)
    bestscore = triviadb.Column(triviadb.Integer, unique=False, nullable=True)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)