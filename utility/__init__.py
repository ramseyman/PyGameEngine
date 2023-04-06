
#Entities

def makeTimer():
    import engine.utility.entity.Timer as ti
    result = ti.Timer()
    return result

def makeSuccessCounter(start):
    import engine.utility.entity.SuccessCounter as sc
    result = sc.SuccessCounter(start)
    return result

def makeTotalCounter(start):
    import engine.utility.entity.TotalCounter as tc
    result = tc.TotalCounter(start)
    return result
    
#Actions

def makeActivateAction():
    import engine.utility.action.Activate as av
    return av.Activate()
    
def makeDeactivateAction():
    import engine.utility.action.Deactivate as da
    return da.Deactivate()
    
def makeIncrementAction():
    import engine.utility.action.Increment as ic
    return ic.IncrementAction()
    
def makeStartAction():
    import engine.utility.action.Start as st 
    return st.StartAction()

def makeUpdateAction():
    import engine.utility.action.Update as up 
    return up.UpdateAction()
    
def makeAlarmAction(allow):
    import engine.utility.action.Alarm as al 
    return al.AlarmAction(allow)