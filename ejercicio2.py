import regex

class MyArray:
    isArithmetic = False

    def __init__(self, testString):
        self.testString = testString

    def operation(self):
        x = regex.match(r'([0-9 \( \s]*+[\/\+\-\*])+([-+]?[0-9 \) \s]*)', self.testString)
        l_paren = regex.findall('\(', self.testString)
        r_paren = regex.findall('\)', self.testString)

        if x != None:
            if (len(l_paren) == len(r_paren)):
                self.isArithmetic = True
            else:
                self.isArithmetic = False
        return self.isArithmetic

    def compute(self):
        if self.isArithmetic:
            op = eval(self.testString)
            return int(op)
        else:
            return False
            
#Casos de prueba
a = "Hello world" 
b = "2 + 10 / 2 - 20" 
c = "(2 + 10) / 2 - 20" 
d = "(2 + 10 / 2 - 20"

#a
ejemplo = MyArray(a)
print(a)
print(ejemplo.operation())
print(ejemplo.compute())
print('\n')

#b
ejemplo = MyArray(b)
print(b)
print(ejemplo.operation())
print(ejemplo.compute())
print('\n')

#c
ejemplo = MyArray(c)
print(c)
print(ejemplo.operation())
print(ejemplo.compute())
print('\n')

#d
ejemplo = MyArray(d)
print(d)
print(ejemplo.operation())
print(ejemplo.compute())

