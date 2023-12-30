from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


window = Tk()
window.title("Secret Notes")
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

def button1_clicked():
    pass

def button2_clicked():
    pass

button1 = Button(text="Save & Encrypt",command=button1_clicked)
button1.pack()
button2 = Button(text="Decrypt",command=button2_clicked)
button2.pack()

window.mainloop()
