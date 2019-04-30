#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:21:52 2019

@author: tpoquillon
"""

import numpy as np
import Genome

class Agent:
  def __init__(self,x,y,myGenome,grid):#Constructor whitch takes an existing genome, a grid  and a position wanted for the agent on this grid
    self.posX_=x
    self.posY_=y
    self.Genome_= Genome.Genome(myGenome.I_,myGenome.O_)
    self.Genome_.Set_Map(myGenome.Map_)
    self.Environment_=np.matrix.copy(grid)
    self.decision_=[False,False,False]
    
    
    
  
  
  
    
if __name__ == '__main__':
  mat1=np.zeros((5,5))
  genom1=Genome.Genome(3,10)
  a=0
  b=0
  ag1=Agent(a,b,genom1,mat1)
  mat1[0,0]=3
  print(ag1.posX_==a,ag1.posY_==b,ag1.Genome_==genom1,ag1.Environment_,mat1,ag1.decision_==[0,0,0])
  print(ag1.Genome_)
  print(genom1)
  
