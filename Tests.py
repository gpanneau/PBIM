#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:33:33 2019

@author: tpoquillon
"""

import Agent
import Genome
import Game

w=Game.Game()
G0=Genome.Genome(25,3)
A0=Agent.Agent(4,2,G0,w.Grid)
w.AddAgent(A0)
filname="Simple"
w.File_to_map(filname+".txt")

t=w.Evolution(Methode=1,Indiv=20,Mute=200,timeMax=200)
print(t)
w.Pop[0].Genome_.PutMap_Into_Txt(str("Best_Genome_on_Map_'"+filname+"'_in_"+str(t)+"_s"))
w.Start()
w.printgridstep()
input("pause")