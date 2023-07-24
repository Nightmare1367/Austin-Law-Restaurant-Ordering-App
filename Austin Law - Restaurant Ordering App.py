"""
Restaurant Ordering App
Written by Austin Law

Note: Make sure you have CustomTkinter installed to ensure the program runs as intended.
This can be done by typing "pip3 install customtkinter" in the command prompt when ran as administrator.

You would also want to make sure that pillow is installed. 
This is done by typing "pip install --upgrade pip" and "pip install --upgrade Pillow" 
into the command prompt to install the 
"""

# Importing the Modules
import customtkinter
from tkinter import *
from PIL import Image, ImageTk

class TopNavBar(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # ---------------------------------- Widgets ---------------------------------- #
        # region | Buttons for the Top Navigation Bar
        mains_btn = customtkinter.CTkButton(self, text="Mains", 
                                           font=customtkinter.CTkFont(family="Calibri", size=35), 
                                           fg_color="transparent", text_color="black", hover_color="gray",
                                           command=lambda: indicate(mains_indicator, mains_page))
        mains_btn.grid(column=0, row=0, padx=10, pady=10, sticky='we')

        appetisers_btn = customtkinter.CTkButton(self, text="Appetisers", 
                                                 font=customtkinter.CTkFont(family="Calibri", size=35), 
                                                 fg_color="transparent",text_color="black", hover_color="gray", 
                                                 command=lambda: indicate(appetisers_indicator, appetisers_page))
        appetisers_btn.grid(column=1, row=0, padx=10, pady=10, sticky='we')

        dessert_btn = customtkinter.CTkButton(self, text="Desserts", 
                                              font=customtkinter.CTkFont(family="Calibri", size=35), 
                                              fg_color="transparent",text_color="black", hover_color="gray", 
                                              command=lambda: indicate(dessert_indicator))
        dessert_btn.grid(column=2, row=0, padx=10, pady=10, sticky='we')
        # endregion

        # region | Frames which would act as an indicator for the buttons
        mains_indicator = customtkinter.CTkFrame(self, corner_radius=5, height=6, width=100, fg_color="black")
        mains_indicator.grid(row=0, column=0, sticky='s',pady=5)
        
        appetisers_indicator = customtkinter.CTkFrame(self, corner_radius=5, height=6, width=175, fg_color="white")
        appetisers_indicator.grid(row=0, column=1, sticky='s',pady=5)

        dessert_indicator = customtkinter.CTkFrame(self, corner_radius=5, height=6, width=140, fg_color="white")
        dessert_indicator.grid(row=0, column=2, sticky='s',pady=5)
        # endregion
        
        # ---------------------------------- Fucntions ---------------------------------- #
        # region | Function to delete the pages 
        def delete_frame():
            for frame in main_windowframe.winfo_children():         # For loop which looks for frames in the main window frame
                frame.destroy()                                     # Deletes the frame shown
        # endregion

        # region | Function for the indicator
        def hide_indicate():                    # Changes the indicators white to match the background of the top navigation frame
            mains_indicator.configure(fg_color="white")
            appetisers_indicator.configure(fg_color="white")
            dessert_indicator.configure(fg_color="white")

        def indicate(fr, page):
            hide_indicate()                     # Calls the function to hide all indicators
            delete_frame()                      # Calls the function to delete the current frame
            fr.configure(fg_color="black")      # The indicator associated with the button will turn black in color
            page()                              # To specify which frame is being shown
        # endregion


class MainsSelection(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        # region | Label for the Mains Page
        title = customtkinter.CTkLabel(self, text="Mains", 
                                       font=customtkinter.CTkFont(size=50, weight="normal", 
                                                                  underline=True, family="Calibri"), text_color="white")
        title.grid(column=0, row=0, pady= 10, padx=35, sticky="nw")
        # endregion

        
        # ---------------------------------- Frames ---------------------------------- #
        mains_displayframe = 9               # Number of display frames
        # List to store widgets 
        mains_frames_list = []
        # Loop that runs depending on the mains_displayframe value divided by the desired number of columns
        for make_list in range((round(mains_displayframe/3))):
            mains_frames_list.append([])        # Appends empty list into the main list 

        # Loop that runs for for however long the dfl value is
        for mains_frame in range(mains_displayframe):
            self.rowitem = customtkinter.CTkFrame(self, corner_radius=10, width=300)        # Creates a base frame for the item display

            # ---------- If Conditions ---------- #
            # Conditioned to only run when the display frame value is less than 3
            if mains_frame < 3:
                self.rowitem.grid(column=0 + mains_frame, row=1, sticky="nsew", pady=20, padx=15)     # Grids the frame to row 1 and increases by 1 in columns
                mains_frames_list[0].append(self.rowitem)
            # Conditioned to run when the display frame value is more or equal to 3
            if mains_frame >= 3 and mains_frame < 6:
                self.rowitem.grid(column=0 + (mains_frame - 3), row=2, sticky="nsew", pady=20, padx=15)   # Grids the frame to row 2 and would subtract 3 to reset the column position
                mains_frames_list[1].append(self.rowitem)
            
            if mains_frame >= 6:
                self.rowitem.grid(column=0 + (mains_frame - 6), row=3, sticky="nsew", pady=20, padx=15)   # Grids the frame to row 2 and would subtract 3 to reset the column position
                mains_frames_list[2].append(self.rowitem)

        
        # ---------------------------------- Images ---------------------------------- #
        # Cutlet Image
        cutlet = customtkinter.CTkImage(Image.open("Images/Cutlet.jpg"), size=(275, 200))               # Imports image 
        cutlet_imgbtn = customtkinter.CTkButton(mains_frames_list[0][0], image=cutlet, text="",         # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")          # Font Configuration
        cutlet_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                       # Gridding for the image button

        # Lasagna Image
        lasagna = customtkinter.CTkImage(Image.open("Images/Lasagna.jpg"), size=(275, 200))             # Imports image 
        lasagna_imgbtn = customtkinter.CTkButton(mains_frames_list[0][1], image=lasagna, text="",       # Puts the image in a button
                                                 fg_color='transparent', hover_color="#333333")         # Font Configuration
        lasagna_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                      # Gridding the image button

        # Burger Image
        burger = customtkinter.CTkImage(Image.open("Images/Burger.jpg"), size=(275, 200))               # Imports image 
        burger_imgbtn = customtkinter.CTkButton(mains_frames_list[0][2], image=burger, text="",         # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")          # Font Configuration
        burger_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                       # Gridding the image button

        # Placeholder Image
        placeholder = customtkinter.CTkImage(Image.open("Images/Placeholder.jpg"), size=(275,200))
        placeholder_imgbtn = customtkinter.CTkButton(mains_frames_list[1][0], image=placeholder, text = "",
                                                     fg_color='transparent', hover_color="#333333")
        placeholder_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)

        # ----------------------------- Buttons / Labels ----------------------------- #
        # Cutlet Button / Label
        cutlet_lbl = customtkinter.CTkButton(mains_frames_list[0][0], text="Chicken Cutlet \n Price: $21.99", 
                                            font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        cutlet_lbl.grid(row=1, column=0, sticky='new', pady=(5,10), padx=10)

        # Lasagna Button / Label
        lasagna_lbl = customtkinter.CTkButton(mains_frames_list[0][1], text="Lasagna \n Price: $15.00", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        lasagna_lbl.grid(row=1, column=0, sticky='new', pady=(5,10), padx=10)

        # Burger Button / Label
        burger_lbl = customtkinter.CTkButton(mains_frames_list[0][2], text="Beef Burger \n Price: $13.00", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        burger_lbl.grid(row=1, column=0, sticky='new', pady=(5,10), padx=10)

        # Testing a add to order Button
        ato_btn = customtkinter.CTkButton(mains_frames_list[0][0], text = "+", width=40,
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        ato_btn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)


class AppetiserSelection(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        title = customtkinter.CTkLabel(self, text="Appetisers", 
                                       font=customtkinter.CTkFont(size=50, weight="normal", underline=True, family="Calibri"), 
                                       text_color="white")
        title.grid(column=0, row=0, pady= 10, padx=35, sticky="nw")

        appetisers_displayframe = 9               # Number of display frames
        # List to store widgets 
        appetisers_frames_list = []
        # Loop that runs depending on the appetisers_displayframe value divided by the desired number of columns
        for make_list in range((round(appetisers_displayframe/3))):
            appetisers_frames_list.append([])        # Appends empty list into the main list 

        # Loop that runs for for however long the dfl value is
        for appetisers_frame in range(appetisers_displayframe):
            self.rowitem = customtkinter.CTkFrame(self, corner_radius=10, width=300)        # Creates a base frame for the item display

            # ---------- If Conditions ---------- #
            # Conditioned to only run when the display frame value is less than 3
            if appetisers_frame < 3:
                self.rowitem.grid(column=0 + appetisers_frame, row=1, sticky="nsew", pady=20, padx=15)     # Grids the frame to row 1 and increases by 1 in columns
                appetisers_frames_list[0].append(self.rowitem)
            # Conditioned to run when the display frame value is more or equal to 3
            if appetisers_frame >= 3 and appetisers_frame < 6:
                self.rowitem.grid(column=0 + (appetisers_frame - 3), row=2, sticky="nsew", pady=20, padx=15)   # Grids the frame to row 2 and would subtract 3 to reset the column position
                appetisers_frames_list[1].append(self.rowitem)
            
            if appetisers_frame >= 6:
                self.rowitem.grid(column=0 + (appetisers_frame - 6), row=3, sticky="nsew", pady=20, padx=15)   # Grids the frame to row 2 and would subtract 3 to reset the column position
                appetisers_frames_list[2].append(self.rowitem)


# ------------------------ Main Window Configurations ------------------------ #
window=customtkinter.CTk()                 # Creates a window 
# Sets the size of the window to fill screen 
# The values in the string wil find the screen width and height and tuck it into the top left corner of the screen
window.geometry("1536x945-8+0")

# ---------------------------- Grid Configuration ---------------------------- #
window.grid_columnconfigure((0, 1), weight=1)

# ---------------------------------- Frames ---------------------------------- #
# Top Navigation Bar
TopNavBarFrame = TopNavBar(window)
TopNavBarFrame.grid(column=0, row=0, sticky='nwes', columnspan=2)
TopNavBarFrame.configure(corner_radius=0, height=75, fg_color="white")

# Main Frame to store different frames (Mains, Appetisers and Desserts)
main_windowframe = customtkinter.CTkFrame(window, height=800, corner_radius=0)
main_windowframe.grid(column=0, row=1, sticky='news', columnspan=2)
main_windowframe.columnconfigure(0, weight=1)

# Menu Selection
# Function to show the mains selection
def mains_page():
    MainsSelectionFrame = MainsSelection(main_windowframe)          # Calls the Class as the frame
    MainsSelectionFrame.grid(column=0, row=0, sticky='news')        # Grids the frame 
    MainsSelectionFrame.configure(height=875, corner_radius=0)     # Configurations to the frame 

# Function to show the appetisers selection
def appetisers_page():
    AppetiserFrame = AppetiserSelection(main_windowframe)           # Calls the Class as the frame 
    AppetiserFrame.grid(column=0, row=0, sticky='news')             # Grids the frame
    AppetiserFrame.configure(height=800, corner_radius=0)          # Configurations to the frame

# Function to show the desserts selection

# Order List
order_list = customtkinter.CTkFrame(window, corner_radius=0,  width=500, fg_color='blue')
order_list.grid(column=2, row=0, rowspan= 2, sticky='nsew')

mains_page()
window.mainloop()