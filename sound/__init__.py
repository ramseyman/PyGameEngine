#Actions

def makeSoundAction():
    import engine.sound.action.MakeSound as ms 
    return ms.SoundAction()
    
def makeFailSoundAction():
    import engine.sound.action.FailSound as fs 
    return fs.FailSoundAction()
    