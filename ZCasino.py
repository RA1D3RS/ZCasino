# -*-coding:Latin-1 -*

import os
# Importation de la fonction randrange du module random
from builtins import type
from random import randrange
# Importation de la fonction ceil du module math
from math import ceil       # arrondir au nombre sup�rieur

"""
JEU DE ROULETTE:
Le joueur mise sur un num�ro entre 0 et 49.
- Si le num�ro gagnant est celui sur lequel le joueur a mis� (probabilit� de 1/50, plut�t faible), 
    le croupier lui remet 3 fois la somme mis�e. 
- Sinon, le croupier regarde si le num�ro mis� par le joueur est de la m�me couleur que le num�ro gagnant
    (s'ils sont tous les deux pairs ou tous les deux impairs). Si c'est le cas, le croupier lui remet 50 % de la somme mis�e. 
- Si ce n'est pas le cas, le joueur perd sa mise.
"""
money = 1000
game_on = True

print ("Bonjour et bienvenue dans le jeu ZCasino".upper())
print("Vous avez des jetons d'un montant de {} $, � vous de jouer!".format(money))

while game_on:
    num�ro_mise = -1
    # le joueur saisi le num�ro sur lequel il veut misez
    while num�ro_mise < 0 or num�ro_mise > 49:
        num�ro_mise = input("Saisissez le num�ro sur lequel vous voulez miser (entre 0 et 49) :\n")
        try: # on s'assure que le joueur entre la valeur comme demand�
            num�ro_mise = int(num�ro_mise)
        except ValueError:
            print("La valeur saisie n'est pas un nombre")
            num�ro_mise = -1
            continue
        if num�ro_mise < 0:
            print("La num�ro saisie est inf�rieur � 0")
        elif num�ro_mise > 49:
            print("la num�ro saisie est sup�rieur � 49")
    montant_mise = 0
    #  le joueur saisi le montant de sa mise
    while montant_mise <= 0 or montant_mise > money:
        montant_mise = input("Saisissez le montant de votre mise :\n")
        try: # on s'assure que le joueur entre la valeur comme demand�
            montant_mise= int(montant_mise)
        except ValueError:
            print("La valeur saisie n'est pas un nombre")
            montant_mise = 0
            continue
        if montant_mise < 0:
            print("Le montant saisi est inf�rieur ou �gal � 0")
        elif montant_mise > money:
            print("la valeur saisie est sup�rieur � ", money, "$")

    # on d�duit la mise du montant initial
    money -= montant_mise
    # On fait tourner la roulette
    numero_gagnant = randrange(50)
    print("La roulette tourne\n     ...\n       ...\n           et s'arr�te sur le num�ro", numero_gagnant,"\n")

    # check les gains du joueur
    if numero_gagnant == num�ro_mise:
        print("F�licitation!!! Vous avez gagner {} $".format(montant_mise*3))
        money += (montant_mise*3) # Triple la mise de d�part
    elif numero_gagnant % 2 == num�ro_mise % 2:
        print("Vous avez misez sur la bonne couleur, vous remportez", ceil(montant_mise/2), "$")
        money += ceil(montant_mise/2) # r�cup�re la moiti� de la mise de d�part
    else:
        print("Perdu pour cette fois, vous perdez votre mise") # perdu = 0

     # interompre le jeu
    if money == 0:
        print("Fin de la partie,vous avez tout perdu")
        game_on = False
        quit()
    else:
        print("Vous avez jusqu'� pr�sent {} $".format(money)) # on affiche le montant restant
        quitter = input("Voulez vous quitter le casino (o/n) ?\n")
        if quitter == "O" or quitter == "o":
            print("Vous quittez le casino avec vos {} $, de gain".format(money))
            game_on = False
            quit()
        else:
            continue

# On met en pause le syst�me
os.system("pause")