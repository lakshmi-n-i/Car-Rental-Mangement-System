#with selection based only on one filter at a time
from tkinter import*
from tkinter import ttk
import mysql.connector
connection=mysql.connector.connect(host='localhost',user='root',password='munich24',database='computerproject')
cursor=connection.cursor()
def screen1():
    global root
    root=Tk()
    root.title("Car Rental Management System")
    root.geometry("1200x800")
    bg=PhotoImage(file=r"C:\Users\91855\Desktop\Carrental\image4.png")
    my_label=Label(root,image=bg)
    my_label.pack()
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to Bon Voyage Rentals!", bg='black', fg='white', font=('Courier',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    btn1=Button(root,text="Rent a car",command=filters,bg="black",fg='white',font=('arial',15,'bold')).place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    btn2=Button(root,text="Return a car",command=returns,bg="black",fg='white',font=('arial',15,'bold')).place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    root.mainloop()

def filters():
    global screen4,tree,e1
    root.destroy()
    screen4= Tk()
    screen4.title("Filters")
    screen4.geometry("1200x600")
    bg2=PhotoImage(file=r"C:\Users\91855\Desktop\Carrental\image8.png")
    my_label2=Label(screen4,image=bg2).pack()
    lb1=Label(screen4,text="Select the filter you would like to apply",bg="black", fg="white",font=("Segoe Print",20,'bold')).place(relx=0.28, rely=0.01)
    global var1,var2,var3,var4,var18,cb1,cb2,cb3,cb4
    var1,var2,var3,var4,var18 =IntVar(screen4),IntVar(screen4),IntVar(screen4),IntVar(screen4),StringVar(screen4)
    frame3=Frame(screen4,bg="black",bd=5).place(relx=0.08,rely=0.2,relwidth=0.25,relheight=0.4)

    cb1= Checkbutton(frame3,text="Pick-up Location",command=showfilter, variable=var1,font=('Segoe Print',14,'bold'))
    cb1.place(relx=0.12, rely=0.22)
    cb2= Checkbutton(frame3,text="With/Without Driver", command=showfilter,variable=var2,font=('Segoe Print',14,'bold'))
    cb2.place(relx=0.12, rely=0.32)
    cb3= Checkbutton(frame3,text="Price Range", command=showfilter,variable=var3,font=('Segoe Print',14,'bold'))
    cb3.place(relx=0.12, rely=0.42)
    cb4= Checkbutton(frame3,text="Seater Capacity", command=showfilter,variable=var4,font=('Segoe Print',14,'bold'))
    cb4.place(relx=0.12, rely=0.52)
    
    #Assign the width, minwidth, and anchor to the respective columns
    tree = ttk.Treeview(screen4, columns=("Car", "Seater Capacity", "Price per day", "Pick-up Location", "Driver Needed?", "Availability"), show="headings")
    tree["columns"] =("Car", "Seater Capacity", "Price per day", "Pick-up Location", "Driver Needed?", "Availability")
    tree.column("Car",width=150,minwidth=30,anchor="s")
    tree.column("Seater Capacity", width=100, minwidth=50, anchor="s")
    tree.column("Price per day", width=100, minwidth=50, anchor="s")
    tree.column("Pick-up Location", width=100, minwidth=50, anchor="s")
    tree.column("Driver Needed?", width=100, minwidth=50, anchor="s")
    tree.column("Availability", width=100, minwidth=50, anchor="s")
    tree.place(relx=0.35, rely=0.2)
    
    #Assign the heading names
    tree.heading("Car",text="Car",anchor="s")
    tree.heading("Seater Capacity", text="Seater Capacity", anchor="s")
    tree.heading("Price per day", text="Price per day", anchor="s")
    tree.heading("Pick-up Location", text="Pick-up Location", anchor="s")
    tree.heading("Driver Needed?", text="Driver Needed?", anchor="s")
    tree.heading("Availability", text="Availability", anchor="s")
    
    e1=Entry(screen4,width=30,textvariable=var18).place(relx=0.70,rely=0.86)
    lb18=Label(screen4,text="Please enter the name of the car you'd like to select:",font=('Arial',14,'bold')).place(relx=0.29,rely=0.85)
    btn6= Button(screen4, text= "SELECT",command=selection, font=('Calibri',15)).place(relx=0.88,rely=0.85)
    btn11= Button(screen4, text= "Try another filter",command=deselect, font=('Calibri',15)).place(relx=0.81,rely=0.65)
    screen4.mainloop()

def showfilter():
    if var1.get()==1:
        pickup()
    if var2.get()==1:
        driver()
    if var3.get()==1:
        price()
    if var4.get()==1:
        seater()

def deselect():
    for item in tree.get_children():
        tree.delete(item)
    cb1.deselect()
    cb2.deselect()
    cb3.deselect()
    cb4.deselect()

def pickup():
    global screen5
    screen5=Toplevel(screen4)
    global var5,var6,var7,var8,var9,var10
    var5,var6,var7,var8,var9,var10=IntVar(screen5),IntVar(screen5),IntVar(screen5),IntVar(screen5),IntVar(screen5),IntVar(screen5),
    screen5.title("Pick-up Location")
    screen5.geometry("800x500")
    bg3=PhotoImage(file=r"C:\Users\91855\Desktop\Carrental\image9.png")
    my_label3=Label(screen5,image=bg3).pack()
    lb2=Label(screen5,text="Please select the pick-up location",bg="black", fg="white",font=("Segoe Print",20,'bold')).place(relx=0.2, rely=0.01)
    cb5= Checkbutton(screen5,text="Bellandur", variable=var5,font=('Calibri',14,'bold')).place(relx=0.15, rely=0.32)
    cb6= Checkbutton(screen5,text="Shivajinagar", variable=var6,font=('Calibri',14,'bold')).place(relx=0.4, rely=0.32)
    cb7= Checkbutton(screen5,text="Koramangala", variable=var7,font=('Calibri',14,'bold')).place(relx=0.67, rely=0.32)
    cb8= Checkbutton(screen5,text="Banashankari", variable=var8,font=('Calibri',14,'bold')).place(relx=0.15, rely=0.52)
    cb9= Checkbutton(screen5,text="Indiranagar", variable=var9,font=('Calibri',14,'bold')).place(relx=0.4, rely=0.52)
    cb10= Checkbutton(screen5,text="Hsr Layout", variable=var10,font=('Calibri',14,'bold')).place(relx=0.67, rely=0.52)
    btn3= Button(screen5, text= "OK",command=show, font=('Calibri',15)).place(relx=0.9,rely=0.8) 
    screen5.mainloop()
def driver():
    global screen6
    screen6= Toplevel(screen4)
    global var11,var12
    var11,var12=IntVar(screen6),IntVar(screen6)
    screen6.title("With/Without Driver")
    screen6.geometry("600x400")
    bg4=PhotoImage(file=r"C:\Users\91855\Desktop\Carrental\image9.png")
    my_label4=Label(screen5,image=bg4).pack()

    lb3=Label(screen6,text="Would you want a driver?",bg="black", fg="white",font=("Segoe Print",20,'bold')).place(relx=0.2, rely=0.01)
    cb11= Checkbutton(screen6,text="Yes", variable=var11,font=('Calibri',20,'bold')).place(relx=0.18, rely=0.3)
    cb12= Checkbutton(screen6,text="No", variable=var12,font=('Calibri',20,'bold')).place(relx=0.68, rely=0.3)
    btn4= Button(screen6, text= "OK",command=show, font=('Calibri',15)).place(relx=0.9,rely=0.8)
    screen6.mainloop()
def price():
    global screen7
    screen7=Toplevel(screen4)
    global var13,var14,var15
    var13,var14,var15=IntVar(screen7),IntVar(screen7),IntVar(screen7)
    screen7.title("Price Range")
    screen7.geometry("600x400")
    bg5=PhotoImage(file=r"C:\Users\91855\Desktop\Carrental\image9.png")
    my_label5=Label(screen7,image=bg5).pack()
    lb4=Label(screen7,text="Choose your price range",bg="black", fg="white",font=("Segoe Print",20,'bold')).place(relx=0.22, rely=0.01)
    cb13= Checkbutton(screen7,text="2000-3000", variable=var13,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.3)
    cb14= Checkbutton(screen7,text="3000-4000", variable=var14,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.5)
    cb15= Checkbutton(screen7,text="4000-5000", variable=var15,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.7)
    btn5= Button(screen7, text= "OK",command=show, font=('Calibri',15)).place(relx=0.9,rely=0.8)
    screen7.mainloop()
def seater():
    global screen8
    screen8=Toplevel()
    global var16,var17,var18
    var16,var17,var18 =IntVar(screen8),IntVar(screen8),IntVar(screen8)
    screen8.title("Seater Capacity")
    screen8.geometry("600x400")
    bg6=PhotoImage(file=r"C:\Users\91855\Desktop\Carrental\image9.png")
    my_label6=Label(screen7,image=bg6).pack()

    lb5=Label(screen8,text="Seater Capacity",bg="black", fg="white",font=("Segoe Print",20,'bold')).place(relx=0.3, rely=0.01)
    cb16= Checkbutton(screen8,text="5-seater", variable=var16,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.3)
    cb17= Checkbutton(screen8,text="7-seater", variable=var17,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.5)
    cb18= Checkbutton(screen8,text="8-seater", variable=var18,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.7)
    btn5= Button(screen8, text= "OK",command=show, font=('Calibri',15)).place(relx=0.9,rely=0.8)
    screen8.main()
#insert values into the window from MySQL table
def show():
    global m,sqlquery
    if var1.get()==1:   
        screen5.destroy()
        if var5.get()==1:
            m="'Bellandur'"
        elif var6.get()==1:
            m="'Shivajinagar'"
        elif var7.get()==1:
            m="'Koramangala'"
        elif var8.get()==1:
            m="'Banashankari'"
        elif var9.get()==1:
            m="'Indiranagar'"
        elif var10.get()==1:
            m="'HSR Layout'"
        sqlquery="select* from cars where pickup=" + m
    
    elif var2.get()==1:
        screen6.destroy()
        if var11.get()==1:
            m="'Yes'"
        else:
            m="'No'"
        sqlquery="select* from cars where driver=" + m
    
    elif var3.get()==1:
        screen7.destroy()
        if var13.get()==1:
            p,q="2000","3000"
        elif var14.get()==1:
            p,q="3000","4000"
        elif var15.get()==1:
            p,q="4000","5000"
        sqlquery="select* from cars where price between "+p+" and "+q
    
    elif var4.get()==1:
        screen8.destroy()
        if var16.get()==1:
            m="5"
        elif var17.get()==1:
            m="7"
        elif var18.get()==1:
            m="8"
        sqlquery="select* from cars where seater=" + m

    cursor.execute(sqlquery)
    rows=cursor.fetchall()
    for x in rows:
        tree.insert('', 'end', values=x) 
   
def selection():
    r="'"+var18.get()+"'"
    remdata="update cars set Availability= 'Unavailable' where carname="+r
    cursor.execute(remdata)
    connection.commit()
    selectiontext="You  have  successfully  rented  " + r +" !"
    lb19=Label(screen4,text=selectiontext,font=('Arial',14,'bold'),bg="black",fg="white").place(relx=0.5,rely=0.75)

def returns():
    root.destroy()
    screen3=Tk()
    screen3.geometry("1200x800")
    screen3.title("Car Returns")
    bg1=PhotoImage(file=r"C:\Users\91855\Desktop\Carrental\image10.png")
    my_label1=Label(screen3,image=bg1)
    my_label1.pack()
    headingFrame2 = Frame(screen3,bg="black",bd=5)
    headingFrame2.place(relx=0.42,rely=0.2,relwidth=0.18,relheight=0.09)
    frame3=Frame(screen3,bg="black")
    frame3.place(relx=0.23,rely=0.33,relwidth=0.55,relheight=0.25)


    lbb=Label(headingFrame2,text="Return a car",bg="white",fg="black",font=("Segoe Print",20,'bold')).place(relx=0.05, rely=0.05)

    def showreturn():
        global z  
        z=cars.get()
        global y
        y=area.get()
        mylabel=Label(screen3,text= "You returned a "+cars.get()+" at "+area.get() ,font=('Calibri',20,'bold'),fg="white",bg="black").place(relx=0.32,rely=0.70)
        cursor.execute("INSERT INTO cars(carname,pickup)  values(%s,%s)", (z,y))
        connection.commit()
   
    cars=StringVar()

    area=StringVar()

    drop=OptionMenu(frame3,cars,"WagonR","Honda City","Swift Dzire","Innova","Xylo","Creta","i20","Jeep Compass","Corolla Altis","Verna","Astar","Duster","i10","Fortuner").place(relx=0.21,rely=0.27,relwidth=0.05 ,relheight=0.05)
    
    lb15=Label(frame3,text="Choose your car",font=("Segoe Print",18,'bold'),fg="black",bg="white").place(relx=0.27,rely=0.13,relheight=0.3,relwidth=0.5)
    drop1=OptionMenu(frame3,area,"Bellandur","Shivajinagar","Koramangala","Indiranagar","HSR Layout","Banashankari").place(relx=0.02,rely=0.69,relwidth=0.05,relheight=0.05)
    lb16=Label(frame3,text="Choose the area you wish to return at",font=("Segoe Print",18,'bold'),fg="black",bg="white").place(relx=0.08,rely=0.52,relwidth=0.85,relheight=0.4)
    mybutton=Button(screen3,text="Show Selection",command=showreturn).place(relx=0.7,rely=0.6)

    e=Entry(screen3,width=30).place(relx=0.30,rely=0.91)
    lb17=Label(screen3,text="Help us improve!",font=('Arial',14,'bold')).place(relx=0.15,rely=0.9)

    screen3.mainloop()


screen1()