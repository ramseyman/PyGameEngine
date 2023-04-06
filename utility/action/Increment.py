import pygame

class IncrementAction():
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
            #Increment associated counter
            self.entityState.counter = self.entityState.counter+1
            for child in self.children:
                child.act()
        return
    
    def insertChild(self,child):
        self.children.append(child)
    
