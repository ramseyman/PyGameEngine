class GravityForceAction:

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
                if data.activeParticle[i]:
                    data.acceleration[i][0] = data.acceleration[i][0] + self.entityState.gravity[0]
                    data.acceleration[i][1] = data.acceleration[i][1] + self.entityState.gravity[1]
        for child in self.children:
                child.act(data)
        return