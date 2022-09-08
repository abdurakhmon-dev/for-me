class User:
    def __init__(self,fullname,age,username,password):
        self.fullname = fullname
        self.username = username
        self.__password = password
        self.age = age

    def user_info(self):
        return(f"""
        Username: {self.username}
        Full name: {self.fullname}
        """)
    
    def showPassword(self):
        return self.__password
    
    def changeName(self,newName):
        self.fullname = newName


user1 = User("samad",34,"samad45","qwert45")
user2 = User("ABdullo",12,"samad45","qwert45")
user3 = User("Asadbek",18,"samad45","qwert45")
user4 = User("Qodir",27,"samad45","qwert45")
user5 = User("Bobur",11,"samad45","qwert45")
user6 = User("Laziz",45,"samad45","qwert45")
user7 = User("humoyun",35,"samad45","qwert45")

lst = [user1, user2,user3,user4,user5,user6,user7]

for i in range(len(lst)):
    for j in range(len(lst)):
        if(lst[i].age < lst[j].age):
            lst[i].age,lst[j].age = lst[j].age,lst[i].age

for user in lst:
    print(user.)









