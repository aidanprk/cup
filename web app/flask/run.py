from flask import *

app = Flask(__name__)

@app.route('/')
def start():
	return render_template('login.html')

app.run()