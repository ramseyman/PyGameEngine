class IsInsideAction:

    def __init__(self):
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
            result = withinBounds(data)
        for child in self.children:
            child.act(data)
        return result
    
    def withinBounds(self, pos):
        if pos[0] < self.entityState.bounds[0]:
            return False
        if pos[0] > self.entityState.bounds[2] +self.entityState.bounds[0]:
            return False
        if pos[1] < self.entityState.bounds[1]:
            return False
        if pos[1] > self.entityState.bounds[3] + self.entityState.bounds[1]:
            return False
        return True