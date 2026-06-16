# Day 3 - Python Basics for Bioinformatics
# Laiba Sultana

name = "Laiba"
age = 25
gpa = 3.8
is_bioinformatician = True

print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Is bioinformatician:", is_bioinformatician)

print("\n--- Data Types ---")
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_bioinformatician))

# LISTS - storing multiple values
print("\n--- Lists ---")
dna_bases = ["A", "T", "G", "C"]
gene_names = ["BRCA1", "BRCA2", "TP53", "EGFR"]
expression_values = [2.5, 1.8, 4.2, 0.9]

print("DNA bases:", dna_bases)
print("Genes:", gene_names)
print("Expression values:", expression_values)
print("First gene:", gene_names[0])
print("Last gene:", gene_names[-1])
print("Number of genes:", len(gene_names))

# LOOPS - doing something to every item
print("\n--- Loops ---")
for gene in gene_names:
    print("Analyzing gene:", gene)

print("\n--- Loop with Expression Values ---")
for i in range(len(gene_names)):
    print(gene_names[i], "→ expression level:", expression_values[i])

# FUNCTIONS - reusable code blocks
print("\n--- Functions ---")

def count_nucleotides(dna_sequence):
    a = dna_sequence.count("A")
    t = dna_sequence.count("T")
    g = dna_sequence.count("G")
    c = dna_sequence.count("C")
    print("Sequence:", dna_sequence)
    print("A:", a, "T:", t, "G:", g, "C:", c)

# Test our function
count_nucleotides("ATGCATGCATGC")
count_nucleotides("BRCA1 sequence: ATGGATTTATCTGCTCTTCGCGTTGAA")
