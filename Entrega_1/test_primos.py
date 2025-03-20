import primos as pr

pr.esprimer(3)

pr.__annotations__

result = pr.esprimer(3)
print("es primer" if result else "No es primer")

for i in range(1, 100):
    print(f"{i}: ", pr.esprimer(i))
    
pr.__doc__
print(pr.__doc__)
help(pr)
