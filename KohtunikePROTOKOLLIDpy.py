
from easygui import *
from tkinter import *
from tkinter import ttk # platvormi ühise stiili saamiseks
from tkinter import messagebox
from datetime import datetime
import time
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

protokoll = open("protokollid.txt", "a", encoding="UTF-8")  #Sisestab protokolli faili kohtuniku nime
protokoll.write("\n" + str(kuupäev_kellaeg) + "\n")
protokoll.write(("Hindamislehti täidab kohtunik: " + kohtunik) + "\n")
protokoll.close()

#....................................................................................
def failist_sonastik(f):  #võtab triki nime ja selle hinde failist
    f=open("trikid.txt", "r", encoding="UTF-8")
    a=[]                                        #tekib kahekordne järjend
    for rida in f:
        rida=rida.strip()                       #eemaldatakse realõpu märgid
        a=a+([rida.split(" ", 1)])              #poolitatakse esimese tühiku juures
    vaartus={}                                  #siia kogutakse sõnastik {triki nimi:hinne}
    j=0
    i=0
    for i in range(len(a)):
        voti= str(a[i][j])
        vaartus[voti]=a[i][j+1]
    return vaartus
#....................................................................................
b=(failist_sonastik(f)) #sõnastik trikkide ja väärtustega
#....................................................................................
c=[]                    #list ainult trikkide nimedest, 
for element in b:       #mis lisatakse nuppude text= ..... väärtusteks
    c.append(element)

    
#....................................................................................
"""12 triki nime ja väärtusega hindamispaneel
NUPUD EKRAANILE, mida kasutatakse võistluse ajal kohtuniku poolt"""

def avame_hinnetelehe(võistleja):
    win = Tk()
    win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight())) #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
    win.title("HINDAMISLEHT")
    a=[] #Siia kogutakse võistlejale antud hinded selle kohtuniku pool
    h=2 #saab muuta nummude kaugust omavahel
    i=0 #saab nuppude tekstid võtta järjendist c
    r=20
    katseid=[]
    miinus=[]
    
    b1 = Button(win,text=c[i], height=h, width= r)
    b2 = Button(win,text=c[i+1], height=h, width= r)
    b3 = Button(win,text=c[i+2], height=h, width= r)
    b4 = Button(win,text=c[i+3], height=h, width= r)
    b5 = Button(win,text=c[i+4], height=h, width= r)
    b6 = Button(win,text=c[i+5], height=h, width= r)
    b7 = Button(win,text=c[i+6], height=h, width= r)
    b8 = Button(win,text=c[i+7], height=h, width= r)
    b9 = Button(win,text=c[i+8], height=h, width= r)
    b10 = Button(win,text=c[i+9], height=h, width= r)
    b11 = Button(win,text=c[i+10], height=h, width= r)
    b12 = Button(win,text=c[i+11], height=h, width= r)
    
    b13 = Button(win,text=c[i], height=h, width= r)
    b14 = Button(win,text=c[i+1], height=h, width= r)
    b15 = Button(win,text=c[i+2], height=h, width= r)
    b16 = Button(win,text=c[i+3], height=h, width= r)
    b17 = Button(win,text=c[i+4], height=h, width= r)
    b18 = Button(win,text=c[i+5], height=h, width= r)
    b19 = Button(win,text=c[i+6], height=h, width= r)
    b20 = Button(win,text=c[i+7], height=h, width= r)
    b21 = Button(win,text=c[i+8], height=h, width= r)
    b22 = Button(win,text=c[i+9], height=h, width= r)
    b23 = Button(win,text=c[i+10], height=h, width= r)
    b24 = Button(win,text=c[i+11], height=h, width= r)

    b1.grid(row=5, column=1)
    b2.grid(row=6, column=1)
    b3.grid(row=7, column=1)
    b4.grid(row=8, column=1)
    b5.grid(row=5, column=2)
    b6.grid(row=6, column=2)
    b7.grid(row=7, column=2)
    b8.grid(row=8, column=2)
    b9.grid(row=5, column=3)
    b10.grid(row=6, column=3)
    b11.grid(row=7, column=3)
    b12.grid(row=8, column=3)
    
    b13.grid(row=5, column=5)
    b14.grid(row=6, column=5)
    b15.grid(row=7, column=5)
    b16.grid(row=8, column=5)
    b17.grid(row=5, column=6)
    b18.grid(row=6, column=6)
    b19.grid(row=7, column=6)
    b20.grid(row=8, column=6)
    b21.grid(row=5, column=7)
    b22.grid(row=6, column=7)
    b23.grid(row=7, column=7)
    b24.grid(row=8, column=7)

    #................................................
    Label(win, text="VÕISTLEJA:").grid(row=1)
    Label(win, text=võistleja).grid(row=2)
    Label(win, text="VÕISTLEJA:").grid(row=1)
    Label(win, text="HINDAV KOHTUNIK:").grid(row=1, column=4)
    Label(win, text=kohtunik).grid(row=2, column=4)
    Label(win, text="Antud punktid:").grid(row = 4, column = 4)
    Label(win, text="Hetkel pukte:").grid(row = 6, column = 4)
    välju= Button(win, text='KATKESTAS')
    välju.grid(row=3)
    min = Button(win, text=' LISA -1 ')
    min.grid(row=4)
    #trikke_mitu=Button(win, text=' TRIKKE "0" ')
    #trikke_mitu.grid(row=5)
    def naita_punkte(a):
        for el in a:
            "\n".join
        Label(win, text = a). grid(row = 5, column = 4)
    def hetkel_punkte(a):
        Label(win, text = sum(a)) .grid(row = 7, column = 4)
        
    #................................................
    """12 nupu vajutamisega kaasnevad funktsioonid"""
    #selleks, et nupule vajutamisel tekiks mitmekordne järjend saadud hinnetest,
    #mida hiljem töödelda/protokollida. str tehakse floatiks, et
    # srvutada hinnete keskmiseid, summat saadud järjendist
    def nupp(x):
        a.append(float(b[c[x]]))
        #b1 = Button(win,text=c[i], height=h, width= r)
        lisa_katse()
        naita_punkte(a)
        hetkel_punkte(a)
    
    def välju1(): # rakendub kui katsete arv on täis
        if a == []: # kui pole trikke, siis pannakse kõik 0
            trikke()
        hinded.append(a)#lisab saadud hinded hined[] listi
        miinused.append(sum(miinus))
        win.destroy()   # lõpetab hindamislehe täitmise 
        return time.sleep(1)
    def lisa_katse():           # def loendab katseid kuni 7-meni ja 
        katseid.append(1)       
        m=katseid.count(1)
        if m>=7:
            välju1()
    def miinus1():
        miinus.append(int(1))
    def trikke():
        a.append(0.0)
        hinded.append(a)
                  
        
    #.......................................................................
    b1.configure(command=lambda :nupp(1))         #Siin on seadistatud, millis juhtub
    b2.configure(command=lambda :nupp(2))         # nupu vajutamisel ja milline
    b3.configure(command=lambda :nupp(3))         # väärtus b=[] järjendist lisatakse
    b4.configure(command=lambda :nupp(4))         # a=[] listi e. saadud hinnete listi
    b5.configure(command=lambda :nupp(5))
    b6.configure(command= lambda :nupp(6))
    b7.configure(command=lambda :nupp(7))
    b8.configure(command=lambda :nupp(8))
    b9.configure(command=lambda :nupp(9))
    b10.configure(command=lambda :nupp(10))
    b11.configure(command=lambda :nupp(11))
    b12.configure(command=lambda :nupp(12))
    b13.configure(command=lambda :nupp(1))         #Siin on seadistatud, millis juhtub
    b14.configure(command=lambda :nupp(2))         # nupu vajutamisel ja milline
    b15.configure(command=lambda :nupp(3))         # väärtus b=[] järjendist lisatakse
    b16.configure(command=lambda :nupp(4))         # a=[] listi e. saadud hinnete listi
    b17.configure(command=lambda :nupp(5))
    b18.configure(command=lambda :nupp(6))
    b19.configure(command=lambda :nupp(7))
    b20.configure(command=lambda :nupp(8))
    b21.configure(command=lambda :nupp(9))
    b22.configure(command=lambda :nupp(10))
    b23.configure(command=lambda :nupp(11))
    b24.configure(command=lambda :nupp(12))

    välju.configure(command=välju1)
    min.configure(command=miinus1)
    
    #trikke_polnud.configure(command=trikke)
    mainloop( )
    



i=0 
nr = 1 #Hindamislehed on nummerdatud
hinded=[]
miinused=[]

for read in f:
    võistleja = read.upper() #loeb registreerinud võistlejate failist esimese võistleja nime. Peale tsükli läbimist järgmise võistleja.
    avame_hinnetelehe(võistleja) #avame_hinnetelehe(võistleja) #lisab failist saadud võistleja nime hinnetelehele
   
    summa = sum(hinded[i])
    hinne = summa - miinused[i]
    keskmine = round((hinne)/ len(hinded[i]), 1)
    print("HINDAMISLEHT nr. " + str(nr))
    print("Võistleja: " + read + "Hinded on: " + str(hinded[i]))
    print("Hinnete summa: " + str(summa))
    print("Miinuseid kokku: -" + str(miinused[i]))
    print("Hinne kokku " + str(hinne))
    print("Hinnete keskmine: " + str(keskmine)) 
    print()
    protokoll = open("protokollid.txt", "a", encoding="UTF-8") #avab protokolli faili, kuhu kirjutab hindamislehe protokolli
    protokoll.write("\nHINDAMISLEHT NR: " + str(nr) +"\n")
    protokoll.write(str(kuupäev_kellaeg))
    protokoll.write("\nVõistleja: " + võistleja + "Hinded: " + str(hinded[i]))
    protokoll.write("\nHinnete summa: " + str(summa))
    protokoll.write("\nMiinuseid kokku: " + str(miinused[i]))
    protokoll.write("\nHinne kokku " + str(summa - miinused[i]))
    protokoll.write("\nHinnete keskmine: " + str(keskmine) +"\n")
    protokoll.close()
    
    f = open("tulemused.txt", "a", encoding="UTF-8") #avab protokolli faili, kuhu kirjutab võistleja tulemused
    f.write( "\n" + võistleja + str(hinne) + "\n" )
    f.close()

    
    i += 1
    nr += 1
