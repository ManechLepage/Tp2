"""
Fait par Manech Lepage
Groupe 403
Ce code permet de jouer a un jeu ou l'ordinateur choisit un nombre aleatoire et le joueur doit trouver le nombre.
"""

import random

def choose_range() :
    number_range = str(input("Choississez les bornes du nombre aleatoire. Mettez un espace entre les deux nombres.\nBornes :  ")).split()
    guessing_nbr = random.randint(int(number_range[0]), int(number_range[1]))
    return guessing_nbr

def main():
    is_playing = True

    while is_playing:
        guessing_nbr = choose_range()
        guessed_found = False
        guess_count = 0

        while not guessed_found:
            guess_count += 1
            user_guess_defined = False
            while not user_guess_defined:
                try:
                    guess = int(input("Choisissez votre nombre : \t"))
                    user_guess_defined = True
                except ValueError:
                    print("Ecrivez un nombre")

            if guess == guessing_nbr:
                guessed_found = True
            elif guess < guessing_nbr:
                print("Votre nombre est plus petit")
            else:
                print("Votre nombre est plus grand")

        print(f"Vous avez trouvez le nombre en {guess_count} essais!")

        if input("Enter pour recommencer") != "":
            is_playing = False
    quit()


if __name__ == "__main__":
    main()
