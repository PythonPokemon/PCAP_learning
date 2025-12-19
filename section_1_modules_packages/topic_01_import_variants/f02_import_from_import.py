"""
PCAP-31-03 – Import basics: from modul import name
Lernziel:
- Verstehen, wie 'from modul import name' funktioniert
- Unterschied zu 'import modul' erkennen
"""

# Erklärung:
# Mit 'from modul import name' wird NUR ein bestimmtes Element importiert.
# Dieses Element kann danach DIREKT verwendet werden – ohne Modulpräfix.

from math import sqrt

# Beispiel:
zahl = 25
wurzel = sqrt(zahl)
print(wurzel)  # Erwartet: 5.0

# Mini-Test:
andere_zahl = 9
andere_wurzel = sqrt(andere_zahl)
print(andere_wurzel)  # Erwartet: 3.0

# Prüfungsfalle (sehr wichtig für PCAP):
# ❌ math.sqrt(zahl)  -> falsch, 'math' wurde NICHT importiert
# ✅ sqrt(zahl)       -> korrekt

# Merksatz:
# 'from modul import name' importiert NUR 'name', nicht das ganze Modul.
