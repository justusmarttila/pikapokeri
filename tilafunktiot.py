import pokerivoitto

def alku_tilanne(self):
    for i in range(8):
        self.naytto.blit(self.kortti, (self.kierroksen_kortit[i][0], self.kierroksen_kortit[i][1]))
    self.pakka_sekoitettu = False
    self.tuplattiin = False
    

def normi_kierros_jako(self):
    for i in range(8):
        self.naytto.blit(self.kortti, (self.kierroksen_kortit[i][0], self.kierroksen_kortit[i][1]))

    if not self.pakka_sekoitettu:
        self.sekoita_pakka()

    for i in range(8):
        if i == 3 or i == 6:
            apu = 15
        elif i == 4 or i == 7:
            apu = 30
        elif i == 5:
            apu = 0
        if i<3:
            if self.kierroksen_kortit[i][0] <= self.paikat[i][0]:
                self.kierroksen_kortit[i][0] += self.nopeus
            if self.kierroksen_kortit[i][1] <= self.paikat[i][1]:
                self.kierroksen_kortit[i][1] += self.nopeus
        elif i<5:
            if self.kierroksen_kortit[i][0] <= self.paikat[2][0]:
                self.kierroksen_kortit[i][0] += self.nopeus
            
            if self.kierroksen_kortit[i][1] <= self.paikat[2][1]+apu:
                self.kierroksen_kortit[i][1] += self.nopeus
        else:
            if self.kierroksen_kortit[i][0] <= self.paikat[3][0]:
                self.kierroksen_kortit[i][0] += self.nopeus
            
            if self.kierroksen_kortit[i][1] <= self.paikat[3][1]+apu:
                self.kierroksen_kortit[i][1] += self.nopeus
            
            if self.kierroksen_kortit[7][1] >= self.paikat[3][1]+30 and self.kierroksen_kortit[7][0] >= self.paikat[3][0]:
                self.normi_jako = False
                self.normi_peli = True

    if self.normi_peli:
        for i in range(8):
            self.kierroksen_kortit[i] = [self.pakka_x, self.pakka_y]

def normi_kierros_pelaus(self):
    if not (self.vasen_valinta or self.oikea_valinta):
        self.naytto.blit(self.kortti, (self.paikat[2][0], self.paikat[2][1]))
        self.naytto.blit(self.kortti, (self.paikat[2][0], self.paikat[2][1]+15))
        self.naytto.blit(self.kortti, (self.paikat[3][0], self.paikat[3][1]))
        self.naytto.blit(self.kortti, (self.paikat[3][0], self.paikat[3][1]+15))

        self.kortti_1, self.kortti_2, self.kortti_3, self.kortti_4 = self.kortit[0], self.kortit[1], self.kortit[2], self.kortit[3]

        for i in range(4):
            if i>1:
                self.naytto.blit(self.kortit[i][2], (self.paikat[i][0], self.paikat[i][1]+30))
            else:
                self.naytto.blit(self.kortit[i][2], (self.paikat[i][0], self.paikat[i][1]))
    elif self.vasen_valinta:
        if self.vasen_valinta_kortti_1_x <= self.paikat[3][0]:
            self.vasen_valinta_kortti_1_x += self.nopeus
        if self.vasen_valinta_kortti_1_y <= self.paikat[3][1]:
            self.vasen_valinta_kortti_1_y += self.nopeus

        if self.vasen_valinta_kortti_2_x <= self.paikat[4][0]:
            self.vasen_valinta_kortti_2_x += self.nopeus
        if self.vasen_valinta_kortti_2_y <= self.paikat[4][1]:
            self.vasen_valinta_kortti_2_y += self.nopeus

        if self.vasen_valinta_kortti_2_x <= self.paikat[4][0]:
            self.naytto.blit(self.kortti, (self.vasen_valinta_kortti_1_x, self.vasen_valinta_kortti_1_y))
            self.naytto.blit(self.kortti, (self.vasen_valinta_kortti_2_x, self.vasen_valinta_kortti_2_y))
        else:
            self.naytto.blit(self.kortit[4][2], (self.paikat[3][0], self.paikat[3][1]))
            self.naytto.blit(self.kortit[5][2], (self.paikat[4][0], self.paikat[4][1]))
            self.tarkista_voitto = True
            self.normi_peli = False
            self.vasen_valinta = False
            valinta_kortit(self)

        for i in range(3):
            self.naytto.blit(self.kortit[i][2], (self.paikat[i][0], self.paikat[i][1]))
        
        self.valittu_rivi = [self.kortit[0], self.kortit[1], self.kortit[2], self.kortit[4], self.kortit[5]]

    elif self.oikea_valinta:
        for i in range(2):
            self.naytto.blit(self.kortit[i][2], (self.paikat[i][0], self.paikat[i][1]))
        
        if self.oikea_valinta_kortti_1_x >= self.paikat[2][0]:
            self.oikea_valinta_kortti_1_x -= self.nopeus
        if self.oikea_valinta_kortti_1_y <= self.paikat[2][1]:
            self.oikea_valinta_kortti_1_y += self.nopeus

        if self.oikea_valinta_kortti_2_x <= self.paikat[4][0]:
            self.oikea_valinta_kortti_2_x += self.nopeus
        if self.oikea_valinta_kortti_2_y <= self.paikat[4][1]:
            self.oikea_valinta_kortti_2_y += self.nopeus

        if self.oikea_valinta_kortti_2_x <= self.paikat[4][0]:
            self.naytto.blit(self.kortti, (self.oikea_valinta_kortti_1_x, self.oikea_valinta_kortti_1_y))
            self.naytto.blit(self.kortti, (self.oikea_valinta_kortti_2_x, self.oikea_valinta_kortti_2_y))
        else:
            self.naytto.blit(self.kortit[6][2], (self.paikat[2][0], self.paikat[2][1]))
            self.naytto.blit(self.kortit[7][2], (self.paikat[4][0], self.paikat[4][1]))
            self.tarkista_voitto = True
            self.normi_peli = False
            self.oikea_valinta = False
            valinta_kortit(self)

        self.naytto.blit(self.kortit[3][2], (self.paikat[3][0], self.paikat[3][1]))
        self.valittu_rivi = [self.kortit[0], self.kortit[1], self.kortit[6], self.kortit[3], self.kortit[7]]

def voiton_tarkistus(self):
    for i in range(5):
        self.naytto.blit(self.valittu_rivi[i][2], (self.paikat[i][0], self.paikat[i][1]))
    
    pokeri_kasi = [[kortti[0], kortti[1]] for kortti in self.valittu_rivi]
    self.voiton_nimi, self.voitto_kerroin = pokerivoitto.pokerivoitto(pokeri_kasi)
    if self.voitto_kerroin != -1:
        self.voitto = True
    
def tuplaus_jakaminen(self):
    for i in range(5):
        if self.kierroksen_kortit[i][0] <= self.paikat[i][0]:
            self.kierroksen_kortit[i][0] += self.nopeus
        if self.kierroksen_kortit[i][1] <= self.paikat[i][1]:
            self.kierroksen_kortit[i][1] += self.nopeus

    if self.kierroksen_kortit[4][1] >= self.paikat[4][1] and self.kierroksen_kortit[4][0] >= self.paikat[4][0]:
        self.naytto.blit(self.kortit[0][2], (self.paikat[0][0], self.paikat[0][1]))
        for i in range(1, 5):
            self.naytto.blit(self.kortti, (self.kierroksen_kortit[i][0], self.kierroksen_kortit[i][1]))
        self.tuplaus_jako_valmis = True
        self.tuplaus = False
    else:
        for i in range(5):
            self.naytto.blit(self.kortti, (self.kierroksen_kortit[i][0], self.kierroksen_kortit[i][1]))

def tuplaus_peli(self):
    self.naytto.blit(self.kortit[0][2], (self.paikat[0][0], self.paikat[0][1]))
    if not self.pakka_sekoitettu:
        self.sekoita_pakka()

    if self.tuplaus_valinta != -1:
        if self.tuplaus_valinta == 1:
            self.naytto.blit(self.kortit[1][2], (self.paikat[1][0], self.paikat[1][1]))
            for i in range(2, 5):
                self.naytto.blit(self.kortti, (self.kierroksen_kortit[i][0], self.kierroksen_kortit[i][1]))
        elif self.tuplaus_valinta == 2:
            self.naytto.blit(self.kortit[2][2], (self.paikat[2][0], self.paikat[2][1]))
            self.naytto.blit(self.kortti, (self.kierroksen_kortit[1][0], self.kierroksen_kortit[1][1]))
            for i in range(3, 5):
                self.naytto.blit(self.kortti, (self.kierroksen_kortit[i][0], self.kierroksen_kortit[i][1]))
        elif self.tuplaus_valinta == 3:
            self.naytto.blit(self.kortit[3][2], (self.paikat[3][0], self.paikat[3][1]))
            self.naytto.blit(self.kortti, (self.kierroksen_kortit[4][0], self.kierroksen_kortit[4][1]))
            for i in range(1, 3):
                self.naytto.blit(self.kortti, (self.kierroksen_kortit[i][0], self.kierroksen_kortit[i][1]))
        elif self.tuplaus_valinta == 4:
            self.naytto.blit(self.kortit[4][2], (self.paikat[4][0], self.paikat[4][1]))
            for i in range(1, 4):
                self.naytto.blit(self.kortti, (self.kierroksen_kortit[i][0], self.kierroksen_kortit[i][1]))
        self.tuplaus_valittu = True
        self.tuplaus_jako_valmis = False
    else:
        for i in range(1, 5):
            self.naytto.blit(self.kortti, (self.kierroksen_kortit[i][0], self.kierroksen_kortit[i][1]))

    if self.tuplaus_valittu:
        for i in range(5):
            self.kierroksen_kortit[i] = [self.pakka_x, self.pakka_y]

def tuplaus_lopetus(self):
    for i in range(5):
        self.naytto.blit(self.kortit[i][2], (self.paikat[i][0], self.paikat[i][1]))

    if self.tuplaus_voitto:
        self.voitto = True
        self.tuplaus_valinta = -1
        self.tuplaus_voitto = False

def valinta_kortit(self):
    self.vasen_valinta_kortti_1_x, self.vasen_valinta_kortti_1_y = self.paikat[2][0], self.paikat[2][1]
    self.vasen_valinta_kortti_2_x, self.vasen_valinta_kortti_2_y = self.paikat[2][0], self.paikat[2][1]+15
    self.oikea_valinta_kortti_1_x, self.oikea_valinta_kortti_1_y = self.paikat[3][0], self.paikat[3][1]
    self.oikea_valinta_kortti_2_x, self.oikea_valinta_kortti_2_y = self.paikat[3][0], self.paikat[3][1]+15