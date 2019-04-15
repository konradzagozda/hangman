import random

# this is a comment XDDD gitcik co

pictures = [
    """
     --------
    |       |
    |       
    |
    |
    |
    """,
    """
     --------
    |       |
    |       O
    |
    |
    |
    """,
    """
     --------
    |       |
    |       O
    |       |
    |       |
    |
    """,
    """
     --------
    |       |
    |       O
    |      /|
    |       |
    |
    """,
    """
     --------
    |       |
    |       O
    |      /|\\
    |       |
    |
    """,
    """
     --------
    |       |
    |       O
    |      /|\\
    |       |
    |      /
    """,
    """
     --------
    |       |
    |       O
    |      /|\\
    |       |
    |      / \\
    """
]


def choose_random_word():
    with open('sowpods.txt', 'r') as dic:
        alist = [line.rstrip() for line in dic.readlines()]
        choice = random.choice(alist)
    return choice


def guess_letters(word):
    print("Welcome to Hangman game!")
    print(pictures[0])
    tries = 0
    incorrect_moves = 0
    letters_already_guessed = []
    hidden_word = ['_' for x in range(len(word))]
    while '_' in hidden_word and incorrect_moves < 6:
        print(' '.join(hidden_word))
        while True:
            guess = input('Guess your letter:').lower()
            if guess not in letters_already_guessed:
                letters_already_guessed.append(guess)
                break
            else:
                print('You\'ve already tried this letter! Try again!')

        tries += 1
        if guess.lower() not in word.lower():
            incorrect_moves += 1
            print(f'Incorrect! You\'ve {6-incorrect_moves} chances left')
            print(pictures[incorrect_moves])

        else:
            how_many = 0
            for i, x in enumerate(word.lower()):
                if x == guess:
                    hidden_word[i] = guess
                    how_many += 1
            print('Correct! ')
    if '_' in hidden_word:
        print('Unfortunately! Maybe next time!')
    else:
        print('Congratulations! You\'ve won!')
    return ''.join(hidden_word)


if __name__ == '__main__':
    while True:
        word = choose_random_word()
        guess_letters(word)
        game = input('Do you want to start a new game? (y/n)').lower()
        if game == 'n':
            break

