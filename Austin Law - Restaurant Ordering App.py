"""
Restaurant Ordering App
Written by Austin Law

Note: Make sure you have CustomTkinter installed to ensure the program runs as intended.
This can be done by typing "pip3 install customtkinter" in the command prompt when ran as administrator.
"""

# Importing the Modules
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Title of the App
        self.title("Testing")

        # Dimensions for the window
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        # Configuring the gridding of the window
        self.grid_columnconfigure(0, weight=1)

        # Frame for the Top Navigation Bar
        self.TopNavBarFrame = customtkinter.CTkFrame(self, corner_radius=0, height=75, fg_color="white")
        self.TopNavBarFrame.grid(column=0, row=0, sticky='we')


app=App()
app.mainloop()