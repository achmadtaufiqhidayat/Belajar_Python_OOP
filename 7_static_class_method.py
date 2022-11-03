class Player :
    job = "Pemain Bola"

    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name


    @staticmethod 
    def retiredIn(age):
        return str(50-age)

    @classmethod
    def generalIn(cls,age): 
        return cls.job + " akan pensiun dalam " + cls.retiredIn(age) + " tahun."

print(Player.generalIn(36))
