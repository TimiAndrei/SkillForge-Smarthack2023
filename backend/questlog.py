class questLog():

    def __init__(self, _name, _description = ""):
        self.name = _name
        self.description = _description
        self.skillList = []

    def addSkill(self, skill):
        self.skillList.append(skill)
    
    def removeSkill(self, skill):
        self.skillList.remove(skill)

    def getSkills(self):
        return self.skillList 

    def getProgress(self):
        currentProgress = 0
        maxProgress = 0
        
        for currentSkill in self.skillList:
            currentProgress += min(currentProgress.getDifficulty(), currentProgress.getPoints())
            maxProgress += currentSkill.getDifficulty() 
        
        return currentProgress/maxProgress 

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
    

qlog = questLog("ciclism", "merg pe bicicleta si ma simt bine")
qlog.addSkill("merg repede")
print(qlog.name, qlog.description, qlog.getSkills())
