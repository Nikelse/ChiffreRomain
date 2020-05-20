# conversion nombre entier en chiffre romain
# version procedurale (v1.0)
# NF.NSI

limite = 5000

saisie = int(input('Entrez un entier compris entre 1 et '+str(limite)))
while not(saisie >= 1 and saisie <= limite) :
    saisie = int(input('Entrez un entier compris entre 1 et '+str(limite)))

# chaine resultante de concatenation pour la constitution du chiffre romain
s = ""
# nombre entier à convertir pour la décrementation
n = saisie

while n >= 1000:
    s += "M"
    n -= 1000
if n >= 900:
    s += "CM"
    n -= 900
if n >= 500:
    s += "D"
    n -= 500
if n >= 400:
    s += "CD"
    n -= 400

while n >= 100:
    s += "C"
    n -= 100
if n >= 90:
    s += "XC"
    n -= 90
if n >= 50:
    s += "L"
    n -= 50
if n >= 40:
    s += "XL"
    n -= 40

while n >= 10:
    s += "X"
    n -= 10
if n >= 9:
    s += "IX"
    n -= 9
if n >= 5:
    s += "V"
    n -= 5
if n >= 4:
    s += "IV"
    n -= 4

while n >= 1:
    s += "I"
    n -= 1

print("Le nombre entier",saisie, "vaut",s,"en chiffre romain")