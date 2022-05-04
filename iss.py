import tkinter as tk
from turtle import onclick
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import json
import config as cfg

def get_image(url:str):
    pic = urlopen(url)
    raw_d = pic.read()
    pic.close()

raw_image = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(raw_image)

display_map.configure(text='--||--',compound=tk.CENTER,image=photo)
display_map.image = photo
display_map.grid(row=0, column=0)

print('Map updated...')


def get_iss_location(url:str):
    try:
        iss_request = urlopen(url)
        iss_location = json.loads(iss_request.read())


        longitude = iss_location['iss_position']['longitude']
        latitude = iss_location['iss_position']['latitude']

        return longitude, latitude
    except Exception as e:
        print(str(e))
        root.quit()




def refresh(x):
    # Using the api to find locatioo of ISS
    longitude, latitude = get_iss_location('http://api.open-notify.org/iss-now.json')
    print('Location obtained...')

    print('Getting map...')
    sat_pic_url="https://api.tomtom.com/map/1/staticimage?layer=basic&style=main&format=png&zoom=02&center="+ str(longitude) +"%2cC"+ str(latitude) + "&width=512&height=512&view=Unified&key=" + cfg.TOMTOM_API_KEY
    get_image(sat_pic_url)

#Window setup
root= tk.Tk()
root.title("Map program - International space station Location")

display_map = tk.Label(root,font=('Arial 18 bold'),fg='red')
display_map.bind('<Button>',refresh)


refresh(1)

root.mainloop()
