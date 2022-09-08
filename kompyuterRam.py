class kompyuter:
    def __init__(self,nomi,rami,narxi,protsessori):
        self.name = nomi
        self.ram = rami
        self.price = narxi
        self.prossor = protsessori
    def show(self):
        print(f"""Komputer name: {self.name}
Komputer name: {self.name}
Komputer ram: {self.ram}
Komputer price: {self.price}
Komputer prossor: {self.prossor}""")
komputer1 = kompyuter("Asus",4,350,"Intel")
komputer2 = kompyuter("Lenovo",8,550,"Intel")
komputer3 = kompyuter("Acer",8,500,"Amd")
komputer4 = kompyuter("Macbook",32,950,"IOS")
komputer5 = kompyuter("Victus",16,750,"Amd")
komputer6 = kompyuter("MSI",32,750,"Intel")
komputers = [komputer1,komputer2,komputer3,komputer4,komputer5,komputer6]
for i in komputers:
    if(i.ram > 4 and i.ram < 16):
        i.show()
        print("====================")