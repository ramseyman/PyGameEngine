import pygame

class Activate():
    def __init__(self):
        self.types = []
        self.entityState = None
        self.children = []
        return
        
    def conditionMet(self):
        if self.entityState == None:
            return False
        if self.entityState.active == False:
            return True
        return False
        
    def act(self):
        if self.conditionMet():
            #Set button active status to true
            self.entityState.active = True
            #Run associated actions, such as incrementing total counter
            for child in self.children:
                child.act()
        return
        
    def insertChild(self,child):
        self.children.append(child)