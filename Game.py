#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:20:10 2019

@author: tpoquillon
"""

import numpy as np
import Agent
import Genome

class Game:
  def __init__(self,H=8,L=100):
    #Grid
    self.Grid=np.zeros((H,L),dtype=int)
    self.Grid[H-3:H,:]=np.ones((3,L),dtype=int)
    self.Grid[:,0:2]=np.ones((H,2),dtype=int)
    self.Grid[:,L-2:L]=np.ones((H,2),dtype=int)
    #Pop
    self.Pop=[]

  def AddAgent(self,agent):
    self.Pop.append(agent)

if __name__ == '__main__':
  g1=Game(8,30)
  print(g1.Grid==[[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
  g2=Game(3,2)
  print(g2.Grid==[[1,1],[1,1],[1,1]])
  print(g1.Pop==g2.Pop==[])
  agent=Agent.Agent(2,2,Genome.Genome(10,4),g1)
  g1.AddAgent(agent)
  print(g1.Pop==[agent])
