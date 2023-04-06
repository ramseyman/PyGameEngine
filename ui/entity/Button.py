import pygame

class Button:
    def __init__(self, bounds, color):
        self.bounds = bounds
        self.color = color
        self.actions = []
        self.active = True
        return

    def insertAction(self,action):
        action.entityState = self
        self.actions.append(action)
        return
    
    def withinBounds(self, pos):
        if pos[0] < self.bounds[0]:
            return False
        if pos[0] > (self.bounds[2] + self.bounds[0]):
            return False
        if pos[1] < self.bounds[1]:
            return False
        if pos[1] > (self.bounds[3] + self.bounds[1]):
            return False
        return True
    
    def addEntityState(self,action):
        action.entityState = self
        return