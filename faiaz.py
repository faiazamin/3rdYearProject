

def signup(name, email, instritution, password):
	if(email == "rahathossain690@gmail.com"):
		return email
	return None

def signin(email, password):
	if email == 'rahathossain690@gmail.com':
		return email
	return None

def userData(email):
	return {"name":"Rahat Hossain", "email" : "rahathossain690@gmail.com", "instritution" : "Univerisity of Dhaka", "solve" : "2", "tried" : "2", "level" : "boss"}

def all_problem(email):
	return [{"number" : "1", "problemid" : "1000", "name" : "Libir's Wisdom", "tag" : "Beginner"}] 

def getNameAgainstEmail(email):
	# will return the {name} for an email
	pass