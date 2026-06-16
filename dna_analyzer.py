# DNA Sequence Analyzer
# Laiba Sultana - Bioinformatics Portfolio Project

def analyze_dna(sequence):
    sequence = sequence.upper()
    length = len(sequence)
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")
    gc_content = ((g + c) / length) * 100

    print("="*40)
    print("DNA SEQUENCE ANALYSIS REPORT")
    print("="*40)
    print("Sequence:", sequence)
    print("Length:", length, "bp")
    print("A:", a, "| T:", t, "| G:", g, "| C:", c)
    print("GC Content:", round(gc_content, 2), "%")

def get_complement(sequence):
    sequence = sequence.upper()
    complement = ""
    for base in sequence:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
    print("Original:  ", sequence)
    print("Complement:", complement)

def dna_to_rna(sequence):
    sequence = sequence.upper()
    rna = sequence.replace("T", "U")
    print("DNA:", sequence)
    print("RNA:", rna)

# Run analysis
print("\n--- ANALYZING BRCA1 GENE SEQUENCE ---")
analyze_dna("ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTT")

print("\n--- COMPLEMENT STRAND ---")
get_complement("ATGGATTTATCTGCTCTTCG")

print("\n--- DNA TO RNA TRANSCRIPTION ---")
dna_to_rna("ATGGATTTATCTGCTCTTCG")
