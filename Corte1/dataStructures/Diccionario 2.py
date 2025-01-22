sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22 }
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print (sensors)
print (num_cameras)
translations = {"mountain": "orod", "bread": "bass","friend" : "mellon", "horse": "roch"}
print (translations)

#Verificando un error:
powers={[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
print (powers)

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"],"Corleone": ["Sonny", "Fredo", "Michael"]}
print (children)

my_empty_dictionary = {}
print (my_empty_dictionary)

menu= {"oatmeal":3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print ("Before: ", menu)
menu["cheesecake"] = 8
print ("After: ", menu)

animals_in_zoo= {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
print (animals_in_zoo)

#Agregando varias claves
sensors = {"living room": 21, "kitchen":23, "bedroom":20}
print("Before: ", sensors)
#Si queremos agregar 3 nuevos cuartos, podemos usar:
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After: ", sensors)
## Sobre escribir valores ##
# Nosotros sabemos que podemos agregar valores usando el siguiente sintaxis:
menu["banana"] = 3
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["oatmeal"] = 5
print("After: ", menu)
# Nota que el valor de "oatmeal" ha sido cambiado a 5.
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before ", oscar_winners)
print()
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1 ", oscar_winners)
print()
oscar_winners["Best Picture"] = "Moonlight"
print("After2 ", oscar_winners)

##Comprencion del diccionario##
# Vamos a decir que nosotros tenemos dos listas que queremos conbinar dentro del diccionario
# como una lista de estudiantes con la lista de sus alturas en pulgadas:
names = {'Jenny', 'Alexus', 'Sam', 'Grace'}
heights = [61, 70, 67, 64]
#Python te permite crear un diccionario usando
# un diccionario de comprensión, con esta sintaxis:
zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)

students = {key:value for key, value in zip(names, heights)}
# students ahora es {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
print("students: ", students)
## zip() Combina dos listas un iterador de tuplas con los elementos de la lista emparejados. Este dictado de comprensión:
drinks = {"espresso", "chai", "decaf", "drip"}
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)