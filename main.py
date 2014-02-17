from tkinter import *
from PIL import Image, ImageTk
from mandelbrot import *


class App(object):
    def __init__(self, master):
        self.ulx, self.uly, self.drx, self.dry, self.def_width = default_settings()
        self.image = ImageTk.PhotoImage(make_fractal(*default_settings()))
        self.img_label = Label(image=self.image)
        self.img_label.image = self.image
        self.img_label.pack()
        
        self.img_label.bind('<ButtonPress-1>', self.press)
        self.img_label.bind('<ButtonRelease-1>', self.release)

    def press(self, event):
        self.sx, self.sy = event.x, event.y

    def release(self, event):
        self.ex, self.ey = event.x, event.y
        self.sx, self.ex = sorted([self.ex, self.sx])
        self.sy, self.ey = sorted([self.ey, self.sy])

        sysw = self.drx - self.ulx
        sysh = self.uly - self.dry
        imw = self.image.width()
        imh = self.image.height()


        oldx, oldy = self.ulx, self.dry

        self.ulx = oldx + self.sx/imw*sysw
        self.uly = oldy + self.ey/imh*sysh
        self.drx = oldx + self.ex/imw*sysw
        self.dry = oldy + self.sy/imh*sysh

        self.update_image()

    def update_image(self):
        img  = make_fractal(self.ulx, self.uly, self.drx, self.dry, self.def_width)
        self.image = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.image)
        self.img_label.image = self.image

root = Tk()
app = App(root)
root.mainloop()
