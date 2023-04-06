
def makeRectangle(bounds, color):
    import engine.actor.entity.Rectangle as r
    result = r.Rectangle(bounds, color)
    return result

def makeRound(center, radius, color):
    import engine.actor.entity.Circle as c
    result = c.Circle(center, radius, color)
    return result
    
def makeColor(red, green, blue):
    import engine.actor.entity.Color as co 
    result = co.Color(red,green,blue)
    return result
    
def makeDrawRectAction():
    import engine.actor.action.DrawRect as re
    return re.DrawRectAction()
    
def makeDrawRoundAction():
    import engine.actor.action.DrawRound as ro
    return ro.DrawRoundAction()
    
def makeIsInsideAction():
    import engine.actor.action.IsInside as ii
    return ii.IsInsideAction()
    
def makePutPositionAction():
    import engine.actor.action.PutPosition as pu
    return pu.PutPositionAction()
    
def makeSplitColorAction():
    import engine.actor.action.SplitColor as sc
    return sc.SplitColorAction()