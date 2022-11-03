class Player :
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed
    
    def getSkill(self):
        return 'normal'


class Playerbwi(Player):
    def getSkill(self):
        return "fast"

class PlayerBLI(Player):
    def getSkill(self):
        return "strenght"
class PlayerSL(Player):
    pass

player = Playerbwi('Taufiq', '77')
print(player.getName() + " skill " + player.getSkill())

player2 = PlayerSL("Hidayat", '54')
print(player2.getName() + " skill "  + player2.getSkill())