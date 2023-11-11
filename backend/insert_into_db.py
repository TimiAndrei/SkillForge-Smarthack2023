import sqlite3
import random
from datetime import date, timedelta

conn = sqlite3.connect('SHDB.db')
cursor = conn.cursor()

def insertUsers():
    nameUsernamePairs = [
        ["Ethan", "Smith", "EthanSmith123"],
        ["Olivia", "Johnson", "OliviaJ21"],
        ["Liam", "Williams", "LiamWills"],
        ["Emma", "Brown", "EmBrownie"],
        ["Noah", "Jones", "NoahJ45"],
        ["Ava", "Davis", "AvaDav"],
        ["Sophia", "Miller", "SophMiller89"],
        ["Jackson", "Taylor", "JackTaylor22"],
        ["Mia", "Anderson", "MiaAnder123"],
        ["Lucas", "Moore", "LucasMoo"],
        ["Isabella", "Jackson", "BellaJack56"],
        ["Carter", "White", "CarterWhiz"],
        ["Amelia", "Harris", "AmeliaHarr"],
        ["Logan", "Martin", "LoganMarti"],
        ["Evelyn", "Thompson", "EveThomp88"],
        ["Aiden", "Clark", "AidenC21"],
        ["Harper", "Lewis", "HarperLew"],
        ["Mason", "Hall", "MasonHall99"],
        ["Grace", "Walker", "GraceWalk1"],
        ["Elijah", "Allen", "EliAll78"],
        ["Chloe", "Young", "ChloeY99"],
        ["Oliver", "Wright", "OllieWri45"],
        ["Charlotte", "Scott", "CharScott22"],
        ["Liam", "Adams", "LiamAdams7"],
        ["Avery", "Nelson", "AveryNel88"],
        ["Benjamin", "Carter", "BenCarter34"],
        ["Mia", "Fisher", "MiaFish22"],
        ["Elijah", "Baker", "EliBake67"],
        ["Scarlett", "Cooper", "ScarCoop12"],
        ["Henry", "Ross", "HenryRoss55"],
        ["Aria", "Howard", "AriaHowa44"],
        ["Ethan", "Garcia", "EthanGar99"],
        ["Hazel", "Cruz", "HazelCruz21"],
        ["Sebastian", "Reed", "SebReed11"],
        ["Luna", "Evans", "LunaEvans8"],
        ["Jack", "Perry", "JackPerry66"],
        ["Madison", "Hill", "MadiHill34"],
        ["Wyatt", "Barnes", "WyattBarn23"],
        ["Ella", "Morris", "EllaMorr89"],
        ["Caleb", "Simmons", "CalebSim22"],
        ["Stella", "Ford", "StellaFord12"],
        ["James", "Woods", "JamesWoo45"],
        ["Penelope", "Murray", "PennyMurr88"],
        ["Gavin", "Fletcher", "GavinFlet67"],
        ["Aubrey", "Perez", "AubPerez21"],
        ["Daniel", "Russell", "DanRuss89"],
        ["Zoe", "Ferguson", "ZoeFerg44"],
        ["Owen", "Stewart", "OwenStew33"],
        ["Avery", "Griffin", "AveryGrif12"],
        ["Leah", "Harrison", "LeahHarr77"]
    ]

    insertQuery = ('''
        INSERT INTO user (firstName, lastName, accountName, organization, friendsList, points, 
                          lastFinished, streak, level, skillList, questList, needApproval)
        VALUES ( ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    ''')

    for pair in nameUsernamePairs:
        signUpTime = date.today() - timedelta(days = random.randint(0, 100))
        cursor.execute(insertQuery, (pair[0], pair[1], pair[2], 
                                    "", "", 0, signUpTime, 0, 0, "", "", 0))

    output = cursor.execute(''' 
            SELECT * FROM user;        
    ''')

    print(output.fetchall())

def insertQuestlogs():
    questLogData =[

    ]

    insertQuery = ('''
        INSERT INTO questLog (name, description, skillList, userID)
        VALUES ( ?, ? ,?, ?);
    ''')

    for pair in questLogData:
        signUpTime = date.today() - timedelta(days = random.randint(0, 100))
        cursor.execute(insertQuery, (pair[0], pair[1], pair[2])) 

    output = cursor.execute(''' 
            SELECT * FROM user;        
    ''')

    print(output.fetchall())
    return

def insertTasks():
    return

def menu():
    userInput = 0
    while userInput != 4:
        userInput = int(input("1 to insert Users\n2 to insert Questlogs\n3 to insert Tasks\n"))
        if userInput == 1:
            insertUsers()
        if userInput == 2: 
            insertQuestlogs()
        if userInput == 3:
            insertTasks()


menu()

conn.commit()
conn.close()
