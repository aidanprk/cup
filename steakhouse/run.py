from flask import *
from cupClasses import *


app = Flask(__name__)
	

#start
@app.route('/')
def main():
	return render_template('login.html')

#login
@app.route('/', methods=['POST'])
def login():
	#Teacher Login
	if request.form['submit'] == "Create new Class":
		className = request.form['classname']
		classCode = request.form['code']
		if className == '' or classCode == '':
				return redirect(url_for('login'))
		else:
			created_class = Classroom(className, classCode) 
			return redirect(url_for('teacher', className = className, code = classCode))

	
	#Student Login	
	if request.form['submit'] == "Join Class":
		uname = request.form['unstudent']
		if uname == '':
			return redirect(url_for('login'))
		else:
			return redirect(url_for('student', username = uname))

#student
@app.route('/student/<username>')
def student(username):
	return render_template('studentpage1.html', name = username)


#teacher
@app.route('/teacher/<className>')
def teacher(className, code):
	return render_template('teacher.html')

app.run(debug = True, port = 1210)

