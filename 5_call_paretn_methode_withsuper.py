class Player :
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed
    
    def getSkill(self):
        return 'normal'


class Playerbwi(Player):
    def __init__(self,name):
        super().__init__(name)
        print ("Hello Banyuwangi")
    def getSkill(self):
        return "fast"


player = Playerbwi('Taufiq Hidayat')
print(player.getName() + " skill " + player.getSkill())
