"""an agent, 13 Nov 2026: literature decisions on DL candidates C01-C18 (queries q_cand1113.txt, hits cand1113a/b.out,
abstracts abs_check_1113.xml) and the mapping of the kept ones onto the borderline rows marked REPLACE."""
import csv, io
DEC = {
 "C01": ("KEEP", "2610.23007 (two-neuron ReLU, 1D data) is a minimal case; two-layer networks in general open"),
 "C02": ("DROP", "answered: Markdahl et al. 2018 (d>=3, connected graph, increasing convex phi synchronizes) covers phi=e^{beta t} for every beta; see Criscitiello-Rebjock-McRae-Boumal 2405.18273"),
 "C03": ("KEEP", "Abbe-Boix-Adsera-Misiakiewicz 2302.11055 prove it for layerwise training; jointly trained open"),
 "C04": ("KEEP", "2610.28800 separates depth 2 from 3 under Gaussian measure; 3 vs 4 open"),
 "C05": ("KEEP", "2609.26679 (homogeneous nets, squared loss) and 2610.22593 are partial; the modular-addition statement with Fourier features open"),
 "C06": ("KEEP", "no hit in the query; NTK-width results only"),
 "C07": ("KEEP", "results need near-orthogonal or moderate-dimension data (2403.06903, 2505.16204)"),
 "C08": ("DROP", "answered in the stochastic setting: Reddi-Kale-Kumar 1904.09237 Thm 3 gives divergence for every fixed beta1<sqrt(beta2)"),
 "C09": ("KEEP", "only quadratic models and empirical work (2301.07737, 2306.04815)"),
 "C10": ("KEEP", "upper bounds only; the optimal dimension dependence (lower bound) open"),
 "C11": ("KEEP", "2410.04887 shows collapse at weight-decay optima of wide networks, 2510.21078 shallow; GD on deep networks open"),
 "C12": ("KEEP", "2309.10402 settles L^p width max(dx,dy,2) and a uniform lower bound d_y+1; the exact uniform width open"),
 "C13": ("KEEP", "linear and specific nonlinear classes only; general characterisation open"),
 "C14": ("KEEP", "no hit; Razin-Cohen show it is not a norm; no explicit characterisation known"),
 "C15": ("DROP", "near-duplicate of replacement N03 (S_5 chain-of-thought separation, gradient lower bound)"),
 "C16": ("DROP", "Barboni-Peyre-Vialard 2403.12887 and earlier mean-field ResNet work cover much of it; statement too loose to vet"),
 "C17": ("DROP", "Damian-Ma-Lee 2021 prove label-noise SGD reaches stationary points of the trace-regularised loss with a rate; remaining gap too loose"),
 "C18": ("KEEP", "2610.26795 is a depth construction for max; the exact width-depth trade-off open"),
}
OLD = ["T313", "T318", "T320", "T321", "T339", "T358", "T399", "T401", "T403", "T404", "T414", "T415", "T419", "T420", "T422"]
rows = list(csv.reader(io.open("DL_CANDIDATES_1113.tsv", encoding="utf-8"), delimiter="\t"))
hdr = rows[0]
if "litcheck" not in hdr: hdr.append("litcheck")
li = hdr.index("litcheck")
for r in rows[1:]:
    while len(r) < len(hdr): r.append("")
    d, why = DEC[r[0]]; r[li] = "%s: %s (13 Nov)" % (d, why)
with io.open("DL_CANDIDATES_1113.tsv", "w", encoding="utf-8", newline="") as fh:
    csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)
keep = [r for r in rows[1:] if DEC[r[0]][0] == "KEEP"]
with io.open("REPLACEMENTS_1113b.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["old_id", "new_key", "new_title", "statement", "litcheck"])
    for o, r in zip(OLD, keep): w.writerow([o, r[0], r[1], r[2], r[li]])
    for o in OLD[len(keep):]: w.writerow([o, "PENDING", "", "", "no kept candidate left (5 of 18 dropped); needs a new candidate"])
print("kept", len(keep), "dropped", 18 - len(keep), "replaced", min(len(keep), len(OLD)), "pending", OLD[len(keep):])
