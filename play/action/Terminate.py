import pygame
import sys
class Terminate():
    def __init__(self):
        self.types = ["event"]
        self.entityState = None
        self.children = []
        return
        
    def conditionMet(self,event):
        if self.entityState == None:
            return False
        if event == None:
            return False
        #Check for window close or escape key press
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
        return False
        
    def act(self,event):
        if self.conditionMet(event):
            #close pygame and python
            pygame.quit()
            sys.exit()
        return
        