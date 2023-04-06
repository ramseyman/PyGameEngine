class OutsideRectangleCollisionAction:

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
                    if data.position[i][0] > self.entityState.llc[0] and data.position[i][0]< self.entityState.urc[0]:
                        if data.position[i][1] > self.entityState.llc[1] and data.position[i][1] < self.entityState.urc[1]:
                            rightTime = (data.position[i][0] - self.entityState.llc[0])/data.velocity[i][0]
                            if rightTime < 0.0:
                                rightTime = 1000000.0
                            leftTime = (data.position[i][0] - self.entityState.urc[0])/data.velocity[i][0]
                            if leftTime < 0.0:
                                leftTime = 1000000.0
                            topTime = (data.position[i][1] - self.entityState.llc[1])/data.velocity[i][1]
                            if topTime < 0.0:
                                topTime = 1000000.
                            bottomTime = (data.position[i][1] - self.entityState.urc[1])/data.velocity[i][1]
                            if bottomTime < 0.0:
                                bottomTime = 1000000.0
                            minTime = min(rightTime,leftTime,topTime,bottomTime)
                            if rightTime == minTime:
                                data.position[i][0] = 2.0*self.entityState.llc[0] - data.position[i][0]
                                data.velocity[i][0] = -data.velocity[i][0]
                            elif leftTime == minTime:
                                data.position[i][0] = 2.0*self.entityState.urc[0] - data.position[i][0]
                                data.velocity[i][0] = -data.velocity[i][0]
                            elif topTime == minTime:
                                data.position[i][1] = 2.0*self.entityState.llc[1] - data.position[i][1]
                                data.velocity[i][1] = -data.velocity[i][1]
                            elif bottomTime == minTime:
                                data.position[i][1] = 2.0*self.entityState.urc[1] - data.position[i][1]
                                data.velocity[i][1] = -data.velocity[i][1]
            for child in self.children:
                child.act(data)
        return