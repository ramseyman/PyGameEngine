import pygame

import sys 

import os

sys.path.insert(0, os.path.dirname(os.getcwd())) 

import engine.play as pl
import engine.ui as ui 
import engine.utility as ut
import engine.sound as so
import engine.physics as phys
import engine.actor as act
import random as rm


pygame.init()

def getCircles(number):
    #Create circles with random colors and positions
    circles = []
    radius = 10
    for i in range(0,number):
        circleBounds = randomPos()
        circleColor = randomColor()
        circle = act.makeRound(circleBounds,radius,circleColor)
        circle.insertAction(act.makeDrawRoundAction())
        circles.append(circle)
    return circles
        
def getParticles(data, boxes):
        particles = []
        
        parts = phys.makeParticles()
        particles.append(parts)
        
        #Create particles with random velocity and location equal to the circles created earlier
        for d in data:
            position = list(d.position)
            velocity = [(25.0*rm.random()),(2.0*rm.random() - 1.0)]
            mass = 1.0
            parts.addParticle(position,velocity,mass)
        
        #Create gravity 
        gravity = phys.makeGravity()
        gravity.gravity = [0.0,0.5]
        gravityAction = phys.makeGravityForceAction()
        gravity.insertAction(gravityAction)
        
        #Create spring force
        spring = phys.makeSpring()
        spring.springConstant = 0.01
        springAction = phys.makeSpringForceAction()
        spring.insertAction(springAction)
        
        #Create drag
        drag = phys.makeDrag()
        drag.dragConstant = 0.05
        dragAction = phys.makeDragForceAction()
        drag.insertAction(dragAction)
        
        #Create position solver
        posSolve = phys.makePositionSolveAction()
        parts.insertAction(posSolve)
        
        #Create velocity solver
        velSolve = phys.makeVelocitySolveAction()
        parts.insertAction(velSolve)
        
        #Add forces to velocity solve
        velSolve.children.append(gravityAction)
        velSolve.children.append(springAction)
        velSolve.children.append(dragAction)
        
        #Create eulor solver and attach pos and vel solvers to it
        eulSolve = phys.makeEulerSolveAction()
        eulSolve.dt = 0.01
        parts.insertAction(eulSolve)
        eulSolve.children.append(posSolve)
        eulSolve.children.append(velSolve)
        
        #Attach circle positions to the positions of the particles
        for i in range(0,len(data)):
            pick = phys.makePickPositionAction(i)
            put = act.makePutPositionAction()
            
            parts.insertAction(pick)
            data[i].insertAction(put)
            pick.children.append(put)
            
            eulSolve.children.append(pick)
            
        #Create frame collision
        windowFrameCollider = phys.makeRectangleCollider([0,0],[1280,720])
        collisions = phys.makeInsideRectangleCollisionAction()
        windowFrameCollider.insertAction(collisions)
        posSolve.children.append(collisions)
        
        #Create colliders for each of the boxes
        for b in boxes:
            urc = [(b.bounds[0][0] + b.bounds[1][0]),(b.bounds[0][1] + b.bounds[1][1])]
            boxCollider = phys.makeRectangleCollider(b.bounds[0],urc)
            collide = phys.makeOutsideRectangleCollisionAction()
            boxCollider.insertAction(collide)
            posSolve.children.append(collide)
        
        return particles

def getBoxes(x,y):
    boxes = []
    rect = act.makeRectangle([(850,0),(50,350)],[255,255,255])
    rect.insertAction(act.makeDrawRectAction())
    boxes.append(rect)
    rect2 = act.makeRectangle([(850,450),(50,720)],[255,255,255])
    rect2.insertAction(act.makeDrawRectAction())
    boxes.append(rect2)
    rect3 = act.makeRectangle([(975,650),(150,15)],[255,255,255])
    rect3.insertAction(act.makeDrawRectAction())
    boxes.append(rect3)
    rect4 = act.makeRectangle([(1050,550),(150,15)],[255,255,255])
    rect4.insertAction(act.makeDrawRectAction())
    boxes.append(rect4)
    return boxes

def randomPos():
    pos = [rm.randint(0,850),rm.randint(0,720)]
    return pos

def randomColor():
    color = (rm.randint(0,255),rm.randint(0,255),rm.randint(0,255))
    return color
    
#Create view window
viewer = pl.makeViewer(1280,720)
viewer.insertAction(pl.makeTerminateAction())
display = pl.makeDisplayAction()
viewer.insertAction(display)

#Create placeholder button
circles = getCircles(100)

boxes = getBoxes(1280,720)

particles = getParticles(circles, boxes)

#Create the rectangle for the appearing box and deactivate it to begin with
rect5 = act.makeRectangle([(850,350),(50,100)],[255,255,255])
rect5.insertAction(act.makeDrawRectAction())
boxes.append(rect5)
deactivate = ut.makeDeactivateAction()
rect5.insertAction(deactivate)
deactivate.act()

#Create collider for the appearing box and deactivate it to begin with 
urc = [(rect5.bounds[0][0] + rect5.bounds[1][0]),(rect5.bounds[0][1] + rect5.bounds[1][1])]
boxCollider = phys.makeRectangleCollider(rect5.bounds[0],urc)
collide = phys.makeOutsideRectangleCollisionAction()
boxCollider.insertAction(collide)
particles[0].actions[0].children.append(collide)
deactivate2 = ut.makeDeactivateAction()
boxCollider.insertAction(deactivate2)
deactivate2.act()

#Create the timer and attach appropriate children
time = ut.makeTimer()
update = ut.makeUpdateAction()
time.insertAction(update)
start = ut.makeStartAction()
alarm = ut.makeAlarmAction(9)
update.insertChild(alarm)

#Reactivate the box and its collider upon alarm 
activate = ut.makeActivateAction()
activate2 = ut.makeActivateAction()
boxCollider.insertAction(activate2)
boxes[4].insertAction(activate)
alarm.insertChild(activate)
alarm.insertChild(activate2)
time.insertAction(start)
time.insertAction(alarm)

#add everything to the gameContent
gameContent = [viewer]
gameContent = gameContent + circles + particles + boxes
gameContent.append(time)

#Add objects to be viewed into the display list
for c in circles:
    display.insertEntity(c)
    
for b in boxes:
    display.insertEntity(b)

#Loop game
gameLooper = pl.makeGameLooper(gameContent)
gameLooper.loop()