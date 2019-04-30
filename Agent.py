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
    self.Environment_=grid
    self.decision_=[False,False,False]
    
    
    
  def Jump(self):
    if(self.decision_[0] and self.Environment_[self.posY_+1,self.posX_]==1 and self.Environment_[self.posY_-1,self.posX_]!=1):
      self.posY_=self.posY_-1
      return True
      
  def MvForward(self):
    if(self.decision_[1] and not(self.decision_[2]) and self.Environment_[self.posY_,self.posX_+1]!=1):
      self.posX_=self.posX_+1
      return True
      
  def MvBackward(self):
    if(self.decision_[2] and not(self.decision_[1]) and self.Environment_[self.posY_,self.posX_-1]!=1):
      self.posX_=self.posX_-1
      return True
      

  
  
    
if __name__ == '__main__':
  mat1=np.zeros((5,5))
  ai1=Genome.Genome(3,10)
  a=0
  b=0
  ag1=Agent(a,b,ai1,mat1)
  print(ag1.posX_==a,ag1.posY_==b,ag1.Genome_==ai1,ag1.Environment_==mat1,ag1.decision_==[0,0,0])