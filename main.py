# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk

import screeninfo
from PIL import Image, ExifTags, ImageTk
from screeninfo import get_monitors
import cv2

Lake = 'Res/BackGroundLake.jpg'
League = 'Res/Aatrox.jpg'
ScreenWarpMP = 'Res/ScreenWarp.mp4'
LebronMP = 'Res/LebronJames.mp4'
Disabled = 'Res/Disabled.webp'

Monitors = screeninfo.get_monitors()
PrimaryMonitor = Monitors[0]

MonitorHeight =  PrimaryMonitor.height
MonitorWidth =  PrimaryMonitor.width
print(MonitorHeight)
print(MonitorWidth)

CurrentKey = None
Captured = None
def PopUpVideo(VideoPath):
    global Captured
    if Captured is not None:
        Captured.release()#releases the place it holds it in ram
    Captured = cv2.VideoCapture(VideoPath)
    Steam()
def Steam():
    global Captured
    if Captured is not None and Captured.isOpened():
        ret, frame = Captured.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            resized_frame = cv2.resize(rgb_frame, (MonitorWidth, MonitorHeight))

            img = Image.fromarray(resized_frame)
            tk_image = ImageTk.PhotoImage(image=img)

            label.config(image=tk_image)
            label.image = tk_image

            root.after(33, Steam) #Reruns every 33 miliseconds
        else:
            # Video ended? Stop it (or you can add logic to loop here)
            Captured.release()

            root.after(33, Steam) 


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
    global Captured
    CurrentKey = event.char
    if Captured is not None:
        Captured.release()

    if event.char == 'W':
        PopUpImage(Lake)
        print("Switching to Cloud!")
    elif event.char == 'P':
        PopUpImage(League)
        print("Switching to Aatrox!")
    elif event.char == 'D':
        PopUpImage(Disabled)
        #My friend requested this not me.
        print("Disabled Image here")
    elif event.char == 'w':
        PopUpVideo(ScreenWarpMP)
        print("VideoTime")
    elif event.char == 'p':
        PopUpVideo(LebronMP)
        print("Lebron")

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

    root.bind("<Key>", OnKeyPress)
    root.bind("<Escape>", lambda event: root.destroy())

    root.mainloop()
    if Captured is not None:
        Captured.release()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
