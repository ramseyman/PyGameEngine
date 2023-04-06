class UpdateAction():
    def __init__(self):
        self.types = ["loop"]
        self.entityState = None
        self.children = []
        return 
        
    def conditionMet(self):
        if self.entityState == None:
            return False
        return True

    def act(self):
        if self.conditionMet:
            self.entityState.tick()
            for child in self.children:
                    child.act()
        return
        
    def insertChild(self,child):
        self.children.append(child)