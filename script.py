from tkinter import *
from random import randint

mainapp = Tk()

mainapp.title("Le jeu du nombre pensé")
mainapp.geometry('800x600')
mainapp.minsize(480, 360)
mainapp.config(background='#41B77F')

# les constantes
point_en_moins = 5
mise_de_depart = 100

# les variables
prix_a_trouver = randint(1, 10)
point_a_gagner = mise_de_depart
point_total = 0
liste_propositions = []
prix_propose = 0


def si_trouve():
    global point_total
    global point_a_gagner
    global mise_de_depart
    global prix_a_trouver
    global liste_propositions
    point_total += point_a_gagner
    info_reponse.config(text="!!! Bonne réponse !!!\nVous cumulez " + str(point_total) + " points.")
    print("!!! Bonne réponse !!!\nVous cumulez", point_total, 'points.')
    point_a_gagner = mise_de_depart
    prix_a_trouver = randint(1, 10)
    liste_propositions = []
    depart()


def si_plus():
    global point_a_gagner
    global point_en_moins
    info_reponse.config(text="C'est plus !")
    print("C'est plus !")
    point_a_gagner -= point_en_moins
    depart()


def si_moins():
    global point_a_gagner
    global point_en_moins
    info_reponse.config(text="C'est moins !")
    print("C'est moins !")
    point_a_gagner -= point_en_moins
    depart()


def valider():
    global prix_propose
    texte_propose = texte_renseigne.get()
    try:
        prix_propose = int(texte_propose)
        print(prix_propose)
        comparaison()
    except ValueError:
        info_reponse.config(text='Valeur rentrée non valide.')
        depart()


def comparaison():
    global liste_propositions
    global prix_propose
    if prix_propose == prix_a_trouver:
        si_trouve()
    elif prix_propose < prix_a_trouver:
        liste_propositions.append(prix_propose)
        si_plus()
    elif prix_propose > prix_a_trouver:
        liste_propositions.append(prix_propose)
        si_moins()


def depart():
    point_et_liste.config(text='Points en jeu : {} ; '
                               'propositions déjà faites : {}'.format(point_a_gagner, liste_propositions))


titre = Label(mainapp, text='Le jeu du nombre pensé !', font=("Courrier", 40), bg='#41B77F', fg='white')
titre.pack(pady=5)

msg_sous_titre = 'Tentez de cumuler le plus de point possible...'
sous_titre = Label(mainapp, text=msg_sous_titre, font=("Courrier", 20), bg='#41B77F', fg='white')
sous_titre.pack(pady=25)

msg_chiffre = 'Proposer un nombre entier entre 1 et 10 :'
demande_chiffre = Label(mainapp, text=msg_chiffre, font=("Courrier", 20), bg='#41B77F', fg='white')
demande_chiffre.pack(pady=20)

info_reponse = Label(mainapp, text="   ", font=("Courrier", 20), bg='#41B77F', fg='white')
info_reponse.pack(pady=20)

texte_renseigne = Entry(mainapp, font=("Courrier", 15), bg='white', fg='#41B77F')
texte_renseigne.pack(pady=20)

btn = Button(mainapp, height=1, width=10, text="Valider", font=("Courrier", 15), bg='#41B77F', fg='white',
             command=valider)
btn.pack()

point_et_liste = Label(mainapp, text='Points en jeu : {} ; propositions déjà faites : {}'.format(point_a_gagner,
                                                                                                 liste_propositions),
                       font=("Courrier", 20), bg='#41B77F', fg='white')
point_et_liste.pack(pady=20)

mainapp.mainloop()
