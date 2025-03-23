"""
Bernat Rubiol

>>> esprimer(4)
False

>>> esprimer(-2)
True

>>> primers(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcmN(42, 60, 70, 63)
1260

>>> mcdN(840, 630, 1050, 1470)
210
"""

def esprimer(num):
    """
    Calcula si num entrant es primer o no
    """
    for test in range(2, num):
        if num%test == 0:
            return False
        
    return True

def primers(num):
    """Retorna una tupla amb tots els nombres primers menors que num."""
    primers_trobats = []
    for n in range(2, num):
        if esprimer(n):
            primers_trobats.append(n)
    return tuple(primers_trobats)

def descompon(num):
    """Retorna una tupla amb la descomposició en factors primers de num."""
    factors = []
    div = 2
    while num > 1:
        while num % div == 0:
            factors.append(div)
            num //= div
        div += 1
    return tuple(factors)

def mcm(num1, num2):
    """Retorna el mínim comú múltiple de dos nombres."""
    factors1 = descompon(num1)
    factors2 = descompon(num2)
    factors_comuns = set(factors1) | set(factors2)
    resultat = 1
    for factor in factors_comuns:
        resultat *= factor ** max(factors1.count(factor), factors2.count(factor))
    return resultat

def mcd(num1, num2):
    """Retorna el màxim comú divisor de dos nombres."""
    factors1 = descompon(num1)
    factors2 = descompon(num2)
    factors_comuns = set(factors1) & set(factors2)
    resultat = 1
    for factor in factors_comuns:
        resultat *= factor ** min(factors1.count(factor), factors2.count(factor))
    return resultat

def mcmN(*numeros):
    """Retorna el mínim comú múltiple d'un nombre arbitrari d'arguments."""
    resultat = numeros[0]
    for num in numeros[1:]:
        resultat = mcm(resultat, num)
    return resultat

def mcdN(*numeros):
    """Retorna el màxim comú divisor d'un nombre arbitrari d'arguments."""
    resultat = numeros[0]
    for num in numeros[1:]:
        resultat = mcd(resultat, num)
    return resultat