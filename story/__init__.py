def makeLevels():
    import engine.story.entity.Levels as l
    result = l.Levels()
    return result
    
def makeLoadLevelAction(display, viewer, content):
    import engine.story.action.LoadLevel as ll
    return ll.LoadLevel(display, viewer,content)