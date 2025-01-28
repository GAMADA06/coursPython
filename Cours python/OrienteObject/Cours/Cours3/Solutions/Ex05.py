class Game:
    def __init__(self):
        self.state = {"scores": {}, "level": 1}

    def save_state(self, filename: str):
        with open(filename, "w") as file:
            file.write(str(self.state))

    def load_state(self, filename: str):
        with open(filename, "r") as file:
            self.state = eval(file.read())

    def update_score(self, player: str, score: int):
        if player in self.state["scores"]:
            self.state["scores"][player] += score
        else:
            self.state["scores"][player] = score


# Exemple d'utilisation
game = Game()
game.update_score("Alice", 10)
game.update_score("Bob", 20)

print("État initial :", game.state)

# Sauvegarde de l'état du jeu
game.save_state("game_save.txt")

# Chargement d'un état sauvegardé
new_game = Game()
new_game.load_state("game_save.txt")
print("État chargé :", new_game.state)
