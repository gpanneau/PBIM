import tkinter as tk

class CreateWorld(tk.Canvas):
	def __init__(self, fenetre):
		tk.Canvas.__init__(self, width = 1000, height = 300, highlightthickness=0,bg="green")
		self.size_in_pixels = 1000
				
	def draw_grid(self, Grid):
		self.w = len(Grid[0])
		self.h = len(Grid)
		self.pixels_height = int(self.size_in_pixels)/self.w
		self.pixels_width = int(self.size_in_pixels)/self.w
		#self.pixels_height = int(self.size_in_pixels)/self.h
		#self.pixels_width = int(self.size_in_pixels)/self.w
		for i in range(self.h):
		    for j in range(self.w):
		        if (Grid[i][j]==0):
		            self.create_rectangle(j*self.pixels_width,i*self.pixels_height, (j+1)*self.pixels_width,(i+1)*self.pixels_height,fill="blue", width=0)
		        elif (Grid[i][j]==2):
		            #imglabel = tk.Label(image=self.img)
		            self.create_rectangle(j*self.pixels_width,i*self.pixels_height, (j+1)*self.pixels_width,(i+1)*self.pixels_height,fill="blue", width=0)
		            self.create_oval(j*self.pixels_width,i*self.pixels_height, (j+1)*self.pixels_width,(i+1)*self.pixels_height,fill="cyan", width=0)
		            self.create_oval((0.5+j)*self.pixels_width,(i+0.2)*self.pixels_height, (j+1-0.2)*self.pixels_width,(i+1-0.4)*self.pixels_height,fill="white")
		            self.create_oval((0.65+j)*self.pixels_width,(i+0.3)*self.pixels_height, (j+1-0.25)*self.pixels_width,(i+1-0.6)*self.pixels_height,fill="black")
		            
		
