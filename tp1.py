from wrapper import Wrapper
from typing import Tuple, Callable
from utils import try_int
from base_exo import BaseExo, BaseTP

class Exo1(BaseExo):
    name = "Exercice 1"

    def execute(self) -> Wrapper:
        user_name: str = input("Entrez votre nom: ")
        print(f"Bonjour {user_name}")
        
        return Wrapper.Success()

class Exo2(BaseExo):
    name = "Exercice 2"

    def execute(self) -> Wrapper:
        nb_box: Wrapper = try_int(input("Entrez un nombre: "))
        if(not nb_box.check):
            return nb_box
        
        nb_1: int = nb_box.data
        
        nb_box: Wrapper = try_int(input("Entrez un autre nombre: "))
        if(not nb_box.check):
            return nb_box
        
        nb_2: int = nb_box.data
        
        somme: int = nb_1 + nb_2
        print(f"Some = {somme}\nDifférence = {nb_1 - nb_2}\nMoyenne = {somme / 2}")
        
        return Wrapper.Success()

class Exo3(BaseExo):
    name = "Exercice 3"    

    def execute(self) -> Wrapper:
        NB_FEUILLE: int = 90
        NB_FEUILLE_PAR_RAMETTE: int = 500
        
        nb_student_box: Wrapper = try_int(input("Entrez le nombre d'élève: "))
        if(not nb_student_box.check):
            return nb_student_box
        
        nb_student: int = nb_student_box.data
        
        nb_feuille: int = nb_student * NB_FEUILLE
        print(f"Nombre de feuille: {nb_feuille}\nNombre de ramette de {NB_FEUILLE_PAR_RAMETTE}: {nb_feuille // NB_FEUILLE_PAR_RAMETTE + 1}")
        
        
        return Wrapper.Success()

class TP1(BaseTP):
    name = "TP 1"
    tp_exo_list = (Exo1(), Exo2(), Exo3())
