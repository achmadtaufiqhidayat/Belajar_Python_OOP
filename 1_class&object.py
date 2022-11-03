class Player:#nama kelas disesuaikan nama file, namun menggunakan huruf besar
    name = 'Rooney'
    nama2 = ""

#self dan ditambah .name untuk mengaksee parameter atau variable name
    def getName(self, nama2): #self daapat diartika n kelasnya sendiri untuk mengakses variable didalam kelas
        #return self.name
        self.nama2 = nama2
        return self.nama2

#diluar kelas
pemaim = Player()
print(pemaim.name)#cara 1
print(pemaim.getName("susi")) #mengambil berdasarkan fungsinya

