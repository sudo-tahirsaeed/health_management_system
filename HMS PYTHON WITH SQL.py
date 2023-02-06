from tkinter import *
from time import strftime
from tkinter import messagebox as msg
import time
from datetime import date
from datetime import time
def files():
    global a
    global current
    active = open("active.txt", 'a')
    active = open("active.txt", 'r')
    if active.readline()=='':
        active.close()
        active=open("active.txt",'w')
        active.write("0")
    active = open("active.txt", 'r')
    a=active.readline()
    current.config(text="Active Patients: "+a + " ")
    current.after(1000,files)
def time1():
    global lbl
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time1)
def backnp():
    global fnewpatient
    fnewpatient.destroy()
def saved():
    global cnict
    global namet
    global f
    global lbl
    global a
    global fnewpatient
    global newp
    global search
    global current
    global new
    global diagnose

    global diagnoseb
    name=namet.get()
    cnic = cnict.get()
    diagnoseg=diagnose.get()
    bed=diagnoseb.get()
    if name!='' and cnic!='' and diagnoseg!='':
        if cnic.isnumeric() and len(cnic)==13 :
            j=open(cnic+'.txt','w')
            j.write('Name: '+ name+'\n')
            j.write('CNIC: '+ cnic+"\n")
            j.write('Diagnose: ' + diagnoseg+'\n')
            a3=date.today()
            d2 = a3.strftime("%B %d, %Y")
            string = strftime('%H:%M:%S %p')
            j.write("Bed No: " + str(bed)+"\n")
            j.write("Admitted on: "+ str(d2) + " At "+ str(string) )
            j.close()
            j=open("active.txt",'r')
            x=int(j.readline())
            j.close()
            xx=str(x+1)
            jj=open("active.txt", 'w')
            jj.write(xx)
            jj.close()
            msg.showinfo('Saved Sucessfully', 'Record for the patient Saved Sucessfully ')
            fnewpatient.destroy()
        else:
            msg.showerror('Error','CNIC can be only 13 digit number without dashes')
    else:
        msg.showerror('Error', 'Please fill all fields and try Again ')
def searchf():
    global f
    global searchrecord
    global namet
    global cnics
    searchrecord=Frame(f)
    searchrecord.config(bg='gray')
    searchrecord.pack(expand=TRUE,fill=BOTH)
    la=Label(searchrecord,text="SEARCH RECORD OF PATIENT FROM DATABASE",font="Comic 15 bold", bg='black', fg="yellow")
    la.place(x=145,y=45)
    lp = Label(searchrecord, text="Enter Cnic: ", font="arial 15 bold", bg='orange', fg="black")
    lp.place(x=160, y=121)
    cnics = Entry(searchrecord, width=40, font="arial 12 bold")
    cnics.place(x=282, y=121, height=29)
    srb = Button(searchrecord, bg='blue', fg='yellow', font='arial 10 bold', text="SEARCH", width=15,command=lambda:srdata())
    srb.place(x=400, y=165)
    backs = Button(searchrecord, bg='black',command=lambda : backs1(),fg='yellow', font='arial 10 bold', text="Back", width=10)
    backs.place(x=300, y=165)
def srdata():
    global f
    global searchrecord
    global foundrecord
    global cnics
    no=cnics.get()
    if no.isnumeric():
# DONT TOUCH THIS PART IT JUST WORKS SAMJ MUJY B NAHI HOW IT DOES xD
        if len(no)==13:
            searchrecord.destroy()
            try:
                f1=open(no+".txt",'r')

                foundrecord=Frame(f)
                foundrecord.config(bg='gray')
                foundrecord.pack(expand=TRUE, fill=BOTH)
                la = Label(foundrecord, text=" RECORD FOUND ", font="Comic 20 bold", bg='black',
                           fg="yellow")
                la.place(x=275, y=45)
                text=Text(foundrecord,width=55,bg='black',fg='white',font="Digital 12 bold ",height=15)
                while TRUE:
                    x=str(f1.readline())
                    if x=='':
                        break
                    text.insert("end","\n"+"\t    "+ x)
                text.insert("end", "\n\n" + "  " + "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")

                text.config(state='disabled')
                text.place(x=160,y=90)
                f1.close()
            except Exception as s:
                print(s)
                msg.showerror("Error","NO RECORD FOUND")
        else:
            msg.showerror("Error", "CNIC can't be less or grater than 13 digits")
    else:
        msg.showerror("Error","CNIC CAN ONLY CONTAIN 13 DIGITS")
    home = Button(foundrecord, bg='green', fg='yellow', font='arial 10 bold', text="GO TO HOME", width=15, command=lambda: home1())
    home.place(x=350, y=390)
def home1():
    global fnewpatient
    global searchrecord
    global foundrecord

    foundrecord.destroy()


def backs1():
        global searchrecord
        searchrecord.destroy()
def newp():
    global f
    global lbl
    global a
    global fnewpatient
    global newp
    global search
    global current
    global new
    global cnict
    global namet
    global diagnose
    global diagnoseb
    fnewpatient = Frame(f)
    fnewpatient.config(bg="grey")

    fnewpatient.pack(fill=BOTH, expand=TRUE)
    na=Label(fnewpatient,text="Patient Name: ",font="arial 13 bold")
    na.config(bg='orange')
    na.place(x=140,y=180)
    cnic = Label(fnewpatient, text="Patient CNIC:  ", font="arial 13 bold")
    cnic.config(bg='orange' )
    cnic.place(x=140, y=220)

    dig = Label(fnewpatient, text="   Diagnose:    ", font="arial 13 bold")
    dig.config(bg='orange')
    dig.place(x=140, y=260)

    bedno = Label(fnewpatient, text="   Bed No:    ", font="arial 13 bold")
    bedno.config(bg='orange')
    bedno.place(x=140, y=300)

    namet=Entry(fnewpatient,width=40,font="arial 12 bold")
    namet.place(x=275,y=180,height=25)
    cnict=Entry(fnewpatient,width=40,font="arial 12 bold")
    cnict.place(x=275,y=220,height=25)
    diagnose = Entry(fnewpatient, width=40, font="arial 12 bold")
    diagnose.place(x=275, y=260, height=25)
    diagnoseb = Entry(fnewpatient, width=40, font="arial 12 bold")
    diagnoseb.place(x=275, y=300, height=25)

    saveb=Button(fnewpatient,bg='red',fg='yellow',font='arial 10 bold',text="Save",width=15,command=lambda : saved())
    saveb.place(x=430, y=345)
    backn = Button(fnewpatient, bg='black', fg='yellow', font='arial 10 bold', text="Back", width=10, command=lambda: backnp())
    backn.place(x=300, y=345)
    fnewpatient.pack()
def gui():
    global lbl
    global ta
    global a
    global f
    global fnewpatient
    global topl
    global new
    global search
    global current

    ta=Tk()
    f=Frame(ta)
    f.config(bg="grey")
    f.pack(fill=BOTH,expand=TRUE)
    ta.title("Hospital Management System - Tahir Saeed / Shehryar / Mamoon")
    ta.geometry("750x680")
    ta.config(bg="gray")
    lbl=Label(f,bg='black',font="digital 20",fg="green")
    lbl.place(x=10,y=90)
    topl=Label(f,bg='cyan',fg='red',font="Verdana 25 bold",text="HOSPITAL MANAGEMENT SYSTEM")
    topl.pack(side=TOP,fill=X)
    topl2 = Label(f, bg='cyan', fg='black', font="Calibiri 12 bold ", text="Developed by Tahir Saeed / Shehryar / Mamoon")
    topl2.pack(side=TOP, fill=X)
    new=Button(f,command=lambda : newp(),bg='yellow',fg='black',font="Arial 16 bold",text="ENTER NEW PATIENT",relief="solid")
    new.place(x=260,y=200)
    search = Button(f,bg='yellow',command=lambda : searchf(),fg='black', font="Arial 16 bold", text="   SEARCH  RECORD  ",relief="solid")
    search.place(x=260, y=270)
    current = Label(f, bg='magenta', font="Arial 12 bold", fg="black")
    current.place(x=10, y=150)
    time1()
    files()
    ta.mainloop()
gui()