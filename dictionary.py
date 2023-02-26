'''CREATING A DICTIONARY'''

players_from_each_sport = {"Football": "Messi", "Basketball": "LeBron James", "Golf": "Tiger Woods"}
print(players_from_each_sport)


'''ACCESSING ELEMENTS FROM DICTIONARY'''

players_from_each_sport = {"Football": "Messi", "Basketball": "LeBron James", "Golf": "Tiger Woods"}

print(players_from_each_sport["Football"])
print(players_from_each_sport["Golf"])


'''FINDING ITEMS IN A DICTIONARY BASED OF USER INPUT'''

players_from_each_sport = {"Football": "Messi", "Basketball": "LeBron James", "Golf": "Tiger Woods"}
search = input("What sport do you want me to find a player from:")

if search in players_from_each_sport:
    print("Aha, a player from the sport", search, "is", players_from_each_sport[search])
else:
    print("Your chosen sport is not in my dictionary")
