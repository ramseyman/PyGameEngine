class EulerSolveAction:
    
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
        if len(self.children) < 2:
            return False
        return True
        
    def act(self,data):
        if self.conditionMet(data):
            #Children used for the solve
            self.children[0].dt = float(self.dt)
            self.children[1].dt = float(self.dt)
            self.children[0].act(data)
            self.children[1].act(data)
            #Remaining children actions
            for child in self.children[2:]:
                child.act(data)
        return