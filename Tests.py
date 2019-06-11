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
w.File_to_map("Complex.txt")

print(w.Evolution(Methode=1,Indiv=20,Mute=200,timeMax=200))
w.Start()
w.printgridstep()
input("pause")