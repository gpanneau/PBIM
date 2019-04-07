#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:23:06 2019

@author: tpoquillon
"""
import numpy as np

class Genome:
  def __init__(self,I=25,O=3):  #Default Contructor
    
    self.O_=O  #range of the Output vector
    
    self.I_=I  #range of the Input vector
    
    self.H_=0  #range of the Hiden vector
    
    self.Hiden_=np.array([])  #Hiden vector
    
    self.Map_=np.zeros((I,O))  #Conection Matrix
    
  def Copy_Genom(self,Gen):  #Copy 
    
    self.O_=Gen.O_  
    
    self.I_=Gen.I_  
    
    self.H_=Gen.H_ 
    
    self.Hiden_=Gen.Hiden_[:]  
    
    self.Map_=Gen.Map_[:,:]  


  def Set_Map(self,Matrix):  #Matrix Seter by copy
    self.H_=len(Matrix)-self.I_
    self.Hiden_=np.zeros((1,self.H_))
    self.Map_=Matrix[:,:]

    

  def Processing(self,Input):  #Product vector of decision based from a vector of action passed as a parameter
    Out=(np.concatenate((Input,self.Hiden_),axis=None).dot(self.Map_))>0  
    self.Hiden_=1*Out[self.O_:self.O_+self.H_]
    return Out[0:self.O_]

  def Add_Gene(self):#This methode add a new gene, an intermediary hiden node between the input and the output. It improve the lenght of Hiden and H by one
    self.H_+=1
    self.Hiden_=np.zeros((1,self.H_))
    M=np.zeros((self.I_+self.H_,self.O_+self.H_))
    M[0:self.I_+self.H_-1,0:self.O_+self.H_-1]=self.Map_
    self.Map_=M
    
  def Add_Genes(self, Number_Of_Genes):# add a selected number of genes
    for i in range(Number_Of_Genes):
      self.Add_Gene()
      
      
  def Add_Connection(self,Source,Target,Value=1): # Add a conection of a chosen value in the chosen position in the Conections Matrix 
    self.Map_[Source,Target]=Value
    
  def Add_Random_Connection(self,Value=1):
    self.Add_Connection(int(np.random.random()*(self.H_+self.I_)),int(np.random.random()*(self.H_+self.O_)),Value) # Add a conection of a chosen value in a random position in the Conections Matrix 
   
    
if __name__ == '__main__':
  print("1: Constructor test")
  gm1=Genome(3,10)
  print(gm1.Map_==np.zeros((3,10)), gm1.O_==10, gm1.I_==3,gm1.H_==0, gm1.Hiden_==np.array([]))
  print("2: Set_Map test")
  gm2=Genome(2,2)
  gm2.Set_Map(np.array([[1, 2], [3, 4]]))
  print(gm2.Map_==np.array([[1, 2], [3, 4]]))
  print("3: Processing test")
  gm3=Genome(2,4)
  gm3.Set_Map(np.array([[0,1,0,1],[1,0,1,0]]))
  print(gm3.Processing(np.array([1,0]))==np.array([False,True,False,True]))
  print(gm3.Processing(np.array([0,1]))==np.array([True,False,True,False]))
  print("4: Copy_Genom test")
  gm4=Genome(14,12)
  gm4.Copy_Genom(gm3)
  print(gm4.Processing(np.array([0,1]))==np.array([True,False,True,False]))
  print(gm4.Processing(np.array([1,0]))==np.array([False,True,False,True]))
  print("5: Add_Gene test")
  gm5=Genome(2,4)
  gm5.Add_Gene()
  print(gm5.H_==1,gm5.Hiden_==np.array([0]))
  print("6: Add_Genes test")
  gm6=Genome(2,4)
  gm6.Set_Map(np.array([[0,1,0,1],[1,0,1,0]]))
  gm6.Add_Genes(3)
  print(gm6.H_==3,gm5.Hiden_==np.zeros(3),gm6.O_==4,gm6.I_==2)
  print(gm6.Map_==np.array([[0,1,0,1,0,0,0],[1,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]))
  print("7: Add_Connection test")
  gm7=Genome(2,4)
  gm7.Add_Connection(0,3,-8)
  print(gm7.Map_[0,3]==-8)
  print("8: Add_Random_Connection test")
  gm8=Genome(1,4)
  gm8.Add_Random_Connection()
  for i in range(4):
    if gm8.Map_[0,i]==1:
      print(True)
  gm8.Add_Random_Connection(-2.5)
  for i in range(4):
    if gm8.Map_[0,i]==-2.5:
      print(True)
    