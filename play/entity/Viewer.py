import pygame

class Viewer:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.actions = []
        self.screen = pygame.display.set_mode((self.x,self.y))
        return

    def insertAction(self,action):
        action.entityState = self
        self.actions.append(action)
        return
    
    def makeFrameViewer(self,x,y):
        screen = pygame.display.set_mode((self.x,self.y))
        return screen