import pygame
from pygame import mixer

class FailSoundAction():
    def __init__(self):
        self.types = []
        self.entityState = None
        self.children = []
        return 
        
    def conditionMet(self):
        if self.entityState == None:
            return False
        return True

    def act(self):
        if self.conditionMet:
            mixer.music.load('hit.wav')
            mixer.music.play()
            for child in self.children:
                    child.act()
        return
        
    def insertChild(self,child):
        self.children.append(child)