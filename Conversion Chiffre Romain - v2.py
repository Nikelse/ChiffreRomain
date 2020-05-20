# conversion nombre entier en chiffre romain
# version tableau (v2.0)
# NF.NSI

# tableau de conversion
chiffres = {
    1    : "I", 2   : "II", 3   : "III", 4   : "IV", 5   : "V", 6   : "VI", 7   : "VII", 8   : "VIII", 9    : "IX",
    10   : "X", 20  : "XX", 30  : "XXX", 40  : "XL", 50  : "L", 60  : "LX", 70  : "LXX", 80  : "LXXX", 90   : "XC",
    100  : "C", 200 : "CC", 300 : "CCC", 400 : "CD", 500 : "D", 600 : "DC", 700 : "DCC", 800 : "DCCC", 900  : "CM",
    1000 : "M"
}

# limite de saisie
limite = 5000

# debut du programme
# ------------------------------------------------------------------------
saisie = int(input('Entrez un entier compris entre 1 et '+str(limite)))
while not(saisie >= 1 and saisie <= limite) :
    saisie = int(input('Entrez un entier compris entre 1 et '+str(limite)))

# tri des clefs du dictionnaire en ordre décroissant sur l'index
chiffres = sorted(chiffres.items(), key=lambda t: t[0], reverse=True)

s = ""
n = saisie

while (n > 0) :
    for nombre, romain in chiffres :
        # N est plus grand que la position de la clef dans le tableau
        if n >= nombre :
            # decrementation du nombre
            n -= nombre
            # concatenation du chiffre romain
            s += romain
            # reset du compteur dans la boucle
            break

print("Le nombre entier",saisie, "vaut",s,"en chiffre romain (v2)")