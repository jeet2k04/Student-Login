#import module
from tkinter import *
from tkinter import messagebox
import pymysql
conobj = pymysql.connect (host = "localhost",user="root",password="",port=3308)
curobj = conobj.cursor ()
curobj.execute ('use LITCSDB;')
#curobj.execute('show databases;')
#dblist = curobj.fetchall ()
#print("data base list :",dblist)

win = Tk ()     #win is a project of Tk class
#print("--------------------------------------------")
def Exit():
        win.destroy ()
#print("--------------------------------------------")

def Reset():
        Ltype.set("Select")
        Lregno.delete(0,END)
        Lacyear.set("Select Acc Year.")
        Ldeptname.set("Select Dept.")
        Lpwd.delete(0,END)

#print("--------------------------------------------")
def Login():
        LRegno = Lregno.get ()
        LAcyear = Lacyear.get ()
        LDeptname = Ldeptname.get ()
        LPwd = Lpwd.get ()
        r=f'select * from student where SREGNO = "{LRegno}" and ACCYEAR = "{LAcyear}" and DEPT="{LDeptname}" and PASSWORD="{LPwd}";'
        curobj.execute(r)
        record=curobj.fetchall()
        if len(record):
                print("Welcome to Home Page")
                messagebox.showinfo("Login Page","Login Successfully.")
                win.destroy()
                win2= Tk()
                def Edit():
                        win2.destroy ()
                win2.minsize (500,500) #minsize (x,y)
                win2.maxsize (500,500)
                win2.title("Student Edit Page")
                win2.configure(bg="#328fce")
                Button (win2,text="Student Edit.",font=("Times New Roman",15,"bold"),
        bg="#00f",fg="#fff",relief="solid",width="15",command="Edit").place(x=20,y=250)

                win2.mainloop ()

        else :
                print("Invalid Record")
                messagebox.showinfo("Error","Try again later..")
                win.destroy()


win.minsize (500,600) #minsize (x,y)
win.maxsize (500,600)
#win.geometry ("300x400")
win.title("Login Page")
win.configure(bg="#728fce")

Label (win,text=" Student Login",font=("Algerian",25,"bold"),
        bg="#ffff00",fg="#ff0000",relief="raised",width="18").place(x=0,y=50)
Ltype = StringVar ()
Ltype.set ("Select")
Op = OptionMenu(win,Ltype, "ADMIN","FACULTY","STUDENT")
Op.place(x=390,y=50)

Label (win,text="Enter Reg Number :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=150)
Lregno= Entry(win, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18")
Lregno.place(x=270,y=150)


Label (win,text="Select Acc Year        :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=200)
Lacyear = StringVar ()
Lacyear.set("Select Acc Year.")
Op1=OptionMenu(win,Lacyear,'16-19','17-20','18-21','19-22','20-23','21-24','22-25','23-26')
Op1.place(x=270,y=200)


Label (win,text="Select Dept Name       :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=250)
Ldeptname = StringVar ()
Ldeptname.set ("Select Dept.")
Op2 = OptionMenu (win,Ldeptname, "BSc. CS(H)","BSc. ITM","BCA","BSc.DS(H)","MCA")
Op2.place(x=270,y=250)


Label (win,text="Enter Password         :",font=("Times New Roman",15,"bold"),
        bg="#ff00ff",fg="#0000ff",relief="solid",width="18").place(x=40,y=300)
Lpwd=Entry(win, font=("Calibri",15,"bold"),bg="white",fg="#000",relief="groove",width="18",show="*")
Lpwd.place(x=270,y=300)


Button(win,text="Login",width="10",height="1", font=("Times New Roman",15,"bold"),
        relief="ridge",bg="#0000ff",fg="#ffffff",command=Login, activebackground="green", bd=5).place(x=37, y=400)

Button(win,text="Reset",width="10",height="1", font=("Times New Roman",15,"bold"),
        relief="ridge",bg="#808080",fg="#ffffff",command=Reset,activebackground="#728fce", bd=5).place(x=200, y=400)

Button(win,text="Exit",width="10",height="1", font=("Times New Roman",15,"bold"),
        relief="ridge",bg="#ff0000",fg="#ffffff",command=Exit,activebackground="yellow", bd=5).place(x=360, y=400)


Label(win,text="Forgot password.",font=("Times New Roman",15,"bold"),
        bg="#728fce",fg="#f00").place(x=170,y=500)

Label(win,text="Don't have an account ?",font=("Times New Roman",15,"bold"),
        bg="#728fce",fg="#000").place(x=120,y=525)

Label(win,text="Sign up",font=("Times New Roman",15,"bold"),
        bg="#728fce",fg="#f00").place(x=330,y=525)


win.mainloop ()
