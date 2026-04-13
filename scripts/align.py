##Simulación de alineamiento
import os

RAW = "../data/raw_fastq"
OUT = "../results/bam"

os.makedirs(OUT, exist_ok=True)

def simulate_alignment(sample):
    print(f"[ALIGN] Alineando {sample} ...")
    bam = os.path.join(OUT, sample + ".bam")
    with open(bam, "w") as f:
        f.write("Simulated BAM alignment\n")
    print(f"[ALIGN] Archivo BAM generado: {bam}")

samples = set([f.split("_R")[0] for f in os.listdir(RAW) if f.endswith(".fastq.gz")])

for s in samples:
    simulate_alignment(s)
