from flask import Flask, render_template, request, url_for, make_response, redirect, abort
from faiaz import signup, signin, userData, all_problem
import random, string

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

signin_link_dict = {}
name_against_email = {}


'''
UNAUTHORIZATION MUST
if Authorized return practice page
'''
@app.route('/')
def index_page():
	# checks for authorization
	email = request.cookies.get('email')
	# if authorized then go
	if email != None:
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
	data = all_problem(email)
	return render_template('practice.html', title=TITLE, data=data)


# problem page
# authorized first
# has to check if problemid exists 
@app.route('/problem/<problemid>')
def problem_page(problemid):
	problemlink = url_for('static', filename='PROBLEM/'+problemid+'.pdf')
	print(problemlink)
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
	return render_template('profile.html', title=TITLE, data=data)

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
	try:
		name = request.form["name"]
		email = request.form["email"]
		instritution = request.form["instritution"]
		password = request.form["pass"]
		signuptry = signup(name, email, instritution, password)
		if signuptry == None:
			return {"Result" : "error", "Message" : "Login failed."}		
		ranstr = randomString(20)
		signin_link_dict[ranstr] = email
		name_against_email[email] = name
		return {"Result" : "success", "Location" : "/profile/newsignin/" + ranstr}
	except:
		return "SORRY"


# signout
@app.route('/signout')
def signout():
	# removes cookies by expiring them
	resp = make_response(render_template('index.html', title=TITLE))
	resp.set_cookie('email', '', expires=0)
	return resp


# New login page
@app.route('/profile/newsignin/<code>')
def new_sign_in_page(code):
	# checks if code is valid for email
	email = signin_link_dict.get(code)
	print(signin_link_dict)
	# aborts if invalid
	if email == None:
		abort(401)
	# pops the code out
	signin_link_dict.pop(code)
	# sets cookies
	resp = make_response(render_template('signinsuccess.html', title=TITLE, name="Rahat"))
	resp.set_cookie('email', email)
	return resp


# submit with problemid
# has to check if authorized
# has to check if valid pid
@app.route('/submit/<problemid>')
def submit_with_problemid(problemid):
	


# returns random string of length stringLength
def randomString(stringLength):
  letters = string.ascii_letters
  return ''.join(random.choice(letters) for i in range(stringLength))	




if __name__ == "__main__":
	app.run()