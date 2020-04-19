import tkinter as tk
import tkinter.font as tkFont
import os
import time

from nametag import *
from advert import *

# Configuration from the environment
def get_from_env(v, d):
  if v in os.environ and '' != os.environ[v]:
    return os.environ[v]
  else:
    return d
MY_NAME = get_from_env('MY_NAME', 'Glen')
MY_PRODUCT = get_from_env('MY_PRODUCT', 'open-horizon')

 
class pocketpi(tk.Tk):

  IMAGE_IBM='IBM.png';
  MESSAGE_IBM='Edge!';

  IMAGE_HORIZON='Horizon.png';
  MESSAGE_HORIZON='EdgeX';

  WIDTH = 640;
  HEIGHT = 480;

  # Times here are in milliseconds
  PAUSE = 5000;
  LONG_PAUSE = 30000;

  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs);
    self.attributes("-fullscreen", True);
    self.configure(background='white');

    # Create the top level container
    self.container = tk.Frame(self);
    self.container.pack(side="top", fill="both", expand=True);
    self.container.config(background='white', cursor='none');
    self.container.grid_rowconfigure(0, weight=1);
    self.container.grid_columnconfigure(0, weight=1);

    # Cretae a set of frames, only one of which will be shown at any moment
    self.frames = [];

    # The nametag frame
    fn = nametag(self.container, self, pocketpi.WIDTH, pocketpi.HEIGHT, MY_NAME);
    fn.grid(row=0, column=0, sticky="nsew")
    self.frames.append(fn);

    # The IBM Edge frame
    if "ibm" == MY_PRODUCT or "both" == MY_PRODUCT:
      fi = advert(self.container, self, pocketpi.WIDTH, pocketpi.HEIGHT, pocketpi.IMAGE_IBM, pocketpi.MESSAGE_IBM);
      fi.grid(row=0, column=0, sticky="nsew")
      self.frames.append(fi);

      # Insert the nametag frame again
      self.frames.append(fn);

    # The Open-Horizon frame
    if "open-horizon" == MY_PRODUCT or "both" == MY_PRODUCT:
      fo = advert(self.container, self, pocketpi.WIDTH, pocketpi.HEIGHT, pocketpi.IMAGE_HORIZON, pocketpi.MESSAGE_HORIZON);
      fo.grid(row=0, column=0, sticky="nsew")
      self.frames.append(fo);

    self.go = True;
    self.which = len(self.frames) - 1;
    self.pause = pocketpi.PAUSE;
    self.after(0, self.animate);
    self.mainloop();

  def next(self):
    self.which += 1;
    if self.which >= len(self.frames):
      self.which = 0;
    self.frames[self.which].tkraise();

  def quit(self):
    self.go = False;
    if self._job is not None:
      self.after_cancel(self._job)
    self.destroy();

  def touch(self, details):
    if self._job is not None:
      self.after_cancel(self._job)
    self.next()
    self._job = self.after(pocketpi.LONG_PAUSE, self.animate);

  def animate(self):
    if self.go:
      self.next();
      self._job = self.after(pocketpi.PAUSE, self.animate);

def main():
  pocketpi();

if __name__ == '__main__':
  main();


