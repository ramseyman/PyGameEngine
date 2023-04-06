import pygame

class SuccessCounter:
    def __init__(self, counter):
        self.counter = counter
        self.actions = []
        self.active = True
        return

    def insertAction(self,action):
        action.entityState = self
        self.actions.append(action)
        return
    