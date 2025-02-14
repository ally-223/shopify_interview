import random

# class Dict:
#     dictionary = ["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"]

class game:
    def __init__(self, dict):
        self.dict = dict
    
    def guess_word(self):
        random_word = random.choice(self.dict)
        return random_word


class main:
    game = game(["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"])
    random_word = game.guess_word()
    print(f"{random_word}\n")

    usr_input = input("input a four letter word\n")
    if usr_input == random_word:
        print("you guessed right\n")
    else:
        print("incorrect guess\n")














