class Player :
    def __init__(self,name):
        self.name = name
        self.__age = "34"
  
    def getName(self):
        return self.name

    def getAge(self):
        return self.__age


class Playerbwi(Player):
    def getSkill(self):
        return "fast"

player = Playerbwi("AHMADA")

player.name = 'ahmada junior' #untuk mengganti nama
print(player.getName() + " -- " + player.getAge())
