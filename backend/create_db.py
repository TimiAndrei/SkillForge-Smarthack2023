import sqlite3


def main():
    conn = sqlite3.connect('SHDB.db')
    cursor = conn.cursor()

    cursor.execute('''
            DROP TABLE IF EXISTS user;
    ''')

    cursor.execute('''
            CREATE TABLE user (
                userID INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName TEXT,
                lastName TEXT,
                email TEXT UNIQUE,
                password TEXT,
                accountName TEXT UNIQUE,
                organization TEXT,
                friendsList TEXT,
                points INTEGER,
                lastFinished DATE,
                streak INTEGER,
                level INTEGER,
                needApproval INTEGER
            );
        ''')

    cursor.execute('''
            DROP TABLE IF EXISTS questLog;
    ''')

    cursor.execute('''
            CREATE TABLE questLog (
                questLogID INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                skillList TEXT,
                userID INTEGER,
                FOREIGN KEY (userID) REFERENCES user (userID)
            );
        ''')

    # Function to create the Skill table
    cursor.execute('''
            DROP TABLE IF EXISTS skill;
    ''')

    cursor.execute('''
            CREATE TABLE skill (
                skillID INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                category TEXT,
                difficulty INTEGER,
                description TEXT,
                deadline DATE,
                creationDate DATE,
                points INTEGER,
                approval INTEGER,
                questLogID INTEGER,
                FOREIGN KEY (questLogID) REFERENCES questLog (questLogID)
            );
    ''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
