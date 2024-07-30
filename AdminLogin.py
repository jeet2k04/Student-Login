	#import module
from tkinter import *
from tkinter import messagebox
import pymysql
import csv
conobj = pymysql.connect (host = "localhost",user="root",password="",port=3306)
curobj = conobj.cursor ()
curobj.execute ('use pydb;')
#curobj.execute('show databases;')
#dblist = curobj.fetchall ()
#print("data base list :",dblist)

win2 = Tk ()	#win2 is a project of Tk class
#print("--------------------------------------------")
def Exit():
	win2.destroy ()
#print("--------------------------------------------")

def Reset():
	
	Lauid.delete(0,END)
	Lapwd.delete(0,END)

#print("--------------------------------------------")
def ALogin():
	LAuid = Lauid.get ()
	LApwd = Lapwd.get ()
	r=f'select * from admin where userid = "{LAuid}" and PASSWORD="{LApwd}";'
	curobj.execute(r)
	record=curobj.fetchall()
	if len(record):
		print("Welcome to Admin Home Page")
		messagebox.showinfo("Login Page","Login Successfully.")
		win2.destroy()
		win3= Tk()
		def Exit():
			win3.destroy()
#-----------------------------------------------
		def ShowAll ():
			win3.destroy()
			win6 = Tk()
			fobj= open("studentdata.csv",'w', newline = "\n")
			cobj = csv.writer (fobj)
			cobj.writerow(['stud_name', 'parent_name', 'Regno', 'Acc_Year', 'Dept', 'Gender', 'Contact', 'password'])

			win6.minsize (700,700) #minsize (x,y)
			win6.maxsize (700,700)
			win6.title("Display All")
			win6.configure(bg="#328fce")
			curobj.execute('select * from student;')
			record = curobj.fetchall()
			for i in record:
				cobj.writerow(i)
				#fobj.write("\n")
			fobj.close()
				#print(i)
			'''
			i=0
			for student in curobj :
				for j in range(len(student)):
					e=Entry(win6,width=20,bg="blue",fg="white",font=("Times New Roman",15,"bold"))
					e.grid(row=i,column=j)
					e.insert(END,student[j])
				i=i+1
				'''
			win6.mainloop()
#-----------------------------------------------
		def DelStudent():
			win3.destroy()
			win4=Tk()
			def Exit():
				win4.destroy()
#----------------------------------------------
			def Delete():
				DREGNO= Dregno.get()
				r='delete from student where regno ="{R}";'
				r1=r.format(R=DREGNO)
				#print(r1)
				curobj.execute(r1)
				conobj.commit()
				win4.destroy()
#----------------------------------------------
		
#------------------------------
			win4.minsize (600,600)
			win4.maxsize (600,600)
			win4.title("Delete Student")
			win4.configure(bg="#758fee")

			Label (win4,text="!Delete Student Page!",font=("Algerian",25,"bold"),
	bg="yellow",fg="#ff0000",relief="solid",width="27").place(x=0,y=50)
			Label (win4,text="Enter RegNo :",font=("Times New Roman",15,"bold"),
	bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=150)
			Dregno=Entry(win4,font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18")
			Dregno.place(x=300,y=150)
			Button(win4,text="Delete",bg="green",fg="red",font=("Times New Roman",15,"bold"),relief="raised",widt=15,command=Delete).place(x=70,y=500)
			Button(win4,text="Exit",bg="Red",fg="black",font=("Times New Roman",15,"bold"),relief="raised",width=15,command=Exit).place(x=300,y=500)

			win4.mainloop()
#----------------------------------------
		def AddStudent():
			win3.destroy ()
			win5=Tk()

			def AAdd ():
				RSNAME = RSname.get()
				RPNAME = Rpname.get()
				RRNO = RRno.get()
				RPWD = Rpwd.get()
				r = 'insert into student(sname,pname,regno,spassword) values ("{S}","{P}","{R}","{PWD}");'
				r1=r.format (S=RSNAME,P=RPNAME,R=RRNO,PWD=RPWD)
				#print(r1)
				curobj.execute(r1)
				conobj.commit()
				win5.destroy()
#-------------------------------------------------
			def AReset ():
				RSname.delete(0,END)
				Rpname.delete(0,END)
				RRno.delete(0,END)
				Rpwd.delete(0,END)
#-------------------------------------------------
			def AExit ():
				win5.destroy()
#-------------------------------------------------				
			win5.minsize (600,600)
			win5.maxsize (600,600)
			win5.title("Add New Student")
			win5.configure(bg="#758fee")

			Label (win5,text="!Enter Student Details!",font=("Algerian",25,"bold"),
	bg="yellow",fg="#ff0000",relief="solid",width="27").place(x=0,y=50)

			Label (win5,text="Enter Student Name :",font=("Times New Roman",15,"bold"),
	bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=150)
			RSname= Entry(win5, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18")
			RSname.place(x=270,y=150)

			Label (win5,text="Enter Parents Name :",font=("Times New Roman",15,"bold"),
	bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=200)
			Rpname= Entry(win5, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18")
			Rpname.place(x=270,y=200)

			Label (win5,text="Enter Student RegNo :",font=("Times New Roman",15,"bold"),
	bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=250)
			RRno= Entry(win5, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18")
			RRno.place(x=270,y=250)

			Label (win5,text="Enter Password 	:",font=("Times New Roman",15,"bold"),
	bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=300)
			Rpwd=Entry(win5, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18",show="*")
			Rpwd.place(x=270,y=300)

			Button(win5,text="Add",width="10",height="1", font=("Times New Roman",15,"bold"),
	relief="ridge",bg="#0000ff",fg="#ffffff",command=AAdd, activebackground="green", bd=5).place(x=37, y=400)

			Button(win5,text="Reset",width="10",height="1", font=("Times New Roman",15,"bold"),
	relief="ridge",bg="#808080",fg="#ffffff",command=AReset,activebackground="#728fce", bd=5).place(x=200, y=400)

			Button(win5,text="Exit",width="10",height="1", font=("Times New Roman",15,"bold"),
	relief="ridge",bg="#ff0000",fg="#ffffff",command=AExit,activebackground="yellow", bd=5).place(x=360, y=400)


			win5.mainloop()
		win3.minsize (700,700) #minsize (x,y)
		win3.maxsize (700,700)
		win3.title("Admin Operation Page")
		win3.configure(bg="#328fce")
		Label (win3,text="!!! Select Any Operation !!!",font=("Algerian",25,"bold"),
	bg="#ffff00",fg="#ff0000",relief="raised",width="35").place(x=0,y=50)

		Button(win3,text="Add New Student",bg="green",fg="red",font=("Times New Roman",15,"bold"),relief="raised",width=20,command=AddStudent).place(x=50,y=150)
		Button(win3,text="Delete Student",bg="green",fg="red",font=("Times New Roman",15,"bold"),relief="raised",width=20,command=DelStudent).place(x=50,y=250)
		Button(win3,text="Exit",bg="orange",fg="black",font=("Times New Roman",15,"bold"),relief="raised",width=10,command=Exit).place(x=50,y=350)
		Button(win3,text="ShowAll",bg="blue",fg="white",font=("Times New Roman",15,"bold"),relief="raised",width=15,command=ShowAll).place(x=200,y=350)
		
		win3.mainloop ()

	else :
		print("Invalid Record")
		messagebox.showinfo("Error","Try again later..")
		win2.destroy()


win2.minsize (500,600) #minsize (x,y)
win2.maxsize (500,600)
#win2.geometry ("300x400")
win2.title("Admin Login Page")
win2.configure(bg="#728fce")

Label (win2,text=" ADMIN Login",font=("Algerian",25,"bold"),
	bg="#ffff00",fg="#ff0000",relief="raised",width="23").place(x=4,y=50)

Label (win2,text="Enter User ID :",font=("Times New Roman",15,"bold"),
	bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=150)
Lauid= Entry(win2, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18")
Lauid.place(x=270,y=150)





Label (win2,text="Enter Password 	:",font=("Times New Roman",15,"bold"),
	bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=300)
Lapwd=Entry(win2, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18",show="*")
Lapwd.place(x=270,y=300)


Button(win2,text="Admin Login",width="10",height="1", font=("Times New Roman",15,"bold"),
	relief="ridge",bg="#0000ff",fg="#ffffff",command=ALogin, activebackground="green", bd=5).place(x=37, y=400)

Button(win2,text="Reset",width="10",height="1", font=("Times New Roman",15,"bold"),
	relief="ridge",bg="#808080",fg="#ffffff",command=Reset,activebackground="#728fce", bd=5).place(x=200, y=400)

Button(win2,text="Exit",width="10",height="1", font=("Times New Roman",15,"bold"),
	relief="ridge",bg="#ff0000",fg="#ffffff",command=Exit,activebackground="yellow", bd=5).place(x=360, y=400)



win2.mainloop()
