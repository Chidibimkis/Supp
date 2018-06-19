import math

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

# Funktion, die die Hamming-Distanz zweier Strings berechnet, welche auch unterschiedliche Länge
# sein können
# Input: 2 Strings
# Output: Integer
def HammDistance(str1, str2):
    # Initialisierung der Countvariablen
    Hdist = 0
    for k,i in zip(str1, str2):
        # Wenn die aktuelle Position nicht übereinstimmt, erhöhe den Count um 1
        if k != i:
            Hdist += 1
    return Hdist

# Funktion, die die Summe aller Hamming-Distanzen von einem festen Pattern zu mehreren Sequenzen
# berechnet
# Input: String (Pattern), Liste von Strings (Sequenzen)
# Output: Integer
def DistanceBetweenPatternAndStrings(pattern, dna):
	k = len(pattern)
	distance = 0
	for t in dna:
        # Hamming-Distanz wird als unendlich initialisiert
		HammingDistance = math.inf
		for kmer in range(len(t) - k + 1):
            # Zwischenvariable der Hamming-Distanz, damit diese nicht doppelt berechnet wird
			ZwHDist = HammDistance(pattern, t[kmer:kmer+k])
            # Wenn die neue Hamming-Distanz kleiner ist als die Alte, so übernehme den kleineren Wert
			if ZwHDist < HammingDistance:
				HammingDistance = ZwHDist
        # Summer aller kleinst möglichen Hamming-Distanzen der unterschiedlichen Sequenzen wird gebildet
		distance += HammingDistance
	return distance

# Funktion, die nach Brute-Force-Methode die Beste Konsensussequenz einer vorgegebenen Länge aus 
# mehreren Sequenzen über die kleinste Hamming-Distanz sucht
# Input: (Liste von) Strings (Sequenzen), Integer (Länge des kmers)
# Output: String
def MedianString(DNA, k):
	distance = math.inf
	# Vergleiche für jedes mögliche kmer die Hamming-Distanz, wenn diese kleiner ist als die aktuelle
	# so übernehme dieses kmer
	for i in range (4**k-1):
		currentpatt = NumberToPattern(i, k)
		ZwHDist = DistanceBetweenPatternAndStrings(currentpatt, DNA)
		if ZwHDist < distance:
			distance = ZwHDist
			Median = currentpatt
	return Median

length = 3
DNAs = ["AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTACGGGACAG"]
lp = 6
seq = ["TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT", "CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA", "TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT", "TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA", "ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG", "TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA", "TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC", "GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA", "CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG", "CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG"]

# Ausgabe der mit Hilfe der Funktion MedianString gefundene Konsussequenz unter Verwendung der 
# erweitertes Sampledatasets der Rosalind-Aufgabe ba2b
print(MedianString(seq, lp))
#print(MedianString(DNAs, length))
