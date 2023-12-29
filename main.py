from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Secret Quiz")
window.minsize(width=300, height=600)


image = Image.open("topsecret.png")


resized_image = image.resize((200, 120))


image = ImageTk.PhotoImage(resized_image)

imageLabel = Label(window, image=image)
imageLabel.pack()

label1 = Label(text="Enter your title")
label1.pack()
text1 = Text(width=30,height=2)
text1.pack()

label2 = Label(text="Enter your secret")
label2.pack()
text2 = Text(width=30,height=15)
text2.pack()

label3 = Label(text="Enter your master key")
label3.pack()
text3 = Text(width=30,height=2)
text3.pack()

button1 = Button(text="Save & Encrypt")
button2 = Button(text="Decrypt")
button1.pack()
button2.pack()

window.mainloop()
