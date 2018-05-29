# Funktion, welche eine DNA-Sequenz in eine Zahl im 4er System umwandelt
# Input: Sequenz, String
# Output: Integer

def patternToNumber(text):
	if len(text) == 0:
		return 0
	return 4 * patternToNumber(text[:-1]) + symbolToNumber(text[-1:])

# Funktion, welche ein Nukleosid in eine Zahl im 4er-System umwandelt
# Input: Base (String)
# Output: Integer
def symbolToNumber(base):
	if base == "A":
		return 0
	if base == "C":
		return 1
	if base == "G":
		return 2
	if base == "T":
		return 3

#Testlauf mit Rosalind sample Dataset "AGT" als Eingabe --> 11 als Output
print(patternToNumber("AGT"))