import primos as pr

pr.esprimer(3)

pr.__annotations__

result = pr.esprimer(3)
print("es primer" if result else "No es primer")

for i in range(1, 100):
    print(f"{i}: ", pr.esprimer(i))
    
# Obtenir tots els nombres primers fins a un cert valor
print("Primers fins a 50:", pr.primers(50))

# Descomposició en factors primers
num = 36 * 175 * 143
print(f"Descomposició en factors primers de {num}: {pr.descompon(num)}")

# Càlcul del mínim comú múltiple i màxim comú divisor per dos nombres
print("MCM de 90 i 14:", pr.mcm(90, 14))
print("MCD de 924 i 780:", pr.mcd(924, 780))

# Càlcul del mínim comú múltiple i màxim comú divisor per múltiples nombres
print("MCM de 42, 60, 70, 63:", pr.mcmN(42, 60, 70, 63))
print("MCD de 840, 630, 1050, 1470:", pr.mcdN(840, 630, 1050, 1470))

# Consultar la documentació del mòdul
print(pr.__doc__)
help(pr)
