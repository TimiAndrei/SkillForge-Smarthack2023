import sqlite3
conn = sqlite3.connect('SHDB.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            fName TEXT,
            lName TEXT,
            accountName TEXT,
            organization TEXT,
            friendsList TEXT,
            points INTEGER,
            lastFinished DATE,
            streak INTEGER,
            level INTEGER,
            skillList TEXT,
            questList TEXT,
            needApproval INTEGER
        )
    ''')

# Function to create the Skill table
cursor.execute('''
        CREATE TABLE IF NOT EXISTS skill (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            difficulty INTEGER,
            description TEXT,
            deadline DATE,
            creationDate DATE,
            points INTEGER,
            approval INTEGER
        )
    ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS questLog (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            skillList TEXT
        )
    ''')


conn.commit()
conn.close()
