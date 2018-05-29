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

# Testdaten aus Rosalind
sequenz = "ACGCGGCTCTGAAA"
k = 2

# Funktion, welche das Frequency-Arrays mit der Sequenz und k anlegt
# Input: String, Int
# Output: Array
def FrequencyArray(text, k):
    a = [0] * 4**k
    for i in range(len(text)-k+1):
	    pattern = text[i:i+k]
	    j = patternToNumber(pattern)
	    a[j] = a[j] + 1

    fArray = ""
    for i in a:
	    fArray += str(i) + " "
    return fArray

print(FrequencyArray(sequenz, k))