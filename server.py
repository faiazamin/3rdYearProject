from flask import Flask, render_template, request, url_for, make_response, redirect, abort
from DatabaseFunctions import *
from extrathings import *

app = Flask(__name__)
TITLE = "ROJ"

'''
TODO:
1. complete all the htmls
2. Database connectivity
3. OJ checking system
4. Task Queue
5. change {{profile}} for authorized connections
'''
# main page

signup_link_dict = {} # it must be brought to database of course

temp_code_storage_for_signin = {}

'''
UNAUTHORIZATION MUST
if Authorized return practice page
'''
@app.route('/')
def index_page():
	# checks for authorization
	email = request.cookies.get('email')
	# if authorized then go
	if email == None:
		return render_template('index.html', title=TITLE)
	# else redirect to practice
	return redirect(url_for('practice_page'))


'''
AUTHORIZATION MUST
Store all problem data 
'''
@app.route('/practice')
def practice_page():
	email = request.cookies.get('email')
	if email == None:
		return redirect(url_for('index_page'))
	#data = all_problem(email)
	data = {}
	all_problem(email)
	return render_template('practice.html', title=TITLE, data=data)


# problem page
# authorized first
# has to check if problemid exists 
@app.route('/problem/<problemid>')
def problem_page(problemid):
	problemlink = url_for('static', filename='PROBLEM/'+problemid+'.pdf')
	data = {"problemid" : 1000, "timelimit" : "2", "memorylimit" : "2"}
	return render_template('problem.html', title=TITLE, problemlink=problemlink, data=data)

# profile page
'''
AUTHORIZATION MUST
Return data based on Cookie email
'''
@app.route('/profile')
def profile_page():
	# checks cookies for authorization
	email = request.cookies.get('email')
	# unauthorized users will go to index
	if email == None:
		return redirect(url_for('index_page'))
	# authorized will have their data
	data = userData(email)
	data = addLevel(data)
	return render_template('profile.html', title=TITLE, data=data, profile=profileText(request.cookies.get('email')))

# change page
'''
AUTHORIZED MUST
'''
@app.route('/change')
def change_page():
	return 'change'

# submission page
'''
AUTHORIZED MUST
'''
@app.route('/sumbission')
def submission_page():
	return 'sumbission'


# sign up page
'''
Unauthorized must
GET and POST METHOD
'''
# authorization test
@app.route('/signup', methods=["GET", "POST"])
def signup_page():
	# checks cookies for authorization
	email = request.cookies.get('email')
	# if valid user then fuck off
	if email != None:
		return redirect(url_for('practice_page'))
	# not registered users portion
	if request.method == 'GET':
		return render_template('signup.html', title=TITLE)
	# Try to sign up the dude
	# try:
	name = request.form["name"]
	email = request.form["email"]
	instritution = request.form["instritution"]
	password = request.form["pass"]
	signuptry = signup(name, email, instritution, password)
	if signuptry == None:
		return {"Result" : "error", "Message" : "Signup failed."}		
	ranstr = randomString(20)
	signup_link_dict[ranstr] = email
	return {"Result" : "success", "Location" : "/newsignup/" + ranstr}
	# except:
	return {"Result" : "error", "Message" : "Signup failed."}	

# UNAUTHORIZATION MUST
@app.route('/signin', methods=["GET", "POST"])
def signin_page():
	if(request.cookies.get('email') != None):
		return redirect('practice')
	if request.method == 'GET':
		return render_template('signin.html', title=TITLE)
	email = request.form["email"]
	password = request.form['pass']
	signintry = signin(email, password)
	if signintry == None:
		return {"Result" : "error", "Message" : "Signin Failed"}
	ranstr = randomString(19)
	temp_code_storage_for_signin[ranstr] = email;
	return {"Result" : "success", "Location" : "/newsignin/" + ranstr}

@app.route('/newsignin/<code>')
def new_sign_in_page(code):
	email = temp_code_storage_for_signin.get(code)
	if email == None:
		return redirect(url_for('index_page'))
	temp_code_storage_for_signin.pop(code)
	resp = make_response(render_template('signinsuccess.html', title=TITLE, name="Rahat"))
	resp.set_cookie('email', email)
	return resp

# signout
@app.route('/signout')
def signout():
	# removes cookies by expiring them
	resp = make_response(render_template('index.html', title=TITLE))
	resp.set_cookie('email', '', expires=0)
	return resp


# New login page
@app.route('/newsignup/<code>')
def new_sign_up_page(code):
	# checks if code is valid for email
	email = signup_link_dict.get(code)
	# aborts if invalid
	if email == None:
		redirect(url_for('index_page'))
	# pops the code out
	signup_link_dict.pop(code)
	verifyUser(email)
	# sets cookies
	resp = make_response(render_template('signinsuccess.html', title=TITLE, name="Rahat"))
	resp.set_cookie('email', email)
	return resp


# submit with problemid
# has to check if authorized
# has to check if valid pid
@app.route('/submit/<problemid>')
def submit_with_problemid(problemid):
	return problemid
	


if __name__ == "__main__":
	app.run()