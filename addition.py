# addition.py
def addiere(zahl1, zahl2):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return zahl1 + zahl2

if __name__ == "__main__":
    num1 = float(input("Gib die erste Zahl ein: "))
    num2 = float(input("Gib die zweite Zahl ein: "))
    
    ergebnis = addiere(num1, num2)
    print(f"Das Ergebnis der Addition von {num1} und {num2} ist {ergebnis}.")
