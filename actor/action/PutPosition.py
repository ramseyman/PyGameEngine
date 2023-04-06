class PutPositionAction:

    def __init__(self):
        self.types = ["position"]
        self.entityState = None
        self.children = []
        
    def conditionMet(self, data):
        if self.entityState == None:
            return False
        if self.entityState.active == False:
            return False
        if len(data) != 2:
            return False
        return True
        
    def act(self, data):
        if self.conditionMet(data):
            self.entityState.position = data
            for child in self.children:
                c.act(data)
        return