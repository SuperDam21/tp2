"""
Nom:    Damien Thibodeau
Groupe: 4-123
Projet: TP2; Fire deviner un chiffre à l'utilisateur
"""
import random
jouer=True
while jouer:
    print("Bienvenue! votre objectif est de deviner mon nombre en moins de 6 essais")
    def minimum():
        nb_min_str= input("Quel est le nombre minimal que vous voulez deviner?: ")
        return int(nb_min_str)
    def maximum():
        nb_max_str = input("Quel est le nombre maximal que vous voulez deviner?: ")
        return int(nb_max_str)

    nombre_str = random.randint(minimum(), maximum())
    nombre=int(nombre_str)

    devine=False
    essais=0

    while not devine:
        reponse=int(input("Quel nombre voulez-vous essayer? "))
        if reponse == nombre:
            print("BRAVO! vous avez deviné!")
            essais = essais+1
            devine = True
        elif reponse > nombre:
            print(f"Mauvaise réponse! le nombre est plus petit que ", reponse)
            essais = essais + 1
        elif reponse < nombre:
            print(f"Mauvaise réponse! le nombre est plus grand que ", reponse)
            essais = essais + 1
        else:
            print("Si vous voyez ceci, une erreur est survenue")
            jouer = False
    if essais < 6:
        print(f"Score final: ",essais, "essais. FÉLICITATIONS!")
    else:
        print(f"Score final: ", essais, "essais. Meilleure chance la prochaine fois!")
    rejouer = input("Entrez n'importe quel caractère pour recommencer, entrez «NON» pour fermer: ")
    if rejouer != "NON":
        jouer = True
    else:
        jouer = False