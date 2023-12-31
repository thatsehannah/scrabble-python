letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# BUILDING POINT DICTIONARY
letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

# SCORING A WORD
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

brownie_points = score_word("BROWNIE")
# print(brownie_points)

# SCORING A GAME
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

def update_point_totals(game_dict):
  player_to_points = {}

  for player, words in game_dict.items():
    player_points = 0

    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

  return player_to_points

# print(update_point_totals(player_to_words))

# ADDING A WORD TO A PLAYER'S LIST
def play_word(player, word):
    if player in player_to_words.keys():
        player_to_words[player].append(word)

play_word("player1", "BOSS")
print("WORDS:")
print(player_to_words)
print()
print("SCORE:")
print(update_point_totals(player_to_words))
