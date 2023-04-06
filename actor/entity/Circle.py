class Circle:

    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color
        self.actions = []
        self.active = True
        
    def insertAction(self, action):
        action.entityState = self
        self.actions.append(action)
        return