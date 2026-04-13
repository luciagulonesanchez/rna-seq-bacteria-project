##Simulación de cuantificación
import os
import random

OUT = "../results/counts"
os.makedirs(OUT, exist_ok=True)

genes = [f"gene_{i}" for i in range(1, 101)]
samples = ["control1", "control2", "control3", "vanco1", "vanco2", "vanco3"]

with open(os.path.join(OUT, "gene_counts.txt"), "w") as f:
    f.write("gene\t" + "\t".join(samples) + "\n")
    for g in genes:
        counts = [str(random.randint(50, 5000)) for _ in samples]
        f.write(g + "\t" + "\t".join(counts) + "\n")

print("[COUNTS] Archivo de conteos generado.")
