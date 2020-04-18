import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()


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


def signin(email, password):
    parameter = (email, password,)
    cursor.execute('SELECT isverified FROM user WHERE email = ? AND password = ?', parameter)
    rtnMessage = cursor.fetchone()
    if rtnMessage == 1:
        return email
    else:
        return None


def verifyUser(email):
    parameter = (email,)
    cursor.execute('UPDATE user SET isverified = 1 WHERE email = ?', parameter)
    conn.commit()


def getNameAgainstEmail(email):
    parameter = (email,)
    cursor.execute('SELECT name FROM user WHERE email = ?', parameter)
    rtnMessage = cursor.fetchone()
    return rtnMessage[0];


def changeVerdict(submissionid, verdict):
    parameter = (verdict, submissionid,)
    cursor.execute('UPDATE submission SET verdict = ? WHERE submissionid = ?', parameter)
    conn.commit()


def newSubmission(email, problemid):
    parameter = ("Not Judged Yet", problemid, email,)
    cursor.execute('INSERT INTO submission VALUES (?,?,?)', parameter)
    conn.commit()
    cursor.execute('SELECT submissionid FROM submission WHERE verdict=? AND problemid=? AND email=?', parameter)
    rtnMessage = cursor.fetchone()
    return rtnMessage[0]


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


def all_problem(email):
    parameter = (email,)
    arrayDictionary = []
    cursor.execute('SELECT problems.problemid, problems.name, problems.tag, problems.solved FROM problems WHERE '
                   'problemid = (SELECT problemid FROM submission WHERE email = ? ) ', parameter)
    count = 1
    rtnMessage = cursor.fetchall()
    for row in rtnMessage:
        if row[3]>0:
            arrayDictionary.append(
                {"number": count, "problemid": row[0], "name": row[1], "tag": row[2], "solved": "TRUE"})
        else:
            arrayDictionary.append(
                {"number": count, "problemid": row[0], "name": row[1], "tag": row[2], "solved": "FALSE"})

        ++count
    return arrayDictionary


def updateTried( problemid ):
    parameter = (problemid,)
    cursor.execute('UPDATE problems SET tried = tried + 1 WHERE problemid = ?',parameter)
    conn.commit()


def updateSolved( problemid ):
    parameter = (problemid,)
    cursor.execute('UPDATE problems SET solved = solved + 1 WHERE problemid = ?',parameter)
    conn.commit()
