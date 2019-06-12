#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:31:27 2019

@author: tpoquillon
"""

import Game
filenames=["Sauter","Grimper","Grimper2","Simple","Complex","tunnelTrap"]

Dict={}
DictM={}
for filename in filenames:
  w=Game.Game()
  w.File_to_map(filename+".txt")
  Dict[filename]=w
  w.printgridstep()
  input("pause")