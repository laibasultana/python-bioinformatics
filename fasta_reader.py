# FASTA File Reader and Analyzer
# Laiba Sultana - Bioinformatics Portfolio Project

def read_fasta(filename):
    sequences = {}
    current_id = ""
    
    file = open(filename, "r")
    
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            sequences[current_id] = ""
        else:
            sequences[current_id] += line
    
    file.close()
    return sequences

# Read our FASTA file
all_sequences = read_fasta("sample_genes.fasta")

print("="*50)
print("FASTA FILE LOADED SUCCESSFULLY")
print("="*50)
print("Total sequences found:", len(all_sequences))
print()

for seq_id, sequence in all_sequences.items():
    print("Gene ID:", seq_id)
    print("Sequence:", sequence)
    print("Length:", len(sequence), "bp")
    print("-"*50)

# Calculate GC content for every sequence
print()
print("="*50)
print("GC CONTENT ANALYSIS - ALL GENES")
print("="*50)

for seq_id, sequence in all_sequences.items():
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    total = len(sequence)
    gc_content = ((g_count + c_count) / total) * 100
    
    print(seq_id, "→ GC Content:", round(gc_content, 2), "%")
