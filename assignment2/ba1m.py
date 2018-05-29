# Funktion, welche eine Zahl index des 4er Systems in eine DNA-Sequenz bestimmter 
# Länge k umwandelt
# Input: Integer, Länge des Patterns
# Output: String

def NumberToPattern (index, k):
    if k == 1:
        return NumberToSymbol(index)
    return NumberToPattern(index // 4, k-1) + NumberToSymbol(index % 4)

# Funktion, welche eine Zahl im 4er-System in ein Nukleosid umwandelt
# Input: Integer
# Output: Base (String)
def NumberToSymbol(zahl):
    if zahl == 0:
        return "A"
    if zahl == 1:
        return "C"
    if zahl == 2:
        return "G"
    if zahl == 3:
        return "T"

#Testlauf mit Rosalind sample Dataset "45,4" als Eingabe --> AGTC als Output
print(NumberToPattern(45,4))