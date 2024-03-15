from domeniu.eveniment import Eveniment


class ServiceEvenimente:

    def __init__(self, validator_eveniment, repo_evenimente):
        self.__validator_eveniment = validator_eveniment
        self.__repo_evenimente = repo_evenimente


    def adauga_eveniment(self, id_eveniment, data, timp, descriere):
        '''
        creeaza un nou eveniment, il valideaza si il adauga in repo
        :param id_eveniment: id
        :param data: data
        :param timp: timp
        :param descriere: descriere
        :return:
        '''
        eveniment = Eveniment(id_eveniment, data, timp, descriere)
        self.__validator_eveniment.valideaza(eveniment)
        #self.__repo_evenimente.adauga_eveniment(eveniment)
        self.__repo_evenimente.adauga_eveniment(eveniment)

    def sterge_eveniment(self, id_eveniment):
        '''
        sterge evenimentul cu id-ul id_eveniment din repo
        :param id_eveniment: id
        :return:
        '''
        self.__repo_evenimente.sterge_eveniment_dupa_id(id_eveniment)

    def modifica_eveniment(self, id_eveniment, data_actualizata, timp_actualizat, descriere_actualizata):
        '''
        actualizeaza data, timpul si descrierea evenimentului cu id-ul id_eveniment
        :param id_eveniment: id
        :param data_actualizata: data
        :param timp_actualizat: timp
        :param descriere_actualizata: descriere
        :return:
        '''
        eveniment_actualizat = Eveniment(id_eveniment, data_actualizata, timp_actualizat, descriere_actualizata)
        self.__validator_eveniment.valideaza(eveniment_actualizat)
        self.__repo_evenimente.modifica_eveniment(eveniment_actualizat)

    def cauta_eveniment(self, id_eveniment):
        '''
        cauta evenimentul cu id-ul id_eveniment si il returneaza
        :param id_eveniment: id
        :return:
        '''
        eveniment = self.__repo_evenimente.cauta_eveniment_dupa_id(id_eveniment)
        return eveniment

    def get_eveniment_dupa_id(self, id_eveniment):
        '''
        returneaza evenimentul care are id-ul id_eveniment
        :param id_eveniment: id
        :return:
        '''
        return self.__repo_evenimente.cauta_eveniment_dupa_id(id_eveniment)

    def get_all_evenimente(self):
        '''
        returneaza toate evenimentele din repo
        :return:
        '''
        return self.__repo_evenimente.get_all()