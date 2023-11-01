#21.10.22
from tkinter import*
from PIL import ImageTk
import mysql.connector
from tkinter import ttk,messagebox
import credential as cr
import csv
import re
import random
from datetime import date

root=Tk()
root.title("↤↤↤↤↤ ˡσⓖ𝔦ℕ ↦↦↦↦↦")
root.iconbitmap("images\coronaicon.ico")
root.geometry("1200x700+0+0")

#Define Image
bg=ImageTk.PhotoImage(file="images/background.png")
bg1=ImageTk.PhotoImage(file="images/passwd.png")
bg2=ImageTk.PhotoImage(file="images\Singup.png")
bg3=ImageTk.PhotoImage(file="images\Login.png")
top_bg=ImageTk.PhotoImage(file="images/regbg.png")
top_bg1=ImageTk.PhotoImage(file="images/register.jpg")
fog_bg=ImageTk.PhotoImage(file="images/fogbg.png")
fog_bg1=ImageTk.PhotoImage(file="images/savebtn.jpg")
main_bg=ImageTk.PhotoImage(file="images\mainbg.png")
main_bg1=ImageTk.PhotoImage(file="images/assess.png")
helpline_bg=ImageTk.PhotoImage(file="images/helpline.png")
pat_bg=ImageTk.PhotoImage(file="images/coronapat.png")

#===Creating export function===
def export():
    #---extracting data from database---
    #creating database object
    mydb=mysql.connector.connect(host=cr.host,user=cr.user,passwd=cr.pas,database=cr.data)
    #creating cursor object
    mycursor=mydb.cursor()

    mycursor.execute("SELECT*FROM data")
    data_rec=mycursor.fetchall()

    mydb.close()

    with open('coronadata.csv','w',newline='') as f:
        w=csv.writer(f)
        for x in data_rec:
            w.writerow(x)
    messagebox.showinfo('Hurray!','Data Exported Successfully')

#creating helpline function----
def helpline():
    help=Toplevel()
    help.title("ᕼEᒪᑭᒪIᑎE")
    help.iconbitmap("images\coronaicon.ico")
    help.resizable(False,False)
    help.geometry("800x600")

    #---helpline level----
    he_level=Label(help,image=helpline_bg)
    he_level.pack()


#===Creating tree function===
def tree():
    tre=Toplevel()
    tre.title("ʀᴇᴄᴏʀᴅ ᴠɪᴇᴡᴇʀ")
    tre.iconbitmap("images\coronaicon.ico")

    #create treeview---
    my_tree=ttk.Treeview(tre)
    my_tree.pack()

    #Define Our columns
    my_tree['columns']=('#1','#2','#3','#4','#5','#6','#7','#8')

    #Format Our Columns
    my_tree.column('#0',width=0,stretch=NO)
    my_tree.column('#1',anchor=W,width=100)
    my_tree.column('#2',anchor=W,width=140)
    my_tree.column('#3',anchor=W,width=140)
    my_tree.column('#4',anchor=W,width=140)
    my_tree.column('#5',anchor=W,width=140)
    my_tree.column('#6',anchor=W,width=140)
    my_tree.column('#7',anchor=W,width=140)
    my_tree.column('#8',anchor=W,width=140)

    #Create Headings
    my_tree.heading('#0',text="",anchor=W)
    my_tree.heading('#1',anchor=W,text="ID")
    my_tree.heading('#2',anchor=W,text="NAME")
    my_tree.heading('#3',anchor=W,text="AGE")
    my_tree.heading('#4',anchor=W,text="GENDER")
    my_tree.heading('#5',anchor=W,text="BLOOD GROUP")
    my_tree.heading('#6',anchor=W,text="Date of ADMISSION")
    my_tree.heading('#7',anchor=W,text="ADDRESS")
    my_tree.heading('#8',anchor=W,text="Contact Number")

    #---extracting data from database---
    #creating database object
    mydb=mysql.connector.connect(host=cr.host,user=cr.user,passwd=cr.pas,database=cr.data)
    #creating cursor object
    mycursor=mydb.cursor()

    mycursor.execute("SELECT*FROM data")
    data_rec=mycursor.fetchall()

    mydb.close()
    c=0
    for x in data_rec:
        my_tree.insert(parent='',index='end',iid=c,text='',values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
        c+=1


#creating arogya function----
def arogya():
    cov=Toplevel()
    cov.title("𝓢𝓔ℒℱ  𝓐𝓢𝓢𝓔𝓢𝓢")
    cov.iconbitmap("images\coronaicon.ico")
    cov.geometry("1225x600+0+0")
    cov.configure(background='#83d5e3')
    messagebox.showinfo("Please give correct answers","Accurate answers help us-help you better.Medical and support staff are valuable and very limited.Be a responsible citizen",parent=cov)

    cov_label=Label(cov,text="Please note that your inputs will \nsupplements the efforts being taken\n to contain the corona pandemic and\n assess the Vaccination status\n symptoms.Please help us in helping\n INDIA.",bg='#642c8e',font=("Helvetica",10,"bold"),fg="White",width=40)
    cov_label.grid(row=0,column=0,pady=5)

    cov_label1=Label(cov,text="As per your registration details your  \n age.Pls confirm your age.",bg='#642c8e',font=("Helvetica",10,"bold"),fg="White",width=40)
    cov_label1.grid(row=1,column=0,pady=5)

    #----saving data into database---
    def save_data():
        if t2.get()=="" or t3.get()=="" or t7.get()=="" or t8.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=pat)
        elif not t2.get().replace(' ',"").isalpha():
            messagebox.showerror("Error!","Enter a Valid Name",parent=pat)
        elif not t3.get().isdigit():
            messagebox.showerror("Error!","Enter Valid Age",parent=pat)
        elif not t8.get().isdigit():
            messagebox.showerror("Error!","Enter 10 digit number",parent=pat)
        elif not len(t8.get())==10:
            messagebox.showerror("Error!","Enter 10 digit number",parent=pat)
        else:
            try:
                #creating database object
                mydb=mysql.connector.connect(host=cr.host,user=cr.user,passwd=cr.pas,database=cr.data)
                #creating cursor object
                mycursor=mydb.cursor()

                mycursor.execute("SELECT*FROM data where id=%s",(r,))
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error!","Try Again!",parent=pat)
                else:
                    mycursor.execute("INSERT INTO data values (%s,%s,%s,%s,%s,%s,%s,%s)",(r,t2.get(),t3.get(),t4.get(),t5.get(),d,t7.get(),t8.get()))

                    #commit changes
                    mydb.commit()
                    #closing connection
                    mydb.close()
                    messagebox.showinfo("Success!","Added Successfully!",parent=pat)
            except ConnectionError:
                messagebox.showerror("Error!","Try Again!",parent=pat)


    #----creating patient function---
    def patient():
        global pat
        cov.destroy()
        pat=Toplevel()
        pat.title("𝐀𝐝𝐝 𝐏𝐚𝐭𝐢𝐞𝐧𝐭")
        pat.iconbitmap("images\coronaicon.ico")
        pat.geometry("800x600+0+0")

        #----placing background image----
        sai=Label(pat,image=pat_bg)
        sai.place(x=0,y=0,relheight=1,relwidth=1)

        #creating frame----
        frame6=Frame(pat,bg='#eae9e8')
        frame6.pack(pady=70)

        #creating labels---
        x1=Label(frame6,text="🇵​🇦​🇹​🇮​🇪​🇳​🇹​'🇸​ 🇮​🇩​:",font=("Helvetica",20,"bold"),fg='#0085fd',bg='#eae9e8')
        x1.grid(row=0,column=0,pady=5)
        x2=Label(frame6,text="​🇳​🇦​🇲​🇪​:",font=("Helvetica",20,"bold"),fg='#0085fd',bg='#eae9e8')
        x2.grid(row=1,column=0,pady=5)
        x3=Label(frame6,text="🇦​🇬​🇪​:",font=("Helvetica",20,"bold"),fg='#0085fd',bg='#eae9e8')
        x3.grid(row=2,column=0,pady=5)
        x4=Label(frame6,text="🇬​🇪​🇳​🇩​🇪​🇷​:",font=("Helvetica",20,"bold"),fg='#0085fd',bg='#eae9e8')
        x4.grid(row=3,column=0,pady=5)
        x5=Label(frame6,text="🇧​🇱​🇴​🇴​🇩​ 🇬​🇷​🇴​🇺​🇵​:",font=("Helvetica",20,"bold"),fg='#0085fd',bg='#eae9e8')
        x5.grid(row=4,column=0,pady=5)
        x6=Label(frame6,text="🇩​🇦​🇹​🇪​ 🇴​🇫​ 🇦​🇩​🇩​🇲​🇮​🇸​🇸​🇮​🇴​🇳​:",font=("Helvetica",20,"bold"),fg='#0085fd',bg='#eae9e8')
        x6.grid(row=5,column=0,pady=5)
        x7=Label(frame6,text="🇦​🇩​🇩​🇷​🇪​🇸​🇸​:",font=("Helvetica",20,"bold"),fg='#0085fd',bg='#eae9e8')
        x7.grid(row=6,column=0,pady=5)
        x8=Label(frame6,text="🇵​🇭​🇴​🇳​🇪​ 🇳​🇴​:",font=("Helvetica",20,"bold"),fg='#0085fd',bg='#eae9e8')
        x8.grid(row=7,column=0,pady=5)
        
        global r,d,t2,t3,t4,t5,t7,t8
        #===getting patient id===
        r=str(random.randint(0,99999999))
        #===getting todays date===
        d=date.today()
        
        #---creating entryboxes---
        t1=Label(frame6,text=r,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
        t1.grid(row=0,column=1,pady=5)
        t2=Entry(frame6,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
        t2.grid(row=1,column=1,pady=5)
        t3=Entry(frame6,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
        t3.grid(row=2,column=1,pady=5)
        t4=ttk.Combobox(frame6,font=('times new roman',13),state='readonly',justify=CENTER)
        t4['values']=("MALE","FEMALE","OTHER")
        t4.grid(row=3,column=1,ipadx=10,ipady=5,pady=5)
        t4.current(0)
        t5=ttk.Combobox(frame6,font=('times new roman',13),state='readonly',justify=CENTER)
        t5['values']=("A+","A-","B+","B-","O+","O-","AB+","AB-")
        t5.grid(row=4,column=1,ipadx=10,ipady=5,pady=5)
        t5.current(0)
        t6=Label(frame6,text=d,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
        t6.grid(row=5,column=1,pady=5)
        t7=Entry(frame6,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
        t7.grid(row=6,column=1,pady=5)
        t8=Entry(frame6,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
        t8.grid(row=7,column=1,pady=5)

        man_btn=Button(pat,image=fog_bg1,command=save_data,borderwidth=0)
        man_btn.pack()

    def answer():
        if p11.get()==1 and p4.get()==1 and p9.get()==1:
            my_label=Label(cov,text='If the information provided\nby you is accurate,if \nit  indicates that you \nare either unwell or \nat risk.Please make\nyourself\n HOME QUARANTINE\n for 14 days',bg='red',font=("Helvetica",20,"bold"),fg="White")
            my_label.place(x=840,y=0)

            #^^^creating add patient button^^^
            pat_btn=Button(cov,text="Add Patient",command=patient,bg="#d89747",borderwidth=0,width=20,height=3)
            pat_btn.place(x=925,y=435)
        elif p11.get()==1 and p10.get()==1 and p9.get()==1:
            my_label=Label(cov,text='If the information provided\nby you is accurate,if \nit  indicates that you \nare either unwell or \nat risk.Please make\nyourself\n HOME QUARANTINE\n for 14 days',bg='red',font=("Helvetica",20,"bold"),fg="White")
            my_label.place(x=840,y=0)

            #^^^creating add patient button^^^
            pat_btn=Button(cov,text="Add Patient",command=patient,bg="#d89747",borderwidth=0,width=20,height=3)
            pat_btn.place(x=925,y=435)
        else:
            my_label=Label(cov,text='Your infection risk is\nlow.We recommend\nthat you stay at\nhome to avoid any\nchance of exposure\nto the Coronavirus.\nRetake the Self-Assessment\nTest if you develop\nsymptoms or come in\ncontact with a COVID-19\nconfirmed patient.Do\nvisit\n https://www.mohfw.gov.in/ \nfor more information',bg='green',font=("Helvetica",20,"bold"),fg="White")
            my_label.place(x=840,y=0)

        
    def next():
        #---making question---
        cov_label8=Label(cov,text="Do you have any of the following \n pre-existing condition?",bg='#642c8e',font=("Helvetica",10,"bold"),fg="White",width=40)
        cov_label8.grid(row=7,column=0,pady=5)

        cond=ttk.Combobox(cov,font=('times new roman',13),state='readonly',justify=LEFT)
        cond['values']=('Diabetes','Hypertension','Lung disease','Heart Disease','Kidney Disorder','Asthma','None of the Above')
        cond.grid(row=8,column=0,pady=5)
        cond.current(0)
        #----2nd question----
        cov_label9=Label(cov,text="Have you travelled in the past 14\n days to any of the states below.",bg='#642c8e',font=("Helvetica",10,"bold"),fg="White",width=40)
        cov_label9.grid(row=9,column=0,pady=5)

        place=ttk.Combobox(cov,font=('times new roman',13),state='readonly',justify=LEFT)
        place['values']=('None','Andhra Pradesh','Arunachal Pradesh','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Assam','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal')
        place.grid(row=10,column=0,pady=5)
        place.current(0)

        #---creating frame for symptoms questiion---
        frame5=Frame(cov,bg='#ed8096')
        frame5.place(x=335,y=0)
        #===creating symptoms label===
        my_label=Label(frame5,text='𝓒𝓞𝓥𝓘𝓓 𝓢𝓨𝓝𝓓𝓡𝓞𝓜𝓔 𝓐𝓝𝓐𝓛𝓨𝓢𝓘𝓢...',bg='#ed8096',font=("Helvetica",25,"bold"),fg="#0e60ca")
        my_label.pack(pady=5)
        global p2,p3,p4,p5,p6,p7,p8,p9,p10,p11
        #---checkbox button---
        p2=IntVar()
        c2=Checkbutton(frame5,text='(っ◔◡◔)っ Are you having normal cough?',variable=p2,font=("Helvetica",15,"bold"),fg="#0e60ca",bg='#ed8096')
        c2.pack()

        p3=IntVar()
        c3=Checkbutton(frame5,text="˜”*°•.˜”*°• Are you having dry cough? •°*”˜.•°*”˜",variable=p3,font=("Helvetica",15,"bold"),fg="#0e60ca",bg='#ed8096')
        c3.pack()

        p4=IntVar()
        c4=Checkbutton(frame5,text='𝘈𝘳𝘦 𝘺𝘰𝘶 𝘩𝘢𝘷𝘪𝘯𝘨 𝘸𝘦𝘵 𝘤𝘰𝘶𝘨𝘩 𝘸𝘪𝘵𝘩 𝘮𝘶𝘤𝘶𝘴?',variable=p4,font=("Helvetica",15,"bold"),fg="#0e60ca",bg='#ed8096')
        c4.pack()

        p5=IntVar()
        c5=Checkbutton(frame5,text='✧∰✧[ Do you have runny Nose? ]✧∰✧',variable=p5,font=("Helvetica",15,"bold"),fg="#0e60ca",bg='#ed8096')
        c5.pack()
        
        p6=IntVar()
        c6=Checkbutton(frame5,text='🇦​🇷​🇪​ 🇾​🇴​🇺​ 🇸​🇳​🇪​🇪​🇿​🇮​🇳​🇬​ 🇹​🇴​🇴​ 🇲​🇺​🇨​🇭​?',variable=p6,font=("Helvetica",15,"bold"),fg="#0e60ca",bg='#ed8096')
        c6.pack()

        p7=IntVar()
        c7=Checkbutton(frame5,text='A̲r̲e̲ ̲y̲o̲u̲ ̲h̲a̲v̲i̲n̲g̲ ̲d̲i̲f̲f̲i̲c̲u̲l̲t̲y̲ ̲i̲n̲ ̲b̲r̲e̲a̲t̲h̲i̲n̲g̲?̲',variable=p7,font=("Helvetica",15,"bold"),fg="#0e60ca",bg='#ed8096')
        c7.pack()

        p8=IntVar()
        c8=Checkbutton(frame5,text='✎﹏﹏Are you feeling body ache?﹏﹏',variable=p8,font=("Helvetica",15,"bold"),fg="#0e60ca",bg='#ed8096')
        c8.pack()

        p9=IntVar()
        c9=Checkbutton(frame5,text='╰☆☆ Are you feeling weak and tired? ☆☆╮',variable=p9,font=("Helvetica",15,"bold"),fg="#0e60ca",bg='#ed8096')
        c9.pack()

        p10=IntVar()
        c10=Checkbutton(frame5,text='(★) Are you having fever? (★)',variable=p10,font=("Helvetica",15,"bold"),fg="#0e60ca",bg='#ed8096')
        c10.pack()

        p11=IntVar()
        c11=Checkbutton(frame5,text='🇭​🇦​🇻​🇪​ 🇾​🇴​🇺​ 🇱​🇴​🇸​🇹​ 🇾​🇴​🇺​ 🇹​🇦​🇸​🇹​🇪​ 🇦​🇳​🇩​ 🇸​🇲​🇪​🇱​🇱​?',variable=p11,font=("Helvetica",20,"bold"),fg="#0e60ca",bg='#ed8096')
        c11.pack()

        con_btn=Button(cov,text="Submit",command=answer,bg="#89b204",borderwidth=0,width=20,height=3)
        con_btn.place(x=525,y=435)

    def vac():
        try:
            int(cov_age.get())
            cov_label3=Label(cov,text="Have you taken the vaccination?      ",bg='#642c8e',font=("Helvetica",10,"bold"),fg="White",width=40)
            cov_label3.grid(row=4,column=0,pady=5)

            p1=ttk.Combobox(cov,font=('times new roman',13),state='readonly',justify=LEFT)
            p1['values']=("Yes",'No')
            p1.grid(row=5,column=0,pady=5)
            p1.current(0)
            #---creating a next button---
            next_btn=Button(cov,text="Next",command=next,bg="#83d5e3",borderwidth=0)
            next_btn.grid(row=6,column=0)
        except ValueError:
            messagebox.showerror("Error","Enter Valid Age",parent=cov)
    global  cov_age
    cov_age=Entry(cov,bg="#d3b3aa",fg="#070000",font=('Consolas',15),justify=LEFT)
    cov_age.grid(row=2,column=0,pady=5)

    go_btn=Button(cov,text="Go",command=vac,bg="#83d5e3",borderwidth=0)
    go_btn.grid(row=3,column=0)

    #

#=====creating view function====
def view():
    root.withdraw()
    global main
    main=Toplevel()
    main.title("𝑀𝐸𝒩𝒰")
    main.iconbitmap("images\coronaicon.ico")
    main.geometry("800x600+0+0")

    #----placing background image----
    lm=Label(main,image=main_bg)
    lm.place(x=0,y=0,relheight=1,relwidth=1)
    #---back function---
    def back():
        main.destroy()
        root.deiconify()

    #----back to login btn----
    lbtn=Button(main,text="ＢＡＣＫ",bg="red",fg="black",command=back)
    lbtn.grid(row=0,column=0,ipadx=10,ipady=5)

    #creating frame----
    frame3=Frame(main,bg='#35403c')
    frame3.place(x=105,y=70)

    #------title----
    main_label=Label(frame3,text="𝓦𝓔𝓛𝓒𝓞𝓜𝓔 𝓣𝓞 𝓜𝓐𝓘𝓝 𝓜𝓔𝓝𝓤",bg='#35403c',font=("Helvetica",30,"bold"),fg="Orange")
    main_label.grid(row=0,column=0)

    #===creating ASSESS again btn===
    view_btn=Button(frame3,image=main_bg1,bg='#35403c',command=arogya)
    view_btn.grid(row=1,column=0,pady=20)

    #----creating btn to view record----
    rec_btn=Button(frame3,text='𝒱𝐼𝐸𝒲 𝑅𝐸𝒞𝒪𝑅𝒟',bg='#f6dba1',command=tree)
    rec_btn.grid(row=2,column=0,pady=20,ipadx=41,ipady=23)

    #----creating btn to export record----
    exe_btn=Button(frame3,text='𝙀𝙭𝙥𝙤𝙧𝙩 𝘿𝙖𝙩𝙖',bg='#dbd9d4',command=export)
    exe_btn.grid(row=3,column=0,pady=20,ipadx=48,ipady=21)
    
    #----creating helpline btn----
    he_btn=Button(frame3,text='𝐻𝑒𝓁𝓅𝓁𝒾𝓃𝑒',bg='#6cb601',command=helpline)
    he_btn.grid(row=4,column=0,pady=20,ipadx=54,ipady=21)

    #_______Quit button------
    qbtn=Button(main,text=" Ｑ Ｕ Ｉ Ｔ ",bg="orange",fg="black",command=root.destroy)
    qbtn.place(x=720,y=575)
#------forgot function---
def forgot():
    fog=Toplevel()
    fog.title("F*** PASSWORD")
    fog.iconbitmap("images\coronaicon.ico")
    fog.geometry("550x550")

    #====Background Image===
    lf=Label(fog,image=fog_bg)
    lf.place(x=0,y=0,relheight=1,relwidth=1)
    global email_fog,passw_fog,use_fog
    #====Creating save function===
    def save():
        if email_fog.get()=="" or passw_fog.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=fog)
        else:
            try:
                #creating database object
                mydb=mysql.connector.connect(host=cr.host,user=cr.user,passwd=cr.pas,database=cr.data)
                #creating cursor object
                mycursor=mydb.cursor()

                mycursor.execute("SELECT*FROM register WHERE email=%s and username=%s",(email_fog.get(),use_fog.get()))
                row=mycursor.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "Email Id doesn't exists or username doesnot match",parent=fog)
                    mydb.close()
                else:
                    mycursor.execute("UPDATE register SET password=%s WHERE email=%s",(passw_fog.get(),email_fog.get()))
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo("Successful", "Password has changed successfully",parent=root)
            except EOFError:
                messagebox.showerror("Error","Sorry",parent=root)

    #------forgot password frame
    frame2=Frame(fog,bg='#a5d3f4')
    frame2.place(x=38,y=100)

    #------title----
    tit=Label(frame2,text="𝓒𝓱𝓪𝓷𝓰𝓮 𝓟𝓪𝓼𝓼𝔀𝓸𝓻𝓭",bg="#a5d3f4",font=("Helvetica",40,"bold"),fg="Blue")
    tit.grid(row=0,column=0,columnspan=2,pady=5)

    #-----email----
    ema=Label(frame2,text="𝐸𝑀𝒜𝐼𝐿",bg='#a5d3f4',font=("Helvetica",20,"bold"),fg="#ec0b0c")
    ema.grid(row=2,column=0,pady=5)
    email_fog=Entry(frame2,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
    email_fog.grid(row=2,column=1,pady=5)

    #-----username----
    use=Label(frame2,text="𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦",bg='#a5d3f4',font=("Helvetica",20,"bold"),fg="#ec0b0c")
    use.grid(row=3,column=0,pady=5)
    use_fog=Entry(frame2,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
    use_fog.grid(row=3,column=1,pady=5)

    #=====forgot  password entry....
    pa=Label(frame2,text="𝙽𝚎𝚠 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍",bg='#a5d3f4',font=("Helvetica",20,"bold"),fg="#ec0b0c")
    pa.grid(row=4,column=0,pady=5)
    passw_fog=Entry(frame2,bg="#d3b3aa",fg="#070000",font=('Consolas',15),show='*')
    passw_fog.grid(row=4,column=1,pady=5)

    #-------Save Button----
    fbtn=Button(frame2,image=fog_bg1,command=save,borderwidth=0)
    fbtn.grid(row=5,column=0,columnspan=2)

def login():
    if elabel_.get()=="" or plabel_.get()=="":
        messagebox.showerror("Error!","All fields are required",parent=root)
    else:
        try:
            #creating database object
            mydb=mysql.connector.connect(host=cr.host,user=cr.user,passwd=cr.pas,database=cr.data)
            #creating cursor object
            mycursor=mydb.cursor()

            mycursor.execute("SELECT*FROM register where email=%s and password=%s",(elabel_.get(),plabel_.get()))
            row=mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error!","Invalid USERNAME & PASSWORD",parent=root)
            else:
                messagebox.showinfo("Success","Wellcome to the Covid Diagnosis",parent=root)
                mydb.close()
                view()
        except EOFError:
            messagebox.showerror("Error","Sorry",parent=root)


def singup():
    #root.withdraw()
    top=Toplevel()
    top.title("REGISTRATION")
    top.iconbitmap("images\coronaicon.ico")
    top.geometry("1200x700+0+0")
    #====Background Image===
    l=Label(top,image=top_bg)
    l.place(x=0,y=0,relheight=1,relwidth=1)

    global fname_E,lname_E,contact_E,email_E,age_E,gender_C,passw_E,cpassw_E

    def register_data():
        econd="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if fname_E.get()=="" or lname_E.get()=="" or contact_E.get()=="" or email_E.get()=="" or age_E.get()=="" or passw_E.get()=="" or cpassw_E.get()=="":
            messagebox.showerror("Error!","All Fields are Required!",parent=top)
        elif not fname_E.get().replace(' ',"").isalpha():
            messagebox.showerror("Error!","Enter a Valid Name",parent=top)
        elif not contact_E.get().isdigit():
            messagebox.showerror("Error!","Enter 10 digit number",parent=top)
        elif not len(contact_E.get())==10:
            messagebox.showerror("Error!","Enter 10 digit number",parent=top)
        elif not re.search(econd,email_E.get()):
            messagebox.showerror("Error!","Enter Valid Email",parent=top)
        elif not age_E.get().isdigit():
            messagebox.showerror("Error!","Enter Valid Age",parent=top)
        elif len(age_E.get())>2:
            messagebox.showerror("Error!","Enter Valid Age",parent=top)
        elif passw_E.get()!=cpassw_E.get():
            messagebox.showerror("Error!","Password Didn't Match!",parent=top)
        elif len(cpassw_E.get())<8:
            messagebox.showerror("Error!","Make your password more than 8 character!",parent=top)
        else:
            try:
                #creating database object
                mydb=mysql.connector.connect(host=cr.host,user=cr.user,passwd=cr.pas,database=cr.data)
                #creating cursor object
                mycursor=mydb.cursor()

                mycursor.execute("SELECT*FROM register where email=%s",(email_E.get(),))
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error!","Email already exists",parent=top)
                else:
                    mycursor.execute("INSERT INTO register (name,username,contact,email,age,gender,password) values (%s,%s,%s,%s,%s,%s,%s)",(fname_E.get(),lname_E.get(),contact_E.get(),email_E.get(),age_E.get(),gender_C.get(),passw_E.get()))

                    #commit changes
                    mydb.commit()
                    #closing connection
                    mydb.close()
                    messagebox.showinfo("Success!","Registration Completed!",parent=root)
            except EOFError:
                messagebox.showerror("Error","Sorry",parent=root)

    #===Register Frame===
    frame1=Frame(top,bg="#ffffff")
    frame1.place(x=430,y=50)

    #===TITLE...
    tlabel=Label(frame1,text="𝓡𝓮𝓰𝓲𝓼𝓽𝓮𝓻 𝓗𝓔𝓡𝓔...",bg="#ffffff",font=("Helvetica",40,"bold"),fg="Blue")
    tlabel.grid(row=0,column=0,columnspan=2,pady=5)

    #---full name
    fname=Label(frame1,text="𝗙𝘂𝗹𝗹 𝗡𝗮𝗺𝗲",bg='#ffffff',font=("Helvetica",20,"bold"),fg="#ec0b0c")
    fname.grid(row=1,column=0,pady=5)
    fname_E=Entry(frame1,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
    fname_E.grid(row=1,column=1,pady=5)

    #===user Name===
    lname=Label(frame1,text="𝕦𝕤𝕖𝕣𝕟𝕒𝕞𝕖",bg='#ffffff',font=("Helvetica",20,"bold"),fg="#ec0b0c")
    lname.grid(row=2,column=0,pady=5)
    lname_E=Entry(frame1,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
    lname_E.grid(row=2,column=1,pady=5)
    
    #---Contact---
    contact=Label(frame1,text="𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐍𝐨",bg='#ffffff',font=("Helvetica",20,"bold"),fg="#ec0b0c")
    contact.grid(row=3,column=0,pady=5)
    contact_E=Entry(frame1,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
    contact_E.grid(row=3,column=1,pady=5)

    #--------Email
    email=Label(frame1,text="𝐸𝑀𝒜𝐼𝐿",bg='#ffffff',font=("Helvetica",20,"bold"),fg="#ec0b0c")
    email.grid(row=4,column=0,pady=5)
    email_E=Entry(frame1,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
    email_E.grid(row=4,column=1,pady=5)

    #===Age===
    age=Label(frame1,text="A̲G̲E̲",bg='#ffffff',font=("Helvetica",20,"bold"),fg="#ec0b0c")
    age.grid(row=5,column=0,pady=5)
    age_E=Entry(frame1,bg="#d3b3aa",fg="#070000",font=('Consolas',15))
    age_E.grid(row=5,column=1,pady=5)

    #------Gender
    gender=Label(frame1,text="ᴳᴱᴺᴰᴱᴿ",bg='#ffffff',font=("Helvetica",20,"bold"),fg="#ec0b0c")
    gender.grid(row=6,column=0,pady=5)
    gender_C=ttk.Combobox(frame1,font=('times new roman',13),state='readonly',justify=CENTER)
    gender_C['values']=("MALE","FEMALE","OTHER")
    gender_C.grid(row=6,column=1,ipadx=10,ipady=5)
    gender_C.current(0)

    #-----password-----
    passw=Label(frame1,text="𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥",bg='#ffffff',font=("Helvetica",20,"bold"),fg="#ec0b0c")
    passw.grid(row=7,column=0,pady=5)
    passw_E=Entry(frame1,bg="#d3b3aa",fg="#070000",font=('Consolas',15),show='*')
    passw_E.grid(row=7,column=1,pady=5)

    #----confirm password---
    cpassw=Label(frame1,text="ᶜᵒⁿᶠⁱʳᵐ ᴾᵃˢˢʷᵒʳᵈ",bg='#ffffff',font=("Helvetica",15,"bold"),fg="#ec0b0c")
    cpassw.grid(row=8,column=0,pady=5)
    cpassw_E=Entry(frame1,bg="#d3b3aa",fg="#070000",font=('Consolas',15),show='*')
    cpassw_E.grid(row=8,column=1,pady=5)

    #Register button with image
    rbtn=Button(frame1,image=top_bg1,command=register_data)
    rbtn.grid(row=9,column=0,columnspan=2)

myl=Label(root,image=bg)
myl.place(x=0,y=0,relheight=1,relwidth=1)

#create a frame
mframe=Frame(root,bg="#f07741")
mframe.place(x=430,y=50)

mylabel=Label(mframe,text="𝓛𝓞𝓖𝓘𝓝 𝓗𝓔𝓡𝓔...",bg="#f07741",font=("Helvetica",40,"bold"),fg="Blue")
mylabel.grid(row=0,column=0,columnspan=2)

#creating labels
elabel=Label(mframe,text="ₑₘₐᵢₗ ₐddᵣₑₛₛ",bg="#f07741",font=("Helvetica",20,"bold"),fg="green")
elabel.grid(row=1,column=0,columnspan=2)
plabel=Label(mframe,text="ℙ𝔸𝕊𝕊𝕎𝕆ℝ𝔻",bg="#f07741",font=("Helvetica",20,"bold"),fg="#000003")
plabel.grid(row=3,column=0,columnspan=2)

#creating entry boxes
global elabel_,plabel_

elabel_=Entry(mframe,width=50,bg="#d3b3aa",fg="#070000",font=('Consolas',10))
elabel_.grid(row=2,column=0,columnspan=2)
plabel_=Entry(mframe,width=50,bg="#d3b3aa",fg="#070000",font=('Consolas',10),show='*')
plabel_.grid(row=4,column=0,columnspan=2,pady=10)

#Creating buttton...
fbtn=Button(root,image=bg1,borderwidth=0,command=forgot)
fbtn.place(x=450,y=250)
cbtn=Button(root,image=bg2,borderwidth=0,command=singup)
cbtn.place(x=650,y=250)
lbtn=Button(root,image=bg3,borderwidth=0,command=login)
lbtn.place(x=525,y=300)

root.mainloop()