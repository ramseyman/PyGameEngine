class VelocitySolveAction:
    
    def __init__(self):
        self.types = ["physics"]
        self.entityState = None
        self.dt = 1.0
        self.children = []
        
    def conditionMet(self,data):
        if self.entityState == None:
            return False
        if self.entityState.active == False:
            return False
        return True
        
    def act(self,data):
        if self.conditionMet(data):
            for i in range(0, len(self.entityState.acceleration)):
                if self.entityState.activeParticle[i]:
                    self.entityState.acceleration[i][0] = 0.0
                    self.entityState.acceleration[i][1] = 0.0
            # Children solve for acceleration using forces
            for child in self.children:
                child.act(self.entityState)
            for i in range(0,len(self.entityState.velocity)):
                if self.entityState.activeParticle[i]:
                    self.entityState.velocity[i][0] = self.entityState.velocity[i][0] + self.dt * self.entityState.acceleration[i][0]
                    self.entityState.velocity[i][1] = self.entityState.velocity[i][1] + self.dt * self.entityState.acceleration[i][1]
        return