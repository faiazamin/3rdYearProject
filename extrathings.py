import random, string
from DatabaseFunctions import *

# returns random string of length stringLength
def randomString(stringLength):
  letters = string.ascii_letters
  return ''.join(random.choice(letters) for i in range(stringLength))	

# adds level to the data field
def addLevel(data):
	solved = data["solved"]
	tried = data["tried"]
	# do something extraordinary here
	data["level"] = "TEST"
	return data

def profileText(email):
	if email == None:
		return "Profile"
	return getNameAgainstEmail(email)