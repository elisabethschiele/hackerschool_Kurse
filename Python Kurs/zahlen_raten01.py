LOESUNG = 7

def main():
    # diese Funktion wird aufgerufen wenn der Code ausgeführt wird

    antwort = int(input("Ich habe mir eine Zahl ausgedacht. Es ist eine Zahl zwischen 0 und 10. Kannst du sie erraten? "))
    if LOESUNG == antwort:
        print("Das ist richtig!")

    else:
        differenz = antwort - LOESUNG
        print("Das ist leider falsch. Meine Zahl ist " + str(differenz) + " entfernt von deiner Antwort.")


# Bitte keinen Code unter diesem Kommentar schreiben
if __name__ == '__main__':
    main()