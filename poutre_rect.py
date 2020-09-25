# Initialisation des variables

F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm
b = 10  # en mm
h = 20  # en mm

# Conversion de GPa en N/mm**2

E = E * 10 ** 3

# Calcul de l'inertie

I = (b * h ** 3) / 12

# Calcul de la déformation maximale
formule_delta_max = (F * L ** 3) / ( 3 * E * I)
delta_max = round(formule_delta_max,2)

print(f"La déformation maximale de la poutre est {delta_max} mm")