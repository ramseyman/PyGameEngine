
def makeHud(line):
    import engine.ui.entity.Hud as hd
    result = hd.Hud(line)
    return result

def makeButton(bounds, color):
    import engine.ui.entity.Button as bu
    result = bu.Button(bounds,color)
    return result
    
def makeButtonPressAction():
    import engine.ui.action.ButtonPress as bp
    return bp.ButtonPressed()
    
def makeDrawButtonAction():
    import engine.ui.action.DrawButton as db
    return db.DrawButtonAction()
    
def makeDrawHudAction():
    import engine.ui.action.DrawHud as dh
    return dh.DrawHudAction()
    
def makeMergeButton():
    import engine.ui.action.MergeButton as mb
    return mb.MergeButton()