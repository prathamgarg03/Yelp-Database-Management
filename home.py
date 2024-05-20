from tkinter import *

def bSearch():
    root.destroy()
    import bSearch
def uSearch():
    root.destroy()
    import uSearch
root = Tk()
root.geometry('500x500+0+0')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (500 / 2))
y_coordinate = int((screen_height / 2) - (500 / 2))
root.geometry(f'500x500+{x_coordinate}+{y_coordinate}')


buttonFrame = Frame(root)
buttonFrame.pack(expand=True)

usernameLabel = Label(buttonFrame, text="Welcome!! ", font=('times new roman', 15, 'bold'))
usernameLabel.pack()

searchBusiness = Button(buttonFrame, text='Search Business', font=('times new roman', 10, 'bold'), cursor='hand2', command=bSearch)
searchBusiness.pack()

searchUsers = Button(buttonFrame, text='Search Users', font=('times new roman', 10, 'bold'), cursor='hand2', command=uSearch)
searchUsers.pack()

root.mainloop()
