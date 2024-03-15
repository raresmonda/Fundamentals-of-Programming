from erori.repo_error import RepoError


class RepoPersoane:

    def __init__(self):
        self._persoane = {}

    def adauga_persoana(self, persoana):
        '''
        adauga o persoana la lista
        :param persoana: persoana
        :return:
        '''
        if persoana.get_id_persoana() in self._persoane:
            raise RepoError("persoana existenta!")
        self._persoane[persoana.get_id_persoana()] = persoana

    def sterge_persoana_dupa_id(self, id_persoana):
        '''
        sterge din lista persoana cu id-ul specificat
        :param id_persoana: id
        :return:
        '''
        if id_persoana not in self._persoane:
            raise RepoError("persoana inexistenta!")
        del self._persoane[id_persoana]

    def cauta_persoana_dupa_id(self, id_persoana):
        '''
        returneaza persoana cu id-ul id_persoana
        :param id_persoana: id
        :return:
        '''
        if id_persoana not in self._persoane:
            raise RepoError("persoana inexistenta!")
        return self._persoane[id_persoana]

    def modifica_persoana(self, persoana_actualizata):
        '''
        actualizeaza datele unei persoane
        :param persoana_actualizata: datele noi ale persoanei
        :return:
        '''
        if persoana_actualizata.get_id_persoana() not in self._persoane:
            raise RepoError("persoana inexistenta!")
        self._persoane[persoana_actualizata.get_id_persoana()] = persoana_actualizata

    def get_all(self):
        '''
        returneaza toate persoanele din lista
        :return:
        '''
        persoane = []
        for persoane_id in self._persoane:
            persoane.append(self._persoane[persoane_id])
        return persoane

    def size(self):
        return len(self._persoane)