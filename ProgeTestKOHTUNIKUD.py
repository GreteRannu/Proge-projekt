
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
    teine=[] #Siia kogutakse TEISE võistlejale antud hinded selle kohtuniku pool
    h=2 #saab muuta nummude kaugust omavahel
    i=0 #saab nuppude tekstid võtta järjendist c
    r=20
    katseidA=[]
    katseidB=[]
    miinus=[]

    
    b1 = Button(win,text=c[i], height=h, width= r)
    b2 = Button(win,text=c[i+1], height=h, width= r)
    b3 = Button(win,text=c[i+2], height=h, width= r)

    
    b13 = Button(win,text=c[i], height=h, width= r)
    b14 = Button(win,text=c[i+1], height=h, width= r)
    b15 = Button(win,text=c[i+2], height=h, width= r)
  

    b1.grid(row=5, column=1)
    b2.grid(row=6, column=1)
    b3.grid(row=7, column=1)

    
    b13.grid(row=5, column=5)
    b14.grid(row=6, column=5)
    b15.grid(row=7, column=5)


    #................................................
    Label(win, text="VÕISTLEJA:").grid(row=1)
    Label(win, text=võistleja).grid(row=2)
    Label(win, text="VÕISTLEJA:").grid(row=1)
    Label(win, text="HINDAV KOHTUNIK:").grid(row=1, column=4)
    Label(win, text=kohtunik).grid(row=2, column=4)
    Label(win, text="Antud punktid A:").grid(row = 4, column = 4)
    Label(win, text="Hetkel pukte A:").grid(row = 6, column = 4)
    Label(win, text="Antud punktid B:").grid(row = 8, column = 4)
    Label(win, text="Hetkel pukte B:").grid(row = 10, column = 4)
    Label(win, text = sum(teine)) .grid(row = 11, column = 4)
    välju= Button(win, text='KATKESTAS')
    välju.grid(row=3)
    min = Button(win, text=' LISA -1 ')
    min.grid(row=4)
    #trikke_mitu=Button(win, text=' TRIKKE "0" ')
    #trikke_mitu.grid(row=5)
##    def naita_punkte(a):
##        for el in a:
##            "\n".join
##        Label(win, text = a). grid(row = 5, column = 4)
    def hetkel_punkte(a):
        Label(win, text = sum(a)) .grid(row = 7, column = 4)
        
    #................................................
    """12 nupu vajutamisega kaasnevad funktsioonid"""
    #selleks, et nupule vajutamisel tekiks mitmekordne järjend saadud hinnetest,
    #mida hiljem töödelda/protokollida. str tehakse floatiks, et
    # srvutada hinnete keskmiseid, summat saadud järjendist
    def nupp(nupp, voistleja):
        print(nupp)
        if voistleja == "a":
            a.append(float(b[c[nupp]]))
            lisa_katse("a")
        if voistleja == "b":
            teine.append(float(b[c[nupp]]))
            print(teine)
            lisa_katse("b")
        #b1 = Button(win,text=c[i], height=h, width= r)
       

    
    def välju1(): # rakendub kui katsete arv on täis
        if a == []: # kui pole trikke, siis pannakse kõik 0
            trikke()
        hinded.append(a)#lisab saadud hinded hined[] listi
        miinused.append(sum(miinus))
        win.destroy()   # lõpetab hindamislehe täitmise 
        return time.sleep(1)
    def lisa_katse(kellele):
        
        # def loendab katseid kuni 7-meni ja
        if kellele == "a":
            katseidA.append(1)
 #           naita_punkte(a) #ERRORIST VABAKS ENNE N"ITAB PUNKTID siis l]petab
            for el in a:
                "\n".join
                Label(win, text = len(a)). grid(row = 5, column = 4)
            #hetkel punkte
            Label(win, text = sum(a)) .grid(row = 7, column = 4)
            A=katseidA.count(1)
            B=katseidB.count(1)
            if A>=7:
                b1.configure(command=lambda :None)         #Siin on seadistatud, millis juhtub
                b2.configure(command=lambda :None)         # nupu vajutamisel ja milline
                b3.configure(command=lambda :None) 
        if kellele == "b":
            katseidB.append(1)
            #Punktid
            for el in teine:
                "\n".join
                Label(win, text = teine). grid(row = 9, column = 4)
            #Hetkel punkte
            Label(win, text = sum(teine)).grid(row = 11, column = 4)
            A=katseidA.count(1)
            B=katseidB.count(1)
            if B>=7:
                    b13.configure(command=lambda :None)         #Siin on seadistatud, millis juhtub
                    b14.configure(command=lambda :None)         # nupu vajutamisel ja milline
                    b15.configure(command=lambda :None) 
                       
        if A>=7 and B>=7:
            print("A=", a, "teine=", teine)
            välju1()
            
    def miinus1():
        miinus.append(int(1))
    def trikke():
        a.append(0.0)
        hinded.append(a)
                  
        
    #.......................................................................
    b1.configure(command=lambda :nupp(0, "a"))         #Siin on seadistatud, millis juhtub
    b2.configure(command=lambda :nupp(1, "a"))         # nupu vajutamisel ja milline
    b3.configure(command=lambda :nupp(2, "a"))         # väärtus b=[] järjendist lisatakse



    b13.configure(command=lambda :nupp(0, "b"))         #Siin on seadistatud, millis juhtub
    b14.configure(command=lambda :nupp(1, "b"))         # nupu vajutamisel ja milline
    b15.configure(command=lambda :nupp(2, "b"))         # väärtus b=[] järjendist lisatakse


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
    
    f = open("tulemused.txt", "w", encoding="UTF-8") #avab protokolli faili, kuhu kirjutab võistleja tulemused
    f.write( "\n" + võistleja + str(hinne) + "\n" )
    f.close()

    
    i += 1
    nr += 1

