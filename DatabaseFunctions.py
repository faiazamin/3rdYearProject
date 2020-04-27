# Code by: Faiaz Amin Khan


import sqlite3




# will check if the email is not already in the database
# if in the database then returns None
# if valid email then makes new entry at the database for it having isverified field false
# returns email if everything is done perfectly

def signup(name, email, institution, password):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    checkmail = (email,)
    cursor.execute('SELECT email FROM user WHERE email=?', checkmail)
    checkRtn = cursor.fetchone()
    if checkRtn == None:
        insertValues = (name, email, institution, password, 0,)
        cursor.execute('INSERT INTO user VALUES (?,?,?,?,?)', insertValues)
        conn.commit()
        conn.close()
        return email
    else:
        conn.commit()
        conn.close()
        return None


# checks if email, pass is true for an entry and also it is verified
# if fine then returns email
# else returns None

def signin(email, password):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    parameter = (email, password,)
    cursor.execute('SELECT isverified FROM user WHERE email = ? AND password = ?', parameter)
    rtnMessage = cursor.fetchone()
    conn.commit()
    conn.close()
    if(rtnMessage == None or rtnMessage[0] == 0):
        return None
    return email


# makes isVerified field True
# returns nothing

def verifyUser(email):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()
    parameter = (email,)
    cursor.execute('UPDATE user SET isverified = 1 WHERE email = ?', parameter)
    conn.commit()
    conn.close()

# will return the {name} for an email

def getNameAgainstEmail(email):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    parameter = (email,)
    cursor.execute('SELECT name FROM user WHERE email = ?', parameter)
    rtnMessage = cursor.fetchone()
    conn.commit()
    conn.close()
    return rtnMessage[0];


# will change the verdict for submissionid
# returns nothing
# increment the solved field value by 1 for that problem if verdict is 'Accepted'

def changeVerdict(submissionid, verdict):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    parameter = (verdict, submissionid,)
    cursor.execute('UPDATE submission SET verdict = ? WHERE submissionid = ?', parameter)
    if verdict == 'Accepted':
        parameter = (submissionid,)
        cursor.execute('SELECT problemid FROM submission WHERE submissionid = ?', parameter)
        problemid = cursor.fetchone()
        updateSolved(problemid[0])
    conn.commit()
    conn.close()

# will create new entry for email and problemid
# verdict will be "Not Judged Yet"
# will return the submissionid of the new entry
# increment the tried field value by 1 for that problem

def newSubmission(email, problemid):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    parameter = ("Not Judged Yet", problemid, email,)
    cursor.execute('INSERT INTO submission (verdict,problemid,email) VALUES (?,?,?)', parameter)
    conn.commit()
    cursor.execute('SELECT submissionid FROM submission WHERE verdict=? AND problemid=? AND email=?', parameter)
    rtnMessage = cursor.fetchone()
    updateTried(problemid)
    conn.commit()
    conn.close()
    return rtnMessage[0]


# returns a dictionary exactly like down one {"name":"Rahat Hossain", "email" : "rahathossain690@gmail.com",
# "instritution" : "Univerisity of Dhaka", "solve" : "2", "tried" : "2"}

def userData(email):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    parameter = (email,)
    cursor.execute('SELECT name,email,institution FROM user WHERE email=?', parameter)
    rtnMessage1 = cursor.fetchone()
    cursor.execute('SELECT COUNT(DISTINCT problemid) FROM submission WHERE email=?', parameter)
    rtnMessage2 = cursor.fetchone()
    parameter = (email, 'Accepted',)
    cursor.execute('SELECT COUNT(DISTINCT problemid) FROM submission WHERE email=? AND verdict = ?', parameter)
    rtnMessage3 = cursor.fetchone()
    conn.commit()
    conn.close()

    return {"name": rtnMessage1[0], "email": rtnMessage1[1], "institution": rtnMessage1[2], "solved": rtnMessage3[0],
            "tried": rtnMessage2[0]}


# if count is False then will return all the submissions
# if count is True then will return last 30 submissions
# will return like an array of dictionary of course

def getSubmission(email, count=False):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    parameter = (email,)
    arrayDictionary = []
    cursor.execute('SELECT submissionid, problemid, verdict FROM submission WHERE email=?', parameter)
    conn.commit()
    conn.close()
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
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()
    parameter = (email,)
    arrayDictionary = []
    cursor.execute('SELECT * FROM problems')
    count = 1
    rtnMessage1 = cursor.fetchall()
    cursor.execute('SELECT problemid, verdict FROM submission WHERE email=?', parameter)
    rtnMessage2 = cursor.fetchall()
    cp_bro = {}
    for item in rtnMessage2:
        current = cp_bro.get(item[0])
        if current == None:
            if item[1] == 'Accepted':
                cp_bro[item[0]] = 2
            else:
                cp_bro[item[0]] = 1
        elif current == 2:
            continue
        else:
            if item[1] == 'Accepted':
                cp_bro[item[0]] = 2
    conn.commit()
    conn.close()
    for row in rtnMessage1:
        haha = {"number": count, "problemid": row[0], "name": row[1], "tag": row[2], "solved": row[3], "tried" : row[4], "timelimit" : row[5], "memorylimit" : row[6]}
        if cp_bro.get(row[0]) == 2:
            haha["has_solved"] = 2
        elif cp_bro.get(row[0]) == 1:
            haha["has_solved"] = 1
        else:
            haha["has_solved"] = 0
        count += 1
        arrayDictionary.append(haha)
    return arrayDictionary
    # for row in rtnMessage:
    #     if row[3] > 0:
    #         arrayDictionary.append(
    #             {"number": count, "problemid": row[0], "name": row[1], "tag": row[2], "solved": "TRUE"})
    #     else:
    #         arrayDictionary.append(
    #             {"number": count, "problemid": row[0], "name": row[1], "tag": row[2], "solved": "FALSE"})

    #     ++count
    # return arrayDictionary


# def all_problem(email):
#     conn = sqlite3.connect('database/judge.db')
#     cursor = conn.cursor()
#     parameter = (email,)
#     cursor.execute('SELECT * FROM problems')
#     rtnMessage = cursor.fetchall()
#     conn.commit()
#     conn.close()
#     print(rtnMessage)

# This function increment the tried field value by 1 for a particular problem
def updateTried(problemid):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    parameter = (problemid,)
    cursor.execute('UPDATE problems SET tried = tried + 1 WHERE problemid = ?', parameter)
    conn.commit()
    conn.close()

# This function increment the solved field value by 1 for a particular problem
def updateSolved(problemid):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    parameter = (problemid,)
    cursor.execute('UPDATE problems SET solved = solved + 1 WHERE problemid = ?', parameter)
    conn.commit()
    conn.close()


# This function returns the solved field value for a particular problem
def getSolvedCount(problemid):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    parameter = (problemid,)
    cursor.execute('SELECT solved FROM problems WHERE problemid = ?', parameter)
    conn.commit()
    conn.close()
    return cursor.fetchone();


# This function returns the tried field value for a particular problem
def getTriedCount(problemid):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()

    parameter = (problemid,)
    cursor.execute('SELECT tried FROM problems WHERE problemid = ?', parameter)
    conn.commit()
    conn.close()
    return cursor.fetchone()

def get_problem_data(problemid):
    conn = sqlite3.connect('database/judge.db')
    cursor = conn.cursor()
    parameter = (problemid,)
    cursor.execute('SELECT timelimit, memorylimit FROM problems WHERE problemid = ?', parameter)
    conn.commit()
    conn.close()
    rtnMessage = cursor.fetchone()
    data = {"time_limit" : int(rtnMessage[0]), "memory_limit" : int(rtnMessage[1])}
    return data