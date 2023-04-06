class DragForceAction:

    def __init__(self):
        self.types = ["force"]
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
        
    def act(self, data):
        #Data is particle entity state
        if self.conditionMet(data):
            for i in range(0,len(data.acceleration)):
                if data.position[i][0] < 850:
                    data.activeParticle[i] = False
                if data.activeParticle[i]:
                    data.acceleration[i][0] = data.acceleration[i][0] - data.velocity[i][0] * self.entityState.dragConstant
                    data.acceleration[i][1] = data.acceleration[i][1] - data.velocity[i][1] * self.entityState.dragConstant
                data.activeParticle[i] = True
        for child in self.children:
                child.act(data)
        return