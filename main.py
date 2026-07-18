# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
from PIL import Image
Lake = 'Res/BackGroundLake.jpg'
League = 'Res/Aatrox.jpg'
def PopUpImage(ImagePath):
    img = Image.open(ImagePath)
    img.show()
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
    root.bind("<Key>", OnKeyPress)
    root.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
