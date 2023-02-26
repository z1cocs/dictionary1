'''HOW TO MAKE A TUPLE'''

#Empty tuple
empty_tuple = ()
print(empty_tuple)

#Tuple with integers
integer_tuple = (1, 2, 3, 4, 5)
print(integer_tuple)

#tuple with mixed datatypes
mixed_tuple = (1, 2, "hello", 3, "goodbye", 4)
print(mixed_tuple)

'''ACCESSING TUPLE ELEMENTS USING INDEXING'''
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",)
print(alphabet[5])
print(alphabet[3])
print(alphabet[0])
print(alphabet[7])


'''ACCESSING TUPLE ELEMENTS USING NEGATIVE INDEXING'''
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",)
print(alphabet[-2])
print(alphabet[-6])
print(alphabet[-3])
print(alphabet[-7])


'''HOW TO PRINT EVERY ITEM OF A TUPLE ON DIFFERENT LINES'''
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",)

for item in alphabet:
    print(item)


'''HOW TO FIND A ITEM IN A TUPLE BASED OFF INPUT FROM A USER'''

#New multiple tuple element
csgo_t_guns = ("ak47", "glock", "mac-10", "ssg 553", "tec-9")

search_for_item = input("Enter a terrorist weapon:")
if search_for_item in csgo_t_guns:
    print("Yep, found it!")
else:
    print("terrorist side weapon not found!")