a = int(input("Unesi broj a: "))
b = int(input("Unesi broj b: "))
operacija = input("Odaberite željenu mat. operaciju: ")

zbroj = a + b
oduzimanje = a - b
množenje = a * b
dijeljenje = a/b

if operacija(zbroj):
    print("Zbroj brojeva {0} i {1} iznosi {2}".format(a, b, zbroj))
elif operacija(oduzimanje):
    print("Oduzimanje brojeva {0} i {1} iznosi {2}".format(a, b, oduzimanje))
elif operacija:
    print("Množenje brojeva {0} i {1} iznosi {2}".format(a, b, množenje))
else:
    print("Dijeljenje brojeva {0} i {1} iznosi {2}".format(a, b, dijeljenje))


