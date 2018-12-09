
from easygui import *
from tkinter import *
#from tkinter import ttk # platvormi ühise stiili saamiseks
#from tkinter import messagebox
from datetime import datetime
import tkinter as tk
from PIL import ImageTk, Image
import time

def failist_sonastik(f):  #võtab triki nime ja selle hinde failist
    f=open("trikid.txt", "r", encoding="UTF-8")
    a=[]                                        #tekib kahekordne järjend
    for rida in f:                       #eemaldatakse realõpu märgid
        a+=([rida.strip().split(" ", 1)])              #poolitatakse esimese tühiku juures
    vaartus={}                                  #siia kogutakse sõnastik {triki nimi:hinne}
    j=0
    i=0
    for i in range(len(a)):
        voti= str(a[i][j])
        vaartus[voti]=a[i][j+1]
    #print(vaartus)
    return vaartus

def nupp(nupp, voistleja):
    #print("nupp", nupp)
    if voistleja == "a":
        a.append(float(nupp))
        lisa_katse("a")
        #print("a", a,"teine", teine)
    if voistleja == "b":
        teine.append(float(nupp))
        #print("teine", teine, "a", a)
        lisa_katse("b")

def protokoll_f():
    global a
    global teine
    global miinused
    protokoll = open("protokollid.txt", "a", encoding="UTF-8")
    summaA = sum(a)
    summaB = sum(teine)
    protokoll.write("\nVõistleja: "+ võistlejaA + "Hinded: " + str(a))
    protokoll.write("\nHinnete summa: " + str(summaA))
    protokoll.write("\nVõistleja: "+ võistlejaB + "Hinded: " + str(teine))
    protokoll.write("\nHinnete summa: " + str(summaB))
    protokoll.close()
    f = open("tulemused.txt", "a", encoding="UTF-8")
    f.write(võistlejaA + str(summaA) + "\n" )
    f.write(võistlejaB + str(summaB) + "\n")
    f.close()
    
def võitja():
    fl = open("tulemused.txt", "r", encoding="UTF-8")
    c = 1
    tulemused_n = []
    tulemused_s = []
    for rida in fl:
        if c % 2 != 0:
            tulemused_n.append(rida.strip())
        if c % 2 == 0:
            tulemused_s.append(rida.strip())
        c += 1
    f.close()
    seni_suurim = tulemused_s[0]
    for summa in tulemused_s:
        if summa > seni_suurim:
            seni_suurim = summa
    print(seni_suurim + " võitja punktid")
    
    võitja_voor = []
    for summa in tulemused_s:
        for i in range(2):
            if tulemused_s[i] > tulemused_s[i+1]:
                võitja_voor.append(tulemused_n[i])
            else:
                võitja_voor.append(tulemused_n[i+1])

def lisa_katse(kellele):# def loendab katseid kuni 7-meni ja
    if kellele == "a":
        katseidA.append(1)
 #           naita_punkte(a) #ERRORIST VABAKS ENNE N"ITAB PUNKTID siis l]petab
        for el in a:
            "\n".join
            Label(win, text = len(a), foreground="white", background="black"). grid(row = 6, column = 0)
            #hetkel punkte
        Label(win, text = sum(a), foreground="white", background="black") .grid(row = 8, column = 0)
        A=katseidA.count(1)
        B=katseidB.count(1)
        if A>=7:
            for el in range(len(c)):
                sõnastikA[c[el]].configure(command= lambda :None)
    if kellele == "b":
        katseidB.append(1)
 #           naita_punkte(teine) #ERRORIST VABAKS ENNE N"ITAB PUNKTID siis l]petab
        for el in teine:
            "\n".join
            Label(win, text = len(teine), foreground="white", background="black"). grid(row = 6, column = 4)
            #Hetkel punkte
        Label(win, text = sum(teine), foreground="white", background="black") .grid(row = 8, column = 4)
        A=katseidA.count(1)
        B=katseidB.count(1)
        if B>=7:
            for el in range(len(c)):
                sõnastikB[c[el]].configure(command= lambda: None)
    if A>=7 and B>=7:
        
        update()
        
def uusRound():
    win = Tk()
    win.geometry("600x70") #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
    win.title("HINDAMISLEHT")
    Label(win, text="JÄRGMINE ROUND", font=("hevetica", 50)).grid(column=3, row=2, pady=10, padx=10)   # lõpetab hindamislehe täitmise

    
def update():
    global võistlejaA
    global võistlejaB
    protokoll_f()
    uusRound()
    global a
    a=[] #Siia kogutakse võistlejale antud hinded selle kohtuniku pool
    global teine
    teine=[]#Siia kogutakse TEISE võistlejale antud hinded selle kohtuniku pool    
    global katseidA
    katseidA=[]
    global katseidB
    katseidB=[]
    global miinus
    miinus=[]
    global i
    i=0 
    global hinded
    hinded=[]
    global miinused
    miinused=[]
    global img2
    global img1

    võistlejaA = võistleja.pop(v)
    võistlejaB = võistleja.pop(v)
    
    Label(win, text=võistlejaA, foreground="white", background="black").grid(column= 1, row=2)
    Label(win, text=võistlejaB, foreground="white", background="black").grid(column=6, row=2 )
    
    img1 = ImageTk.PhotoImage(Image.open("pilt3.png"))
    img2 = ImageTk.PhotoImage(Image.open("pilt4.png"))
    Label(win, text="PILT", image=img1, height= 150, width= 150).grid(column=1, row=0, pady=(20, 0))
    Label(win, text="PILT", image=img2, height= 150, width= 150).grid(column=6, row=0, pady=(20, 0))
    
    
    Label(win, text = len(a), foreground="white", background="black"). grid(row = 6, column = 0)
    Label(win, text = sum(a), foreground="white", background="black").grid(row = 8, column = 0)
    Label(win, text = len(teine), foreground="white", background="black"). grid(row = 6, column = 4)
    Label(win, text = sum(teine), foreground="white", background="black") .grid(row = 8, column = 4)
 
    
    for el in range(len(c)):
        sõnastikA[c[el]].configure(command = lambda nuppu=b[c[el]]:nupp(nuppu, "a"))
        sõnastikB[c[el]].configure(command = lambda nuppu=b[c[el]]:nupp(nuppu, "b"))

    
    
def välju1(): # rakendub kui katsete arv on täis
    if a == []: # kui pole trikke, siis pannakse kõik 0
        trikke()
    hinded.append(a)#lisab saadud hinded hined[] listi
    miinused.append(sum(miinus))
          

def miinus1():
    miinus.append(int(1))
def trikke():
    a.append(0.0)
    hinded.append(a)


kuupäev_kellaeg = datetime.today()
#....................................................................................
"""hindamislehe KOHTUNIKU SEADISTAMINE"""

f = open("võistlejad.txt", "r", encoding="UTF-8")   #registreerinud võistlejate nimekiri failis

msg ="Kohtunik NR 1\nSisesta oma ees- ja perekonnanimi:"
title = "Lohesurfi Vabastiili EMV 2016"
kohtunik = enterbox(msg, title).upper() #Kohtunik, kelle hindamisleht see on
while kohtunik == None or kohtunik == "":
    msgbox("Te ei sisetanud midagi!")
    kohtunik = enterbox(msg, title)
else:
    msgbox(kohtunik + " , olete registreeritud käesoleva hindamislehe kohtunikuks.")


#....................................................................................
b=(failist_sonastik(f)) #sõnastik trikkide ja väärtustega
#....................................................................................
c=[]                    #list ainult trikkide nimedest, 
for element in b:       #mis lisatakse nuppude text= ..... väärtusteks
    c.append(element)
#
v=0
võistleja = [] #võistlejate list
for read in f:
    võistlejad = read.upper()#loeb registreerinud võistlejate failist esimese võistleja nime. Peale tsükli läbimist järgmise võistleja.
    võistleja.append(võistlejad)
    #print("Võistlejad", võistlejad)

võistlejaA = võistleja.pop(v)
võistlejaB = võistleja.pop(v) 
#....................................................................................
"""12 triki nime ja väärtusega hindamispaneel
NUPUD EKRAANILE, mida kasutatakse võistluse ajal kohtuniku poolt"""

a=[] #Siia kogutakse võistlejale antud hinded selle kohtuniku pool
teine=[] #Siia kogutakse TEISE võistlejale antud hinded selle kohtuniku pool    
katseidA=[]
katseidB=[]
miinus=[]

i=0 
nr = 1 #Hindamislehed on nummerdatud
hinded=[]
miinused=[]


win = Tk()
win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
win.title("HINDAMISLEHT")
win.configure(background='black')

h=3 #saab muuta nuppude kõrgus
i=0 #saab nuppude tekstid võtta järjendist c
r=20



#img = PhotoImage(file="EsimeneA.gif")
img1 = ImageTk.PhotoImage(Image.open("./pilt1.png"))
img2 = ImageTk.PhotoImage(Image.open("./pilt2.png"))
Label(win, text="PILT", image=img1, height= 150, width= 150).grid(column=1, row=0, pady=(20, 0))
Label(win, text="PILT", image=img2, height= 150, width= 150).grid(column=6, row=0, pady=(20, 0))


Label(win, text="VÕISTLEJA A:", foreground="white", background="black").grid(column = 1, row=1, pady=(20, 0))
Label(win, text="Tehtud katseid A:", foreground="white", background="black").grid(row = 5, column = 0)
Label(win, text="Hetkel pukte A:", foreground="white", background="black").grid(row = 7, column = 0)

Label(win, text="VÕISTLEJA B:", foreground="white", background="black").grid(column=6, row=1, pady=(20, 0))
Label(win, text="Tehtud katseid B:", height= h, width= 20, foreground="white", background="black").grid(row = 5, column = 4)
Label(win, text="Hetkel pukte B:", height= h, width= 20, foreground="white", background="black").grid(row = 7, column = 4)


Label(win, text="KOHTUNIK:", foreground="white", background="black").grid(row=15, column=0, pady=(50, 0)) #Kohtunik
Label(win, text=kohtunik, foreground="white", background="black").grid(row=16, column=0)


välju= Button(win, text='KATKESTAS', height= h-1, width= 10) #Võistleja A
välju.grid(row=3, column=0, pady=(2, 2), padx=(2, 2))
min = Button(win, text=' LISA -1 ', height= h-1, width= 10)
min.grid(row=4, column=0, pady=(2, 2), padx=(2, 2))

välju= Button(win, text='KATKESTAS', height= h-1, width= 10)# Võistleja B
välju.grid(row=3, column=4, pady=(2, 2), padx=(2, 2))
min = Button(win, text=' LISA -1 ', height= h-1, width= 10)
min.grid(row=4, column=4, pady=(2, 2), padx=(2, 2))
 
Label(win, text=võistlejaA, foreground="white", background="black").grid(column= 1, row=2)
Label(win, text = len(a), foreground="white", background="black"). grid(row = 6, column = 0) #Võistleja A
Label(win, text = sum(a), foreground="white", background="black").grid(row = 8, column = 0)

Label(win, text= võistlejaB, foreground="white", background="black").grid(column=6, row=2)
Label(win, text = len(teine), foreground="white", background="black"). grid(row = 6, column = 4) #Võistleja B
Label(win, text = sum(teine), foreground="white", background="black").grid(row = 8, column = 4)


sõnastikA = {}   
sõnastikB = {}


if len(c) % 3 == 0:
    print('Nuppude arv jagub 3 veeru jaoks täpselt. Jääk on', len(c) % 3)
else:
    s = 3 - ((len(c))%3) 
    print('Nuppude arv ei jagu 3 veeru jaoks täpselt. Jääk on', (len(c))%3)
    print('Lahutame jäägi maha 3-mest ehk 3 -', (len(c))%3)
    print("Lisanuppe tehakse s tk ehk s=", s)
    while s > 0:
        c.append(str(s))
        b[str(s)]= 0.0
        s -= 1
    print("Nupud e c:", c)
    print("b:", b)

    
nuppe = len(c)
ridu= int(nuppe / 3) # i tsüklisse läheb 3 korda vähem kordi
el = 0 # list(range(nuppe))
print(el, ridu)

nupu_fn={}

for i in range(ridu):
    #print(ridu)
    for j in range(3):
        nuppu=b[c[el]]
        #print("nuppu: ", nuppu)
        sõnastikA[c[el]] = Button(win, text=c[el], height=h, width= r, command = lambda nuppu=b[c[el]]:nupp(nuppu, "a"))
 #       sõnastikA[c[el]].configure(command = lambda: nupp(nuppu, "a"))

        sõnastikA[c[el]].grid(column=j+ 1, row= i+5, pady=(2, 2), padx=(2, 2))
        #print("EL -", el, "EL-1", el-1)
        
        sõnastikB[c[el]] = Button(win, text=c[el], height=h, width= r, command = lambda nuppu=b[c[el]]:nupp(nuppu, "b"))
        #print("nupu NIMI", c[el])
        #print("NUPPu", nuppu)
 #       sõnastikB[c[el]].configure(command= lambda: nupp(nuppu, "b"))
        
        sõnastikB[c[el]].grid(column=j+6, row= i+5, pady=(2, 2), padx=(2, 2))
 #       sõnastikB[c[el]].pack()
        #print(i, j)
        j +=1
        el+=1

välju.configure(command=välju1)
min.configure(command=miinus1)

#print("nupu_fn", nupu_fn, "A-", sõnastikB, "B-",sõnastikA)

print("Hindamislehte täidab kohtunik: " + kohtunik)

protokoll = open("protokollid.txt", "w", encoding="UTF-8")  #Sisestab protokolli faili kohtuniku nime
protokoll.write("\n" + str(kuupäev_kellaeg) + "\n")
protokoll.write(("Hindamislehti täidab kohtunik: " + kohtunik) + "\n")
protokoll.close()
        
 
##summa = sum(hinded[i])
##hinne = summa - miinused[i]
##keskmine = round((hinne)/ len(hinded[i]), 1)
##print("HINDAMISLEHT nr. " + str(nr))
##print("Võistleja: " + read + "Hinded on: " + str(hinded[i]))
##print("Hinnete summa: " + str(summa))
##print("Miinuseid kokku: -" + str(miinused[i]))
##print("Hinne kokku " + str(hinne))
##print("Hinnete keskmine: " + str(keskmine)) 
##print()
##protokoll = open("protokollid.txt", "a", encoding="UTF-8") #avab protokolli faili, kuhu kirjutab hindamislehe protokolli
##protokoll.write("\nHINDAMISLEHT NR: " + str(nr) +"\n")
##protokoll.write(str(kuupäev_kellaeg))
##protokoll.write("\nVõistleja: " + võistleja + "Hinded: " + str(hinded[i]))
##protokoll.write("\nHinnete summa: " + str(summa))
##protokoll.write("\nMiinuseid kokku: " + str(miinused[i]))
##protokoll.write("\nHinne kokku " + str(summa - miinused[i]))
##protokoll.close()
##    
##f = open("tulemused.txt", "a", encoding="UTF-8") #avab protokolli faili, kuhu kirjutab võistleja tulemused
##f.write( "\n" + võistleja + str(hinne) + "\n" )
##f.close()
##
##    
##i += 1
####nr += 1

open("tulemused.txt", "w", encoding="UTF-8")
win.mainloop( )
#võitja()



