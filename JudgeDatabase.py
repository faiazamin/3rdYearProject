import sqlite3

CONNECTION = sqlite3.connect('judge.db')

CURSOR = CONNECTION.cursor()

CURSOR.execute('''CREATE TABLE user (
    name TEXT NOT NULL,
    email TEXT NOT NULL PRIMARY KEY,
    institution TEXT NOT NULL,
    password TEXT NOT NULL,
    isverified INTEGER DEFAULT 0 NOT NULL
)
''')

CURSOR.execute('''CREATE TABLE problems (
    problemid TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL ,
    tag TEXT NOT NULL,
    solved INTEGER DEFAULT 0 NOT NULL,
    tried INTEGER DEFAULT 0 NOT NULL
)
''')

CURSOR.execute('''CREATE TABLE submission ( 
    submissionid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    verdict TEXT NOT NULL, 
    problemid TEXT NOT NULL, 
    email TEXT NOT NULL,
    FOREIGN KEY(email) REFERENCES user(email),
    FOREIGN KEY(problemid) REFERENCES problems(problemid))''')

CONNECTION.commit()

CONNECTION.close()