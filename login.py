from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root =customtkinter.CTk()
root.title('Tkinter.com - Custom Tkinter Buttons')
# root.iconbitmap('images/codemy.ico')
root.geometry('600x350')

def hello():
    print("Hello")


my_button = customtkinter.CTkButton(root, text="Hello world",command=hello)
my_button.grid(row = 0 , column = 0 ,pady=80)
my_button_1 = customtkinter.CTkButton(root, text="Hello world",command=hello)
my_button_1.grid(row = 0 , column = 1,pady=5)
root.mainloop()
