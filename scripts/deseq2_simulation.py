##Simulación de análisis diferencial
import pandas as pd
import numpy as np

counts = pd.read_csv("../results/counts/gene_counts.txt", sep="\t")

# Simulación de log2FC y p-values
np.random.seed(42)
counts["log2FC"] = np.random.normal(0, 2, len(counts))
counts["pvalue"] = np.random.uniform(0, 1, len(counts))

counts.to_csv("../results/deseq2/deseq2_results.csv", index=False)

print("[DESEQ2] Resultados simulados generados.")
