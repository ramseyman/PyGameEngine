import time

class Timer:
    def __init__(self):
        self.start = time.perf_counter()
        self.current = None
        self.actions = []
    
    def startTimer(self):
        self.start = time.perf_counter()
        return
    
    def tick(self):
        self.current = time.perf_counter()
        return
    
    def elapsedTime(self):
        return self.current - self.start
        
    def insertAction(self,action):
        action.entityState = self
        self.actions.append(action)
        return