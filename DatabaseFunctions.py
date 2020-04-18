# Code by: Faiaz Amin Khan


import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()


# will check if the email is not already in the database
# if in the database then returns None
# if valid email then makes new entry at the database for it having isverified field false
# returns email if everything is done perfectly

def signup(name, email, institution, password):
    checkmail = (email,)
    cursor.execute('SELECT email FROM user WHERE email=?', checkmail)
    checkRtn = cursor.fetchone()
    if checkRtn == None:
        insertValues = (name, email, institution, password,)
        cursor.execute('INSERT INTO user VALUES (?,?,?,?)', insertValues)
        conn.commit()
        return email
    else:
        return None


# checks if email, pass is true for an entry and also it is verified
# if fine then returns email
# else returns None

def signin(email, password):
    parameter = (email, password,)
    cursor.execute('SELECT isverified FROM user WHERE email = ? AND password = ?', parameter)
    rtnMessage = cursor.fetchone()
    if rtnMessage == 1:
        return email
    else:
        return None


# makes isVerified field True
# returns nothing

def verifyUser(email):
    parameter = (email,)
    cursor.execute('UPDATE user SET isverified = 1 WHERE email = ?', parameter)
    conn.commit()


# will return the {name} for an email

def getNameAgainstEmail(email):
    parameter = (email,)
    cursor.execute('SELECT name FROM user WHERE email = ?', parameter)
    rtnMessage = cursor.fetchone()
    return rtnMessage[0];


# will change the verdict for submissionid
# returns nothing

def changeVerdict(submissionid, verdict):
    parameter = (verdict, submissionid,)
    cursor.execute('UPDATE submission SET verdict = ? WHERE submissionid = ?', parameter)
    conn.commit()


# will create new entry for email and problemid
# verdict will be "Not Judged Yet"
# will return the submissionid of the new entry

def newSubmission(email, problemid):
    parameter = ("Not Judged Yet", problemid, email,)
    cursor.execute('INSERT INTO submission VALUES (?,?,?)', parameter)
    conn.commit()
    cursor.execute('SELECT submissionid FROM submission WHERE verdict=? AND problemid=? AND email=?', parameter)
    rtnMessage = cursor.fetchone()
    return rtnMessage[0]


# returns a dictionary exactly like down one
# {"name":"Rahat Hossain", "email" : "rahathossain690@gmail.com", "instritution" : "Univerisity of Dhaka", "solve" : "2", "tried" : "2"}

def userData(email):
    parameter = (email,)
    cursor.execute('SELECT name,email,institution FROM user WHERE email=?', parameter)
    rtnMessage1 = cursor.fetchone()
    cursor.execute('SELECT COUNT(DISTINCT problemid) FROM submission WHERE email=?', parameter)
    rtnMessage2 = cursor.fetchone()
    parameter = (email, 'Accepted',)
    cursor.execute('SELECT COUNT(DISTINCT problemid) FROM submission WHERE email=? AND verdict = ?', parameter)
    rtnMessage3 = cursor.fetchone()

    return {"name": rtnMessage1[0], "email": rtnMessage1[1], "institution": rtnMessage1[2], "solved": rtnMessage3[0],
            "tried": rtnMessage2[0]}


# if count is False then will return all the submissions
# if count is True then will return last 30 submissions
# will return like an array of dictionary of course

def getSubmission(email, count=False):
    parameter = (email,)
    arrayDictionary = []
    cursor.execute('SELECT submissionid, problemid, verdict FROM submission WHERE email=?', parameter)
    if count:
        rtnMessage = cursor.fetchmany(30)
        for row in rtnMessage:
            arrayDictionary.append({"submissionid": row[0], "problemid": row[1], "verdict": row[2]})
        return arrayDictionary
    else:
        rtnMessage = cursor.fetchall()
        for row in rtnMessage:
            arrayDictionary.append({"submissionid": row[0], "problemid": row[1], "verdict": row[2]})
        return arrayDictionary


# returns all problems exactly like this (array of dictionary)
# [{"number" : "1", "problemid" : "1000", "name" : "Libir's Wisdom", "tag" : "Beginner", "solved" : }]

def all_problem(email):
    parameter = (email,)
    arrayDictionary = []
    cursor.execute('SELECT problems.problemid, problems.name, problems.tag, problems.solved FROM problems WHERE '
                   'problemid = (SELECT problemid FROM submission WHERE email = ? ) ', parameter)
    count = 1
    rtnMessage = cursor.fetchall()
    for row in rtnMessage:
        if row[3] > 0:
            arrayDictionary.append(
                {"number": count, "problemid": row[0], "name": row[1], "tag": row[2], "solved": "TRUE"})
        else:
            arrayDictionary.append(
                {"number": count, "problemid": row[0], "name": row[1], "tag": row[2], "solved": "FALSE"})

        ++count
    return arrayDictionary

# This function increment the tried field value by 1 for a particular problem
def updateTried(problemid):
    parameter = (problemid,)
    cursor.execute('UPDATE problems SET tried = tried + 1 WHERE problemid = ?', parameter)
    conn.commit()

# This function increment the solved field value by 1 for a particular problem
def updateSolved(problemid):
    parameter = (problemid,)
    cursor.execute('UPDATE problems SET solved = solved + 1 WHERE problemid = ?', parameter)
    conn.commit()
