def viitoset(rivi: list):
    for i in range(len(rivi)):
        if rivi[i][0] == "jokeri":
            rivi.pop(i)
            break
    else:
        return False
    numero = rivi[0][1]
    if rivi[1][1] == numero and rivi[2][1] == numero and rivi[3][1] == numero:
        return True
    return False 

def kuningasvarisuora(rivi: list):
    maat_samat = False
    assa = False
    kymppi = False
    jatka = False
    kuningatar = False
    kunkku = False

    maa = rivi[0][0]
    if rivi[1][0] == maa and rivi[2][0] == maa and rivi[3][0] == maa and rivi[4][0] == maa:
        maat_samat = True

    for i in range(len(rivi)):
        if rivi[i][1] == 1:
            assa = True
        elif rivi[i][1] == 10:
            kymppi = True
        elif rivi[i][1] == 11:
            jatka = True
        elif rivi[i][1] == 12:
            kuningatar = True
        elif rivi[i][1] == 13:
            kunkku = True
    
    if assa and kunkku and kuningatar and jatka and kymppi and maat_samat:
        return True
    return False

def varisuora(rivi: list):
    maat_samat = False
    maa = rivi[0][0]
    if rivi[1][0] == maa and rivi[2][0] == maa and rivi[3][0] == maa and rivi[4][0] == maa:
        maat_samat = True
  
    pienin = min(rivi, key=lambda kortti: kortti[1])
    suurin = max(rivi, key=lambda kortti: kortti[1])
    if pienin[1]+4 == suurin[1] and maat_samat:
        return True
    return False

def neloset(rivi: list):
    numerot = [kortti[1] for kortti in rivi]
    for numero in numerot:
        maara = numerot.count(numero)
        if maara == 4:
            return True
    return False

def tayskasi(rivi: list):
    numerot = [kortti[1] for kortti in rivi]
    numerot = list(dict.fromkeys(numerot))
    if len(numerot) == 2:
        return True
    return False

def vari(rivi: list):
    maat = [kortti[0] for kortti in rivi]
    maat = list(dict.fromkeys(maat))
    if len(maat) == 1:
        return True
    return False

def suora(rivi: list):
    kymppi = False
    assa = False
    suora = False
    for i in range(len(rivi)):
        if rivi[i][1] == 1:
            indeksi = i
        elif rivi[i][1] == 10:
            kymppi = True
    
    if kymppi and assa:
        rivi[indeksi][1] = 14
    pienin = min(rivi, key=lambda kortti: kortti[1])
    suurin = max(rivi, key=lambda kortti: kortti[1])
    
    if pienin[1]+5 == suurin[1]:
        suora = True
    if kymppi and assa:
        rivi[indeksi][1] = 1
    return suora

def kolmoset(rivi: list):
    numerot = [kortti[1] for kortti in rivi]
    for numero in numerot:
        if numerot.count(numero) == 3:
            return True
    return False

def kaksi_paria(rivi: list):
    numerot = [kortti[1] for kortti in rivi]
    numerot = list(dict.fromkeys(numerot))
    if len(numerot) == 3:
        return True
    return False

def kymppi_A_pari(rivi: list):
    numerot = [kortti[1] for kortti in rivi]
    for numero in numerot:
        if (10<=numero<=13 or numero == 1) and numerot.count(numero) == 2:
            return True
    return False

def pokerivoitto(rivi: list):
    if viitoset(rivi):
        return "Viitoset", 100
    elif kuningasvarisuora(rivi):
        return "Kuningasvärisuora", 100
    elif varisuora(rivi):
        return "Värisuora", 75
    elif neloset(rivi):
        return "Neloset", 50
    elif tayskasi(rivi):
        return "Täyskäsi", 20
    elif vari(rivi):
        return "Väri", 15
    elif suora(rivi):
        return "Suora", 11
    elif kolmoset(rivi):
        return "Kolmoset", 5
    elif kaksi_paria(rivi):
        return "Kaksi paria", 3
    elif kymppi_A_pari(rivi):
        return "10-A Pari", 2
    else:
        return "ei voittoa", -1

if __name__ == "__main__":
    print(pokerivoitto([["pata", 6 ],["pata", 5],["pata", 6],["pata", 8],["risti", 9] ]))