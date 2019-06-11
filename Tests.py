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
filenames=["Avancer","Sauter","Grimper","Tunel","Reculer","GrandSaut","Simple"]

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
t_final=120
mutation=200
mutvar=100
ident=0
Serie=0
while time.time()-t_init<t_final and Serie<100:
  
  for filename in filenames:
    w=Dict[filename]
    w.AddAgent(A)
    E=w.Evolution(Methode=0,Indiv=200,Mute=DictM[filename],timeMax=2)
    w.SortByFitness()
    A=w.Pop[0]
    if E[1]==0 :
      Serie+=1
      if Serie==100:
        w.Pop[0].Genome_.PutMap_Into_Txt(str("Bobbies/id"+str(ident)+"_on_Map_"+filename+"_in_"+str(int(E[0]*1000000))+"_ns"))
      
    else:
      Serie=0
    print(E,Serie,filename,DictM[filename],w.Pop[0].posX_)
    w.Pop=[]
    DictM[filename]=int(E[0]*100+5)
    ident+=1

print(time.time()-t_init)

