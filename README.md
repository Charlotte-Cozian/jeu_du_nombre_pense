# jeu_du_nombre_pense
L'ordinateur a choisi un nombre entier entre 1 et 10, à vous de trouver lequel !

ligne 1 et 2 : importation des modules nécessaires ('tkinter' pour l'interface et 'randint' pour avoir un nombre au hazard)
ligne 4 à 9 : création de l'interface
ligne 12 à 20 : initialisation des variables
ligne 23 à 35 : fonction appelée si la proposition faite par l'utilisateur est correcte
  ligne 24 à 28 : appel des variables
  ligne 29 : ajout des points gagnés aux point total de la partie
  ligne 30 : modification du message affiché à l'utilisateur
  ligne 31 : affichage du message dans la console pour le suivi du programme
  ligne 32 : remise à zéro du nombre de point à gagner
  ligne 33 : création d'un nouveau nombre à deviner
  ligne 34 : vidage de la liste des propositions
  ligne 35 : appel de la fonction de départ
ligne 38 à 44 : fonction appelée si la proposition faite est inférieur au nombre à trouver
ligne 47 à 53 : fonction appelée si la proposition faite est supérieur
ligne 56 à 65 : fonction qui vérifie l'intégrité de la valeur récupérée par l'interface
ligne 68 à 78 : fonction qui vérifie si la proposition correspond à la valeur recherchée
ligne 81 à 83 : fonction de départ qui affiche les points en jeu et la liste des nombres déjà proposées
ligne 86 à 110 : création des widgets
ligne 112 : fonction qui met à jour l'interface en continu
