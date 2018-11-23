f = open("võistlejad.txt", "r", encoding="UTF-8")
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
b=(failist_sonastik(f))
c=[]                    
for element in b:      
    c.append(element)

#b1 = Button(win,text=c[i], height=h, width= r)
#b2 = Button(win,text=c[i+1], height=h, width= r)

#b1.grid(row=5, column=1)
#b2.grid(row=6, column=1)
def nupp(i):
        print(float(b[c[i]]))
        print(c[i])
        #b1 = Button(win,text=c[i], height=h, width= r)
        #b1.grid(row=i+5, column=1)
        
print(c)
i = 14
while i <= 14:
    nupp(i)
    i -= 1
#b1.configure(command=nupp1) 
#b2.configure(command=nupp2)
