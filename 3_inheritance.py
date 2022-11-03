class Player :
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

class Playerbwi(Player):
    def setAgePlayer(self, age):
        self.age = age
        return self.age

pemain = Playerbwi('Ahmada', '47')


print(pemain.getName() + " berkecepatan " + pemain.getSpeed() + " dan berumur " + pemain.setAgePlayer('17'))