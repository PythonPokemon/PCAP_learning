"""
PCAP-31-03 – Import basics: import as (Alias)
Lernziel:
- Verstehen, wie 'import modul as alias' funktioniert
"""

# Erklärung:
# Mit 'import modul as alias' wird ein Modul unter einem anderen Namen verfügbar gemacht.
# Das ist nützlich, um lange Modulnamen abzukürzen oder Kollisionen zu vermeiden.

import math as mathematik

# Beispiel:
zahl = 36
wurzel = mathematik.sqrt(zahl)
print(wurzel)  # Erwartet: 6.0

# Mini-Test:
kreiszahl_pi = mathematik.pi
print(kreiszahl_pi)

# Prüfungsfalle:
# ❌ math.sqrt(zahl)        -> falsch, 'math' existiert nicht im Namensraum
# ❌ sqrt(zahl)             -> falsch, keine Direkt-Import
# ✅ mathematik.sqrt(zahl)  -> korrekt
