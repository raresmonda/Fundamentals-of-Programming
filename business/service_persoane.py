from domeniu.persoana import Persoana

class ServicePersoane:

    def __init__(self, validator_persoana, repo_persoane):
        self.__validator_persoana = validator_persoana
        self.__repo_persoane = repo_persoane

    def adauga_persoana(self, id_persoana, nume, adresa):
        '''
        creeaza o persoana, o valideaza si o adauga in repo
        :param id_persoana: id-ul persoanei
        :param nume: numele persoanei
        :param adresa: adresa persoanei
        :return:
        '''
        persoana = Persoana(id_persoana, nume, adresa)
        self.__validator_persoana.valideaza(persoana)
        #self.__file_repo_persoane.adauga_persoana(persoana)
        self.__repo_persoane.adauga_persoana(persoana)

    def sterge_persoana(self, id_persoana):
        '''
        sterge persoana din repo dupa id
        :param id_persoana: id
        :return:
        '''
        self.__repo_persoane.sterge_persoana_dupa_id(id_persoana)


    def modifica_persoana(self, id_persoana, nume_actualizat, adresa_actualizata):
        '''
        modifica numele si adresa persoanei cu id-ul id_persoana
        :param id_persoana: id
        :param nume_actualizat: numele nou
        :param adresa_actualizata: adresa noua
        :return:
        '''
        persoana_actualizata = Persoana(id_persoana, nume_actualizat, adresa_actualizata)
        self.__validator_persoana.valideaza(persoana_actualizata)
        self.__repo_persoane.modifica_persoana(persoana_actualizata)

    def cauta_persoana(self, id_persoana):
        '''
        cauta o persoana dupa id in repo si o returneaza
        :param id_persoana: id
        :return:
        '''
        persoana = self.__repo_persoane.cauta_persoana_dupa_id(id_persoana)
        return persoana

    def get_persoana_dupa_id(self, id_persoana):
        '''
        returneaza persoana care are id-ul id persoana
        :param id_persoana: id
        :return:
        '''
        return self.__repo_persoane.cauta_persoana_dupa_id(id_persoana)

    def get_all_persoane(self):
        '''
        returneaza toate persoanele din repo
        :return:
        '''
        return self.__repo_persoane.get_all()