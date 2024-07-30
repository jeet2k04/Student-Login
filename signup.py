#import module
from tkinter import *
from tkinter import messagebox
import pymysql
conobj = pymysql.connect (host = "localhost",user="root",password="",port=3306)
curobj = conobj.cursor ()
curobj.execute ('use LITCSDB;')
#curobj.execute('create table student (SNAME varchar(30),PNAME varchar(30),SREGNO char(20)primary key,SGENDER varchar(3),SCONCT varchar(10),ACCYEAR varchar(10),DEPT varchar(10),PASSWORD varchar(16));')


win1 = Tk ()    #win1 is a project of Tk class
#print("--------------------------------------------")
def Submit ():
        rsname= RSname.get ()
        rpname= RPname.get ()
        rrno= RRno.get ()
        gender= Gender.get ()
        rscno= RSCno.get ()
        racyear= Racyear.get ()
        rdeptname= Rdeptname.get ()
        rpwd= Rpwd.get ()
        r='insert into student values("{}","{}","{}","{}","{}","{}","{}","{}");'
        r1=r.format(rsname,rpname,rrno,gender,rscno,racyear,rdeptname,rpwd)
        messagebox.showinfo("Inserted", "Insert record Successfully..")
        curobj.execute(r1)
        conobj.commit()
        curobj.close()
        conobj.close()
        win1.destroy ()
        #print(r1)
        #print(rsname,rpname,rrno,rscno,rpwd,racyear,rdeptname,gender)
#print("--------------------------------------------")
def RSet() :
        RSname.delete(0,END)
        RPname.delete(0,END)
        RRno.delete(0,END)
        Gender.set(None)
        RSCno.delete(0,END)
        Racyear.set("Select Acc Year")
        Rdeptname.set("Select Dept. Name")
        Rpwd.delete(0,END)
#print("--------------------------------------------")
def RExit() :
        win1.destroy ()

win1.minsize (500,700) #minsize (x,y)
win1.maxsize (500,700)
#win1.geometry ("300x400")
win1.title("Student Registration Page")
win1.configure(bg="#728fce")

Label (win1,text="!!!Student Registration!!!",font=("Algerian",25,"bold"),
        bg="#ffff00",fg="#ff0000",relief="raised",width="25").place(x=0,y=50)

Label (win1,text="Enter Student Name :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=150)
RSname= Entry(win1, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18")
RSname.place(x=270,y=150)

Label (win1,text="Enter Parents Name :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=200)
RPname= Entry(win1, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18")
RPname.place(x=270,y=200)

Label (win1,text="Enter Student Regno :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=250)
RRno= Entry(win1, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18")
RRno.place(x=270,y=250)

Label (win1,text="Select Gender :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=300)
Gender = StringVar ()
Radiobutton (win1, text="Male",variable=Gender,value="M").place(x=270,y=300)
Radiobutton (win1, text="Female",variable=Gender,value="F").place(x=370,y=300)


Label (win1,text="Contactno :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=350)
RSCno= Entry(win1, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18")
RSCno.place(x=270,y=350)


Label (win1,text="Select Acc Year       :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=400)
Racyear = StringVar ()
Racyear.set("Select Acc Year.")
Op1=OptionMenu(win1,Racyear,'16-19','17-20','18-21','19-22','20-23','21-24','22-25','23-26')
Op1.place(x=270,y=400)


Label (win1,text="Select Dept. Name     :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=450)
Rdeptname = StringVar ()
Rdeptname.set ("Select Dept. Name")
Op2 = OptionMenu (win1,Rdeptname, "BSc. CS(H)","BSc. ITM","BCA","BSc.DS(H)","MCA")
Op2.place(x=270,y=450)


Label (win1,text="Enter Password        :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=500)
Rpwd=Entry(win1, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18",show="*")
Rpwd.place(x=270,y=500)


Button(win1,text="Submit",width="10",height="1", font=("Times New Roman",15,"bold"),
        relief="ridge",bg="#0000ff",fg="#ffffff",command=Submit, activebackground="green", bd=5).place(x=37, y=600)

Button(win1,text="Reset",width="10",height="1", font=("Times New Roman",15,"bold"),
        relief="ridge",bg="#808080",fg="#ffffff",command=RSet,activebackground="#728fce", bd=5).place(x=200, y=600)

Button(win1,text="Exit",width="10",height="1", font=("Times New Roman",15,"bold"),
        relief="ridge",bg="#ff0000",fg="#ffffff",command=RExit,activebackground="yellow", bd=5).place(x=360, y=600)


win1.mainloop()
