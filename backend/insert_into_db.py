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
                          lastFinished, streak, level, needApproval, email, password)
        VALUES ( ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    ''')

    for pair in nameUsernamePairs:
        signUpTime = date.today() - timedelta(days = random.randint(0, 100))
        cursor.execute(insertQuery, (pair[0], pair[1], pair[2], 
                                    "", "", 0, signUpTime, 0, 0, 0, pair[2] + "@gmail.com", "pass"))

    output = cursor.execute(''' 
            SELECT * FROM user;        
    ''')

    print(output.fetchall())

def insertQuestlogs():
    questLogData = [
            ["Master a New Language", "I aim to become proficient in a new language by practicing daily and engaging in conversations with native speakers."],
            ["Enhance Creativity", "I want to unleash my creative potential by dedicating time each day to artistic pursuits such as drawing, painting, or writing."],
            ["Become a Tech Guru", "I aspire to improve my technical skills by taking online courses and working on real-world coding projects to stay updated with the latest technologies."],
            ["Cultivate Mindfulness", "I am committed to practicing mindfulness and meditation regularly to reduce stress, enhance focus, and promote overall mental well-being."],
            ["Level Up Networking Skills", "I want to expand my professional network by attending industry events, joining relevant online communities, and initiating meaningful conversations."],
            ["Excel at Public Speaking", "I aim to conquer my fear of public speaking by participating in speaking clubs, seeking constructive feedback, and gradually taking on larger speaking engagements."],
            ["Achieve Financial Literacy", "I am determined to improve my financial knowledge by reading books, attending workshops, and actively managing my budget and investments."],
            ["Mastery in Cooking", "I want to enhance my culinary skills by learning new recipes, experimenting with diverse cuisines, and hosting regular dinner parties to share my creations."],
            ["Develop a Fitness Routine", "I plan to establish a consistent fitness routine by incorporating a variety of exercises, setting achievable fitness goals, and tracking my progress."],
            ["Bolster Emotional Intelligence", "I am dedicated to enhancing my emotional intelligence by actively listening, practicing empathy, and seeking opportunities for self-reflection."],
            ["Expand Photography Skills", "I want to become a proficient photographer by exploring various photography styles, learning advanced techniques, and capturing moments that tell compelling stories."],
            ["Master Time Management", "I aim to improve my productivity and time management skills by setting clear goals, prioritizing tasks, and minimizing distractions."],
            ["Improve Conflict Resolution Skills", "I aspire to become adept at resolving conflicts by studying conflict resolution strategies, practicing effective communication, and seeking resolutions in a calm and constructive manner."],
            ["Attain Expertise in a Hobby", "I want to become an expert in my chosen hobby by dedicating focused time to it regularly, seeking mentorship, and pushing the boundaries of my skills."],
            ["Enhance Leadership Abilities", "I am committed to developing strong leadership skills by taking on leadership roles, seeking feedback, and continuously learning about effective leadership practices."]
    ]

    insertQuery = ('''
        INSERT INTO questLog (name, description, 
                              userID)
        VALUES ( ?, ?, ?);
    ''')

    countToThree = 0
    userId = 0
    for pair in questLogData:
        cursor.execute(insertQuery, (pair[0], pair[1], userId))
        
        countToThree += 1
        if countToThree == 3:
            userId += 1
            countToThree = 0

    output = cursor.execute(''' 
            SELECT * FROM questLog;        
    ''')

    print(output.fetchall())

def insertSkills():
    taskData = [
        ["Learn 10 Random New Words", "Language Learning", "Learn 10 random new words from the dictionary to rapidly expand your vocabulary."],
        ["Full-day Language Immersion", "Language Practice", "Immerse yourself in the language for an entire day by engaging in conversations, watching movies, and reading articles exclusively in the target language."],
        ["Translate-a-thon", "Language Application", "Translate two articles or stories from your native language to the target language, honing your translation skills and reinforcing grammar and syntax."],

        ["Create 10 Detailed Sketches", "Artistic Expression", "Challenge yourself to create 10 detailed sketches, exploring various themes and pushing the boundaries of your creativity."],
        ["Write-a-Day Challenge", "Creative Writing", "Write a 1,000-word short story, experimenting with different genres and styles to enhance your creative writing skills."],
        ["Color Explosion Day", "Painting Exploration", "Experiment with a vibrant and unconventional color palette in a painting session, pushing the boundaries of your artistic expression."],

        ["Code Blitz Day", "Programming Practice", "Solve 20 coding challenges on a platform like LeetCode or HackerRank, strengthening your coding skills and problem-solving abilities."],
        ["App Development Sprint", "Application Development", "Embark on a coding sprint to build a small, practical application, applying the knowledge gained from online courses and implementing at least three key features."],
        ["Tech News Marathon", "Industry Awareness", "Fully immerse yourself in reading five tech blogs, attending two webinars, and summarizing the latest trends and technologies in a comprehensive report."],

        ["Meditation Marathon", "Mindfulness Practice", "Engage in a 2-hour meditation session followed by a 30-minute mindfulness walk in nature, focusing on your breath and promoting relaxation to reduce stress levels."],
        ["Breathwork Intensive", "Stress Reduction", "Go for a walk in the park, focusing on deep breathing exercises and mindfulness to promote relaxation and reduce stress levels."],
        ["Gratitude Day Journaling", "Positive Psychology", "Dedicate 2 hours to intensive gratitude journaling, reflecting on and appreciating 20 specific aspects of your life."],

        ["LinkedIn Blitz", "Online Networking", "Reach out to at least 10 new connections on LinkedIn, introducing yourself with personalized messages and expressing genuine interest in their work."],
        ["Networking Event Extravaganza", "In-person Networking", "Attend three networking events, actively engaging with at least five professionals at each event to broaden your connections."],
        ["Coffee Chat Marathon", "Professional Conversations", "Schedule and conduct a series of four 30-minute coffee chats with colleagues or industry professionals to build relationships and exchange insights."],

        ["Speech-a-Thon", "Public Speaking Practice", "Deliver a series of three speeches throughout the day, gradually increasing complexity and challenging yourself to speak on diverse topics."],
        ["Record and Reflect Day", "Self-Reflection", "Record three speeches, presentations, or monologues, then spend 1 hour reflecting on your delivery, identifying areas for improvement, and planning adjustments."],
        ["Debate Day", "Critical Thinking", "Participate in three debates or discussions throughout the day, refining your ability to think on your feet and articulate ideas persuasively."],

        ["Budget Mastery Day", "Financial Planning", "Thoroughly review and optimize your monthly budget, track income and expenses, and identify areas for financial improvement."],
        ["Investment Challenge", "Investment Knowledge", "Explore and simulate various investment strategies using a virtual trading platform, gaining practical insights into the world of investments."],
        ["Financial Literature Dive", "Educational Reading", "Immerse yourself in reading two books on personal finance and investment, deepening your understanding of financial concepts."],

        ["Global Cuisine Day", "Culinary Exploration", "Choose a specific international cuisine and spend the day preparing a multi-course meal with at least three dishes, mastering various cooking techniques."],
        ["Perfect Dessert Day", "Baking Skills", "Focus on perfecting a challenging dessert recipe, refining your baking techniques and presenting the dessert in an aesthetically pleasing manner."],
        ["Epic Dinner Party", "Social Cooking", "Plan and host an elaborate dinner party, showcasing your culinary skills and sharing the joy of good food with at least eight friends and family members."],

        ["Personalized Workout Creation", "Exercise Planning", "Design a personalized workout routine, incorporating various exercises to address cardiovascular fitness, strength, and flexibility."],
        ["Fitness Class Marathon", "Variety in Exercise", "Explore three different fitness classes, from yoga to kickboxing, to keep your workouts diverse and engaging."],
        ["Fitness Goal Sprint", "Goal Setting", "Set and achieve three challenging fitness goals, tracking and celebrating your achievements."],

        ["Active Listening Marathon", "Communication Skills", "Engage in a series of five conversations throughout the day, focusing specifically on active listening and understanding others' perspectives."],
        ["Empathy Day", "Real-world Empathy", "Participate in four hours of volunteer activities or community service to actively practice empathy in real-world scenarios."],
        ["Reflective Journal Marathon", "Self-awareness", "Devote an entire day to reflective journaling, exploring your own emotions, reactions, and personal growth through detailed self-reflection."],

        ["Photo-a-Day Deep Dive", "Daily Photography", "Capture and share 10 photographs, experimenting with composition, lighting, and subject matter to enhance your photography skills."],
        ["Advanced Editing Session", "Post-Processing Skills", "Spend a day mastering three advanced photo editing techniques using software like Adobe Lightroom or Photoshop."],
        ["Photography Critique Marathon", "Peer Feedback", "Join an online photography community and share five photographs for constructive feedback within a single day."],

        ["Priority Power Hour", "Task Prioritization", "Dedicate a focused hour to prioritize tasks, emphasizing high-impact activities for better time management."],
        ["Time Blocking Experiment", "Scheduling Mastery", "Experiment with time blocking to allocate specific time slots to different tasks and enhance productivity."],
        ["Weekly Review Blitz", "Self-assessment", "Conduct an intensive weekly review, evaluating achievements, identifying areas for improvement, and adjusting goals accordingly."],

        ["Role-playing Intensive", "Interactive Learning", "Engage in a day-long session of role-playing scenarios to simulate conflicts and practice various resolution strategies."],
        ["Feedback Day", "Feedback Loop", "Proactively seek feedback from at least three colleagues or friends on your conflict resolution approach, dedicating a day to improvement."],
        ["Conflict Analysis Day", "Reflective Practice", "Spend a day analyzing two past conflicts in a conflict journal, identifying patterns and strategizing for improvement."],

        ["Focused Skill Masterclass", "Skill Refinement", "Select a specific advanced skill or technique and spend a dedicated day mastering it through focused practice and experimentation."],
        ["Day with a Hobby Expert", "Learning from Experts", "Arrange a day to shadow or spend at least six hours with an expert in your hobby, absorbing their insights and knowledge."],
        ["Community Project Immersion", "Collaborative Creation", "Participate in an intensive day-long session of a community project, collaborating with others to contribute your skills and learn from diverse perspectives."],

        ["Team Leadership Day", "Project Leadership", "Lead a team through a day-long project, applying leadership principles to guide and motivate team members toward a common goal."],
        ["Conflict Resolution Workshop Intensive", "Leadership Training", "Attend a day-long conflict resolution workshop, gaining in-depth insights and practicing resolving conflicts in various scenarios."],
        ["Leadership Book Marathon", "Leadership Development", "Dedicate an entire day to an in-depth study of a leadership book, extracting key insights and strategies for immediate implementation in your leadership approach."]
    ]

    insertQuery = ('''
        INSERT INTO skill (name, category, description, 
                           difficulty, deadline, creationDate, points, approval, questLogID)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    ''')

    countToThree = 0
    questLogID = 0
    for pair in taskData:
        creationDate = date.today() - timedelta(days = random.randint(50, 100))
        deadline = date.today() + timedelta(days = random.randint(-20, 60))

        cursor.execute(insertQuery, (pair[0], pair[1], pair[2], random.randint(1, 3), deadline, creationDate, 0, 0, questLogID))
        
        countToThree += 1
        if countToThree == 3:
            questLogID += 1
            countToThree = 0

    output = cursor.execute(''' 
            SELECT * FROM skill;        
    ''')

    print(output.fetchall())


def menu():
    userInput = 0
    while userInput != 4:
        userInput = int(input("1 to insert Users\n2 to insert Questlogs\n3 to insert Tasks\n"))
        if userInput == 1:
            insertUsers()
        if userInput == 2: 
            insertQuestlogs()
        if userInput == 3:
            insertSkills()
        


menu()

conn.commit()
conn.close()
