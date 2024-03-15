from domeniu.inscrieri import Inscriere
from erori.repo_error import RepoError


class ServiceInscrieri:

    def __init__(self, validator_inscriere, repo_inscrieri, repo_persoane, repo_evenimente):
        self.__validator_inscriere = validator_inscriere
        self.__repo_inscrieri = repo_inscrieri
        self.__repo_persoane = repo_persoane
        self.__repo_evenimente = repo_evenimente

    def adauga_inscriere(self, id_inscriere, persoana, eveniment):
        '''
        creeaza o inscriere noua, o valideaza dupa care o adauga in repo
        :param id_inscriere: id
        :param persoana: persoana
        :param eveniment: eveniment
        :return:
        '''
        inscriere = Inscriere(id_inscriere, persoana, eveniment)
        self.__validator_inscriere.valideaza(inscriere)
        #self.__file_repo_inscrieri.adauga_inscriere(inscriere)
        self.__repo_inscrieri.adauga_inscriere(inscriere)

    def sterge_inscriere_dupa_persoana(self, id_persoana):
        '''
        sterge toate inscrierile la care participa persoana cu id-ul id_persoana
        :param id_persoana: id
        :return:
        '''
        lista = self.__repo_inscrieri.get_all()
        for inscriere in lista:
            if inscriere.get_persoana().get_id_persoana() == id_persoana:
                self.__repo_inscrieri.sterge_inscriere_dupa_id(inscriere.get_id_inscriere())

    def sterge_inscriere_dupa_eveniment(self, id_eveniment):
        '''
        sterge toate inscrierile care au ca eveniment evenimentul cu id-ul id_eveniment
        :param id_eveniment: id
        :return:
        '''
        lista = self.__repo_inscrieri.get_all()
        for inscriere in lista:
            if inscriere.get_eveniment().get_id_eveniment() == id_eveniment:
                self.__repo_inscrieri.sterge_inscriere_dupa_id(inscriere.get_id_inscriere())

    def genereaza_raport_cei_mai_multi_participanti_la_eveniment(self):
        '''
        returneaza id-urile persoanelor care participa la cele mai multe evenimente
        :return:
        '''
        lista = self.__repo_inscrieri.get_all()
        participari = []
        aparitii = {}
        for inscriere in lista:
            participari.append(inscriere.get_persoana().get_id_persoana())
        for participant in participari:
            if participant in aparitii:
                aparitii[participant] += 1
            else:
                aparitii[participant] = 1
        maxim = 0
        for aparitie in aparitii:
            if aparitii[aparitie] > maxim:
                maxim = aparitii[aparitie]
        id_persoane = []
        for aparitie in aparitii:
            if aparitii[aparitie] == maxim:
                id_persoane.append(int(aparitie))
        return id_persoane

    def creeaza_situatie_persoane(self):
        '''
        creaza un dictionar care are drept key id-ul unei persoane, in care vor fi introduse evenimentele la care va participa persoana
        :return:
        '''
        inscrieri = self.__repo_inscrieri.get_all()
        situatie_inscrieri = {}
        for inscriere in inscrieri:
            id_persoana = inscriere.get_persoana().get_id_persoana()
            if id_persoana not in situatie_inscrieri:
                situatie_inscrieri[id_persoana] = []
            situatie_inscrieri[id_persoana].append(inscriere.get_eveniment())
        return situatie_inscrieri

    def bubble_sort(self, lst, key_func):
        n = len(lst)
        for i in range(n):
            for j in range(0, n - i - 1):
                if key_func(lst[j]) > key_func(lst[j + 1]):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst

    def shell_sort(self, lst, key_func, cmp):
        gap = len(lst) // 2
        while gap > 0:
            for i in range(gap, len(lst)):
                temp = lst[i]
                j = i
                while j >= gap and key_func(temp) < key_func(lst[j - gap]) and cmp(temp, lst[j - gap], key_func):
                    lst[j] = lst[j - gap]
                    j -= gap
                lst[j] = temp
            gap //= 2
        return lst

    def cmp(self, el1, el2, key):
        if key(el1)[0] < key(el2)[0]:
            return True
        else:
            if key(el1)[0] == key(el2)[0]:
                return key(el1)[1] < key(el2)[1]
        return False

    def lista_de_evenimente_pentru_o_persoana_ordonata_alfabetic(self, id_persoana):
        '''
        returneaza id-urile evenimentelor la care participa persoana cu id-ul id_persoana
        sortate alfabetic dupa descriere
        :param id_persoana: id
        :return:
        '''
        self.__repo_persoane.cauta_persoana_dupa_id(id_persoana)
        situatie_inscrieri = self.creeaza_situatie_persoane()
        if id_persoana in situatie_inscrieri:
            lista_evenimente = situatie_inscrieri[id_persoana]
            lista_evenimente = self.bubble_sort(lista_evenimente, key_func=lambda x: (x.get_descriere(), x.get_data()))
        else:
            raise RepoError("Persoana nu are inscrieri!")
        id_evenimente = []
        for i in range(len(lista_evenimente)):
            id_evenimente.append(lista_evenimente[i].get_id_eveniment())
        return id_evenimente

    def lista_de_evenimente_pentru_o_persoana_ordonata_dupa_data(self, id_persoana):
        '''
        returneaza id-urile evenimentelor la care participa persoana cu id-ul id_persoana
        sortate dupa data
        :param id_persoana: id
        :return:
        '''
        self.__repo_persoane.cauta_persoana_dupa_id(id_persoana)
        situatie_inscrieri = self.creeaza_situatie_persoane()
        if id_persoana in situatie_inscrieri:
            lista_evenimente = situatie_inscrieri[id_persoana]
            lista_evenimente = self.shell_sort(lista_evenimente, key_func=lambda x: (x.get_data(), x.get_descriere()), cmp = self.cmp)
        else:
            raise RepoError("Persoana nu are inscrieri!")
        id_evenimente = []
        for i in range(len(lista_evenimente)):
            id_evenimente.append(lista_evenimente[i].get_id_eveniment())
        return id_evenimente

    def genereaza_raport_primele_evenimente(self):
        '''
        returneaza id-urile evenimentelor cu primii 20% cei mai multi participanti
        :return:
        '''
        evenimente = self.__repo_evenimente.get_all()
        procent = round(len(evenimente) / 5)
        lista = self.__repo_inscrieri.get_all()
        participari = []
        aparitii = {}
        for inscriere in lista:
            participari.append(inscriere.get_eveniment().get_id_eveniment())
        for participant in participari:
            if participant in aparitii:
                aparitii[participant] += 1
            else:
                aparitii[participant] = 1
        aparitii_sortate = sorted(aparitii.items(), key=lambda x:x[1], reverse=True)
        id_evenimente = []
        for aparitie in aparitii_sortate:
            if len(id_evenimente) < procent:
                id_evenimente.append(aparitie[0])
                id_evenimente.append(aparitie[1])
        return id_evenimente

    def genereaza_raport_persoane_participante_la_un_eveniment(self, id_eveniment):
        '''
        returneaza id-urile persoanelor care participa la evenimentul cu id-ul id_eveniment
        :param id_eveniment:
        :return:
        '''
        lista = self.__repo_inscrieri.get_all()
        id_persoane = []
        for inscriere in lista:
            if inscriere.get_eveniment().get_id_eveniment() == id_eveniment:
                id_persoane.append(inscriere.get_persoana().get_id_persoana())
        return id_persoane

    def printeaza_raport_in_fisier(self, persoane):
        cale_catre_fisier = "file_raport.txt"
        with open(cale_catre_fisier, "w") as f:
            pass
        with open(cale_catre_fisier, "w") as f:
            for persoana in persoane:
                f.write(str(persoana) + "\n")

    def get_inscriere_dupa_persoana(self, persoana):
        '''
        returneaza inscrierea care are ca si participant persoana
        :param persoana: persoana
        :return:
        '''
        return self.__repo_inscrieri.cauta_inscriere_dupa_persoana(persoana)

    def get_all_inscrieri(self):
        '''
        returneaza toate inscrierile
        :return:
        '''
        return self.__repo_inscrieri.get_all()