from erori.validation_error import ValidError

class ValidatorInscriere:

    def __init__(self):
        pass

    def valideaza(self, inscriere):
        '''
        verifica daca parametrii inscrierii sunt valizi
        :param inscriere: inscriere
        :return:
        '''
        erori = ""
        if inscriere.get_id_inscriere() < 0:
            erori += "id invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)