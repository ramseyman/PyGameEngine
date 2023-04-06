class GravityForce:

    def __init__(self):
        self.gravity = [0,-1]
        self.actions = []
        self.active = True
        return
        
    def insertAction(self, action):
        action.entityState = self;
        self.actions.append(action)
        return