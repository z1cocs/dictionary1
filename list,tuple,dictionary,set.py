'''HOW TO MAKE A BASIC LIST'''

#Making a python list with 5 integers
numbers = [1, 2, 3, 4, 5]

#printing all numbers in the list
print(numbers)


'''#HOW TO ACCESS ELEMENTS IN A LIST, 
NOTE INDEXING STARTS FROM 0'''

#New list of computer games
computer_games = ["csgo", "valorant", "forza"]

#how to access "csgo" on the list
print(computer_games[0])

#How to access "forza" on the lost
print(computer_games[2])


'''NEGATIVE INDEXING'''

#New csgo gun list
types_of_csgo_guns = ["p250", "AWP", "m4a4", "glock-18", "negev" ]

#how to acess an item on a list with negative indexing
print(types_of_csgo_guns[-3])
print(types_of_csgo_guns[-5])


'''HOW TO FIND A ITEM IN A LIST BASED OFF INPUT FROM USER'''

csgo_rifles_list = ["AUG", "Famas", "m4a4", "SSG 08", "AWP", "SCAR-20" ]
user_input = input("\nEnter a rifle to search for:")

for item in csgo_rifles_list:
    if item == user_input:
        print("Rifle found!")
        break
else:
    print("Rifle not found.")