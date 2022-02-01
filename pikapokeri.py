import random
import pygame
import grafiikka
import tilafunktiot

class Pikapokeri:
    def __init__(self):
        pygame.init()
        self.leveys_ruutu = 1918
        self.korkeus_ruutu = 1007
        self.naytto = pygame.display.set_mode((self.leveys_ruutu, self.korkeus_ruutu))
        grafiikka.alusta_kuvat(self)
        

        self.pakka_x, self.pakka_y = 218, 88
        self.kierroksen_kortit = []
        for i in range(8):
            self.kierroksen_kortit.append([self.pakka_x, self.pakka_y])

        #globaalit muuttujat
        self.panos = 0.50
        self.saldo = 20
        self.voitto_maara = 0
        self.nopeus = 20
        self.voitto_kerroin = 0
        self.tuplaus_valinta = -1
        self.voiton_nimi = "ei voittoa"
        #tilat
        self.alku = True
        self.jokeri_kierrokset = False
        self.normi_jako = False
        self.normi_peli = False
        self.tarkista_voitto = False
        self.tuplaus_jako_valmis = False
        self.tuplaus = False
        self.tuplaus_valittu = False
        #apuarvot
        self.peli_kaynnissa = False
        self.voitto = False
        self.talteen = False
        self.pakka_sekoitettu = False
        self.vasen_valinta = False
        self.oikea_valinta = False
        self.tuplaus_voitto = False
        self.tuplattiin = False
        
        self.paikat = []
        for i in range(5):
            self.paikat.append([self.leveys_ruutu-(1693-275*i), self.korkeus_ruutu-545])

        tilafunktiot.valinta_kortit(self)
        self.valittu_rivi = []

        pygame.display.set_caption("Pikapokeri")
        self.kello = pygame.time.Clock()
        self.paa_silmukka()

    def piirra_grafiikka(self):
        self.naytto.fill((0, 100, 0))
        grafiikka.napit(self)
        grafiikka.voittotaulukko(self)
        grafiikka.pakka_ja_kortti_paikat(self)
        grafiikka.napit(self)
        grafiikka.voitto(self)
    
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
                    paikka_1_painaus = self.paikat[1][0] <= hiiri_x <= self.paikat[1][0]+self.kortti.get_width() and self.paikat[1][1] <= hiiri_y <= self.paikat[1][1]+self.kortti.get_height()
                    paikka_2_painaus = self.paikat[2][0] <= hiiri_x <= self.paikat[2][0]+self.kortti.get_width() and self.paikat[2][1] <= hiiri_y <= self.paikat[2][1]+self.kortti.get_height()
                    paikka_3_painaus = self.paikat[3][0] <= hiiri_x <= self.paikat[3][0]+self.kortti.get_width() and self.paikat[3][1] <= hiiri_y <= self.paikat[3][1]+self.kortti.get_height()
                    paikka_4_painaus = self.paikat[4][0] <= hiiri_x <= self.paikat[4][0]+self.kortti.get_width() and self.paikat[4][1] <= hiiri_y <= self.paikat[4][1]+self.kortti.get_height()

                    if self.normi_peli:
                        if paikka_2_painaus:
                            self.vasen_valinta = True
                        elif paikka_3_painaus:
                            self.oikea_valinta = True

                    if (self.pelaa_nappi_x <= hiiri_x <= self.pelaa_nappi_x+200 and self.pelaa_nappi_y <= hiiri_y <= self.pelaa_nappi_y+100) and (self.tarkista_voitto or self.alku or (not self.tuplaus_voitto)) and not (self.normi_jako or self.normi_peli) and not (self.voitto) and (self.saldo>=self.panos):
                        if self.alku:
                            self.alku = False
                            self.normi_jako = True
                        elif self.tarkista_voitto or not self.tuplaus_voitto:
                            self.normi_jako = True
                            self.tuplaus_valittu = False
                            self.tuplaus_valinta = -1
                            self.tuplaus_voitto = False
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

                    if self.voitto:
                        if self.voitot_talteen_x <= hiiri_x <= self.voitot_talteen_x+200 and self.voitot_talteen_y <= hiiri_y <= self.voitot_talteen_y+100:
                            self.voitto = False
                            self.alku = True
                            if not self.tuplattiin:
                                self.voitto_maara = self.panos*self.voitto_kerroin
                            self.saldo += self.voitto_maara
                        elif self.tuplaus_nappi_x <= hiiri_x <= self.tuplaus_nappi_x+200 and self.tuplaus_nappi_y <= hiiri_y <= self.tuplaus_nappi_y+100:
                            self.tuplattiin = True
                            if self.tuplaus_valittu:
                                self.sekoita_pakka()
                                self.tuplaus_valittu = False
                            self.tuplaus = True
                            self.voitto = False
                            if self.tarkista_voitto:
                                self.voitto_maara = self.panos*self.voitto_kerroin
                                self.tarkista_voitto = False
                            
                    if self.tuplaus_jako_valmis and (paikka_1_painaus or paikka_2_painaus or paikka_3_painaus or paikka_4_painaus): 
                        if paikka_1_painaus:
                            self.tuplaus_valinta = 1
                        elif paikka_2_painaus:
                            self.tuplaus_valinta = 2
                        elif paikka_3_painaus:
                            self.tuplaus_valinta = 3
                        elif paikka_4_painaus:
                            self.tuplaus_valinta = 4
                            
                        if self.kortit[0][1]<self.kortit[self.tuplaus_valinta][1]:
                            self.voitto_maara *= 2
                            self.tuplaus_voitto = True
                        else:
                            self.tuplaus_voitto = False
                            self.voitto = False
                            self.voitto_maara = 0
                         
            if event.type == pygame.QUIT:
                exit()

    def piirra_naytto(self):
        self.piirra_grafiikka()

        if self.alku:
            tilafunktiot.alku_tilanne(self)
        elif self.normi_jako:
            tilafunktiot.normi_kierros_jako(self)
        elif self.normi_peli:
            tilafunktiot.normi_kierros_pelaus(self)
        elif self.tarkista_voitto:
            tilafunktiot.voiton_tarkistus(self)
        elif self.tuplaus:
            tilafunktiot.tuplaus_jakaminen(self)
        elif self.tuplaus_jako_valmis:
            tilafunktiot.tuplaus_peli(self)
        elif self.tuplaus_valittu:
            tilafunktiot.tuplaus_lopetus(self)
        
        pygame.display.flip()
        self.kello.tick(60)

    def sekoita_pakka(self):
        random.shuffle(self.kortit)
        self.pakka_sekoitettu = True

if __name__ == "__main__":
    Pikapokeri()    
