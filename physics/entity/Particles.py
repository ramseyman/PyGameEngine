class Particles:
    
    def __init__(self):
        self.position = []
        self.velocity = []
        self.acceleration = []
        self.mass = []
        self.activeParticle = []
        self.actions = []
        self.active = True;
        return
    
    def insertAction(self, action):
        action.entityState = self
        self.actions.append(action)
        return
        
    def addParticle(self, p, v, m):
        self.position.append(p)
        self.velocity.append(v)
        self.acceleration.append([0,0,0,0])
        self.mass.append(m)
        self.activeParticle.append(True)