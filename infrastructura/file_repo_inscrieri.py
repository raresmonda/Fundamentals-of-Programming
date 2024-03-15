from domeniu.eveniment import Eveniment
from domeniu.inscrieri import Inscriere
from domeniu.persoana import Persoana
from infrastructura.repo_inscrieri import RepoInscrieri


class FileRepoInscrieri(RepoInscrieri):

    def __init__(self, cale_catre_fisier_inscrieri):
        RepoInscrieri.__init__(self)
        self.__cale_catre_fisier_inscrieri = cale_catre_fisier_inscrieri

    def __read_all_from_file(self):
        with open(self.__cale_catre_fisier_inscrieri, "r") as f:
            lines = f.readlines()
            self._inscrieri.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split("|")
                    id_inscriere = int(parts[0])
                    persoanastr = parts[1]
                    evenimentstr = parts[2]
                    partspersoana = persoanastr.split("/")
                    parteveniment = evenimentstr.split("/")
                    id_persoana = int(partspersoana[0])
                    numepersoana = partspersoana[1]
                    adresapersoana = partspersoana[2]
                    persoana = Persoana(id_persoana, numepersoana, adresapersoana)
                    id_eveniment = int(parteveniment[0])
                    dataeveniment = parteveniment[1]
                    timpeveniment = int(parteveniment[2])
                    descriere_eveniment = parteveniment[3]
                    eveniment = Eveniment(id_eveniment, dataeveniment, timpeveniment, descriere_eveniment)
                    inscriere = Inscriere(id_inscriere, persoana, eveniment)
                    self._inscrieri[id_inscriere] = inscriere

    def __write_all_to_file(self):
        with open(self.__cale_catre_fisier_inscrieri, "w") as f:
            for persoana in self._inscrieri.values():
                f.write(str(persoana)+"\n")

    def adauga_inscriere(self, inscriere):
        self.__read_all_from_file()
        RepoInscrieri.adauga_inscriere(self, inscriere)
        self.__write_all_to_file()

    def sterge_inscriere_dupa_id(self, id_inscriere):
        self.__read_all_from_file()
        RepoInscrieri.sterge_inscriere_dupa_id(self, id_inscriere)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepoInscrieri.get_all(self)

    def size(self):
        self.__read_all_from_file()
        return RepoInscrieri.size(self)