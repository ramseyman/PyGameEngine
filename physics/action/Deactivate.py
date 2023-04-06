import pygame

class DeactivateAction():
    def __init__(self):
        self.types = []
        self.entityState = None
        self.children = []
        return
        
    def conditionMet(self,data):
        if self.entityState == None:
            return False
        return True
        
    def act(self,data):
        if self.conditionMet():
            data = False
            for child in self.children:
                child.act()
        return