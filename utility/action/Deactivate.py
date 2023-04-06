import pygame

class Deactivate():
    def __init__(self):
        self.types = []
        self.entityState = None
        self.children = []
        return
        
    def conditionMet(self):
        if self.entityState == None:
            return False
        return True
        
    def act(self):
        if self.conditionMet():
            #Set the button's active state to false
            self.entityState.active = False
            #Run associated actions, such as moving the button
            for child in self.children:
                child.act()
        return
        
    def insertChild(self,child):
        self.children.append(child)