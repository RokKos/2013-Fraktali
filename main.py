from tkinter import *
from PIL import Image, ImageTk
from mandelbrot import *


class App(object):
    def __init__(self, master):
        self.ulx, self.uly, self.drx, self.dry, self.def_width = default_settings()
        self.image = ImageTk.PhotoImage(make_fractal(*default_settings()))
        self.canvas = Canvas(master, width=self.image.width(), height=self.image.height())
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.image, anchor=NW)
        
        self.canvas.bind('<ButtonPress-1>', self.press)
        self.canvas.bind('<ButtonRelease-1>', self.release)
        self.canvas.bind('<B1-Motion>', self.motion)

    def press(self, event):
        self.sx, self.sy = event.x, event.y

    def release(self, event):
        self.ex, self.ey = event.x, event.y
        self.sx, self.ex = sorted([self.ex, self.sx])
        self.sy, self.ey = sorted([self.ey, self.sy])

        sysw = self.drx - self.ulx
        sysh = self.uly - self.dry
        imw, imh = self.image.width(), self.image.height()

        oldx, oldy = self.ulx, self.dry

        self.ulx = oldx + self.sx/imw*sysw
        self.uly = oldy + self.ey/imh*sysh
        self.drx = oldx + self.ex/imw*sysw
        self.dry = oldy + self.sy/imh*sysh

        self.update_image()

    def motion(self, event):
        if self.sx == -1: return
        ex, ey = event.x, event.y
        try:
            self.canvas.delete(self.rect)
        except: pass
        finally:
            self.rect = self.canvas.create_rectangle((self.sx, self.sy, ex, ey), fill='',
                    outline='white')

    def update_image(self):
        img  = make_fractal(self.ulx, self.uly, self.drx, self.dry, self.def_width)
        self.image = ImageTk.PhotoImage(img)
        self.canvas.config(width=self.image.width(), height=self.image.height())
        self.canvas.create_image(0,0,image=self.image,anchor=NW)

root = Tk()
app = App(root)
root.mainloop()
