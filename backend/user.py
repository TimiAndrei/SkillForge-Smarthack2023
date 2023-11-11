from datetime import date, timedelta
from skill import skill
from questlog import questLog

class user:
    levelThreshold = 6

    def __init__(self, fName, lName, accountName, password, email, organization, friendsList=[], points=0, lastFinished = date.today() + timedelta(days=-2), streak = 0, level=0, skillList=[], questList=[], needApproval = 0):
        self.fName = fName
        self.lName = lName
        self.accountName = accountName
        self.password = password
        self.email = email
        self.organization = organization
        self.friendsList = friendsList
        self.points = points
        self.lastFinished = lastFinished
        self.streak = streak
        self.level = level
        self.skillList = skillList
        self.questList = questList
        self.needApproval = needApproval

    def getName(self):
        return self.fName + " " + self.lName
    def get_accountName(self):
        return self.accountName
    def getOrganization(self):
        return self.organization
    def getfriendsList(self):
        return self.friendsList
    def getPoints(self):
        return self.points
    def getStreak(self):
        return self.streak
    def getLevel(self):
        return self.level
    def getEmail(self):
        return self.email
    def getCategories(self):
        uniqueCategories = []
        for item in self.skillList:
            if item.getCategory() not in uniqueCategories:
                uniqueCategories.append(item.getCategory())

        return uniqueCategories
    def resetStreak(self):
        if self.lastFinished < date.today() + timedelta(days=-2):
            self.streak = 0

    def authenticate(self, password):
        return self.password == password

    def addQuest(self, quest):
        self.questList.append(quest)

    def addSkill(self, skill):
        self.skillList.append(skill)
        
    def finishTask(self, task, percentage=100):
        if self.lastFinished == date.today() + timedelta(days=-1):
            self.streak += 1
            self.lastFinished = date.today()
        elif self.lastFinished < date.today() + timedelta(days=-1):
            self.streak = 0
            self.lastFinished = date.today()
        task.markAsDone(percentage)
        self.points += task.getPoints()

        self.level = self.points / 6

