class PositionSolveAction:

    def __init__(self):
        self.types = ["physics"]
        self.entityState = None
        self.dt = 1.0
        self.children = []
        
    def conditionMet(self, data):
        if self.entityState == None:
            return False
        if self.entityState.active == False:
            return False
        return True
        
    def act(self, data):
        if self.conditionMet(data):
            for i in range(0,len(self.entityState.position)):
                if self.entityState.activeParticle[i]:
                    self.entityState.position[i][0] = self.entityState.position[i][0] + self.dt * self.entityState.velocity[i][0]
                    self.entityState.position[i][1] = self.entityState.position[i][1] + self.dt * self.entityState.velocity[i][1]
            for child in self.children:
                child.act(self.entityState)
        return 