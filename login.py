from tkinter import *
import customtkinter
# from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.title('Login')
app.geometry('600x440')

l1 = customtkinter.CTkLabel(master=app)
l1.pack()  

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.grid(row=0, column=0, pady=30)

l2=customtkinter.CTkLabel(master=frame, text="Login into your Account", font=('century Gothic', 20))
l2.place(x=50,y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
entry1.place(x=50,y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password")
entry2.place(x=50,y=165)

l2=customtkinter.CTkLabel(master=frame, text="Forget Password", font=('century Gothic', 12))
l2.place(x=165,y=195)

button1 = customtkinter.CTkButton(master=frame, width=220, text='Login', corner_radius=6)
button1.place(x=50,y=240)

button2 = customtkinter.CTkButton(master=frame, width=220, text='Sign up', corner_radius=6)
button2.place(x=50,y=280)

app.mainloop()
