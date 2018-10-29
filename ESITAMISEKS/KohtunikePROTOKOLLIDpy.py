"""
Programm: Lohesurfi vastiili hindavate kohtunike hindamislehed ja protokoll
Autor: Kerli Otti

Kirjutasin antud programmi reaalsest vajadusest.
Programm on edasiarendus Programmeerimine I lõputööst.
Lohesurfi võistlust hinnates peab kohtunik jälgima suure tuule ja vihma käes
võistlejat ning suutma kiirelt kirja panema nähtud soorituse (triki) ja selle hinde.
Iga kohtuniku hindamisest tuleb säilitada protokoll.

Programm:
a)  Registreerib hindamislehti täitva kohtuniku nime ja aja, mil ta võistlejat hindab.
b)  Jälgib reeglites lubatud soorituste arvu ühe võistleja kohta (max 7).
c)  Avab nuppudega hindamislehe, kus iga triki (nupu nimi) on võetud failist.
    Iga nupp on seotud failist saadud väärtusega (rida-kahekordne järjend-sõnastik).
    Kui nuppu vajutatakse, siis lisatakse hindeks vastava triki väärtuse e. punktisumma.
d)  Võtab osalejate nimed failist ja laseb hinnata a) lubatud soorituste arvuni  või b) kui
    vajutatakse nuppu "VÄLJU LEHELT". Eraldi nupuna on "LISA -1", millega saab võtta punkte maha,
    kui sooritus ei olnud väärtusele kohane. Miinused arvutatakse hiljem maha punktisummast.
e)  Kirjutab kohtuniku hindamisest protokolli iga võistleja kohta (automaatne aeg, nimi, soorituste
    hinded, miinused, punktisumma kokku ja soorituste keskmine hinne) 
f)  Kirjutab võistleja lõpliku punktisummaeraldi faili. Sellesse faili peaksid salvestuma ka
    teiste kohtunike poolt saadud tulemused ja mida saab tulevikus kasutada lõplike võistlustulemuste
    genereerimisel. 

Vajalikud failid:
Nuppudele nime ja väärtuse jaoks kuni 12 reaga fail, milles sisaldub ühel real triki nimi ja arvuline
väärtus (float) eraldatud tühikuga (trikid.txt)
Osalejate registreerimisleht e võistlejate nimedega fail (võistlejad.txt)
Antud hinnete kokkuvõtted e protokoll (protokoll.txt)
Tulemuste fail, kuhu salvestatakse vaid võistleja nimi ja punktisumma (tulemused.txt)
Graafiline programm (easygui.py)

"""
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
    win.geometry("1080x1900") #siin saab muuta hindamisel kasutatava ekraani mõõtmeid
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

    #................................................
    Label(win, text="VÕISTLEJA:").grid(row=1)
    Label(win, text=võistleja).grid(row=2)
    Label(win, text="VÕISTLEJA:").grid(row=1)
    Label(win, text="HINDAV KOHTUNIK:").grid(row=1, column=4)
    Label(win, text=kohtunik).grid(row=2, column=4)
    välju= Button(win, text='KATKESTAS')
    välju.grid(row=3)
    min = Button(win, text=' LISA -1 ')
    min.grid(row=4)
    #trikke_mitu=Button(win, text=' TRIKKE "0" ')
    #trikke_mitu.grid(row=5)
    
    #................................................
    """12 nupu vajutamisega kaasnevad funktsioonid"""
    #selleks, et nupule vajutamisel tekiks mitmekordne järjend saadud hinnetest,
    #mida hiljem töödelda/protokollida. str tehakse floatiks, et
    # srvutada hinnete keskmiseid, summat saadud järjendist
    def nupp1():
        a.append(float(b[c[i]]))
        lisa_katse()
    def nupp2():
        a.append(float(b[c[i+1]]))
        lisa_katse()
    def nupp3():
        a.append(float(b[c[i+2]]))
        lisa_katse()
    def nupp4():
        a.append(float(b[c[i+3]]))
        lisa_katse()
    def nupp5():
        a.append(float(b[c[i+4]]))
        lisa_katse()
    def nupp6():
        a.append(float(b[c[i+5]]))
        lisa_katse()
    def nupp7():
        a.append(float(b[c[i+6]]))
        lisa_katse()
    def nupp8():
        a.append(float(b[c[i+7]]))
        lisa_katse()
    def nupp9():
        a.append(float(b[c[i+8]]))
        lisa_katse()
    def nupp10():
        a.append(float(b[c[i+9]]))
        lisa_katse()
    def nupp11():
        a.append(float(b[c[i+10]]))
        lisa_katse()
    def nupp12():
        a.append(float(b[c[i+11]]))
        lisa_katse()
    def välju1(): # rakendub kui katsete arv on täis
        if a == []: # kui pole trikke, siis rpannakse kõik 0
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
    b1.configure(command=nupp1)         #Siin on seadistatud, millis juhtub
    b2.configure(command=nupp2)         # nupu vajutamisel ja milline
    b3.configure(command=nupp3)         # väärtus b=[] järjendist lisatakse
    b4.configure(command=nupp4)         # a=[] listi e. saadud hinnete listi
    b5.configure(command=nupp5)
    b6.configure(command=nupp6)
    b7.configure(command=nupp7)
    b8.configure(command=nupp8)
    b9.configure(command=nupp9)
    b10.configure(command=nupp10)
    b11.configure(command=nupp11)
    b12.configure(command=nupp12)
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
    avame_hinnetelehe(võistleja) #lisab failist saadud võistleja nime hinnetelehele
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