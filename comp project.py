from tkinter import*
from tkinter import ttk
import mysql.connector

connection=mysql.connector.connect(host='localhost',user='root',password='munich24',database='computerproject')
cursor=connection.cursor()


root=Tk()
root.title("Car Rental Management System")
root.geometry("600x500")
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to bon voyage rentals", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

def clicked():
    lb2=Label(root,text="select car").grid(row=5,column=2)
    lb3=Label(root,text="return a car").grid(row=7,column=2)


btn1=Button(root,text="rent a car",command=clicked,bg="black",fg='white',font=('arial',20,'bold'))
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
btn2=Button(root,text="return a car",command=clicked,bg="black",fg='white',font=('arial',20,'bold'))
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)



root.mainloop()

