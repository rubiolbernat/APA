class Vector:
    #Atributs de classe
    
    
    #Constructor
    def __init__(self, iterable): #el primer argument es el mateix objecte
        # [expressio for element in iterable if condicio]
        self._vector= [element for element in iterable]
        return None
    
    #Metodes
    def __repr__(self):
        return f"Vector({self._vector})"
    
    def __str__(self):
        cadena="["
        for i in self._vector:
            cadena += f" {i}"
        cadena += "]"
        return cadena
    
    def __getitem__(self, index):
        return self._vector[index]
    
    def __setitem__(self, index, value):
        self._vector[index] = value
        
    def __len__(self):
        return len(self._vector)
    
    def __add__(self, other):
        if isinstance(other,(int, float, complex)):
            return Vector([i + other for i in self._vector]) #Retornem un nou objecte
        else:
            return Vector([num1+ num2 for num1, num2 in zip(self, other)])
        
    __radd__=__add__