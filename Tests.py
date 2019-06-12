#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:33:33 2019

@author: tpoquillon
"""

import Agent
import Genome
import Game
import time
import math
filenames=["Avancer","Sauter","Sauter2","Grimper","Tunel","Tunel2","GrandSaut","Grimper2"]

Dict={}
DictM={}
for filename in filenames:
  w=Game.Game()
  w.File_to_map(filename+".txt")
  Dict[filename]=w
  DictM[filename]=200
G=Genome.Genome(25,3)
A=Agent.Agent(4,2,G,Dict["Avancer"].Grid)

t_init=time.time()

t_final=12000
mutation=200
mutvar=100
ident=0
Serie=0
while time.time()-t_init<t_final and Serie<100:
  
  for filename in filenames:
    w=Dict[filename]
    w.AddAgent(A)
    E=w.Evolution(Methode=0,Indiv=200,Mute=DictM[filename],timeMax=10)
    w.SortByFitness()
    A=w.Pop[0]
    if E[1]==0 :
      Serie+=1
      if Serie==100:
        w.Pop[0].Genome_.PutMap_Into_Txt(str("Bobbies/id"+str(ident)+"_tests_simples_took_"+str(int(time.time()-t_init))+"s"))
      
    else:
      Serie=0
    print(E,Serie,filename,DictM[filename],w.Pop[0].posX_)
    w.Pop=[]
    DictM[filename]=int(E[0]*30+5)
    ident+=1

print(time.time()-t_init)


"""
Gsucces=Genome.Genome(25,3)
Gsucces.SetMap_From_Txt("Bobbies/id181_took_195s.txt")
A=Agent.Agent(4,2,Gsucces,Dict["Avancer"].Grid)
for filename in filenames:
    w=Dict[filename]
    w.AddAgent(A)
    w.Start()
    w.printgridstep()
    input("pause")
"""

