# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk

import screeninfo
from PIL import Image, ExifTags, ImageTk
from screeninfo import get_monitors
from tkVideoPlayer import TkinterVideo
Lake = 'Res/BackGroundLake.jpg'
League = 'Res/Aatrox.jpg'
ScreenWarpMP = 'Res/ScreenWarp.mp4'

Monitors = screeninfo.get_monitors()
PrimaryMonitor = Monitors[0]

MonitorHeight =  PrimaryMonitor.height
MonitorWidth =  PrimaryMonitor.width
print(MonitorHeight)
print(MonitorWidth)

CurrentKey = None
rootVideo = tk.Tk()
videoplayer = TkinterVideo(master=rootVideo, scaled=True)
def PopUpVideo(VideoPath):
    ScaledVideo = ScaleVideo(VideoPath)
    tk_image = ImageTk.PhotoImage(ScaledVideo)
    label.config(image=tk_image)
    label.image = tk_image
def ScaleVideo(VideoPath):
    Video = videoplayer.load(VideoPath)
    ScaledVideo = Video.set_scaled(True)
    videoplayer.pack(expand=True, fill="both")
    return ScaledVideo
def PopUpImage(ImagePath):
    ScaledImage = ScaleImage(ImagePath)
    tk_image = ImageTk.PhotoImage(ScaledImage)
    label.config(image=tk_image)
    label.image = tk_image

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
# def SetCurrentKey(event):
#     return event.char Didnt work
def OnKeyPress(event):
    CurrentKey = event.char
    if event.char == 'W':
        PopUpImage(Lake)
        print("Switching to Cloud!")
    elif event.char == 'P':
        PopUpImage(League)
        print("Switching to Aatrox!")
    elif event.char == 'w':
        PopUpVideo()
    elif None:
        print("select a valid key")
    else:
        print("Unrecongized")


if __name__ == '__main__':
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # removes that funky stuff
    # root.bind("<Key>", SetCurrentKey)


    label = tk.Label(root, bg='black')
    label.pack(expand=True, fill=tk.BOTH)
    videoplayer.play()

    root.bind("<Key>", OnKeyPress)
    root.bind("<Escape>", lambda event: root.destroy())

    root.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
