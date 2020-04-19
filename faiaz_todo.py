'''----------------------------------
tables
1. user{ name, email, isverified, instritution, password }
2. submission{ submissionid, problemid, email, verdict }
3. problems { problemid, name, tag, solved, tried }
----------------------------------'''


def signup(name, email, instritution, password):
	# will check if the email is not already in the database
	# if in the database then returns None
	# if valid email then makes new entry at the database for it having isverified field false
	# returns email if everything is done perfectly
	pass

def verifyUser(email):
	# makes isVerified field True
	# returns nothing
	pass

def signin(email, password):
	# checks if email, pass is true for an entry and also it is verified
	# if fine then returns email
	# else returns None
	pass

def userData(email):
	# returns a dictionary exactly like down one
	# {"name":"Rahat Hossain", "email" : "rahathossain690@gmail.com", "instritution" : "Univerisity of Dhaka", "solve" : "2", "tried" : "2"}
	pass

def all_problem(email):
	# returns all problems exactly like this (array of dictionary)
	# [{"number" : "1", "problemid" : "1000", "name" : "Libir's Wisdom", "tag" : "Beginner", "solved" : "True"}]
	pass

def getNameAgainstEmail(email):
	# will return the {name} for an email
	pass

def changeVerdict(submissionid, verdict):
	# will change the verdict for submissionid
	# returns nothing
	pass

def newSubmission(email, problemid):
	# will create new entry for email and problemid
	# verdict will be "Not Judged Yet"
	# will return the submissionid of the new entry
	pass

def getSubmission(email, count=False):
	# if count is False then will return all the submissions
	# if count is True then will return last 30 submissions
	# will return like an array of dictionary of course
	pass

