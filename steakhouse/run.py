from flask import *
from cupClasses import *


app = Flask(__name__)

@app.route('/')
def main():
	return render_template('login.html')

@app.route('/', methods=['POST'])
def login():
	#Teacher Login
	if request.form['submit'] == "Create new Class":
		className = request.form['classname']
		classCode = request.form['code']
		if className == '' or classCode == '':
				return redirect(url_for('login'))
		else:
			myClass = Classroom(className, classCode)
			return redirect(url_for('teacher', className = myClass.name, classObject = myClass))


	
	#Student Login	
	if request.form['submit'] == "Join Class":
		uname = request.form['unstudent']
		if uname == '':
			return redirect(url_for('login'))
		else:
			me = Student(uname)
			redirect(url_for['student'],username = uname)



@app.route('/student/<username>')
def student(username):
	return render_template('studentpage1.html')

@app.route('/teacher/<className>')
def teacher(className, classObject):
	myClass = classObject
	return render_template('teacher.html')

app.run(debug = True, port = 1200)


	
