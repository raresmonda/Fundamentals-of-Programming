from domeniu.eveniment import Eveniment
from infrastructura.repo_evenimente import RepoEvenimente


class FileRepoEvenimente(RepoEvenimente):

    def __init__(self, cale_catre_fisier_evenimente):
        RepoEvenimente.__init__(self)
        self.__cale_catre_fisier_evenimente = cale_catre_fisier_evenimente

    def __read_all_from_file(self):
        with open(self.__cale_catre_fisier_evenimente, "r") as f:
            lines = f.readlines()
            self._evenimente.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split("/")
                    id_eveniment = int(parts[0])
                    data = parts[1]
                    timp = int(parts[2])
                    descriere = parts[3]
                    eveniment = Eveniment(id_eveniment, data, timp, descriere)
                    self._evenimente[id_eveniment] = eveniment

    def __write_all_to_file(self):
        with open(self.__cale_catre_fisier_evenimente, "w") as f:
            for eveniment in self._evenimente.values():
                f.write(str(eveniment)+"\n")

    def adauga_eveniment(self, eveniment):
        self.__read_all_from_file()
        RepoEvenimente.adauga_eveniment(self, eveniment)
        self.__write_all_to_file()

    def modifica_persoana(self, eveniment_actualizat):
        self.__read_all_from_file()
        RepoEvenimente.modifica_eveniment(self, eveniment_actualizat)
        self.__write_all_to_file()

    def sterge_persoana_dupa_id(self, id_eveniment):
        self.__read_all_from_file()
        RepoEvenimente.sterge_eveniment_dupa_id(self, id_eveniment)
        self.__write_all_to_file()

    def cauta_persoana_dupa_id(self, id_eveniment):
        self.__read_all_from_file()
        return RepoEvenimente.cauta_eveniment_dupa_id(self, id_eveniment)

    def get_all(self):
        self.__read_all_from_file()
        return RepoEvenimente.get_all(self)

    def size(self):
        self.__read_all_from_file()
        return RepoEvenimente.size(self)