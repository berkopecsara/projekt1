# -*- encoding: utf-8 -*-

import random

def main():
    skrito_stevilo = random.randint(5, 20)
    ugibano_stevilo = int(raw_input("Ugibaj skrito stevilo od 5 do 20: "))

    while ugibano_stevilo != skrito_stevilo:
        ugibano_stevilo = raw_input("Ups! Poskusite se enkrat: ")
    else:
        print "Bravo! Uspelo ti je."


if __name__ == "__main__":
    main()

