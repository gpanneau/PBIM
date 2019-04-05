#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:23:06 2019

@author: tpoquillon
"""
import numpy as np

class AI:
  def __init__(self,I,O):
    
    self.O=O  #range of the Output vector
    
    self.I=I  #range of the Input vector
    
    self.H=0  #range of the Hiden vector
    
    self.Hiden=np.array([])  #Hiden vector
    
    self.Map=np.zeros((I,O))  #Conection Matrix
    
if __name__ == '__main__':
  g1=AI(3,10)
  print(g1.Map==np.zeros((3,10)), g1.O==10, g1.I==3,g1.H==0, g1.Hiden==np.array([]))