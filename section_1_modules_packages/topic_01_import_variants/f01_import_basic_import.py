"""
PCAP-31-03 – Import basics: import module
Lernziel:
- Verstehen, was 'import modulename' macht
"""

# Erklärung:
# Mit 'import modulename' wird das komplette Modul geladen.
# Auf Inhalte greift man über 'modulename.element' zu.

import math

# Beispiel:
zahl = 16
wurzel = math.sqrt(zahl)
print(wurzel)  # Erwartet: 4.0

# Mini-Test:
kreiszahl_pi = math.pi
print(kreiszahl_pi)

# Prüfungsfalle:
# ❌ sqrt(zahl) → falsch
# ✅ math.sqrt(zahl) → korrekt