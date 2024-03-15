from erori.repo_error import RepoError


class RepoInscrieri:

    def __init__(self):
        self._inscrieri = {}

    def adauga_inscriere(self, inscriere):
        '''
        inscrie o persoana la un eveniment
        :param inscriere: inscriere
        :return:
        '''
        if inscriere.get_id_inscriere() in self._inscrieri:
            raise RepoError("inscriere existenta!")
        self._inscrieri[inscriere.get_id_inscriere()] = inscriere

    def sterge_inscriere_dupa_id(self, id_inscriere):
        '''
        sterge inscrierea cu id-ul specificat
        :param id_inscriere: id
        :return:
        '''
        if id_inscriere not in self._inscrieri:
            raise RepoError("inscriere inexistenta!")
        del self._inscrieri[id_inscriere]

    def get_all(self):
        '''
        returneaza lista cu inscrieri
        :return:
        '''
        inscrieri = []
        for inscriere_id in self._inscrieri:
            inscrieri.append(self._inscrieri[inscriere_id])
        return inscrieri

    def size(self):
        return len(self._inscrieri)