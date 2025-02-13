def addiere(zahl1, zahl2):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return zahl1 + zahl2

def subtrahiere(zahl1, zahl2):
    """Subtrahiert zwei Zahlen und gibt das Ergebnis zurück."""
    return zahl1 - zahl2

def multipliziere(zahl1, zahl2):
    """Multipliziert zwei Zahlen und gibt das Ergebnis zurück."""
    return zahl1 * zahl2

def dividiere(zahl1, zahl2):
    """Dividiert zwei Zahlen und gibt das Ergebnis zurück."""
    if zahl2 == 0:
        return "Division durch Null ist nicht erlaubt."
    return zahl1 / zahl2

def main():
    """Hauptfunktion des Programms."""
    print("Willkommen zum erweiterten Taschenrechner!")

    while True:
        try:
            num1 = float(input("Gib die erste Zahl ein: "))
            num2 = float(input("Gib die zweite Zahl ein: "))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib Zahlen ein.")
            continue

        print("\nBitte wähle eine Operation:")
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")
        print("5. Beenden")

        wahl = input("Deine Wahl: ")

        if wahl == '1':
            ergebnis = addiere(num1, num2)
        elif wahl == '2':
            ergebnis = subtrahiere(num1, num2)
        elif wahl == '3':
            ergebnis = multipliziere(num1, num2)
        elif wahl == '4':
            ergebnis = dividiere(num1, num2)
        elif wahl == '5':
            break
        else:
            print("Ungültige Wahl. Bitte wähle eine der Optionen 1-5.")
            continue

        print(f"Das Ergebnis ist: {ergebnis}")

if __name__ == "__main__":
    main()
