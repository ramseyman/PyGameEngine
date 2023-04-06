import pygame

class TotalCounter:
    def __init__(self, counter):
        self.counter = counter
        self.actions = []
        self.active = True
        return

    def insertAction(self,action):
        action.entityState = self
        self.actions.append(action)
        return
        
    def addEntityState(self,action):
        action.entityState = self
        return