class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0
    
# Primeiro game
game1 = Game()
game1.name = "Destiny 2"
game1.yearLaunch = 2018
game1.multiplayer = True
game1.note = 8.5

print("---Dados Do Jogo---")
print(f"Nome do jogo: {game1.name}\n Ano de lancamento: {game1.yearLaunch}\n ON-line: {game1.multiplayer}\n nota: {game1.note}")


# Segundo Jogo

game2 = Game()
game2.name = "God Of War"
game2.yearLaunch = 2005
game2.multiplayer = False
game2.note = 9.3

print("---Dados Do Jogo---")
print(f"Nome do jogo: {game2.name}\n Ano de lancamento: {game2.yearLaunch}\n ON-line: {game2.multiplayer}\n nota: {game2.note}")


