import random
import pygame
import korttipakka
import pokerwin

class Pikapokeri:
    def __init__(self):
        pygame.init()
        self.alusta_kuvat()
        self.leveys_ruutu = 1918
        self.korkeus_ruutu = 1007

        self.pakka_x, self.pakka_y = 218, 88
        self.kierroksen_kortit = []
        for i in range(8):
            self.kierroksen_kortit.append([self.pakka_x, self.pakka_y])

        self.panos = 0.50
        self.saldo = 100
        self.nopeus = 20
        self.voitto_kerroin = 0
        self.voiton_nimi = "ei voittoa"

        self.alku = True
        self.jokeri_kierrokset = False
        self.normi_jako = False
        self.normi_peli = False
        self.tuplaus_jako = False
        self.tuplaus_peli = False
        self.pakka_sekoitettu = False
        self.vasen_valinta = False
        self.oikea_valinta = False
        self.tarkista_voitto = False
        self.peli_kaynnissa = False
        self.voitto = False
        self.talteen = False

        self.naytto = pygame.display.set_mode((self.leveys_ruutu, self.korkeus_ruutu))
        
        self.paikat = []
        for i in range(5):
            self.paikat.append([self.leveys_ruutu-(1693-275*i), self.korkeus_ruutu-545])

        self.__valinta_kortit()
        self.valittu_rivi = []

        pygame.display.set_caption("Pikapokeri")
        self.kello = pygame.time.Clock()
        self.paa_silmukka()

    def alusta_kuvat(self):
        self.apu_kortti = pygame.image.load("black_joker.png")
        kortin_koko = (self.apu_kortti.get_width()-(self.apu_kortti.get_width()/1.8), self.apu_kortti.get_height()-(self.apu_kortti.get_height()/1.8))

        self.kortit = []
        maat = ["spades", "diamonds", "hearts", "clubs"]
        x, y = 0, 0
        for maa in maat:
            for i in range(1,14):
                kuva = pygame.image.load(f"{i}_of_{maa}.png")
                skaalattu = pygame.transform.scale(kuva, kortin_koko)
                kortti = [maa, i, skaalattu, x, y]
                self.kortit.append(kortti)
        
        self.jokeri = ("jokeri", 14, pygame.transform.scale(pygame.image.load("red_joker.png"), kortin_koko))
        self.kortti = pygame.transform.scale(pygame.image.load("card_backside.png"), kortin_koko)
        self.fontti = pygame.font.SysFont("Aharoni", 42)
        self.voitto_taulukko = pygame.image.load("voittotaulukko.png")

    def piirra_grafiikka(self):
        self.naytto.fill((0, 100, 0))
        self.pelaa_nappi_x, self.pelaa_nappi_y = self.leveys_ruutu-550, self.korkeus_ruutu-150
        pygame.draw.rect(self.naytto, (0, 255, 0), (self.pelaa_nappi_x, self.pelaa_nappi_y , 200, 100), 0, 25)
        self.panos_nappi_x, self.panos_nappi_y = self.leveys_ruutu-800, self.korkeus_ruutu-150
        pygame.draw.rect(self.naytto, (50, 100, 200), (self.panos_nappi_x, self.panos_nappi_y, 200, 100), 0, 25)
        
        self.korttipaikat = []
        for i in range(5):
            self.korttipaikat.append(pygame.draw.rect(self.naytto, (0, 50, 0), (self.leveys_ruutu-(1700-i*275), self.korkeus_ruutu-550, self.jokeri[2].get_width()+20, self.jokeri[2].get_height()+20), 0, 10))

        pelaa_teksti = self.fontti.render("PELAA", True, (0, 0, 0))
        saldo_teksti = self.fontti.render(f"{self.saldo:.2f}€", True, (0, 0, 0))
        panos_teksti = self.fontti.render("PANOS", True, (0, 0, 0))
        panos_numero = self.fontti.render(f"{self.panos:.2f}", True, (0, 0, 0))
        
        self.naytto.blit(pelaa_teksti, (self.leveys_ruutu-500, self.korkeus_ruutu-95))
        self.naytto.blit(saldo_teksti, (self.leveys_ruutu-500, self.korkeus_ruutu-128))
        self.naytto.blit(panos_teksti, (self.leveys_ruutu-750, self.korkeus_ruutu-95))
        self.naytto.blit(panos_numero, (self.leveys_ruutu-730, self.korkeus_ruutu-128))

        self.tuplaus_nappi_x, self.tuplaus_nappi_y = self.leveys_ruutu-1300, self.korkeus_ruutu-150
        self.voitot_talteen_x, self.voitot_talteen_y = self.leveys_ruutu-1050, self.korkeus_ruutu-150
        tuplaa_teksti = self.fontti.render("TUPLAA", True, (0, 0, 0))
        voitot_teksti = self.fontti.render("VOITOT", True, (0, 0, 0))
        talteen_teksti = self.fontti.render("TALTEEN", True, (0, 0, 0))
        
        for i in range(7):
            self.naytto.blit(self.kortti, (200+3*i, 70+3*i))
        self.naytto.blit(self.voitto_taulukko, (self.leveys_ruutu-960, self.korkeus_ruutu-900))
        
        if self.panos == 0.50:
            viiva_1_x, viiva_2_x = self.leveys_ruutu-730, self.leveys_ruutu-660
        elif self.panos == 1:
            viiva_1_x, viiva_2_x = self.leveys_ruutu-660, self.leveys_ruutu-580
        elif self.panos == 2:
            viiva_1_x, viiva_2_x = self.leveys_ruutu-580, self.leveys_ruutu-520
        elif self.panos == 3:
            viiva_1_x, viiva_2_x = self.leveys_ruutu-520, self.leveys_ruutu-450
        else: 
            viiva_1_x, viiva_2_x = self.leveys_ruutu-450, self.leveys_ruutu-380

        pygame.draw.line(self.naytto, (255, 255, 255), (viiva_1_x, (self.korkeus_ruutu-900)+self.voitto_taulukko.get_height()), (viiva_1_x, self.korkeus_ruutu-900), 3)
        pygame.draw.line(self.naytto, (255, 255, 255), (viiva_2_x, (self.korkeus_ruutu-900)+self.voitto_taulukko.get_height()), (viiva_2_x, self.korkeus_ruutu-900), 3)

        if self.voitto:
            pygame.draw.rect(self.naytto, (255, 150, 50), (self.tuplaus_nappi_x, self.tuplaus_nappi_y, 200, 100), 0, 25)
            pygame.draw.rect(self.naytto, (255, 0, 0), (self.voitot_talteen_x, self.voitot_talteen_y, 200, 100), 0, 25 )
            self.naytto.blit(tuplaa_teksti, (self.leveys_ruutu-1260, self.korkeus_ruutu-113))
            self.naytto.blit(voitot_teksti, (self.leveys_ruutu-1010, self.korkeus_ruutu-128))
            self.naytto.blit(talteen_teksti, (self.leveys_ruutu-1015, self.korkeus_ruutu-95))
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

            pygame.draw.line(self.naytto, (255, 0, 0), (viiva_1_x, voitto_viiva_1_y), (viiva_2_x, voitto_viiva_1_y), 3)
            pygame.draw.line(self.naytto, (255, 0, 0), (viiva_1_x, voitto_viiva_2_y), (viiva_2_x, voitto_viiva_2_y), 3)

    def paa_silmukka(self):
        while True:
            self.tarkista_tapahtumat()
            self.piirra_naytto()

    def tarkista_tapahtumat(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    hiiri_x = event.pos[0]
                    hiiri_y = event.pos[1]
                    if self.normi_peli:
                        if self.paikat[2][0] <= hiiri_x <= self.paikat[2][0]+self.kortti.get_width() and self.paikat[2][1] <= hiiri_y <= self.paikat[2][1]+self.kortti.get_height():
                            self.vasen_valinta = True
                        elif self.paikat[3][0] <= hiiri_x <= self.paikat[3][0]+self.kortti.get_width() and self.paikat[3][1] <= hiiri_y <= self.paikat[3][1]+self.kortti.get_height():
                            self.oikea_valinta = True
                    if (self.pelaa_nappi_x <= hiiri_x <= self.pelaa_nappi_x+200 and self.pelaa_nappi_y <= hiiri_y <= self.pelaa_nappi_y+100) and (self.tarkista_voitto or self.alku) and not (self.normi_jako or self.normi_peli) and not (self.voitto) and (self.saldo>=self.panos):
                        if self.alku:
                            self.alku = False
                            self.normi_jako = True
                        elif self.tarkista_voitto:
                            self.normi_jako = True
                            self.sekoita_pakka()
                        if self.saldo-self.panos>=0:
                            self.saldo -= self.panos
                    if self.panos_nappi_x <= hiiri_x <= self.panos_nappi_x+200 and self.panos_nappi_y <= hiiri_y <= self.panos_nappi_y+100 and (not self.normi_peli) and (not self.normi_jako) and (not self.voitto):
                        if self.panos == 0.50:
                            self.panos = 1
                        elif self.panos<3:
                            self.panos +=1
                        elif self.panos == 3:
                            self.panos = 5
                        else:
                            self.panos = 0.50
                    if self.voitto and (self.voitot_talteen_x <= hiiri_x <= self.voitot_talteen_x+200 and self.voitot_talteen_y <= hiiri_y <= self.voitot_talteen_y+100):
                        self.voitto = False
                        self.alku = True
                        self.saldo += self.panos*self.voitto_kerroin
                
            if event.type == pygame.QUIT:
                exit()

    def piirra_naytto(self):
        self.piirra_grafiikka()
        self.tarkista_tila()

        if self.alku:
            self.alku_tilanne()
        elif self.normi_jako:
            self.normi_kierros_jako()
        elif self.normi_peli:
            self.normi_kierros_pelaus()
        elif self.tarkista_voitto:
            self.voiton_tarkistus()
        

        pygame.display.flip()
        self.kello.tick(60)

    def alku_tilanne(self):
        for i in range(8):
            self.naytto.blit(self.kortti, (self.kierroksen_kortit[i][0], self.kierroksen_kortit[i][1]))
        
        self.pakka_sekoitettu = False

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
                self.__valinta_kortit()

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
                self.__valinta_kortit()

            self.naytto.blit(self.kortit[3][2], (self.paikat[3][0], self.paikat[3][1]))

            self.valittu_rivi = [self.kortit[0], self.kortit[1], self.kortit[6], self.kortit[3], self.kortit[7]]

    def voiton_tarkistus(self):
        for i in range(5):
            self.naytto.blit(self.valittu_rivi[i][2], (self.paikat[i][0], self.paikat[i][1]))
        
        pokeri_kasi = [[kortti[0], kortti[1]] for kortti in self.valittu_rivi]
        self.voiton_nimi, self.voitto_kerroin = pokerwin.pokerivoitto(pokeri_kasi)
        if self.voitto_kerroin != -1:
            self.voitto = True

    def sekoita_pakka(self):
        random.shuffle(self.kortit)
        self.pakka_sekoitettu = True

    def tarkista_tila(self):
        if self.normi_peli or self.normi_jako  or self.tuplaus_jako or self.tuplaus_peli or self.jokeri_kierrokset:
            self.peli_kaynnissa = True

    def __valinta_kortit(self):
        self.vasen_valinta_kortti_1_x, self.vasen_valinta_kortti_1_y = self.paikat[2][0], self.paikat[2][1]
        self.vasen_valinta_kortti_2_x, self.vasen_valinta_kortti_2_y = self.paikat[2][0], self.paikat[2][1]+15
        self.oikea_valinta_kortti_1_x, self.oikea_valinta_kortti_1_y = self.paikat[3][0], self.paikat[3][1]
        self.oikea_valinta_kortti_2_x, self.oikea_valinta_kortti_2_y = self.paikat[3][0], self.paikat[3][1]+15

if __name__ == "__main__":
    Pikapokeri()    
