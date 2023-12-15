#Funkcije
def zbroji(a,b):
    rezultat = a + b
    print(rezultat)

def oduzmi(a,b):
    rezultat = a - b
    print(rezultat)

def mnozi(a,b):
    rezultat = a * b
    print(rezultat)

def dijeli(a,b):
    rezultat = a / b
    print(rezultat)

#Unos
a = int(input("Unesi broj a: "))
b = int(input("Unesi broj b: "))
o = input("Odaberi matematičku operaciju +, -, *, /: ")

#Odabir
if o == "+":
    zbroji(a, b)
elif o == "-":
    oduzmi(a,b)
elif o == "*":
    mnozi(a,b)
else: dijeli(a,b)