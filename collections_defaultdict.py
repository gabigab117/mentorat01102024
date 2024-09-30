from collections import defaultdict


# Sous classe de dict
# Valeur par défaut pour les clés inexistantes

# Spécifier une fonction ou type qui sera appelé pour la valeur par défaut (int, list, str, fonction perso)


# 1 basique int
int_dict = defaultdict(int)  # 0
print(int_dict)
words = ["pomme", "banane", "pomme"]
for word in words:
    int_dict[word] += 1

print(int_dict)
print(int_dict["cerise"])
print(int_dict)

# 2 basique list
list_dict = defaultdict(list)
list_dict["clé"] = [1, 2]
list_dict["autre_clé"]
print(list_dict)
