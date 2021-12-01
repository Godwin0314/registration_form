from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

window=Tk()
window.title('Registration form')
window.geometry('600x500')
window.configure(background='skyblue')

con = mysql.connect(host='localhost',user='root',password='asdfghjkl',port='3308',database='sample')

heading_lbl=Label(window,text='Student Registration Form',fg='red',font=('bold',25),bg='skyblue')
heading_lbl.place(x=100,y=20)

fname_lbl=Label(window,text='First Name',font=(25),bg='skyblue')
fname_lbl.place(x=150,y=80)

fname_txt=Entry(window)
fname_txt.place(x=260,y=87)

lname_lbl=Label(window,text='Last Name',font=(25),bg='skyblue')
lname_lbl.place(x=150,y=120)

lname_txt=Entry(window)
lname_txt.place(x=260,y=127)

age_lbl=Label(window,text='Age',font=(25),bg='skyblue')
age_lbl.place(x=150,y=160)

age_txt=Entry(window)
age_txt.place(x=260,y=167)

gender_lbl=Label(window,text='Gender',font=(25),bg='skyblue')
gender_lbl.place(x=150,y=200)

gender_txt=Entry(window)
gender_txt.place(x=260,y=207)

city_lbl=Label(window,text='City',font=(25),bg='skyblue')
city_lbl.place(x=150,y=240)

city_txt=Entry(window)
city_txt.place(x=260,y=247)

phn_num_lbl=Label(window,text='Phone Number',font=(25),bg='skyblue')
phn_num_lbl.place(x=110,y=280)

phn_num_txt=Entry(window)
phn_num_txt.place(x=260,y=287)

course_name_lbl=Label(window,text='Course Name',font=(25),bg='skyblue')
course_name_lbl.place(x=110,y=320)

course_name_txt=Entry(window)
course_name_txt.place(x=260,y=327)

def insert():
    fname = fname_txt.get()
    lname = lname_txt.get()
    age = age_txt.get()
    gender = gender_txt.get()
    city = city_txt.get()
    phn_num = phn_num_txt.get()
    course_name = course_name_txt.get()
    if fname=='' or lname=='' or age=='' or gender=='' or city=='' or phn_num=='' or course_name=='':
        MessageBox.showinfo('alert','please fill all fields')
    else:
        ex=con.cursor()
        ex.execute("insert into registration values('"+fname+"','"+lname+"','"+age+"','"+gender+"','"+city+"','"+phn_num+"','"+course_name+"')")
        ex.execute("commit")
        MessageBox.showinfo('success','Successfully Registered')
        clear_entry()

def clear_entry():
    fname_txt.delete(0,END)
    lname_txt.delete(0,END)
    age_txt.delete(0,END)
    gender_txt.delete(0,END)
    city_txt.delete(0,END)
    phn_num_txt.delete(0,END)
    course_name_txt.delete(0,END)

submit_btn=Button(window,text='Submit',command=insert,font=(25),bg='green')
submit_btn.place(x=225,y=380)

window.mainloop()
