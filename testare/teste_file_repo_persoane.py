from infrastructura.file_repo_evenimente import FileRepoEvenimente
from infrastructura.file_repo_persoane import FileRepoPersoane
from domeniu.persoana import Persoana
from domeniu.eveniment import Eveniment
from erori.validation_error import ValidError
from erori.repo_error import RepoError
from datetime import date, datetime


class TesteFilePersoane:

    def __init__(self, validator_persoana, validator_eveniment, file_repo_persoane, file_repo_evenimente, service_persoane, service_evenimente, service_inscrieri, file_repo_inscrieri):
        self.__validator_persoana = validator_persoana
        self.__validator_eveniment = validator_eveniment
        self.__file_repo_persoane = file_repo_persoane
        self.__file_repo_evenimente = file_repo_evenimente
        self.__file_repo_inscrieri = file_repo_inscrieri
        self.__service_persoane = service_persoane
        self.__service_evenimente = service_evenimente
        self.__service_inscrieri = service_inscrieri

    def ruleaza_toate_testele_file(self):
        self.__ruleaza_teste_persoana()
        print("Teste persoana trecute cu succes!")
        self.__ruleaza_teste_eveniment()
        print("Teste eveniment trecute cu succes!")
        self.__ruleaza_teste_validator_persoana()
        print("Teste validator persoana trecute cu succes!")
        self.__ruleaza_teste_validator_eveniment()
        print("Teste validator eveniment trecute cu succes!")
        self.__ruleaza_teste_repo_file_persoane()
        print("Teste file repo persoane trecute cu succes!")
        self.__ruleaza_teste_repo_evenimente()
        print("Teste file repo evenimente trecute cu succes!")
        self.__ruleaza_teste_service_persoane()
        print("Teste service persoane trecute cu succes!")
        self.__ruleaza_teste_service_evenimente()
        print("Teste service evenimente trecute cu succes!")
        self.__ruleaza_teste_rapoarte()

    def __goleste_fisier_persoane(self, cale_test_file_persoane):
        with open(cale_test_file_persoane, "w") as f:
            pass

    def __goleste_fisier_evenimente(self, cale_test_file_evenimente):
        with open(cale_test_file_evenimente, "w") as g:
            pass

    def __goleste_fisier_inscrieri(self, cale_test_file_inscrieri):
        with open(cale_test_file_inscrieri, "w") as h:
            pass


    def __ruleaza_teste_persoana(self):
        id_persoana = 1
        nume = "Ion"
        adresa = "Strada Avram Iancu"
        persoana = Persoana(id_persoana, nume, adresa)
        assert(id_persoana == persoana.get_id_persoana())
        assert(nume == persoana.get_nume())
        assert(adresa == persoana.get_adresa())

    def __ruleaza_teste_eveniment(self):
        id_eveniment = 1
        data = "22.10.2022"
        timp = 3
        descriere = "Test analiza"
        eveniment = Eveniment(id_eveniment, data, timp, descriere)
        assert(id_eveniment == eveniment.get_id_eveniment())
        assert (data == eveniment.get_data())
        assert(timp == eveniment.get_timp())
        assert(descriere == eveniment.get_descriere())

    def __ruleaza_teste_validator_persoana(self):
        id_persoana = 1
        nume = "Ion"
        adresa = "Strada Avram Iancu"
        persoana = Persoana(id_persoana, nume, adresa)
        self.__validator_persoana.valideaza(persoana)
        id_persoana_gresit = -1
        persoana_gresita = Persoana(id_persoana_gresit, nume, adresa)
        try:
            self.__validator_persoana.valideaza(persoana_gresita)
            assert False
        except ValidError as ve:
            assert(str(ve) == "id invalid!\n")

    def __ruleaza_teste_validator_eveniment(self):
        id_eveniment = 1
        an = 2022
        luna = 12
        zi = 10
        data = date(an, luna, zi)
        timp = 3
        descriere = "Test analiza"
        eveniment = Eveniment(id_eveniment, data, timp, descriere)
        self.__validator_eveniment.valideaza(eveniment)
        id_eveniment_gresit = -1
        data_gresita = ""
        timp_gresit = -1
        descriere_gresita = ""
        eveniment_gresit = Eveniment(id_eveniment_gresit, data_gresita, timp_gresit, descriere_gresita)
        try:
            self.__validator_eveniment.valideaza(eveniment_gresit)
            assert False
        except ValidError as ve:
            assert (str(ve) == "id invalid!\ntimp invalid!\ndescriere invalida!")

    def __ruleaza_teste_repo_file_persoane(self):
        cale_test_file_persoane = "testare/persoane_test.txt"
        self.__goleste_fisier_persoane(cale_test_file_persoane)
        file_repo_persoane = FileRepoPersoane(cale_test_file_persoane)
        assert file_repo_persoane.size() == 0
        persoana = Persoana(1, "Ion", "Strada Avram Iancu")
        file_repo_persoane.adauga_persoana(persoana)
        assert file_repo_persoane.size() == 1
        acelasi_id_persoana = 1
        acelasi_nume = "Ion"
        aceeasi_adresa = "Strada Avram Iancu"
        alta_persoana_acelasi_id = Persoana(acelasi_id_persoana, acelasi_nume, aceeasi_adresa)
        try:
            file_repo_persoane.adauga_persoana(alta_persoana_acelasi_id)
            assert False
        except RepoError as re:
            assert (str(re) == "persoana existenta!")

    def __ruleaza_teste_repo_evenimente(self):
        cale_test_file_evenimente = "testare/evenimente_test.txt"
        self.__goleste_fisier_evenimente(cale_test_file_evenimente)
        file_repo_evenimente = FileRepoEvenimente(cale_test_file_evenimente)
        id_eveniment = 1
        data = "22.10.2022"
        timp = 3
        descriere = "Test analiza"
        eveniment = Eveniment(id_eveniment, data, timp, descriere)
        assert file_repo_evenimente.size() == 0
        file_repo_evenimente.adauga_eveniment(eveniment)
        assert file_repo_evenimente.size() == 1
        acelasi_id_eveniment = 1
        aceeasi_data = "22.10.2022"
        acelasi_timp = 3
        aceeasi_descriere = "Test analiza"
        alt_eveniment_acelasi_id = Eveniment(acelasi_id_eveniment, aceeasi_data, acelasi_timp, aceeasi_descriere)
        try:
            file_repo_evenimente.adauga_eveniment(alt_eveniment_acelasi_id)
            assert False
        except RepoError as re:
            assert(str(re) == "eveniment existent!")
        file_repo_evenimente.sterge_eveniment_dupa_id(id_eveniment)

    def __ruleaza_teste_service_persoane(self):
        id_persoana = 1
        nume = "Ion"
        adresa = "Strada Avram Iancu"
        assert (len(self.__service_persoane.get_all_persoane()) == 5)
        self.__service_persoane.adauga_persoana(id_persoana, nume, adresa)
        assert (len(self.__service_persoane.get_all_persoane()) == 6)
        acelasi_id_persoana = 1
        acelasi_nume = "Ion"
        aceeasi_adresa = "Strada Avram Iancu"
        try:
            self.__service_persoane.adauga_persoana(acelasi_id_persoana, acelasi_nume, aceeasi_adresa)
            assert False
        except RepoError as re:
            assert (str(re) == "persoana existenta!")
        self.__service_persoane.sterge_persoana(id_persoana)

    def __ruleaza_teste_service_evenimente(self):
        id_eveniment = 1
        data = "22.10.2022"
        timp = 3
        descriere = "Test analiza"
        assert (len(self.__service_evenimente.get_all_evenimente()) == 5)
        self.__service_evenimente.adauga_eveniment(id_eveniment, data, timp, descriere)
        assert (len(self.__service_evenimente.get_all_evenimente()) == 6)
        acelasi_id_eveniment = 1
        aceeasi_data = "22.10.2022"
        acelasi_timp = 3
        aceeasi_descriere = "Test analiza"
        try:
            self.__service_evenimente.adauga_eveniment(acelasi_id_eveniment, aceeasi_data, acelasi_timp, aceeasi_descriere)
            assert False
        except RepoError as re:
            assert (str(re) == "eveniment existent!")
        self.__service_evenimente.sterge_eveniment(id_eveniment)

    def __ruleaza_teste_rapoarte(self):
        nume1 = "Ion"
        nume2 = "Gheorghe"
        nume3 = "Gigel"
        adresa1 = ["Strada", "Avram", "Iancu"]
        adresa2 = ["Strada", "Falezei"]
        adresa3 = ["Bulevardul", "Independentei"]
        self.__service_persoane.adauga_persoana(1, nume1, adresa1)
        self.__service_persoane.adauga_persoana(2, nume2, adresa2)
        self.__service_persoane.adauga_persoana(3, nume3, adresa3)
        an = 2022
        luna1 = 11
        luna2 = 12
        zi1 = 26
        zi2 = 10
        zi3 = 24
        data1 = date(an, luna1, zi1)
        data2 = date(an, luna2, zi2)
        data3 = date(an, luna2, zi3)
        descriere1 = ["Test", "la", "asc"]
        descriere2 = ["Partial", "la", "algebra"]
        descriere3 = ["Concurs", "de", "patinaj"]
        persoana1 = Persoana(1, nume1, adresa1)
        persoana2 = Persoana(2, nume2, adresa2)
        persoana3 = Persoana(3, nume3, adresa3)
        eveniment1 = Eveniment(1, data1, 30, descriere1)
        eveniment2 = Eveniment(2, data2, 120, descriere2)
        eveniment3 = Eveniment(3, data3, 120, descriere3)
        #self.__service_evenimente.adauga_eveniment(1, data1, 30, descriere1)
        self.__service_evenimente.adauga_eveniment(2, data2, 120, descriere2)
        self.__service_evenimente.adauga_eveniment(3, data3, 120, descriere3)
        self.__service_inscrieri.adauga_inscriere(1, persoana1, eveniment1)
        self.__service_inscrieri.adauga_inscriere(2, persoana1, eveniment2)
        self.__service_inscrieri.adauga_inscriere(3, persoana1, eveniment3)
        self.__service_inscrieri.adauga_inscriere(4, persoana2, eveniment1)
        self.__service_inscrieri.adauga_inscriere(5, persoana2, eveniment2)
        self.__service_inscrieri.adauga_inscriere(6, persoana3, eveniment1)
        assert self.__service_inscrieri.genereaza_raport_cei_mai_multi_participanti_la_eveniment() == [1]
        assert self.__service_inscrieri.genereaza_raport_primele_evenimente() == [1,3]