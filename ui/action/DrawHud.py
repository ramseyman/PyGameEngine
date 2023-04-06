import pygame

class DrawHudAction():
    def __init__(self):
        self.types = ["display"]
        self.entityState = None
        return
    
    def conditionMet(self,data):
        if self.entityState == None:
            return False
        if data == None:
            return False
        return True
    
    def act(self,data):
        if self.conditionMet(data):
            self.draw(data)
        return
    
    def draw(self,screen):
        font = pygame.font.Font(None,20)
        text = font.render(self.entityState.line,True, (255,255,255))
        rect = pygame.Rect(5,5,200,30)
        screen.blit(text,rect)
        return