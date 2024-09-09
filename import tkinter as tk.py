import math

# Valores proporcionados
NA = 1170.503
EA = 1309.652
NB = 1078.806
EB = 1395.454
AlP = 122.36194444
BET = 29.58055556

# Convertir grados a radianes
AlP_rad = math.radians(AlP)
BET_rad = math.radians(BET)

# Calcular las cotangentes
cot_alpha = 1 / math.tan(AlP_rad)
cot_beta = 1 / math.tan(BET_rad)

# Imprimir cotangentes para verificar
print(f"cot_alpha: {cot_alpha}")
print(f"cot_beta: {cot_beta}")

# Calcular el numerador y denominador para NP
numerador = (EA - EB) + (NA * cot_beta) + (NB * cot_alpha)
denominador = cot_alpha + cot_beta

# Imprimir numerador y denominador para verificar
print(f"Numerador para NP: {numerador}")
print(f"Denominador para NP: {denominador}")

NP = numerador / denominador
print(f"El valor de la norte del punto P es: {NP}")

# Calcular el numerador y denominador para EP
numerador2 = (NB - NA) + (EA * cot_beta) + (EB * cot_alpha)
denominador2 = cot_alpha + cot_beta

# Imprimir numerador y denominador para verificar
print(f"Numerador para EP: {numerador2}")
print(f"Denominador para EP: {denominador2}")

EP = numerador2 / denominador2
print(f"El valor del este del punto P es: {EP}")
