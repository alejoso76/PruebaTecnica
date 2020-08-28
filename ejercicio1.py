import numpy as np
import regex

class MyMatrix:
    count = 0
    dimension = 0
    def __init__(self, matrix):
        self.matrix = matrix

    def dimension(self, prof=0):
        strMatrix = str(self.matrix)
        strMatrix = strMatrix.replace('list(', '')
        strMatrix = strMatrix.replace(')', ',')
        dim = 0
        for c in strMatrix:
            if c == '[':
                dim += 1
            else:
                break
        self.dimension = dim
        return dim 
        
    def straight(self):
        if(regex.findall('list', str(self.matrix))):
            return False
        elif self.dimension == 1:
            return True
        elif self.matrix.shape:
            return True
        
    def compute(self):
        strMatrix = str(self.matrix)
        numbers = regex.findall('[0-9]+', strMatrix)
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        return(sum(numbers))

#Casos de prueba
a = np.array([1,2])

b = np.array([[1,2], [2,4]])

c = np.array([[1,2], [2,4], [2,4]])

d = np.array([[[3,4], [6,5]]])
    
#No es una matriz válida, por lo tanto no se puede tratar como una
e = np.array([[[1, 2, 3]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]])

#La suma correcta de este array es 74, no 66
f = np.array([[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]])

print('Matriz a')
ejemplo = MyMatrix(a)
print(ejemplo.dimension())
print(ejemplo.straight())
print(ejemplo.compute())
print('\n')

print('Matriz b')
ejemplo = MyMatrix(b)
print(ejemplo.dimension())
print(ejemplo.straight())
print(ejemplo.compute())
print('\n')

print('Matriz c')
ejemplo = MyMatrix(c)
print(ejemplo.dimension())
print(ejemplo.straight())
print(ejemplo.compute())
print('\n')

print('Matriz d')
ejemplo = MyMatrix(d)
print(ejemplo.dimension())
print(ejemplo.straight())
print(ejemplo.compute())
print('\n')

print('Matriz e')
ejemplo = MyMatrix(e)
print(ejemplo.dimension())
print(ejemplo.straight())
print(ejemplo.compute())
print('\n')

print('Matriz f')
ejemplo = MyMatrix(f)
print(ejemplo.dimension())
print(ejemplo.straight())
print(ejemplo.compute())
print('\n')