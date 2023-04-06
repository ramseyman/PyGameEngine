import pygame

class ButtonPressed():
    def __init__(self):
        self.types = ["event"]
        self.entityState = None
        self.children = []
        return
        
    def conditionMet(self,event):
        if self.entityState == None:
            return False
        if self.entityState.active == False:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Check if mouse is within button area
            pos = event.pos
            return self.entityState.withinBounds(pos)
        return False
        
    def act(self,event):
        if self.conditionMet(event):
            #Execute all children actions
            for child in self.children:
                child.act(self.entityState)
        return
    
    def insertChild(self,child):
        self.children.append(child)
        