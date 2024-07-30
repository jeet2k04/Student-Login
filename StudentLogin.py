#import module 
from tkinter import * 
from tkinter import messagebox
import pymysql 
conobj = pymysql. connect ( host = "localhost", user = "root", password= "", port= 3306)
curobj = conobj .cursor () 
curobj . execute ('use pydb;')
#curobj . execute('show databases;')
#dblist = curobj. fetchall () 
#print ("data base list=", dblist)

win = Tk () # win is a object of Tk class
#print ("----------------------------------------------------")
def Exit () :
                win.destroy () 
#print ("---------------------------------------------------")
def Reset () : 
        Lregno . delete (0, END)
        Lpwd . delete(0, END)
        
#print ("-------------------------------------------------")
def Login () : 
        LRegno = Lregno. get () 
        LPwd = Lpwd .get ()
        r = f'select  * from student where regno = "{LRegno}"and spassword = "{LPwd}"; '
        curobj.execute(r)
        record = curobj.fetchall()
        if len (record) : 
                print ("welcome to home page" )
                #print (LRegno, "\t",LAcyear, "\t",LDeptname, "\t", LPwd)
                messagebox.showinfo ( "login msg","Login successfully ")
                win.destroy()
                win2 = Tk ()
                #print("---------------------------------")
                def Update ():
                        OPT1 = opt1.get()
                        OPTV1 = optv1.get()
                        OPT2 = opt2.get()
                        OPTV2 = optv2.get()
                        OPT3 = opt3.get()
                        OPTV3 = optv3.get()
                        OPT4 = opt4.get()
                        OPTV4 = optv4.get()
                        OPT5 = opt5.get()
                        OPTV5 = optv5.get()
                        OPT6 = opt6.get()
                        OPTV6 = optv6.get()
                        OPT7 = opt7.get()
                        OPTV7 = optv7.get()
                        #print(OPT1, OPTV1,OPT2, OPTV2,OPT3, OPTV3,OPT4, OPTV4,OPT5, OPTV5,OPT6, OPTV6,OPT7, OPTV7)
                        r=f'update student set sname="{OPTV1}",pname="{OPTV2}",AccYear="{OPTV3}",DeptName="{OPTV4}",Gender="{OPTV5}",Cont="{OPTV6}",spassword="{OPTV7}" where regno = "{LRegno}";'
                        curobj.execute(r)
                        conobj.commit()
                        win2.destroy()

                #print("-----------------------------------")
                def Reset ():
                        optv1.delete(0,END)
                        optv2.delete(0,END)
                        optv3.delete(0,END)
                        optv4.delete(0,END)
                        optv5.delete(0,END)
                        optv6.delete(0,END)
                        optv7.delete(0,END)
                        opt1.set("sName")
                        opt2.set("pNAme")
                        opt3.set("AccYear")
                        opt4.set("DeptName")
                        opt5.set("Gender")
                        opt6.set("ContNo")
                        opt7.set("Password")

                #print("-----------------------------------")
                def Exit ():
                        win2.destroy()
                win2.maxsize ( 500, 600) #maxsize (x, y)
                win2.minsize ( 500, 600) #maxsize (x, y)

                win2.title ("student update ")
                win2.configure (bg ="#728fce")
  
                Label (win2, text = "please update studnt information", font = ("Elephant", 18), bg ="blue", fg = "aqua", relief= "raised", width = 30). place (x= 0, y = 50)
                Label (win2, text = "My reg. num", font = ("arial", 18), bg ="green", fg = "red", relief= "raised", width = 15). place (x= 50, y = 150)
                Label (win2, text = LRegno, font = ("arial", 18), bg ="blue", fg = "aqua", relief= "raised", width = 15). place (x= 260, y = 150)

                opt1 = StringVar ()
                opt1.set ("Select Option")
                om1 = OptionMenu(win2,opt1, "SNAME","PNAME","ACC-YEAR","DEPT","GENDER","CONTACT","PASSWORD")
                om1.place(x=70,y=200)
                optv1=Entry(win2,font=("Times New Roman",20,"bold"),
                bg="white",fg="#0000ff",relief="solid",width="18")
                optv1.place(x=200,y=200)
  
                opt2 = StringVar ()
                opt2.set ("Select Option")
                om2 = OptionMenu(win2,opt1, "SNAME","PNAME","ACC-YEAR","DEPT","GENDER","CONTACT","PASSWORD")
                om2.place(x=70,y=250)
                optv2=Entry(win2,font=("Times New Roman",20,"bold"),
                bg="white",fg="#0000ff",relief="solid",width="18")
                optv2.place(x=200,y=250)

                opt3 = StringVar ()
                opt3.set ("Select Option")
                om3 = OptionMenu(win2,opt3, "SNAME","PNAME","ACC-YEAR","DEPT","GENDER","CONTACT","PASSWORD")
                om3.place(x=70,y=300)
                optv3=Entry(win2,font=("Times New Roman",20,"bold"),
                bg="white",fg="#0000ff",relief="solid",width="18")
                optv3.place(x=200,y=300)
  
                opt4 = StringVar ()
                opt4.set ("Select Option")
                om4 = OptionMenu(win2,opt4, "SNAME","PNAME","ACC-YEAR","DEPT","GENDER","CONTACT","PASSWORD")
                om4.place(x=70,y=350)
                optv4=Entry(win2,font=("Times New Roman",20,"bold"),
                bg="white",fg="#0000ff",relief="solid",width="18")
                optv4.place(x=200,y=350)
                
                opt5 = StringVar ()
                opt5.set ("Select Option")
                om5 = OptionMenu(win2,opt5, "SNAME","PNAME","ACC-YEAR","DEPT","GENDER","CONTACT","PASSWORD")
                om5.place(x=70,y=400)
                optv5=Entry(win2,font=("Times New Roman",20,"bold"),
                bg="white",fg="#0000ff",relief="solid",width="18")
                optv5.place(x=200,y=400)
  
                opt6 = StringVar ()
                opt6.set ("Select Option")
                om6 = OptionMenu(win2,opt6, "SNAME","PNAME","ACC-YEAR","DEPT","GENDER","CONTACT","PASSWORD")
                om6.place(x=70,y=450)
                optv6=Entry(win2,font=("Times New Roman",20,"bold"),
                bg="white",fg="#0000ff",relief="solid",width="18")
                optv6.place(x=200,y=450)
  
                opt7 = StringVar ()
                opt7.set ("Select Option")
                om7 = OptionMenu(win2,opt7, "SNAME","PNAME","ACC-YEAR","DEPT","GENDER","CONTACT","PASSWORD")
                om7.place(x=70,y=500)
                optv7=Entry(win2,font=("Times New Roman",20,"bold"),
                bg="white",fg="#0000ff",relief="solid",width="18")
                optv7.place(x=200,y=500)


                Button (win2, text= "Update", width= 7, height=1,font = ("Elephant", 14), relief= "groove", bg= "pink", activebackground = "green", bd = 5 ,command=Update). place       (x=40, y = 550 )

                Button (win2, text= "Reset", width= 7, height=1,font = ("Elephant", 14), relief= "groove", bg="brown", command = Reset ). place  (x=200, y = 550 )

                Button (win2, text= "Exit", width= 7, height=1,font = ("Elephant", 14), relief= "groove", bg = "red", command = Exit). place     (x=360, y = 550 )


                win2.mainloop () 
        else : 
                print ("invalid login")
                messagebox.showinfo ( "Error","Try again ")
                win.destroy() 

win.maxsize ( 500, 600) #maxsize (x, y)
win.minsize ( 500, 600) #maxsize (x, y)
#win.geometry ("300x400")
win.title ("Login Page ")
win.configure (bg ="#728fce")

Label (win, text = "!!! Student Login !!!", font = ("Elephant", 18), bg ="blue", fg = "aqua", relief= "raised", width = 20). place (x= 0, y = 50)

Label (win, text = "Enter RegNumber", font = ("Elephant", 14), bg ="#728fce", fg = "#fff300", relief= "solid",width=15). place (x= 40, y = 150)

Lregno = Entry (win , font = ("Elephant", 14),bg ="white", fg = "black", relief= "groove",width=15)
Lregno. place(x = 260, y = 150)



Label (win, text = "Enter Password", font = ("Elephant", 14), bg ="#728fce", fg = "#fff300", relief= "solid",width=15). place (x= 40, y = 300)

Lpwd = Entry (win , font = ("Elephant", 14),bg ="white", fg = "black", relief= "groove",width=15, show = "*")
Lpwd. place(x = 260, y = 300)



Button (win, text= "Login", width= 7, height=1,font = ("Elephant", 14), relief= "groove", bg= "pink", command= Login, activebackground = "green", bd = 5 ). place       (x=40, y = 400 )

Button (win, text= "Reset", width= 7, height=1,font = ("Elephant", 14), relief= "groove", bg="brown", command = Reset ). place  (x=200, y = 400 )

Button (win, text= "Exit", width= 7, height=1,font = ("Elephant", 14), relief= "groove", bg = "red", command = Exit). place     (x=360, y = 400 )

win.mainloop()
