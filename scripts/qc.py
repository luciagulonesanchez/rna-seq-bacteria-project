##Simulación de control de calidad
RAW = "../data/raw_fastq"
OUT = "../results/qc"

os.makedirs(OUT, exist_ok=True)

def simulate_fastqc(file):
    print(f"[QC] Analizando {file} ...")
    report = os.path.join(OUT, os.path.basename(file).replace(".fastq.gz", "_qc.txt"))
    with open(report, "w") as f:
        f.write("Simulated FastQC report\n")
    print(f"[QC] Reporte generado: {report}")

for file in os.listdir(RAW):
    if file.endswith(".fastq.gz"):
        simulate_fastqc(os.path.join(RAW, file))
