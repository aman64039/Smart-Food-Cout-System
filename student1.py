from Tkinter import*
import Tkinter
import MySQLdb
import time
db=MySQLdb.connect("localhost","root","Amanpreet","aproov")
cursor=db.cursor()

top = Tkinter.Tk()
top.geometry("600x700")
top.title("Institute Portal")
top.configure(background='green')

def exit1(event):
	top3.destroy()
def registerstudent(event):
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("800x700")
    top3.configure(background='green')
    top3.title("Register Student") 
    top3.configure(background='green')
    lab31=Label(top3,text="Register Student",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()
    
    lab32=Label(top3,text="First Name")
    lab32.place(x=100,y=100)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=100)
    
    lab33=Label(top3,text="Last Name")
    lab33.place(x=100,y=150)
    E33=Tkinter.Entry(top3,bd=2)
    E33.place(x=325,y=150)
    
    lab34=Label(top3,text="Course")
    lab34.place(x=100,y=200)
    E34=Tkinter.Entry(top3,bd=2)
    E34.place(x=325,y=200)
 
    lab35=Label(top3,text="Start Date\n(Y-M-D)")
    lab35.place(x=100,y=250)
    E35=Tkinter.Entry(top3,bd=2)
    E35.place(x=325,y=250)

    lab36=Label(top3,text="Contact")
    lab36.place(x=100,y=300)
    E36=Tkinter.Entry(top3,bd=2)
    E36.place(x=325,y=300)
    lab37=Label(top3,text="Email")
    lab37.place(x=100,y=350)
    E37=Tkinter.Entry(top3,bd=2)
    E37.place(x=325,y=350)
       

    def sub11(event):
        name= E32.get()
        lname= E33.get()
        course= E34.get()
        stdate= E35.get()
        contact= E36.get()
        email=E37.get()
        try:
            cursor.execute("insert into aman (name,lname,course,stdate,contact,email) values('%s','%s','%s','%s','%s','%s');" %(name,lname,course,stdate,contact,email))
            db.commit()
            sublab=Label(top3,text="Succesfully Registered",fg="GREEN")
            sublab.place(x=100,y=550)
            
        except Exception as e:
            sublab=Label(top3,text="Could not be Registered:'%s'" %(e),fg="RED")
            sublab.place(x=100,y=550)
            db.rollback()


    
    
    busub1=Tkinter.Button(top3,text="Submit",command=sub11,height=2,width=10)
    busub1.place(x=100,y=450)
    busub1.bind('<Return>',sub11)

    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=450)
    busub2.bind('<Return>', exit)

def exit5(event):
	top5.destroy()

def sub5(event):
	name= E5.get()
        course= E6.get()
        try:
            cursor.execute("insert into aman1 (name,course,vdate) values('%s','%s',CURDATE());" %(name,course))
            db.commit()
            sublab=Label(top5,text="Succesfully Registered",fg="GREEN")
            sublab.place(x=100,y=550)
            
        except Exception as e:
            sublab=Label(top5,text="Could not be Registered:'%s'" %(e),fg="RED")
            sublab.place(x=100,y=550)
            db.rollback()


def Inter(event):
	top2.destroy()
	global top5,E5,E6
	top5=Tkinter.Tk()
    	top5.geometry("500x600")
    	top5.configure(background='green')
    	top5.title("Register Student") 
    	top5.configure(background='green')
    	lab31=Label(top5,text="Student Details",fg="RED")
    	lab31.config(font=("TIMES NEW ROMAN",22))
    	lab31.pack()
    
    	lab33=Label(top5,text="Name")
    	lab33.place(x=100,y=150)
    	E5=Tkinter.Entry(top5,bd=2)
    	E5.place(x=225,y=150)
    	
    	lab34=Label(top5,text="Course")
    	lab34.place(x=100,y=200)
    	E6=Tkinter.Entry(top5,bd=2)
    	E6.place(x=225,y=200)
 
	busub1=Tkinter.Button(top5,text="Submit",command=sub5,height=2,width=10)
    	busub1.place(x=100,y=450)
    	busub1.bind('<Return>',sub5)
	
    	busub2=Tkinter.Button(top5,text="Exit",command=exit5,height=2,width=10)
    	busub2.place(x=350,y=450)
    	busub2.bind('<Return>', exit5)

def exit8():
	top8.destroy()
def inter2(event):
	global top8
	top2.destroy()
	top8=Tkinter.Tk()
	top8.geometry("800x900")
	top8.configure(background='green')
	lab21=Label(top8,text="Welcome Aman")
    	lab21.config(font=("TIMES NEW ROMAN",22))
    	lab21.pack()
    	someFrame = Frame(top8)
	someFrame.pack(side=TOP)
	cursor.execute("""select * from aman1""")
	results3 = cursor.fetchall()
	for i in results3:

		someLabel = Label(someFrame, text=i)
		someLabel.pack()
	button=Tkinter.Button(top8,text="Exit",command=exit8,height=2,width=10,fg="red")
	button.place(x=600,y=700)
    
def exit0(event):
	top2.destroy()

def webtechman1():    
    top.destroy()
    global top2
    top2=Tkinter.Tk()
    top2.geometry("600x700")
    lab21=Label(top2,text="Welcome Aman",fg='RED')
    top2.configure(background='green')
    lab21.config(font=("TIMES NEW ROMAN",22))
    lab21.pack()
    bu11=Tkinter.Button(top2,text="Register Student",command=registerstudent,height=5,width=50,bg="red")
    bu11.place(x=100,y=100)
    bu11.bind('<Return>',registerstudent )
    bu22=Tkinter.Button(top2,text="Student Details",command=view,height=5,width=50,bg="red")
    bu22.place(x=100,y=200)
    bu22.bind('<Return>', view)

    bu2=Tkinter.Button(top2,text="Intrection Student",command=Inter,height=5,width=50,bg="red")
    bu2.place(x=100,y=300)
    bu2.bind('<Return>', Inter)

    bu23=Tkinter.Button(top2,text="Intrection Student\nDeatils",command=inter2,height=5,width=50,bg="red")
    bu23.place(x=100,y=400)
    bu23.bind('<Return>', inter2)

    bu24=Tkinter.Button(top2,text="EXIT",command=exit0,height=5,width=50,bg="red")
    bu24.place(x=100,y=500,)
    bu24.bind('<Return>', exit0)



    
def exit1():
	top4.destroy()   
    
def view(event):
	global top4
	top2.destroy()
	top4=Tkinter.Tk()
	top4.geometry("800x900")
	top4.configure(background='green')
	lab21=Label(top4,text="Welcome Aman")
    	lab21.config(font=("TIMES NEW ROMAN",22))
    	lab21.pack()
    	someFrame = Frame(top4)
	someFrame.pack(side=TOP)
	cursor.execute("""select * from aman""")
	results3 = cursor.fetchall()
	for i in results3:

		someLabel = Label(someFrame, text=i)
		someLabel.pack()
	button=Tkinter.Button(top4,text="Exit",command=exit1,height=2,width=10)
	button.place(x=600,y=700)
    

    

def sub(event):
	a=E12.get()
        b=E13.get()
	lab14=Label(top,text="Logging In. Redirecting in few seconds...")
	lab14.config(font=("TIMES NEW ROMAN",22))
        lab14.place(x=100,y=380)
        if(a=="aman" and b=="1234"):
            webtechman1()

        else:
            lab15=Label(top,text="Invalid Username or Password")
            lab15.place(x=100,y=580)


def exit2(event):
	top.destroy()


lab11=Label(top,text="Amanpreet's Login",fg="RED")
lab11.config(font=("TIMES NEW ROMAN",22))
lab11.place(x=100,y=100)
lab12=Label(top,text="Username")
lab12.place(x=100,y=150)
E12=Entry(top,bd=2)
E12.place(x=300,y=150)
lab13=Label(top,text="Password")
lab13.place(x=100,y=180)
E13=Entry(top,bd=2,show='*')
E13.place(x=300,y=180)
submit=Tkinter.Button(top,text="Submit",command=sub ,height=2,width=10)
submit.place(x=100,y=220)
submit.bind('<Return>', sub)
button=Tkinter.Button(top,text="Exit",command=exit2,height=2,width=10)
button.place(x=200,y=220)
button.bind('<Return>', exit2)

  
top.mainloop()
