class Color:

    def __init__ (self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.actions = []
        self.active = True
        
    def insertAction(self, action):
        action.entityState = self
        self.actions.append(action)
        return