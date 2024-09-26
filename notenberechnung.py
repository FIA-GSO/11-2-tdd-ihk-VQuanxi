def berechne_prozentwert(erreichte_punkte, gesamt_punkte):
    return round((erreichte_punkte / gesamt_punkte) * 100, 2)

def bestimme_note(prozent):
    if prozent >= 92:
        return "sehr gut"
    elif prozent >= 81:
        return "gut"
    elif prozent >= 67:
        return "befriedigend"
    elif prozent >= 50:
        return "ausreichend"
    else:
        return "ungenügend"

# Hauptprogramm
wahl = input("Wählen Sie 'a' (Prozent berechnen) oder 'b' (Note ermitteln): ")

if wahl == "a":
    erreichte = float(input("Erreichte Punkte: "))
    gesamt = float(input("Gesamtpunkte: "))
    print(f"Prozent: {berechne_prozentwert(erreichte, gesamt)}%")
elif wahl == "b":
    prozent = float(input("Prozentwert: "))
    print(f"Note: {bestimme_note(prozent)}")
else:
    print("Ungültige Auswahl")


def func(testwert):
    if not testwert.isdigit():
        raise ValueError("Ungültiger Wert: Es muss eine Zahl sein.")
    return testwert
