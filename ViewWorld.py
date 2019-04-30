import tkinter as tk

class CreateWorld(tk.Canvas):
	def __init__(self, fenetre):
		tk.Canvas.__init__(self, width = 1000, height = 1000, highlightthickness=0,bg="green")
		self.size_in_pixels = 1000
    
	def draw_grid(self, Mygrid):
		self.w = len(Mygrid[0])
		self.h = len(Mygrid)
		self.pixels_height = int(self.size_in_pixels)/self.h
		self.pixels_width = int(self.size_in_pixels)/self.w
		for i in range(self.h):
		    for j in range(self.w):
		        if (Mygrid[i][j]==0):
		            self.create_rectangle(j*self.pixels_width,i*self.pixels_height, (j+1)*self.pixels_width,(i+1)*self.pixels_height,fill="blue")
		        elif (Mygrid[i][j]==2):
		            self.create_rectangle(j*self.pixels_width,i*self.pixels_height, (j+1)*self.pixels_width,(i+1)*self.pixels_height,fill="red")
