from skill import skill
from datetime import date, timedelta

class questLog():

    def __init__(self, _name, _description = ""):
        self.name = _name
        self.description = _description
        self.skillList = []

    def addSkill(self, skill):
        self.skillList.append(skill)
        return skill

    def removeSkill(self, skill):
        self.skillList.remove(skill)

    def getSkills(self):
        return self.skillList 

    def getProgress(self):
        currentProgress = 0
        maxProgress = 0
        
        for currentSkill in self.skillList:
            currentProgress += min(currentSkill.getDifficulty(), currentSkill.getPoints())
            maxProgress += currentSkill.getDifficulty() 
        
        return 100 * currentProgress/maxProgress 

    def getDificultyPercentages(self):
        # percentages[0] represents the percentage of easy, but easy returns 1 point so difficulty - 1 = indice of percetages
        toSkillPosition = 1
        
        # easy medium hard averageOfAverages
        percentages = [0, 0, 0]

        # get number of tasks in each cathegory
        for currentSkill in self.skillList:
            percentages[currentSkill.getDifficulty() - toSkillPosition] += 1
        
        numberOfSkills = len(self.skillList)

        for i in range(0, 3):
            percentages[i] = 100.0 * percentages[i] / numberOfSkills

        return percentages
    
difficulty = {"easy":1, "medium":2, "hard":3}


qlog = questLog("ciclism", "merg pe bicicleta si ma simt bine")
qlog.addSkill(skill("learn Smoke On The Water on guitar", "music", difficulty["easy"], "Most basic song", date.today() + timedelta(days=2), date.today() + timedelta(days=-2)))
obj = qlog.addSkill(skill("write a cook-book", "cooking", difficulty["hard"], "a dream that must come true", date.today(), date.today() + timedelta(days=-10)))
qlog.addSkill(skill("write another cook-book", "cooking", difficulty["hard"], "another dream that must come true", date.today(), date.today() + timedelta(days=-10)))
qlog.removeSkill(obj)
print(qlog.getSkills())
