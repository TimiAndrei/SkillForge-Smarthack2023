import sqlite3
conn = sqlite3.connect('SHDB.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            userID INTEGER PRIMARY KEY,
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
            skillID INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            difficulty INTEGER,
            description TEXT,
            deadline DATE,
            creationDate DATE,
            points INTEGER,
            approval INTEGER,
            FOREIGN KEY (questLogId)
                REFERENCES questLog (questLogID)
               
        )
    ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS questLog (
            questLogID INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            skillList TEXT,
            FOREIGN KEY (userID)
                REFERENCES user (userID)
        )
    ''')


conn.commit()
conn.close()
