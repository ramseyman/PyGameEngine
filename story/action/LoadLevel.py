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
import pygame

class LoadLevel():

    
    def __init__(self, display, viewer, content):
        self.types = []
        self.viewer = viewer
        self.display = display
        self.content = content
        self.current = 0
        self.entityState = None
        self.children = []
        return
        
    def conditionMet(self,button):
        if self.entityState == None:
            return False
        if(button.color[0] == self.entityState.goals[self.current][0]):
            if(button.color[1] == self.entityState.goals[self.current][1]):
                if(button.color[2] == self.entityState.goals[self.current][2]):
                    return True
        
        return False
        
    def initial(self): 
        components = []
        #Split each goal color into x component colors based on difficulty
        for i in range(0, self.entityState.numGoals[self.current]):
            color = act.makeColor(self.entityState.goals[self.current][0], self.entityState.goals[self.current][1],self.entityState.goals[self.current][2])
            split = act.makeSplitColorAction()
            color.insertAction(split)
            components =  components + split.act(self.entityState.difficulty[self.current])
        merge = ui.makeMergeButton()
        
        #Turn each color into its own button
        for i in range (0,len(components)):
            button = ui.makeButton((rm.randint(0,1280-60),rm.randint(0,720-60),60,60),components[i])
            #Create press action
            press = ui.makeButtonPressAction()
            #Add press action and drawing to the button 
            button.insertAction(press)
            button.insertAction(ui.makeDrawButtonAction())
            #Merge two buttons when the second is pressed
            press.insertChild(merge)
            self.content.append(button)
            self.display.insertEntity(button)
            #If merge creates proper color load next level
            merge.insertChild(self)
        rect = act.makeRectangle((0,0,50,50),self.entityState.goals[self.current])
        drawRect = act.makeDrawRectAction()
        rect.insertAction(drawRect)
        self.display.insertEntity(rect)
        self.content.append(rect)
        #Execute all children actions
        for child in self.children:
            child.act()

        return
    
    def act(self,button):
        if self.conditionMet(button): 
            self.current = self.current + 1
            self.content.clear()
            self.content.append(self.viewer)
            self.display.entities = []
            components = []
            for i in range(0, self.entityState.numGoals[self.current]):
                color = act.makeColor(self.entityState.goals[self.current][0], self.entityState.goals[self.current][1],self.entityState.goals[self.current][2])
                split = act.makeSplitColorAction()
                color.insertAction(split)
                components =  components + split.act(self.entityState.difficulty[self.current])
            merge = ui.makeMergeButton()
            for i in range (0,len(components)):
                button = ui.makeButton((rm.randint(0,1280-60),rm.randint(0,720-60),60,60),components[i])
                #Create press action
                press = ui.makeButtonPressAction()
                #Add press action and drawing to the button 
                button.insertAction(press)
                button.insertAction(ui.makeDrawButtonAction())
                press.insertChild(merge)
                self.content.append(button)
                self.display.insertEntity(button)
                merge.insertChild(self)
            rect = act.makeRectangle((0,0,50,50),self.entityState.goals[self.current])
            drawRect = act.makeDrawRectAction()
            rect.insertAction(drawRect)
            self.display.insertEntity(rect)
            self.content.append(rect)
            #Execute all children actions
            for child in self.children:
                child.act()

        return
    def insertChild(self,child):
        self.children.append(child)
        