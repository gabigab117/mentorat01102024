from collections import defaultdict


# Fonction personnalisée
def default_value():
    return "Valeur par défaut"

perso_defaultdict = defaultdict(default_value)
perso_defaultdict["clé"]
print(perso_defaultdict)

# Avec une lambda
lambda_default_dict = defaultdict(lambda: "Valeur par défaut")
lambda_default_dict["clé1"]
print(lambda_default_dict)
