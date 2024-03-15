from erori.validation_error import ValidError


class ValidatorPersoana:

    def __init__(self):
        pass

    def valideaza(self, persoana):
        '''
        verifica daca parametrii persoanei sunt valizi
        :param persoana: persoana
        :return:
        '''
        erori = ""
        if persoana.get_id_persoana() < 0:
            erori += "id invalid!\n"
        if persoana.get_nume() == "":
            erori += "nume invalid!\n"
        if persoana.get_adresa() == "":
            erori += "adresa invalida!"
        if len(erori) > 0:
            raise ValidError(erori)