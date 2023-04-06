import pygame

class DrawRectAction():
    def __init__(self):
        self.types = ["display"]
        self.entityState = None
        self.children = []
        return
    
    def conditionMet(self,data):
        if self.entityState == None:
            return False
        if self.entityState.active == False:
            return False
        if data == None:
            return False
        return True
    
    def act(self,data):
        if self.conditionMet(data):
            self.draw(data)
        for child in self.children:
            child.act(data)
        return
    
    def draw(self,screen):
        pygame.draw.rect(screen, self.entityState.color, self.entityState.bounds)
        return