from datetime import date, timedelta
from skill import skill
from questlog import questLog

class user:
    def __init__(self, fName, lName, accountName, organization, friendsList=[], points=0, skillList=[], questList=[], needApproval = 0):
        self.fName = fName
        self.lName = lName
        self.accountName = accountName
        self.organization = organization
        self.friendsList = friendsList
        self.points = points
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

    def addQuest(self, quest):
        questList.append(quest)
    def addSkill(self, skill):
        self.skillList.append(skill)
    def finishTask(self, task, percentage=100):
        task.markAsDone(percentage)
        self.points += task.getPoints()

