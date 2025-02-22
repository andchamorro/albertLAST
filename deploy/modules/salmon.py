import os
import json
import pandas as pd
import glob
from collections import defaultdict

def _run_salmon(sample, input_dir, output_dir, index, salmon_path, num_threads, is_gz=False):
    r1 = os.path.join(input_dir, f"{sample}_R1.fq" + (".gz" if is_gz else ""))
    r2 = os.path.join(input_dir, f"{sample}_R2.fq" + (".gz" if is_gz else ""))
    output = os.path.join(output_dir, sample)
    os.makedirs(output, exist_ok=True)
    
    if os.path.exists(r2):
        cmd = f"{salmon_path} quant -q -i {index} -l A -1 {r1} -2 {r2} -o {output} -p {num_threads} 2>/dev/null"
    else:
        cmd = f"{salmon_path} quant -q -i {index} -l A -r {r1} -o {output} -p {num_threads} 2>/dev/null"
    
    os.system(cmd)

def get_abundance(fname, expr_type):
    abundance = defaultdict(float)
    with open(fname, "r") as inp:
        inp.readline()  # Skip header
        for line in inp:
            line = line.strip().split()
            name = line[0]
            abundance[name] += float(line[3]) if expr_type == "TPM" else float(line[-1])
    return abundance

def collect_abundance(samples, output_dir, expr_type, index_label):
    tb = {}
    for sample in samples:
        file = os.path.join(output_dir, sample, "quant.sf")
        tb[sample] = get_abundance(file, expr_type)
    df = pd.DataFrame(tb)
    df.to_csv(os.path.join(output_dir, "expr.csv"), sep=",", index_label=index_label)

def get_mappability(fname):
    with open(fname, "r") as inp:
        data = json.load(inp)
    sid = os.path.basename(os.path.dirname(os.path.dirname(fname)))
    return {
        "id": sid,
        "num_mapped": data["num_mapped"],
        "num_processed": data["num_processed"],
        "percent_mapped": data["percent_mapped"]
    }

def collect_mappability(samples, output_dir):
    tb = []
    for sample in samples:
        file = os.path.join(output_dir, sample, "aux_info/meta_info.json")
        tb.append(get_mappability(file))
    df = pd.DataFrame(tb).set_index("id")
    df.to_csv(os.path.join(output_dir, "mapping_info.csv"), sep=",", index_label="id")

def run(config):
    index = config["index"]
    index_label = config["index_label"]
    input_dir = config["input_path"]
    output_dir = config["output_path"]
    salmon_path = config["salmon"]
    num_threads = str(config["num_threads"])
    samples_fq = [os.path.basename(f).split("_R1.fq")[0] for f in glob.glob(os.path.join(input_dir, "*_R1.fq"))]
    samples_gz = [os.path.basename(f).split("_R1.fq.gz")[0] for f in glob.glob(os.path.join(input_dir, "*_R1.fq.gz"))]
    expr_type = config["exprtype"]

    for sample in samples_fq:
        _run_salmon(sample, input_dir, output_dir, index, salmon_path, num_threads, is_gz=False)
    for sample in samples_gz:
        _run_salmon(sample, input_dir, output_dir, index, salmon_path, num_threads, is_gz=True)

    collect_abundance(samples_fq + samples_gz, output_dir, expr_type, index_label)
    collect_mappability(samples_fq + samples_gz, output_dir)