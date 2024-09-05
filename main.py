from tkinter import *
from tkinter import PhotoImage
import threading
import qrcode
from tkinter import messagebox
class QRGenerator:
    def __init__(self):
        self.root=Tk()
        self.root.title('QRCode Generator')
        self.root.geometry("380x380")
        self.root.resizable(False, False)
        self.title= Label(text="Enter your link in this text box",anchor=CENTER,font=("Calibri",18))
        self.title.pack(pady=20)
        self.input= Entry(width=100)
        self.input.pack()
        self.button=Button(text="Generate QR Code", font=("Calibri",12),justify="center",overrelief="raised",command=self.click)
        self.button.pack(pady=10)
        self.image_label = Label(self.root)
        self.image_label.pack()
        self.generate=False
        self.root.mainloop()
    def click(self):
        if self.generate:
            self.generate=False
            self.button.config(fg='black')

        else:
            self.generate=True
            self.button.config(fg='blue',state=DISABLED)
            threading.Thread(target=self.generate_code).start()
    def generate_code(self):
        input_text= self.input.get()
        if len(input_text)<10 or (input_text.find('https://')==-1):
            messagebox.showwarning("Input Error", "Please enter valid URL.")
            self.button.config(fg='black',state=NORMAL)
            self.generate = False
            return
        img = qrcode.make(input_text)
        image=img.resize((250,250))
        image.save('MyQRCode1.png')
        self.photo = PhotoImage(file='MyQRCode1.png')
        self.image_label.config(image=self.photo)
        self.button.config(state=NORMAL)
        self.generate = False
        self.input.delete(END)
QRGenerator()
