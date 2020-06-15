# -*-coding:Latin-1 -*

import os
# Importation de la fonction randrange du module random
from builtins import type
from random import randrange
# Importation de la fonction ceil du module math
from math import ceil       # arrondir au nombre supérieur

"""
JEU DE ROULETTE:
Le joueur mise sur un numéro entre 0 et 49.
- Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible), 
    le croupier lui remet 3 fois la somme misée. 
- Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que le numéro gagnant
    (s'ils sont tous les deux pairs ou tous les deux impairs). Si c'est le cas, le croupier lui remet 50 % de la somme misée. 
- Si ce n'est pas le cas, le joueur perd sa mise.
"""
money = 1000
game_on = True

print ("Bonjour et bienvenue dans le jeu ZCasino".upper())
print("Vous avez des jetons d'un montant de {} $, à vous de jouer!".format(money))

while game_on:
    numéro_mise = -1
    # le joueur saisi le numéro sur lequel il veut misez
    while numéro_mise < 0 or numéro_mise > 49:
        numéro_mise = input("Saisissez le numéro sur lequel vous voulez miser (entre 0 et 49) :\n")
        try: # on s'assure que le joueur entre la valeur comme demandé
            numéro_mise = int(numéro_mise)
        except ValueError:
            print("La valeur saisie n'est pas un nombre")
            numéro_mise = -1
            continue
        if numéro_mise < 0:
            print("La numéro saisie est inférieur à 0")
        elif numéro_mise > 49:
            print("la numéro saisie est supérieur à 49")
    montant_mise = 0
    #  le joueur saisi le montant de sa mise
    while montant_mise <= 0 or montant_mise > money:
        montant_mise = input("Saisissez le montant de votre mise :\n")
        try: # on s'assure que le joueur entre la valeur comme demandé
            montant_mise= int(montant_mise)
        except ValueError:
            print("La valeur saisie n'est pas un nombre")
            montant_mise = 0
            continue
        if montant_mise < 0:
            print("Le montant saisi est inférieur ou égal à 0")
        elif montant_mise > money:
            print("la valeur saisie est supérieur à ", money, "$")

    # on déduit la mise du montant initial
    money -= montant_mise
    # On fait tourner la roulette
    numero_gagnant = randrange(50)
    print("La roulette tourne\n     ...\n       ...\n           et s'arrête sur le numéro", numero_gagnant,"\n")

    # check les gains du joueur
    if numero_gagnant == numéro_mise:
        print("Félicitation!!! Vous avez gagner {} $".format(montant_mise*3))
        money += (montant_mise*3) # Triple la mise de départ
    elif numero_gagnant % 2 == numéro_mise % 2:
        print("Vous avez misez sur la bonne couleur, vous remportez", ceil(montant_mise/2), "$")
        money += ceil(montant_mise/2) # récupère la moitié de la mise de départ
    else:
        print("Perdu pour cette fois, vous perdez votre mise") # perdu = 0

     # interompre le jeu
    if money == 0:
        print("Fin de la partie,vous avez tout perdu")
        game_on = False
        quit()
    else:
        print("Vous avez jusqu'à présent {} $".format(money)) # on affiche le montant restant
        quitter = input("Voulez vous quitter le casino (o/n) ?\n")
        if quitter == "O" or quitter == "o":
            print("Vous quittez le casino avec vos {} $, de gain".format(money))
            game_on = False
            quit()
        else:
            continue

# On met en pause le système
os.system("pause")