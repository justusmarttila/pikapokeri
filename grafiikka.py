import pygame
import os

def tuplaus_voitot_talteen_napit(self):
    pygame.draw.rect(self.naytto, (255, 150, 50), (self.tuplaus_nappi_x, self.tuplaus_nappi_y, 200, 100), 0, 25)
    pygame.draw.rect(self.naytto, (255, 0, 0), (self.voitot_talteen_x, self.voitot_talteen_y, 200, 100), 0, 25 )
    self.naytto.blit(self.tuplaa_teksti, (self.leveys_ruutu-1260, self.korkeus_ruutu-113))
    self.naytto.blit(self.voitot_teksti, (self.leveys_ruutu-1010, self.korkeus_ruutu-128))
    self.naytto.blit(self.talteen_teksti, (self.leveys_ruutu-1015, self.korkeus_ruutu-95))

def voittotaulukko(self):
    self.naytto.blit(self.voitto_taulukko, (self.leveys_ruutu-960, self.korkeus_ruutu-900))
        
    if self.panos == 0.50:
        self.viiva_1_x, self.viiva_2_x = self.leveys_ruutu-730, self.leveys_ruutu-660
    elif self.panos == 1:
        self.viiva_1_x, self.viiva_2_x = self.leveys_ruutu-660, self.leveys_ruutu-580
    elif self.panos == 2:
        self.viiva_1_x, self.viiva_2_x = self.leveys_ruutu-580, self.leveys_ruutu-520
    elif self.panos == 3:
        self.viiva_1_x, self.viiva_2_x = self.leveys_ruutu-520, self.leveys_ruutu-450
    else: 
        self.viiva_1_x, self.viiva_2_x = self.leveys_ruutu-450, self.leveys_ruutu-380

    pygame.draw.line(self.naytto, (255, 255, 255), (self.viiva_1_x, (self.korkeus_ruutu-900)+self.voitto_taulukko.get_height()), (self.viiva_1_x, self.korkeus_ruutu-900), 3)
    pygame.draw.line(self.naytto, (255, 255, 255), (self.viiva_2_x, (self.korkeus_ruutu-900)+self.voitto_taulukko.get_height()), (self.viiva_2_x, self.korkeus_ruutu-900), 3)

def napit(self):
    self.pelaa_nappi_x, self.pelaa_nappi_y = self.leveys_ruutu-550, self.korkeus_ruutu-150
    pygame.draw.rect(self.naytto, (0, 255, 0), (self.pelaa_nappi_x, self.pelaa_nappi_y , 200, 100), 0, 25)
    self.panos_nappi_x, self.panos_nappi_y = self.leveys_ruutu-800, self.korkeus_ruutu-150
    pygame.draw.rect(self.naytto, (50, 100, 200), (self.panos_nappi_x, self.panos_nappi_y, 200, 100), 0, 25)

    pelaa_teksti = self.fontti.render("PELAA", True, (0, 0, 0))
    saldo_teksti = self.fontti.render(f"{self.saldo:.2f}€", True, (0, 0, 0))
    panos_teksti = self.fontti.render("PANOS", True, (0, 0, 0))
    panos_numero = self.fontti.render(f"{self.panos:.2f}", True, (0, 0, 0))
    self.voitto_maara_teksti = self.fontti.render(f"Voitat {self.voitto_maara*2:.2f}", True, (0, 0, 0))
    
    self.naytto.blit(pelaa_teksti, (self.leveys_ruutu-500, self.korkeus_ruutu-95))
    self.naytto.blit(saldo_teksti, (self.leveys_ruutu-500, self.korkeus_ruutu-128))
    self.naytto.blit(panos_teksti, (self.leveys_ruutu-750, self.korkeus_ruutu-95))
    self.naytto.blit(panos_numero, (self.leveys_ruutu-730, self.korkeus_ruutu-128))

    self.tuplaus_nappi_x, self.tuplaus_nappi_y = self.leveys_ruutu-1300, self.korkeus_ruutu-150
    self.voitot_talteen_x, self.voitot_talteen_y = self.leveys_ruutu-1050, self.korkeus_ruutu-150
    self.tuplaa_teksti = self.fontti.render("TUPLAA", True, (0, 0, 0))
    self.voitot_teksti = self.fontti.render("VOITOT", True, (0, 0, 0))
    self.talteen_teksti = self.fontti.render("TALTEEN", True, (0, 0, 0))
    self.mika_voitto = self.fontti.render(self.voiton_nimi, True, (0, 0, 0))

def voitto(self):
    if self.tuplaus_valittu or self.tuplaus or self.tuplaus_jako_valmis:
        self.naytto.blit(self.voitto_maara_teksti, (self.leveys_ruutu-1100, self.korkeus_ruutu-190))
    if self.voitto or (self.tuplaus_valittu and self.tuplaus_voitto):
        tuplaus_voitot_talteen_napit(self)
        ero = 27
        alku = 612
        if self.voiton_nimi == "Viitoset":
            voitto_viiva_1_y, voitto_viiva_2_y = self.korkeus_ruutu-(alku+10*ero), self.korkeus_ruutu-(alku+9*ero)
        elif self.voiton_nimi == "Kuningasvärisuora":
            voitto_viiva_1_y, voitto_viiva_2_y = self.korkeus_ruutu-(alku+9*ero), self.korkeus_ruutu-(alku+8*ero)
        elif self.voiton_nimi == "Värisuora":
            voitto_viiva_1_y, voitto_viiva_2_y = self.korkeus_ruutu-(alku+8*ero), self.korkeus_ruutu-(alku+7*ero)
        elif self.voiton_nimi == "Neloset":
            voitto_viiva_1_y, voitto_viiva_2_y = self.korkeus_ruutu-(alku+7*ero), self.korkeus_ruutu-(alku+6*ero)
        elif self.voiton_nimi == "Täyskäsi":
            voitto_viiva_1_y, voitto_viiva_2_y = self.korkeus_ruutu-(alku+6*ero), self.korkeus_ruutu-(alku+5*ero)
        elif self.voiton_nimi == "Väri":
            voitto_viiva_1_y, voitto_viiva_2_y = self.korkeus_ruutu-(alku+5*ero), self.korkeus_ruutu-(alku+4*ero)
        elif self.voiton_nimi == "Suora":
            voitto_viiva_1_y, voitto_viiva_2_y = self.korkeus_ruutu-(alku+4*ero), self.korkeus_ruutu-(alku+3*ero)
        elif self.voiton_nimi == "Kolmoset":
            voitto_viiva_1_y, voitto_viiva_2_y = self.korkeus_ruutu-(alku+3*ero), self.korkeus_ruutu-(alku+2*ero)
        elif self.voiton_nimi == "Kaksi paria":
            voitto_viiva_1_y, voitto_viiva_2_y = self.korkeus_ruutu-(alku+2*ero), self.korkeus_ruutu-(alku+ero)
        elif self.voiton_nimi == "10-A Pari":
            voitto_viiva_1_y, voitto_viiva_2_y = self.korkeus_ruutu-(alku+ero), self.korkeus_ruutu-alku

        pygame.draw.line(self.naytto, (255, 0, 0), (self.viiva_1_x, voitto_viiva_1_y), (self.viiva_2_x, voitto_viiva_1_y), 3)
        pygame.draw.line(self.naytto, (255, 0, 0), (self.viiva_1_x, voitto_viiva_2_y), (self.viiva_2_x, voitto_viiva_2_y), 3)
        self.naytto.blit(self.mika_voitto, (self.leveys_ruutu-1090, self.korkeus_ruutu-590))


def pakka_ja_kortti_paikat(self):
    self.korttipaikat = []
    for i in range(5):
        self.korttipaikat.append(pygame.draw.rect(self.naytto, (0, 50, 0), (self.leveys_ruutu-(1700-i*275), self.korkeus_ruutu-550, self.jokeri[2].get_width()+20, self.jokeri[2].get_height()+20), 0, 10))
    
    for i in range(7):
        self.naytto.blit(self.kortti, (200+3*i, 70+3*i))

def alusta_kuvat(self):
    self.apu_kortti = pygame.image.load(os.path.join("pictures", "black_joker.png")).convert()
    kortin_koko = (self.apu_kortti.get_width()-(self.apu_kortti.get_width()/1.8), self.apu_kortti.get_height()-(self.apu_kortti.get_height()/1.8))

    self.kortit = []
    maat = ["spades", "diamonds", "hearts", "clubs"]
    x, y = 0, 0
    for maa in maat:
        for i in range(1,14):
            kuva = pygame.image.load(os.path.join("pictures", f"{i}_of_{maa}.png")).convert()
            skaalattu = pygame.transform.scale(kuva, kortin_koko)
            kortti = [maa, i, skaalattu, x, y]
            self.kortit.append(kortti)
    
    self.jokeri = ("jokeri", 15, pygame.transform.scale(pygame.image.load(os.path.join("pictures", "red_joker.png")).convert(), kortin_koko))
    self.kortti = pygame.transform.scale(pygame.image.load(os.path.join("pictures", "card_backside.png")).convert(), kortin_koko)
    self.voitto_taulukko = pygame.image.load(os.path.join("pictures", "voittotaulukko.png")).convert()
    self.fontti = pygame.font.SysFont("Aharoni", 42)
    