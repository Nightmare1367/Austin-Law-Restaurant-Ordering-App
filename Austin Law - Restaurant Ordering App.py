"""
Restaurant Ordering App
Written by Austin Law

Note: Make sure you have CustomTkinter installed to ensure the program runs as intended.
This can be done by typing "pip3 install customtkinter" in the command prompt when ran as administrator.

You would also want to make sure that pillow is installed. 
This is done by typing "pip install --upgrade pip" and "pip install --upgrade Pillow" 
into the command prompt to install the 
"""

# region | Importing the Modules
import customtkinter
from tkinter import *
from PIL import Image
# endregion


# Dictionary to store name and price of product
# This is used for the order section
prices = {
    # Mains
    "Chicken Cutlet"        : 21.99,
    "Lasagna"               : 15.00,
    "Beef Burger"           : 13.00,
    "Butter Chicken"        : 15.99,
    "Pasta"                 : 20.00,
    "Pizza"                 : 13.99,
    "Mains Placeholder"     : 25.00,

    # Appetiser
    "Shoe String Fries"     : 5.00,
    "Hand Cut Fries"        : 4.50,
    "Onion Rings"           : 6.99,
    "Caesar Salad"          : 5.50,
    "Chicken Nibbles"       : 5.50,
    "Garlic Bread"          : 3.50,
    "Seafood Chowder"       : 6.99,
    "Appetiser Placeholder" : 3.99,

    # Desserts
    "Apple Crumble"         : 10.50,
    "Brownie"               : 8.99,
    "Cheesecake"            : 6.99,
    "Ice Cream"             : 12.50,
    "Macaron"               : 12.00,
    "Panna Cotta"           : 5.90,
    "Dessert Placeholder"   : 5.00,

    # Drinks
    "Coca-Cola"             : 2.99,
    "Chocolate Milkshake"   : 7.99,
    "Strawberry Juice"      : 4.99,
    "Bubble Tea"            : 6.50,
    "Hot Chocolate"         : 3.99,
    "Coffee"                : 4.50,
}

# List to store the customers order
cart = []


# Function to add the order to the cart
def add(btn):
    # Globalling Variable
    global cart
    
    # Looks for the item selected
    prices_value = (prices[btn.cget("text")])                      # Gets the price of the product
    decimal = "{:.2f}".format(prices_value)                        # Makes the price show with 2 decimal places
    item = btn.cget("text")                                        # Gets the item

    # Updating the Order
    # If statement which looks at whether there is an existing item in the cart
    if len(cart) == 0:                              # If the item selected does not exist, this will run
        cart.append([item, 1, float(decimal)])      # Appends the item to the list following the name, amount, and price
    # Runs this section if the item selected already exists in the list
    else:
        itemexist = False           # Variable which will be used to check if the item exists
        for i in range (len(cart)): # For loop which will look at the specifed item 
            if cart[i][0] == item:  # Runs if the item matches with cart
                itemexist = True    # Changes variable to true
                cart[i][1] += 1     # Adds 1 to the total amount of that item
                cart[i][2] = round(cart[i][2] + float(decimal),2)       # Updates the price to match the amount selected.

        # Runs if the item does not exist in the list
        if itemexist == False: 
            cart.append([item, 1, float(decimal)])
    printcart()


# Function to remove the selected order
def remove(btn):
    global cart
    prices_value = (prices[btn.cget("text")])   # Price of the selected item
    decimal = "{:.2f}".format(prices_value)     # Converts the item to sho up to 2 decimal points
    item = btn.cget("text")                     # Name of the item
    
    # For loop which will remove the item from the list
    for i in range (len(cart)):
        # Checks if the item matches with each other
        if cart[i][0] == item: 
            # Runs if the amount of that item is one
            if cart[i][1] == 1: 
                del(cart[i])    # Delets the list
                break           # Breaks the code to prevent error
            # Runs if there are more than one of that item
            else:
                cart[i][1] -= 1     # Subtracts one from the amount
                # Updates the price to show cost after removing the one item
                cart[i][2] = "{:.2f}".format(cart[i][2] - float(decimal))  
    printcart()


# Function to display and update the cart
def printcart():
    # Looks for widgets and destroys the frame which stores the order
    for widget in order_list_frame.winfo_children():
        widget.destroy()  
 
    rownum = 0
    for i in range(len(cart)):
        order_lbl = customtkinter.CTkLabel(order_list_frame, text = (cart[i][0] + " | x" + str(cart[i][1]) + " | $" + str(cart[i][2])), 
                               font = customtkinter.CTkFont(family = "Calibri", size=25))
        order_lbl.grid(row=rownum, column=0, pady=5, padx=5, sticky="nw")
        rownum += 1
 
    def costcalc():
        totalcost = 0
        for i in range(len(cart)): totalcost += cart[i][2]
        return(str("{:.2f}".format(totalcost)))

    # Updating the order total label
    totalorder_lbl.configure(text="Total Price: $"+costcalc())


class TopNavBar(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        global indicate, mains_indicator, mains_page
        # ---------------------------------- Widgets ---------------------------------- #
        # region | Buttons for the Top Navigation Bar
        mains_btn = customtkinter.CTkButton(self, text="Mains",
                                           font=customtkinter.CTkFont(family="Calibri", size=35), 
                                           fg_color="transparent", text_color="black", hover_color="gray",
                                           command=lambda: indicate(mains_indicator, mains_page))
        mains_btn.grid(column=0, row=0, padx=10, pady=10, sticky='we')

        appetisers_btn = customtkinter.CTkButton(self, text="Appetisers", 
                                                 font=customtkinter.CTkFont(family="Calibri", size=35), 
                                                 fg_color="transparent", text_color="black", hover_color="gray", 
                                                 command=lambda: indicate(appetisers_indicator, appetisers_page))
        appetisers_btn.grid(column=1, row=0, padx=10, pady=10, sticky='we')

        dessert_btn = customtkinter.CTkButton(self, text="Desserts", 
                                              font=customtkinter.CTkFont(family="Calibri", size=35), 
                                              fg_color="transparent", text_color="black", hover_color="gray", 
                                              command=lambda: indicate(dessert_indicator, desserts_page))
        dessert_btn.grid(column=2, row=0, padx=10, pady=10, sticky='we')

        drink_btn = customtkinter.CTkButton(self, text="Drinks", width=100,
                                              font=customtkinter.CTkFont(family="Calibri", size=35), 
                                              fg_color="transparent", text_color="black", hover_color="gray", 
                                              command=lambda: indicate(drinks_indicator, drinks_page))
        drink_btn.grid(column=3, row=0, padx=10, pady=10, sticky='we')
        # endregion

        # region | Frames which would act as an indicator for the buttons
        mains_indicator = customtkinter.CTkFrame(self, corner_radius=5, height=6, width=100, fg_color="#DEE2E6")
        mains_indicator.grid(row=0, column=0, sticky='s',pady=5)
        
        appetisers_indicator = customtkinter.CTkFrame(self, corner_radius=5, height=6, width=175, fg_color="#DEE2E6")
        appetisers_indicator.grid(row=0, column=1, sticky='s',pady=5)

        dessert_indicator = customtkinter.CTkFrame(self, corner_radius=5, height=6, width=140, fg_color="#DEE2E6")
        dessert_indicator.grid(row=0, column=2, sticky='s',pady=5)

        drinks_indicator = customtkinter.CTkFrame(self, corner_radius=5, height=6, width=100, fg_color="#DEE2E6")
        drinks_indicator.grid(row=0, column=3, sticky='s',pady=5)
        # endregion
        
        # ---------------------------------- Functions ---------------------------------- #
        # region | Function to delete the pages 
        def delete_frame():
            for frame in main_windowframe.winfo_children():         # For loop which looks for frames in the main window frame
                frame.destroy()                                     # Deletes the frame shown
        # endregion

        # region | Function for the indicator
        def hide_indicate():                    # Changes the indicators white to match the background of the top navigation frame
            mains_indicator.configure(fg_color="#DEE2E6")
            appetisers_indicator.configure(fg_color="#DEE2E6")
            dessert_indicator.configure(fg_color="#DEE2E6")
            drinks_indicator.configure(fg_color="#DEE2E6")

        def indicate(fr, page):
            hide_indicate()                     # Calls the function to hide all indicators
            delete_frame()                      # Calls the function to delete the current frame
            fr.configure(fg_color="black")      # The indicator associated with the button will turn black in color
            page()                              # To specify which frame is being shown
        # endregion


class WelcomePage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # ---------- Grid Configurations ---------- #
        self.grid_columnconfigure(0, weight=1)

        # region | Title of the page
        title_top = customtkinter.CTkLabel(self, text="Welcome", text_color="#DEE2E6",
                                       font=customtkinter.CTkFont(family="Calibri", size=70, weight="bold"))
        title_top.grid(column=0, row=0, pady=(200,0))

        title_bottom = customtkinter.CTkLabel(self, text = "to Austin's Restaurant",  text_color="#DEE2E6",
                                             font = customtkinter.CTkFont(family="Calibri", size=40))
        title_bottom.grid(row=1, column=0)
        # endregion
        
        # region | Seperator Frame between Title and Description
        titledescription_frame = customtkinter.CTkFrame(self, fg_color='#DEE2E6', height=7, width=450, corner_radius=10)
        titledescription_frame.grid(row=2, column=0, pady=10)
        # endregion

        # region | Description of restaurant
        description = ("Austin's Restaurant offers a variety of dishes.\n"
                       "Start by either selecting one of the categories\n"
                       "on the top navigation bar or by clicking the \n"
                       "'Get Started' button below.")
        
        description_lbl = customtkinter.CTkLabel(self, text=description, justify=CENTER, text_color="#DEE2E6",
                                                 font=customtkinter.CTkFont(family="Calibri", size=25))
        description_lbl.grid(row=3, column=0, pady=10)
        # endregion

        # region | Button To Mains Section
        mains_button = customtkinter.CTkButton(self, text="Get Started", text_color="black", 
                                               fg_color="#DEE2E6", hover_color="gray",
                                               command = lambda: indicate(mains_indicator, mains_page),
                                               font=customtkinter.CTkFont(family="Calibri", size=25))
        mains_button.grid(row=4, column=0, pady=5, ipady=5, ipadx=10)
        # endregion


class MainsSelection(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        # region | Label for the Mains Page
        mains_title = customtkinter.CTkLabel(self, text="Mains", 
                                       font=customtkinter.CTkFont(size=50, weight="normal", 
                                                                  underline=True, family="Calibri"), text_color="white")
        mains_title.grid(column=0, row=0, pady= 10, padx=35, sticky="nw")
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
                self.rowitem.grid(column=0 + mains_frame, row=1, sticky="nsew", pady=20, padx=15)         # Grids the frame to row 1 and increases by 1 in columns
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
        cutlet = customtkinter.CTkImage(Image.open("Images/Mains/Cutlet.jpg"), size=(275, 200))         # Imports image 
        cutlet_imgbtn = customtkinter.CTkButton(mains_frames_list[0][0], image=cutlet, text="",         # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")          # Configuration to button background
        cutlet_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                       # Gridding for the image button

        # Lasagna Image
        lasagna = customtkinter.CTkImage(Image.open("Images/Mains/Lasagna.jpg"), size=(275, 200))       # Imports image 
        lasagna_imgbtn = customtkinter.CTkButton(mains_frames_list[0][1], image=lasagna, text="",       # Puts the image in a button
                                                 fg_color='transparent', hover_color="#333333")         # Configuration to button background
        lasagna_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                      # Gridding the image button

        # Burger Image
        burger = customtkinter.CTkImage(Image.open("Images/Mains/Burger.jpg"), size=(275, 200))         # Imports image 
        burger_imgbtn = customtkinter.CTkButton(mains_frames_list[0][2], image=burger, text="",         # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")          # Configuration to button background
        burger_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                       # Gridding the image button

        # Butter Chicken Image
        butter_chicken = customtkinter.CTkImage(Image.open("Images/Mains/Butter_Chicken.jpg"), size=(275, 200))   # Imports image 
        butter_chicken_imgbtn = customtkinter.CTkButton(mains_frames_list[1][0], image=butter_chicken, text="",   # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                    # Configuration to button background
        butter_chicken_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                         # Gridding the image button

        # Pasta Image
        pasta = customtkinter.CTkImage(Image.open("Images/Mains/Pasta.jpg"), size=(275, 200))           # Imports image 
        pasta_imgbtn = customtkinter.CTkButton(mains_frames_list[1][1], image=pasta, text="",           # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")          # Configuration to button background
        pasta_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                        # Gridding the image button

        # Pizza Image
        pizza = customtkinter.CTkImage(Image.open("Images/Mains/Pizza.jpg"), size=(275, 200))           # Imports image 
        pizza_imgbtn = customtkinter.CTkButton(mains_frames_list[1][2], image=pizza, text="",           # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")          # Configuration to button background
        pizza_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                        # Gridding the image button

        # region | Placeholder Images
        placeholder = customtkinter.CTkImage(Image.open("Images/Placeholder.jpg"), size=(275,200))
        placeholder1_imgbtn = customtkinter.CTkButton(mains_frames_list[2][0], image=placeholder, text = "",
                                                     fg_color='transparent', hover_color="#333333")
        placeholder1_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        
        placeholder1_imgbtn = customtkinter.CTkButton(mains_frames_list[2][1], image=placeholder, text = "",
                                                     fg_color='transparent', hover_color="#333333")
        placeholder1_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)

        placeholder1_imgbtn = customtkinter.CTkButton(mains_frames_list[2][2], image=placeholder, text = "",
                                                     fg_color='transparent', hover_color="#333333")
        placeholder1_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # ----------------------------- Buttons / Labels ----------------------------- #
        # region | Cutlet Button / Label
        cutlet_lbl = customtkinter.CTkButton(mains_frames_list[0][0], text="Chicken Cutlet", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        cutlet_lbl.grid(row=1, column=0, sticky='news', pady=(5,0), padx=10)

        cutlet_price = customtkinter.CTkButton(mains_frames_list[0][0], text="Price: $21.99", 
                                               font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        cutlet_price.grid(row=2, column=0, sticky='news', pady=(0, 10), padx=10)

        # Add to Order Button for Cutlet
        cutlet_atobtn = customtkinter.CTkButton(mains_frames_list[0][0], text = "+", width=40, command = lambda: add(cutlet_lbl),
                                                font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        cutlet_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Cutlet
        cutlet_remove = customtkinter.CTkButton(mains_frames_list[0][0], text = "-", width=40, command = lambda: remove(cutlet_lbl),
                                                font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        cutlet_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)
        # endregion

        # region | Lasagna Button / Label
        lasagna_lbl = customtkinter.CTkButton(mains_frames_list[0][1], text="Lasagna", 
                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        lasagna_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        lasagna_price = customtkinter.CTkButton(mains_frames_list[0][1], text="Price: $15.00", 
        font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        lasagna_price.grid(row=2, column=0, sticky='news', pady=(0, 10), padx=10)

        # Add to Order Button for Lasagna
        lasagna_atobtn = customtkinter.CTkButton(mains_frames_list[0][1], text = "+", width=40, command = lambda: add(lasagna_lbl),
                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        lasagna_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Cutlet
        lasagna_remove = customtkinter.CTkButton(mains_frames_list[0][1], text = "-", width=40, command = lambda: remove(lasagna_lbl),
                                                font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        lasagna_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)
        # endregion

        # region | Burger Button / Label
        burger_lbl = customtkinter.CTkButton(mains_frames_list[0][2], text="Beef Burger", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        burger_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        burger_price = customtkinter.CTkButton(mains_frames_list[0][2], text="Price: $13.00", 
                                               font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        burger_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Burger
        burger_atobtn = customtkinter.CTkButton(mains_frames_list[0][2], text = "+", width=40, command = lambda: add(burger_lbl),
                                                font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        burger_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Butter Chicken Button / Label
        butter_chicken_lbl = customtkinter.CTkButton(mains_frames_list[1][0], text="Butter Chicken", 
                                                     font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        butter_chicken_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        butter_chicken_price = customtkinter.CTkButton(mains_frames_list[1][0], text="Price: $15.99", 
                                                       font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        butter_chicken_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Butter Chicken
        butter_chicken_atobtn = customtkinter.CTkButton(mains_frames_list[1][0], text = "+", width=40, command = lambda: add(butter_chicken_lbl),
                                                        font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        butter_chicken_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Pasta Button / Label
        pasta_lbl = customtkinter.CTkButton(mains_frames_list[1][1], text="Pasta", 
                                            font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        pasta_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        pasta_price = customtkinter.CTkButton(mains_frames_list[1][1], text="Price: $20.00", 
                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        pasta_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Pasta
        pasta_atobtn = customtkinter.CTkButton(mains_frames_list[1][1], text = "+", width=40, command = lambda: add(pasta_lbl),
                                               font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        pasta_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Pizza Button / Label
        pizza_lbl = customtkinter.CTkButton(mains_frames_list[1][2], text="Pizza", 
                                            font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        pizza_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        pizza_price = customtkinter.CTkButton(mains_frames_list[1][2], text="Price: $13.99", 
                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        pizza_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Pizza
        pizza_atobtn = customtkinter.CTkButton(mains_frames_list[1][2], text = "+", width=40, command = lambda: add(pizza_lbl),
                                               font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        pizza_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Placeholder Button \ Label
        # Label for Placeholder 1
        mains_placeholder1_lbl = customtkinter.CTkButton(mains_frames_list[2][0], text="Mains Placeholder", 
                                                   font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        mains_placeholder1_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        mains_placeholder1_price = customtkinter.CTkButton(mains_frames_list[2][0], text="Price: $25.00", 
                                                     font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        mains_placeholder1_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 1
        mains_placeholder1_atobtn = customtkinter.CTkButton(mains_frames_list[2][0], text = "+", 
                                                      width=40, command = lambda: add(mains_placeholder1_lbl),
                                                      font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        mains_placeholder1_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)


        # Label for Placeholder 2
        mains_placeholder2_lbl = customtkinter.CTkButton(mains_frames_list[2][1], text="Mains Placeholder", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        mains_placeholder2_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        mains_placeholder2_price = customtkinter.CTkButton(mains_frames_list[2][1], text="Price: $25.00", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        mains_placeholder2_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 2
        mains_placeholder2_atobtn = customtkinter.CTkButton(mains_frames_list[2][1], text = "+", 
                                                      width=40, command = lambda: add(mains_placeholder2_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        mains_placeholder2_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)


        # Label for Placeholder 3
        mains_placeholder3_lbl = customtkinter.CTkButton(mains_frames_list[2][2], text="Mains Placeholder", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        mains_placeholder3_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        mains_placeholder3_price = customtkinter.CTkButton(mains_frames_list[2][2], text="Price: $25.00", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        mains_placeholder3_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 3
        mains_placeholder3_atobtn = customtkinter.CTkButton(mains_frames_list[2][2], text = "+", 
                                                      width=40, command = lambda: add(mains_placeholder3_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        mains_placeholder3_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion


class AppetiserSelection(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        appetisers_title = customtkinter.CTkLabel(self, text="Appetisers", 
                                       font=customtkinter.CTkFont(size=50, weight="normal", underline=True, family="Calibri"), 
                                       text_color="white")
        appetisers_title.grid(column=0, row=0, pady= 10, padx=35, sticky="nw")

        # ---------------------------------- Frames ---------------------------------- #
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

        # ---------------------------------- Images ---------------------------------- #
        # Shoe String Fries Image
        shoe_string = customtkinter.CTkImage(Image.open("Images/Appetisers/Shoe_String.jpg"), size=(275, 200))               # Imports image 
        shoe_string_imgbtn = customtkinter.CTkButton(appetisers_frames_list[0][0], image=shoe_string, text="",              # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                              # Configuration to button background
        shoe_string_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Hand Cut Fries Image
        hand_cut = customtkinter.CTkImage(Image.open("Images/Appetisers/Hand_Cut.jpg"), size=(275, 200))                     # Imports image 
        hand_cut_imgbtn = customtkinter.CTkButton(appetisers_frames_list[0][1], image=hand_cut, text="",                    # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                              # Configuration to button background
        hand_cut_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Onion Rings Image
        onion_rings = customtkinter.CTkImage(Image.open("Images/Appetisers/Onion_Rings.jpg"), size=(275, 200))               # Imports image 
        onion_rings_imgbtn = customtkinter.CTkButton(appetisers_frames_list[0][2], image=onion_rings, text="",              # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                              # Configuration to button background
        onion_rings_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Caeser Salad Image
        caeser_salad = customtkinter.CTkImage(Image.open("Images/Appetisers/Caesar_Salad.jpg"), size=(275, 200))             # Imports image 
        caeser_salad_imgbtn = customtkinter.CTkButton(appetisers_frames_list[1][0], image=caeser_salad, text="",            # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                              # Configuration to button background
        caeser_salad_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Chicken Nibbles Image
        chicken_nibbles = customtkinter.CTkImage(Image.open("Images/Appetisers/Chicken_Nibbles.jpg"), size=(275, 200))       # Imports image 
        chicken_nibbles_imgbtn = customtkinter.CTkButton(appetisers_frames_list[1][1], image=chicken_nibbles, text="",      # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                              # Configuration to button background
        chicken_nibbles_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Garlic Bread Image
        garlic_bread = customtkinter.CTkImage(Image.open("Images/Appetisers/Garlic_Bread.jpg"), size=(275, 200))             # Imports image 
        garlic_bread_imgbtn = customtkinter.CTkButton(appetisers_frames_list[1][2], image=garlic_bread, text="",            # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                              # Configuration to button background
        garlic_bread_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)

        # Seafood Chowder Image
        seafood_chowder = customtkinter.CTkImage(Image.open("Images/Appetisers/Seafood_Chowder.jpg"), size=(275, 200))       # Imports image 
        seafood_chowder_imgbtn = customtkinter.CTkButton(appetisers_frames_list[2][0], image=seafood_chowder, text="",      # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                              # Configuration to button background
        seafood_chowder_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)

        # region | Placeholder Images
        placeholder1 = customtkinter.CTkImage(Image.open("Images/Placeholder.jpg"), size=(275,200))
        placeholder1_imgbtn = customtkinter.CTkButton(appetisers_frames_list[2][1], image=placeholder1, text = "",
                                                     fg_color='transparent', hover_color="#333333")
        placeholder1_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        
        placeholder2 = customtkinter.CTkImage(Image.open("Images/Placeholder.jpg"), size=(275,200))
        placeholder2_imgbtn = customtkinter.CTkButton(appetisers_frames_list[2][2], image=placeholder2, text = "",
                                                     fg_color='transparent', hover_color="#333333")
        placeholder2_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # ----------------------------- Buttons / Labels ----------------------------- #
        # region | Label for Shoe String Fries
        shoe_string_lbl = customtkinter.CTkButton(appetisers_frames_list[0][0], text="Shoe String Fries", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        shoe_string_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        shoe_string_price = customtkinter.CTkButton(appetisers_frames_list[0][0], text="Price: $5.00", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        shoe_string_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Shoe String Fries
        shoe_string_atobtn = customtkinter.CTkButton(appetisers_frames_list[0][0], text = "+", 
                                                     width=40, command = lambda: add(shoe_string_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        shoe_string_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Hand Cut Fries
        hand_cut_lbl = customtkinter.CTkButton(appetisers_frames_list[0][1], text="Hand Cut Fries", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        hand_cut_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        hand_cut_price = customtkinter.CTkButton(appetisers_frames_list[0][1], text="Price: $4.50", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        hand_cut_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Hand Cut Fries
        hand_cut_atobtn = customtkinter.CTkButton(appetisers_frames_list[0][1], text = "+", 
                                                  width=40, command = lambda: add(hand_cut_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        hand_cut_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Onion Rings
        onion_rings_lbl = customtkinter.CTkButton(appetisers_frames_list[0][2], text="Onion Rings", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        onion_rings_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)
        
        onion_rings_price = customtkinter.CTkButton(appetisers_frames_list[0][2], text="Price: $6.99", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        onion_rings_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Onion Rings
        onion_rings_atobtn = customtkinter.CTkButton(appetisers_frames_list[0][2], text = "+", 
                                                     width=40, command = lambda: add(onion_rings_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        onion_rings_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Caesar Salad
        caeser_salad_lbl = customtkinter.CTkButton(appetisers_frames_list[1][0], text="Caesar Salad", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        caeser_salad_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        caeser_salad_price = customtkinter.CTkButton(appetisers_frames_list[1][0], text="Price: $5.50", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        caeser_salad_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Caesar Salad
        caeser_salad_atobtn = customtkinter.CTkButton(appetisers_frames_list[1][0], text = "+", 
                                                      width=40, command = lambda: add(caeser_salad_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        caeser_salad_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Chicken Nibbles
        chicken_nibbles_lbl = customtkinter.CTkButton(appetisers_frames_list[1][1], text="Chicken Nibbles", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        chicken_nibbles_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        chicken_nibbles_price = customtkinter.CTkButton(appetisers_frames_list[1][1], text="Price: $5.50", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        chicken_nibbles_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Chicken Nibbles
        chicken_nibbles_atobtn = customtkinter.CTkButton(appetisers_frames_list[1][1], text = "+", 
                                                         width=40, command = lambda: add(chicken_nibbles_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        chicken_nibbles_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Garlic Bread
        garlic_bread_lbl = customtkinter.CTkButton(appetisers_frames_list[1][2], text="Garlic Bread", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        garlic_bread_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        garlic_bread_price = customtkinter.CTkButton(appetisers_frames_list[1][2], text="Price: $3.50", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        garlic_bread_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Garlic Bread
        garlic_bread_atobtn = customtkinter.CTkButton(appetisers_frames_list[1][2], text = "+", 
                                                      width=40, command = lambda: add(garlic_bread_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        garlic_bread_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Seafood Chowder
        seafood_chowder_lbl = customtkinter.CTkButton(appetisers_frames_list[2][0], text="Seafood Chowder", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        seafood_chowder_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        seafood_chowder_price = customtkinter.CTkButton(appetisers_frames_list[2][0], text="Price: $6.99", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        seafood_chowder_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Seafood Chowder
        seafood_chowder_atobtn = customtkinter.CTkButton(appetisers_frames_list[2][0], text = "+", 
                                                         width=40, command = lambda: add(seafood_chowder_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        seafood_chowder_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Placeholder Button \ Label
        # Label for Placeholder 1
        placeholder1_lbl = customtkinter.CTkButton(appetisers_frames_list[2][1], text="Appetiser Placeholder", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        placeholder1_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        placeholder1_price = customtkinter.CTkButton(appetisers_frames_list[2][1], text="Price: $3.99", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        placeholder1_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 1
        placeholder1_atobtn = customtkinter.CTkButton(appetisers_frames_list[2][1], text = "+", 
                                                      width=40, command = lambda: add(placeholder1_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        placeholder1_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)


        # Label for Placeholder 2
        placeholder2_lbl = customtkinter.CTkButton(appetisers_frames_list[2][2], text="Appetiser Placeholder", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        placeholder2_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        placeholder2_price = customtkinter.CTkButton(appetisers_frames_list[2][2], text="Price: $3.99", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        placeholder2_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 2
        placeholder2_atobtn = customtkinter.CTkButton(appetisers_frames_list[2][2], text = "+", 
                                                      width=40, command = lambda: add(placeholder2_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        placeholder2_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion


class DessertSelection(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        deeserts_title = customtkinter.CTkLabel(self, text="Desserts", 
                                       font=customtkinter.CTkFont(size=50, weight="normal", underline=True, family="Calibri"), 
                                       text_color="white")
        deeserts_title.grid(column=0, row=0, pady= 10, padx=35, sticky="nw")

        # ---------------------------------- Frames ---------------------------------- #
        desserts_displayframe = 8               # Number of display frames
        # List to store widgets 
        desserts_frames_list = []
        # Loop that runs depending on the appetisers_displayframe value divided by the desired number of columns
        for make_list in range((round(desserts_displayframe/3))):
            desserts_frames_list.append([])        # Appends empty list into the main list             

        # Loop that runs for for however long the dfl value is
        for desserts_frame in range(desserts_displayframe):
            self.rowitem = customtkinter.CTkFrame(self, corner_radius=10, width=300)        # Creates a base frame for the item display

            # ---------- If Conditions ---------- #
            # Conditioned to only run when the display frame value is less than 3
            if desserts_frame < 3:
                self.rowitem.grid(column=0 + desserts_frame, row=1, sticky="nsew", pady=20, padx=15)     # Grids the frame to row 1 and increases by 1 in columns
                desserts_frames_list[0].append(self.rowitem)
            # Conditioned to run when the display frame value is more or equal to 3
            if desserts_frame >= 3 and desserts_frame < 6:
                self.rowitem.grid(column=0 + (desserts_frame - 3), row=2, sticky="nsew", pady=20, padx=15)   # Grids the frame to row 2 and would subtract 3 to reset the column position
                desserts_frames_list[1].append(self.rowitem)
            
            if desserts_frame >= 6:
                self.rowitem.grid(column=0 + (desserts_frame - 6), row=3, sticky="nsew", pady=20, padx=15)   # Grids the frame to row 2 and would subtract 3 to reset the column position
                desserts_frames_list[2].append(self.rowitem)


        # ---------------------------------- Images ---------------------------------- #
        # region
        # Apple Crumble Image
        apple_crumble = customtkinter.CTkImage(Image.open("Images/Desserts/Apple_Crumble.jpg"), size=(275, 200))    # Imports image 
        apple_crumble_imgbtn = customtkinter.CTkButton(desserts_frames_list[0][0], image=apple_crumble, text="",    # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                      # Configuration to button background
        apple_crumble_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Brownie Image
        brownie = customtkinter.CTkImage(Image.open("Images/Desserts/Brownie.jpg"), size=(275, 200))                # Imports image 
        brownie_imgbtn = customtkinter.CTkButton(desserts_frames_list[0][1], image=brownie, text="",                # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                      # Configuration to button background
        brownie_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Cheesecake Image
        cheesecake = customtkinter.CTkImage(Image.open("Images/Desserts/Cheesecake.jpg"), size=(275, 200))          # Imports image 
        cheesecake_imgbtn = customtkinter.CTkButton(desserts_frames_list[0][2], image=cheesecake, text="",          # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                      # Configuration to button background
        cheesecake_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Ice Cream Image
        ice_cream = customtkinter.CTkImage(Image.open("Images/Desserts/Ice_Cream.jpg"), size=(275, 200))            # Imports image 
        ice_cream_imgbtn = customtkinter.CTkButton(desserts_frames_list[1][0], image=ice_cream, text="",            # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                      # Configuration to button background
        ice_cream_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Macaron Image
        macaron = customtkinter.CTkImage(Image.open("Images/Desserts/Macaron.jpg"), size=(275, 200))                # Imports image 
        macaron_imgbtn = customtkinter.CTkButton(desserts_frames_list[1][1], image=macaron, text="",                # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                      # Configuration to button background
        macaron_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Panna Cotta Image
        panna_cotta = customtkinter.CTkImage(Image.open("Images/Desserts/Panna_Cotta.jpg"), size=(275, 200))        # Imports image 
        panna_cotta_imgbtn = customtkinter.CTkButton(desserts_frames_list[1][2], image=panna_cotta, text="",        # Puts the image in a button
                                                fg_color='transparent', hover_color="#333333")                      # Configuration to button background
        panna_cotta_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 
        # endregion

        # region | Placeholder Images
        placeholder1 = customtkinter.CTkImage(Image.open("Images/Placeholder.jpg"), size=(275,200))
        placeholder1_imgbtn = customtkinter.CTkButton(desserts_frames_list[2][0], image=placeholder1, text = "",
                                                     fg_color='transparent', hover_color="#333333")
        placeholder1_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        
        placeholder2 = customtkinter.CTkImage(Image.open("Images/Placeholder.jpg"), size=(275,200))
        placeholder2_imgbtn = customtkinter.CTkButton(desserts_frames_list[2][1], image=placeholder2, text = "",
                                                     fg_color='transparent', hover_color="#333333")
        placeholder2_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion


        # ----------------------------- Buttons / Labels ----------------------------- #
        # region | Label for Apple Crumble
        apple_crumble_lbl = customtkinter.CTkButton(desserts_frames_list[0][0], text="Apple Crumble", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        apple_crumble_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        apple_crumble_price = customtkinter.CTkButton(desserts_frames_list[0][0], text="Price: $10.50", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        apple_crumble_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Apple Crumble
        apple_crumble_atobtn = customtkinter.CTkButton(desserts_frames_list[0][0], text = "+", 
                                                       width=40, command = lambda: add(apple_crumble_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        apple_crumble_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Brownie
        brownie_lbl = customtkinter.CTkButton(desserts_frames_list[0][1], text="Brownie", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        brownie_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        brownie_price = customtkinter.CTkButton(desserts_frames_list[0][1], text="Price: $8.99", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        brownie_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Brownie
        brownie_atobtn = customtkinter.CTkButton(desserts_frames_list[0][1], text = "+", 
                                                 width=40, command = lambda: add(brownie_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        brownie_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Cheesecake
        cheesecake_lbl = customtkinter.CTkButton(desserts_frames_list[0][2], text="Cheesecake", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        cheesecake_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        cheesecake_price = customtkinter.CTkButton(desserts_frames_list[0][2], text="Price: $6.99", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        cheesecake_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Cheesecake
        cheesecake_atobtn = customtkinter.CTkButton(desserts_frames_list[0][2], text = "+", 
                                                    width=40, command = lambda: add(cheesecake_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        cheesecake_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Ice Cream
        ice_cream_lbl = customtkinter.CTkButton(desserts_frames_list[1][0], text="Ice Cream", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        ice_cream_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        ice_cream_price = customtkinter.CTkButton(desserts_frames_list[1][0], text="Price: $12.50", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        ice_cream_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Ice Cream
        ice_cream_atobtn = customtkinter.CTkButton(desserts_frames_list[1][0], text = "+", 
                                                   width=40, command = lambda: add(ice_cream_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        ice_cream_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Macaron
        macaron_lbl = customtkinter.CTkButton(desserts_frames_list[1][1], text="Macaron", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        macaron_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        macaron_price = customtkinter.CTkButton(desserts_frames_list[1][1], text="Price: $12.00", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        macaron_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Macaron
        macaron_atobtn = customtkinter.CTkButton(desserts_frames_list[1][1], text = "+", 
                                                 width=40, command = lambda: add(macaron_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        macaron_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Panna Cotta
        panna_cotta_lbl = customtkinter.CTkButton(desserts_frames_list[1][2], text="Panna Cotta", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        panna_cotta_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        panna_cotta_price = customtkinter.CTkButton(desserts_frames_list[1][2], text="Price: $5.90", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        panna_cotta_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)
        
        # Add to Order Button for Panna Cotta
        panna_cotta_atobtn = customtkinter.CTkButton(desserts_frames_list[1][2], text = "+", 
                                                     width=40, command = lambda: add(panna_cotta_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        panna_cotta_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Placeholder Button \ Label
        # Label for Placeholder 1
        placeholder1_lbl = customtkinter.CTkButton(desserts_frames_list[2][0], text="Dessert Placeholder", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        placeholder1_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        placeholder1_price = customtkinter.CTkButton(desserts_frames_list[2][0], text="Price: $5.00", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        placeholder1_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 1
        placeholder1_atobtn = customtkinter.CTkButton(desserts_frames_list[2][0], text = "+", 
                                                      width=40, command = lambda: add(placeholder1_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        placeholder1_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Label for Placeholder 2
        placeholder2_lbl = customtkinter.CTkButton(desserts_frames_list[2][1], text="Dessert Placeholder", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        placeholder2_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        placeholder2_price = customtkinter.CTkButton(desserts_frames_list[2][1], text="Price: $5.00", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        placeholder2_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 2
        placeholder2_atobtn = customtkinter.CTkButton(desserts_frames_list[2][1], text = "+", 
                                                      width=40, command = lambda: add(placeholder2_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        placeholder2_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion


class DrinkSelection(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        drinks_title = customtkinter.CTkLabel(self, text="Drinks", 
                                       font=customtkinter.CTkFont(size=50, weight="normal", underline=True, family="Calibri"), 
                                       text_color="white")
        drinks_title.grid(column=0, row=0, pady= 10, padx=35, sticky="nw")

        # ---------------------------------- Frames ---------------------------------- #
        drinks_displayframe = 6               # Number of display frames
        # List to store widgets 
        drinks_frames_list = []
        # Loop that runs depending on the drinks_displayframe value divided by the desired number of columns
        for make_list in range((round(drinks_displayframe/3))):
            drinks_frames_list.append([])        # Appends empty list into the main list             

        # Loop that runs for for however long the dfl value is
        for drinks_frame in range(drinks_displayframe):
            self.rowitem = customtkinter.CTkFrame(self, corner_radius=10, width=300)        # Creates a base frame for the item display

            # ---------- If Conditions ---------- #
            # Conditioned to only run when the display frame value is less than 3
            if drinks_frame < 3:
                self.rowitem.grid(column=0 + drinks_frame, row=1, sticky="nsew", pady=20, padx=15)     # Grids the frame to row 1 and increases by 1 in columns
                drinks_frames_list[0].append(self.rowitem)
            # Conditioned to run when the display frame value is more or equal to 3
            if drinks_frame >= 3 and drinks_frame < 6:
                self.rowitem.grid(column=0 + (drinks_frame - 3), row=2, sticky="nsew", pady=20, padx=15)   # Grids the frame to row 2 and would subtract 3 to reset the column position
                drinks_frames_list[1].append(self.rowitem)
            
            if drinks_frame >= 6:
                self.rowitem.grid(column=0 + (drinks_frame - 6), row=3, sticky="nsew", pady=20, padx=15)   # Grids the frame to row 2 and would subtract 3 to reset the column position
                drinks_frames_list[2].append(self.rowitem)

        # ---------------------------------- Images ---------------------------------- #
        # region | Coke Image
        coke = customtkinter.CTkImage(Image.open("Images/Drinks/Coke.jpg"), size=(275,200))
        coke_imgbtn = customtkinter.CTkButton(drinks_frames_list[0][0], image=coke, text="",        
                                                fg_color='transparent', hover_color="#333333")
        coke_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # region | Milkshake Image
        milkshake = customtkinter.CTkImage(Image.open("Images/Drinks/Milkshake.jpg"), size=(275,200))
        milkshake_imgbtn = customtkinter.CTkButton(drinks_frames_list[0][1], image=milkshake, text="",        
                                                fg_color='transparent', hover_color="#333333")
        milkshake_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # region | Strawberry Juice Image
        strawberry_juice = customtkinter.CTkImage(Image.open("Images/Drinks/Strawberry_Juice.jpg"), size=(275,200))
        strawberry_juice_imgbtn = customtkinter.CTkButton(drinks_frames_list[0][2], image=strawberry_juice, text="",        
                                                fg_color='transparent', hover_color="#333333")
        strawberry_juice_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # region | Bubble Tea Image
        bubble_tea = customtkinter.CTkImage(Image.open("Images/Drinks/Boba.jpg"), size=(275,200))
        bubble_tea_imgbtn = customtkinter.CTkButton(drinks_frames_list[1][0], image=bubble_tea, text="",        
                                                fg_color='transparent', hover_color="#333333")
        bubble_tea_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # region | Hot Chocolate Image
        hot_chocolate = customtkinter.CTkImage(Image.open("Images/Drinks/Hot_Chocolate.jpg"), size=(275,200))
        hot_chocolate_imgbtn = customtkinter.CTkButton(drinks_frames_list[1][1], image=hot_chocolate, text="",        
                                                fg_color='transparent', hover_color="#333333")
        hot_chocolate_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # region | Coffee Image
        coffee = customtkinter.CTkImage(Image.open("Images/Drinks/Coffee.png"), size=(275,200))
        coffee_imgbtn = customtkinter.CTkButton(drinks_frames_list[1][2], image=coffee, text="",        
                                                fg_color='transparent', hover_color="#333333")
        coffee_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # ----------------------------- Buttons / Labels ----------------------------- #
        # region | Label for Coke Drink
        coke_lbl = customtkinter.CTkButton(drinks_frames_list[0][0], text="Coca-Cola", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        coke_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        coke_price = customtkinter.CTkButton(drinks_frames_list[0][0], text="Price: $2.99", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        coke_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Coke Drink
        coke_atobtn = customtkinter.CTkButton(drinks_frames_list[0][0], text = "+", 
                                              width=40, command = lambda: add(coke_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        coke_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Chocolate Milkshake Drink
        milkshake_lbl = customtkinter.CTkButton(drinks_frames_list[0][1], text="Chocolate Milkshake", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        milkshake_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        milkshake_price = customtkinter.CTkButton(drinks_frames_list[0][1], text="Price: $7.99", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        milkshake_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Chocolate Milkshake Drink
        milkshake_atobtn = customtkinter.CTkButton(drinks_frames_list[0][1], text = "+", 
                                                   width=40, command = lambda: add(milkshake_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        milkshake_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Strawberry Juice
        strawberry_juice_lbl = customtkinter.CTkButton(drinks_frames_list[0][2], text="Strawberry Juice", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        strawberry_juice_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        strawberry_juice_price = customtkinter.CTkButton(drinks_frames_list[0][2], text="Price: $4.99", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        strawberry_juice_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Strawberry Juice
        strawberry_juice_atobtn = customtkinter.CTkButton(drinks_frames_list[0][2], text = "+", 
                                                          width=40, command = lambda: add(strawberry_juice_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        strawberry_juice_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Bubble Tea Drink
        boba_lbl = customtkinter.CTkButton(drinks_frames_list[1][0], text="Bubble Tea", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        boba_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        boba_price = customtkinter.CTkButton(drinks_frames_list[1][0], text="Price: $6.50", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        boba_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Bubble Tea Drink
        boba_atobtn = customtkinter.CTkButton(drinks_frames_list[1][0], text = "+", 
                                              width=40, command = lambda: add(boba_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        boba_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Hot Chocolate Drink
        hot_chocolate_lbl = customtkinter.CTkButton(drinks_frames_list[1][1], text="Hot Chocolate", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        hot_chocolate_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        hot_chocolate_price = customtkinter.CTkButton(drinks_frames_list[1][1], text="Price: $3.99", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        hot_chocolate_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Hot Chocolate Drink
        hot_chocolate_atobtn = customtkinter.CTkButton(drinks_frames_list[1][1], text = "+", 
                                                       width=40, command = lambda: add(hot_chocolate_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        hot_chocolate_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion

        # region | Label for Coffee Drink
        coffee_lbl = customtkinter.CTkButton(drinks_frames_list[1][2], text="Coffee", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        coffee_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        coffee_price = customtkinter.CTkButton(drinks_frames_list[1][2], text="Price: $4.50", 
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        coffee_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Coffee Drink
        coffee_atobtn = customtkinter.CTkButton(drinks_frames_list[1][2], text = "+", 
                                                width=40, command = lambda: add(coffee_lbl),
                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        coffee_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)
        # endregion


# ------------------------ Main Window Configurations ------------------------ #
window=customtkinter.CTk()                          # Creates a window 
window.title("Austin's Restaurant Ordering App")    # Title of the window
# Sets the size of the window to fill screen 
# The values in the string wil find the screen width and height and tuck it into the top left corner of the screen
window.geometry("1536x945-7+0")


# ---------------------------------- Frames ---------------------------------- #
# Top Navigation Bar
TopNavBarFrame = TopNavBar(window)
TopNavBarFrame.grid(column=0, row=0, sticky='nwes', columnspan=2)
TopNavBarFrame.configure(corner_radius=0, height=75, fg_color="#DEE2E6")

# Main Frame to store different frames (Mains, Appetisers, Desserts and Drinks)
main_windowframe = customtkinter.CTkFrame(window, height=800, corner_radius=0)
main_windowframe.grid(column=0, row=1, sticky='news', columnspan=2)
main_windowframe.columnconfigure(0, weight=1)

# region |  Frame for when the user first opens the program
welcome_frame = WelcomePage(main_windowframe)
welcome_frame.grid(column=0, row=0, sticky='news')
welcome_frame.configure(height=875, corner_radius=0)
# endregion

# region | Menu Selection
# Function to show the mains selection
def mains_page():
    MainsSelectionFrame = MainsSelection(main_windowframe)          # Calls the Class as the frame
    MainsSelectionFrame.grid(column=0, row=0, sticky='news')        # Grids the frame 
    MainsSelectionFrame.configure(height=875, corner_radius=0)      # Configurations to the frame 

# Function to show the appetisers selection
def appetisers_page():
    AppetiserFrame = AppetiserSelection(main_windowframe)           # Calls the Class as the frame 
    AppetiserFrame.grid(column=0, row=0, sticky='news')             # Grids the frame
    AppetiserFrame.configure(height=875, corner_radius=0)           # Configurations to the frame

# Function to show the desserts selection
def desserts_page():
    DessertFrame = DessertSelection(main_windowframe)             # Calls the Class as the frame
    DessertFrame.grid(column=0, row=0, sticky='news')             # Grids the frame
    DessertFrame.configure(height=875, corner_radius=0)           # Configurations to the frame

# Function to show the drinks selection
def drinks_page():
    global DrinksFrame
    DrinksFrame = DrinkSelection(main_windowframe)                # Calls the Class as the frame
    DrinksFrame.grid(column=0, row=0, sticky='news')              # Grids the frame
    DrinksFrame.configure(height=875, corner_radius=0,            # Configurations to the frame
                          scrollbar_button_color='#333333')    
# endregion

# Seperator
seperator_frame = customtkinter.CTkFrame(window, corner_radius=0, width=5, height=945, fg_color="black")
seperator_frame.grid(row=0, column=2, rowspan=2, sticky='ns')

# Order List
order_frame = customtkinter.CTkFrame(window, corner_radius=0,  width=500)
order_frame.grid(column=3, row=0, rowspan= 2, sticky='nsew')


# ---------------------------- Grid Configuration ---------------------------- #
window.grid_columnconfigure((0, 1, 3), weight=1)
window.grid_rowconfigure(1, weight =1)
main_windowframe.grid_rowconfigure(0, weight=1)


# ------------------------------ Order Section ------------------------------ #
# Grid Configuration
order_frame.grid_columnconfigure(0, weight=1)
order_frame.grid_rowconfigure(1, weight =1)
# region | Title for Order Section
order_lbl = customtkinter.CTkLabel(order_frame, text = "Order:", 
                                   font=customtkinter.CTkFont(family="Calibri", size=50, weight='bold', underline=True))
order_lbl.grid(row=0, column=0, sticky='nws', pady=5, padx=20)
# endregion

# region | Frame for Orders
order_list_frame = customtkinter.CTkScrollableFrame(order_frame, corner_radius=10, height=500, width=200)
order_list_frame.grid(row=1, column=0, pady=(10,0), padx=20, sticky='news', ipady=10, ipadx=10)
# endregion

# region | Total Label
totalorder_lbl = customtkinter.CTkLabel(order_frame, text = "Total Price: $0", text_color="white", 
                                        font=customtkinter.CTkFont(family="Calibri", size=35))
totalorder_lbl.grid(row=2, column=0, sticky='nw', pady=5, padx=20)
# endregion

# region | Button to place order
place_order_btn = customtkinter.CTkButton(order_frame, text="Place Order", text_color="black", fg_color="#333333",
                                          font=customtkinter.CTkFont(family="Calibri", size=50))
place_order_btn.grid(row=3, column=0, sticky="news", pady=5, padx=20)
# endregion

window.mainloop()