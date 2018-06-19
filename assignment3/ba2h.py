import math

#Inputs der Rosalindplattform für die Aufgabe ba2h
pattern = "AAA"
DNAs = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]
pp= "AATTGGG"
dna = ["TCTGCAGAGCGCAAGCGTCTCAATGTTTTTCGCTGCAAGTGTTAGCTGCGTTTGTCGACACACAAATGAAGTGACCACATCAAACCTAATTATG","TCCCGCTCGAGGACAGACACCGGTGCAGCCGAGGGTATTATAGTCTGCTCGTATGGTTTGTATGGAGGATAATAGATGGGGTGACGAAATGAGA","CCTCCCTGCCAGGTTGGTGAATTTAAGCATAAAGACCTGGAGGACTGACGGGTCTGGTCGACCACCATTCGTCGGTTCTCGAGCGCTGTTTCTA","GATACAGGTCGCTTGAAATGTCCCTGAGACGTCCGGGCCAAGAGCGAAACAAATCTCAGTCCTGGGTGGCGGCAGCGAAGGGATTAGATTACTT","ATGGAACCGTGTCACGGCAGTCTACCTTTTACCCAGAGCTGTATATGACGGTTAGTCCCCGAGGCCATCTCGCACCCTACTGAGCACAAATATA","AATCCCTGCAGGTCAGGCTGTTCTGAAAGAACCCTGCAGGCTGGTGCTATTCCTTAAGACGCCGAGGTTCAGATACTCTCAGCCAGAGAGCAGA","CCTATTAACTTCTCTCTAGATCGTAAACGACTATGGACTTACACGTCCCGCTTTCTTGTCTTGGGTGCCGTCACACTAGCCCACTACAGTCGGG","GGCGCACCTTCGATATTAATGCGAGTCAATTGCCGTTTAAGTCCGCGCGTAGCGGATGCACGTAGGGACTTTAAAGCCCCATGCCAACTGTATA"]

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

print(DistanceBetweenPatternAndStrings(pattern, DNAs))
#print(DistanceBetweenPatternAndStrings(pp, dna))
