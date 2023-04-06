class DragForce:
    def __init__(self):
        self.dragConstant = 1.0
        self.actions = []
        self.active = True
        return
        
    def insertAction(self, action):
        action.entityState = self
        self.actions.append(action)
        return