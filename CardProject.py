import Tkinter
import tkMessageBox
from Tkinter import *
import time
from PIL import Image
from PIL import ImageTk

import MySQLdb
db=MySQLdb.connect("localhost","root","Amanpreet","project")
cursor=db.cursor()
global scan,n,lbl
global m
global amount
global G 
global results1


window= Tkinter.Tk()
window.title("Amanpreet Complex")
window.geometry("1200x1000")
image= Image.open('/home/aman/f5crUvz.jpg')
img = ImageTk.PhotoImage(image)
background_label = Label(window, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

singh =['\x02', '5', '4', '0', '0', '2', 'E', '5', 'E', '7', 'F', '5', 'B']
deep = ['\x02', '2', '0', '0', '0', '6', '5', 'A', '6', '6', '1', '8', '2']
aman = ['\x02', '5', '4', '0', '0', '2', 'E', 'E', '7', '4', '3', 'D', 'E']
preet = ['\x02', '5', '4', '0', '0', '2', 'D', 'D', 'C', 'C', 'A', '6', 'F']
def singh1():	
	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Singh',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	text2 = "total amount in the card is ",h
	lbl=Tkinter.Label(window3,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
	lbl.pack()

	print h
	db.close()
def deep1():
	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Deep',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	text2 = "total amount in the card is ",h
	lbl=Tkinter.Label(window3,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
	lbl.pack()

	print h
	db.close()
def preet1():
	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Preet',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	text2 = "total amount in the card is ",h
	lbl=Tkinter.Label(window3,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
	lbl.pack()

	print h
	db.close()

def aman1():
	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Aman',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	text2 = "total amount in the card is ",h
	lbl=Tkinter.Label(window3,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
	lbl.pack()

	print h
	db.close()

def amount_singh():
	amount1=int(ent_amount1.get())
	l="Recharge is successfully \ndone of RS. : ",amount1
	lbl=Tkinter.Label(window3,text=l,font=("Arial Bold", 25))
	lbl.pack()
	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Singh',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	print h
	g=amount1+h
	print g
	
	cursor.execute("""UPDATE aman SET amount= '%s' \
	Where name = %s """,(g,'Singh',))
	db.commit()
	print "done"

def amount_aman():
	amount1=int(ent_amount1.get())
	l="Recharge is successfully \ndone of RS. : ",amount1
	lbl=Tkinter.Label(window3,text=l,font=("Arial Bold", 25))
	lbl.pack()
	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Aman',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	print h
	g=amount1+h
	print g
	
	cursor.execute("""UPDATE aman SET amount= '%s' \
	Where name = %s """,(g,'Aman',))
	db.commit()
	print "done"
def amount_preet():
	amount1=int(ent_amount1.get())
	l="Recharge is successfully \ndone of RS. : ",amount1
	lbl=Tkinter.Label(window3,text=l,font=("Arial Bold", 25))
	lbl.pack()
	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Preet',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	print h
	g=amount1+h
	print g
	
	cursor.execute("""UPDATE aman SET amount= '%s' \
	Where name = %s """,(g,'Preet',))
	db.commit()
	print "done"
def amount_deep():
	global G
	amount1=int(ent_amount1.get())
	l="Recharge is successfully \ndone of RS. : ",amount1
	lbl=Tkinter.Label(window3,text=l,font=("Arial Bold", 25))
	lbl.pack()
	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Deep',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	print h
	g=amount1+h
	print g
	
	cursor.execute("""UPDATE aman SET amount= '%s' \
	Where name = %s """,(g,'Deep',))
	db.commit()
	print "done"
	
def rec1():
	global ent_amount1	
	global amount1
	lbl_amount1 = Tkinter.Label(window3, text="please enter the amount",font=("Arial Bold", 25),bg="#a1dbcd")
	ent_amount1 = Tkinter.Entry(window3)	
	lbl_amount1.pack()
	ent_amount1.pack()
	B7= Tkinter.Button(window3, text="done",command=amount_singh,width=15, height=5, bd=10,bg="SeaGreen2")
	B7.pack()
def rec2():
	global ent_amount1	
	global amount1
	lbl_amount1 = Tkinter.Label(window3, text="please enter the amount",font=("Arial Bold", 25), bg="#a1dbcd")
	ent_amount1 = Tkinter.Entry(window3)	
	lbl_amount1.pack()
	ent_amount1.pack()
	B7= Tkinter.Button(window3, text="done",command=amount_aman,width=15, height=5, bd=10,bg="SeaGreen2")
	B7.pack()
def rec3():
	global ent_amount1	
	global amount1
	lbl_amount1 = Tkinter.Label(window3, text="please enter the amount",font=("Arial Bold", 25),bg="#a1dbcd")
	ent_amount1 = Tkinter.Entry(window3)	
	lbl_amount1.pack()
	ent_amount1.pack()
	B7= Tkinter.Button(window3, text="done",command=amount_preet,width=15, height=5, bd=10,bg="SeaGreen2")
	B7.pack()
def rec4():
	global ent_amount1	
	global amount1
	lbl_amount1 = Tkinter.Label(window3, text="please enter the amount",font=("Arial Bold", 25), bg="#a1dbcd")
	ent_amount1 = Tkinter.Entry(window3)	
	lbl_amount1.pack()
	ent_amount1.pack()
	B7= Tkinter.Button(window3, text="done",command=amount_deep,width=15, height=5, bd=10,bg="SeaGreen2")
	B7.pack()
	
def scan():
	print "welcome"
	global m
	time.sleep(5)
	import serial
	count=0
	m=[]
	with serial.Serial('/dev/ttyUSB0',9600,timeout=1) as ser:
		i=0
		count=0
		while(i<=14):
			x=ser.read()
			if(x!=''):
				m.append(x)
			i=i+1
	del m[13:]
	print m
def check():
	singh =['\x02', '5', '4', '0', '0', '2', 'E', '5', 'E', '7', 'F', '5', 'B']
	deep = ['\x02', '2', '0', '0', '0', '6', '5', 'A', '6', '6', '1', '8', '2']
	aman = ['\x02', '5', '4', '0', '0', '2', 'E', 'E', '7', '4', '3', 'D', 'E']
	preet = ['\x02', '5', '4', '0', '0', '2', 'D', 'D', 'C', 'C', 'A', '6', 'F']
	global window3
	if(m==singh):
		time.sleep(1)
		window3= Tkinter.Tk()
		window3.title("Amanpreet Complex")
		window3.geometry("1200x1000")
		

		

		text1 = "Card holder name is: Singh"
		lbl=Tkinter.Label(window3,text=text1,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()

		B5 = Tkinter.Button(window3, text="recharge", command=rec1,width=15, height=5, bd=10,bg="SeaGreen2")
		B5.pack()
		
		B6= Tkinter.Button(window3, text="check balance", command=singh1,width=15, height=5, bd=10,bg="SeaGreen2")
		B6.pack()
	elif(m==aman):
		
		time.sleep(1)
		window3= Tkinter.Tk()
		window3.title("Amanpreet Complex")
		window3.geometry("1200x1000")
		

		text1 = "Card holder name is: Aman"
		lbl=Tkinter.Label(window3,text=text1,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()

		B5 = Tkinter.Button(window3, text="recharge", command=rec2,width=15, height=5, bd=10,bg="SeaGreen2")
		B5.pack()
		
		B6= Tkinter.Button(window3, text="check balance", command=aman1,width=15, height=5, bd=10,bg="SeaGreen2")
		B6.pack()
	elif(m==preet):
		time.sleep(1)
		window3= Tkinter.Tk()
		window3.title("Amanpreet Complex")
		window3.geometry("1200x1000")
	

		text1 = "Card holder name is: Preet"
		lbl=Tkinter.Label(window3,text=text1,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()

		B5 = Tkinter.Button(window3, text="recharge", command=rec3,width=15, height=5, bd=10,bg="SeaGreen2")
		B5.pack()
		
		B6= Tkinter.Button(window3, text="check balance", command=preet1,width=15, height=5, bd=10,bg="SeaGreen2")
		B6.pack()
	elif(m==deep):
		time.sleep(5)
		window3= Tkinter.Tk()
		window3.title("Amanpreet Complex")
		window3.geometry("1200x1000")
		
		
		text1 = "Card holder name is: Deep"
		lbl=Tkinter.Label(window3,text=text1,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()

		B5 = Tkinter.Button(window3, text="recharge", command=rec4,width=15, height=5, bd=10,bg="SeaGreen2")
		B5.pack()
		
		B6= Tkinter.Button(window3, text="check balance", command=deep1)
		B6.pack()
	else:
		global window9
		time.sleep(5) 
		window9=Tkinter.Tk()
		window9.title("Amanpreet Complex")
		window9.geometry("1200x1000")
		lbl = Tkinter.Label(window9 , text="Invalid coustmer id*****",font=("Arial Bold", 25))
		lbl.pack()
def pays():
	window23.destroy()
	global window24

	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Singh',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	print h
	if(h>total):
		print "if"
		window24=Tkinter.Tk()
		window24.title("Amanpreet Complex")
		window24.geometry("1200x1000")

	
		g=h-total
		print g
	
		cursor.execute("""UPDATE aman SET amount= '%s' \
		Where name = %s """,(g,'Singh',))
		db.commit()
		print "done"
		cursor.execute("""select amount from aman where name = %s""",('Singh',))
		results3 = cursor.fetchall()
		for row in results3:
			o=row[0]
		print o	
		f="Thankyou for pay ,Your Total \nremaining amount is ",o
		lbl=Tkinter.Label(window24,text=f,font=("Arial Bold", 25))
		lbl.pack()
	else:
		print "else"
		window24=Tkinter.Tk()
		window24.title("Amanpreet Complex")
		window24.geometry("1200x1000")

		lbl=Tkinter.Label(window24,text="Sorry You have no sufficent balance**",font=("Arial Bold", 25))
		lbl.pack()

def paya():
	window23.destroy()
	global window24
	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Aman',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	print h
	if(h > total):
		print "if"
		window24=Tkinter.Tk()
		window24.title("Amanpreet Complex")
		window24.geometry("1200x1000")

	
		g= h-total
		print g
	
		cursor.execute("""UPDATE aman SET amount= '%s' \
		Where name = %s """,(g,'Aman',))
		db.commit()
		print "done"
		cursor.execute("""select amount from aman where name = %s""",('Aman',))
		results3 = cursor.fetchall()
		for row in results3:
			o=row[0]
		print o	
		f="Thankyou for pay ,Your Total \nremaining amount is ",o
		lbl=Tkinter.Label(window24,text=f,font=("Arial Bold", 25))
		lbl.pack()
	else:
		print"else"
		window24=Tkinter.Tk()
		window24.title("Amanpreet Complex")
		window24.geometry("1200x1000")

		lbl=Tkinter.Label(window24,text="Sorry You have no \nsufficent balance**",font=("Arial Bold", 25))
		lbl.pack()

def payd():
	window23.destroy()
	global window24

	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Deep',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	print h
	if(h>total):
		print "if"
		window24=Tkinter.Tk()
		window24.title("Amanpreet Complex")
		window24.geometry("1200x1000")

		g=h-total
		print g
		import MySQLdb
		db=MySQLdb.connect("localhost","root","Amanpreet","project")
		cursor=db.cursor()
	
		cursor.execute("""UPDATE aman SET amount= '%s' \
		Where name = %s """,(g,'Deep',))
		db.commit()
		print "done"
		cursor.execute("""select amount from aman where name = %s""",('Deep',))
		results3 = cursor.fetchall()
		for row in results3:
			o=row[0]
		print o	
		f="Thankyou for pay ,Your Total \nremaining amount is ",o
		lbl=Tkinter.Label(window24,text=f,font=("Arial Bold", 25))
		lbl.pack()
	else:
		print "else"
		window24=Tkinter.Tk()
		window24.title("Amanpreet Complex")
		window24.geometry("1200x1000")

		lbl=Tkinter.Label(window24,text="Sorry You have no \nsufficent balance**",font=("Arial Bold", 25))
		lbl.pack()

def payp():
	window23.destroy()
	global window24
	global total
	import MySQLdb
	db=MySQLdb.connect("localhost","root","Amanpreet","project")
	cursor=db.cursor()
	cursor.execute("""select amount from aman where name = %s""",('Preet',))
	results3 = cursor.fetchall()
	for row in results3:
		h=row[0]
	print h
	if(h>total):
		print "if"
		window24=Tkinter.Tk()
		window24.title("Amanpreet Complex")
		window24.geometry("1200x1000")

		g=h-total
		print g
	
		cursor.execute("""UPDATE aman SET amount= '%s' \
		Where name = %s """,(g,'Preet',))
		db.commit()
		print "done"
		cursor.execute("""select amount from aman where name = %s""",('Preet',))
		results3 = cursor.fetchall()
		for row in results3:
			o=row[0]
		print o	
		f="Thankyou for pay ,Your Total\n remaining amount is ",o
		lbl=Tkinter.Label(window24,text=f,font=("Arial Bold", 25))
		lbl.pack()
	else:
		print "else"
		window24=Tkinter.Tk()
		window24.title("Amanpreet Complex")
		window24.geometry("1200x1000")

		lbl=Tkinter.Label(window24,text="Sorry You have no\n sufficent balance**",font=("Arial Bold", 25))
		lbl.pack()

def check2():
	singh =['\x02', '5', '4', '0', '0', '2', 'E', '5', 'E', '7', 'F', '5', 'B']
	deep = ['\x02', '2', '0', '0', '0', '6', '5', 'A', '6', '6', '1', '8', '2']
	aman = ['\x02', '5', '4', '0', '0', '2', 'E', 'E', '7', '4', '3', 'D', 'E']
	preet = ['\x02', '5', '4', '0', '0', '2', 'D', 'D', 'C', 'C', 'A', '6', 'F']
	window22.destroy()
	global window23
	window23=Tkinter.Tk()
	window23.title("Amanpreet Complex")
	window23.geometry("1200x1000")

	if(m==singh):
		lbl=Tkinter.Label(window23,text="Card Holder name is : Singh",font=("Arial Bold", 25))
		lbl.pack()
		import MySQLdb
		db=MySQLdb.connect("localhost","root","Amanpreet","project")
		cursor=db.cursor()
		cursor.execute("""select amount from aman where name = %s""",('Singh',))
		results3 = cursor.fetchall()
		for row in results3:
			h=row[0]
		text2 = "total amount in the card is ",h
		lbl=Tkinter.Label(window23,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()
		uj="and total amount to be paid is ",total
		lbl1=Tkinter.Label(window23,text=uj,font=("Arial Bold", 25))
		lbl1.pack()
		db.close()
		B15= Tkinter.Button(window23, text ="Pay", command = pays, width=15, height=5, bd=10,bg="SeaGreen2")
		B15.pack()


		

		
	elif(m==aman):
		lbl1=Tkinter.Label(window23,text="Card Holder name is : Aman",font=("Arial Bold", 25))
		lbl1.pack()
		import MySQLdb
		db=MySQLdb.connect("localhost","root","Amanpreet","project")
		cursor=db.cursor()
		cursor.execute("""select amount from aman where name = %s""",('Aman',))
		results3 = cursor.fetchall()
		for row in results3:
			h=row[0]
		text2 = "Total amount in the card is ",h
		lbl2=Tkinter.Label(window23,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl2.pack()
		uj="and total amount to be paid is ",total
		lbl1=Tkinter.Label(window23,text=uj,font=("Arial Bold", 25))
		lbl1.pack()
		
		db.close()
		B15= Tkinter.Button(window23, text ="Pay", command = paya, width=15, height=5, bd=10,bg="SeaGreen2")
		B15.pack()


	elif(m==preet):
		lbl1=Tkinter.Label(window23,text="Card Holder name is : Preet",font=("Arial Bold", 25))
		lbl1.pack()
		import MySQLdb
		db=MySQLdb.connect("localhost","root","Amanpreet","project")
		cursor=db.cursor()
		cursor.execute("""select amount from aman where name = %s""",('Preet',))
		results3 = cursor.fetchall()
		for row in results3:
			h=row[0]
		text2 = "Total amount in the card is ",h
		lbl2=Tkinter.Label(window23,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl2.pack()
		uj="and total amount to be paid is ",total
		lbl1=Tkinter.Label(window23,text=uj,font=("Arial Bold", 25))
		lbl1.pack()
		
		db.close()
		B15= Tkinter.Button(window23, text ="Pay", command = payp, width=15, height=5, bd=10,bg="SeaGreen2")
		B15.pack()

	elif(m==deep):
		lbl1=Tkinter.Label(window23,text="Card Holder name is : Deep",font=("Arial Bold", 25))
		lbl1.pack()
		import MySQLdb
		db=MySQLdb.connect("localhost","root","Amanpreet","project")
		cursor=db.cursor()
		cursor.execute("""select amount from aman where name = %s""",('Deep',))
		results3 = cursor.fetchall()
		for row in results3:
			h=row[0]
		text2 = "Total amount in the card is ",h
		lbl2=Tkinter.Label(window23,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl2.pack()
		uj="and total amount to be paid is ",total
		lbl1=Tkinter.Label(window23,text=uj,font=("Arial Bold", 25))
		lbl1.pack()
		
		db.close()
		B15= Tkinter.Button(window23, text ="Pay", command = payd, width=15, height=5, bd=10,bg="SeaGreen2")
		B15.pack()

		
	else:
		global window9
		time.sleep(5) 
		window9=Tkinter.Tk()
		window9.title("Amanpreet Complex")
		window9.geometry("1200x1000")
		lbl = Tkinter.Label(window9 , text="Invalid coustmer id*****",font=("Arial Bold", 25))
		lbl.pack()


def scan3():
	lbl=Tkinter.Label(window22,text="Please Scan The Card For Payment",font=("Arial Bold", 25))
	lbl.pack()
	print "welcome"
	global m
	time.sleep(5)
	import serial
	count=0
	m=[]
	with serial.Serial('/dev/ttyUSB0',9600,timeout=1) as ser:
		i=0
		count=0
		while(i<=14):
			x=ser.read()
			if(x!=''):
				m.append(x)
			i=i+1
	del m[13:]
	print m
	check2()
	
def bill_1():
	window14.destroy()
	global window22
	window22= Tkinter.Tk()
	window22.title("Amanpreet Complex")
	window22.geometry("1200x1000")
	global total

	Bill=349
	Gst=(349/100)*18
	total=Bill+Gst
	lbl1=Tkinter.Label(window22,text="Your bill is :349",font=("Arial Bold", 25))
	lbl1.pack()
	w="And GST ON bill is :",Gst
	lbl2=Tkinter.Label(window22,text=w,font=("Arial Bold", 25))
	lbl2.pack()
	e="Your total bill is ",total
	lbl3=Tkinter.Label(window22,text=e,font=("Arial Bold", 25))
	lbl3.pack()
	B10 = Tkinter.Button(window22, text="Done", command=scan3 ,width=15, height=5, bd=10,bg="SeaGreen2")
	B10.pack()
	
def bill_2():
	window14.destroy()
	global window22
	window22= Tkinter.Tk()
	window22.title("Amanpreet Complex")
	window22.geometry("1200x1000")
	global total

	Bill=449
	Gst=(449/100)*18
	total=Bill+Gst
	lbl1=Tkinter.Label(window22,text="Your bill is :449",font=("Arial Bold", 25))
	lbl1.pack()
	w="And GST ON bill is :",Gst
	lbl2=Tkinter.Label(window22,text=w,font=("Arial Bold", 25))
	lbl2.pack()
	e="Your total bill is ",total
	lbl3=Tkinter.Label(window22,text=e,font=("Arial Bold", 25))
	lbl3.pack()
	B10 = Tkinter.Button(window22, text="Done", command=scan3 ,width=15, height=5, bd=10,bg="SeaGreen2")
	B10.pack()
	
def bill_3():
	window14.destroy()
	global window22
	global total
	window22= Tkinter.Tk()
	window22.title("Amanpreet Complex")
	window22.geometry("1200x1000")
	Bill=549
	Gst=(549/100)*18
	total=Bill+Gst
	lbl1=Tkinter.Label(window22,text="Your bill is :549",font=("Arial Bold", 25))
	lbl1.pack()
	w="And GST OF bill is :",Gst
	lbl2=Tkinter.Label(window22,text=w,font=("Arial Bold", 25))
	lbl2.pack()
	e="Your total bill is ",total
	lbl3=Tkinter.Label(window22,text=e,font=("Arial Bold", 25))
	lbl3.pack()
	B10 = Tkinter.Button(window22, text="Done", command=scan3 ,width=15, height=5, bd=10,bg="SeaGreen2")
	B10.pack()

def bill_4():
	window14.destroy()
	global window22
	global total
	window22= Tkinter.Tk()
	window22.title("Amanpreet Complex")
	window22.geometry("1200x1000")
	Bill = 101
	Gst = (101/100)*18
	print Gst
	total=Bill+Gst
	lbl1=Tkinter.Label(window22,text="Your bill is :101",font=("Arial Bold", 25))
	lbl1.pack()
	w="And GST OF bill is :",Gst
	lbl2=Tkinter.Label(window22,text=w,font=("Arial Bold", 25))
	lbl2.pack()
	e="Your total bill is ",total
	lbl3=Tkinter.Label(window22,text=e,font=("Arial Bold", 25))
	lbl3.pack()
	B10 = Tkinter.Button(window22, text="Done", command=scan3 ,width=15, height=5, bd=10,bg="SeaGreen2")
	B10.pack()

def bill_5():
	window14.destroy()
	global window22
	window22= Tkinter.Tk()
	window22.title("Amanpreet Complex")
	window22.geometry("1200x1000")
	global total

	Bill=119
	Gst=(119/100)*18
	total=Bill+Gst
	lbl1=Tkinter.Label(window22,text="Your bill is :119",font=("Arial Bold", 25))
	lbl1.pack()
	w="And GST OF bill is :",Gst
	lbl2=Tkinter.Label(window22,text=w,font=("Arial Bold", 25))
	lbl2.pack()
	e="Your total bill is ",total
	lbl3=Tkinter.Label(window22,text=e,font=("Arial Bold", 25))
	lbl3.pack()
	B10 = Tkinter.Button(window22, text="Done", command=scan3 ,width=15, height=5, bd=10,bg="SeaGreen2")
	B10.pack()

def bill_6():
	window14.destroy()
	global window22
	window22= Tkinter.Tk()
	window22.title("Amanpreet Complex")
	window22.geometry("1200x1000")
	global total

	Bill=149
	Gst=(149/100)*18
	total=Bill+Gst
	lbl1=Tkinter.Label(window22,text="Your bill is :149",font=("Arial Bold", 25))
	lbl1.pack()
	w="And GST OF bill is :",Gst
	lbl2=Tkinter.Label(window22,text=w,font=("Arial Bold", 25))
	lbl2.pack()
	e="Your total bill is ",total
	lbl3=Tkinter.Label(window22,text=e,font=("Arial Bold", 25))
	lbl3.pack()
	B10 = Tkinter.Button(window22, text="Done", command=scan3 ,width=15, height=5, bd=10,bg="SeaGreen2")
	B10.pack()


def kfc():
	window13.destroy()
	global window14
	window14= Tkinter.Tk()
	window14.title("Amanpreet Complex")
	window14.geometry("1200x1000")
	lbl=Tkinter.Label(window14 ,text="please click on your choice",font=("Arial Bold", 25))
	lbl.pack()
	
	kfc = Radiobutton(window14, text ="1.SMOKY GRILLED \nWINGS 15 PC",command = bill_1, width=15, height=5, bd=10,bg="SeaGreen2")
	kfc1 = Radiobutton(window14, text ="2.SMOKY WINGS 15 \nPC & 2 PEPSI CAN ",command = bill_2, width=15, height=5, bd=10,bg="SeaGreen2")
	kfc2 = Radiobutton(window14, text ="3.HALF N HALF\n MEAL ", command = bill_3, width=15, height=5, bd=10,bg="SeaGreen2")	
	kfc.pack()
	kfc1.pack()
	kfc2.pack()
def mcd():

	window13.destroy()
	global window14
	global Radiobutton
	window14= Tkinter.Tk()
	window14.title("Amanpreet Complex")
	window14.geometry("1200x1000")
	lbl=Tkinter.Label(window14 ,text="please click on your choice",font=("Arial Bold", 25))
	lbl.pack()

	mcd = Radiobutton(window14, text ="1.MC ALLO \nTIKKI BURGER", command = bill_4, width=15, height=5, bd=10,bg="SeaGreen2")
	mcd1 = Radiobutton(window14, text ="2.MC CHICK \nBURGER ", command = bill_5, width=15, height=5, bd=10,bg="SeaGreen2")
	mcd2 = Radiobutton(window14, text ="3.MC JUMBO CHICK \n& CHEESY BURGER ", command = bill_6, width=15, height=5, bd=10,bg="SeaGreen2")	
	mcd.pack()
	mcd1.pack()
	mcd2.pack()



	
def food():
	window11.destroy()
	global window13
	window13=Tkinter.Tk()
	window13.title("Amanpreet Complex")
	window13.geometry("1200x1000")
	
	lbl=Tkinter.Label(window13,text="Please click on your choice",font=("Arial Bold", 25),bg="#a1dbcd")
	lbl.pack()
	B8 = Tkinter.Button(window13, text="Kfc", command=kfc ,width=15, height=5, bd=10,bg="SeaGreen2")
	B8.pack()
	B9 = Tkinter.Button(window13, text="McDonald's", command=mcd ,width=15, height=5, bd=10,bg="SeaGreen2")
	B9.pack()
	
			
def check1():
	global window12
	singh =['\x02', '5', '4', '0', '0', '2', 'E', '5', 'E', '7', 'F', '5', 'B']
	deep = ['\x02', '2', '0', '0', '0', '6', '5', 'A', '6', '6', '1', '8', '2']
	aman = ['\x02', '5', '4', '0', '0', '2', 'E', 'E', '7', '4', '3', 'D', 'E']
	preet = ['\x02', '5', '4', '0', '0', '2', 'D', 'D', 'C', 'C', 'A', '6', 'F']
	
	window12= Tkinter.Tk()
	window12.title("Amanpreet Complex")
	window12.geometry("1200x1000")
	if(m==singh):
		text4="Card Holder Name is [Singh]"
		lbl=Tkinter.Label(window12,text=text4,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()

		import MySQLdb
		db=MySQLdb.connect("localhost","root","Amanpreet","project")
		cursor=db.cursor()
		cursor.execute("""select amount from aman where name = %s""",('Singh',))
		results3 = cursor.fetchall()
		for row in results3:
			h=row[0]
		text2 = "total amount in the card is ",h
		lbl=Tkinter.Label(window12,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()

		print h
		db.close()
		
	elif(m==aman):
		text4="Card Holder Name is [Aman]"
		lbl=Tkinter.Label(window12,text=text4,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()

		import MySQLdb
		db=MySQLdb.connect("localhost","root","Amanpreet","project")
		cursor=db.cursor()
		cursor.execute("""select amount from aman where name = %s""",('Aman',))
		results3 = cursor.fetchall()
		for row in results3:
			h=row[0]
		text2 = "total amount in the card is ",h
		lbl=Tkinter.Label(window12,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()
	
		print h
		db.close()
	elif(m==preet):
		text4="Card Holder Name is [Preet]"
		lbl=Tkinter.Label(window12,text=text4,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()

		import MySQLdb
		db=MySQLdb.connect("localhost","root","Amanpreet","project")
		cursor=db.cursor()
		cursor.execute("""select amount from aman where name = %s""",('Preet',))
		results3 = cursor.fetchall()
		for row in results3:
			h=row[0]
		text2 = "total amount in the card is ",h
		lbl=Tkinter.Label(window12,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()

		print h
		db.close()
	elif(m==deep):
		text4="Card Holder Name is [Deep]"
		lbl=Tkinter.Label(window12,text=text4,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()
	
		import MySQLdb
		db=MySQLdb.connect("localhost","root","Amanpreet","project")
		cursor=db.cursor()
		cursor.execute("""select amount from aman where name = %s""",('Deep',))
		results3 = cursor.fetchall()
		for row in results3:
			h=row[0]
		text2 = "total amount in the card is ",h
		lbl=Tkinter.Label(window12,text=text2,font=("Arial Bold", 25),bg="#a1dbcd")
		lbl.pack()
	
		print h
		db.close()
	else:
		global window19
		time.sleep(5) 
		window9=Tkinter.Tk()
		window9.title("Amanpreet Complex")
		window9.geometry("1200x1000")
		lbl = Tkinter.Label(window19 , text="Invalid coustmer id*****",font=("Arial Bold", 15))
		lbl.pack()

def option():
		username = ent_username.get() 
		password = ent_password.get() 
		if username == "aman" and password=="1421708":
			window1.destroy()
			print"Please Scan the Card"
			scan()
			check()
			
		else:
			window1.destroy()
			window2=Tkinter.Tk()
			window2.title("Amanpreet Complex")
			window2.geometry("1200x1000")
			lbl = Tkinter.Label(window2 , text="Invalid user id and pasword*****",font=("Arial Bold", 25))
			lbl.pack()
		
	
def man():
	global ent_username,ent_password	
	window.destroy()
	global window1
	window1= Tkinter.Tk()
	window1.title("Amanpreet Complex")
	window1.geometry("1200x1000")
	
	lbl_username = Tkinter.Label(window1, text="Username",font=("Arial Bold", 25), bg="#a1dbcd")
	ent_username = Tkinter.Entry(window1)
	
		
	lbl_username.pack()
	ent_username.pack()

	username = ent_username.get()
	lbl_password = Tkinter.Label(window1, text="Password",font=("Arial Bold", 25), bg="#a1dbcd")
	ent_password = Tkinter.Entry(window1)
	password = ent_password.get()
	lbl_password.pack()
	ent_password.pack()
	btn = Tkinter.Button(window1, text="Sign In", command=option,width=15, height=5,bd=10)
	btn.pack()
def scan1():
	window11.destroy()
	print "Please Sacn your card"
	global m
	time.sleep(5)
	import serial
	count=0
	m=[]
	with serial.Serial('/dev/ttyUSB0',9600,timeout=1) as ser:
		i=0
		count=0
		while(i<=14):
			x=ser.read()
			if(x!=''):
				m.append(x)
			i=i+1
	del m[13:]
	print m
	time.sleep(1)
	check1()

def cus():
	window.destroy()
	global window11
	window11= Tkinter.Tk()
	window11.title("Amanpreet Complex")
	window11.geometry("1200x1000")
	lbl = Tkinter.Label(window11, text="Welcome to Amanpreet Complex",font=("Arial Bold", 25), bg="#a1dbcd")
	lbl.pack()
	B1 = Tkinter.Button(window11, text ="Food Court", command = food, width=15, height=5, bd=10,bg="SeaGreen2")
	B2= Tkinter.Button(window11, text ="Check Balance", command =scan1, width=15, height=5, bd=10,bg="SeaGreen2")
	B1.pack()
	B2.pack()
		
	

lbl = Tkinter.Label(window, text="Welcome to Amanpreet Complex",font=("Arial Bold", 25), bg="#a1dbcd")
lbl.pack()	
B1 = Tkinter.Button(window, text ="Manager", command = man, width=15, height=5, bd=10,bg="SeaGreen2")
B2= Tkinter.Button(window, text ="Coustmer", command = cus, width=15, height=5, bd=10,bg="SeaGreen2")
B1.pack()
B2.pack()
window.mainloop()

