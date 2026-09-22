class Oqituvchi:
    def __init__(self, ism, fan, tajriba):
        self.ism = ism
        self.fan = fan
        self.tajriba = tajriba

    def malumot(self):
        print(f"O'qituvchi: {self.ism}, Fani: {self.fan}, Tajribasi: {self.tajriba} yil")


class Taom:
    def __init__(self, nomi, narxi, turi):
        self.nomi = nomi
        self.narxi = narxi
        self.turi = turi

    def malumot(self):
        print(f"Taom: {self.nomi}, Narxi: {self.narxi} so'm, Turi: {self.turi}")


class Kompyuter:
    def __init__(self, nomi, ram, xotira):
        self.nomi = nomi
        self.ram = ram
        self.xotira = xotira

    def yoqish(self):
        print(f"{self.nomi} kompyuteri yoqildi.")


class Telefon:
    def __init__(self, model, batareya):
        self.model = model
        self.batareya = batareya

    def zaryad(self, miqdor):
        self.batareya += miqdor
        if self.batareya > 100:
            self.batareya = 100
        print(f"Batareya quvvati: {self.batareya}%")


class Futbolchi:
    def __init__(self, ism, jamoa, gol):
        self.ism = ism
        self.jamoa = jamoa
        self.gol = gol

    def gol_urdi(self):
        self.gol += 1
        print(f"Gollar soni: {self.gol}")


class Mahsulot:
    def __init__(self, nomi, narxi, soni):
        self.nomi = nomi
        self.narxi = narxi
        self.soni = soni

    def sotish(self, miqdor):
        if self.soni >= miqdor:
            self.soni -= miqdor
            print(f"Qoldi: {self.soni} ta")
        else:
            print("Yetarli mahsulot yo'q")


class Uy:
    def __init__(self, manzil, xonalar, qavat):
        self.manzil = manzil
        self.xonalar = xonalar
        self.qavat = qavat

    def malumot(self):
        print(f"Manzil: {self.manzil}, Xonalar: {self.xonalar}, Qavat: {self.qavat}")


class Transport:
    def __init__(self, tezlik):
        self.tezlik = tezlik

    def harakat(self):
        print(f"{self.tezlik} km/s tezlikda harakat")


class Mashina(Transport):
    def __init__(self, tezlik, model):
        super().__init__(tezlik)
        self.model = model


class Hayvon:
    def yemish(self):
        pass


class Sher(Hayvon):
    def yemish(self):
        print("Go'sht")


class Sigir(Hayvon):
    def yemish(self):
        print("O't")


class Talaba:
    def __init__(self, ism, kurs, ball):
        self.ism = ism
        self.kurs = kurs
        self.ball = ball

    def imtihon(self, yangi_ball):
        self.ball += yangi_ball
        if self.ball > 60:
            print("O‘tdi")
