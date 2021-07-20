class Sikeres: #Sikeres vizsgaadatok beolvasása
    def __init__(self,sor):
        split = sor.split(';')
        self.Nyelv=split[0]
        self.Evek = split[1:]
        self.Evszamok = [int(x) for x in self.Evek]
        self.Arany = {}
        self.Arany[self.Nyelv]=self.Arany.get(self.Nyelv, [x for x in self.Evek])

class Sikertelen(Sikeres): #Sikertelen  vizsgaadatok beolvasása
    def __init__(self, sor):
        super().__init__(sor)

#Beolvasás függvény
def Beolvasas(dokumentum, osztaly):
    with open(dokumentum,'r') as Beolvas:
        Beolvas.readline()
        return [osztaly(x.strip()) for x in Beolvas]

#Adatok beolvasása
sikeres = Beolvasas("sikeres.csv", Sikeres)
sikertelen = Beolvasas("sikertelen.csv", Sikertelen)

#Vizsgaadatok kigyűjtése
sikeresseg=dict()
sikertelenseg=dict()
osszegzes = dict()


#2. feladat:
for x in sikeres:
    sikeresseg[x.Nyelv]=sikeresseg.get(x.Nyelv,0)+sum(x.Evszamok)
for x in sikertelen:
    sikertelenseg[x.Nyelv]=sikertelenseg.get(x.Nyelv,0)+sum(x.Evszamok)
    osszegzes[x.Nyelv]=osszegzes.get(x.Nyelv,0)+(sikeresseg[x.Nyelv]+sikertelenseg[x.Nyelv])

sorrend =sorted(osszegzes.items(), key=lambda x : x[1], reverse=True)
print("2. feladat: A legnépszerűbb nyelvek:")
i=0
for i in range(3):
    print(f"\t{sorrend[i][0]}")

#3. feladat:
print("3. feladat:")
vizsgalando = int(input("\tVizsgálandó év: "))
while vizsgalando>2018 or vizsgalando<2009:
    vizsgalando = int(input("\tVizsgálandó év: "))
ev = (2009-vizsgalando)*-1
max = {}
for x in range(len(sikeres)):
   try:
        siker = sikeres[x].Evszamok[ev]
        sikerte=sikertelen[x].Evszamok[ev]
        max[sikeres[x].Nyelv]=max.get(sikeres[x].Nyelv,0+float((sikerte/(siker+sikerte))*100))
   except :
        max[sikeres[x].Nyelv]=0
max = sorted(max.items(), key =lambda x: x[1], reverse = True)


#4.feladat:
print(f"4. feladat: {vizsgalando} évben {max[0][0]} nyelvből sikertelen vizsgák aránya: {max[0][1]:.2f}%")

#5. feladat:
print("5. feladat:")
[print(f"\t{x[0]}") for x in max if x[1]==0.0]


#6. feladat:
print("6. feladat: osszesites.txt")
with open("osszesites.txt","w") as kiiras:
    for x,y in osszegzes.items():
        szazalek= float((sikeresseg[x]/osszegzes[x])*100)
        kiiras.write(f"{x};{y};{szazalek:.2f}%\n")