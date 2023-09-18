from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
import tkinter.font as tkFont
import mysql.connector
import os

import tk


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

    mycursor.execute("SELECT * FROM products")
    records = mycursor.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                               record[7], record[8], record[9], record[10]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                               record[7], record[8], record[9], record[10]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    db.commit()
    db.close()


def primary_color():
    primary_color = colorchooser.askcolor()[1]

    if primary_color:
        my_tree.tag_configure('evenrow', background=primary_color)


def secondary_color():
    secondary_color = colorchooser.askcolor()[1]

    if secondary_color:
        my_tree.tag_configure('oddrow', background=secondary_color)


def highlight_color():
    highlight_color = colorchooser.askcolor()[1]

    if highlight_color:
        style.map('Treeview',
                  background=[('selected', highlight_color)])


def search_barcode(event=None):
    barcode = barcode_entry.get()

    for record in my_tree.get_children():
        my_tree.delete(record)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="inventory"
    )

    mycursor = db.cursor()

    sql = "SELECT * FROM products WHERE barcode=%s"

    mycursor.execute(sql, (barcode,))
    records = mycursor.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                               record[7], record[8], record[9], record[10]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                               record[7], record[8], record[9], record[10]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    db.commit()
    db.close()

    barcode_entry.delete(0, END)
    name_entry.delete(0, END)
    brand_entry.delete(0, END)
    category_entry.delete(0, END)
    location_entry.delete(0, END)
    size_entry.delete(0, END)
    price_entry.delete(0, END)
    cost_entry.delete(0, END)
    quantity_entry.delete(0, END)
    color_entry.delete(0, END)


# Define the function that binds the enter key to the search function
def toggle_bind(event=None):
    if toggle_var.get() == 1:
        root.bind("<Return>", search_barcode)
    else:
        root.unbind("<Return>")


def search_name():
    search_name = name_entry.get()

    for record in my_tree.get_children():
        my_tree.delete(record)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="inventory"
    )

    mycursor = db.cursor()

    sql = "SELECT * FROM products WHERE name like %s"

    mycursor.execute(sql, (search_name,))
    records = mycursor.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                               record[7], record[8], record[9], record[10]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                               record[7], record[8], record[9], record[10]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    db.commit()
    db.close()

    barcode_entry.delete(0, END)
    name_entry.delete(0, END)
    brand_entry.delete(0, END)
    category_entry.delete(0, END)
    location_entry.delete(0, END)
    size_entry.delete(0, END)
    price_entry.delete(0, END)
    cost_entry.delete(0, END)
    quantity_entry.delete(0, END)
    color_entry.delete(0, END)


def search_brand():
    search_brand = brand_entry.get()

    for record in my_tree.get_children():
        my_tree.delete(record)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="inventory"
    )

    mycursor = db.cursor()

    sql = "SELECT * FROM products WHERE brand like %s"

    mycursor.execute(sql, (search_brand,))
    records = mycursor.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                               record[7], record[8], record[9], record[10]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                               record[7], record[8], record[9], record[10]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    db.commit()
    db.close()

    barcode_entry.delete(0, END)
    name_entry.delete(0, END)
    brand_entry.delete(0, END)
    category_entry.delete(0, END)
    location_entry.delete(0, END)
    size_entry.delete(0, END)
    price_entry.delete(0, END)
    cost_entry.delete(0, END)
    quantity_entry.delete(0, END)
    color_entry.delete(0, END)


def search_category():
    search_category = category_entry.get()

    for record in my_tree.get_children():
        my_tree.delete(record)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="inventory"
    )

    mycursor = db.cursor()

    sql_command = "SELECT * FROM products WHERE category like %s"

    mycursor.execute(sql_command, (search_category,))
    records = mycursor.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                               record[7], record[8], record[9], record[10]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                               record[7], record[8], record[9], record[10]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    db.commit()
    db.close()

    barcode_entry.delete(0, END)
    name_entry.delete(0, END)
    brand_entry.delete(0, END)
    category_entry.delete(0, END)
    location_entry.delete(0, END)
    size_entry.delete(0, END)
    price_entry.delete(0, END)
    cost_entry.delete(0, END)
    quantity_entry.delete(0, END)
    color_entry.delete(0, END)


root = Tk()
root.title('Gena Beauty Supply')
root.geometry("1500x1000")

my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Change Color", menu=options_menu)
options_menu.add_command(label="Primary Color", command=primary_color)
options_menu.add_command(label="Secondary Color", command=secondary_color)
options_menu.add_command(label="Highlight Color", command=highlight_color)

search_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search By", menu=search_menu)

search_menu.add_command(label="Barcode", command=search_barcode)
search_menu.add_command(label="Name", command=search_name)
search_menu.add_command(label="Brand", command=search_brand)
search_menu.add_command(label="Category", command=search_category)
search_menu.add_separator()
search_menu.add_command(label="Reset", command=query_database)

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
tree_frame = Frame(root)
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
    "ID", "Barcode", "Name", "Brand", "Category", "Location", "Size", "Price", "Cost", "Quantity", "Color")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=CENTER, width=50)
my_tree.column("Barcode", anchor=CENTER, width=140)
my_tree.column("Name", anchor=CENTER, width=280)
my_tree.column("Brand", anchor=CENTER, width=110)
my_tree.column("Category", anchor=CENTER, width=100)
my_tree.column("Location", anchor=CENTER, width=120)
my_tree.column("Size", anchor=CENTER, width=80)
my_tree.column("Price", anchor=CENTER, width=80)
my_tree.column("Cost", anchor=CENTER, width=80)
my_tree.column("Quantity", anchor=CENTER, width=60)
my_tree.column("Color", anchor=CENTER, width=120)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Barcode", text="Barcode", anchor=CENTER)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("Brand", text="Brand", anchor=CENTER)
my_tree.heading("Category", text="Category", anchor=CENTER)
my_tree.heading("Location", text="Location", anchor=CENTER)
my_tree.heading("Size", text="Size", anchor=CENTER)
my_tree.heading("Price", text="Price", anchor=CENTER)
my_tree.heading("Cost", text="Cost", anchor=CENTER)
my_tree.heading("Quantity", text="Quantity", anchor=CENTER)
my_tree.heading("Color", text="Color", anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=10, padx=10, pady=10)
global id_entry
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=11, padx=10, pady=10)

barcode_label = Label(data_frame, text="Barcode")
barcode_label.grid(row=0, column=0, padx=10, pady=10)
global barcode_entry
barcode_entry = Entry(data_frame)
barcode_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = Label(data_frame, text="Name")
name_label.grid(row=0, column=2, padx=10, pady=10)
global name_entry
name_entry = Entry(data_frame)
name_entry.grid(row=0, column=3, padx=10, pady=10)

brand_label = Label(data_frame, text="Brand")
brand_label.grid(row=1, column=0, padx=10, pady=10)
global brand_entry
brand_entry = Entry(data_frame)
brand_entry.grid(row=1, column=1, padx=10, pady=10)

category_label = Label(data_frame, text="Category")
category_label.grid(row=1, column=2, padx=10, pady=10)
global category_entry
category_entry = Entry(data_frame)
category_entry.grid(row=1, column=3, padx=10, pady=10)

location_label = Label(data_frame, text="Location")
location_label.grid(row=1, column=4, padx=10, pady=10)
global location_entry
location_entry = Entry(data_frame)
location_entry.grid(row=1, column=5, padx=10, pady=10)

size_label = Label(data_frame, text="Size")
size_label.grid(row=1, column=6, padx=10, pady=10)
global size_entry
size_entry = Entry(data_frame)
size_entry.grid(row=1, column=7, padx=10, pady=10)

price_label = Label(data_frame, text="Price")
price_label.grid(row=0, column=4, padx=10, pady=10)
global price_entry
price_entry = Entry(data_frame)
price_entry.grid(row=0, column=5, padx=10, pady=10)

cost_label = Label(data_frame, text="Cost")
cost_label.grid(row=1, column=8, padx=10, pady=10)
global cost_entry
cost_entry = Entry(data_frame)
cost_entry.grid(row=1, column=9, padx=10, pady=10)

quantity_label = Label(data_frame, text="Quantity")
quantity_label.grid(row=0, column=6, padx=10, pady=10)
global quantity_entry
quantity_entry = Entry(data_frame)
quantity_entry.grid(row=0, column=7, padx=10, pady=10)

color_label = Label(data_frame, text="Color")
color_label.grid(row=0, column=8, padx=10, pady=10)
global color_entry
color_entry = Entry(data_frame)
color_entry.grid(row=0, column=9, padx=10, pady=10)

def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)


def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="inventory"
    )

    mycursor = db.cursor()

    mycursor.execute("DELETE FROM products WHERE id=" + id_entry.get())

    db.commit()
    db.close()

    clear_entries()

def clear_entries():
    id_entry.delete(0, END)
    barcode_entry.delete(0, END)
    name_entry.delete(0, END)
    brand_entry.delete(0, END)
    category_entry.delete(0, END)
    location_entry.delete(0, END)
    size_entry.delete(0, END)
    price_entry.delete(0, END)
    cost_entry.delete(0, END)
    quantity_entry.delete(0, END)
    color_entry.delete(0, END)


def select_record(e):
    id_entry.delete(0, END)
    barcode_entry.delete(0, END)
    name_entry.delete(0, END)
    brand_entry.delete(0, END)
    category_entry.delete(0, END)
    location_entry.delete(0, END)
    size_entry.delete(0, END)
    price_entry.delete(0, END)
    cost_entry.delete(0, END)
    quantity_entry.delete(0, END)
    color_entry.delete(0, END)

    # Grab Record Number
    selected = my_tree.focus()
    # Grab Record Values
    values = my_tree.item(selected, 'values')

    # Output To Entry Boxes
    id_entry.insert(0, values[0])
    barcode_entry.insert(0, values[1])
    name_entry.insert(0, values[2])
    brand_entry.insert(0, values[3])
    category_entry.insert(0, values[4])
    location_entry.insert(0, values[5])
    size_entry.insert(0, values[6])
    price_entry.insert(0, values[7])
    cost_entry.insert(0, values[8])
    quantity_entry.insert(0, values[9])
    color_entry.insert(0, values[10])


def update_record():
    # Update Treeview
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(
        id_entry.get(), barcode_entry.get(), name_entry.get(), brand_entry.get(), category_entry.get(),
        location_entry.get(), size_entry.get(), price_entry.get(), cost_entry.get(), quantity_entry.get(), color_entry.get(),))

    # Update Database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="inventory"
    )

    mycursor = db.cursor()

    sql_command = """UPDATE products SET barcode=%s, name=%s, brand=%s, category=%s, location=%s, size=%s, price=%s, cost=%s, quantity=%s, color=%s WHERE id = %s"""

    barcode = barcode_entry.get()
    name = name_entry.get()
    brand = brand_entry.get()
    category = category_entry.get()
    location = location_entry.get()
    size = size_entry.get()
    price = price_entry.get()
    cost = cost_entry.get()
    quantity = quantity_entry.get()
    color = color_entry.get()

    id = id_entry.get()

    inputs = (barcode, name, brand, category, location, size, price, cost, quantity, color, id)

    mycursor.execute(sql_command, inputs)

    db.commit()
    db.close()

    id_entry.delete(0, END)
    barcode_entry.delete(0, END)
    name_entry.delete(0, END)
    brand_entry.delete(0, END)
    category_entry.delete(0, END)
    location_entry.delete(0, END)
    size_entry.delete(0, END)
    price_entry.delete(0, END)
    cost_entry.delete(0, END)
    quantity_entry.delete(0, END)
    color_entry.delete(0, END)


def add_record():
    # Update Treeview
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(
        barcode_entry.get(), name_entry.get(), brand_entry.get(), category_entry.get(),
        location_entry.get(), size_entry.get(), price_entry.get(), cost_entry.get(), quantity_entry.get(), color_entry.get(),))

    # Update Database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="inventory"
    )

    mycursor = db.cursor()

    barcode = barcode_entry.get()
    name = name_entry.get()
    brand = brand_entry.get()
    category = category_entry.get()
    location = location_entry.get()
    size = size_entry.get()
    price = price_entry.get()
    cost = cost_entry.get()
    quantity = quantity_entry.get()
    color = color_entry.get()

    insert_query = "INSERT INTO products (barcode, name, brand, category, location, size, price, cost, quantity, color) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    vals = (barcode, name, brand, category, location, size, price, cost, quantity, color)

    mycursor.execute(insert_query, vals)

    db.commit()
    db.close()

    id_entry.delete(0, END)
    barcode_entry.delete(0, END)
    name_entry.delete(0, END)
    brand_entry.delete(0, END)
    category_entry.delete(0, END)
    location_entry.delete(0, END)
    size_entry.delete(0, END)
    price_entry.delete(0, END)
    cost_entry.delete(0, END)
    quantity_entry.delete(0, END)
    color_entry.delete(0, END)

    # Update Tree View
    my_tree.delete(*my_tree.get_children())
    # Query Database And Refresh Treeview
    query_database()


# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Delete Record", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

reset_button = Button(button_frame, text="Reset", command=query_database)
reset_button.grid(row=0, column=8, padx=10, pady=10)

# Create the toggle button
toggle_var = IntVar()
toggle_button = Checkbutton(button_frame, text="Search Mode", variable=toggle_var, command=toggle_bind)
toggle_button.grid(row=0, column=10, padx=10, pady=10)

my_tree.bind("<ButtonRelease-1>", select_record)

query_database()

root.mainloop()
