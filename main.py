import random


def main():
    is_playing = True

    while is_playing:

        guessing_nbr = random.randint(0, 1000)
        guessed_found = False

        while not guessed_found:

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

        print("Vous avez trouvez le nombre!")

        if input("Enter pour recommencer") != "":
            is_playing = False
    quit()


if __name__ == "__main__":
    main()
