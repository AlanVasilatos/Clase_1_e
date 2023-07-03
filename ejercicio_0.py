from customtkinter import *

app = CTk()

def button_ok_click():
    print("vamos a aprender phyton!!")


button = CTkButton( master=app, text="Click me!", command=button_ok_click)
button.grid()

app.mainloop()