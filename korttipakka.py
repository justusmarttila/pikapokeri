import random

class Kortti:
    def __init__(self, maa: str, numero: int, kuva: str, x_koord, y_koord):
        self.maa = maa
        self.numero = numero
        self.x_koord = 0
        self.y_koord = 0
        self.kuva = kuva

    def kuva_func(self):
        return self.kuva

    def __str__(self):
        return f"{self._maa} {self._numero}"

class Korttipakka:
    def __init__(self):
        self.kortit = []
        maat = ["pata", "risti", "hertta", "ruutu"]
        for maa in maat:
            for i in range(1,14):
                self.kortit.append(Kortti(maa, i))

    def sekoita(self):
        random.shuffle(self.kortit)

    def tulosta_kortit(self):
        for kortti in self.kortit:
            print(kortti)

    def kaikki_kortit(self):
        return self.kortit

if __name__ == "__main__":
    korttipakka = Korttipakka()
    korttipakka.sekoita()
    kortit = korttipakka.kaikki_kortit()
    for kortti in kortit:
        print(kortti)
    

    

