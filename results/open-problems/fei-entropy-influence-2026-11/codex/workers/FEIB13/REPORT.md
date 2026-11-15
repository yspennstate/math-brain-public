# FEIB13 report

PROVED correction to FLOW 3b: AND₂ (`0x8`) has an empty Fourier entropy contribution of 0.5 bit. Its H is 2 bits, while 2P+2(I−Var)=1.5 bits. The read-once zero-cancellation statement needs to exclude the empty derivative for biased functions. P, A and the general identities retaining Gamma are unaffected.

General containment P≤CI remains OPEN. The completed work gives exhaustive small-function data, analytic counterexamples to three proposed moment shortcuts, and a sharp tribes classification for the weakened W discount. Full proofs are in PROOFS.md and tables in RESULTS.md.

1. Sparse split — CHECKED all NPN classes through n=5, 5,120 samples each at n=6,7, and all requested families. Every tested function satisfies Sp₂≤0.5056921 I; Sp₆≤0.0546876 I. PROVED Sp_K≤2I for all equal-width tribes. Universal sparse containment is OPEN. Extremal truth tables and actual carrier sets are saved.

2. T and budgets — PROVED T_t≤P+(1−t)I; for tribes T_(1/2)≤2.5I. AND_n forces the constant to be at least 1.5. General T and its relative-increment form are OPEN. PROVED F_R(1/2)≤up(R)p(R)^(1/3). Both untruncated counting proposals are FALSE: the up count fails even with theta=0, and the tau count fails for every theta>0. M=ceil(2I),ceil(4I) cutoffs passed the numerical tests; a general proof remains OPEN.

3. W — FALSE as stated for every finite c,K, by balanced tribes. PROVED for all equal-width tribes and every 0<theta<1: c≥2^theta/(2^(1−theta)−1), K=2^(4−2theta) suffice; every smaller c fails. At theta=1/2 take c=2+sqrt(2), K=8. General weakened W remains OPEN.

4. References — PROVED the thinned laws and uniform mixture are ≤up and have cost between H and H+I. Their universal linear cost is equivalent to FEI. CHECKED bounded ratios over tribes through width 64 and majority through n=255 simultaneously; PROVED cost≤7I for all equal-width tribes. The proposed Markov product equals up(R), is not a sub-probability, and its normalization has unbounded cost/I on tribes.

5. P and A — PROVED for every equal-width tribes function P≤2I and A≤4I−2Var; for AND and all address functions P≤I, A≤3I. Every general implication is stated for both P and A, with the moment Jensen constant explicit. No universal containment constant is claimed.

Verification: complete NPN counts 2, 4, 14, 222, 616126; the independent audit covers all 65,536 four-variable truth tables and every stored extremal witness. Small-family formulas match independent restriction sums. AND budgets use 160 decimal digits to avoid catastrophic rounding near 1. audit.json, census.json, structured.json, families.json and mux.json are the numerical sources. resources.json records actual memory and elapsed seconds.

Useful files: PROOFS.md, RESULTS.md, extremal_truth_tables.csv, carriers.json. Reproduce with `python3 run.py`. No subagents, model calls, publishing, shared writes, or production processes were used. Brain recall helped orientation; the math store was unavailable.

Open work is mathematical, not a missing input: T’s relative increments, the M=aI cutoff budget, and a weakened W for arbitrary Boolean functions. The two untruncated budgets and original W cannot prove containment in their stated forms.
CHECKED measured reproduction: peak resident size 270,745,600 bytes (258.203125 MiB); sum of child elapsed times 58.029360 seconds; every child exited 0 at nice 10. Source: resources.json. The runner completed with REPRODUCTION PASS and the independent audit with AUDIT PASS.


Task: “uniform-in-level containment” — brief read 2026-11-10 02:59 +04.
