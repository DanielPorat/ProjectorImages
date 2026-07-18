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
Disabled = 'Res/Disabled.webp'
Town = 'Res/CoolBackgroundNotFlipped.png'
FRCgoat = 'Res/FRCgoat.png'
UnnamedFriend = 'Res/UnnamedFriend.png'
Max = 'Res/Max.jpg'
ScreenWarpMP = 'Res/ScreenWarp.mp4'
LebronMP = 'Res/LebronJames.mp4'
JustDoItMP = 'Res/JustDoit.mp4'
EyesMP = 'Res/EyesBack.mp4'

Monitors = screeninfo.get_monitors()
PrimaryMonitor = Monitors[0]

MonitorHeight =  PrimaryMonitor.height
MonitorWidth =  PrimaryMonitor.width
print(MonitorHeight)
print(MonitorWidth)

CurrentKey = None
Captured = None
CurrentVid = None #Checks the current video

def CancelStream():
    global CurrentVid
    if CurrentVid is not None:
        root.after_cancel(CurrentVid)
        CurrentVid = None
def PopUpVideo(VideoPath):
    global Captured
    CancelStream()
    Release()
    if Captured is not None:
        Captured.release()#releases the place it holds it in ram
    Captured = cv2.VideoCapture(VideoPath)
    Steam()
def Steam():
    global Captured, CurrentVid
    if Captured is not None and Captured.isOpened():
        ret, frame = Captured.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            resized_frame = cv2.resize(rgb_frame, (MonitorWidth, MonitorHeight))

            img = Image.fromarray(resized_frame)
            tk_image = ImageTk.PhotoImage(image=img)

            old_image = label.cget('image')
            if old_image:
                root.tk.call('image', 'delete', old_image)

            label.config(image=tk_image)
            label.image = tk_image

            CurrentVid = root.after(17, Steam)  #Reruns every 33 miliseconds
        else:

            Captured.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = Captured.read()

            CurrentVid = root.after(17, Steam)


def PopUpImage(ImagePath, flip=False):
    CancelStream()
    Release()
    ScaledImage = ScaleImage(ImagePath,flip)
    tk_image = ImageTk.PhotoImage(ScaledImage)
    label.config(image=tk_image)
    label.image = tk_image

def ScaleImage(ImagePath, flip=False):
    img = Image.open(ImagePath)

    with Image.open(ImagePath) as img_buffer:
        if flip:
            img_buffer = img_buffer.transpose(Image.ROTATE_90)

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
def Release():
    global Captured
    if Captured is not None:
        Captured.release()
        Captured = None
def OnKeyPress(event):
    global Captured
    CurrentKey = event.char


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
    elif event.char == 'T':
        PopUpImage(Town,flip=True)
        print("Town")
    elif event.char == 'F':
        PopUpImage(FRCgoat)
        print("FRC")
    elif event.char == 'X':
        PopUpImage(UnnamedFriend)
        print("Tyson")
    elif event.char == 'M':
        PopUpImage(Max)
        print("Max")
    elif event.char == 'w':
        PopUpVideo(ScreenWarpMP)
        print("VideoTime")
    elif event.char == 'p':
        PopUpVideo(LebronMP)
        print("Lebron")
    elif event.char == 'j':
        PopUpVideo(JustDoItMP)
        print("Just Do it!")
    elif event.char == 'e':
        PopUpVideo(EyesMP)
        print("Just Do it!")

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

    CancelStream()
    Release()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
