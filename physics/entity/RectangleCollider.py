class RectangleCollider:

    def __init__(self, llc = [0.0,0.0], urc = [100.0,100.0]):
        self.llc = llc
        self.urc = urc
        self.actions = []
        self.active = True
        return
        
    def insertAction(self, action):
        action.entityState = self
        self.actions.append(action)
        return