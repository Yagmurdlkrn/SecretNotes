from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Secret Quiz")
window.minsize(width=300, height=600)

# Resmi aç
image = Image.open("topsecret.png")

# Resmi istediğiniz boyutlara boyutlandır
resized_image = image.resize((200, 120))

# Tkinter PhotoImage'a dönüştür
image = ImageTk.PhotoImage(resized_image)

imageLabel = Label(window, image=image)
imageLabel.pack()

window.mainloop()
