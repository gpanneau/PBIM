#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:20:10 2019

@author: tpoquillon
"""

import numpy as np
import Agent
import Genome
import ViewWorld
import tkinter as tk
import time

class Game:
  
  #CONSTRUCTEUR  
  def __init__(self,H=9,L=100):
    #Grid
    self.Grid=np.zeros((H,L),dtype=int)#The grid is a table full of zeros (H columns x L rows)
    self.Grid[H-2:H,:]=np.ones((2,L),dtype=int)#The grid has the 2 lines at the bottom full of ones (the floor)
    self.Grid[0:2,:]=np.ones((2,L),dtype=int)#The grid has the 2 lines at the top full of ones (the ceil)
    self.Grid[:,0:2]=np.ones((H,2),dtype=int)#The grid has the 2 columns at the lest full of ones (the left wall)
    self.Grid[:,L-2:L]=np.ones((H,2),dtype=int)#The grid has the 2 columns at the right full of ones (the right wall)
    #Pop
    self.Pop=[]#Pop is a list containing all the different agents : the population
    #Time
    self.Time=0#Time is counting how many time the agents have been run.
    #World
    self.World=ViewWorld.CreateWorld()
    self.World.pack(padx=000,pady=000)
    self.B = tk.Button(master=self.World.frame, text="Run Bobby, RUUUN !", bg='yellow', fg='red', width=25, height = 5, command=lambda:self.run()).pack(side=tk.LEFT)
    self.lenth=L
    self.hight=H

  #AFFICHAGE  
  def printgridstep(self):  
    self.World.draw_grid(self.Grid)
    
  #TERRAIN  
  def MakePit(self,x): #Fait un trou à la position x
    self.Grid[2:,x]=np.zeros((len(self.Grid[2:,x])),dtype=int)

  def AddBlockStratum(self,xl,xr): #Ajoute une strate de bloques entre xl et xr
    H=len(self.Grid)
    for col in range(xl,xr+1):
      i=4
      while i<H and self.Grid[i][col]!=1:
        i+=1
      if i!=0 and i!=H:
        self.Grid[i-1][col]=1
        
  def Random_Level_generation(self,nbPit,nblayer):
    for i in range(nbPit):
      x=int(np.random.random()*(len(self.Grid[0,:])-5)+2)
      if self.Grid[len(self.Grid)-1,x-1]!=0 or self.Grid[len(self.Grid)-1,x+1]!=0:
        self.MakePit(x)
    dicti={}
    for i in range(nblayer):
      xl=int(np.random.random()*(len(self.Grid[0,:])-5)+2)
      xr=xl+int(np.random.random()*8)+1
      if self.Grid[len(self.Grid)-1,xl]!=0 and self.Grid[len(self.Grid)-1,xl-1]!=0 and xr<len(self.Grid[0,:])-2 and (xl not in dicti or dicti[xl]==1):
        self.AddBlockStratum(xl,xr)
        if xl in dicti:
          dicti[xl]=2
        if xl not in dicti:
          dicti[xl]=1
        
    return True
  
  
  def File_to_map(self,s):#Charge un terrain depuis un fichier texte
    self.Grid=np.loadtxt(s)
    self.lenth=len(self.Grid[0,:])
    self.hight=len(self.Grid[:,0])
    for agent in self.Pop:
      agent.Environment_=self.Grid
      
  #POPULATION
  def AddAgent(self,agent):#ajout d'un agent dans la population
    self.Pop.append(agent)  
    
  def SortByFitness(self): #tri la popuolation des individus avec la meilleur fitnesse à ceux avec la pire
    for agent in self.Pop:
      if not agent.Alive:
        agent.posX_=-1 #
    i = len(self.Pop)-1 #si les agent sont mort on set leurs posx (fitness) à -1
    while i!=0 : #algorithme de tri en fonction de posX_
      for j in range(i):
        if self.Pop[j].posX_<self.Pop[j+1].posX_:
          inter=self.Pop[j]
          self.Pop[j]=self.Pop[j+1]
          self.Pop[j+1]=inter   
      i=i-1
  def New_Generation(self,Methode=0,Indiv=50,Mute=10):#crée une nouvelle génération d'individus à partir d'une ancienne population triée par fitness en fonction de la methode choisie
    if Methode==0:
      for i in range(1,Indiv):
        G=Genome.Genome(25,3)
        G.Set_Map(self.Pop[0].Genome_.Map_[:,:])
        self.Pop[i]=Agent.Agent(self.Pop[0].posX_,self.Pop[0].posY_,G,self.Grid)
        self.Pop[i].Mutate(Mute,1)
    if Methode==1:
      j=0
      PopBis=[]
      for agent in self.Pop:#chaque agent peut se reproduire dans la limite des places disponible. Les plus performent se reproduiront en premier
        if j<Indiv:
          PopBis.append(agent)
          j+=1
          if j<Indiv:
            G=Genome.Genome(25,3)
            G.Set_Map(agent.Genome_.Map_[:,:])
            A=Agent.Agent(agent.posX_,agent.posY_,G,self.Grid)
            A.Mutate(Mute,1)
            PopBis.append(A)
            j+=1
        else:
          break
      self.Pop=PopBis


#JEU
  def run(self):
    self.Time+=1
    for Ag in self.Pop:
      if Ag.Alive:
        self.Grid[Ag.posY_,Ag.posX_]=0
        Ag.Make_Decision()
        if(not(Ag.Jump())):
          Ag.Fall()
        Ag.MvForward()
        Ag.MvBackward()
    for Ag in self.Pop:
      if Ag.Alive:
        self.Grid[Ag.posY_,Ag.posX_]=2
    self.World.draw_grid(self.Grid)
    for Ag in self.Pop:
      if Ag.Alive:
        self.Grid[Ag.posY_,Ag.posX_]=0
        
  def RunBlind(self): #run without printing anything
    self.Time+=1
    for Ag in self.Pop:
      if Ag.Alive:
        Ag.Make_Decision()
        if(not(Ag.Jump())):
          Ag.Fall()
        Ag.MvForward()
        Ag.MvBackward()
        
  def PopTest(self):
    while self.Time<1.5*self.lenth:
      self.RunBlind()
      self.Time+=1
    self.Time=0    

    

#EVOLUTION
  def FindBestAgent(self):
    best=0
    x=0
    for agent in range(len(self.Pop)):#finds a better one if it exists
      if(self.Pop[agent].Alive and self.Pop[agent].posX_>x):
        best=agent
        x=self.Pop[agent].posX_
    return [best,x]
  

  def EvolveByDivision(self,IndivMax,MutationsRate,Generation=500):
    t=time.time()
    end=False;
    for i in range(Generation):
      self.PopTest()#fait résoudre le circuit à l'ensemble de la population
      self.SortByFitness()# tris les individus par fitness dans l'ordre décroissant
      if (self.Pop[0].posX_==len(self.Grid[0,:])-3):# verifie quaucun individu n'a complètement résolut le circuit
        end=True
      j=0
      PopBis=[]
      for agent in self.Pop:#chaque agent peut se reproduire dans la limite des places disponible. Les plus performent se reproduiront en premier
        if j<IndivMax:
          agent.posX_=4
          agent.posy_=2
          #agent.Mutate(MutationsRate,1)
          PopBis.append(agent)
          j+=1
          if j<IndivMax:
            G=Genome.Genome(25,3)
    """Add an agent to the list Pop"""
            G.Set_Map(agent.Genome_.Map_[:,:])
            A=Agent.Agent(4,2,G,self.Grid)
            A.Mutate(MutationsRate,1)
            PopBis.append(A)
            j+=1
      self.Pop=PopBis
      if end:
        return time.time()-t
    return time.time()-t

  def Evolve(self,Children,MutationsRate,Generation=500):
    t=time.time()
    end=False
    for i in range(Generation):
      self.PopTest()
      Father=self.Pop[self.FindBestAgent()[0]]
      if (Father.posX_==len(self.Grid[0,:])-3):
        end=True 
      self.Pop=[]
      for j in range(Children):
        G=Genome.Genome(25,3)
        G.Set_Map(Father.Genome_.Map_[:,:])
        A=Agent.Agent(4,2,G,self.Grid)
        if j!=0:
          A.Mutate(MutationsRate,1)
        self.AddAgent(A)
      if end:
        return time.time()-t
    return time.time()-t
  

if __name__ == '__main__':  
  w1=Game(L=60,H=18)
  w1.Random_Level_generation(7,100)
  """w1.AddBlockStratum(5,12)
  w1.AddBlockStratum(7,15)
  w1.AddBlockStratum(18,21)
  w1.MakePit(9)
  w1.MakePit(11)
  w1.MakePit(15)
  w1.MakePit(20)
  Gsucces=Genome.Genome(25,3)
  Gsucces.Set_Map(np.loadtxt("Bobby"))
  A2=Agent.Agent(4,2,Gsucces,w1.Grid)
  w1.AddAgent(A2)
  for i in range(5):
    Galea=Genome.Genome(25,3)
    A1=Agent.Agent(4,2,Gsucces,w1.Grid)
    A1.Mutate(100,0.95)
    w1.AddAgent(A1)"""
  #w1.printgridstep()
  #input('it works!') #Je sais pas pourquoi mais ça marche pas si cette ligne là est absente...

  """ g1=Game(8,30)
  print(g1.Grid==[[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
  g2=Game(3,2)
  print(g2.Grid==[[1,1],[1,1],[1,1]])
  print(g1.Pop==g2.Pop==[])
  agent=Agent.Agent(2,2,Genome.Genome(10,4),g1.Grid)
  g1.AddAgent(agent)
  print(g1.Pop==[agent])
  print(g1.Time==g2.Time==0)
  g1.step()
  g2.step()
  print(g1.Time==g2.Time==1)
  g1.MakePit(10)
  print(g1.Grid==[[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
  g1.MakePit(29)
  print(g1.Grid==[[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
  g1.MakePit(0)
  print(g1.Grid==[[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
  print(g1.Grid==[[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
  g1.AddBlockStratum(0,29)
  print(g1.Grid==[[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
  g1.AddBlockStratum(5,12)
  print(g1.Grid==[[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
  """

  
  """#test findbest agent
  w1.AddAgent(agent)
  print(agent.posX_)
  print(agent)
  print(A2.posX_)
  print(A2)
  best=w1.FindBestAgent()
  print(best.posX_)
  print(best)"""
  Galea=Genome.Genome(25,3)
  A1=Agent.Agent(4,2,Galea,w1.Grid)
  w1.AddAgent(A1)
  print(w1.EvolveByDivision(5,5)," seconde de calcule")
  w1.printgridstep()
  input('it works!') #Je sais pas pourquoi mais ça marche pas si cette ligne là est absente...
  w1.Pop=[]
  w1.AddAgent(A1)
  print(w1.Evolve(5,5)," seconde de calcule")
  w1.printgridstep()
  input('it works!') #Je sais pas pourquoi mais ça marche pas si cette ligne là est absente...
  for i in range(5):
    w1.Pop[i].posX_=i
  w1.SortByFitness()
  for agent in w1.Pop:
    print(agent.posX_)
  input('pause') 
  w1.New_Generation(1,5,5)
  for agent in w1.Pop:
    print(agent.posX_)  
  input('pause')
  w1.New_Generation(0,5,5)
  for agent in w1.Pop:
    print(agent.posX_)