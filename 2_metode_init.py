class Player :
    name = ''
    speed = ''

    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

pemain = Player('Ahmada', '47')
pemain2 = Player('Benzema', '56')

print(pemain.getName() + " punya kecepatan " + pemain.getSpeed())
print(pemain2.getName() + " punya kecepatan " + pemain2.getSpeed())