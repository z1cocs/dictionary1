
'''CREATING SETS IN PYTHON'''

# creating a set with integers only
weapon_price = {112, 114, 116, 118, 115}
print('weapon price:', weapon_price)

# creating a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# creating a set of mixed data types
mixed_values = {'AWP', 1500, -300, 'Knife'}
print('Set of mixed data types:', mixed_values)


'''ADDING ITEMS TO A SET'''

weapon_values = {'300', '50', '500', '1500', '0'}

print('Initial Set:',weapon_values)

#Adding another value with .add
weapon_values.add(150)

print('Updated Set:', weapon_values)