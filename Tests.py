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
filenames=["Avancer","Reculer","Reculer2","Sauter","Sauter2","Grimper","Tunel","Tunel2","GrandSaut","Grimper2"]
filenames2=["Avancer"]
Dict={}
DictM={}
for filename in filenames:
  w=Game.Game()
  w.File_to_map(filename+".txt")
  Dict[filename]=w
  DictM[filename]=200
G=Genome.Genome(25,3)
G.PutMap_Into_Txt("Bobbies/Bobby0")
A=Agent.Agent(4,2,G,Dict["Avancer"].Grid)

t_init=time.time()

t_final=12000
mutation=200
mutvar=100
ident=0
Serie=0
i=0
end=False
while time.time()-t_init<t_final and i<10:
  
  for filename in filenames2:
    w=Dict[filename]
    w.AddAgent(A)
    E=w.Evolution(Methode=0,Indiv=100,Mute=20,timeMax=10)
    w.SortByFitness()
    A=w.Pop[0]
    if E[1]==0 :
      Serie+=1
      if Serie==(i+1):
        w.Pop[0].Genome_.PutMap_Into_Txt("Bobbies/Bobby"+str(80+i))
        i=(i+1)
        filenames2.append(filenames[i%10])
        Serie=0
      
    else:
      Serie=0
    print(i,E,Serie,filename,DictM[filename],w.Pop[0].posX_)
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

