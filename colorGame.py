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
import engine.story as st
import random as rm


pygame.init()
    
#Create view window
viewer = pl.makeViewer(1280,720)
viewer.insertAction(pl.makeTerminateAction())
display = pl.makeDisplayAction()
viewer.insertAction(display)
gameContent = [viewer]

#Generate random levels with increasing difficulty
levels = st.makeLevels()
for i in range(0,23):
    levels.addLevel((rm.randint(0,255),rm.randint(0,255),rm.randint(0,255)),i+2,1)
load = st.makeLoadLevelAction(display, viewer, gameContent)
levels.insertAction(load)

#Load the initial level
load.initial()
    
#Loop game
gameLooper = pl.makeGameLooper(gameContent)
gameLooper.loop()