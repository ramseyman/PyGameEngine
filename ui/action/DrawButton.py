import pygame

class DrawButtonAction():
    def __init__(self):
        self.types = ["display"]
        self.entityState = None
        return
    
    def conditionMet(self,data):
        if self.entityState == None:
            return False
        if self.entityState == False:
            return False
        #Check to ensure button is currently active
        if self.entityState.active == False:
            return False
        if data == None:
            return False
        return True
    
    def act(self,data):
        if self.conditionMet(data):
            self.draw(data)
        return
    
    def draw(self,screen):
        pygame.draw.rect(screen, self.entityState.color, self.entityState.bounds)
        return