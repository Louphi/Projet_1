import math

# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

#Conversion de GPa en N/mm**2

E = E * 10 ** 3

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm
I_rectangulaire = (b * h ** 3) / 12

# poutre carrée

a = 15  # en mm
I_carree = a ** 4 / 12

# poutre ronde
d = 5  # en mm
I_ronde = math.pi * d ** 4 / 64

# poutre creuse
D = 15  # en mm
d = 5  # en mm
I_creuse = (math.pi * (D ** 4 - d ** 4)) / 64

# liste des types et valeurs de I pour chaque type
liste_type_and_I = [
    ("carree", I_carree),
    ("rectangulaire", I_rectangulaire),
    ("creuse", I_creuse),
    ("ronde", I_ronde)
]

# Numero des index pour la liste des types et des valeurs de I
INDEX_TYPE = 0
INDEX_I = 1

# Calcul de la section optimale
liste_delta=[]

for I in liste_type_and_I:
    formule_delta_max = (F * L ** 3) / (3 * E * I[INDEX_I])
    delta_max = round(formule_delta_max,2)
    liste_delta.append(delta_max)

# Trouver la valeur la plus petite de delta_max
delta_optimale = min(liste_delta)

# Trouver type optimal asssocie a la valeur optimale
type_optimal = liste_type_and_I[liste_delta.index(delta_optimale)]

# Afficher la valeur et le type optimaux
print(f'Le type de section minimisant la déformation maximale '
      f'est {type_optimal[INDEX_TYPE]}, avec une déformation de '
      f'{delta_optimale} mm')




