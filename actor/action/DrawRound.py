import pygame

class DrawRoundAction():
    def __init__(self):
        self.types = ["display"]
        self.entityState = None
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
        return
    
    def draw(self,screen):
        pygame.draw.circle(screen, self.entityState.color, self.entityState.position, self.entityState.radius)
        return