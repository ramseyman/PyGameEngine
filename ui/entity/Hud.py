import pygame

class Hud:
    def __init__(self, line):
        self.line = line
        self.actions = []
        self.active = True
        return

    def insertAction(self,action):
        action.entityState = self
        self.actions.append(action)
        return
    