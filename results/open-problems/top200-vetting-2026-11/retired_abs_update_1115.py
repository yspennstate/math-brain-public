"""Write the 15 Nov abstract reads of the retirement sources into column 7 of DESERVE.tsv (22 rows)."""
import sys

P = "DESERVE.tsv"
TAG = "2026-11-15 retirement source abstract read on arXiv (retired_abs_1115.out), an agent (Opus 5.5): "
NOTE = {
    "T009": "2610.11611 is the Bethe lattice, not Z^3; it names the OpenAI preprint, which stays the only source for Z^3 (unrefereed, highest risk, keep REPORTED)",
    "T018": "Bizeul-Klartag-Lehec abstract presents a proof of KLS via the Song-Zhang tilt criterion; supports",
    "T020": "Lopatto abstract: replica symmetry for all (beta,h>0) predicted by AT; supports",
    "T026": "abstracts: quartic Salem reciprocals give Hausdorff and correlation dimension below one, so singular although not Pisot; the row was the every-non-Pisot form, so the retirement holds; transcendental form kept as T075",
    "T035": "Yau-Yin 2501.01718, the zigzag paper 2506.06441 and 2508.05802 read on 11 Nov; one dimension only; supports in d=1 (d=2,3 kept as T076)",
    "T040": "Ky-Tran and the computer-assisted 2609.24931 both state the Courtade-Kumar inequality with dictators extremal; supports",
    "T041": "Lu-Guo-Fang abstract states Talagrand's conjecture psi(u) <= C_a/sqrt(log u) for the noise measures mu_a; supports",
    "T051": "Lopatto abstract: Parisi measure supported on [0,q_beta] with smooth density and an atom, every beta>1, zero field; supports",
    "T052": "Newman-Stein read on 11 Nov: periodic-b.c. metastate unique, one spin-reversed pair; scope is the metastate",
    "T061": "Ling abstract proves Samuels' conjecture and with it Feige's; 2608.22816 and 2610.10380 restate it; supports",
    "T066": "Guo-Fang-Lu abstract: Komlos bound 3 sqrt(2 pi); 2609.27172 sharpens to 6.9013 and calls it proved; supports",
    "T069": "own paper (the author, 2607.11010); not re-read here, author's own source is not an independent check",
    "T074": "Gu-Sellke counterexample (fifth derivative), log-concave family 2608.30275; disproved, supports",
    "T082": "Simanyi 1205.0061 read on 11 Nov; published 2013; confirmed",
    "T113": "Ouimet-Greaves abstract proves the strong GPI for all positive exponents; supports",
    "T114": "published 2004 (Cordero-Erausquin, Fradelizi, Maurey); no arXiv source to read; confirmed from the record",
    "T135": "Kosenko-Tiozzo abstract resolves the singularity conjecture for finitely supported walks on cocompact Fuchsian groups; supports",
    "T140": "Hadas-Peled abstract: long-range order on Z^d for fugacity Omega(log d/d), critical fugacity d^(-1+o(1)); supports",
    "T143": "Zhou abstract gives the Gumbel plus log critical GMC mass limit law; supports",
    "T150": "Aronow-Lopatto abstract proves temperature chaos for the zero-field SK model at every pair of temperatures; supports",
    "T161": "not re-fetched; still rests on Remark 1.10(1) of 2403.07256, medium confidence",
    "T164": "no arXiv source; Lean counterexample repository; keep REPORTED",
}
rows = open(P, encoding="utf-8").read().split("\n")
done = 0
for k, line in enumerate(rows):
    f = line.split("\t")
    if len(f) == 7 and f[0] in NOTE and "title read" in f[6]:
        f[6] = TAG + NOTE[f[0]] + "; earlier: " + f[6]
        rows[k] = "\t".join(f)
        done += 1
open(P, "w", encoding="utf-8", newline="").write("\n".join(rows))
print("updated", done, "of", len(NOTE))
sys.exit(0 if done == len(NOTE) else 1)
