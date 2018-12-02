
from easygui import *
from tkinter import *
from tkinter import ttk # platvormi ühise stiili saamiseks
from tkinter import messagebox
from datetime import datetime
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
    print(vaartus)
    return vaartus

def nupp(nupp, voistleja):
    print("nupp", nupp)
    if voistleja == "a":
        a.append(float(nupp))
        
        lisa_katse("a")
        print("a", a,"teine", teine)
    if voistleja == "b":
        teine.append(float(nupp))
        
        print("teine", teine, "a", a)
        lisa_katse("b")
            
            
def lisa_katse(kellele):# def loendab katseid kuni 7-meni ja
    if kellele == "a":
        katseidA.append(1)
 #           naita_punkte(a) #ERRORIST VABAKS ENNE N"ITAB PUNKTID siis l]petab
        for el in a:
            "\n".join
            Label(win, text = len(a)). grid(row = 6, column = 0)
            #hetkel punkte
        Label(win, text = sum(a)) .grid(row = 8, column = 0)
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
            Label(win, text = len(teine)). grid(row = 6, column = 4)
            #Hetkel punkte
        Label(win, text = sum(teine)) .grid(row = 8, column = 4)
        A=katseidA.count(1)
        B=katseidB.count(1)
        if B>=7:
            for el in range(len(c)):
                sõnastikB[c[el]].configure(command= lambda: None)
    if A>=7 and B>=7:
        print("A=", a, "teine=", teine)
 #       välju1()
        update()
def uusRound():
    win = Tk()
    win.geometry("600x70") #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
    win.title("HINDAMISLEHT")
    
    Label(win, text="JÄRGMINE ROUND", font=("hevetica", 50)).grid(row=2)   # lõpetab hindamislehe täitmise 
        
    
    
    
def update():
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
    
    võistlejaA = "Mari"
    võistlejaB = "Kalle"
    
    Label(win, text=võistlejaA).grid(column= 2, row=1)
    Label(win, text=võistlejaB).grid(column=7, row=1 )
    print(a, teine)
    Label(win, text = len(a)). grid(row = 6, column = 0)
    Label(win, text = sum(a)).grid(row = 8, column = 0)
    Label(win, text = len(teine)). grid(row = 6, column = 4)
    Label(win, text = sum(teine)) .grid(row = 8, column = 4)
 
    
    for el in range(len(c)):
        sõnastikA[c[el]].configure(command= lambda: nupp(el-1, "a"))
        sõnastikB[c[el]].configure(command= lambda: nupp(el-1, "b"))
        
    
    
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
    
print("Hindamislehte täidab kohtunik: " + kohtunik)

protokoll = open("protokollid.txt", "w", encoding="UTF-8")  #Sisestab protokolli faili kohtuniku nime
protokoll.write("\n" + str(kuupäev_kellaeg) + "\n")
protokoll.write(("Hindamislehti täidab kohtunik: " + kohtunik) + "\n")
protokoll.close()

#....................................................................................
b=(failist_sonastik(f)) #sõnastik trikkide ja väärtustega
#....................................................................................
c=[]                    #list ainult trikkide nimedest, 
for element in b:       #mis lisatakse nuppude text= ..... väärtusteks
    c.append(element)


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

võistleja = [] #võistlejate list


win = Tk()
win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
win.title("HINDAMISLEHT")
win.configure(background='white')

h=3 #saab muuta nuppude kõrgus
i=0 #saab nuppude tekstid võtta järjendist c
r=20


img = PhotoImage(file="EsimeneA.gif")

Label(win, text="PILT", image=img, height= 150, width= 150).grid(column=1, row=0)
Label(win, text="PILT", image=img, height= 150, width= 150).grid(column=6, row=0)

Label(win, text="VÕISTLEJA A:").grid(column = 1, row=1)
Label(win, text="Tehtud katseid A:").grid(row = 5, column = 0)
Label(win, text="Hetkel pukte A:").grid(row = 7, column = 0)


Label(win, text="VÕISTLEJA B:", height= h).grid(column=6, row=1)
Label(win, text="Tehtud katseid B:").grid(row = 5, column = 4)
Label(win, text="Hetkel pukte B:").grid(row = 7, column = 4)

Label(win, text="Hindav kohtunik:").grid(row=15, column=0) #Kohtunik
Label(win, text=kohtunik).grid(row=16, column=0)

välju= Button(win, text='KATKESTAS', height= h-1, width= 10) #Võistleja A
välju.grid(row=3, column=0)
min = Button(win, text=' LISA -1 ', height= h-1, width= 10)
min.grid(row=4, column=0)

välju= Button(win, text='KATKESTAS', height= h-1, width= 10)# Võistleja B
välju.grid(row=3, column=4)
min = Button(win, text=' LISA -1 ', height= h-1, width= 10)
min.grid(row=4, column=4)
 
#Label(win, text=võistlejaA).grid(row=1)
Label(win, text = len(a)). grid(row = 6, column = 0) #Võistleja A
Label(win, text = sum(a)).grid(row = 8, column = 0)

#Label(win, text= võistlejaB).grid(column=7, row=1)
Label(win, text = len(teine)). grid(row = 6, column = 4) #Võistleja B
Label(win, text = sum(teine)).grid(row = 8, column = 4)


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

for i in range(ridu):
    #print(ridu)
    for j in range(3):
        nuppu=b[c[el]]
        print(nuppu)
        sõnastikA[c[el]] = Button(win, text=c[el], height=h, width= r)
        sõnastikA[c[el]].configure(command= lambda: nupp(nuppu, "a"))
        sõnastikA[c[el]].grid(column=j+ 1, row= i+5)
        print("EL -", el, "EL-1", el-1)
        
        sõnastikB[c[el]] = Button(win, text=c[el], height=h, width= r)
        print(sõnastikB[c[el]])
        sõnastikB[c[el]].configure(command= lambda: nupp(nuppu, "b"))
        sõnastikB[c[el]].grid(column=j+ 6, row= i+5)
        #print(i, j)
        j +=1
        el+=1

välju.configure(command=välju1)
min.configure(command=miinus1)

print("A-", sõnastikB, "B-",sõnastikA)

for read in f:
    võistlejad = read.upper()#loeb registreerinud võistlejate failist esimese võistleja nime. Peale tsükli läbimist järgmise võistleja.
    võistleja.append(võistlejad)
    print("Võistlejad", võistlejad)

võistlejaA = võistleja[0]
võistlejaB = võistleja[0+1] 


        
 
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
##protokoll.write("\nHinnete keskmine: " + str(keskmine) +"\n")
##protokoll.close()
##    
##f = open("tulemused.txt", "a", encoding="UTF-8") #avab protokolli faili, kuhu kirjutab võistleja tulemused
##f.write( "\n" + võistleja + str(hinne) + "\n" )
##f.close()
##
##    
##i += 1
####nr += 1

win.mainloop(0)

