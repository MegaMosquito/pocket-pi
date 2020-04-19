import tkinter as tk
import tkinter.font as tkFont 

class nametag(tk.Frame):

  HI_MESSAGE = "Hello, my name is:"
  HI_PORTION = 0.25

  def __init__(self, parent, controller, w, h, name):

    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.w = w
    self.h = h

    # Create a canvas to draw in
    self.canvas = tk.Canvas(self, bg='white', width=self.w, height=self.h)
    self.canvas.pack()

    # Setup the background rectangles
    self.hirect = self.canvas.create_rectangle(0, 0, self.w, nametag.HI_PORTION * self.h, fill="red")
    self.namerect = self.canvas.create_rectangle(0, nametag.HI_PORTION * self.h, self.w, self.h, fill="white")

    # Draw the "Hi" message on the top
    hifont = tkFont.Font(family="Helvetica",size=48,weight="bold")
    self.hi = self.canvas.create_text(self.w / 2.0, (nametag.HI_PORTION / 2.0) * self.h, fill="white", font=hifont, justify=tk.CENTER, text=nametag.HI_MESSAGE)

    # Draw the name below that
    NAMEFONT = tkFont.Font(family="Helvetica",size=128,weight="bold")
    self.name = self.canvas.create_text(self.w / 2.0, (nametag.HI_PORTION + (1 - nametag.HI_PORTION) / 2.0) * self.h, fill="black", font=NAMEFONT, justify=tk.CENTER, text=name)

    # Bind the mouse button action, and update
    self.canvas.bind("<Button-1>", self.controller.touch)
    self.canvas.update()
