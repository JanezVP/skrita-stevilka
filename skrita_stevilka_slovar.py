from random import randint

def preveri(stevilka, ugibano, cifra):
    pravi_odgovor = cifra [stevilka]

    if pravi_odgovor == ugibano:
        print ("Bravo!!!")
        return True
    else:
        print ("Narobe.")
        return False

def main():
    cifra = {"A: ": "1", "B: ": "2", "C: ": "3", "D: ": "4", "E: ": "5"}

    zadnji_odgovor = True

    while True:
        if zadnji_odgovor:
            st_stevilka = randint(0, len(cifra)-1)
        stevilka = cifra.keys()[st_stevilka]
        ugibano = raw_input("Vpisite stevilko med 1 in 5. " + stevilka )
        ugibano = ugibano.lower()
        zadnji_odgovor = preveri(stevilka, ugibano, cifra)

        if zadnji_odgovor:
            del cifra[stevilka]

        odgovor= raw_input("Ali zelis poskusiti znova (da/ne): ")
        if odgovor == "ne":
            print "Hvala"
            break
        if odgovor != "da":
            continue


if __name__ == "__main__":
    main()




