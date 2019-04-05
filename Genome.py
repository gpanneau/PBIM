#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:23:06 2019

@author: tpoquillon
"""
import numpy as np

class Genome:
  def __init__(self,I,O):  #Default Contructor
    
    self.O_=O  #range of the Output vector
    
    self.I_=I  #range of the Input vector
    
    self.H_=0  #range of the Hiden vector
    
    self.Hiden_=np.array([])  #Hiden vector
    
    self.Map_=np.zeros((I,O))  #Conection Matrix


  def Set_Map(self,Matrix):  #Matrix Seter by copy
    self.H_=len(Matrix)-self.I_
    self.Hiden_=np.zeros((1,self.H_))
    self.Map_=Matrix[:,:]

    

  def Processing(self,Input):  #Product vector of decision based from a vector of action passed as a parameter
    Out=(np.concatenate((Input,self.Hiden_),axis=None).dot(self.Map_))>0  
    self.Hiden_=1*Out[self.O_:self.O_+self.H_]
    return Out[0:self.O_]

if __name__ == '__main__':
  gm1=Genome(3,10)
  print(gm1.Map_==np.zeros((3,10)), gm1.O_==10, gm1.I_==3,gm1.H_==0, gm1.Hiden_==np.array([]))
  gm2=Genome(2,2)
  gm2.Set_Map(np.array([[1, 2], [3, 4]]))
  print(gm2.Map_==np.array([[1, 2], [3, 4]]))
  gm3=Genome(2,4)
  gm3.Set_Map(np.array([[0,1,0,1],[1,0,1,0]]))
  print(gm3.Processing(np.array([1,0]))==np.array([False,True,False,True]))
  