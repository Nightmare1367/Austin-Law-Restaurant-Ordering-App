"""
Restaurant Ordering App
Written by Austin Law

Note: Make sure you have CustomTkinter installed to ensure the program runs as intended.
This can be done by typing "pip3 install customtkinter" in the command prompt when ran as administrator.

You would also want to make sure that pillow is installed. 
This is done by typing "pip install --upgrade pip" and "pip install --upgrade Pillow" 
into the command prompt to install the Pillow module
"""

# region | Importing the Modules
import customtkinter
from tkinter import *
from PIL import Image
from datetime import date
from datetime import datetime
import random
# endregion


# region | Importing files
import about_page
# endregion


# region | Customisation of window
customtkinter.set_appearance_mode("dark")       # Sets the window to dark mode
customtkinter.set_default_color_theme("green")  # Makes the default colour for widgets with a changable background to green
# endregion


# Dictionary to store name and price of product
# This is used for the order section
PRICES = {
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
order = []


# -------------------------------- Functions --------------------------------- #
# Fucntion for Order ID
def order_id():
    global order_name
    # A list for the program to get the numbers and letters
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
               'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
    
    # Variables to store the randomised numbers and letters
    order_name = ""
    random_letter = ""
    random_number = ""

    # For loop to run 3 times 
    for i in range(0,3):
        random_letter += random.choice(letter)    # Selects 3 random letters and stores it in the random_letters variable
        random_number += str(random.choice(number))    # Selects 3 random numbers and stores it in the random_numbers variable

    # Combines the randomly selected letters and numbers together
    order_name += random_letter + random_number
    return order_name


# Function to display and update the cart
def printcart():
    # Looks for widgets and destroys the frame which stores the order
    for widget in order_list_frame.winfo_children():
        widget.destroy()  

    rownum = 0
    # Runs for however many items are in the cart
    for i in range(len(order)):
        # Displays the item in the format of "Name" | "Amount" | "Price"
        order_listlbl = customtkinter.CTkLabel(order_list_frame, text = (order[i][0] + " | x" + str(order[i][1]) + " | $" + str(order[i][2])), 
                                           font = customtkinter.CTkFont(family = "Calibri", size=25))
        order_listlbl.grid(row=rownum, column=0, pady=5, padx=5, sticky="nw")
        # Makes the items display one row below each other
        rownum += 1
    
    # Function to calculate the total cost
    def totalprice():
        global totalcost
        totalcost = 0
        # Runs for however many items are in the order
        for i in range(len(order)): 
            # Adds the total cost with the price specified in each list
            totalcost += order[i][2]
        return(str("{:.2f}".format(totalcost)))

    # Updating the order total label
    totalorder_lbl.configure(text="Total Price: $" + totalprice())


# Function to create a description page
def description_page(btn, img):
    # Creating a window for the description page
    about_window = customtkinter.CTkToplevel(window)
    about_window.title(btn.cget("text"))
    about_window.resizable(False, False)

    # Dimensions for the pop up window
    w = 700        # Width of window
    h = 300         # height of window
    ws = about_window.winfo_screenwidth()
    hs = about_window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    about_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Makes the window stay at the top
    about_window.attributes('-topmost',True)

    # Grid Configurations
    about_window.grid_rowconfigure((2), weight=1)
    about_window.grid_columnconfigure(1, weight=1)

    # Makes the keys and values from the description dictionary
    # into a list 
    item_list = list(about_page.DESCRIPTION.keys())     # List for keys
    item_list2 = list(about_page.DESCRIPTION.values())  # List for values
    # Finds the dish name and finds it in the keys from the description dictionary
    specific = item_list.index(btn.cget("text"))

    # Function to close the window
    def delete_window():
        about_window.destroy()
    
    # Back Button
    back_btn = customtkinter.CTkButton(about_window, fg_color="transparent", text = "< Back", 
                                       width=20, command=delete_window,
                                       font=customtkinter.CTkFont(family='Calibri',size=15))
    back_btn.grid(row=0, column=1, sticky='nw', pady=(10, 5), padx=20)

    # Image of item
    item_image=customtkinter.CTkLabel(about_window, image = img, text="")
    item_image.grid(column=0, row=0, pady=20, padx=(20,0), rowspan=3)

    # Name of the item
    item_name = customtkinter.CTkLabel(about_window, text=btn.cget("text"), font=customtkinter.CTkFont(family='Calibri',size=30, weight= 'bold', underline=True))
    item_name.grid(row=1, column=1, pady=(0, 15), padx=20, sticky="swn")

    # Widgets for description
    description_frame = customtkinter.CTkFrame(about_window, corner_radius=10)
    description_frame.grid(row=2, column=1, pady=(5,20), sticky="news", padx= 20)
    # Provides the description of the item
    item_description = customtkinter.CTkLabel(description_frame, text=f"About the Dish: \n{item_list2[specific][0]}", wraplength=350, 
                                              font=customtkinter.CTkFont(family="Calibri", size=15), justify=LEFT)
    item_description.grid(row=0, column=0, pady=10, padx=10, sticky="w")
    # Provides the ingredients typically used
    item_ingredient = customtkinter.CTkLabel(description_frame, text=f"Ingredients: \n{item_list2[specific][1]}", wraplength=350, 
                                             font=customtkinter.CTkFont(family="Calibri", size=15), justify=LEFT)
    item_ingredient.grid(row=1, column=0, pady=10, padx=10,sticky="w")


# Function to create receipt
def place_order():
    receipt = order_id_lbl.cget("text")
    receipt = receipt.replace("Order ID: ", "")

    # Gets the time and day of when the "Place Order" button was pressed
    order_day = date.today()
    order_time = datetime.now()

    def popupwindow():
        global pu_window, sizing
        # Creating pop up window
        pu_window = customtkinter.CTkToplevel(window)
        pu_window.title("No Items in Order")       # Title of the window
        # Makes the window unresizable on both axis
        pu_window.resizable(False, False)

        # Dimensions for the pop up window
        def sizing(w, h):
            ws = pu_window.winfo_screenwidth()
            hs = pu_window.winfo_screenheight()
            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            pu_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Makes the window stay at the top
        pu_window.attributes('-topmost',True)

        # Makes the widgets appear in the middle horizontally
        pu_window.grid_columnconfigure(0, weight=1)

    # Runs if there is nothing in the order list
    if len(order) == 0:
        # Opens window
        popupwindow()

        # Changes the dimensions to have a width of 350 and height of 120
        sizing(350, 120)

        # Widgets for the window
        # Title to give the general information of what went wrong
        noitems_title = customtkinter.CTkLabel(pu_window, text="Note: There are no items in the order.", text_color="white", 
                                               font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"))
        noitems_title.grid(row=0, column=0, pady=(20, 0), sticky="news")

        # A label wich includes an explanation on what they need to do
        noitems_lbl = customtkinter.CTkLabel(pu_window, text="Please add a dish before placing order.", text_color="white", 
                                             font=customtkinter.CTkFont(family="Calibri", size=17, weight="bold"))
        noitems_lbl.grid(row=1, column=0, pady=(5, 0), sticky="news")

    # Runs if there the total cost is between $0 and $5000
    elif 0 <= totalcost <= 5000:
        # Opens window
        popupwindow()

        # Changes the dimensions to have a width of 350 and height of 120
        sizing(350, 120)    
        
        # Called out when the yes button is pressed
        def createreceipt():
            # Destroys confirmation window
            pu_window.destroy()

            # Creates a new window
            popupwindow()
            
            # Changes the dimensions to have a width of 200 and height of 120
            sizing(200, 120)    
            pu_window.title("") # Title of Window

            # Thank You Label
            thankyou_title = customtkinter.CTkLabel(pu_window, text = "Thank You", 
                                                    font = customtkinter.CTkFont(family = "Calibri", size=20))
            thankyou_title.grid(row=0, column=0, pady=(20, 0), sticky="news")

            thankyou_lbl = customtkinter.CTkLabel(pu_window, text="for ordering",
                                                  font = customtkinter.CTkFont(family = "Calibri", size=20))
            thankyou_lbl.grid(row=1, column=0, pady=(5, 0), sticky="news")

            # Creates .txt file
            with open(f"Order/{receipt}", 'w') as file:
                # Writes the information of the order in the .txt file
                file.write("Austin's Restaurant Ordering App")
                file.write("\n________________________________________________________\n")
                file.write(order_day.strftime("%x"))        # Date of time order was made
                file.write("\n")
                file.write(order_time.strftime("%X"))       # Time of order
                file.write(f"\n\nOrder ID: {order_name}\n")  # Order ID
                file.write(f"Order: \n")
                for item in order:      # For loop to keep running for however many items were in the order 
                    # Follows the format of "Name", "Amount", and "Price" in a new line
                    file.write(f"{item[0]} | Amount: {item[1]}\n      Price: ${item[2]}\n\n")
                file.write("________________________________________________________")
                file.write("\n")
                file.write(totalorder_lbl.cget("text"))     # Total Cost of Order

            totalorder_lbl.configure(text = "Total: $0")    # Resets the total price to zero
            order_id_lbl.configure(text = "Order ID: " + order_id())    # Creates a new order ID
            # Clears the order displayed in the order frame
            for widget in order_list_frame.winfo_children():
                widget.destroy()  
            order.clear()       # Clears the list 
        
        def window_destroy():       # Function to destroy window
            pu_window.destroy()

        # Title of window
        pu_window.title("Place Order")

        # Grid Configurations
        pu_window.grid_columnconfigure(0, weight=0)
        pu_window.grid_rowconfigure(0, weight=1)

        # region | Widgets
        # Label asking user if they want to place order
        confirmationlbl = customtkinter.CTkLabel(pu_window, text="Would you like to place your order?", 
                                                 font=customtkinter.CTkFont(family="Calibri", size=20))
        confirmationlbl.grid(row=0, column=0, pady=(20, 0), padx=(20,0), sticky="news", columnspan = 2)

        # Button to place order
        yesbtn = customtkinter.CTkButton(pu_window, text="Yes", fg_color="transparent", 
                                         font=customtkinter.CTkFont(family="Calibri", size=15),
                                         corner_radius=10, command=createreceipt, width=30)
        yesbtn.grid(row=1, column=0, pady=10, padx=20, sticky="news")

        # Button to let user continue their order
        nobtn = customtkinter.CTkButton(pu_window, text="No", width=30, 
                                        font=customtkinter.CTkFont(family="Calibri", size=15),
                                        command=window_destroy, corner_radius=10, fg_color="transparent")
        nobtn.grid(row=1, column=1, pady=10, padx=20, sticky="news")
        # endregion

    # Runs if the total price is over $5,000
    elif totalcost > 5000: 
        # Opens window
        popupwindow()

        # Changes the dimensions to have a width of 350 and height of 120
        sizing(350, 120)
        # Creating pop up window
        pu_window.title("Not enough ingredients")       # Title of the window

        # Makes the window stay at the top
        pu_window.attributes('-topmost',True)

        # region | Label telling user they ordered too much
        unablelbl = customtkinter.CTkLabel(pu_window, text="Unable to complete order due to \nlack of ingredients.", 
                                           font=customtkinter.CTkFont(family="Calibri", size=20, weight="bold"))
        unablelbl.grid(row=0, column=0, pady=(10, 0), sticky="news")

        unablelbl1 = customtkinter.CTkLabel(pu_window, text="Please remove some items.\nSorry for the inconvenience.",
                                            font=customtkinter.CTkFont(family="Calibri", size=17, weight="bold"))
        unablelbl1.grid(row=1, column=0, pady=(5, 0), sticky="news")
        # endregion


# Function to add the order to the order
def add(btn):
    # Globalling Variable
    global order
    
    # Looks for the item selected
    prices_value = (PRICES[btn.cget("text")])         # Gets the price of the product
    decimal = "{:.2f}".format(prices_value)           # Makes the price show with 2 decimal places
    item = btn.cget("text")                           # Gets the name of the item

    # Updating the Order
    # If statement which looks at whether there is an existing item in the order
    if len(order) == 0:                              # If the item selected does not exist, this will run
        order.append([item, 1, float(decimal)])      # Appends the item to the list following the name, amount, and price
    # Runs this section if the item selected already exists in the list
    else:
        itemexist = False           # Variable which will be used to check if the item exists
        for i in range (len(order)): # For loop which will look at the specifed item 
            if order[i][0] == item:  # Runs if the item matches with order
                itemexist = True    # Changes variable to true
                order[i][1] += 1     # Adds 1 to the total amount of that item
                order[i][2] = round(order[i][2] + float(decimal),2)       # Updates the price to match the amount selected.

        # Runs if the item does not exist in the list
        if itemexist == False: 
            order.append([item, 1, float(decimal)])
    printcart()


# Function to remove the selected order
def remove(btn):
    global order
    prices_value = (PRICES[btn.cget("text")])   # Gets the price of the selected item
    decimal = "{:.2f}".format(prices_value)     # Converts the item to show up to 2 decimal points
    item = btn.cget("text")                     # Gets the name of the item
    
    # For loop which will remove the item from the list
    for i in range (len(order)):
        # Checks if the item matches with each other
        if order[i][0] == item: 
            # Runs if the amount of that item is one
            if order[i][1] == 1: 
                del(order[i])    # Delets the list
                break           # Breaks the code to prevent error
            # Runs if there are more than one of that item
            else:
                order[i][1] -= 1     # Subtracts one from the amount
                # Updates the price to show cost after removing the one item
                order[i][2] = round(order[i][2] - float(decimal),2)  
    printcart()


# --------------------------------- Classes ---------------------------------- #
class TopNavBar(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        global indicate, mains_indicator, mains_page
        # ---------------------------------- Widgets ---------------------------------- #
        # region | Buttons for the Top Navigation Bar
        # Mains Button
        mains_btn = customtkinter.CTkButton(self, text="Mains",
                                           font=customtkinter.CTkFont(family="Calibri", size=35), 
                                           fg_color="transparent", text_color="black", hover_color="gray",
                                           command=lambda: indicate(mains_indicator, mains_page))
        mains_btn.grid(column=0, row=0, padx=10, pady=10, sticky='we')

        # Appetisers Button
        appetisers_btn = customtkinter.CTkButton(self, text="Appetisers", 
                                                 font=customtkinter.CTkFont(family="Calibri", size=35), 
                                                 fg_color="transparent", text_color="black", hover_color="gray", 
                                                 command=lambda: indicate(appetisers_indicator, appetisers_page))
        appetisers_btn.grid(column=1, row=0, padx=10, pady=10, sticky='we')

        # Desserts Button
        dessert_btn = customtkinter.CTkButton(self, text="Desserts", 
                                              font=customtkinter.CTkFont(family="Calibri", size=35), 
                                              fg_color="transparent", text_color="black", hover_color="gray", 
                                              command=lambda: indicate(dessert_indicator, desserts_page))
        dessert_btn.grid(column=2, row=0, padx=10, pady=10, sticky='we')

        # Drinks Button
        drink_btn = customtkinter.CTkButton(self, text="Drinks", width=100,
                                              font=customtkinter.CTkFont(family="Calibri", size=35), 
                                              fg_color="transparent", text_color="black", hover_color="gray", 
                                              command=lambda: indicate(drinks_indicator, drinks_page))
        drink_btn.grid(column=3, row=0, padx=10, pady=10, sticky='we')
        # endregion

        # region | Frames which would act as an indicator for the buttons
        # The colour of the frame is made to match with the background colour of the navigation bar,
        # The functions within the class will change the colour to black to indicate which page the user is on
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
        def hide_indicate():                    # Changes the indicators #DEE2E6 to match the background of the top navigation frame
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
        title_top.grid(column=0, row=0, pady=(170,0))

        title_bottom = customtkinter.CTkLabel(self, text = "to Austin's Restaurant",  text_color="#DEE2E6",
                                             font = customtkinter.CTkFont(family="Calibri", size=40))
        title_bottom.grid(row=1, column=0)
        # endregion
        
        # region | Seperator Frame between Title and Description
        titledescription_frame = customtkinter.CTkFrame(self, fg_color='#DEE2E6', 
                                                        height=7, width=450, corner_radius=10)
        titledescription_frame.grid(row=2, column=0, pady=10)
        # endregion

        # region | Description of restaurant
        description = ("Austin's Restaurant offers a variety of dishes.\n"
                       "Start by either selecting one of the categories\n"
                       "on the top navigation bar or by clicking the \n"
                       "'Get Started' button below. Once you have finished\n"
                       "your order, click the 'Place Order' button to\n"
                       "complete your order.")
        
        description_lbl = customtkinter.CTkLabel(self, text=description, justify=CENTER, text_color="#DEE2E6",
                                                 font=customtkinter.CTkFont(family="Calibri", size=25))
        description_lbl.grid(row=3, column=0, pady=10)
        # endregion

        # region | Button To Mains Section
        getstartedbtn = customtkinter.CTkButton(self, text="Get Started", text_color="black", 
                                               fg_color="#DEE2E6", hover_color="gray",
                                               command = lambda: indicate(mains_indicator, mains_page),
                                               font=customtkinter.CTkFont(family="Calibri", size=25))
        getstartedbtn.grid(row=4, column=0, pady=5, ipady=5, ipadx=10)
        # endregion


# region | Pages
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
        cutlet_imgbtn = customtkinter.CTkButton(mains_frames_list[0][0], image=cutlet, text="",         # Configuration to buttons appearance
                                                fg_color='transparent', hover_color="#333333",          
                                                command = lambda: description_page(cutlet_lbl, cutlet)) # Opens description page for dish
        cutlet_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                       # Gridding for the image button

        # Lasagna Image
        lasagna = customtkinter.CTkImage(Image.open("Images/Mains/Lasagna.jpg"), size=(275, 200))       # Imports image 
        lasagna_imgbtn = customtkinter.CTkButton(mains_frames_list[0][1], image=lasagna, text="",       # Configuration to buttons appearance
                                                 fg_color='transparent', hover_color="#333333",         
                                                 command = lambda: description_page(lasagna_lbl, lasagna))      # Opens description page for dish  
        lasagna_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                      # Gridding for the image button

        # Burger Image
        burger = customtkinter.CTkImage(Image.open("Images/Mains/Burger.jpg"), size=(275, 200))         # Imports image 
        burger_imgbtn = customtkinter.CTkButton(mains_frames_list[0][2], image=burger, text="",         # Configuration to buttons appearance
                                                fg_color='transparent', hover_color="#333333",          
                                                command = lambda: description_page(burger_lbl, burger))         # Opens description page for dish 
        burger_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                       # Gridding for the image button

        # Butter Chicken Image
        butter_chicken = customtkinter.CTkImage(Image.open("Images/Mains/Butter_Chicken.jpg"), size=(275, 200)) # Imports image 
        butter_chicken_imgbtn = customtkinter.CTkButton(mains_frames_list[1][0], image=butter_chicken, text="", # Configuration to buttons appearance
                                                        fg_color='transparent', hover_color="#333333",            
                                                        command = lambda: description_page(butter_chicken_lbl,butter_chicken))        # Opens description page for dish    
        butter_chicken_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                         

        # Pasta Image
        pasta = customtkinter.CTkImage(Image.open("Images/Mains/Pasta.jpg"), size=(275, 200))           # Imports image 
        pasta_imgbtn = customtkinter.CTkButton(mains_frames_list[1][1], image=pasta, text="",           # Configuration to buttons appearance
                                               fg_color='transparent', hover_color="#333333",
                                               command = lambda: description_page(pasta_lbl, pasta))    # Opens description page for dish
        pasta_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                        # Gridding for the image button

        # Pizza Image
        pizza = customtkinter.CTkImage(Image.open("Images/Mains/Pizza.jpg"), size=(275, 200))           # Imports image   
        pizza_imgbtn = customtkinter.CTkButton(mains_frames_list[1][2], image=pizza, text="",           # Configuration to buttons appearance
                                               fg_color='transparent', hover_color="#333333",
                                               command = lambda: description_page(pizza_lbl, pizza),)   # Opens description page for dish
        pizza_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                        # Gridding for the image button

        # region | Placeholder Images
        placeholder = customtkinter.CTkImage(Image.open("Images/Placeholder.jpg"), size=(275,200))      # Imports image 
        placeholder1_imgbtn = customtkinter.CTkButton(mains_frames_list[2][0], image=placeholder, text = "",    # Configuration to buttons appearance
                                                      fg_color='transparent', hover_color="#333333",
                                                      command = lambda: description_page(mains_placeholder1_lbl, placeholder),) # Opens description page for dish
        placeholder1_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                 # Gridding for the image button
        
        placeholder1_imgbtn = customtkinter.CTkButton(mains_frames_list[2][1], image=placeholder, text = "",    # Configuration to buttons appearance
                                                      fg_color='transparent', hover_color="#333333",
                                                      command = lambda: description_page(mains_placeholder2_lbl, placeholder),) # Opens description page for dish
        placeholder1_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                 # Gridding for the image button

        placeholder1_imgbtn = customtkinter.CTkButton(mains_frames_list[2][2], image=placeholder, text = "",    # Configuration to buttons appearance
                                                      fg_color='transparent', hover_color="#333333",
                                                      command = lambda: description_page(mains_placeholder2_lbl, placeholder),) # Opens description page for dish
        placeholder1_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                 # Gridding for the image button
        # endregion

        # ----------------------------- Buttons / Labels ----------------------------- #
        # region | Cutlet Button / Label
        cutlet_lbl = customtkinter.CTkButton(mains_frames_list[0][0], text="Chicken Cutlet", 
                                             command = lambda: description_page(cutlet_lbl, cutlet),    # Opens description page for dish
                                             fg_color='transparent', hover_color="#333333",             # Changes to labels appearance
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))  # Font customisation
        cutlet_lbl.grid(row=1, column=0, sticky='news', pady=(5,0), padx=10)                # Griding for the widget

        cutlet_price = customtkinter.CTkButton(mains_frames_list[0][0], text="Price: $21.99", 
                                               command = lambda: description_page(cutlet_lbl, cutlet),  # Opens description page for dish
                                               fg_color='transparent', hover_color="#333333",               # Changes to labels appearance
                                               font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))    # Font customisation
        cutlet_price.grid(row=2, column=0, sticky='news', pady=(0, 10), padx=10)                # Griding for the widget

        # Add to Order Button for Cutlet
        cutlet_atobtn = customtkinter.CTkButton(mains_frames_list[0][0], text = "+", width=40,  # Configurations to buttons appearance
                                                command = lambda: add(cutlet_lbl),              # Adds the dish to order
                                                font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        cutlet_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)              # Griding for the widget

        # Remove Button for Cutlet
        cutlet_remove = customtkinter.CTkButton(mains_frames_list[0][0], text = "-", width=40,  # Configuration to buttons appearance
                                                fg_color='#e5383b', hover_color="#a4161a",          
                                                command = lambda: remove(cutlet_lbl),       # Removes dish from order
                                                font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        cutlet_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)              # Griding for the widget
        # endregion

        # region | Lasagna Button / Label
        lasagna_lbl = customtkinter.CTkButton(mains_frames_list[0][1], text="Lasagna", 
                                              command = lambda: description_page(lasagna_lbl, lasagna), # Opens description page for dish
                                              fg_color='transparent', hover_color="#333333",                # Configuration to labels appearance
                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25)) # Font customisation
        lasagna_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)                # Griding for the widget

        lasagna_price = customtkinter.CTkButton(mains_frames_list[0][1], text="Price: $15.00", 
                                                command = lambda: description_page(lasagna_lbl, lasagna),   # Opens description page for dish
                                                fg_color='transparent', hover_color="#333333",              # Configuration to labels appearance
                                                font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))   # Font customisation
        lasagna_price.grid(row=2, column=0, sticky='news', pady=(0, 10), padx=10)               # Griding for the widget

        # Add to Order Button for Lasagna
        lasagna_atobtn = customtkinter.CTkButton(mains_frames_list[0][1], text = "+", width=40, bg_color="#7f7768", # Configurations to buttons appearance
                                                 command = lambda: add(lasagna_lbl),                # Adds the dish to order
                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        lasagna_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)             # Griding for the widget

        # Remove Button for Lasagna
        lasagna_remove = customtkinter.CTkButton(mains_frames_list[0][1], text = "-", width=40, bg_color="#6c5e4d", # Configuration to buttons appearance
                                                 fg_color='#e5383b', hover_color="#a4161a",         
                                                 command = lambda: remove(lasagna_lbl),     # Removes dish from order
                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        lasagna_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)             # Griding for the widget
        # endregion

        # region | Burger Button / Label
        burger_lbl = customtkinter.CTkButton(mains_frames_list[0][2], text="Beef Burger", 
                                             command = lambda: description_page(burger_lbl, burger),    # Opens description page for dish
                                             fg_color='transparent', hover_color="#333333",             # Configuration to labels appearance
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))  # Font customisation
        burger_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)             # Griding for the widget

        burger_price = customtkinter.CTkButton(mains_frames_list[0][2], text="Price: $13.00", 
                                               command = lambda: description_page(burger_lbl, burger),  # Opens description page for dish
                                               fg_color='transparent', hover_color="#333333",               # Configuration to labels appearance
                                               font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))    # Font customisation
        burger_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)              # Griding for the widget

        # Add to Order Button for Burger
        burger_atobtn = customtkinter.CTkButton(mains_frames_list[0][2], text = "+", width=40, bg_color="#a39c81",  # Configurations to buttons appearance
                                                command = lambda: add(burger_lbl),              # Adds the dish to order
                                                font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        burger_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)              # Griding for the widget

        # Remove Button for Burger
        burger_remove = customtkinter.CTkButton(mains_frames_list[0][2], text = "-", width=40, bg_color="#a39c81",  # Configuration to buttons appearance
                                                fg_color='#e5383b', hover_color="#a4161a",          
                                                command = lambda: remove(burger_lbl),       # Removes dish from order
                                                font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        burger_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)              # Griding for the widget
        # endregion

        # region | Butter Chicken Button / Label
        butter_chicken_lbl = customtkinter.CTkButton(mains_frames_list[1][0], text="Butter Chicken", 
                                                     command = lambda: description_page(butter_chicken_lbl, butter_chicken),    # Opens description page for dish
                                                     fg_color='transparent', hover_color="#333333",             # Configuration to labels appearance
                                                     font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))  # Font customisation
        butter_chicken_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        butter_chicken_price = customtkinter.CTkButton(mains_frames_list[1][0], text="Price: $15.99", 
                                                       command = lambda: description_page(butter_chicken_lbl, butter_chicken),  # Opens description page for dish
                                                       fg_color='transparent', hover_color="#333333",               # Configuration to labels appearance
                                                       font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))    # Font customisation
        butter_chicken_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)              # Griding for the widget

        # Add to Order Button for Butter Chicken
        butter_chicken_atobtn = customtkinter.CTkButton(mains_frames_list[1][0], text = "+", width=40, bg_color="#e2e2d6",  # Configurations to buttons appearance
                                                        command = lambda: add(butter_chicken_lbl),              # Adds the dish to order
                                                        font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        butter_chicken_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)              # Griding for the widget

        # Remove Button for Butter Chicken
        butter_chicken_remove = customtkinter.CTkButton(mains_frames_list[1][0], text = "-", width=40, bg_color="#78021f",  # Configuration to buttons appearance
                                                        fg_color='#e5383b', hover_color="#a4161a",          
                                                        command = lambda: remove(butter_chicken_lbl),       # Removes dish from order
                                                        font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        butter_chicken_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)              # Griding for the widget
        # endregion

        # region | Pasta Button / Label
        pasta_lbl = customtkinter.CTkButton(mains_frames_list[1][1], text="Pasta", 
                                            command = lambda: description_page(pasta_lbl, pasta),   # Opens description page for dish
                                            fg_color='transparent', hover_color="#333333",              # Configuration to labels appearance
                                            font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))   # Font customisation
        pasta_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)              # Griding for the widget

        pasta_price = customtkinter.CTkButton(mains_frames_list[1][1], text="Price: $20.00", 
                                              command = lambda: description_page(pasta_lbl, pasta), # Opens description page for dish
                                              fg_color='transparent', hover_color="#333333",                # Configuration to labels appearance
                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25)) # Font customisation
        pasta_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)               # Griding for the widget

        # Add to Order Button for Pasta
        pasta_atobtn = customtkinter.CTkButton(mains_frames_list[1][1], text = "+", width=40, bg_color="#887a71",   # Configurations to buttons appearance
                                               command = lambda: add(pasta_lbl),                # Adds the dish to order
                                               font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        pasta_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)               # Griding for the widget

        # Remove Button for Pasta
        pasta_remove = customtkinter.CTkButton(mains_frames_list[1][1], text = "-", width=40, bg_color="#887a71",   # Configuration to buttons appearance
                                               fg_color='#e5383b', hover_color="#a4161a",           
                                               command = lambda: remove(pasta_lbl),     # Removes dish from order
                                               font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        pasta_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)               # Griding for the widget
        # endregion

        # region | Pizza Button / Label
        pizza_lbl = customtkinter.CTkButton(mains_frames_list[1][2], text="Pizza", 
                                            command = lambda: description_page(pizza_lbl, pizza),   # Opens description page for dish
                                            fg_color='transparent', hover_color="#333333",              # Configuration to labels appearance
                                            font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))   # Font customisation
        pizza_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)              # Griding for the widget

        pizza_price = customtkinter.CTkButton(mains_frames_list[1][2], text="Price: $13.99", 
                                              command = lambda: description_page(pizza_lbl, pizza), # Opens description page for dish
                                              fg_color='transparent', hover_color="#333333",                # Configuration to labels appearance
                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25)) # Font customisation
        pizza_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)               # Griding for the widget

        # Add to Order Button for Pizza
        pizza_atobtn = customtkinter.CTkButton(mains_frames_list[1][2], text = "+", width=40, bg_color="#a67d69",   # Configurations to buttons appearance
                                               command = lambda: add(pizza_lbl),                # Adds the dish to order
                                               font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        pizza_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)               # Griding for the widget

        # Remove Button for Pizza
        pizza_remove = customtkinter.CTkButton(mains_frames_list[1][2], text = "-", width=40, bg_color="#953b21",   # Configuration to buttons appearance
                                               fg_color='#e5383b', hover_color="#a4161a",           
                                               command = lambda: remove(pizza_lbl),     # Removes dish from order
                                               font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        pizza_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)               # Griding for the widget
        # endregion

        # region | Placeholder Button \ Label
        # Label for Placeholder 1
        mains_placeholder1_lbl = customtkinter.CTkButton(mains_frames_list[2][0], text="Mains Placeholder", 
                                                         command = lambda: description_page(mains_placeholder1_lbl, placeholder),   # Opens description page for dish
                                                         fg_color='transparent', hover_color="#333333",             # Configuration to labels appearance
                                                         font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))  # Font customisation
        mains_placeholder1_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)             # Griding for the widget

        mains_placeholder1_price = customtkinter.CTkButton(mains_frames_list[2][0], text="Price: $25.00", 
                                                           command = lambda: description_page(mains_placeholder1_lbl, placeholder), # Opens description page for dish
                                                           fg_color='transparent', hover_color="#333333",               # Configuration to labels appearance
                                                           font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))    # Font customisation
        mains_placeholder1_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)              # Griding for the widget

        # Add to Order Button for Placeholder 1
        mains_placeholder1_atobtn = customtkinter.CTkButton(mains_frames_list[2][0], text = "+", bg_color="white",  # Configurations to buttons appearance
                                                            width=40, command = lambda: add(mains_placeholder1_lbl),                # Adds the dish to order
                                                            font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        mains_placeholder1_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)              # Griding for the widget

        # Remove Button for Placeholder 1
        mains_placeholder1_remove = customtkinter.CTkButton(mains_frames_list[2][0], text = "-", width=40, bg_color="white",    # Configuration to buttons appearance
                                                            fg_color='#e5383b', hover_color="#a4161a",          
                                                            command = lambda: remove(mains_placeholder1_lbl),       # Removes dish from order
                                                            font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        mains_placeholder1_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)              # Griding for the widget


        # Label for Placeholder 2
        mains_placeholder2_lbl = customtkinter.CTkButton(mains_frames_list[2][1], text="Mains Placeholder", 
                                                         command = lambda: description_page(mains_placeholder2_lbl, placeholder),   # Opens description page for dish
                                                         fg_color='transparent', hover_color="#333333",             # Configuration to labels appearance
                                                         font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))  # Font customisation
        mains_placeholder2_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)             # Griding for the widget

        mains_placeholder2_price = customtkinter.CTkButton(mains_frames_list[2][1], text="Price: $25.00",
                                                           command = lambda: description_page(mains_placeholder2_lbl, placeholder), # Opens description page for dish
                                                           fg_color='transparent', hover_color="#333333",               # Configuration to labels appearance
                                                           font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))    # Font customisation
        mains_placeholder2_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)              # Griding for the widget

        # Add to Order Button for Placeholder 2
        mains_placeholder2_atobtn = customtkinter.CTkButton(mains_frames_list[2][1], text = "+", bg_color="white",  # Configurations to buttons appearance
                                                            width=40, command = lambda: add(mains_placeholder2_lbl),                # Adds the dish to order
                                                            font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        mains_placeholder2_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)              # Griding for the widget

        # Remove Button for Placeholder 2 
        mains_placeholder2_remove = customtkinter.CTkButton(mains_frames_list[2][1], text = "-", width=40, bg_color="white",    # Configuration to buttons appearance
                                                            fg_color='#e5383b', hover_color="#a4161a",          
                                                            command = lambda: remove(mains_placeholder2_lbl),       # Removes dish from order
                                                            font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        mains_placeholder2_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)              # Griding for the widget


        # Label for Placeholder 3
        mains_placeholder3_lbl = customtkinter.CTkButton(mains_frames_list[2][2], text="Mains Placeholder", 
                                                         command = lambda: description_page(mains_placeholder3_lbl, placeholder),   # Opens description page for dish
                                                         fg_color='transparent', hover_color="#333333",             # Configuration to labels appearance
                                                         font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))  # Font customisation
        mains_placeholder3_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)             # Griding for the widget

        mains_placeholder3_price = customtkinter.CTkButton(mains_frames_list[2][2], text="Price: $25.00", 
                                                           command = lambda: description_page(mains_placeholder3_lbl, placeholder), # Opens description page for dish
                                                           fg_color='transparent', hover_color="#333333",               # Configuration to labels appearance
                                                           font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))    # Font customisation
        mains_placeholder3_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)              # Griding for the widget

        # Add to Order Button for Placeholder 3
        mains_placeholder3_atobtn = customtkinter.CTkButton(mains_frames_list[2][2], text = "+", bg_color="white",      # Configuration to buttons appearance
                                                            width=40, command = lambda: add(mains_placeholder3_lbl),    # Adds dish to order
                                                            font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        mains_placeholder3_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)              # Griding for the widget

        # Remove Button for Placeholder3
        mains_placeholder3_remove = customtkinter.CTkButton(mains_frames_list[2][2], text = "-", width=40, bg_color="white",
                                                            fg_color='#e5383b', hover_color="#a4161a",
                                                            command = lambda: remove(mains_placeholder3_lbl),       # Removes dish from order
                                                            font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        mains_placeholder3_remove.grid(row=0, column=0, sticky="ne", pady=25, padx=75)              # Griding for the widget
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
        shoe_string_imgbtn = customtkinter.CTkButton(appetisers_frames_list[0][0], image=shoe_string, text="",               # Puts the image in a button
                                                     fg_color='transparent', hover_color="#333333",                          # Configuration to button background
                                                     command = lambda: description_page(shoe_string_lbl, shoe_string))       # Opens description page for dish
        shoe_string_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Hand Cut Fries Image
        hand_cut = customtkinter.CTkImage(Image.open("Images/Appetisers/Hand_Cut.jpg"), size=(275, 200))                    # Imports image 
        hand_cut_imgbtn = customtkinter.CTkButton(appetisers_frames_list[0][1], image=hand_cut, text="",                    # Puts the image in a button
                                                  fg_color='transparent', hover_color="#333333",                            # Configuration to button background 
                                                  command = lambda: description_page(hand_cut_lbl, hand_cut))               # Opens description page for dish
        hand_cut_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Onion Rings Image
        onion_rings = customtkinter.CTkImage(Image.open("Images/Appetisers/Onion_Rings.jpg"), size=(275, 200))              # Imports image 
        onion_rings_imgbtn = customtkinter.CTkButton(appetisers_frames_list[0][2], image=onion_rings, text="",              # Puts the image in a button
                                                     fg_color='transparent', hover_color="#333333",                         # Configuration to button background
                                                     command = lambda: description_page(onion_rings_lbl, onion_rings))      # Opens description page for dish
        onion_rings_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Caeser Salad Image
        caeser_salad = customtkinter.CTkImage(Image.open("Images/Appetisers/Caesar_Salad.jpg"), size=(275, 200))            # Imports image 
        caeser_salad_imgbtn = customtkinter.CTkButton(appetisers_frames_list[1][0], image=caeser_salad, text="",            # Puts the image in a button
                                                      fg_color='transparent', hover_color="#333333",                        # Configuration to button background
                                                      command = lambda: description_page(caeser_salad_lbl, caeser_salad))   # Opens description page for dish
        caeser_salad_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Chicken Nibbles Image
        chicken_nibbles = customtkinter.CTkImage(Image.open("Images/Appetisers/Chicken_Nibbles.jpg"), size=(275, 200))      # Imports image 
        chicken_nibbles_imgbtn = customtkinter.CTkButton(appetisers_frames_list[1][1], image=chicken_nibbles, text="",      # Puts the image in a button
                                                         fg_color='transparent', hover_color="#333333",                     # Configuration to button background
                                                         command = lambda: description_page(chicken_nibbles_lbl, chicken_nibbles))  # Opens description page for dish
        chicken_nibbles_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Garlic Bread Image
        garlic_bread = customtkinter.CTkImage(Image.open("Images/Appetisers/Garlic_Bread.jpg"), size=(275, 200))            # Imports image 
        garlic_bread_imgbtn = customtkinter.CTkButton(appetisers_frames_list[1][2], image=garlic_bread, text="",            # Puts the image in a button
                                                      fg_color='transparent', hover_color="#333333",                        # Configuration to button background
                                                      command = lambda: description_page(garlic_bread_lbl, garlic_bread))   # Opens description page for dish
        garlic_bread_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)

        # Seafood Chowder Image
        seafood_chowder = customtkinter.CTkImage(Image.open("Images/Appetisers/Seafood_Chowder.jpg"), size=(275, 200))      # Imports image 
        seafood_chowder_imgbtn = customtkinter.CTkButton(appetisers_frames_list[2][0], image=seafood_chowder, text="",      # Puts the image in a button
                                                         fg_color='transparent', hover_color="#333333",                     # Configuration to button background
                                                         command = lambda: description_page(seafood_chowder_lbl, seafood_chowder))  # Opens description page for dish
        seafood_chowder_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)

        # region | Placeholder Images
        placeholder1 = customtkinter.CTkImage(Image.open("Images/Placeholder.jpg"), size=(275,200))                         # Imports image 
        placeholder1_imgbtn = customtkinter.CTkButton(appetisers_frames_list[2][1], image=placeholder1, text = "",          # Puts the image in a button
                                                      fg_color='transparent', hover_color="#333333",                        # Configuration to button background
                                                      command = lambda: description_page(appetisers_placeholder1_lbl, placeholder1))    # Opens description page for dish
        placeholder1_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        
        placeholder2_imgbtn = customtkinter.CTkButton(appetisers_frames_list[2][2], image=placeholder1, text = "",          # Puts the image in a button
                                                      fg_color='transparent', hover_color="#333333",                        # Configuration to button background
                                                      command = lambda: description_page(appetisers_placeholder2_lbl, placeholder1))    # Opens description page for dish
        placeholder2_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # ----------------------------- Buttons / Labels ----------------------------- #
        # region | Label for Shoe String Fries
        shoe_string_lbl = customtkinter.CTkButton(appetisers_frames_list[0][0], text="Shoe String Fries", 
                                                  command = lambda: description_page(shoe_string_lbl, shoe_string),         # Opens description page for dish
                                                  fg_color='transparent', hover_color="#333333",                            # Configurations to button
                                                  font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        shoe_string_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)                                            # Gridding for button

        shoe_string_price = customtkinter.CTkButton(appetisers_frames_list[0][0], text="Price: $5.00", 
                                                    command = lambda: description_page(shoe_string_lbl, shoe_string),       # Opens description page for dish
                                                    fg_color='transparent', hover_color="#333333",                          # Configurations to button
                                                    font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        shoe_string_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)                                         # Gridding for button

        # Add to Order Button for Shoe String Fries
        shoe_string_atobtn = customtkinter.CTkButton(appetisers_frames_list[0][0], text = "+", bg_color="#7a9098",
                                                     width=40, command = lambda: add(shoe_string_lbl),                      # Adds one of dish to order
                                                     font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        shoe_string_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)                                             # Gridding for button

        # Remove Button for Shoe String Fries
        shoe_string_remove = customtkinter.CTkButton(appetisers_frames_list[0][0], text = "-", bg_color="#8597a1",
                                                     fg_color='#e5383b', hover_color="#a4161a",                             # Configurations to button
                                                     width=40, command = lambda: remove(shoe_string_lbl),                   # Removes one of dish from order
                                                     font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        shoe_string_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)                                             # Gridding for button
        # endregion

        # region | Label for Hand Cut Fries
        hand_cut_lbl = customtkinter.CTkButton(appetisers_frames_list[0][1], text="Hand Cut Fries", 
                                               command = lambda: description_page(hand_cut_lbl, hand_cut),
                                               fg_color='transparent', hover_color="#333333",
                                               font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        hand_cut_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        hand_cut_price = customtkinter.CTkButton(appetisers_frames_list[0][1], text="Price: $4.50", 
                                                 command = lambda: description_page(hand_cut_lbl, hand_cut),
                                                 fg_color='transparent', hover_color="#333333",
                                                 font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        hand_cut_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Hand Cut Fries
        hand_cut_atobtn = customtkinter.CTkButton(appetisers_frames_list[0][1], text = "+", bg_color="#e4e5e7",
                                                  width=40, command = lambda: add(hand_cut_lbl),
                                                  font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        hand_cut_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Hand Cut Fries
        hand_cut_remove = customtkinter.CTkButton(appetisers_frames_list[0][1], text = "-", 
                                                  fg_color='#e5383b', hover_color="#a4161a",
                                                  width=40, command = lambda: remove(hand_cut_lbl),
                                                  font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        hand_cut_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Onion Rings
        onion_rings_lbl = customtkinter.CTkButton(appetisers_frames_list[0][2], text="Onion Rings", 
                                                  command = lambda: description_page(onion_rings_lbl, onion_rings),
                                                  fg_color='transparent', hover_color="#333333",
                                                  font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        onion_rings_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)
        
        onion_rings_price = customtkinter.CTkButton(appetisers_frames_list[0][2], text="Price: $6.99", 
                                                    command = lambda: description_page(onion_rings_lbl, onion_rings),
                                                    fg_color='transparent', hover_color="#333333",
                                                    font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        onion_rings_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Onion Rings
        onion_rings_atobtn = customtkinter.CTkButton(appetisers_frames_list[0][2], text = "+", bg_color="#a29a8c",
                                                    width=40, command = lambda: add(onion_rings_lbl),
                                                    font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        onion_rings_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Onion Rings 
        onion_rings_remove = customtkinter.CTkButton(appetisers_frames_list[0][2], text = "-", bg_color="#b05e11",
                                                     fg_color='#e5383b', hover_color="#a4161a",
                                                    width=40, command = lambda: remove(onion_rings_lbl),
                                                    font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        onion_rings_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Caesar Salad
        caeser_salad_lbl = customtkinter.CTkButton(appetisers_frames_list[1][0], text="Caesar Salad", 
                                                   command = lambda: description_page(caeser_salad_lbl, caeser_salad),
                                                   fg_color='transparent', hover_color="#333333",
                                                   font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        caeser_salad_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        caeser_salad_price = customtkinter.CTkButton(appetisers_frames_list[1][0], text="Price: $5.50", 
                                                     command = lambda: description_page(caeser_salad_lbl, caeser_salad),
                                                     fg_color='transparent', hover_color="#333333",
                                                     font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        caeser_salad_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Caesar Salad
        caeser_salad_atobtn = customtkinter.CTkButton(appetisers_frames_list[1][0], text = "+", bg_color="#041237",
                                                      width=40, command = lambda: add(caeser_salad_lbl),
                                                      font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        caeser_salad_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Caesar Salad
        caeser_salad_remove = customtkinter.CTkButton(appetisers_frames_list[1][0], text = "-", bg_color="#5a6e9a",
                                                      fg_color='#e5383b', hover_color="#a4161a",
                                                     width=40, command = lambda: remove(caeser_salad_lbl),
                                                     font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        caeser_salad_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Chicken Nibbles
        chicken_nibbles_lbl = customtkinter.CTkButton(appetisers_frames_list[1][1], text="Chicken Nibbles", 
                                                      command = lambda: description_page(chicken_nibbles_lbl, chicken_nibbles),
                                                      fg_color='transparent', hover_color="#333333",
                                                      font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        chicken_nibbles_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        chicken_nibbles_price = customtkinter.CTkButton(appetisers_frames_list[1][1], text="Price: $5.50", 
                                                        command = lambda: description_page(chicken_nibbles_lbl, chicken_nibbles),
                                                        fg_color='transparent', hover_color="#333333",
                                                        font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        chicken_nibbles_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Chicken Nibbles
        chicken_nibbles_atobtn = customtkinter.CTkButton(appetisers_frames_list[1][1], text = "+",
                                                         width=40, command = lambda: add(chicken_nibbles_lbl),
                                                         font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        chicken_nibbles_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Chicken Nibbles
        chicken_nibbles_remove = customtkinter.CTkButton(appetisers_frames_list[1][1], text = "-", bg_color="#ea6d3c",
                                                         fg_color='#e5383b', hover_color="#a4161a",
                                                         width=40, command = lambda: remove(chicken_nibbles_lbl),
                                                         font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        chicken_nibbles_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Garlic Bread
        garlic_bread_lbl = customtkinter.CTkButton(appetisers_frames_list[1][2], text="Garlic Bread", 
                                                   command = lambda: description_page(garlic_bread_lbl, garlic_bread),
                                                   fg_color='transparent', hover_color="#333333",
                                                   font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        garlic_bread_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        garlic_bread_price = customtkinter.CTkButton(appetisers_frames_list[1][2], text="Price: $3.50", 
                                                     command = lambda: description_page(garlic_bread_lbl, garlic_bread),
                                                     fg_color='transparent', hover_color="#333333",
                                                     font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        garlic_bread_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Garlic Bread
        garlic_bread_atobtn = customtkinter.CTkButton(appetisers_frames_list[1][2], text = "+", bg_color="#953c1a",
                                                      width=40, command = lambda: add(garlic_bread_lbl),
                                                      font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        garlic_bread_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Garlic Bread
        garlic_bread_remove = customtkinter.CTkButton(appetisers_frames_list[1][2], text = "-", bg_color="#f38a45",
                                                      fg_color='#e5383b', hover_color="#a4161a",
                                                      width=40, command = lambda: remove(garlic_bread_lbl),
                                                      font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        garlic_bread_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Seafood Chowder
        seafood_chowder_lbl = customtkinter.CTkButton(appetisers_frames_list[2][0], text="Seafood Chowder", 
                                                      command = lambda: description_page(seafood_chowder_lbl, seafood_chowder),
                                                      fg_color='transparent', hover_color="#333333",
                                                      font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        seafood_chowder_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        seafood_chowder_price = customtkinter.CTkButton(appetisers_frames_list[2][0], text="Price: $6.99", 
                                                        command = lambda: description_page(seafood_chowder_lbl, seafood_chowder),
                                                        fg_color='transparent', hover_color="#333333",
                                                        font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        seafood_chowder_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Seafood Chowder
        seafood_chowder_atobtn = customtkinter.CTkButton(appetisers_frames_list[2][0], text = "+", bg_color="#d69c64",
                                                         width=40, command = lambda: add(seafood_chowder_lbl),
                                                         font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        seafood_chowder_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Seafood Chowder
        seafood_chowder_remove = customtkinter.CTkButton(appetisers_frames_list[2][0], text = "-", bg_color="#f6ead7",
                                                         fg_color='#e5383b', hover_color="#a4161a",
                                                         width=40, command = lambda: remove(seafood_chowder_lbl),
                                                         font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        seafood_chowder_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Placeholder Button \ Label
        # Label for Placeholder 1
        appetisers_placeholder1_lbl = customtkinter.CTkButton(appetisers_frames_list[2][1], text="Appetiser Placeholder", 
                                                              command = lambda: description_page(appetisers_placeholder1_lbl, placeholder1),
                                                              fg_color='transparent', hover_color="#333333",
                                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        appetisers_placeholder1_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        appetisers_placeholder1_price = customtkinter.CTkButton(appetisers_frames_list[2][1], text="Price: $3.99", 
                                                                command = lambda: description_page(appetisers_placeholder1_lbl, placeholder1),
                                                                fg_color='transparent', hover_color="#333333",
                                                                font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        appetisers_placeholder1_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 1
        appetisers_placeholder1_atobtn = customtkinter.CTkButton(appetisers_frames_list[2][1], text = "+", bg_color="white",
                                                                 width=40, command = lambda: add(appetisers_placeholder1_lbl),
                                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        appetisers_placeholder1_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Placeholder 1
        appetisers_placeholder1_remove = customtkinter.CTkButton(appetisers_frames_list[2][1], text = "-", bg_color="white",
                                                                 fg_color='#e5383b', hover_color="#a4161a",
                                                                 width=40, command = lambda: remove(appetisers_placeholder1_lbl),
                                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        appetisers_placeholder1_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)


        # Label for Placeholder 2
        appetisers_placeholder2_lbl = customtkinter.CTkButton(appetisers_frames_list[2][2], text="Appetiser Placeholder", 
                                                              command = lambda: description_page(appetisers_placeholder2_lbl, placeholder1),
                                                              fg_color='transparent', hover_color="#333333",
                                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        appetisers_placeholder2_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        appetisers_placeholder2_price = customtkinter.CTkButton(appetisers_frames_list[2][2], text="Price: $3.99", 
                                                                command = lambda: description_page(appetisers_placeholder2_lbl, placeholder1),
                                                                fg_color='transparent', hover_color="#333333",
                                                                font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        appetisers_placeholder2_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 2
        appetisers_placeholder2_atobtn = customtkinter.CTkButton(appetisers_frames_list[2][2], text = "+", bg_color="white",
                                                                 width=40, command = lambda: add(appetisers_placeholder2_lbl),
                                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        appetisers_placeholder2_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Placeholder 2
        appetisers_placeholder2_remove = customtkinter.CTkButton(appetisers_frames_list[2][2], text = "-", bg_color="white",
                                                                 fg_color='#e5383b', hover_color="#a4161a",
                                                                 width=40, command = lambda: remove(appetisers_placeholder2_lbl),
                                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        appetisers_placeholder2_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
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
                                                       fg_color='transparent', hover_color="#333333",               # Configuration to button background
                                                       command = lambda: description_page(apple_crumble_lbl, apple_crumble))   # Opens description page for dish            
        apple_crumble_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                            # Gridding for image

        # Brownie Image
        brownie = customtkinter.CTkImage(Image.open("Images/Desserts/Brownie.jpg"), size=(275, 200))                
        brownie_imgbtn = customtkinter.CTkButton(desserts_frames_list[0][1], image=brownie, text="",                
                                                 fg_color='transparent', hover_color="#333333",
                                                 command = lambda: description_page(brownie_lbl, brownie))                     
        brownie_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Cheesecake Image
        cheesecake = customtkinter.CTkImage(Image.open("Images/Desserts/Cheesecake.jpg"), size=(275, 200))          
        cheesecake_imgbtn = customtkinter.CTkButton(desserts_frames_list[0][2], image=cheesecake, text="",          
                                                    fg_color='transparent', hover_color="#333333",
                                                    command = lambda: description_page(cheesecake_lbl, cheesecake))                  
        cheesecake_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Ice Cream Image
        ice_cream = customtkinter.CTkImage(Image.open("Images/Desserts/Ice_Cream.jpg"), size=(275, 200))            
        ice_cream_imgbtn = customtkinter.CTkButton(desserts_frames_list[1][0], image=ice_cream, text="",            
                                                   fg_color='transparent', hover_color="#333333",
                                                   command = lambda: description_page(ice_cream_lbl, ice_cream))                   
        ice_cream_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Macaron Image
        macaron = customtkinter.CTkImage(Image.open("Images/Desserts/Macaron.jpg"), size=(275, 200))                
        macaron_imgbtn = customtkinter.CTkButton(desserts_frames_list[1][1], image=macaron, text="",                
                                                 fg_color='transparent', hover_color="#333333",
                                                 command = lambda: description_page(macaron_lbl, macaron))                     
        macaron_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 

        # Panna Cotta Image
        panna_cotta = customtkinter.CTkImage(Image.open("Images/Desserts/Panna_Cotta.jpg"), size=(275, 200))        
        panna_cotta_imgbtn = customtkinter.CTkButton(desserts_frames_list[1][2], image=panna_cotta, text="",        
                                                     fg_color='transparent', hover_color="#333333",
                                                     command = lambda: description_page(panna_cotta_lbl, panna_cotta))                 
        panna_cotta_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 
        # endregion

        # region | Placeholder Images
        placeholder1 = customtkinter.CTkImage(Image.open("Images/Placeholder.jpg"), size=(275,200))
        placeholder1_imgbtn = customtkinter.CTkButton(desserts_frames_list[2][0], image=placeholder1, text = "",
                                                      fg_color='transparent', hover_color="#333333",
                                                      command = lambda: description_page(desserts_placeholder1_lbl, placeholder1))                        
        placeholder1_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        
        placeholder2_imgbtn = customtkinter.CTkButton(desserts_frames_list[2][1], image=placeholder1, text = "",
                                                      fg_color='transparent', hover_color="#333333",
                                                      command = lambda: description_page(desserts_placeholder2_lbl, placeholder1))
        placeholder2_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion


        # ----------------------------- Buttons / Labels ----------------------------- #
        # region | Label for Apple Crumble
        apple_crumble_lbl = customtkinter.CTkButton(desserts_frames_list[0][0], text="Apple Crumble", 
                                                    command = lambda: description_page(apple_crumble_lbl, apple_crumble),          # Opens description page for dish
                                                    fg_color='transparent', hover_color="#333333",                                 # Configurations for button
                                                    font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        apple_crumble_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)                                                 # Gridding for button

        apple_crumble_price = customtkinter.CTkButton(desserts_frames_list[0][0], text="Price: $10.50", 
                                                      command = lambda: description_page(apple_crumble_lbl, apple_crumble),         # Opens description page for dish
                                                      fg_color='transparent', hover_color="#333333",                                # Configurations for button
                                                      font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        apple_crumble_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)                                               # Gridding for button

        # Add to Order Button for Apple Crumble
        apple_crumble_atobtn = customtkinter.CTkButton(desserts_frames_list[0][0], text = "+", bg_color="#606471",
                                                       width=40, command = lambda: add(apple_crumble_lbl),                          # Adds one of dish to order
                                                       font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        apple_crumble_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)                                                   # Gridding for button

        # Remove Button for Apple Crumble
        apple_crumble_remove = customtkinter.CTkButton(desserts_frames_list[0][0], text = "-", bg_color="#6d7d95",
                                                       fg_color='#e5383b', hover_color="#a4161a",
                                                       width=40, command = lambda: remove(apple_crumble_lbl),                       # Removes one of dish from order
                                                       font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        apple_crumble_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)                                                   # Gridding for button
        # endregion

        # region | Label for Brownie
        brownie_lbl = customtkinter.CTkButton(desserts_frames_list[0][1], text="Brownie", 
                                              command = lambda: description_page(brownie_lbl, brownie),
                                              fg_color='transparent', hover_color="#333333",
                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        brownie_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        brownie_price = customtkinter.CTkButton(desserts_frames_list[0][1], text="Price: $8.99", 
                                                command = lambda: description_page(brownie_lbl, brownie),
                                                fg_color='transparent', hover_color="#333333",
                                                font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        brownie_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Brownie
        brownie_atobtn = customtkinter.CTkButton(desserts_frames_list[0][1], text = "+", 
                                                 width=40, command = lambda: add(brownie_lbl),
                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        brownie_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Brownie
        brownie_remove = customtkinter.CTkButton(desserts_frames_list[0][1], text = "-", 
                                                 fg_color='#e5383b', hover_color="#a4161a",
                                                 width=40, command = lambda: remove(brownie_lbl),
                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        brownie_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Cheesecake
        cheesecake_lbl = customtkinter.CTkButton(desserts_frames_list[0][2], text="Cheesecake", 
                                                 command = lambda: description_page(cheesecake_lbl, cheesecake),
                                                 fg_color='transparent', hover_color="#333333",
                                                 font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        cheesecake_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        cheesecake_price = customtkinter.CTkButton(desserts_frames_list[0][2], text="Price: $6.99", 
                                                   command = lambda: description_page(cheesecake_lbl, cheesecake),
                                                   fg_color='transparent', hover_color="#333333",
                                                   font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        cheesecake_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Cheesecake
        cheesecake_atobtn = customtkinter.CTkButton(desserts_frames_list[0][2], text = "+", bg_color="#fac6c8",
                                                    width=40, command = lambda: add(cheesecake_lbl),
                                                    font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        cheesecake_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Cheescake
        cheesecake_remove = customtkinter.CTkButton(desserts_frames_list[0][2], text = "-", bg_color="#fac6c8",
                                                    fg_color='#e5383b', hover_color="#a4161a",
                                                    width=40, command = lambda: remove(cheesecake_lbl),
                                                    font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        cheesecake_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Ice Cream
        ice_cream_lbl = customtkinter.CTkButton(desserts_frames_list[1][0], text="Ice Cream", 
                                                command = lambda: description_page(ice_cream_lbl, ice_cream),
                                                fg_color='transparent', hover_color="#333333",
                                                font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        ice_cream_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)                                                      

        ice_cream_price = customtkinter.CTkButton(desserts_frames_list[1][0], text="Price: $12.50", 
                                                  command = lambda: description_page(ice_cream_lbl, ice_cream),
                                                  fg_color='transparent', hover_color="#333333",
                                                  font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        ice_cream_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Ice Cream
        ice_cream_atobtn = customtkinter.CTkButton(desserts_frames_list[1][0], text = "+", bg_color="#889baa",
                                                   width=40, command = lambda: add(ice_cream_lbl),
                                                   font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        ice_cream_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Ice Cream
        ice_cream_remove = customtkinter.CTkButton(desserts_frames_list[1][0], text = "-", bg_color="#8a9199",
                                                   fg_color='#e5383b', hover_color="#a4161a",
                                                   width=40, command = lambda: remove(ice_cream_lbl),
                                                   font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        ice_cream_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Macaron
        macaron_lbl = customtkinter.CTkButton(desserts_frames_list[1][1], text="Macaron", 
                                              command = lambda: description_page(macaron_lbl, macaron),
                                              fg_color='transparent', hover_color="#333333",
                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        macaron_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        macaron_price = customtkinter.CTkButton(desserts_frames_list[1][1], text="Price: $12.00", 
                                                command = lambda: description_page(macaron_lbl, macaron),
                                                fg_color='transparent', hover_color="#333333",
                                                font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        macaron_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Macaron
        macaron_atobtn = customtkinter.CTkButton(desserts_frames_list[1][1], text = "+", bg_color="#c9c9b4",
                                                 width=40, command = lambda: add(macaron_lbl),
                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        macaron_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Macaron
        macaron_remove = customtkinter.CTkButton(desserts_frames_list[1][1], text = "-", bg_color="#7d4d59",
                                                 fg_color='#e5383b', hover_color="#a4161a",
                                                 width=40, command = lambda: remove(macaron_lbl),
                                                 font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        macaron_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Panna Cotta
        panna_cotta_lbl = customtkinter.CTkButton(desserts_frames_list[1][2], text="Panna Cotta", 
                                                  command = lambda: description_page(panna_cotta_lbl, panna_cotta),
                                                  fg_color='transparent', hover_color="#333333",
                                                  font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        panna_cotta_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        panna_cotta_price = customtkinter.CTkButton(desserts_frames_list[1][2], text="Price: $5.90", 
                                                    command = lambda: description_page(panna_cotta_lbl, panna_cotta),
                                                    fg_color='transparent', hover_color="#333333",
                                                    font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        panna_cotta_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)
        
        # Add to Order Button for Panna Cotta
        panna_cotta_atobtn = customtkinter.CTkButton(desserts_frames_list[1][2], text = "+", bg_color="#475863",
                                                     width=40, command = lambda: add(panna_cotta_lbl),
                                                     font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        panna_cotta_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Panna Cotta
        panna_cotta_remove = customtkinter.CTkButton(desserts_frames_list[1][2], text = "-", bg_color="#4b7584",
                                                     fg_color='#e5383b', hover_color="#a4161a",
                                                     width=40, command = lambda: remove(panna_cotta_lbl),
                                                     font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        panna_cotta_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Placeholder Button \ Label
        # Label for Placeholder 1
        desserts_placeholder1_lbl = customtkinter.CTkButton(desserts_frames_list[2][0], text="Dessert Placeholder", 
                                                            command = lambda: description_page(desserts_placeholder1_lbl, placeholder1),
                                                            fg_color='transparent', hover_color="#333333",
                                                            font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        desserts_placeholder1_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        desserts_placeholder1_price = customtkinter.CTkButton(desserts_frames_list[2][0], text="Price: $5.00", 
                                                              command = lambda: description_page(desserts_placeholder1_lbl, placeholder1),
                                                              fg_color='transparent', hover_color="#333333",
                                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        desserts_placeholder1_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 1
        desserts_placeholder1_atobtn = customtkinter.CTkButton(desserts_frames_list[2][0], text = "+", bg_color="white",
                                                               width=40, command = lambda: add(desserts_placeholder1_lbl),
                                                               font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        desserts_placeholder1_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Placeholder 1
        desserts_placeholder1_remove = customtkinter.CTkButton(desserts_frames_list[2][0], text = "-", bg_color="white",
                                                               fg_color='#e5383b', hover_color="#a4161a",
                                                               width=40, command = lambda: remove(desserts_placeholder1_lbl),
                                                               font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        desserts_placeholder1_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)

        # Label for Placeholder 2
        desserts_placeholder2_lbl = customtkinter.CTkButton(desserts_frames_list[2][1], text="Dessert Placeholder", 
                                                            command = lambda: description_page(desserts_placeholder2_lbl, placeholder1),
                                                            fg_color='transparent', hover_color="#333333",
                                                            font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        desserts_placeholder2_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        desserts_placeholder2_price = customtkinter.CTkButton(desserts_frames_list[2][1], text="Price: $5.00", 
                                                              command = lambda: description_page(desserts_placeholder2_lbl, placeholder1),
                                                              fg_color='transparent', hover_color="#333333",
                                                              font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        desserts_placeholder2_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Placeholder 2
        desserts_placeholder2_atobtn = customtkinter.CTkButton(desserts_frames_list[2][1], text = "+", bg_color="white",
                                                               width=40, command = lambda: add(desserts_placeholder2_lbl),
                                                               font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        desserts_placeholder2_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Placeholder 2
        desserts_placeholder2_remove = customtkinter.CTkButton(desserts_frames_list[2][1], text = "-", bg_color="white",
                                                               fg_color='#e5383b', hover_color="#a4161a",
                                                               width=40, command = lambda: remove(desserts_placeholder2_lbl),
                                                               font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        desserts_placeholder2_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
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
        coke = customtkinter.CTkImage(Image.open("Images/Drinks/Coke.jpg"), size=(275,200))             # Imports Image 
        coke_imgbtn = customtkinter.CTkButton(drinks_frames_list[0][0], image=coke, text="",
                                              command = lambda: description_page(coke_lbl, coke),       # Opens description page for drink
                                              fg_color='transparent', hover_color="#333333")            # Configuration to image button
        coke_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)                         # Gridding for button
        # endregion

        # region | Milkshake Image
        milkshake = customtkinter.CTkImage(Image.open("Images/Drinks/Milkshake.jpg"), size=(275,200))
        milkshake_imgbtn = customtkinter.CTkButton(drinks_frames_list[0][1], image=milkshake, text="", 
                                                   command = lambda: description_page(milkshake_lbl, milkshake),       
                                                   fg_color='transparent', hover_color="#333333")
        milkshake_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # region | Strawberry Juice Image
        strawberry_juice = customtkinter.CTkImage(Image.open("Images/Drinks/Strawberry_Juice.jpg"), size=(275,200))
        strawberry_juice_imgbtn = customtkinter.CTkButton(drinks_frames_list[0][2], image=strawberry_juice, text="",  
                                                          command = lambda: description_page(strawberry_juice_lbl, strawberry_juice),      
                                                          fg_color='transparent', hover_color="#333333")
        strawberry_juice_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # region | Bubble Tea Image
        boba = customtkinter.CTkImage(Image.open("Images/Drinks/Boba.jpg"), size=(275,200))
        boba_imgbtn = customtkinter.CTkButton(drinks_frames_list[1][0], image=boba, text="",
                                                    command = lambda: description_page(boba_lbl, boba),
                                                    fg_color='transparent', hover_color="#333333")
        boba_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # region | Hot Chocolate Image
        hot_chocolate = customtkinter.CTkImage(Image.open("Images/Drinks/Hot_Chocolate.jpg"), size=(275,200))
        hot_chocolate_imgbtn = customtkinter.CTkButton(drinks_frames_list[1][1], image=hot_chocolate, text="",
                                                       command = lambda: description_page(hot_chocolate_lbl, hot_chocolate),
                                                       fg_color='transparent', hover_color="#333333")
        hot_chocolate_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # region | Coffee Image
        coffee = customtkinter.CTkImage(Image.open("Images/Drinks/Coffee.png"), size=(275,200))
        coffee_imgbtn = customtkinter.CTkButton(drinks_frames_list[1][2], image=coffee, text="",
                                                command = lambda: description_page(coffee_lbl, coffee),
                                                fg_color='transparent', hover_color="#333333")
        coffee_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10)
        # endregion

        # ----------------------------- Buttons / Labels ----------------------------- #
        # region | Label for Coke Drink
        coke_lbl = customtkinter.CTkButton(drinks_frames_list[0][0], text="Coca-Cola",
                                           command = lambda: description_page(coke_lbl, coke),          # Opens description page for drink
                                           fg_color='transparent', hover_color="#333333",               # Configurations to button
                                           font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        coke_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)                               # Gridding for button

        coke_price = customtkinter.CTkButton(drinks_frames_list[0][0], text="Price: $2.99",
                                             command = lambda: description_page(coke_lbl, coke), 
                                             fg_color='transparent', hover_color="#333333",             # Configurations to button
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        coke_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)                            # Gridding for button

        # Add to Order Button for Coke Drink
        coke_atobtn = customtkinter.CTkButton(drinks_frames_list[0][0], text = "+", 
                                              width=40, command = lambda: add(coke_lbl),                # Adds one drink
                                              font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        coke_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)                                # Gridding for button

        # Remove Button for Coke Drink
        coke_remove = customtkinter.CTkButton(drinks_frames_list[0][0], text = "-", 
                                              fg_color='#e5383b', hover_color="#a4161a",                # Configurations to button
                                              width=40, command = lambda: remove(coke_lbl),             # Removes one drink
                                              font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        coke_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)                                # Gridding for button
        # endregion

        # region | Label for Chocolate Milkshake Drink
        milkshake_lbl = customtkinter.CTkButton(drinks_frames_list[0][1], text="Chocolate Milkshake", 
                                                command = lambda: description_page(milkshake_lbl, milkshake),
                                                fg_color='transparent', hover_color="#333333",
                                                font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        milkshake_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        milkshake_price = customtkinter.CTkButton(drinks_frames_list[0][1], text="Price: $7.99", 
                                                  command = lambda: description_page(milkshake_lbl, milkshake),
                                                  fg_color='transparent', hover_color="#333333",
                                                  font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        milkshake_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Chocolate Milkshake Drink
        milkshake_atobtn = customtkinter.CTkButton(drinks_frames_list[0][1], text = "+", bg_color="#e4dfda",
                                                   width=40, command = lambda: add(milkshake_lbl),
                                                   font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        milkshake_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Chocolate Milkshake Drink
        milkshake_remove = customtkinter.CTkButton(drinks_frames_list[0][1], text = "-", bg_color="#e6e1de",
                                                   fg_color='#e5383b', hover_color="#a4161a",
                                                   width=40, command = lambda: remove(milkshake_lbl),
                                                   font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        milkshake_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Strawberry Juice
        strawberry_juice_lbl = customtkinter.CTkButton(drinks_frames_list[0][2], text="Strawberry Juice",
                                                       command = lambda: description_page(strawberry_juice_lbl, strawberry_juice),
                                                       fg_color='transparent', hover_color="#333333",
                                                       font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        strawberry_juice_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        strawberry_juice_price = customtkinter.CTkButton(drinks_frames_list[0][2], text="Price: $4.99",
                                                         command = lambda: description_page(strawberry_juice_lbl, strawberry_juice),
                                                         fg_color='transparent', hover_color="#333333",
                                                         font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        strawberry_juice_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Strawberry Juice
        strawberry_juice_atobtn = customtkinter.CTkButton(drinks_frames_list[0][2], text = "+", bg_color="#f1f1f1",
                                                          width=40, command = lambda: add(strawberry_juice_lbl),
                                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        strawberry_juice_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Strawberry Juice
        strawberry_juice_remove = customtkinter.CTkButton(drinks_frames_list[0][2], text = "-", bg_color="#e30e31",
                                                          fg_color='#e5383b', hover_color="#a4161a",
                                                          width=40, command = lambda: remove(strawberry_juice_lbl),
                                                          font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        strawberry_juice_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Bubble Tea Drink
        boba_lbl = customtkinter.CTkButton(drinks_frames_list[1][0], text="Bubble Tea", 
                                           command = lambda: description_page(boba_lbl, boba),
                                           fg_color='transparent', hover_color="#333333",
                                           font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        boba_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        boba_price = customtkinter.CTkButton(drinks_frames_list[1][0], text="Price: $6.50",
                                             command = lambda: description_page(boba_lbl, boba), 
                                             fg_color='transparent', hover_color="#333333",
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        boba_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Bubble Tea Drink
        boba_atobtn = customtkinter.CTkButton(drinks_frames_list[1][0], text = "+", bg_color="#e2e2e2",
                                              width=40, command = lambda: add(boba_lbl),
                                              font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        boba_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Bubble Tea Drink
        boba_remove = customtkinter.CTkButton(drinks_frames_list[1][0], text = "-", bg_color="#dadada",
                                              width=40, command = lambda: remove(boba_lbl),
                                              fg_color='#e5383b', hover_color="#a4161a",
                                              font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        boba_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Hot Chocolate Drink
        hot_chocolate_lbl = customtkinter.CTkButton(drinks_frames_list[1][1], text="Hot Chocolate", 
                                                    command = lambda: description_page(hot_chocolate_lbl, hot_chocolate),
                                                    fg_color='transparent', hover_color="#333333",
                                                    font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        hot_chocolate_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        hot_chocolate_price = customtkinter.CTkButton(drinks_frames_list[1][1], text="Price: $3.99", 
                                                      command = lambda: description_page(hot_chocolate_lbl, hot_chocolate),
                                                      fg_color='transparent', hover_color="#333333",
                                                      font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        hot_chocolate_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Hot Chocolate Drink
        hot_chocolate_atobtn = customtkinter.CTkButton(drinks_frames_list[1][1], text = "+", bg_color="#c8c7cc",
                                                       width=40, command = lambda: add(hot_chocolate_lbl),
                                                       font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        hot_chocolate_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Hot Chocolate Drink
        hot_chocolate_remove = customtkinter.CTkButton(drinks_frames_list[1][1], text = "-", bg_color="#cbcacf",
                                                       width=40, command = lambda: remove(hot_chocolate_lbl),
                                                       fg_color='#e5383b', hover_color="#a4161a",
                                                       font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        hot_chocolate_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion

        # region | Label for Coffee Drink
        coffee_lbl = customtkinter.CTkButton(drinks_frames_list[1][2], text="Coffee", 
                                             command = lambda: description_page(coffee_lbl, coffee),
                                             fg_color='transparent', hover_color="#333333",
                                             font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        coffee_lbl.grid(row=1, column=0, sticky='new', pady=(5,0), padx=10)

        coffee_price = customtkinter.CTkButton(drinks_frames_list[1][2], text="Price: $4.50", 
                                               command = lambda: description_page(coffee_lbl, coffee),
                                               fg_color='transparent', hover_color="#333333",
                                               font=customtkinter.CTkFont(family='Calibri', weight='bold', size=25))
        coffee_price.grid(row=2, column=0, sticky='new', pady=(0,10), padx=10)

        # Add to Order Button for Coffee Drink
        coffee_atobtn = customtkinter.CTkButton(drinks_frames_list[1][2], text = "+", 
                                                width=40, command = lambda: add(coffee_lbl),
                                                font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        coffee_atobtn.grid(row=0, column=0, sticky='ne', pady=25, padx=25)

        # Remove Button for Coffee Drink
        coffee_remove = customtkinter.CTkButton(drinks_frames_list[1][2], text = "-", bg_color="#9b4e02",
                                                width=40, command = lambda: remove(coffee_lbl),
                                                fg_color='#e5383b', hover_color="#a4161a",
                                                font=customtkinter.CTkFont(family='Calibri', size=20, weight='bold'))
        coffee_remove.grid(row=0, column=0, sticky='ne', pady=25, padx=75)
        # endregion
# endregion


# ------------------------ Main Window Configurations ------------------------ #
window=customtkinter.CTk()                          # Creates a window 
window.title("Austin's Restaurant Ordering App")    # Title of the window

# Sets the size of the window to fill screen 
# The values in the string wil find the screen width and height and tuck it into the top left corner of the screen
window.geometry("1536x800-7+0")
window.resizable(False, False)
# 1536x945-7+0  (Old Dimensions)


# ---------------------------------- Frames ---------------------------------- #
# Top Navigation Bar
TopNavBarFrame = TopNavBar(window)
TopNavBarFrame.grid(column=0, row=0, sticky='nwes', columnspan=2)
TopNavBarFrame.configure(corner_radius=0, height=75, fg_color="#DEE2E6")

# Main Frame to store different frames (Mains, Appetisers, Desserts and Drinks)
main_windowframe = customtkinter.CTkFrame(window, height=700, corner_radius=0)
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
    MainsSelectionFrame.configure(height=700, corner_radius=0)      # Configurations to the frame 

# Function to show the appetisers selection
def appetisers_page():
    AppetiserFrame = AppetiserSelection(main_windowframe)           # Calls the Class as the frame 
    AppetiserFrame.grid(column=0, row=0, sticky='news')             # Grids the frame
    AppetiserFrame.configure(height=700, corner_radius=0)           # Configurations to the frame

# Function to show the desserts selection
def desserts_page():
    DessertFrame = DessertSelection(main_windowframe)             # Calls the Class as the frame
    DessertFrame.grid(column=0, row=0, sticky='news')             # Grids the frame
    DessertFrame.configure(height=700, corner_radius=0)           # Configurations to the frame

# Function to show the drinks selection
def drinks_page():
    global DrinksFrame
    DrinksFrame = DrinkSelection(main_windowframe)                # Calls the Class as the frame
    DrinksFrame.grid(column=0, row=0, sticky='news')              # Grids the frame
    DrinksFrame.configure(height=700, corner_radius=0)            # Configurations to the frame 
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
order_frame.grid_columnconfigure(0, weight = 1)
#order_frame.grid_rowconfigure(1, weight = 1)

# region | Frame for Orders
order_list_frame = customtkinter.CTkScrollableFrame(order_frame, corner_radius=10, height=550, width=200)
order_list_frame.grid(row=1, column=0, pady=(10,0), padx=20, sticky='news', ipady=10, ipadx=10)
# endregion

# region | Title for Order Section
order_lbl = customtkinter.CTkLabel(order_frame, text = "Order:", text_color="#DEE2E6",
                                   font=customtkinter.CTkFont(family="Calibri", size=50, weight='bold', underline=True))
order_lbl.grid(row=0, column=0, sticky='nws', pady=5, padx=20)
# endregion

# region | Label for Order ID
order_id_lbl = customtkinter.CTkLabel(order_frame, text = "Order ID: " + order_id(), text_color="#DEE2E6",
                                   font=customtkinter.CTkFont(family="Calibri", size=25, weight='bold', underline=True))
order_id_lbl.grid(row=0, column=0, sticky='es', pady=10, padx=20)
# endregion

# region | Total Price Label
totalorder_lbl = customtkinter.CTkLabel(order_frame, text = "Total Price: $0", text_color="#DEE2E6", 
                                        font=customtkinter.CTkFont(family="Calibri", size=30))
totalorder_lbl.grid(row=2, column=0, sticky='nw', pady=5, padx=(20,0))
# endregion

# region | Button to place order
place_order_btn = customtkinter.CTkButton(order_frame, text="Place Order", text_color="#DEE2E6", fg_color="#333333",
                                          command = place_order,
                                          font=customtkinter.CTkFont(family="Calibri", size=50))
place_order_btn.grid(row=3, column=0, sticky="news", pady=5, padx=20)
# endregion

window.mainloop()