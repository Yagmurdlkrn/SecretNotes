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
    title = text1.get("1.0", END)
    message = text2.get("1.0", END)
    secret = text3.get("1.0", END)

    if len(title) == 0 or len(message) == 0 or len(secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        message_encrypted = encode(secret, message)

        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f'\n{title}\n{message_encrypted}')
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f'\n{title}\n{message_encrypted}')
        finally:
            text1.delete("1.0", END)
            text3.delete("1.0", END)
            text2.delete("1.0", END)


def button2_clicked():
    message_encrypted = text2.get("1.0", END)
    secret = text3.get("1.0", END)

    if len(message_encrypted) == 0 or len(secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(secret, message_encrypted)
            text2.delete("1.0", END)
            text2.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")

button1 = Button(text="Save & Encrypt",command=button1_clicked)
button1.pack()
button2 = Button(text="Decrypt",command=button2_clicked)
button2.pack()

window.mainloop()
