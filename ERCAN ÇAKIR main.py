# Initialer Kontostand
kontostand = 1000

# Benutzer fragen, was sie tun möchten
transaktion = input("Möchten Sie eine Einzahlung oder eine Auszahlung tätigen? ")

if transaktion == "Einzahlung":
    # Betrag für Einzahlung eingeben
    betrag = int(input("Wie viel möchten Sie einzahlen? "))
    kontostand += betrag
elif transaktion == "Auszahlung":
    # Betrag für Auszahlung eingeben
    betrag = int(input("Wie viel möchten Sie abheben? "))
    kontostand -= betrag
else:
    # Ungültige Transaktion
    print("Ungültige Transaktion")

# Überprüfen, ob der Kontostand negativ ist
if kontostand < 0:
    print("Sie können keinen negativen Kontostand haben!")
else:
    print("Ihr endgültiger Kontostand ist kontostand EURO.")
