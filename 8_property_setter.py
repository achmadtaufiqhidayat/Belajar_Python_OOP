class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @property
    def infoPlayer(self):
        return self.name + " berusia " + self.age


    @infoPlayer.setter
    def infoPlayer(self, data):
        name, age = data.split(' ')
        self.name = name
        self.age = age

player = Player('Dybala', '22')
player.infoPlayer = 'WhineRooney 34'
print(player.infoPlayer)

