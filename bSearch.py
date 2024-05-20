import datetime
import pyodbc
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import a
import uuid

def make_review(logged_in_user_id, business_id, stars):
    connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=cypress.csil.sfu.ca;Database=pga47354;uid=s_pga47;pwd=4P2GhAqj2n3bLEF2')
    cursor = connection.cursor()

    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    review_id = str(uuid.uuid4())[:22]
    insert_review_query = "INSERT INTO Review (review_id, user_id, business_id, stars, date) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(insert_review_query, review_id, logged_in_user_id, business_id, stars, current_date)

    connection.commit()

    cursor.close()
    connection.close()

def on_user_select(event):
    item = tree.selection()[0]
    business_id = tree.item(item, 'values')[0]
    print(f"Selected Business ID: {business_id}")

    

    make_review(a.uid, business_id, stars.get())
    messagebox.showinfo("Success", "Review recorded successfully!")

    
def search_business():
    result_text.delete('1.0', END)
    for child in tree.get_children():
        tree.delete(child)
    bus = name.get()
    strs = stars.get()
    cty = city.get()
    sort = var.get()
    ordr = order.get()
    if sort=="sort" or ordr=="order":
        messagebox.showerror('Error', 'Sort and Order fields cannot be empty')
    connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=cypress.csil.sfu.ca;Database=pga47354;uid=s_pga47;pwd=4P2GhAqj2n3bLEF2')
    cursor = connection.cursor()

    filters = []

    if bus:
        filters.append(f"LOWER(name) LIKE '%{bus}%'")

    if strs:
        filters.append(f"stars >= '{strs}'")

    if cty:
        filters.append(f"LOWER(city) = '{cty}'")

    where_clause = " AND ".join(filters)

    base_query = "SELECT business_id, name, address, city, stars FROM business"
    
    if where_clause:
        full_query = f"{base_query} WHERE {where_clause} ORDER BY '{sort}' {ordr}"
    else:
        full_query = f"{base_query} ORDER BY '{sort}' {ordr}"

    print(full_query)
    cursor.execute(full_query)
    rows = cursor.fetchall()

    if not rows:
        messagebox.showerror("Error", "No Record Found!!")
    else:
        for row in rows:
            corrected_row = row[:2] + (' '.join(row[2:-2]),) + row[-2:]
            tree.insert("", END, values=corrected_row)

    cursor.close()
    connection.close()

root = Tk()
root.geometry('700x700+0+0')
root.title("Business ID Search")

name_label = Label(root, text="Enter Business Name:")
name_label.pack()
name = Entry(root)
name.pack()

stars_label = Label(root, text="Enter Minimum No. Of Stars:")
stars_label.pack()
stars = Entry(root)
stars.pack()


city_label = Label(root, text="Enter City:")
city_label.pack()
city = Entry(root)
city.pack()


var = StringVar(value="sort")
R0 = Radiobutton(root, text="Sort By:", variable=var, value="sort")
R0.configure(state = DISABLED)
R0.pack( anchor = W )
R1 = Radiobutton(root, text="Name", variable=var, value="name")
R1.pack( anchor = W )
R2 = Radiobutton(root, text="City", variable=var, value="city")
R2.pack( anchor = W )
R3 = Radiobutton(root, text="Stars", variable=var, value="stars")
R3.pack( anchor = W)

order = StringVar(value="order")
R4 = Radiobutton(root, text="Order:", variable=order, value="order")
R4.configure(state = DISABLED)
R4.pack( anchor = W )
R5 = Radiobutton(root, text="Ascending", variable=order, value="asc")
R5.pack( anchor = W )
R6 = Radiobutton(root, text="Descending", variable=order, value="desc")
R6.pack( anchor = W )


search_button = Button(root, text="Search", command=search_business)
search_button.pack()

result_text = Text(root, height=20, width=50)
result_text.pack()


headers = ['Business ID', 'Name', 'Address', 'City', 'Stars']
tree = ttk.Treeview(result_text, columns=headers, show="headings")
for col in headers:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(fill=BOTH, expand=1)
tree.bind("<Double-1>", on_user_select)
root.mainloop()

