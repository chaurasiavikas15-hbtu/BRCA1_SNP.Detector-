import csv

def read_fasta(filename):
    sequence = ""
    with open(filename, "r") as file:
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip().upper()
    return sequence

print("Reading files...")
normal_seq = read_fasta("normal_big.fasta")
mutant_seq = read_fasta("mutant_big.fasta")

print(f"Normal Length: {len(normal_seq)}")
print(f"Mutant Length: {len(mutant_seq)}")

mutations = []
for i, (n, m) in enumerate(zip(normal_seq, mutant_seq)):
    if n != m:
        mutations.append([i+1, n, m])

with open("SNP_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Position", "Normal_Base", "Mutant_Base"])
    writer.writerows(mutations)

print(f"\nDone! Found {len(mutations)} SNPs")
print("Report saved as: SNP_report.csv")
