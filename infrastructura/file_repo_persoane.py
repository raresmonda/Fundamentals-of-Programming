from domeniu.persoana import Persoana
from infrastructura.repo_persoane import RepoPersoane


class FileRepoPersoane(RepoPersoane):

    def __init__(self, cale_catre_fisier_persoane):
        RepoPersoane.__init__(self)
        self.__cale_catre_fisier_persoane = cale_catre_fisier_persoane

    def __read_all_from_file(self):
        with open(self.__cale_catre_fisier_persoane, "r") as f:
            lines = f.readlines()
            self._persoane.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split("/")
                    id_persoana = int(parts[0])
                    nume = parts[1]
                    adresa = parts[2]
                    persoana = Persoana(id_persoana, nume, adresa)
                    self._persoane[id_persoana] = persoana

    def __write_all_to_file(self):
        with open(self.__cale_catre_fisier_persoane, "w") as f:
            for persoana in self._persoane.values():
                f.write(str(persoana)+"\n")

    def adauga_persoana(self, persoana):
        self.__read_all_from_file()
        RepoPersoane.adauga_persoana(self, persoana)
        self.__write_all_to_file()

    def modifica_persoana(self, persoana_actualizata):
        self.__read_all_from_file()
        RepoPersoane.modifica_persoana(self, persoana_actualizata)
        self.__write_all_to_file()

    def sterge_persoana_dupa_id(self, id_persoana):
        self.__read_all_from_file()
        RepoPersoane.sterge_persoana_dupa_id(self, id_persoana)
        self.__write_all_to_file()

    def cauta_persoana_dupa_id(self, id_persoana):
        self.__read_all_from_file()
        return RepoPersoane.cauta_persoana_dupa_id(self, id_persoana)

    def get_all(self):
        self.__read_all_from_file()
        return RepoPersoane.get_all(self)

    def size(self):
        self.__read_all_from_file()
        return RepoPersoane.size(self)