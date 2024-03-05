from tkinter import *
import customtkinter
from tkinter import messagebox

# from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


    
app = customtkinter.CTk()
app.title('Login')
app.geometry('600x440')
    

    #Sign UP Page 

def button_function():
        app.destroy()
        w=customtkinter.CTk()
        w.geometry('600x440')
        w.title('welcome')

        #Message Box
        def sign_up():
         messagebox.showinfo("Sign Up", "SIGN UP SUCCESSFULLY")


        frame = customtkinter.CTkFrame(master=w, width=340, height=380, corner_radius=15)
        frame.grid(row=0, column=1, padx=130, pady=30)
        l3=customtkinter.CTkLabel(master=frame, text="Sign up Account", font=('Century Gothic', 20))
        l3.place(x=70, y=30)

        entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
        entry1.place(x=60,y=100)

        entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Email")
        entry2.place(x=60,y=150)   

        entry3 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password")
        entry3.place(x=60, y=200)
    
        entry4 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Confirm Password")
        entry4.place(x=60, y=250)

        button1 = customtkinter.CTkButton(master=frame, width=100, text='SIGIN UP', corner_radius=6, compound="left", text_color='black', command=sign_up)
        button1.place(x=180,y=300)

        button2 = customtkinter.CTkButton(master=frame, width=100, text='BACK', corner_radius=6, compound="left", text_color='black')
        button2.place(x=60,y=300)
        w.mainloop()


    #LOGIN PAGE

def button_function1():
        app.destroy()
        z=customtkinter.CTk()
        z.geometry('600x440')
        z.title('LOGIN PAGE')
        l4=customtkinter.CTkLabel(master=z, text="Login Successfully", font=('Century Gothic', 20))
        l4.grid(row=0, column=1, padx=220, pady=170)
        z.mainloop()

l1 = customtkinter.CTkLabel(master=app)
l1.pack()  

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.grid(row=0, column=0, pady=30)

l2=customtkinter.CTkLabel(master=frame, text="Login into your Account", font=('Century Gothic', 20))
l2.place(x=50,y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
entry1.place(x=50,y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password")
entry2.place(x=50,y=165)

l2=customtkinter.CTkLabel(master=frame, text="Forget Password", font=('century Gothic', 12))
l2.place(x=165,y=195)

button1 = customtkinter.CTkButton(master=frame, width=100, text='LOGIN', corner_radius=6, compound="left", text_color='black', command=button_function1)
button1.place(x=50,y=240)

button2 = customtkinter.CTkButton(master=frame, width=100, text='SIGN UP', corner_radius=6, compound="left", text_color='black', command=button_function)
button2.place(x=170,y=240)

app.mainloop()

