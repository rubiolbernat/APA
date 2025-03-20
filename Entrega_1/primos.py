"""
Bernat Rubiol

>>>esprimer(4)
False

>>>esprimer(-2)
True
"""

def esprimer(num):
    """
    Calcula si num entrant es primer o no
    """
    for test in range(2, num):
        if num%test == 0:
            return False
        
    return True
