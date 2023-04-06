class PickPositionAction:

    def __init__(self,index):
        self.types = ["position"]
        self.particleIndex = index
        self.entityState = None
        self.children = []
        
    def conditionMet(self, data):
        if self.entityState == None:
            return False
        if self.entityState.active == False:
            return False
        if self.particleIndex >= len(self.entityState.position):
            return False
        if self.entityState.activeParticle[self.particleIndex] == False:
            return False
        return True
        
    def act(self, data):
        if self.conditionMet(data):
            newData = list(self.entityState.position[self.particleIndex])
            for child in self.children:
                child.act(newData)
        return