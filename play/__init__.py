#Entities

def makeViewer(x, y):
    import engine.play.entity.Viewer as vi
    result = vi.Viewer(x,y)
    return result

def makeGameLooper(content):
    import engine.play.entity.GameLooper as gl 
    result = gl.GameLooper(content)
    return result
    
#Actions

def makeDisplayAction():
    import engine.play.action.Display as di
    return di.Display()
    
def makeTerminateAction():
    import engine.play.action.Terminate as te
    return te.Terminate()