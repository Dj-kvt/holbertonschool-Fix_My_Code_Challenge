#!/usr/bin/python3
""" FizzBuzz corrigé
"""
import sys


def fizzbuzz(n):
    """
    La fonction FizzBuzz affiche les nombres de 1 à n séparés par un espace.

    - Pour les multiples de 3, afficher "Fizz".
    - Pour les multiples de 5, afficher "Buzz".
    - Pour les multiples de 3 et 5, afficher "FizzBuzz".
    """
    if n < 1:
        return

    resultat = []
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            resultat.append("FizzBuzz")
        elif (i % 3 == 0):
            resultat.append("Fizz")
        elif (i % 5 == 0):
            resultat.append("Buzz")
        else:
            resultat.append(str(i))
    print(" ".join(resultat))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Nombre manquant")
        print("Utilisation: ./0-fizzbuzz.py <nombre>")
        print("Exemple: ./0-fizzbuzz.py 89")
        sys.exit(1)

    nombre = int(sys.argv[1])
    fizzbuzz(nombre)
