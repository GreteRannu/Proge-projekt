
from easygui import *
from tkinter import *
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
    print(vaartus)
    return vaartus


def muuda_katseid():
    global katseidA
    global katseidB
    global n_katseid
    if len(katseidA) > 0 or len(katseidB) > 0:
        return msgbox("""Kahjuks ei saa vooru toimumis ajal katsete arvu muuta!
                      Muuda katsete arv peale vooru lõppu!""")
    msg ="Muuda katsete arvu:"
    title = "ScoreFreestyle"
    n_katseid = enterbox(msg, title).upper() 
    while n_katseid == None or n_katseid == "":
        msgbox("Te ei sisetanud midagi!")
        n_katseid = int(enterbox(msg, title))
    while n_katseid.isnumeric() == False:
        msgbox("Sisestus peab olema number!")
        n_katseid = int(enterbox(msg, title))
    else:
        Label(win, text="Lubatud: "+str(n_katseid), foreground="white", background="black").grid(row=9, column=0, pady=(50, 0))
    n_katseid = int(n_katseid)
 
 
def set_kohtunik():
    global kohtunik
    kohtunik = kohtunik_sisend.get()
    set.destroy()
 
 
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
            
def lisa_katse(kellele):# def loendab katseid kuni n_katseid-meni ja
    if kellele == "a":
        katseidA.append(1)
        for el in a:
            "\n".join
            Label(win, text = len(a), foreground="white", background="black"). grid(row = 6, column = 0)
            #hetkel punkte
        Label(win, text = sum(a)-miinusedA.count(1), foreground="white", background="black") .grid(row = 8, column = 0)
        A=katseidA.count(1)
        B=katseidB.count(1)
        if A>=n_katseid or katkestasA == True: #Kui katseta arv on täis või võistleja katkestas
            for el in range(len(c)):
                sõnastikA[c[el]].configure(command= lambda :None)
    if kellele == "b":
        katseidB.append(1)
        for el in teine:
            "\n".join
            Label(win, text = len(teine), foreground="white", background="black"). grid(row = 6, column = 4)
        Label(win, text = sum(teine)-miinusedB.count(1), foreground="white", background="black") .grid(row = 8, column = 4)
        A=katseidA.count(1)
        B=katseidB.count(1)
        if B>=n_katseid or katkestasB == True:  #Kui katseta arv on täis või võistleja katkestas
            for el in range(len(c)):
                sõnastikB[c[el]].configure(command= lambda: None)
    kas_vooru_lõpp()
        
def kas_vooru_lõpp(): #Lühendamiseks, need read olid nii katkestus() kui lisa_katse() all
    global katkestasA
    global katkestasB
    A=katseidA.count(1)
    B=katseidB.count(1)
    if A>=n_katseid and B>=n_katseid:
        print("A=", a, "teine=", teine)
        loo_protokollid()
        võitjad_listi()
        update()
    elif A>=n_katseid and katkestasB == True: #Kui üks võistlejatest katkestab
        print("A=", a, "teine=", teine)
        loo_protokollid()
        võitjad_listi()
        update()
    elif katkestasA == True and B>=n_katseid:
        print("A=", a, "teine=", teine)
        loo_protokollid()
        võitjad_listi()
        update()
    elif katkestasA == True and katkestasB == True: #Kui mõlemad võistlejad katkestavad
        print("A=", a, "teine=", teine)
        loo_protokollid()
        võitjad_listi()
        update()
    else:
        pass

def loo_protokollid():
    summaA = sum(a)
    summaB = sum(teine)
    protokoll = open("protokollid.txt", "a", encoding="UTF-8")
    if katkestasA == True:
        protokoll.write("\nVõistleja: " + võistlejaA + ": Katkestas \n")
    else:
        protokoll.write("\nVõistleja: " + võistlejaA + " Hinded: " + str(a)[1:-1])
        protokoll.write("\nHinnete summa: " + str(summaA))
        protokoll.write("\nMiinuseid kokku: " + str(miinusedA.count(1)))
        protokoll.write("\nHinne kokku " + str(summaA - miinusedA.count(1))+ "\n")
        
    if katkestasB == True:
        protokoll.write("\nVõistleja: " + võistlejaB + ": Katkestas \n")
    else:
        protokoll.write("\nVõistleja: " + võistlejaB + " Hinded: " + str(teine)[1:-1])
        protokoll.write("\nHinnete summa: " + str(summaB))
        protokoll.write("\nMiinuseid kokku: " + str(miinusedB.count(1)))
        protokoll.write("\nHinne kokku " + str(summaB - miinusedB.count(1))+ "\n")
    protokoll.close()
    
        
def uusRound():
    round = Tk()
    round.geometry("{0}x{1}".format(round.winfo_screenwidth(), round.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
    round.title("Uus voor")
    round.configure(background='black')
    Label(round, text="# uus voor", font=("hevetica", 50), foreground="white", background="black").grid(column=6, row=2, pady=100, padx=550)
    round_nupp = Button(round, text='ALUSTA', height=2, width= 20, command = lambda: round.destroy()).grid(column=6, row=3, pady=0, padx=0)


def viimaneRound():
    viimane = Tk()
    viimane.geometry("{0}x{1}".format(viimane.winfo_screenwidth(), viimane.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
    viimane.title("Uus voor")
    viimane.configure(background='black')
    Label(viimane, text="# roundi lõpp #", font=("hevetica", 50), foreground="white", background="black").grid(column=6, row=2, pady=100, padx=550)
    
    #tuleks täpsustada, et mis peaks täpselt juhtuma - kas on olemas uue roundi süsteem või kuidas väljuda kogu programmist.
    #!!!!!!!!!!!!!!!!!!!!!!!!!! Siin tuleks teha veel I ROUND kohta protokoll :)
    # !!!!!!!!!!!!  lambdasse tuleks lisada fail, kus on võitjad -> võistlejad_failist("võistlejad.txt", viimane)
    
    viimase_round_nupp1 = Button(viimane, text='ALUSTA uut roundi', height=2, width= 20, command = lambda: uued_võistlejad(võistlejad, viimane)).grid(column=6, row=3, pady=0, padx=0)
    protokoll = open("protokollid.txt", "a", encoding="UTF-8")
    protokoll.write("\nUus round-----\n")
    protokoll.close()

def võistlejad_failist(fail, viimane):
    global võistleja
    global v
    f = open(fail, "r", encoding="UTF-8")   #registreerinud võistlejate nimekiri failis#
    v=0
    võistleja = [] #võistlejate list
    for read in f:
        võistlejad = read.upper().strip()#loeb registreerinud võistlejate failist esimese võistleja nime. Peale tsükli läbimist järgmise võistleja.
        võistleja.append(võistlejad)
        print("Võistlejad", võistlejad)
    f.close()
    update()
    viimane.destroy()
    
def uued_võistlejad(võistlejad, viimane):
    global võistleja
    global võitjad
    global v
    v=0
    võistleja = võitjad
    update()
    viimane.destroy()
    
def võitjad_listi():
    if sum(a)-miinusedA.count(1) > sum(teine)-miinusedB.count(1):
        võitjad.append(võistlejaA)
    else:
        võitjad.append(võistlejaB)
    return võitjad
    
def update():
    global võitjad
    global võistlejaA, võistlejaB
    global võistleja
    global a
    global teine
    a=[]             #VõistlejaA hinded
    teine=[]         #VõistlejaB hinded   
    global katseidA
    katseidA=[]
    global katseidB
    katseidB=[]
    global miinusedA, miinusedB
    miinusedA=[]
    miinusedB=[]
    global i
    i=0 
    global hinded
    hinded=[]
    global img2
    global img1
    global katkestasA, katkestasB
    katkestasA = False
    katkestasB = False
    
    if len(võistleja)<=0:
        viimaneRound() # kui osalejad otsas tuleb uus round
    
    elif len(võistleja)== 1:
            kuuluta_võitja()
    else:
        uusRound()
        võistlejaA = võistleja.pop(v)
        võistlejaB = võistleja.pop(v)
    
    A=Label(win, text=võistlejaA, foreground="white", background="black", width= 20).grid(column= 1, row=2)
    B=Label(win, text=võistlejaB, foreground="white", background="black", width= 20).grid(column=6, row=2 )

    img1 = ImageTk.PhotoImage(Image.open("./pildid/"+võistlejaA+".png"))
    img2 = ImageTk.PhotoImage(Image.open("./pildid/"+võistlejaB+".png"))
    Label(win, text="PILT", image=img1, height= 150, width= 150, background="black").grid(column=1, row=0, pady=(20, 0))
    Label(win, text="PILT", image=img2, height= 150, width= 150, background="black").grid(column=6, row=0, pady=(20, 0))
       
    Label(win, text = len(a), foreground="white", background="black"). grid(row = 6, column = 0)
    Label(win, text = sum(a), foreground="white", background="black").grid(row = 8, column = 0)
    Label(win, text = len(teine), foreground="white", background="black"). grid(row = 6, column = 4)
    Label(win, text = sum(teine), foreground="white", background="black") .grid(row = 8, column = 4)
 
    for el in range(len(c)):
        sõnastikA[c[el]].configure(command = lambda nuppu=b[c[el]]:nupp(nuppu, "a"))
        sõnastikB[c[el]].configure(command = lambda nuppu=b[c[el]]:nupp(nuppu, "b"))

    
    
def välju1():                     # rakendub kui katsete arv on täis
    win.destroy()
    exit()
    
def kuuluta_võitja():
    kuulutus = Tk()
    kuulutus.geometry("{0}x{1}".format(kuulutus.winfo_screenwidth(), kuulutus.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
    kuulutus.title("Võitja selgunud!")
    kuulutus.configure(background='black')
    Label(kuulutus, text="Võitja on: " + võistleja[0] + "!", font=("hevetica", 42), foreground="white", background="black").grid(column=2, row=2, pady=100, padx=550)
    välju_nupp = Button(kuulutus, text='OK', height=2, width= 20, command = välju1).grid(column=2, row=3, pady=0, padx=0)
    
def miinus1(kellele):
    if kellele == "a":
        miinusedA.append(int(1))
        Label(win, text = sum(a)-miinusedA.count(1), foreground="white", background="black") .grid(row = 8, column = 0)
    elif kellele == "b":
        miinusedB.append(int(1))
        Label(win, text = sum(teine)-miinusedB.count(1), foreground="white", background="black") .grid(row = 8, column = 4)
        
def katkestus(kellele):
    global katkestasA
    global katkestasB
    global a, teine
    if kellele == "a":
        katkestasA = True
        a = []
    elif kellele == "b":
        katkestasB = True
        teine = []
    kas_vooru_lõpp()

def trikke():
    a.append(0.0)
    hinded.append(a)
    
"""
____________________________________________  Vaikeväärtused | kuupäev | katsete arv | vaikekohtunik  _____________________________________________________________
"""    

kuupäev_kellaeg = datetime.today()
kohtunik = "Registreerimata kohtunik"               #vaikeväärtus kohtunikul
n_katseid = 1 #vaikeväärtus katsete arvul
katkestasA = False
katkestasB = False

"""
____________________________________________  1. aken ________  Siestus - Entry | Kohtunik  _____________________________________________________________
"""


set = Tk()
set.geometry("{0}x{1}+0+0".format(set.winfo_screenwidth(), set.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
set.title("HINDAMISLEHT")
set.configure(background='black')
img3 = ImageTk.PhotoImage(Image.open("./logo2.png"))  #Võistleja A
Label(set, text="PILT", image=img3, background="black").grid(column=1, row=0, pady=(0, 0))  #Võist

Label(set, text="KOHTUNIK:", foreground="white", background="black").grid(row=4, column=0, padx=(50, 0)) #Kohtunik
kohtunik_sisend = Entry(set,  text="Kohtunik", width=15)
#kohtunik_sisend.pack()
kohtunik_sisend.focus_set()
kohtunik_sisend.grid(column=0, row=5, padx=(50, 0), pady=(15, 0))

sisestus = Button(set, text="Kinnita", width=10, command = lambda: set_kohtunik())
#sisestus.pack()
sisestus.grid(row=7, column=0, padx=(50, 0), pady=(15, 0))

set.mainloop( )



"""
____________________________________________________  Võistlejate nimekiri | failist _____________________________________________________________
"""
   
    
f = open("võistlejad.txt", "r", encoding="UTF-8")   #registreerinud võistlejate nimekiri failis#
v=0
võistleja = [] #võistlejate list
for read in f:
    võistlejad = read.upper().strip()#loeb registreerinud võistlejate failist esimese võistleja nime. Peale tsükli läbimist järgmise võistleja.
    võistleja.append(võistlejad)
    print("Võistlejad", võistlejad)
f.close()

võistlejaA = võistleja.pop(v)
võistlejaB = võistleja.pop(v)


"""
______________________________________  Põhiprogrammi seadistamine | trikid failist, vaikeväärtused ___________________________________________________
"""


b=(failist_sonastik(f)) #sõnastik trikkide ja väärtustega

c=[]                    #list ainult trikkide nimedest 
for element in b:       #lisatakse nuppude (text= .....) muutuja nimendeks
    c.append(element)
    
a=[]                    #VõistlejaA hinded
teine=[]                #VõistlejaB hinded   

katseidA=[]
katseidB=[]

hinded=[]
miinusedA=[]
miinusedB=[]
võitjad = []

h=3                    #nuppude kõrgus
i=0                    #index listist lugemiseks (nt c)
r=20                   #nuppude laius

"""
____________________________________________ 1. aken  _____  Aken avaneb siin   ________________________________________
"""
             
win = Tk()        
win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
win.title("HINDAMISLEHT")
win.configure(background='black')

print("KOHTUNIKUKS REGISTREERUS:", kohtunik)


"""
                                            VÕISTLEJATE seadistamine avatud aknas 

__________________________________________________       Pildid     ______________________________________________________
"""
img1 = ImageTk.PhotoImage(Image.open("./pildid/"+võistlejaA+".png"))  #Võistleja A
img2 = ImageTk.PhotoImage(Image.open("./pildid/"+võistlejaB+".png"))  #Võistleja B
Label(win, text="PILT", image=img1, height= 150, width= 150, background="black").grid(column=1, row=0, pady=(20, 0))  #Võistleja A
Label(win, text="PILT", image=img2, height= 150, width= 150, background="black").grid(column=6, row=0, pady=(20, 0))  #Võistleja B



"""
__________________________________________________    Võistleja    A   ____________________________________________________
"""
Label(win, text="VÕISTLEJA A:", foreground="white", background="black").grid(column = 1, row=1, pady=(20, 0))
A=Label(win, text=võistlejaA, foreground="white", background="black", width= 20).grid(column= 1, row=2)

Label(win, text="Tehtud katseid A:", foreground="white", background="black").grid(row = 5, column = 0)
Label(win, text = len(a), foreground="white", background="black"). grid(row = 6, column = 0) #Võistleja A

Label(win, text="Hetkel pukte A:", foreground="white", background="black").grid(row = 7, column = 0)
Label(win, text = sum(a), foreground="white", background="black").grid(row = 8, column = 0)

välju= Button(win, text='KATKESTAS', height= h-1, width= 10) #Võistleja A
välju.grid(row=3, column=0, pady=(2, 2), padx=(2, 2))
välju.configure(command= lambda: katkestus("a"))

min = Button(win, text=' LISA -1 ', height= h-1, width= 10)
min.grid(row=4, column=0, pady=(2, 2), padx=(2, 2))
min.configure(command= lambda: miinus1("a"))

"""
__________________________________________________    Võistleja    B   ____________________________________________________
"""
Label(win, text="VÕISTLEJA B:", foreground="white", background="black").grid(column=6, row=1, pady=(20, 0)) #Võistleja B
B=Label(win, text= võistlejaB, foreground="white", background="black", width= 20).grid(column=6, row=2)

Label(win, text="Tehtud katseid B:", height= h, width= 20, foreground="white", background="black").grid(row = 5, column = 4)
Label(win, text = len(teine), foreground="white", background="black"). grid(row = 6, column = 4) #Võistleja B

Label(win, text="Hetkel pukte B:", height= h, width= 20, foreground="white", background="black").grid(row = 7, column = 4)
Label(win, text = sum(teine), foreground="white", background="black").grid(row = 8, column = 4)

välju= Button(win, text='KATKESTAS', height= h-1, width= 10)# Võistleja B
välju.grid(row=3, column=4, pady=(2, 2), padx=(2, 2))
välju.configure(command= lambda: katkestus("b"))

min = Button(win, text=' LISA -1 ', height= h-1, width= 10)
min.grid(row=4, column=4, pady=(2, 2), padx=(2, 2))
min.configure(command= lambda: miinus1("b"))

"""
__________________________________________ Muud nupud | Muuda katsete arv| Uue roundi nupp _________________________________________________________________
"""

Label(win, text="Lubatud: "+str(n_katseid), foreground="white", background="black").grid(row=9, column=0, pady=(50, 0)) #N;itab lubatud katsete arvu 2 aknas
sisestus2 = Button(win, text="Muuda", width=10, command = lambda: muuda_katseid()).grid(row=10, column=0, pady=(0, 0))

uusRoundNupp = Button(win, text = 'Uus round', height = h-1, width = 10)
uusRoundNupp.grid(row=10, column=9)
uusRoundNupp.configure(command = update)

"""
____________________________________________ Nuppude genereerimine ja seadistamine  ____________________________________________________________________
"""

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
        c.append(str(""))
        b[str("")]= 0.0
        s -= 1
    #print("Nupud e c:", c)
    #print("b:", b)

    
nuppe = len(c)
ridu= int(nuppe / 3) # i tsüklisse läheb 3 korda vähem kordi
el = 0 # list(range(nuppe))
#print(el, ridu)

for i in range(ridu):
    #print(ridu)
    for j in range(3):
        nuppu=b[c[el]]
        #print("nuppu: ", nuppu)
        sõnastikA[c[el]] = Button(win, text=c[el], height=h, width= r, command = lambda nuppu=b[c[el]]:nupp(nuppu, "a"))
        sõnastikA[c[el]].grid(column=j+ 1, row= i+5, pady=(2, 2), padx=(2, 2))
        #print("EL -", el, "EL-1", el-1)
        sõnastikB[c[el]] = Button(win, text=c[el], height=h, width= r, command = lambda nuppu=b[c[el]]:nupp(nuppu, "b"))
        #sõnastikB[c[el]].pack()
        #print("nupu NIMI", c[el])
        #print("NUPPu", nuppu)
        sõnastikB[c[el]].grid(column=j+6, row= i+5, pady=(2, 2), padx=(2, 2))
        j +=1
        el+=1



"""
____________________________________________    Protokollid  ____________________________________________________________________
"""

protokoll = open("protokollid.txt", "a", encoding="UTF-8")  #Sisestab protokolli faili kohtuniku nime
protokoll.write("\n-------------------------------------\n")
protokoll.write(("Hindamislehti täidab kohtunik: " + kohtunik) + "\n")
protokoll.write(str(kuupäev_kellaeg) + "\n")
protokoll.close()







win.mainloop( )





