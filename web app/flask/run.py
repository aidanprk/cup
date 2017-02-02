from flask import *

app = Flask(__name__)

@app.route('/')
def login():
	return render_template('login.html')

@app.route('/teacher')
def teacher():
	return render_template('teacher.html')

@app.route('/studentpage1')
def studentpage1():
	return render_template('studentpage1.html')




if __name__ == '__main__':
	app.run(debug=True)