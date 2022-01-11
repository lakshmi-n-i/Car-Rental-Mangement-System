#WE HAVE TO ADD DESCRIPTION FOR EACH CAR
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
import mysql.connector
connection=mysql.connector.connect(host='localhost',user='root',password='munich24',database='computerproject')
cursor=connection.cursor()
def screen1():
    global root
    root=Tk()
    root.title("Car Rental Management System")
    root.geometry("1200x800")
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to Bon Voyage Rentals!", bg='black', fg='white', font=('Courier',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    btn1=Button(root,text="Rent a car",command=rent,bg="black",fg='white',font=('arial',15,'bold'))
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    btn2=Button(root,text="Return a car",command=returns,bg="black",fg='white',font=('arial',15,'bold'))
    btn2.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    
    root.mainloop()


def rent():
    #root.destroy()
    global screen2
    screen2=Tk()
    screen2.geometry("800x800")
    screen2.title("Car Rentals")
    lb2=Label(screen2,text="Please fill in your specifications",bg="black",fg="white",font=("Segoe Print",20,'bold'))
    lb2.place(relx=0.35,rely=0.01)
    lb3=Label(screen2,text="Seater capacty",bg="black", fg="white",font=("Arial",15,'bold'))
    lb3.place(relx=0.03, rely=0.1)
    global var1
    global var2
    global var3
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    var11=IntVar()
    cb1= Checkbutton(screen2,text="5-seater", variable=var1,font=('Calibri',14,'bold'))
    cb2= Checkbutton(screen2,text="7-seater", variable=var2,font=('Calibri',14,'bold'))
    cb3= Checkbutton(screen2,text="8-seater", variable=var3,font=('Calibri',14,'bold'))
    '''
    cb1.deselect()
    cb2.deselect()
    cb3.deselect()
    '''
    cb1.place(relx=0.03, rely=0.14)
    cb2.place(relx=0.03, rely=0.18)
    cb3.place(relx=0.03, rely=0.22)
    lb4=Label(screen2,text="Pick-up Location",bg="black", fg="white",font=("Arial",15,'bold'))
    lb4.place(relx=0.03, rely=0.3)
    cb4= Checkbutton(screen2,text="Bellandur", variable=var4,font=('Calibri',14,'bold'))
    cb5= Checkbutton(screen2,text="Shivajinagar", variable=var5,font=('Calibri',14,'bold'))
    cb6= Checkbutton(screen2,text="Koramangala", variable=var6,font=('Calibri',14,'bold'))
    cb7= Checkbutton(screen2,text="Banashankari", variable=var7,font=('Calibri',14,'bold'))
    cb8= Checkbutton(screen2,text="Indiranagar", variable=var8,font=('Calibri',14,'bold'))
    cb9= Checkbutton(screen2,text="Hsr Layout", variable=var9,font=('Calibri',14,'bold'))
    cb4.place(relx=0.03, rely=0.34)
    cb5.place(relx=0.03, rely=0.38)
    cb6.place(relx=0.03, rely=0.42)
    cb7.place(relx=0.03, rely=0.46)
    cb8.place(relx=0.03, rely=0.5)
    cb9.place(relx=0.03, rely=0.54)
    lb5=Label(screen2,text="Driver Needed?",bg="black", fg="white",font=("Arial",15,'bold'))
    lb5.place(relx=0.03, rely=0.62)
    cb10= Checkbutton(screen2,text="Yes", variable=var10,font=('Calibri',14,'bold'))
    cb11= Checkbutton(screen2,text="No", variable=var11,font=('Calibri',14,'bold'))
    cb10.place(relx=0.03, rely=0.66)
    cb11.place(relx=0.03, rely=0.7)
    btn3= Button(screen2, text= "OK",font=('Calibri',15)).place(relx=0.9,rely=0.9)
    screen2.mainloop()

def returns():
    #root.destroy()
    screen3=Tk()
    screen3.geometry("1200x800")
    screen3.title("Car Returns")
    lbb=Label(screen3,text="Return a car",bg="black",fg="white",font=("arial",25,'bold')).place(relx=0.44, rely=0.1)

    def show():
        mylabel=Label(screen3,text= "You returned a "+cars.get()+" at "+area.get() ,font=('Calibri',20,'bold'),fg="white",bg="black").place(relx=0.32,rely=0.7)
       
    cars=StringVar()
    cars.set("WagonR")
    area=StringVar()

    drop=OptionMenu(screen3,cars,"WagonR","Honda City","Swift Dzire","Innova","Xylo","Creta","i20","Jeep Compass","Corolla Altis","Verna","Astar","Duster","i10","Fortuner").place(relx=0.28,rely=0.3,relwidth=0.05 ,relheight=0.05)
    lb15=Label(screen3,text="Choose your car",font=("Arial",15,'bold')).place(relx=0.38,rely=0.30)
    drop1=OptionMenu(screen3,area,"Bellandur","Shivajinagar","Koramangala","Indiranagar","HSR Layout","Banashankari").place(relx=0.28,rely=0.5,relwidth=0.05,relheight=0.05)
    lb16=Label(screen3,text="Choose the area you wish to return at",font=("Arial",15,'bold')).place(relx=0.38,rely=0.50)
    mybutton=Button(screen3,text="Show Selection",command=show).place(relx=0.7,rely=0.6)

    e=Entry(screen3,width=30).place(relx=0.30,rely=0.91)
    lb17=Label(screen3,text="Help us improve!",font=('Arial',14,'bold')).place(relx=0.15,rely=0.9)
    





    screen3.mainloop()




screen1()