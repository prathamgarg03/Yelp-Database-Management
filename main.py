from tkinter import *
from tkinter import messagebox
import pyodbc

class a:
    uid = ''

def login():
    if usernameEntry.get() == "":
        messagebox.showerror('Error', 'Field cannot be empty')
    connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=cypress.csil.sfu.ca;Database=pga47354;uid=s_pga47;pwd=4P2GhAqj2n3bLEF2')
    cursor = connection.cursor()
    sql_query = f"SELECT user_id from user_yelp where user_id = '{usernameEntry.get()}'"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    if not rows:
        messagebox.showerror('Error', 'Incorrect User Id')
    else:
        a.uid = usernameEntry.get()
        messagebox.showinfo('Success', 'Login Successful')
        window.destroy()
        import home
        
        
    cursor.close()
    connection.close()



window = Tk()
window.geometry('500x500+0+0')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (500 / 2)
y_coordinate = (screen_height / 2) - (500 / 2)
window.geometry(f'{500}x{500}+{int(x_coordinate)}+{int(y_coordinate)}')

loginFrame = Frame(window)
loginFrame.pack(pady=20)

usernameLabel = Label(loginFrame, text="UserID: ", font=('times new roman', 15, 'bold'))
usernameLabel.grid(row=0, column=0)

usernameEntry = Entry(loginFrame)
usernameEntry.grid(row=0, column=1)

loginButton = Button(loginFrame, text='Login', font=('times new roman', 10, 'bold'), cursor='hand2', command=login)
loginButton.grid(row=2, columnspan=2)



window.mainloop()
