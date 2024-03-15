from domeniu.inscrieri import Inscriere
from domeniu.persoana import Persoana
from domeniu.eveniment import Eveniment
import unittest

from erori.validation_error import ValidError


class TestePersoana(unittest.TestCase):

    def setUp(self):
        self.persoana1 = Persoana(1, "Ion", "Strada Avram Iancu")
        self.persoana2 = Persoana(2, "Gheorghe", "Strada Teodor Mihali")

    def ruleaza_teste(self):
        self.setUp()
        self.test_id()
        self.test_nume()
        self.test_adresa()
        self.test_update_nume()
        print("Teste unittest trecute cu succes!")

    def test_id(self):
        self.assertEqual(self.persoana1.get_id_persoana(), 1)
        self.assertNotEqual(self.persoana1.get_id_persoana(), -1)
        self.assertEqual(self.persoana2.get_id_persoana(), 2)
        self.assertNotEqual(self.persoana2.get_id_persoana(), -2)

    def test_nume(self):
        self.assertEqual(self.persoana1.get_nume(), "Ion")
        self.assertEqual(self.persoana2.get_nume(), "Gheorghe")
        self.assertNotEqual(self.persoana1.get_nume(), "Marius")
        self.assertNotEqual(self.persoana2.get_nume(), "Adrian")

    def test_adresa(self):
        self.assertEqual(self.persoana1.get_adresa(), "Strada Avram Iancu")
        self.assertNotEqual(self.persoana2.get_adresa(), "Strada Avram Iancu")
        self.assertEqual(self.persoana2.get_adresa(), "Strada Teodor Mihali")
        self.assertNotEqual(self.persoana1.get_adresa(), "Strada Teodor Mihali")

    def test_update_nume(self):
        self.persoana1.set_nume("Marius")
        self.assertEqual(self.persoana1.get_nume(), "Marius")
        self.assertNotEqual(self.persoana1.get_nume(), "Ion")

    def test_update_adresa(self):
        self.persoana1.set_adresa("Strada Memorandumului")
        self.assertEqual(self.persoana1.get_adresa(), "Strada Memorandumului")
        self.assertNotEqual(self.persoana1.get_id_persoana(), "Strada Avram Iancu")

class TesteEveniment(unittest.TestCase):

    def setUp(self):
        self.eveniment = Eveniment(1, "22.10.2022", 3, "Test analiza")

    def ruleaza_teste(self):
        self.setUp()
        self.test_id()
        self.test_data()
        self.test_data()
        self.test_update_data()
        self.test_update_timp()
        self.test_update_descriere()

    def test_id(self):
        self.assertEqual(self.eveniment.get_id_eveniment(), 1)
        self.assertNotEqual(self.eveniment.get_id_eveniment(), -1)

    def test_data(self):
        self.assertEqual(self.eveniment.get_data(), "22.10.2022")
        self.assertNotEqual(self.eveniment.get_data(), "12.11.2023")

    def test_timp(self):
        self.assertEqual(self.eveniment.get_timp(), 3)
        self.assertNotEqual(self.eveniment.get_timp(), 1)

    def test_descriere(self):
        self.assertEqual(self.eveniment.get_descriere(), "Test analiza")
        self.assertNotEqual(self.eveniment.get_descriere(), "Test ASC")

    def test_update_data(self):
        self.eveniment.set_data("12.11.2023")
        self.assertNotEqual(self.eveniment.get_data(), "22.10.2022")
        self.assertEqual(self.eveniment.get_data(), "12.11.2023")

    def test_update_timp(self):
        self.eveniment.set_timp(1)
        self.assertEqual(self.eveniment.get_timp(), 1)
        self.assertNotEqual(self.eveniment.get_timp(), 3)

    def test_update_descriere(self):
        self.eveniment.set_descriere("Test ASC")
        self.assertEqual(self.eveniment.get_descriere(), "Test ASC")
        self.assertNotEqual(self.eveniment.get_descriere(), "Test Analiza")

class TesteRepoPersoane(unittest.TestCase):

    def __init__(self, repo_persoane):
        super().__init__()
        self.__repo_persoane = repo_persoane

    def setUp(self):
        self.persoana = Persoana(1, "Ion", "Strada Avram Iancu")

    def ruleaza_teste(self):
        self.setUp()
        self.test_adaugare()
        self.test_modificare()
        self.test_stergere()

    def test_adaugare(self):
        self.assertEqual(len(self.__repo_persoane.get_all()), 0)
        self.__repo_persoane.adauga_persoana(self.persoana)
        self.assertEqual(len(self.__repo_persoane.get_all()), 1)

    def test_modificare(self):
        persoana_modificata = Persoana(1, "Gheorghe", "Strada Teodor Mihali")
        self.__repo_persoane.modifica_persoana(persoana_modificata)
        self.assertEqual(self.__repo_persoane.cauta_persoana_dupa_id(1).get_nume(), "Gheorghe")
        self.assertEqual(self.__repo_persoane.cauta_persoana_dupa_id(1).get_adresa(), "Strada Teodor Mihali")

    def test_stergere(self):
        self.assertEqual(len(self.__repo_persoane.get_all()), 1)
        self.__repo_persoane.sterge_persoana_dupa_id(1)
        self.assertEqual(len(self.__repo_persoane.get_all()), 0)

class TesteRepoEvenimente(unittest.TestCase):

    def __init__(self, repo_evenimente):
        super().__init__()
        self.__repo_evenimente = repo_evenimente

    def setUp(self):
        self.eveniment = Eveniment(1, "22.10.2022", 3, "Test Analiza")

    def ruleaza_teste(self):
        self.setUp()
        self.test_adaugare()
        self.test_modificare()
        self.test_stergere()

    def test_adaugare(self):
        self.assertEqual(len(self.__repo_evenimente.get_all()), 0)
        self.__repo_evenimente.adauga_eveniment(self.eveniment)
        self.assertEqual(len(self.__repo_evenimente.get_all()), 1)

    def test_modificare(self):
        eveniment_modificat = Eveniment(1, "10.12.2022", 3, "Test ASC")
        self.__repo_evenimente.modifica_eveniment(eveniment_modificat)
        self.assertEqual(self.__repo_evenimente.cauta_eveniment_dupa_id(1).get_data(), "10.12.2022")
        self.assertEqual(self.__repo_evenimente.cauta_eveniment_dupa_id(1).get_timp(), 3)
        self.assertEqual(self.__repo_evenimente.cauta_eveniment_dupa_id(1).get_descriere(), "Test ASC")

    def test_stergere(self):
        self.assertEqual(len(self.__repo_evenimente.get_all()), 1)
        self.__repo_evenimente.sterge_eveniment_dupa_id(1)
        self.assertEqual(len(self.__repo_evenimente.get_all()), 0)

class TesteRepoInscrieri(unittest.TestCase):

    def __init__(self, repo_inscrieri):
        super().__init__()
        self.__repo_inscrieri = repo_inscrieri

    def setUp(self):
        self.persoana = Persoana(1, "Ion", "Strada Avram Iancu")
        self.eveniment = Eveniment(1, "22.10.2022", 3, "Test Analiza")
        self.inscriere = Inscriere(1, self.persoana, self.eveniment)

    def ruleaza_teste(self):
        self.setUp()
        self.test_adaugare()
        self.test_stergere()

    def test_adaugare(self):
        self.assertEqual(len(self.__repo_inscrieri.get_all()), 0)
        self.__repo_inscrieri.adauga_inscriere(self.inscriere)
        self.assertEqual(len(self.__repo_inscrieri.get_all()), 1)

    def test_stergere(self):
        self.assertEqual(len(self.__repo_inscrieri.get_all()), 1)
        self.__repo_inscrieri.sterge_inscriere_dupa_id(1)
        self.assertEqual(len(self.__repo_inscrieri.get_all()), 0)

class TesteValidatorPersoana(unittest.TestCase):

    def __init__(self, validator_persoana):
        super().__init__()
        self.__validator_persoana = validator_persoana

    def setUp(self):
        self.persoana = Persoana(1, "Ion", "Strada Avram Iancu")
        self.persoana_gresita = Persoana(-1,"", "")
        self.persoana_id_gresit = Persoana(-1, "Ion", "Strada Avram Iancu")
        self.persoana_nume_gresit = Persoana(1, "", "Strada Avram Iancu")
        self.persoana_adresa_gresita = Persoana(1, "Ion", "")


    def ruleaza_teste(self):
        self.setUp()
        self.valideaza_black_box()
        self.valideaza_white_box()

    def valideaza_black_box(self):
        self.assertEqual(self.__validator_persoana.valideaza(self.persoana), None)
        self.assertRaises(ValidError, self.__validator_persoana.valideaza, self.persoana_gresita)

    def valideaza_white_box(self):
        self.assertEqual(self.__validator_persoana.valideaza(self.persoana), None)
        self.assertRaises(ValidError, self.__validator_persoana.valideaza, self.persoana_gresita)
        self.assertRaises(ValidError, self.__validator_persoana.valideaza, self.persoana_id_gresit)
        self.assertRaises(ValidError, self.__validator_persoana.valideaza, self.persoana_nume_gresit)
        self.assertRaises(ValidError, self.__validator_persoana.valideaza, self.persoana_adresa_gresita)

class TesteValidatorEveniment(unittest.TestCase):

    def __init__(self, validator_eveniment):
        super().__init__()
        self.__validator_eveniment = validator_eveniment

    def setUp(self):
        self.eveniment = Eveniment(1, "22.10.2022", 3, "Test Analiza")

    def ruleaza_teste(self):
        self.setUp()
        self.valideaza()

    def valideaza(self):
        self.assertEqual(self.__validator_eveniment.valideaza(self.eveniment), None)

class TesteServicePersoane(unittest.TestCase):

    def __init__(self, service_persoane):
        super().__init__()
        self.__service_persoane = service_persoane

    def ruleaza_teste(self):
        self.test_adaugare()
        self.test_modificare()
        self.teste_stergere()

    def test_adaugare(self):
        self.assertEqual(len(self.__service_persoane.get_all_persoane()), 0)
        self.__service_persoane.adauga_persoana(1, "Ion", "Strada Avram Iancu")
        self.assertEqual(len(self.__service_persoane.get_all_persoane()), 1)

    def test_modificare(self):
        self.__service_persoane.modifica_persoana(1, "Gheorghe", "Strada Teodor Mihali")
        self.assertEqual(self.__service_persoane.cauta_persoana(1).get_nume(), "Gheorghe")
        self.assertEqual(self.__service_persoane.cauta_persoana(1).get_adresa(), "Strada Teodor Mihali")

    def teste_stergere(self):
        self.assertEqual(len(self.__service_persoane.get_all_persoane()), 1)
        self.__service_persoane.sterge_persoana(1)
        self.assertEqual(len(self.__service_persoane.get_all_persoane()), 0)

class TesteServiceEvenimente(unittest.TestCase):

    def __init__(self, service_evenimente):
        super().__init__()
        self.__service_evenimente = service_evenimente

    def ruleaza_teste(self):
        self.test_adaugare()
        self.test_modificare()
        self.teste_stergere()

    def test_adaugare(self):
        self.assertEqual(len(self.__service_evenimente.get_all_evenimente()), 0)
        self.__service_evenimente.adauga_eveniment(1, "22.10.2022", 3, "Test Analiza")
        self.assertEqual(len(self.__service_evenimente.get_all_evenimente()), 1)

    def test_modificare(self):
        self.__service_evenimente.modifica_eveniment(1, "10.12.2022", 3, "Test ASC")
        self.assertEqual(self.__service_evenimente.cauta_eveniment(1).get_data(), "10.12.2022")
        self.assertEqual(self.__service_evenimente.cauta_eveniment(1).get_timp(), 3)
        self.assertEqual(self.__service_evenimente.cauta_eveniment(1).get_descriere(), "Test ASC")

    def teste_stergere(self):
        self.assertEqual(len(self.__service_evenimente.get_all_evenimente()), 1)
        self.__service_evenimente.sterge_eveniment(1)
        self.assertEqual(len(self.__service_evenimente.get_all_evenimente()), 0)

class TesteServiceInscrieri(unittest.TestCase):

    def __init__(self, service_inscrieri):
        super().__init__()
        self.__service_inscrieri = service_inscrieri

    def setUp(self):
        self.persoana = Persoana(1, "Ion", "Strada Avram Iancu")
        self.eveniment = Eveniment(1, "22.10.2022", 3, "Test Analiza")

    def ruleaza_teste(self):
        self.setUp()
        self.test_adaugare()
        self.teste_stergeri()

    def test_adaugare(self):
        self.assertEqual(len(self.__service_inscrieri.get_all_inscrieri()), 0)
        self.__service_inscrieri.adauga_inscriere(1, self.persoana, self.eveniment)
        self.assertEqual(len(self.__service_inscrieri.get_all_inscrieri()), 1)

    def teste_stergeri(self):
        self.assertEqual(len(self.__service_inscrieri.get_all_inscrieri()), 1)
        self.__service_inscrieri.sterge_inscriere_dupa_persoana(1)
        self.__service_inscrieri.adauga_inscriere(1, self.persoana, self.eveniment)
        self.__service_inscrieri.sterge_inscriere_dupa_eveniment(1)
        self.assertEqual(len(self.__service_inscrieri.get_all_inscrieri()), 0)