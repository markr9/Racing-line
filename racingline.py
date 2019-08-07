# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:50:26 2019

@author: MR
"""

#racing line radius
from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox as box
import numpy as np

class Gui:
    
    def __init__(self):    
        win=Tk()
        win.title('Racing Line')
        self.txradius=Label(win,text='Radius (m)')
        self.radius=Entry(win)
        self.txwidth=Label(win,text='Track width (m)')
        self.width=Entry(win)
        self.txangle=Label(win,text='Angle (deg)')
        self.angle=Entry(win)
        self.txoutput=Label(win,text='Racing line radius (m)')
        self.output=Label(win,text='Output')
        self.btnenter=Button(win,text='Enter')
        self.pos()
        self.command()
        win.mainloop()
        
    def pos(self):
        self.txradius.grid(row=1,column=1)
        self.radius.grid(row=2,column=1)
        self.txwidth.grid(row=1,column=2)
        self.width.grid(row=2,column=2)
        self.txangle.grid(row=1,column=3)
        self.angle.grid(row=2,column=3)
        self.txoutput.grid(row=3,column=1)
        self.output.grid(row=3,column=2,columnspan=2)
        self.btnenter.grid(row=4,column=1)
        
    def command(self):
        self.btnenter.configure(command=self.calculate)
        
    def calculate(self):
        try: 
            float(self.radius.get())
        except Exception:
            box.showerror(message='Non-numeric entered!')
            return
        try: 
            float(self.width.get())
        except Exception:
            box.showerror(message='Non-numeric entered!')
            return
        try: 
            float(self.angle.get())
        except Exception:
            box.showerror(message='Non-numeric entered!')
            return
        output=float(self.width.get())/(np.sin((float(self.angle.get())*np.pi/180)/2)*np.tan((float(self.angle.get())*np.pi/180)/4))
        txoutput=str(output+float(self.radius.get()))+' with constant for angle of (m) '+str(output)
        self.output.configure(text=txoutput)
        
gui=Gui()