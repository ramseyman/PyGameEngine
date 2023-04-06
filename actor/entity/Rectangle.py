class Rectangle:

    def __init__ (self, bounds, color):
        self.bounds = bounds
        self.color = color
        self.actions = []
        self.active = True
        
    def insertAction(self, action):
        action.entityState = self
        self.actions.append(action)
        return