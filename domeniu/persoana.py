class Persoana:

    def __init__(self, id_persoana, nume, adresa):
        self.__id_persoana = id_persoana
        self.__nume = nume
        self.__adresa = adresa
        self.__persoana = {
            "id_persoana":id_persoana,
            "nume":nume,
            "adresa":adresa
        }

    def creeaza_persoana(self, id_persoana, nume, adresa):
        '''
        creeaza o persoana cu id-ul unic de tip int id_persoana, numele de tip string nume
        si adresa de tip string adresa adresa
        :param id_persoana: int
        :param nume: string
        :param adresa: string
        :return: rez: persoana cu id-ul id_persoana, numele nume si adresa adresa
        '''
        self.__persoana = {
            "id_persoana":id_persoana,
            "nume":nume,
            "adresa":adresa
        }
        return self.__persoana

    def get_id_persoana(self):
        '''
        returneaza id-ul persoanei
        :return:
        '''
        #return self.__id_persoana
        return self.__persoana["id_persoana"]

    def get_nume(self):
        '''
        returneaza numele persoanei
        :return:
        '''
        #return self.__nume
        return self.__persoana["nume"]

    def set_nume(self, nume):
        '''
        schimba numele persoanei cu alt nume
        :param nume: numele nou
        :return:
        '''
        #self.__nume = nume
        self.__persoana["nume"] = nume

    def get_adresa(self):
        '''
        returneaza adresa persoanei
        :return:
        '''
        #return self.__adresa
        return self.__persoana["adresa"]

    def set_adresa(self, adresa):
        '''
        schimba adresa persoanei cu alta adresa
        :param adresa: adresa noua
        :return:
        '''
        self.__persoana["adresa"] = adresa

    def __eq__(self, other):
        return self.__id_persoana == other.__id_persoana

    def __str__(self):
        return f"{self.__id_persoana}/{self.__nume}/{self.__adresa}"
