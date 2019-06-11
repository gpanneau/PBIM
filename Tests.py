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
filenames=["Avancer","Sauter","Grimper","Tunel","Sauter2","Reculer","GrandSaut"]
Dict={}
for filename in filenames:
  w=Game.Game()
  w.File_to_map(filename+".txt")
  Dict[filename]=w

G=Genome.Genome(25,3)
A=Agent.Agent(4,2,G,Dict["Avancer"].Grid)
t_init=time.time()
t_final=60
mutation=200
mutvar=100
ident=0
while time.time()-t_init<t_final:
  
  for filename in filenames:
    w=Dict[filename]
    w.AddAgent(A)
    E=w.Evolution(Methode=1,Indiv=50,Mute=mutation,timeMax=200)
    w.SortByFitness()
    A=w.Pop[0]
    if E[1]==0:
      w.Pop[0].Genome_.PutMap_Into_Txt(str("Bobbies/Best_Genome_id"+str(ident)+"_on_Map_'"+filename+"'_in_"+str(int(E[0]*1000))+"_ms"))
    print(E,filename,mutation)
    mutation=int(E[0]+mutvar+2)
    ident+=1
  mutvar=mutvar*0.8



