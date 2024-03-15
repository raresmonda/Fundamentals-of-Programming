import random
import string
from datetime import date

class Random:
    def __init__(self, service_persoane, service_evenimente):
        self.__service_persoane = service_persoane
        self.__service_evenimente = service_evenimente

    def get_random_string(self):
        '''
        genereaza random un sir de litere mici
        :return:
        '''
        lungime = random.randint(5,20)
        sir = ''.join(random.choice(string.ascii_lowercase) for i in range(lungime))
        return sir

    def generare_persoane(self):
        '''
        genereaza random persoane si le adauga in repo
        :return:
        '''
        for i in range(0, 5):
            id_random = random.randint(4, 999)
            nume_random = self.get_random_string()
            lungime_adresa = random.randint(1, 4)
            adresa_random = []
            for j in range(lungime_adresa):
                adresa_random.append(self.get_random_string())
            self.__service_persoane.adauga_persoana(id_random, nume_random, adresa_random)

    def generare_evenimente(self):
        '''
        genereaza random evenimente si le adauga in repo
        :return:
        '''
        for i in range(0, 5):
            id_random = random.randint(4, 999)
            an_random = random.randint(1900, 2099)
            luna_random = random.randint(1, 12)
            zi_random = random.randint(1, 28)
            data_random = date(an_random, luna_random, zi_random)
            timp_random = random.randint(1, 600)
            lungime_descriere = random.randint(1, 8)
            descriere_random = []
            for j in range(lungime_descriere):
                descriere_random.append(self.get_random_string())
            self.__service_evenimente.adauga_eveniment(id_random, data_random, timp_random, descriere_random)
