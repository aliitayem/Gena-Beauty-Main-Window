from datetime import date, time, datetime
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import os
import tk as tk

cart = Tk()
cart.title("Gena Beauty Supply | Cart Mode")
cart.geometry("1500x1000")

# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
          background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(cart)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview())

# Define Our Treeview Columns
my_tree['columns'] = ('Name', 'Price')

# Format Treeview Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=800)
my_tree.column("Price", anchor=W, width=50)

# Create Treeview Headings
my_tree.heading("#0", text="")
my_tree.heading("Name", text="")
my_tree.heading("Price", text="")


# Display Treeview
my_tree.pack()

my_tree.configure()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="inventory",
    passwd="root"
)

mycursor = mydb.cursor()


# Create the widgets
enter_barcode_label = Label(cart, text="Enter Barcode:")
enter_barcode_entry = Entry(cart)
add_to_cart_btn = Button(cart, text="Add to Cart")

def query_database():

    for record in my_tree.get_children():
        my_tree.delete(record)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="inventory"
    )

    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM carts")
    records = mycursor.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[4], record[1]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[4], record[1]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    db.commit()
    db.close()


# Define the action when the button is clicked
def add_to_cart():
    # Get the barcode
    barcode = enter_barcode_entry.get()

    # Create a cursor to interact with the database
    mycursor = mydb.cursor()

    # Select the data from the products table
    sql = "SELECT * FROM products WHERE barcode = %s"
    val = (barcode,)
    mycursor.execute(sql, val)

    # Get the data
    product = mycursor.fetchone()

    # Insert the product into the carts table
    sql = "INSERT INTO carts (name, price, quantity, barcode) VALUES (%s, %s, %s, %s)"
    val = (product[2], product[7], product[9], product[1])
    mycursor.execute(sql, val)
    mydb.commit()

    # Update Tree View
    my_tree.delete(*my_tree.get_children())
    # Query Database And Refresh Treeview
    query_database()


# Configure the widgets
enter_barcode_label.pack()
enter_barcode_entry.pack()
add_to_cart_btn.pack()
reset_button = Button(cart, text="Reset", command=query_database)
reset_button.pack()

# Call the function when the button is clicked
add_to_cart_btn.configure(command=add_to_cart)

query_database()

cart.mainloop()