class MergeButton():

    
    def __init__(self):
        self.types = []
        self.pressed = []
        self.entityState = None
        self.children = []
        return
        
    def conditionMet(self):
        if len(self.pressed) < 2:
            return False
        return True
        
    def act(self,button):
        self.pressed.append(button)
        if self.conditionMet():
            self.pressed[0].active = False
            self.pressed[1].color = (min((self.pressed[1].color[0]+self.pressed[0].color[0]),255),min((self.pressed[1].color[1]+self.pressed[0].color[1]),255),min((self.pressed[1].color[2]+self.pressed[0].color[2]),255))
            self.pressed = []
            #Execute all children actions
            for child in self.children:
                child.act(button)

        return
    
    def insertChild(self,child):
        self.children.append(child)
        