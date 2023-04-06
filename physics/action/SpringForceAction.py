class SpringForceAction:
    
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
        
    def act(self,data):
        #Data is the particle entity state
        if self.conditionMet(data):
            totalMass = 0.0
            centerOfMass = [0.0,0.0]
            for i in range(0,len(data.acceleration)):
                if data.position[i][0] > 850:
                    data.activeParticle[i] = False
                elif data.position[i][0] <850:
                    data.activeParticle[i] = True
                if data.activeParticle[i]:
                    totalMass = totalMass + data.mass[i]
                    centerOfMass[0] = centerOfMass[0] + data.mass[i] * data.position[i][0]
                    centerOfMass[1] = centerOfMass[1] + data.mass[i] * data.position[i][1]
            centerOfMass[0] = centerOfMass[0]/totalMass
            centerOfMass[1] = centerOfMass[1]/totalMass
            
            for i in range(0,len(data.acceleration)):
                if data.activeParticle[i]:
                    accel = [0.0,0.0]
                    accel[0] = (centerOfMass[0] - data.position[i][0]) * self.entityState.springConstant / data.mass[i]
                    accel[1] = (centerOfMass[1] - data.position[i][1]) * self.entityState.springConstant / data.mass[i]
                    data.acceleration[i][0] = data.acceleration[i][0] + accel[0]
                    data.acceleration[i][1] = data.acceleration[i][1] + accel[1]
                data.activeParticle[i] = True
        for child in self.children:
            child.act(data)
        return
               