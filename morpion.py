import random

def creer_grille():
    return [[' ' for _ in range(3)] for _ in range(3)]


def afficher_grille(grille):
    for ligne in grille:
        print('|'.join(ligne))
        print('-' * 5)


def mouvement_valide(grille, ligne, colonne):
    return grille[ligne][colonne] == ' '


def ligne_gagnante(grille, symbole):
    for ligne in grille:
        if all(pion == symbole for pion in ligne):
            return True
    return False


def colonne_gagnante(grille, symbole):
    for j in range(3):
        if all(grille[i][j] == symbole for i in range(3)):
            return True
    return False


def diagonale_gagnante(grille, symbole):
    if all(grille[i][i] == symbole for i in range(3)) or \
       all(grille[i][2-i] == symbole for i in range(3)):
        return True
    return False


def verifier_victoire(grille, symbole):
    return ligne_gagnante(grille, symbole) or \
           colonne_gagnante(grille, symbole) or \
           diagonale_gagnante(grille, symbole)


def grille_pleine(grille):
    return all(pion != ' ' for ligne in grille for pion in ligne)


def tour_joueur(grille):
    while True:
        try:
            ligne = int(input("Entrez le numéro de ligne (0, 1 ou 2) : "))
            colonne = int(input("Entrez le numéro de colonne (0, 1 ou 2) : "))
            if 0 <= ligne < 3 and 0 <= colonne < 3 and mouvement_valide(grille, ligne, colonne):
                grille[ligne][colonne] = 'X'
                break
            else:
                print("Mouvement invalide. Réessayez.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")


def tour_ordinateur(grille):
    while True:
        ligne = random.randint(0, 2)
        colonne = random.randint(0, 2)
        if mouvement_valide(grille, ligne, colonne):
            grille[ligne][colonne] = 'O'
            break


def jouer_morpion():
    while True:
        grille = creer_grille()
        tour = 0

        while True:
            afficher_grille(grille)

            if tour % 2 == 0:
                tour_joueur(grille)
                symbole = 'X'
            else:
                tour_ordinateur(grille)
                symbole = 'O'

            if verifier_victoire(grille, symbole):
                afficher_grille(grille)
                print(f"Le joueur {symbole} a gagné !")
                break
            elif grille_pleine(grille):
                afficher_grille(grille)
                print("Match nul !")
                break

            tour += 1

        rejouer = input("Voulez-vous rejouer ? (o/n) : ")
        if rejouer.lower() != 'o':
            break

if __name__ == "__main__":
    jouer_morpion()

