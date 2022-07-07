from distutils.cmd import Command
from itertools import count
from tkinter import *
import tkinter as tk
from typing import List 
from tkinter import messagebox 
import pypyodbc 

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=EXCALIBUR-PC;'
    'Database=Kayıtol;'
    'Trusted_Connection=True;'
)
cursor = db.cursor()
 

def giris_yap():
    pencere = Tk()
    global g_entry , g_entry1
    pencere.title(" Giriş Yap ")
    pencere.geometry("400x200")

    label=Label(pencere)
    label.config(text="E-mail Adresini giriniz.", font= ("Arial",12))
    label.place(x= 10 , y= 16 )
    
    g_entry=Entry(pencere, font="Arial 12")
    g_entry.place(x=180 , y= 20 , width= 180)

    label1=Label(pencere)
    label1.config(text="Şifrenizi giriniz.",  font = ("Arial",12))
    label1.place(x=10 , y=46)
    
    g_entry1=Entry(pencere ,show= "*" , font="Arial 12")
    g_entry1.place(x=180, y=50 , width= 120, )

    
    button = Button(pencere)
    button.config(text="Giriş yap", bg="black",fg="white", command=giris )
    button.place(x=210 , y= 130 , width=120 , height= 40)


def giris():
    e_mail = g_entry.get()
    sifre = g_entry1.get()
    girisverileri=(e_mail,sifre)    
    cursor.execute('SELECT [email],[sifre] FROM KayitGiris ')
    query = cursor.fetchall()
    
    if (query.count(girisverileri) > 0 ):
        print("Giriş başarılı")            
        pencere= Tk()
        var = messagebox.showinfo("Uyarı" , "Başarıyla giriş yapıldı.")
        pencere.destroy()
        
    else:
        print("Giriş Başarısız")
        var = messagebox.showwarning("Uyarı" , "E-Mail yada şifre yanlış lütfen kontrol ediniz.")          
   

def kayit_ol():   
    global  entry , entry1 , entry2 , entry3 , entry4
    pencere = Tk()

    pencere.title(" Kayıt Ol ")
    pencere.geometry("400x400")

    label=Label(pencere)
    label.config(text="Adınızı giriniz. ",font=("Arial",12))
    label.place(x=10,y=16) 
    
    entry=Entry(pencere, font="Arial 12")
    entry.place(x=200,y=20 , width= 110)

    label1=Label(pencere)
    label1.config(text="Soyadınızı giriniz. ", font=("Arial",12))
    label1.place(x=10 , y= 46 )

    entry1=Entry(pencere, font="Arial 12")
    entry1.place(x=200 , y=50 , width=110)

    label2=Label(pencere)
    label2.config(text="E-Mail Adresi Giriniz. ", font= ("Arial",12))
    label2.place(x=10 , y= 76 )

    entry2=Entry(pencere, font="Arial 12")
    entry2.place(x=200 , y=80 , width= 170)

    label3=Label(pencere)
    label3.config(text="Telefon Numarası Giriniz. " , font= ("Arial",12))
    label3.place(x=10 , y=106 )

    entry3=Entry(pencere, font="Arial 12")
    entry3.place(x=200 , y=110 , width=120)

    label4=Label(pencere)
    label4.config(text="Şifre giriniz.  ",  font=("Arial",12))
    label4.place(x=10 , y=136)

    entry4=Entry(pencere, show= "*" , font="Arial 12")
    entry4.place(x=200 , y=140 , width= 120 )    




    buton=Button(pencere)
    buton.config(text="KAYIT OL ",bg="black",fg="white",command=kayit)
    buton.place(x=250,y=300, width=90 , height=60)
    
    
    


def kayit():
    pencere = Tk()
    ad=entry.get()
    soyad=entry1.get()
    e_mail=entry2.get()
    telefon=entry3.get()
    sifre=entry4.get()
    
    kayit_veri=( ad, soyad , e_mail , sifre , telefon)
    ekle_komut='INSERT INTO KayitGiris (adi,soyadi,email,sifre,telefon) VALUES (?,?,?,?,?);'
    kayit_calistir = cursor.execute(ekle_komut,kayit_veri)
    db.commit()    
    var = messagebox.showinfo("Uyarı" , "Başarıyla kayıt oldunuz.")
    pencere.destroy()
    print(ad , soyad , e_mail , telefon , sifre)



def ana_menu():
    pencere = Tk()
    pencere.title(" Ana Menü ")
    pencere.geometry("600x600")
 
    uygulama = Frame(pencere)
    uygulama.grid()


 

    button1 = Button(uygulama, text = " Kayıt Ol  " , width=40,height=5, command=kayit_ol)
    button1.grid(padx=165, pady=85)

    button2 = Button(uygulama, text = " Giriş Yap " , width=40,height=5, command=giris_yap)
    button2.grid(padx=165, pady=85)
    
    pencere.mainloop()

ana_menu()

