import PIL.Image
from PIL import ImageTk
import text_to_speech as t
import pytesseract as T
import speech_recognition as s
import googletrans
import textblob
import pickle
import tkinter
from tkinter import filedialog as f
from tkinter import *
from tkinter import ttk,messagebox
from translate import Translator
import mysql.connector
import random
def moduletrans():
    W = Tk()
    W.geometry("650x300")
    W.title("Language Translator")
    photoback=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\lang_bg.png")
    photo2 = ImageTk.PhotoImage(photoback)
    L4=tkinter.Label(image=photo2)
    L4.image=photo2
    L4.pack()
    def speak():
        t.speak(Outputlang,file="Test.mp3")
    def speak1():
        t.speak(text1,file="Test.mp3")
    def speak2():
        t.speak(text,file="Test.mp3")
    def destr():
            W.destroy()
    def TRANSTAB2():
        B2.destroy()
        B3.destroy()
        Lbl11.destroy()
        Lbl12.destroy()
        global B1,language,L1L,Textbox,B5,L2L
        B1 = Button(W,text="TRANSLATE",font="Roboto 15 bold italic",activebackground="purple"
                    ,cursor="hand2",bd=5,bg="red",command=translate_now2)
        B1.place(x=350,y=160)
        
        language = googletrans.LANGUAGES
        languageV = list(language.values())
        lang1 = language.keys()
        L1L= ttk.Combobox(W,values=languageV,font="Roboto 14",state="r")
        L1L.place(x=70,y=10)
        L1L.set("ENGLISH")
        Textbox = Entry(W,font="Robote 10",bg="#00FFFF",relief=GROOVE)
        Textbox.place(x=70,y=70,width=250,height=30)
        B5=Button(W,text="Back",command=dlt2,bg="#ff9900",font=("Roboto 20 bold italic"))
        B5.place(x=170,y=155)
        L2L= ttk.Combobox(W,values=languageV,font="Roboto 14",state="r")
        L2L.place(x=380,y=10)
        L2L.set("SELECT LANGUAGE")
        TRANS()
    def TRANS():
        T.pytesseract.tesseract_cmd=r"C:\\Users\\Mayank\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
        name= f.askopenfilename()
        img=PIL.Image.open(name)
        global text
        text=T.image_to_string(img)
        Textbox.insert(0,text)
    def dlt2():
        B1.destroy()
        L1.destroy()
        Textbox.destroy()
        B5.destroy()
        L2.destroy()
        global B2,B3,Lbl11,Lbl12
        photomic=PhotoImage(file="Mc.png")
        B2=Button(W,command=TRANSTAB,image=photomic)
        B2.place(x=100,y=50)
        Lbl11=Label(W, text="TRANSLATE BY VOICE RECOGNITION ",font=("Arial",15) ,width=35)
        Lbl11.config(bg="#3709ff")
        Lbl11.place(x=200,y=70)
        photolens=PhotoImage(file="Lens.png")
        B3=tkinter.Button(W,command=TRANSTAB2,image=photolens)
        B3.place(x=100,y=150)
        Lbl12=Label(W, text="TRANSLATE BY IMAGE",font=("Arial",15) ,width=25)
        Lbl12.config(bg="#3709ff")
        Lbl12.place(x=200,y=165)
        W.configure(bg="#ADD8E6")
        W.mainloop()
    def dlt():
        B1.destroy()
        L1.destroy()
        T1.destroy()
        B5.destroy()
        L2.destroy()
        global B2,B3,Lbl11,Lbl12
        photomic=PhotoImage(file="Mc.png")
        B2=Button(W,command=TRANSTAB,image=photomic)
        B2.place(x=100,y=50)
        Lbl11=Label(W, text="TRANSLATE BY VOICE RECOGNITION ",font=("Arial",15) ,width=35)
        Lbl11.config(bg="#3709ff")
        Lbl11.place(x=200,y=70)
        photolens=PhotoImage(file="Lens.png")
        B3=tkinter.Button(W,command=TRANSTAB2,image=photolens)
        B3.place(x=100,y=150)
        Lbl12=Label(W, text="TRANSLATE BY IMAGE ",font=("Arial",15) ,width=25)
        Lbl12.config(bg="#3709ff")
        Lbl12.place(x=200,y=165)
        W.configure(bg="#ADD8E6")
        W.mainloop()
    def TRANSTAB():
        B2.destroy()
        B3.destroy()
        Lbl11.destroy()
        Lbl12.destroy()
        global B1,language,L11,T1,B5,L21
        def destr():
            W.destroy()
        B1 = Button(W,text="TRANSLATE",font="Roboto 15 bold italic",
                    activebackground="purple",cursor="hand2",bd=5,bg="red"
                    ,command=lambda:[translate_now(),destr()])
        B1.place(x=350,y=160)
        language = googletrans.LANGUAGES
        languageV = list(language.values())
        lang1 = language.keys()
        L11 = ttk.Combobox(W,values=languageV,font="Roboto 14",state="r")
        L11.place(x=70,y=10)
        L11.set("ENGLISH")
        T1 = Entry(W,font="Robote 10",bg="#00FFFF",relief=GROOVE)
        T1.place(x=70,y=70,width=250,height=30)
        B5=Button(W,text="Back",command=dlt,bg="#ff9900",font=("Roboto 20 bold italic"))
        B5.place(x=170,y=155)
        L21 = ttk.Combobox(W,values=languageV,font="Roboto 14",state="r")
        L21.place(x=380,y=10)
        L21.set("SELECT LANGUAGE")
        messagebox.showinfo("Language Translator","Listening...")
        speechrecg()
    def translate_now2():
        F = open("Translate.dat","wb")
        global Inputlang
        Inputlang = text
        text_ = Textbox.get()
        c2 = L1L.get()
        c3 = L2L.get()
        try:
            if (text_):
                words = textblob.TextBlob(text_)
                lan = words.detect_language()
                for i,j in language.items():
                    if(j==c3):
                        lan_=i
                words = words.translate(from_lang=lan,to=str(lan_))
                global Outputlang
                Outputlang = str(words)
                T = (Inputlang,Outputlang)
                pickle.dump(T,F)
                destr()
                F = open("Translate.dat","rb")
                try:
                    NW= Tk()
                    NW.geometry("650x300")
                    NW.title("Language Translator")
                    photoback=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\lang_bg.png")
                    photo2 = ImageTk.PhotoImage(photoback)
                    L4=tkinter.Label(image=photo2)
                    L4.image=photo2
                    L4.pack()
                    ima=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\speaker.png")
                    img=ImageTk.PhotoImage(ima)
                    Lab=tkinter.Button(image=img,command=speak2,bd=0)
                    Lab.image=img
                    Lab.place(x=70,y=130)
                    
                    ima1=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\speaker.png")
                    img1=ImageTk.PhotoImage(ima1)
                    Lab1=tkinter.Button(image=img1,command=speak,bd=0)
                    Lab1.image=img1
                    Lab1.place(x=380,y=100)
                    x = pickle.load(F)
                    L=Label(NW, text="INPUT WORD",font=("Arial",15) ,width=20)
                    L.config(bg="#3709ff")
                    L.place(x=30,y=30)
                    L2=Label(NW, text=x[0],font=("Arial",15) ,width=20)
                    L2.config(bg="#67d6f1")
                    L2.place(x=30,y=70)
                    L1=Label(NW, text="TRANSLATED WORD",font=("Arial",15) ,width=20)
                    L1.config(bg="#3709ff")
                    L1.place(x=350,y=30)
                    L3=Label(NW, text=x[1],font=("Arial",15) ,width=20)
                    L3.config(bg="#67d6f1")
                    L3.place(x=350,y=70)
                    label = Label(NW,text="THANK YOU",width=40,bg="yellow",font=("calibre",20,"bold"))
                    label.place(x=0,y=230)
                    def destroy():
                        NW.destroy()
                    B=Button(NW,text="Back",command=lambda:[destroy(),moduletrans()],bg="#ff9900",
                             font=("Roboto 20 bold italic"))
                    B.place(x=180,y=160)
                    B1=Button(NW,text="EXIT",command=destroy,bg="#ff9900",
                             font=("Roboto 20 bold italic"))
                    B1.place(x=340,y=160)
                    NW.mainloop()
                except EOFError:
                    F.close()
        except Exception as e:
                messagebox.showerror("GOOGLETRANS","PLEASE TRY AGAIN")
    def translate_now():
        F = open("Translate.dat","wb")
        Inputlang = T1.get()
        text_ = T1.get()
        c2 = L11.get()
        c3 = L21.get()
        if (text_):
            words = textblob.TextBlob(text_)
            lan = words.detect_language()
            for i,j in language.items():
                if(j==c3):
                    lan_=i
            words = words.translate(from_lang=lan,to=str(lan_))
            global Outputlang
            Outputlang = str(words)
            T = (Inputlang,Outputlang)
            pickle.dump(T,F)
            destr()
        F = open("Translate.dat","rb")
        try:
            NW= Tk()
            NW.geometry("650x300")
            NW.title("Language Translator")
            photoback=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\lang_bg.png")
            photo2 = ImageTk.PhotoImage(photoback)
            L4=tkinter.Label(image=photo2)
            L4.image=photo2
            L4.pack()
            ima=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\speaker.png")
            img=ImageTk.PhotoImage(ima)
            Lab=tkinter.Button(image=img,command=speak1,bd=0)
            Lab.image=img
            Lab.place(x=70,y=130)
            
            ima1=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\speaker.png")
            img1=ImageTk.PhotoImage(ima1)
            Lab1=tkinter.Button(image=img1,command=speak,bd=0)
            Lab1.image=img1
            Lab1.place(x=380,y=100)
            x = pickle.load(F)
            L=Label(NW, text="INPUT WORD",font=("Arial",15) ,width=20)
            L.config(bg="#3709ff")
            L.place(x=30,y=30)
            L2=Label(NW, text=x[0],font=("Arial",15) ,width=20)
            L2.config(bg="#67d6f1")
            L2.place(x=30,y=70)
            L1=Label(NW, text="TRANSLATED WORD",font=("Arial",15) ,width=20)
            L1.config(bg="#3709ff")
            L1.place(x=350,y=30)
            L3=Label(NW, text=x[1],font=("Arial",15) ,width=20)
            L3.config(bg="#67d6f1")
            L3.place(x=350,y=70)
            label = Label(NW,text="THANK YOU",width=40,bg="yellow",font=("calibre",20,"bold"))
            label.place(x=0,y=230)
            def destroy():
                NW.destroy()
            B=Button(NW,text="Back",command=lambda:[destroy(),moduletrans()],bg="#ff9900",
                     font=("Roboto 20 bold italic"))
            B.place(x=180,y=160)
            B1=Button(NW,text="EXIT",command=destroy,bg="#ff9900",
                     font=("Roboto 20 bold italic"))
            B1.place(x=340,y=160)
            NW.mainloop()
        except EOFError:
            F.close()
    def speechrecg():
        global text1
        r=s.Recognizer()
        with s.Microphone() as source:
            audio=r.listen(source)
        try:
            text1=r.recognize_google(audio)
            T1.delete(0,"end")
            T1.insert(0,text1)
        except:
            messagebox.showerror("Error", "Couldn't recognize your voice")
            messagebox.showinfo("Language Translator","Listening...")
            speechrecg()
    def MAINMOD():
        global B2,B3,Lbl11,Lbl12
        photomic=PhotoImage(file="Mc.png")
        B2=Button(W,command=TRANSTAB,image=photomic)
        B2.place(x=100,y=50)
        Lbl11=Label(W, text="TRANSLATE BY VOICE RECOGNITION ",font=("Arial",15) ,width=35)
        Lbl11.config(bg="#3709ff")
        Lbl11.place(x=200,y=70)
        photolens=PhotoImage(file="Lens.png")
        B3=tkinter.Button(W,command=TRANSTAB2,image=photolens)
        B3.place(x=100,y=150)
        Lbl12=Label(W, text="TRANSLATE BY IMAGE",font=("Arial",15) ,width=25)
        Lbl12.config(bg="#3709ff")
        Lbl12.place(x=200,y=165)
        def Exit():
            W.destroy()   
        Bu1=Button(W,text="EXIT",command=Exit,bg="#3709ff",font=("Arial",20),bd=5,activebackground="#3709ff")
        Bu1.place(x=260,y=220)
        W.configure(bg="#ADD8E7")
        W.mainloop()
    MAINMOD()
def loginsign():
    N=Tk()
    N.geometry("800x400")
    N.title("Language Translator")
    imgage1=PhotoImage(file="back1.png")
    Lb1=Label(N, image=imgage1)
    Lb1.pack()
    def Page1():
        global L2,PLb11,PLb12,PText1,PText2,PText3,B4,B5,B6,Lab,Labl
        B3.destroy()
        ima=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Pytrans.png")
        img=ImageTk.PhotoImage(ima)
        Lab=tkinter.Label(image=img,bd=0)
        Lab.image=img
        Lab.place(x=100,y=10)
        F=Frame(N,bg="#3d14ec", width=400, height=200, bd=0)
        F.place(x=400,y=150)
        imga=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Login.png")
        img1=ImageTk.PhotoImage(imga)
        Lbl=tkinter.Label(image=img1,bd=0)
        Lbl.image=img1
        Lbl.place(x=50,y=270)
        L2=Label(N,text="Login", bg= "yellow"
             ,font=("Arial",12,"bold"))
        L2.pack(fill=BOTH , padx=10,pady=30)
        PLb11=Label(F, text="Enter your User id ", width=20)
        PLb11.place(x=10,y=20)
        PText1=Entry(F, width=30)
        PText1.place(x=200,y=20)
        PLb12=Label(F, text="Enter your Name", width=20)
        PLb12.place(x=10,y=50)
        PText2=Entry(F, width=30)
        PText2.place(x=200,y=50)
        PLb13=Label(F, text="Enter your Password", width=20)
        PLb13.place(x=10,y=80)
        PText3=Entry(F, width=30,show="*")
        PText3.place(x=200,y=80)
        B4=Button(F,text="Login",command=Check,bg="#ff9900",font=("Arial",12))
        B4.place(x=100,y=110)
        B5=Button(F,text="Back",command=lambda:[front1(),delete1()],bg="#ff9900",font=("Arial",12))
        B5.place(x=200,y=110)
        B6=Button(F,text="Clear",bg="#ff9900",font=("Arial",12)
              ,width=6,command=clearing1)
        B6.place(x=300,y=110)
        delete()
    def delete():
        L.destroy()
        Lb11.destroy()
        Lb12.destroy()
        Text1.destroy()
        Text2.destroy()
        B1.destroy()
        B2.destroy()
        L1.destroy()
        B2.destroy()
        Ll.destroy()
    def delete1():
        Lab1.destroy()
        Lab.destroy()
        L2.destroy()
        PLb11.destroy()
        PLb12.destroy()
        PText1.destroy()
        PText2.destroy()
        B4.destroy()
        B5.destroy()
        B6.destroy()
        Lbl.destroy()
    def Check():
        count=0
        con=mysql.connector.connect(user="root",password="tiger",database="Project")
        cur=con.cursor()
        Uid=PText1.get()
        a=Uid.capitalize()
        Name=PText2.get()
        Pass=PText3.get()
        query="select * From Users where Uid='{}' and UName='{}' and Password='{}'".format(a,Name,Pass)
        cur.execute(query)
        records=cur.fetchall()
        for i in records:
            count+=1
        if PText1.get()=="" or PText2.get()=="" or PText3.get()=="": 
                messagebox.showerror("Project","Invalid Details!!!")
        else:
            if count==0:
                messagebox.showerror("Project","No such user found!!! Signup first")
                clearing1()
            else:
                 messagebox.showinfo("Project","Login successful")
                 N.destroy()
                 moduletrans()                
    def connection():
        global Text1,Text2
        con=mysql.connector.connect(user="root",password="tiger",database="project")
        cur=con.cursor()
        uname=Text1.get()
        passw=Text2.get()
        if Text1.get()=="":
            messagebox.showerror("Project","Invalid Details")
        else:
            if len(passw)>=6:
                u=random.randint(100,1000)
                a=uname[0]
                uid=a.capitalize()+str(u)
                Query="Insert into users values ('{}','{}','{}')".format(uid,uname,passw)
                q=messagebox.askquestion("Project","Do you want to Submit")
                if q=="yes":
                    messagebox.showinfo("Project","Signup done successfully!!!")
                    messagebox.showinfo("Project","Your User id is "+uid)
                    cur.execute(Query)
                    cur.execute("commit")
                    Page1()
                    delete()
                else:
                    clearing()
                con.close()
            else:
                messagebox.showerror("Project","Create a strong password (Greater than 6 characters)")
                Text2.delete("0",END)           
    def clearing():
        Text1.delete("0",END)
        Text2.delete("0",END)
    def clearing1():
        PText1.delete("0",END)
        PText2.delete("0",END)
        PText3.delete("0",END)
    def dest():
        N.destroy()
    def front1():
        global L,La,L1,Ll,Lb11,Text1,Text2,Lb12,B1,B2,B3
        image=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Pytrans.png")
        img=ImageTk.PhotoImage(image)
        L=tkinter.Label(image=img,bd=0)
        L.image=img
        L.place(x=100,y=10)
        im=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Text.png")
        img1=ImageTk.PhotoImage(im)
        La=tkinter.Label(image=img1,bd=0)
        La.image=img1
        La.place(x=15,y=200)
        i=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Signup.png")
        img2=ImageTk.PhotoImage(i)
        Ll=tkinter.Label(image=img2,bd=0)
        Ll.image=img2
        Ll.place(x=50,y=270)
        F=Frame(N,bg="#3d14ec", width=400, height=200, bd=0)
        F.place(x=400,y=150)
        L1=Label(N,text="Signup", bg= "yellow",font=("Arial",12,"bold"))
        L1.pack(fill=BOTH , padx=10,pady=30)
        Lb11=Label(F, text="Enter your name", width=20)
        Lb11.place(x=10,y=20)
        Text1=Entry(F, width=30)
        Text1.place(x=200,y=20)
        Lb12=Label(F, text="Create your Password", width=20)
        Lb12.place(x=10,y=50)
        Text2=Entry(F, width=30,show="*")
        Text2.place(x=200,y=50)
        B1=Button(F,text="Login",command=lambda:[delete(),Page1()],bg="#ff9900",font=("Arial",12))
        B1.place(x=200,y=110)
        B2=Button(F,text="Clear",bg="#ff9900",font=("Arial",12)
                  ,width=6,command=clearing)
        B2.place(x=300,y=110)
        B2=Button(F,text="Signup",bg="#ff9900",font=("Arial",12)
                  ,width=6,command=connection)
        B2.place(x=100,y=110)
        B3=Button(F,text="Back",bg="#ff9900",font=("Arial",12)
                  ,width=6,command=lambda:[dest(),Admin()])
        B3.place(x=195,y=165)
    front1()
    N.mainloop()
def Admin():
    T=Tk()
    T.geometry("485x430")
    def des():
        T.destroy()
    T.title("Language Translator")
    global L4,Bu1,Bu2
    photoback=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\logo.png")
    photo2=ImageTk.PhotoImage(photoback)
    L4=tkinter.Label(image=photo2,bd=0)
    L4.image=photo2
    L4.place(x=120,y=30)
    Bu1=Button(T,text="ADMIN",command=lambda:[des(),adminscreen()],bg="#3709ff"
               ,font=("Algerian",30),bd=5,activebackground="#3709ff")
    Bu1.place(x=60,y=320)
    Bu2=Button(T,text="USER",command=lambda:[des(),loginsign()],bg="#3709ff"
               ,font=("Algerian",30),bd=5,activebackground="#3709ff")
    Bu2.place(x=260,y=320)
    T.configure(bg="#67d6f1")
    T.mainloop()
def ADMIN():
    A=Tk()
    A.geometry("650x300")
    A.title("Language Translator")
    photoback=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\lang_bg.png")
    photo2 = ImageTk.PhotoImage(photoback)
    L4=tkinter.Label(image=photo2)
    L4.image=photo2
    L4.pack()
    def Exit():
        A.destroy() 
    B2=Button(A,text="Adding User",command=lambda:[Exit(),Insertion()],bg="#ff9900"
               ,font=("Algerian",20),bd=5,activebackground="#3709ff")
    B2.place(x=100,y=10)
    B3=Button(A,text="Updating User Details",command=lambda:[Exit(),Updation()],bg="#ff9900"
               ,font=("Algerian",20),bd=5,activebackground="#3709ff")
    B3.place(x=100,y=80)
    B3=Button(A,text="Deleting User",command=lambda:[Exit(),Deletion()],bg="#ff9900"
               ,font=("Algerian",20),bd=5,activebackground="#3709ff")
    B3.place(x=100,y=150)  
    Bu1=Button(A,text="EXIT",command=lambda:[Exit(),Admin()],bg="#3709ff",font=("Arial",20),bd=5,activebackground="#3709ff")
    Bu1.place(x=260,y=220)
    def add():
            con=mysql.connector.connect(user="root",password="tiger",database="project")
            cur=con.cursor()
            uname=Text1.get()
            passw=Text2.get()
            if Text1.get()=="" or Text2.get()=="":
                messagebox.showerror("Project","Invalid Details")
            else:
                if len(passw)>=6:
                    u=random.randint(100,1000)
                    a=uname[0]
                    uid=a.capitalize()+str(u)
                    Query="Insert into users values ('{}','{}','{}')".format(uid,uname,passw)
                    q=messagebox.askquestion("Project","Do you want to Submit")
                    if q=="yes":
                        messagebox.showinfo("Project","User Successfully Added!!!")
                        messagebox.showinfo("Project","The User id is "+uid)
                        cur.execute(Query)
                        cur.execute("commit")
    def Insertion():
        global Text1,Text2
        B=Tk()
        B.geometry("800x400")
        B.title("Language Translator")
        imgage1=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\back1.png")
        img1=ImageTk.PhotoImage(imgage1)
        Lb1=tkinter.Label(image=img1)
        Lb1.image=img1
        Lb1.pack()
        image=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Pytrans.png")
        img=ImageTk.PhotoImage(image)
        L=tkinter.Label(image=img,bd=0)
        L.image=img
        L.place(x=100,y=10)
        im=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Text.png")
        img1=ImageTk.PhotoImage(im)
        La=tkinter.Label(image=img1,bd=0)
        La.image=img1
        La.place(x=15,y=200)
        F=Frame(B,bg="#3d14ec", width=400, height=200, bd=0)
        F.place(x=400,y=150)
        L1=Label(B,text="ADDING USER", bg= "yellow",font=("Arial",12,"bold"))
        L1.pack(fill=BOTH , padx=10,pady=30)
        Lb11=Label(F, text="Enter the Name", width=20)
        Lb11.place(x=10,y=20)
        Text1=Entry(F, width=30)
        Text1.place(x=200,y=20)
        Lb12=Label(F, text="Create Password", width=20)
        Lb12.place(x=10,y=50)
        Text2=Entry(F, width=30,show="*")
        Text2.place(x=200,y=50)
        B4=Button(F,text="ADD USER",command=add,bg="#ff9900",font=("Arial",12))
        B4.place(x=50,y=110)
        B6=Button(F,text="Clear",bg="#ff9900",font=("Arial",12)
              ,width=6,command=clearing)
        B6.place(x=300,y=110)
        def Exit1():
            B.destroy()
        B3=Button(F,text="Back",bg="#ff9900",font=("Arial",12)
                  ,width=6,command=lambda:[Exit1(),ADMIN()])
        B3.place(x=195,y=110)
    def upd():
            count=0
            con=mysql.connector.connect(user="root",password="tiger",database="project")
            cur=con.cursor()
            uid=PText1.get()
            uname=Text1.get()
            passw=Text2.get()
            if Text1.get()=="" or Text2.get()=="":
                messagebox.showerror("Project","Invalid Details")
            else:
                query="select * From Users where Uid='{}'".format(uid)
                cur.execute(query)
                records=cur.fetchall()
                for i in records:
                    count=count+1
                if count>0:
                    con1=mysql.connector.connect(user="root",password="tiger",database="project")
                    cur1=con.cursor()
                    Query="Update Users Set UName='{}' , Password='{}' where Uid='{}'".format(uname,passw,uid)
                    q=messagebox.askquestion("Project","Do you want to Submit")
                    if q=="yes":
                        messagebox.showinfo("Project","User Successfully Updated!!!")
                        cur1.execute(Query)
                        cur1.execute("commit")
                else:
                    messagebox.showerror("Project","No such User Found!!!")
                    
    def Updation():
        global PText1,Text1,Text2
        B=Tk()
        B.geometry("800x400")
        B.title("Language Translator")
        imgage1=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\back1.png")
        img1=ImageTk.PhotoImage(imgage1)
        Lb1=tkinter.Label(image=img1)
        Lb1.image=img1
        Lb1.pack()
        image=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Pytrans.png")
        img=ImageTk.PhotoImage(image)
        L=tkinter.Label(image=img,bd=0)
        L.image=img
        L.place(x=100,y=10)
        im=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Text.png")
        img1=ImageTk.PhotoImage(im)
        La=tkinter.Label(image=img1,bd=0)
        La.image=img1
        La.place(x=15,y=200)
        F=Frame(B,bg="#3d14ec", width=400, height=200, bd=0)
        F.place(x=400,y=150)
        L1=Label(B,text="Updating User Details", bg= "yellow",font=("Arial",12,"bold"))
        L1.pack(fill=BOTH , padx=10,pady=30)
        PLb11=Label(F, text="Enter your User id ", width=20)
        PLb11.place(x=10,y=20)
        PText1=Entry(F, width=30)
        PText1.place(x=200,y=20)
        Lb11=Label(F, text="Update Name", width=20)
        Lb11.place(x=10,y=50)
        Text1=Entry(F, width=30)
        Text1.place(x=200,y=50)
        Lb12=Label(F, text="Update Password", width=20)
        Lb12.place(x=10,y=80)
        Text2=Entry(F, width=30,show="*")
        Text2.place(x=200,y=80)
        B4=Button(F,text="Update User",command=upd,bg="#ff9900",font=("Arial",12))
        B4.place(x=50,y=110)
        B6=Button(F,text="Clear",bg="#ff9900",font=("Arial",12)
              ,width=6,command=clearing)
        B6.place(x=300,y=110)
        def Exit2():
            B.destroy()
        B3=Button(F,text="Back",bg="#ff9900",font=("Arial",12)
                  ,width=6,command=lambda:[Exit2(),ADMIN()])
        B3.place(x=195,y=110)
    def delt():
        count=0
        con=mysql.connector.connect(user="root",password="tiger",database="project")
        cur=con.cursor()
        uid=PText1.get()
        uname=Text1.get()
        passw=Text2.get()
        if Text1.get()=="" or Text2.get()=="":
            messagebox.showerror("Project","Invalid Details")
        else:
            query="select * From Users where Uid='{}'".format(uid)
            cur.execute(query)
            records=cur.fetchall()
            for i in records:
                count=count+1
            if count>0:
                con1=mysql.connector.connect(user="root",password="tiger",database="project")
                cur1=con.cursor()
                Query="Delete From Users Where Uid='{}'".format(uid)
                q=messagebox.askquestion("Project","Do you want to Submit")
                if q=="yes":
                    messagebox.showinfo("Project","User Details Successfully Deleted!!!")
                    cur1.execute(Query)
                    cur1.execute("commit")
            else:
                messagebox.showerror("Project","No such User Found!!!")
                    
    def Deletion():
        global PText1,Text1,Text2
        B=Tk()
        B.geometry("800x400")
        B.title("Language Translator")
        imgage1=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\back1.png")
        img1=ImageTk.PhotoImage(imgage1)
        Lb1=tkinter.Label(image=img1)
        Lb1.image=img1
        Lb1.pack()
        image=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Pytrans.png")
        img=ImageTk.PhotoImage(image)
        L=tkinter.Label(image=img,bd=0)
        L.image=img
        L.place(x=100,y=10)
        im=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Text.png")
        img1=ImageTk.PhotoImage(im)
        La=tkinter.Label(image=img1,bd=0)
        La.image=img1
        La.place(x=15,y=200)
        F=Frame(B,bg="#3d14ec", width=400, height=200, bd=0)
        F.place(x=400,y=150)
        L1=Label(B,text="Deleting User", bg= "yellow",font=("Arial",12,"bold"))
        L1.pack(fill=BOTH , padx=10,pady=30)
        PLb11=Label(F, text="Enter the User id ", width=20)
        PLb11.place(x=10,y=20)
        PText1=Entry(F, width=30)
        PText1.place(x=200,y=20)
        Lb11=Label(F, text="Enter the  Name", width=20)
        Lb11.place(x=10,y=50)
        Text1=Entry(F, width=30)
        Text1.place(x=200,y=50)
        Lb12=Label(F, text="Enter the Password", width=20)
        Lb12.place(x=10,y=80)
        Text2=Entry(F, width=30,show="*")
        Text2.place(x=200,y=80)
        B4=Button(F,text="Delete User",command=delt,bg="#ff9900",font=("Arial",12))
        B4.place(x=50,y=110)
        B6=Button(F,text="Clear",bg="#ff9900",font=("Arial",12)
              ,width=6,command=clearing)
        B6.place(x=300,y=110)
        def Exit3():
            B.destroy()
        B3=Button(F,text="Back",bg="#ff9900",font=("Arial",12)
                  ,width=6,command=lambda:[Exit3(),ADMIN()])
        B3.place(x=195,y=110)
    def clearing():
        Text1.delete("0",END)
        Text2.delete("0",END)
    A.configure(bg="#ADD8E7")
    A.mainloop()
def adminscreen():
    N=Tk()
    N.geometry("800x400")
    N.title("Language Translator")
    imgage1=PhotoImage(file="back1.png")
    Lb1=Label(N, image=imgage1)
    Lb1.pack()
    def clearing1():
        PText1.delete("0",END)
        PText2.delete("0",END)
        PText3.delete("0",END)
    
    ima=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\Pytrans.png")
    img=ImageTk.PhotoImage(ima)
    Lab=tkinter.Label(image=img,bd=0)
    Lab.image=img
    Lab.place(x=100,y=10)
    F=Frame(N,bg="#3d14ec", width=400, height=200, bd=0)
    F.place(x=400,y=150)
    imga=PIL.Image.open("C:\\Users\\Mayank\\Desktop\\Final\\adminlogin.png")
    img1=ImageTk.PhotoImage(imga)
    Lbl=tkinter.Label(image=img1,bd=0)
    Lbl.image=img1
    Lbl.place(x=50,y=270)
    L2=Label(N,text="Login", bg= "yellow"
         ,font=("Arial",12,"bold"))
    L2.pack(fill=BOTH , padx=10,pady=30)
    PLb11=Label(F, text="Enter your User id ", width=20)
    PLb11.place(x=10,y=20)
    PText1=Entry(F, width=30)
    PText1.place(x=200,y=20)
    PLb12=Label(F, text="Enter your Name", width=20)
    PLb12.place(x=10,y=50)
    PText2=Entry(F, width=30)
    PText2.place(x=200,y=50)
    PLb13=Label(F, text="Enter your Password", width=20)
    PLb13.place(x=10,y=80)
    PText3=Entry(F, width=30,show="*")
    PText3.place(x=200,y=80)
    def check():
        count=0
        con=mysql.connector.connect(user="root",password="tiger",database="Project")
        cur=con.cursor()
        x=PText1.get()
        y=PText2.get()
        z=PText3.get()
        query = "SELECT * FROM ADMIN WHERE ADMName='{}' and ADMId='{}' and ADMPassword='{}'".format(y,x,z)
        cur.execute(query)
        records = cur.fetchall()
        for i in records:
            count+=1
        if PText1.get()=="" or PText2.get()=="" or PText3.get()=="": 
            messagebox.showerror("Project","Invalid Details!!!")
        else:
            if count==0:
                messagebox.showerror("Project","No such Admin found!!! ")
                clearing1()
            else:
                 messagebox.showinfo("Project","Login successful")
                 N.destroy()
                 ADMIN()
    B4=Button(F,text="Login",command=check,bg="#ff9900",font=("Arial",12))
    B4.place(x=100,y=110)
    B5=Button(F,text="Back",command=lambda:[dest(),Admin()],bg="#ff9900",font=("Arial",12))
    B5.place(x=200,y=110)
    B6=Button(F,text="Clear",bg="#ff9900",font=("Arial",12)
          ,width=6,command=clearing1)
    B6.place(x=300,y=110)
    def dest():
        N.destroy()
    N.mainloop()
def Mainscreen():
    w= Tk()
    w.geometry("485x430")
    w.title("PROJECT")
    def des():
        w.destroy()
    imgage1=PhotoImage(file="Back.png")
    Lb1=Label(w,image=imgage1,bd=0)
    Lb1.pack()
    image2=PhotoImage(file="button.png")
    Bu1=Button(w,image=image2,text="Lets Start",command=lambda:[des(),Admin()]
               ,bg="#3709ff",font=("Arial",20),bd=5,activebackground="#3709ff")
    Bu1.place(x=150,y=340)
    w.configure(bg="#67d6f1")
    w.mainloop()
Mainscreen()
