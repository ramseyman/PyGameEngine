import pygame

class Display():
    def __init__(self):
        self.types = ["display"]
        self.entityState = None
        self.entities = []
        return
        
    def insertEntity(self, entity):
        self.entities.append(entity)
        return
        
    def conditionMet(self, data):
        if self.entityState == None:
            return False
        if data == None:
            return False
        return True
        
    def act(self, data):
        if self.conditionMet(data):
            #Execute all entitiy actions of type "display"
            color = (0,0,0)
            data.fill(color)
            for entity in self.entities:
                for action in entity.actions:
                    if action.types == ["display"]:
                        action.act(data)
            pygame.display.flip()
        return
    
 