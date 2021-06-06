#Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
#If you want to know more http://en.wikipedia.org/wiki/DNA
#In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
#More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

#e.g.
#DNA_strand ("ATTGC") # return "TAACG"
#DNA_strand ("GTAT") # return "CATA"

#solution
def DNA_strand(dna):
    #create dictionary with key value pairs
    dna_complements = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    #list comprehension
    #dna_complements[c] for c in dna - pulls complement value for each key
    #"".join - joins complement values together with no spacing
    return "".join(dna_complements[c] for c in dna)
