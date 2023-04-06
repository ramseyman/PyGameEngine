import random as rm
class SplitColorAction:


    def __init__(self):
        self.types = []
        self.entityState = None
        self.children = []
        
    def conditionMet(self, data):
        if self.entityState == None:
            return False
        if self.entityState.active == False:
            return False
        if data < 1:
            return False
        return True
        
    def act(self, x):
        newColors = []
        if self.conditionMet(x):
            #split the color into x random component colors
            
            remainingRed = self.entityState.red
            remainingGreen = self.entityState.green
            remainingBlue = self.entityState.blue
            split = x
            for i in range (0,x-1):
                split = x-i
                resultRed = rm.randint(0,int(remainingRed/split))
                resultGreen = rm.randint(0,int(remainingGreen/split))
                resultBlue = rm.randint(0,int(remainingBlue/split))
                newColors.append((resultRed,resultGreen,resultBlue))
                remainingRed = remainingRed - resultRed
                remainingGreen = remainingGreen - resultGreen
                remainingBlue = remainingBlue - resultBlue
            newColors.append((remainingRed,remainingGreen,remainingBlue))
            for child in self.children:
                c.act(data)
        return newColors