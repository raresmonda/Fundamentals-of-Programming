class Inscriere:

    def __init__(self, id_inscriere, persoana, eveniment):
        self.__id_inscriere = id_inscriere
        self.__persoana = persoana
        self.__eveniment = eveniment

    def get_id_inscriere(self):
        '''
        returneaza id-ul inscrierii
        :return:
        '''
        return self.__id_inscriere

    def get_persoana(self):
        '''
        returneaza persoana care este inscrisa la eveniment
        :return:
        '''
        return self.__persoana

    def get_eveniment(self):
        '''
        returneaza evenimentul la care este inscrisa persoana
        :return:
        '''
        return self.__eveniment

    def __eq__(self, other):
        return self.__id_inscriere == other.__id_inscriere

    def __str__(self):
        return f"{self.__id_inscriere}|{self.__persoana}|{self.__eveniment}"