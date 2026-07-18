# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk

import screeninfo
from PIL import Image, ExifTags, ImageTk
from screeninfo import get_monitors
Lake = 'Res/BackGroundLake.jpg'
League = 'Res/Aatrox.jpg'
Monitors = screeninfo.get_monitors()
PrimaryMonitor = Monitors[0]
MonitorHeight =  PrimaryMonitor.height
MonitorWidth =  PrimaryMonitor.width
print(MonitorHeight)
print(MonitorWidth)
def PopUpImage(ImagePath):
    ScaledImage = ScaleImage(ImagePath)
    tk_image = ImageTk.PhotoImage(ScaledImage)
    label = tk.Label(root, image=tk_image, bg='black')
    label.pack(expand=True, fill=tk.BOTH)
def ScaleImage(ImagePath):
    img = Image.open(ImagePath)

    with Image.open(ImagePath) as img_buffer:
        ImageWidth = img_buffer.width
        ImageHeight = img_buffer.height


        ScaleHeight = MonitorHeight/ImageHeight
        ScaleWidth = MonitorWidth/ImageWidth

        ScaledImage = img_buffer.resize((MonitorWidth,MonitorHeight),  Image.LANCZOS)
        print(ImageWidth )
        print(f"\n + {ImageHeight}")
    # exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}

    return ScaledImage
def OnKeyPress(event):
    if event.char == 'W':
        PopUpImage(Lake)
        print("Switching to Cloud!")
    elif event.char == 'P':
        PopUpImage(League)
    else:
        print("Unrecongized")


if __name__ == '__main__':
    root = tk.Tk()
    root.attributes('-fullscreen', True) #removes that funky stuff
    root.bind("<Key>", OnKeyPress)
    root.bind("<Escape>", lambda event: root.destroy())

    root.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
