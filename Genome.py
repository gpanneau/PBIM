#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:23:06 2019

@author: tpoquillon
"""
import numpy as np

class Genome:
  def __init__(self,I,O):  #Default Contructor
    
    self.O=O  #range of the Output vector
    
    self.I=I  #range of the Input vector
    
    self.H=0  #range of the Hiden vector
    
    self.Hiden=np.array([])  #Hiden vector
    
    self.Map=np.zeros((I,O))  #Conection Matrix


  def Copy_Map(self,Matrix):  #Matrix Seter by copy
    self.H=len(Matrix)-self.I
    self.Hiden=np.zeros((1,self.H))
    self.Map=Matrix[:,:]

    

if __name__ == '__main__':
  gm1=Genome(3,10)
  print(gm1.Map==np.zeros((3,10)), gm1.O==10, gm1.I==3,gm1.H==0, gm1.Hiden==np.array([]))
  gm2=Genome(2,2)
  gm2.Copy_Map(np.array([[1, 2], [3, 4]]))
  print(gm2.Map==np.array([[1, 2], [3, 4]]))