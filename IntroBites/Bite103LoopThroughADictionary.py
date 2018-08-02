games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

"""Loop through games_won's dict k, v pairs (items) and
       print how many games each person has won, pluralize
       'game' based on number"""

for name, noOfGames in games_won.items():
    plural = 'game' if noOfGames == 1 else 'games'

    print(f"{name} has won {noOfGames} {plural}")
