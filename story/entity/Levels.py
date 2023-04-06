class Levels:
    
    def __init__(self):
        self.entities = []
        self.goals = []
        self.numGoals = []
        self.difficulty = []
        self.actions = []
        return
    
    def insertAction(self, action):
        action.entityState = self
        self.actions.append(action)
        return
        
    def addLevel(self, newGoals, newDifficulty, newNum):
        self.goals.append(newGoals)
        self.difficulty.append(newDifficulty)
        self.numGoals.append(newNum)