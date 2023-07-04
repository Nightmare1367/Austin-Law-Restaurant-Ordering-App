"""
Restaurant Ordering App
Written by Austin Law

Note: Make sure you have CustomTkinter installed to ensure the program runs as intended.
This can be done by typing "pip3 install customtkinter" in the command prompt when ran as administrator.
"""
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Testing")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))


app=App()
app.mainloop()