from flask import Flask, render_template, request, url_for, make_response, redirect, abort
from DatabaseFunctions import *
from extrathings import *
from ProblemManager import *
import threading
from MailVerify import *
from Validity import *

app = Flask(__name__)
TITLE = "ROJ"
ALL_TESTS = {}
temp_code_storage_for_signin = {}


# Checkout here
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # if you want, you can use other mail server. But you need to configure
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'i0wont0forget0this0ever@gmail.com'
app.config['MAIL_PASSWORD'] = 'amaderoj#1'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# complete
@app.route('/')
def index_page():
	# checks for authorization
	email = request.cookies.get('email')
	# if authorized then go
	if email == None:
		return render_template('index.html', title=TITLE)
	# else redirect to practice
	return redirect(url_for('practice_page'))

# complete
@app.route('/practice')
def practice_page():
	email = request.cookies.get('email')
	if email == None:
		return redirect(url_for('index_page'))
	return render_template('practice.html', title=TITLE, data=all_problem(email), profile=profileText(request.cookies.get('email')))

# not complete
# problemid is not checked if real
@app.route('/problem/<problemid>')
def problem_page(problemid):
	problemlink = url_for('static', filename='PROBLEM/'+problemid+'.pdf')
	return render_template('problem.html', title=TITLE, problemlink=problemlink, problemid=problemid, profile=profileText(request.cookies.get('email')))

# not complete
# compare not added
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

# incomplete
@app.route('/change')
def change_page():
	return 'change'

# incomplete
@app.route('/submission')
def submission_page():
	return 'render_template()'

# complete
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
		if fails_signup_validity(name, email, instritution, password):
			return {"Result" : "error", "Message" : fails_signup_validity(name, email, instritution, password)}
		signuptry = signup(name, email, instritution, password)
		if signuptry == None:
			return {"Result" : "error", "Message" : "Signup failed. Use unique email and valid informations."}	
		msg = send_mail(email)
		thread = threading.Thread(target=mailing_matching, args=(mail, msg,))
		thread.start()
		return {"Result" : "success"}
	except:
		return {"Result" : "error", "Message" : "Signup failed."}	

# complete
def mailing_matching(mail, msg):
	with app.app_context():
		mail.send(msg)
	return 'fuck'

# complete
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

# complete
@app.route('/newsignin/<code>')
def new_sign_in_page(code):
	email = temp_code_storage_for_signin.get(code)
	if email == None:
		return redirect(url_for('index_page'))
	temp_code_storage_for_signin.pop(code)
	resp = make_response(render_template('signinsuccess.html', title=TITLE, name="Rahat"))
	resp.set_cookie('email', email)
	return resp


# complete
@app.route('/signout')
def signout():
	# removes cookies by expiring them
	resp = make_response(render_template('index.html', title=TITLE))
	resp.set_cookie('email', '', expires=0)
	return resp

# complete
@app.route('/confirm_email/<token>')
def confirm_email(token):
  try:
    email = SECRET_SERIALIZER.loads(token, salt='email-confirm', max_age=3600)
    verifyUser(email)
    resp = make_response(render_template('signinsuccess.html', title=TITLE, name="User"))
    resp.set_cookie('email', email)
    return resp
  except:
    abort(401)

# not complete
@app.route('/submit', methods=["GET", "POST"])
def submit_page():
	if request.cookies.get('email') == None:
		return redirect(url_for('index_page'))
	PID = request.args.get('problem')
	if request.method == 'GET':	
		return render_template('submit.html', title=TITLE, problemid=PID, profile=profileText(request.cookies.get('email')))
	problemid = request.form.get('problemid')
	language = request.form.get('language')
	code = request.form.get('code')
	# if everything not fine
	# return {"Result" : "error", "Message" : "haha"}
	# supply the next thing
	return {"Result" : "success", "Location" : "/submission"}

# incomplete
@app.route('/submit/<problemid>')
def submit_with_problemid(problemid):
	return problemid
	


if __name__ == "__main__":
	global ALL_TESTS
	ALL_TESTS = get_tests()
	app.run()