from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
import tkinter.font as tkFont
import tkinter as tk
import mysql.connector
import os


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="inventory"
)

mycursor = db.cursor()

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
                               record[0], record[1], record[2], record[3], record[4]))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4]))
        count += 1
    db.commit()
    db.close()


def add_To_Cart(self):

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="inventory"
    )

    mycursor = db.cursor()

    barcode = barcode_entry.get()

    mycursor.execute("SELECT price, barcode, name FROM inventory.products WHERE barcode = %s", (barcode,))
    result = mycursor.fetchone()

    if result:
        price, barcode, name = result

        mycursor.execute("INSERT INTO inventory.carts (price, quantity, barcode, name) VALUES (%s, 1, %s, %s)  ON DUPLICATE KEY UPDATE quantity = quantity + 1", (price, barcode, name))
        print("Item Added To Cart Successfully")
    else:
        print("Item Not Found")

    db.commit()
    db.close()

    barcode_entry.delete(0, END)

    query_database()


def complete_Order():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="inventory"
    )

    mycursor = db.cursor()

    mycursor.execute("SELECT barcode, quantity FROM inventory.carts")
    records = mycursor.fetchall()


    for barcode, quantity in records:
        mycursor.execute("INSERT INTO inventory.report (barcode, quantity) VALUES (%s, %s) ON DUPLICATE KEY UPDATE quantity = report.quantity + %s", (barcode, quantity, quantity))

    mycursor.execute("DELETE FROM inventory.carts")

    db.commit()
    db.close()

    query_database()


window = tk.Tk()
window.title("Cart")

# Create a Treeview Frame
tree_frame = Frame(window)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = (
    "ID", "Barcode", "Name", "Price", "Quantity")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=CENTER, width=50)
my_tree.column("Price", anchor=CENTER, width=140)
my_tree.column("Quantity", anchor=CENTER, width=280)
my_tree.column("Barcode", anchor=CENTER, width=80)
my_tree.column("Name", anchor=CENTER, width=60)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Price", text="Barcode", anchor=CENTER)
my_tree.heading("Quantity", text="Name", anchor=CENTER)
my_tree.heading("Barcode", text="Price", anchor=CENTER)
my_tree.heading("Name", text="Quantity", anchor=CENTER)

barcode_entry = Entry(window)
barcode_entry.pack()

complete_order_button = tk.Button(window, text="Complete Order", command=complete_Order)
complete_order_button.pack()

add_to_cart_button = tk.Button(window, text="Add To Cart", command=add_To_Cart)
add_to_cart_button.pack()

window.bind("<Return>", add_To_Cart)

query_database()

window.mainloop()
