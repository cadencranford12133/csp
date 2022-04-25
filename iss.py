import tkinter as tk
from turtle import onclick
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import json
from setuptools import setup
import config as cfg

def get_iss_location(url:str):
    try:
        iss_request = urlopen(url)
        iss_location = json.loads(iss_request.read)

        print(iss_location)

        longitude = iss_location['iss_postition']['longitude']
        latitude = iss_location['iss_postition']['latitude']

        return longitude, latitude
    except Exception as e:
        print(str(e))
        root.quit()




def refresh(x):
    pass

#Window setup
root= tk.TK()
root.title("Map program - International space station Location")
root.geometry('600x600')

display_map = tk.Label(root,font=('Arial 18 bold'),fg='red')
display_map.bind('<Buttion',refresh)
display_map.grid(row=0, column=0)

longitude, latitude = get_iss_location('https://api.open-notify.org/iss-now.json')

root.mainloop()