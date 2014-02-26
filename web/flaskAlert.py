#!/usr/bin/env python

from flask import *
app = Flask(__name__)

@app.route('/')
def front_page():
	return "Hello World!!!!!!!!"

@app.route('/enroll', methods = ['GET', 'POST'])
def enroll_number():
	if request.args.get('message'):
		return "To %s : %s" % (request.args['phonenumber'], request.args['message'])
	else:
		#show enrollment form
		return render_template('enroll.html')

if __name__ == '__main__':
	app.run(debug = True)