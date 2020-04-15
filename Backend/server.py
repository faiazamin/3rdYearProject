from flask import Flask, render_template, request, url_for, make_response


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

user_dict = {}

@app.route('/')
def index_page():
	'''
	UNAUTHORIZATION MUST
	if Authorized return practice page
	'''
	return render_template('index.html', title=TITLE)

# main page
@app.route('/practice')
def practice_page():
	'''
	AUTHORIZATION MUST
	Store all problem data 
	'''
	data = [{"number" : "1", "problemid" : "1000", "name" : "Libir's Wisdom", "tag" : "Beginner"}]
	return render_template('practice.html', title=TITLE, data=data)

# problem page
@app.route('/problem/<problemid>')
def problem_page(problemid):
	return problemid

# profile page
@app.route('/profile')
def profile_page():
	'''
	AUTHORIZATION MUST
	Return data based on Cookie email
	'''
	data = {"name":"Rahat Hossain", "email" : "rahathossain690@gmail.com", "instritution" : "Univerisity of Dhaka", "solve" : "2", "tried" : "2", "level" : "boss"}
	return render_template('profile.html', title=TITLE, data=data)

# change page
@app.route('/change')
def change_page():
	'''
	AUTHORIZED MUST
	'''
	return 'change'

# submission page
@app.route('/sumbission')
def submission_page():
	'''
	AUTHORIZED MUST
	'''
	return 'sumbission'

# sign up page
@app.route('/signup')
def signup_page():
	'''
	Unauthorized must
	GET and POST METHOD
	'''
	return render_template('signup.html', title=TITLE)




if __name__ == "__main__":
	app.run()