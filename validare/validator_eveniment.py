from erori.validation_error import ValidError
from datetime import datetime

class ValidatorEveniment:

    def __init__(self):
        pass

    def valideaza(self, eveniment):
        '''
        verifica daca parametrii evenimentului sunt valizi
        :param eveniment: eveniment
        :return:
        '''
        erori = ""
        if eveniment.get_id_eveniment() < 0:
            erori += "id invalid!\n"

        if eveniment.get_timp() < 0:
            erori += "timp invalid!\n"
        if eveniment.get_descriere() == "":
            erori += "descriere invalida!"
        if len(erori) > 0:
            raise ValidError(erori)