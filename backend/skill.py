from datetime import date, timedelta
from math import floor

class skill:

    dificulty = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    def __init__(self, name="Default Name", category="Default Category", difficulty=1, description="Default Description", deadline=date.today(), creationDate=date.today(), points=0):
        self.name = name
        self.category = category
        self.difficulty = difficulty
        self.description = description
        self.deadline = deadline
        self.creationDate = creationDate
        self.points = points

        print("Created Skill " + self.name)

    def getName(self):
        return self.name
    def getCategory(self):
        return self.category
    def getDifficulty(self):
        return self.difficulty
    def getDescription(self):
        return self.description
    def getDeadline(self):
        return self.deadline
    def getCreationDate(self):
        return self.creationDate
    def getPoints(self):
        return self.points
    def isDone(self):
        return self.points != 0

    def getSkill(self):
        skillDict = {
            "name": self.name,
            "category": self.category,
            "difficulty": self.difficulty,
            "description": self.description,
            "deadline": self.deadline
        }
        return skillDict

    def markAsDone(self, percentage=100):
        points = (percentage / 100) * self.difficulty

        if percentage == 100:
            duration = self.deadline - self.creationDate
            daysToDeadline = self.deadline - date.today()
            usedDaysPercentage = floor(daysToDeadline.days * 100.0 / duration.days)

            if usedDaysPercentage > 100:
                points -= min(0.5, usedDaysPercentage / 100.0 - 1)

            elif usedDaysPercentage < 100:
                points += min(0.5, usedDaysPercentage / 100.0)

        self.points = points


testus = skill("Testus", "Test", 1, "Test", date.today() + timedelta(days=-2), date.today() + timedelta(days=-10))

testus.markAsDone(100)

print(testus.getDeadline())
print(testus.getPoints())