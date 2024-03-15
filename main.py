from random import random
from infrastructura.file_repo_evenimente import FileRepoEvenimente
from infrastructura.file_repo_inscrieri import FileRepoInscrieri
from infrastructura.file_repo_persoane import FileRepoPersoane
from testare.teste_unittest import TestePersoana, TesteEveniment, TesteRepoPersoane, TesteRepoEvenimente, \
    TesteRepoInscrieri, TesteValidatorPersoana, TesteValidatorEveniment, TesteServicePersoane, TesteServiceEvenimente, \
    TesteServiceInscrieri
from validare.validator_persoana import ValidatorPersoana
from validare.validator_eveniment import ValidatorEveniment
from validare.validator_inscriere import ValidatorInscriere
from infrastructura.repo_persoane import RepoPersoane
from infrastructura.repo_evenimente import RepoEvenimente
from infrastructura.repo_inscrieri import RepoInscrieri
from business.service_persoane import ServicePersoane
from business.service_evenimente import ServiceEvenimente
from business.service_inscrieri import ServiceInscrieri
from prezentare.ui import UI
from testare.teste import Teste
from testare.teste_file_repo_persoane import TesteFilePersoane
from generare.random import Random

if __name__ == '__main__':
    validator_persoana = ValidatorPersoana()
    validator_eveniment = ValidatorEveniment()
    validator_inscriere = ValidatorInscriere()
    repo_persoane = RepoPersoane()
    repo_evenimente = RepoEvenimente()
    repo_inscrieri = RepoInscrieri()

    cale_catre_fisier_persoane = "persoane.txt"
    file_repo_persoane = FileRepoPersoane(cale_catre_fisier_persoane)
    cale_catre_fisier_evenimente = "evenimente.txt"
    file_repo_evenimente = FileRepoEvenimente(cale_catre_fisier_evenimente)
    cale_catre_fisier_inscrieri = "inscrieri.txt"
    file_repo_inscrieri = FileRepoInscrieri(cale_catre_fisier_inscrieri)

    with open(cale_catre_fisier_persoane, "w") as f:
        pass
    with open(cale_catre_fisier_evenimente, "w") as g:
        pass
    with open(cale_catre_fisier_inscrieri, "w") as g:
        pass

    service_persoane = ServicePersoane(validator_persoana, repo_persoane)
    service_evenimente = ServiceEvenimente(validator_eveniment, repo_evenimente)
    service_inscrieri = ServiceInscrieri(validator_inscriere, repo_inscrieri, repo_persoane, repo_evenimente)
    ui = UI(service_persoane, service_evenimente, service_inscrieri)
    teste = Teste(validator_persoana, validator_eveniment, repo_persoane, repo_persoane, repo_evenimente, service_persoane, service_evenimente, service_inscrieri, repo_inscrieri)
    teste_file_persoane = TesteFilePersoane(validator_persoana, validator_eveniment, repo_persoane, repo_evenimente, service_persoane, service_evenimente, service_inscrieri, file_repo_inscrieri)

    testepersoana = TestePersoana()
    testeeveniment = TesteEveniment()
    testevalidatorpersoana = TesteValidatorPersoana(validator_persoana)
    testevalidatoreveniment = TesteValidatorEveniment(validator_eveniment)
    testerepopersoane = TesteRepoPersoane(repo_persoane)
    testerepoevenimete = TesteRepoEvenimente(repo_evenimente)
    testerepoinscrieri = TesteRepoInscrieri(repo_inscrieri)
    testeservicepersoane = TesteServicePersoane(service_persoane)
    testeserviceevenimente = TesteServiceEvenimente(service_evenimente)
    testeserviceinscrieri = TesteServiceInscrieri(service_inscrieri)

    testepersoana.ruleaza_teste()
    testeeveniment.ruleaza_teste()
    testerepopersoane.ruleaza_teste()
    testerepoevenimete.ruleaza_teste()
    testerepoinscrieri.ruleaza_teste()
    testevalidatorpersoana.ruleaza_teste()
    testevalidatoreveniment.ruleaza_teste()
    testeservicepersoane.ruleaza_teste()
    #testeserviceevenimente.ruleaza_teste()
    testeserviceinscrieri.ruleaza_teste()

    random = Random(service_persoane, service_evenimente)
    random.generare_persoane()
    random.generare_evenimente()
    #teste_file_persoane.ruleaza_toate_testele_file()
    teste.ruleaza_toate_testele()
    ui.run()


