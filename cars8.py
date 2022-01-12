#with selection based only on one filter at a time
from tkinter import*
from tkinter import ttk
import mysql.connector
connection=mysql.connector.connect(host='localhost',user='vaidu',password='vaiducomp',database='sem1proj')
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
    btn1=Button(root,text="Rent a car",command=filters,bg="black",fg='white',font=('arial',15,'bold')).place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    btn2=Button(root,text="Return a car",command=returns,bg="black",fg='white',font=('arial',15,'bold')).place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    root.mainloop()

def filters():
    global screen4,tree
    root.destroy()
    screen4= Tk()
    screen4.title("Filters")
    screen4.geometry("1200x600")
    lb1=Label(screen4,text="Select the filter you would like to apply",bg="black", fg="white",font=("Segoe Print",20,'bold')).place(relx=0.28, rely=0.01)
    global var1,var2,var3,var4
    var1,var2,var3,var4 =IntVar(screen4),IntVar(screen4),IntVar(screen4),IntVar(screen4),
    cb1= Checkbutton(screen4,text="Pick-up Location",command=pickup, variable=var1,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.22)
    cb2= Checkbutton(screen4,text="With/Without Driver", command=driver,variable=var2,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.32)
    cb3= Checkbutton(screen4,text="Price Range", command=price,variable=var3,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.42)
    cb4= Checkbutton(screen4,text="Seater Capacity", command=seater,variable=var4,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.52)
    
    #Assign the width, minwidth, and anchor to the respective columns
    tree = ttk.Treeview(screen4, columns=("Car", "Seater Capacity", "Price per hour", "Pick-up Location", "Driver Needed?", "Availability"), show="headings")
    tree["columns"] =("Car", "Seater Capacity", "Price per hour", "Pick-up Location", "Driver Needed?", "Availability")
    tree.column("Car",width=150,minwidth=30,anchor="s")
    tree.column("Seater Capacity", width=100, minwidth=50, anchor="s")
    tree.column("Price per hour", width=100, minwidth=50, anchor="s")
    tree.column("Pick-up Location", width=100, minwidth=50, anchor="s")
    tree.column("Driver Needed?", width=100, minwidth=50, anchor="s")
    tree.column("Availability", width=100, minwidth=50, anchor="s")
    tree.place(relx=0.35, rely=0.2)
    
    #Assign the heading names
    tree.heading("Car",text="Car",anchor="s")
    tree.heading("Seater Capacity", text="Seater Capacity", anchor="s")
    tree.heading("Price per hour", text="Price per hour", anchor="s")
    tree.heading("Pick-up Location", text="Pick-up Location", anchor="s")
    tree.heading("Driver Needed?", text="Driver Needed?", anchor="s")
    tree.heading("Availability", text="Availability", anchor="s")
    screen4.mainloop()

def pickup():
    global screen5
    screen5= Tk()
    global var5,var6,var7,var8,var9,var10
    var5,var6,var7,var8,var9,var10=IntVar(screen5),IntVar(screen5),IntVar(screen5),IntVar(screen5),IntVar(screen5),IntVar(screen5),
    screen5.title("Pick-up Location")
    screen5.geometry("800x500")
    lb2=Label(screen5,text="Please select the pick-up location",bg="black", fg="white",font=("Segoe Print",20,'bold')).place(relx=0.2, rely=0.01)
    cb5= Checkbutton(screen5,text="Bellandur", variable=var5,font=('Calibri',14,'bold')).place(relx=0.15, rely=0.32)
    cb6= Checkbutton(screen5,text="Shivajinagar", variable=var6,font=('Calibri',14,'bold')).place(relx=0.4, rely=0.32)
    cb7= Checkbutton(screen5,text="Koramangala", variable=var7,font=('Calibri',14,'bold')).place(relx=0.67, rely=0.32)
    cb8= Checkbutton(screen5,text="Banashankari", variable=var8,font=('Calibri',14,'bold')).place(relx=0.15, rely=0.52)
    cb9= Checkbutton(screen5,text="Indiranagar", variable=var9,font=('Calibri',14,'bold')).place(relx=0.4, rely=0.52)
    cb10= Checkbutton(screen5,text="Hsr Layout", variable=var10,font=('Calibri',14,'bold')).place(relx=0.67, rely=0.52)
    btn3= Button(screen5, text= "OK",command=show, font=('Calibri',15)).place(relx=0.9,rely=0.8) 
  
def driver():
    global screen6
    screen6= Tk()
    global var11,var12
    var11,var12=IntVar(screen6),IntVar(screen6)
    screen6.title("With/Without Driver")
    screen6.geometry("600x400")
    lb3=Label(screen6,text="Would you want a driver?",bg="black", fg="white",font=("Segoe Print",20,'bold')).place(relx=0.2, rely=0.01)
    cb11= Checkbutton(screen6,text="Yes", variable=var11,font=('Calibri',20,'bold')).place(relx=0.18, rely=0.3)
    cb12= Checkbutton(screen6,text="No", variable=var12,font=('Calibri',20,'bold')).place(relx=0.68, rely=0.3)
    btn4= Button(screen6, text= "OK",command=show, font=('Calibri',15)).place(relx=0.9,rely=0.8)

def price():
    global screen7
    screen7=Tk()
    global var13,var14,var15
    var13,var14,var15=IntVar(screen7),IntVar(screen7),IntVar(screen7)
    screen7.title("Price Range")
    screen7.geometry("600x400")
    lb4=Label(screen7,text="Choose your price range",bg="black", fg="white",font=("Segoe Print",20,'bold')).place(relx=0.22, rely=0.01)
    cb13= Checkbutton(screen7,text="2000-3000", variable=var13,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.3)
    cb14= Checkbutton(screen7,text="3000-4000", variable=var14,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.5)
    cb15= Checkbutton(screen7,text="4000-5000", variable=var15,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.7)
    btn5= Button(screen7, text= "OK",command=show, font=('Calibri',15)).place(relx=0.9,rely=0.8)

def seater():
    global screen8
    screen8=Tk()
    global var16,var17,var18
    var16,var17,var18 =IntVar(screen8),IntVar(screen8),IntVar(screen8)
    screen8.title("Seater Capacity")
    screen8.geometry("600x400")
    lb5=Label(screen8,text="Seater Capacity",bg="black", fg="white",font=("Segoe Print",20,'bold')).place(relx=0.3, rely=0.01)
    cb16= Checkbutton(screen8,text="5-seater", variable=var16,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.3)
    cb17= Checkbutton(screen8,text="7-seater", variable=var17,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.5)
    cb18= Checkbutton(screen8,text="8-seater", variable=var18,font=('Calibri',14,'bold')).place(relx=0.08, rely=0.7)
    btn5= Button(screen8, text= "OK",command=show, font=('Calibri',15)).place(relx=0.9,rely=0.8)

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
   

def returns():
    root.destroy()
    screen3=Tk()
    screen3.geometry("1200x800")
    screen3.title("Car Returns")
    lbb=Label(screen3,text="Return a car",bg="black",fg="white",font=("Segoe Print",20,'bold')).place(relx=0.44, rely=0.1)

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