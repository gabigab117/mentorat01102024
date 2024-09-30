from collections import Counter


# Sous classe de dict
# Compter les objets hashables
# Création à partir d'une liste, d'un dictionnaire, ou de mots clés, de str...

# Un objet hashable est un objet qui a une valeur de hachage qui ne change pas durant sa durée de vie,
# ce qui permet de l'utiliser comme clé dans un dictionnaire ou comme élément dans un ensemble.

# Si un élément est absent retourne 0
# most_common
# update, elements, subtract
# Occurence, comptage, fréquence

# 1 Création d'un Counter
# Depuis une liste
fruits = ['pomme', 'banane', 'pomme', 'cerise', 'banane', 'pomme']
fruit_counter = Counter(fruits)
print(fruit_counter)
print(isinstance(fruit_counter, dict))  # Sous classe de dict :)

# Depuis un dict
mon_dico = {'a': 4, 'c': 0, 'b': 1, 'd': -2}
dict_counter = Counter(mon_dico)
print(dict_counter)
print(dict_counter.most_common())

# A partir de mots-clés
keyword_counter = Counter(chats=4, chiens=2)
print(keyword_counter)

# D'une str
str_counter = Counter("Salut")
print(str_counter)


# 2 Accès/Modifs
print(fruit_counter["pomme"])
fruit_counter["pomme"] = 4
fruit_counter.update(["nashi"])
print(fruit_counter)
print(fruit_counter["figue"])

# 3 Méthodes
print(fruit_counter.most_common())
print(sum(fruit_counter.values()))
print(list(fruit_counter.elements()))  # Elements avec répétitions

# 4 Soustraction
fruit_counter.subtract(["nashi"])
print(fruit_counter)

# 5 Addition intersection union
other_fruits = Counter(["mineolas", "pomme"])
print(fruit_counter + other_fruits)
print(fruit_counter & other_fruits) # Intersection garde les éléments communs avec le minimum de compte
print(fruit_counter | other_fruits) # Union tous les éléments avec le maximum
