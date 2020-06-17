# ZCasino
Jeu de roulette avec des règles simplifiées, dans le cadre d'un TP j'ai réalisé ce code.

Les règles sont simples:
  - le joueur est invité à rentrer le numéro sur lequel il veut miser, on vérifie la veleur entrée.
    la valeur doit être comprise entre 0 et 49.
  - le joueur est invité à rentrer le montant de sa mise, on revérifie la veleur entrée.
    La valeur doit être comprise entre 1 et 1000$ pour commencer.
   
   *  Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible), 
    le croupier lui remet 3 fois la somme misée. 
   *  Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que le numéro gagnant
    (s'ils sont tous les deux pairs ou tous les deux impairs). Si c'est le cas, le croupier lui remet 50 % de la somme misée. 
   *  Si ce n'est pas le cas, le joueur perd sa mise.

Après chaque tour on demande au joueur s'il désire quitter la partie et repartir avec ses gains.
le joueur peut quitter le jeu à n'import quelle moment.
Si le joueur perd tout sont argent le jeu s'arrête automatiquement.
