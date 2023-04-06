
def makeParticles():
    import engine.physics.entity.Particles as p
    result = p.Particles()
    return result

def makeGravity():
    import engine.physics.entity.GravityForce as g
    result = g.GravityForce()
    return result
    
def makeSpring():
    import engine.physics.entity.SpringForce as s
    result = s.SpringForce()
    return result
    
def makeDrag():
    import engine.physics.entity.DragForce as d
    result = d.DragForce()
    return result
    
def makeRectangleCollider(llc,urc):
    import engine.physics.entity.RectangleCollider as rc
    result = rc.RectangleCollider(llc,urc)
    return result
    
def makeOutsideRectangleCollisionAction():
    import engine.physics.action.OutsideRectangleCollision as oc
    return oc.OutsideRectangleCollisionAction()

def makeInsideRectangleCollisionAction():
    import engine.physics.action.InsideRectangleCollision as ic
    return ic.InsideRectangleCollisionAction()
    
def makePickPositionAction(index):
    import engine.physics.action.PickPosition as pi
    return pi.PickPositionAction(index)
    
def makePositionSolveAction():
    import engine.physics.action.PositionSolve as ps
    return ps.PositionSolveAction()
    
def makeVelocitySolveAction():
    import engine.physics.action.VelocitySolve as vs
    return vs.VelocitySolveAction()
    
def makeEulerSolveAction():
    import engine.physics.action.EulerSolve as es
    return es.EulerSolveAction()
    
def makeGravityForceAction():
    import engine.physics.action.GravityForceAction as gf
    return gf.GravityForceAction()

def makeSpringForceAction():
    import engine.physics.action.SpringForceAction as sf
    return sf.SpringForceAction()
    
def makeDragForceAction():
    import engine.physics.action.DragForceAction as df
    return df.DragForceAction()
    
def makeDeactivateAction():
    import engine.physics.action.DeactivateAction as da
    return da.DeactivateAction()