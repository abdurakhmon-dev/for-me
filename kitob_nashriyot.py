class kitob:
    def __init__(self,nomi,muallifi,narxi,nashriyoti):
        self.name = nomi
        self.autor = muallifi
        self.price = narxi
        self.publish = nashriyoti
    
    def show(self):
        print(f"""Book name: {self.name}
Book author: {self.autor}
Book price: {self.price}
Book publish: {self.publish}""")
book1 = kitob("Baxtiyor oila","Muhammad Sodiq Muhammad Yusuf",63000,"Hilol nashr")
book2 = kitob("Daftar hoshiyasidagi bitiklar","O'tkir Hoshimov",25000,"Sharq nashr")
book3 = kitob("Sariq devni minib","Xudoyberdi To'xtaboyev",30000,"Bunyodkor")
book4 = kitob("Vatan","Muhammad Yusuf",15000,"G'afur G'ulom")
book5 = kitob("Kuyla","Mirkarim Osim",20000,"Meros")
books = [book1,book2,book3,book4,book5]
for i in books:
    if(i.name[0] in "ABCDEFGabcdefg"):
        i.show()
        print("=============================")

        