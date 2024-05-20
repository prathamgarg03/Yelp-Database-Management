import pyodbc
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import a

def make_friend(logged_in_user_id, selected_user_id):
    connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=cypress.csil.sfu.ca;Database=pga47354;uid=s_pga47;pwd=4P2GhAqj2n3bLEF2')
    cursor = connection.cursor()

    select_query = "SELECT * FROM friendship WHERE (user_id = ? AND friend = ?) OR (user_id = ? AND friend = ?)"
    params = (logged_in_user_id, selected_user_id, selected_user_id, logged_in_user_id)
    cursor.execute(select_query, params)
    existing_friendship = cursor.fetchone()

    if existing_friendship:
        messagebox.showinfo("ahh","Friendship already exists!")
    else:
        insert_query = "INSERT INTO friendship (user_id, friend) VALUES (?, ?), (?, ?)"
        params = (logged_in_user_id, selected_user_id, selected_user_id, logged_in_user_id)
        cursor.execute(insert_query, params)
        connection.commit()

        messagebox.showinfo("success",f"Friendship created between User ID {logged_in_user_id} and User ID {selected_user_id}")
    cursor.close()
    connection.close()


def on_user_select(event):
    item = tree.selection()[0]
    user_id = tree.item(item, 'values')[0]
    print(f"Selected User ID: {user_id}")
    print(a.uid)
    make_friend(a.uid, user_id)
    
def search_business():
    result_text.delete('1.0', END)
    for child in tree.get_children():
        tree.delete(child)
    us = name.get()
    rvw = review.get()
    strs = stars.get()


    connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=cypress.csil.sfu.ca;Database=pga47354;uid=s_pga47;pwd=4P2GhAqj2n3bLEF2')
    cursor = connection.cursor()

    filters = []

    if us:
        filters.append(f"LOWER(name) LIKE '%{us}%'")

    if rvw:
        filters.append(f"review_count >= '{rvw}'")

    if strs:
        filters.append(f"LOWER(average_stars) = '{strs}'")

    where_clause = " AND ".join(filters)

    base_query = "SELECT user_id, name, review_count, useful, funny, cool, average_stars, yelping_since FROM user_yelp"

    if where_clause:
        full_query = f"{base_query} WHERE {where_clause}"
    else:
        full_query = f"{base_query}"

    print(full_query)
    cursor.execute(full_query)
    rows = cursor.fetchall()

    if not rows:
        messagebox.showerror("Error", "No Record Found!!")
    else:
        for row in rows:
            # Assuming 'row' is a tuple fetched from the database
            corrected_row = row[:2] + tuple(str(item) for item in row[2:-2]) + row[-2:]
            tree.insert("", END, values=corrected_row)

    cursor.close()
    connection.close()

root = Tk()
root.geometry('700x700+0+0')
root.title("Business ID Search")

name_label = Label(root, text="Enter User's Name:")
name_label.pack()
name = Entry(root)
name.pack()

review_label = Label(root, text="Enter minimum Review Count:")
review_label.pack()
review = Entry(root)
review.pack()


stars_label = Label(root, text="Enter minimum average stars:")
stars_label.pack()
stars = Entry(root)
stars.pack()





search_button = Button(root, text="Search", command=search_business)
search_button.pack()

result_text = Text(root, height=20, width=50)
result_text.pack()


headers = ['User ID', 'Name', 'Review Count', 'Useful', 'Funny', 'Cool', 'Average Stars', 'Date']
tree = ttk.Treeview(result_text, columns=headers, show="headings")
for col in headers:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(fill=BOTH, expand=1)
tree.bind("<Double-1>", on_user_select)
root.mainloop()

