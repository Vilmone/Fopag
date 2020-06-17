from PIL import Image
from PIL import ImageTk
import tkinter

image = Image.open('img.png')
image = image.resize((20, 20))
image = ImageTk.PhotoImage(image)

canv = Canvas(root, width=80, height=80, bg='white')
canv.grid(row=2, column=3)

img = PhotoImage(file=image)