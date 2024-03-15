from domeniu import eveniment
from erori.repo_error import RepoError


class RepoEvenimente:

    def __init__(self):
        self._evenimente = {}

    def adauga_eveniment(self, eveniment):
        '''
        adauga un eveniment in lista
        :param eveniment: eveniment
        :return:
        '''
        if eveniment.get_id_eveniment() in self._evenimente:
            raise RepoError("eveniment existent!")
        self._evenimente[eveniment.get_id_eveniment()] = eveniment

    def sterge_eveniment_dupa_id(self, id_eveniment):
        '''
        sterge evenimentul cu id-ul id_eveniment din lista
        :param id_eveniment: id
        :return:
        '''
        if id_eveniment not in self._evenimente:
            raise RepoError("eveniment inexistent!")
        del self._evenimente[id_eveniment]

    def cauta_eveniment_dupa_id(self, id_eveniment):
        '''
        returneaza evenimentul cu id-ul id_eveniment
        :param id_eveniment: id
        :return:
        '''
        if id_eveniment not in self._evenimente:
            raise RepoError("eveniment inexistent!")
        return self._evenimente[id_eveniment]

    def modifica_eveniment(self, eveniment):
        '''
        actualizeaza un eveniment
        :param eveniment: eveniment
        :return:
        '''
        if eveniment.get_id_eveniment() not in self._evenimente:
            raise RepoError("evenimente inexistent!")
        self._evenimente[eveniment.get_id_eveniment()] = eveniment

    def get_all(self):
        '''
        returneaza toate evenimentele din lista
        :return:
        '''
        evenimente = []
        for eveniment_id in self._evenimente:
            evenimente.append(self._evenimente[eveniment_id])
        return evenimente

    def size(self):
        return len(self._evenimente)