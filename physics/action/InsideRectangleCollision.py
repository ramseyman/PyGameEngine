class InsideRectangleCollisionAction:

    def __init__(self):
        self.types = ["physics"]
        self.entityState = None
        self.children = []
        
    def conditionMet(self,data):
        if self.entityState == None:
            return False
        if self.entityState.active == False:
            return False
        if data == None:
            return False
        return True
        
    def act(self,data):
        if self.conditionMet(data):
            for i in range(0,len(data.position)):
                if data.activeParticle[i]:
                    if data.position[i][0] < self.entityState.llc[0]:
                        data.position[i][0] = 2.0*self.entityState.llc[0] - data.position[i][0]
                        data.velocity[i][0] = -data.velocity[i][0]
                    if data.position[i][0] > self.entityState.urc[0]:
                        data.position[i][0] = 2.0*self.entityState.urc[0] - data.position[i][0]
                        data.velocity[i][0] = -data.velocity[i][0]
                    if data.position[i][1] < self.entityState.llc[0]:
                        data.position[i][1] = 2.0*self.entityState.llc[1] - data.position[i][1]
                        data.velocity[i][1] = -data.velocity[i][1]
                    if data.position[i][1] > self.entityState.urc[1]:
                        data.position[i][1] = 2.0*self.entityState.urc[1] - data.position[i][1]
                        data.velocity[i][1] = -data.velocity[i][1]
            for child in self.children:
                child.act(data)
        return