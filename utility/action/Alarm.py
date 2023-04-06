class AlarmAction():
    def __init__(self, allowed):
        self.types = []
        self.entityState = None
        self.children = []
        self.allowed = allowed
        return 
        
    def conditionMet(self):
        if self.entityState == None:
            return False
        #Check if elapsed time has exceeded allowed time
        if self.entityState.elapsedTime()>self.allowed:
            return True
        return False

    def act(self):
        if self.conditionMet():
            for child in self.children:
                child.act()
        return
        
    def insertChild(self,child):
        self.children.append(child)