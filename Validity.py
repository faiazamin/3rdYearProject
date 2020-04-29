import re


# returns False if everything is correct
# returns the error message if anything wrong
def fails_signup_validity(name, email, instrituion, password):
	# name part
	# # name cannot be empty
	if name == "":
		return "Name cannot be empty"
	# # name cannot have non-alphabetic character
	for char in name:
		if ('a' <= char and char <= 'z') or ('A' <= char and char <= 'Z'):
			pass
		else:
			return "Name cannot have non-alphabetic character"
	# email part
	# # email has to maintain regex
	match_email = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email, re.M|re.I)
	if match_email:
		pass
	else:
		return "Not a valid email"
	# instritution part
	# # simple check
	if instritution == "":
		return "Instritution cannot be empty"
	# pass check
	# # pass has to be at least 6 char
	if len(password) < 6:
		return "Password's minimum length is 6" 
	return False
