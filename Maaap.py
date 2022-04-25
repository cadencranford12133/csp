
import tkinter as tk
from turtle import onclick
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import json
from parted import Geometry

from setuptools import setup
import config as cfg

def refresh(x):
    pass

#Window setup
root= tk.TK()
root.title("Map program - International space station Location")
root.geometry('600x600')

display_map = tk.Label(root,font=('Arial 18 bold'),fg='red')
display_map.bind('<Buttion',refresh)

root.mainloop()