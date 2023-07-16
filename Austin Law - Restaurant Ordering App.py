"""
Restaurant Ordering App
Written by Austin Law

Note: Make sure you have CustomTkinter installed to ensure the program runs as intended.
This can be done by typing "pip3 install customtkinter" in the command prompt when ran as administrator.
"""

# Importing the Modules
import customtkinter
from tkinter import *

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Restaurant Ordering App")
        self.attributes('-fullscreen',True)
        self.grid_columnconfigure((0,1), weight=1)

        # ---------------------------------- Frames ---------------------------------- #
        # Top Navigation Bar
        self.TopNavBarFrame = customtkinter.CTkFrame(self, corner_radius=0, height=75, fg_color="white")
        self.TopNavBarFrame.grid(column=0, row=0, sticky='nwes', columnspan=2)
        
        main_indicator = customtkinter.CTkFrame(self.TopNavBarFrame, corner_radius=5, height=6, width=100, fg_color="black")
        main_indicator.grid(row=0, column=0, sticky='s',pady=5)
        
        appetisers_indicator = customtkinter.CTkFrame(self.TopNavBarFrame, corner_radius=5, height=6, width=175, fg_color="white")
        appetisers_indicator.grid(row=0, column=1, sticky='s',pady=5)

        dessert_indicator = customtkinter.CTkFrame(self.TopNavBarFrame, corner_radius=5, height=6, width=140, fg_color="white")
        dessert_indicator.grid(row=0, column=2, sticky='s',pady=5)

        # Menu Selection
        self.menu_selection = customtkinter.CTkFrame(self, fg_color='red', corner_radius=0, height=1500)
        self.menu_selection.grid(column=0, row=1, sticky='news', columnspan=2)
        
        # Order List
        self.order_list = customtkinter.CTkFrame(self, corner_radius=0,  width=500, fg_color='blue')
        self.order_list.grid(column=2, row=0, rowspan= 2, sticky='nsew')


        # ---------------------------------- Widgets ---------------------------------- #
        # Buttons for the Top Navigation Bar
        main_btn = customtkinter.CTkButton(self.TopNavBarFrame, text="Mains", 
                                           font=customtkinter.CTkFont(size=30, weight='bold'), 
                                           fg_color="transparent", text_color="black", hover_color="gray",
                                           command=lambda: indicate(main_indicator))
        main_btn.grid(column=0, row=0, padx=10, pady=10, sticky='we')

        appetisers_btn = customtkinter.CTkButton(self.TopNavBarFrame, text="Appetisers", font=customtkinter.CTkFont(family="Caprasimo", size=30, weight='bold'), 
                                           fg_color="transparent",text_color="black", hover_color="gray", command=lambda: indicate(appetisers_indicator))
        appetisers_btn.grid(column=1, row=0, padx=10, pady=10, sticky='we')

        dessert_btn = customtkinter.CTkButton(self.TopNavBarFrame, text="Desserts", font=customtkinter.CTkFont(family="Playfair Display", size=30, weight='bold'), 
                                           fg_color="transparent",text_color="black", hover_color="gray", command=lambda: indicate(dessert_indicator))
        dessert_btn.grid(column=2, row=0, padx=10, pady=10, sticky='we')

        # Function for the indicator
        def hide_indicate():                    # Changes the indicators white to match the background of the top navigation frame
            main_indicator.configure(fg_color="white")
            appetisers_indicator.configure(fg_color="white")
            dessert_indicator.configure(fg_color="white")

        def indicate(fr):
            hide_indicate()                     # Calls the function to hide all indicators
            fr.configure(fg_color="black")      # The indicator associated with the button will turn black in color

        # Menu Selection for the Mains Page


app=App()
app.mainloop()