class Eveniment:

    def __init__(self, id_eveniment, data, timp, descriere):
        self.__id_eveniment = id_eveniment
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere

    def get_id_eveniment(self):
        '''
        returneaza id-ul evenimentului
        :return:
        '''
        return self.__id_eveniment

    def get_data(self):
        '''
        returneaza data evenimentului
        :return:
        '''
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_timp(self):
        '''
        returneaza durata evenimentului, in minute
        :return:
        '''
        return self.__timp

    def set_timp(self, timp):
        self.__timp = timp

    def get_descriere(self):
        '''
        returneaza descrierea evenimentului
        :return:
        '''
        return self.__descriere

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def __eq__(self, other):
        return self.__id_eveniment == other.__id_eveniment

    def __str__(self):
        return f"{self.__id_eveniment}/{self.__data}/{self.__timp}/{self.__descriere}"