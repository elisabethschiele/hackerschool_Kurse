
import random

LOESUNG = random.rantint(1, 10)

def main():
    # diese Funktion wird aufgerufen wenn der Code ausgeführt wird

    antwort = int(input("Ich habe mir eine Zahl ausgedacht. Es ist eine Zahl zwischen 0 und 10. Kannst du sie erraten? "))

    while LOESUNG != antwort:
        if LOESUNG < antwort:
            print("Das ist leider falsch. Meine Zahl ist kleiner als das.")
        else:
            print("Das ist leider falsch. Meine Zahl ist größer als das.")
        antwort = int(input("Versuch es nochmal "))

    print("Das ist richtig!")

# Bitte keinen Code unter diesem Kommentar schreiben
if __name__ == '__main__':
    main()