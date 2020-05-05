import random

ZIEL = 3                                    # Anzah korrekter Rechenaufgaben

def main():
    """

    """
    streak = 0
    while streak < ZIEL:

        var1 = random.randint(10,99)        # Erster Summand
        var2 = random.randint(10,99)        # Zweiter Summand

        print("Was ist " + str(var1) + " + " + str(var2) + "?")
        user_loesung = int(input("Antwort: "))

        echte_loesung = var1 + var2           # die Aufgabe lösen

        if echte_loesung == user_loesung:
            streak = streak + 1
            print("Richtig! du hast schon " + str(streak) + " Aufgabe(n) richtig hintereinander gelöst.")
        else:
            streak = 0
            print("Leider falsch. Die richtige Antwort ist " + str(real_result))

    print("Herzlichen Glückwunsch!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()