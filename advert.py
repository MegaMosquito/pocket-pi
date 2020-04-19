import tkinter as tk
import tkinter.font as tkFont 
from PIL import ImageTk, Image  

class advert(tk.Frame):

  ASK_MESSAGE = "Ask me about:  ";
  ASK_PORTION = 0.25;

  IMAGE_PORTION = 0.4;
  IMAGE_CENTER_H = 0.5;
  TEXT_CENTER_H = 0.8;

  def __init__(self, parent, controller, w, h, img, txt):

    tk.Frame.__init__(self, parent);
    self.controller = controller;
    self.w = w;
    self.h = h;

    # Create a canvas to draw in
    self.canvas = tk.Canvas(self, bg='white', width=self.w, height=self.h);
    self.canvas.pack();

    # Setup the background rectangles
    self.toprect = self.canvas.create_rectangle(0, 0, self.w, advert.ASK_PORTION * self.h, fill="blue")
    self.bottomrect = self.canvas.create_rectangle(0, advert.ASK_PORTION * self.h, self.w, self.h, fill="white")

    # Get the image and resize it appropriately
    i = Image.open(img);
    [iw, ih] = i.size;
    new_ih = int(advert.IMAGE_PORTION * self.h);
    new_iw = int((iw / float(ih)) * new_ih);
    i = i.resize((new_iw, new_ih), Image.ANTIALIAS)
    self.i = ImageTk.PhotoImage(i)
    self.text = txt;

    # Draw the "ask me" message on the top
    hifont = tkFont.Font(family="Helvetica",size=48,weight="bold")
    self.hi = self.canvas.create_text(self.w / 2.0, (advert.ASK_PORTION / 2.0) * self.h, fill="white", font=hifont, justify=tk.CENTER, text=advert.ASK_MESSAGE)

    # Draw the image in the Middle
    self.image = self.canvas.create_image(self.w / 2.0, advert.IMAGE_CENTER_H * self.h, anchor=tk.CENTER, image=self.i)

    # Draw the text below
    namefont = tkFont.Font(family="Helvetica",size=80,weight="bold")
    self.name = self.canvas.create_text(self.w / 2.0, advert.TEXT_CENTER_H * self.h, fill="navy", font=namefont, justify=tk.CENTER, text=self.text)

    # Bind the mouse button action, and update
    self.canvas.bind("<Button-1>", self.controller.touch)
    self.canvas.update()
