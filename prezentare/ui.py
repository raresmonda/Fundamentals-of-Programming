from erori.validation_error import ValidError
from erori.repo_error import RepoError
from datetime import datetime, date

class UI:

    def __init__(self, service_persoane, service_evenimente, service_inscrieri):
        self.__service_persoane = service_persoane
        self.__service_evenimente = service_evenimente
        self.__service_inscrieri = service_inscrieri
        self.__comenzi = {
            "adauga_persoana":self.__ui_adauga_persoana,
            "printeaza_persoane":self.__ui_printeaza_persoane,
            "sterge_persoana":self.__ui_sterge_persoana,
            "modifica_persoana":self.__ui_modifica_persoana,
            "cauta_persoana":self.__ui_cauta_persoana,
            "adauga_eveniment":self.__ui_adauga_eveniment,
            "printeaza_evenimente":self.__ui__printeaza_evenimente,
            "sterge_eveniment":self.__ui_sterge_eveniment,
            "modifica_eveniment":self.__ui_modifica_eveniment,
            "cauta_eveniment":self.__ui_cauta_eveniment,
            "adauga_inscriere":self.__ui_adauga_inscriere,
            "printeaza_inscrieri":self.__ui_printeaza_inscrieri,
            "raport1":self.__ui_raport_evenimente_persoana_ordonat,
            "raport2":self.__ui_raport_cei_mai_multi_participanti_la_eveniment,
            "raport3":self.__ui_raport_primele_evenimente,
            "raport4":self.__ui_raport_persoane_participante_la_un_eveniment
        }

    def __ui_adauga_persoana(self):
        '''
        adauga o persoana la lista
        :return:
        '''
        if len(self.__params) < 3:
            print("Numar parametrii invalid!")
            return
        id_persoana = int(self.__params[0])
        nume = self.__params[1]
        adresa = self.__params[2:]
        self.__service_persoane.adauga_persoana(id_persoana, nume, adresa)
        print("Persoana adaugata cu succes!")

    def __ui_printeaza_persoane(self):
        '''
        printeaza lista cu persoane
        :return:
        '''
        if len(self.__params) != 0:
            print("Numar parametrii invalid!")
            return
        persoane = self.__service_persoane.get_all_persoane()
        if len(persoane) == 0:
            print("nu exista persoane in aplicatie!")
            return
        self.__ui_printeaza_persoane_recursiv(persoane)

    def __ui_printeaza_persoane_recursiv(self, persoane):
        if len(persoane) == 0:
            return
        print(f"{persoane[0]}")
        self.__ui_printeaza_persoane_recursiv(persoane[1:])

    def __ui_sterge_persoana(self):
        '''
        sterge o persoana din lista
        :return:
        '''
        if len(self.__params) != 1:
            print("Numar parametrii invalid!")
            return
        id_persoana = int(self.__params[0])
        self.__service_persoane.sterge_persoana(id_persoana)
        self.__service_inscrieri.sterge_inscriere_dupa_persoana(id_persoana)
        print("Persoana stearsa cu succes!")

    def __ui_modifica_persoana(self):
        '''
        actualizeaza datele unei persoane
        :return:
        '''
        if len(self.__params) < 3:
            print("Numar parametrii invalid!")
            return
        id_persoana = int(self.__params[0])
        nume_actualizat = self.__params[1]
        adresa_actualizata = self.__params[2:]
        self.__service_persoane.modifica_persoana(id_persoana, nume_actualizat, adresa_actualizata)
        print("Persoana modificata cu succes!")

    def __ui_cauta_persoana(self):
        '''
        cauta o persoana dupa id si o afiseaza
        :return:
        '''
        if len(self.__params) != 1:
            print("Numar parametrii invalid!")
            return
        id_persoana = int(self.__params[0])
        persoana = self.__service_persoane.cauta_persoana(id_persoana)
        print(f"Persoana cautata este {persoana}")

    def __ui_adauga_eveniment(self):
        '''
        adauga un eveniment la lista
        :return:
        '''
        if len(self.__params) < 6:
            print("Numar parametrii invalid!")
            return
        id_eveniment = int(self.__params[0])
        an = int(self.__params[1])
        luna = int(self.__params[2])
        zi = int(self.__params[3])
        data_test = f"{an}-{luna}-{zi}"
        if data_test != datetime.strptime(data_test, "%Y-%m-%d").strftime('%Y-%m-%d'):
            print("Data invalida!\n")
            return
        data = date(an, luna, zi)
        timp = int(self.__params[4])
        descriere = self.__params[5:]
        self.__service_evenimente.adauga_eveniment(id_eveniment, data, timp, descriere)
        print("Eveniment adaugat cu succes!")

    def __ui__printeaza_evenimente(self):
        '''
        printeaza lista cu evenimente
        :return:
        '''
        if len(self.__params) != 0:
            print("Numar parametrii invalid!")
            return
        evenimente = self.__service_evenimente.get_all_evenimente()
        if len(evenimente) == 0:
            print("nu exista evenimente in aplicatie!")
            return
        self.__ui_printeaza_evenimente_recursiv(evenimente)

    def __ui_printeaza_evenimente_recursiv(self, evenimente):
        if len(evenimente) == 0:
            return
        print(f"{evenimente[0]}")
        self.__ui_printeaza_evenimente_recursiv(evenimente[1:])

    def __ui_sterge_eveniment(self):
        '''
        sterge un eveniment din lista
        :return:
        '''
        if len(self.__params) != 1:
            print("Numar parametrii invalid!")
            return
        id_eveniment = int(self.__params[0])
        self.__service_evenimente.sterge_eveniment(id_eveniment)
        self.__service_inscrieri.sterge_inscriere_dupa_eveniment(id_eveniment)
        print("Eveniment sters cu succes!")

    def __ui_modifica_eveniment(self):
        '''
        actualizeaza datele evenimentului cu id-ul precizat
        :return:
        '''
        if len(self.__params) < 4:
            print("Numar parametrii invalid!")
            return
        id_eveniment = int(self.__params[0])
        data_actualizata = self.__params[1]
        timp_actualizat = int(self.__params[2])
        descriere_actualizata = self.__params[3:]
        self.__service_evenimente.modifica_eveniment(id_eveniment, data_actualizata, timp_actualizat, descriere_actualizata)
        print("Eveniment modificat cu succes!")

    def __ui_cauta_eveniment(self):
        '''
        cauta un eveniment dupa id si il afiseaza
        :return:
        '''
        if len(self.__params) != 1:
            print("Numar parametrii invalid!")
            return
        id_eveniment = int(self.__params[0])
        eveniment = self.__service_evenimente.cauta_eveniment(id_eveniment)
        print(f"Evenimentul cautat este {eveniment}")

    def __ui_cauta_persoana_pentru_inscrieri(self, id_persoana_ceruta):
        '''
        cauta o persoana dupa id si o returneaza
        :param id_persoana_ceruta: id
        :return:
        '''
        return self.__service_persoane.cauta_persoana(id_persoana_ceruta)

    def __ui_cauta_eveniment_pentru_inscrieri(self, id_eveniment_cerut):
        '''
        cauta un eveniment dupa id si il returneaza
        :param id_eveniment_cerut: id
        :return:
        '''
        return self.__service_evenimente.cauta_eveniment(id_eveniment_cerut)

    def __ui_adauga_inscriere(self):
        '''
        inscrie o persoana la un eveniment
        :return:
        '''
        if len(self.__params) != 3:
            print("Numar parametrii invalid!")
            return
        id_inscriere = int(self.__params[0])
        id_persoana = int(self.__params[1])
        id_eveniment = int(self.__params[2])
        persoana = self.__ui_cauta_persoana_pentru_inscrieri(id_persoana)
        eveniment = self.__ui_cauta_eveniment_pentru_inscrieri(id_eveniment)
        self.__service_inscrieri.adauga_inscriere(id_inscriere, persoana, eveniment)

    def __ui_printeaza_inscrieri(self):
        '''
        printeaza lista cu inscrieri
        :return:
        '''
        if len(self.__params) != 0:
            print("Numar parametrii invalid!")
            return
        inscrieri = self.__service_inscrieri.get_all_inscrieri()
        if len(inscrieri) == 0:
            print("nu exista persoane in aplicatie!")
            return
        for inscriere in inscrieri:
            print(f"{inscriere}")

    def __ui_raport_cei_mai_multi_participanti_la_eveniment(self):
        if len(self.__params) != 0:
            print("Numar parametrii invalid!")
            return
        id_persoane = self.__service_inscrieri.genereaza_raport_cei_mai_multi_participanti_la_eveniment()
        persoane = []
        for id_persoana in id_persoane:
            persoana = self.__ui_cauta_persoana_pentru_inscrieri(id_persoana)
            print(persoana)
            persoane.append(self.__ui_cauta_persoana_pentru_inscrieri(id_persoana))
        self.__service_inscrieri.printeaza_raport_in_fisier(persoane)

    def __ui_raport_evenimente_persoana_ordonat(self):
        if len(self.__params) != 1:
            print("Numar parametrii invalid!")
            return
        id_persoana = int(self.__params[0])
        id_evenimente = self.__service_inscrieri.lista_de_evenimente_pentru_o_persoana_ordonata_alfabetic(id_persoana)
        print("Evenimentele la care participa persoana ordonate dupa descriere")
        for id_eveniment in id_evenimente:
            eveniment = self.__service_evenimente.cauta_eveniment(id_eveniment)
            print(eveniment)
        id_evenimente_data = self.__service_inscrieri.lista_de_evenimente_pentru_o_persoana_ordonata_dupa_data(id_persoana)
        print("Evenimentele la care participa persoana ordonate dupa data")
        for id_eveniment_data in id_evenimente_data:
            eveniment_data = self.__service_evenimente.cauta_eveniment(id_eveniment_data)
            print(eveniment_data)

    def __ui_raport_primele_evenimente(self):
        if len(self.__params) != 0:
            print("Numar paramertrii invalid!")
            return
        id_evenimente = self.__service_inscrieri.genereaza_raport_primele_evenimente()
        for i in range(len(id_evenimente)):
            if i % 2 == 0:
                eveniment = self.__service_evenimente.cauta_eveniment(id_evenimente[i])
                print(eveniment.get_descriere(), "Numarul de participanti:", id_evenimente[i + 1])

    def __ui_raport_persoane_participante_la_un_eveniment(self):
        if len(self.__params) != 1:
            print("Numar parametrii invalid!")
            return
        id_eveniment = int(self.__params[0])
        id_persoane = self.__service_inscrieri.genereaza_raport_persoane_participante_la_un_eveniment(id_eveniment)
        for id_persoana in id_persoane:
            persoana = self.__service_persoane.cauta_persoana(id_persoana)
            print(persoana)

    def run(self):
        while True:
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("Eroare UI: tip numeric invalid!")
                except ValidError as ve:
                    print(f"Valid Error:{ve}")
                except RepoError as re:
                    print(f"Repo Error:{re}")
            else:
                print("Comanda invalida!")

                #adauga_comanda 1 Gherghe Strada Avram Iancu
                #nume_comanda = adauga_comanda
                #self.__params = 1 Gherghe Strada Avram Iancu
                #               [0]  [1]     [2]   [3]   [4]