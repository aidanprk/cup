from flask import *

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('login.html')

@app.route('/', methods=['POST'])
def login():
	if request.method == 'POST':
		print('createclass')
	if request.method == 'POST' and request.form['submit'] == 'createuser':
		print('createuser')
	else:
		print('failed')



@app.route('/student/<username>')
def student(username):
	return render_template('studentpage1.html')

@app.route('/teacher/<className>')
def teacher(className):
	return render_template('teacher.html')

app.run(debug = True, port = 1200)

