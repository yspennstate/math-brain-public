# T139 working log

Task: “push this problem forward by one checkable piece.” Session began 2026-11-14, 22:02 Asia/Tbilisi (18:02 UTC).

## Startup

- Read the supplied instructions, local file listing, startup memory index, brain navigation index, and compute governor state. Folder initially contained only PROMPT.md.
- The task's folder-only rule overrides the global requests to register mesh/checklist entries and write brain memories outside this folder. No external state was intentionally changed; no subagents or git used.
- Startup command used `OMP_NUM_THREADS=1 nice -n 15 python3` for small read-only file reads. The launcher reported `nice: setpriority: Operation not permitted` but Python completed. Investigating inherited scheduling priority before computation.
- Governor: status `warn`, mode `owner_away_open`, CPU 97.8%, free memory 74%. Choose a small proof or a brief exact computation; no heavy workload.
- Literature search started at 18:02 UTC; stop by 18:12 UTC. Queries: `Mansour conjecture DNF Fourier concentration 2025 2026`; `Mansour conjecture Fourier DNF Lecomte Tan 2024 2025 solved`.

## Literature check completed (18:04 UTC, under ten minutes)

Opened and read the following primary pages:

- Victor Lecomte and Li-Yang Tan, *Sharper bounds on the Fourier concentration of DNFs*, https://arxiv.org/abs/2109.04525 (v2, 2021). Its read-number improvements match the brief.
- Adam Klivans, Homin Lee, and Andrew Wan, *Mansour’s Conjecture is True for Random DNF Formulas*, https://eccc.weizmann.ac.il/report/2010/023/ (revision 3, 2010). The abstract also covers constant-read DNFs; revision 2 corrected the read-k section. Do not use an earlier draft without checking it.
- Mohsen Heidari and Roni Khardon, *Learning DNF through Generalized Fourier Representations*, https://arxiv.org/abs/2506.01075 (v2, June 2026). This concerns non-product distributions; the abstract does not establish general uniform-distribution DNF concentration.
- Esty Kelman, Guy Kindler, Noam Lifshitz, Dor Minzer, and Muli Safra, *Towards a Proof of the Fourier--Entropy Conjecture?*, https://arxiv.org/abs/1911.10579. The abstract gives concentration of order exp(O(I log I)) for constant variance, not the desired removal of log I.
- Xiao Han, *A New Bound for the Fourier-Entropy-Influence Conjecture*, Combinatorica 45, article 4 (2025), https://doi.org/10.1007/s00493-024-00133-z. The abstract bounds entropy using the individual influences; it does not settle the DNF conjecture.

Additional searches combined exact conjecture phrases with 2025/2026 and Fourier concentration. No later solution or substantial improvement to the stated general DNF bound was found. This is a limited search, not proof that none exists. No SOLVED_ELSEWHERE.md is warranted.

## Chosen piece (before implementation)

Compute the exact worst-case Fourier tail after retaining m coefficients, for every m=0,...,16 and every DNF term budget t=0,...,8, among all 65,536 Boolean functions on four variables. This settles the finite concentration problem for n<=4 at every error tolerance, not only selected epsilons, and supplies explicit extremizers. It is deliberately a finite result; no asymptotic advance is claimed.

Method: enumerate all 3^4=81 consistent conjunctions, including the empty conjunction. Compute minimum DNF term counts by shortest paths under union of their truth sets. Independently check each minimum with exact prime-implicant set cover. Compute all Fourier coefficients with an integer Walsh transform and independently with direct character sums. Record all function data and the worst-tail envelope, with explicit witness DNFs. Use only the standard library, one thread, <1 GB memory, a hard 20-minute timeout, and scheduling priority >=15.

Priority investigation: `ps -o pid,ppid,ni,command -p $$` was blocked by the sandbox. Read the existing verified memory `macos_os_nice_raises_at_nice_20_stacked_relative_nice_2026_11_10.md`; it says relative nice can fail when already at nice 20. The computation will query `os.getpriority` and refuse to run if its actual priority is below 15. No raising of priority is attempted.

## Implementation and first launch

- Added `compute_four_variable.py`, with exact integer arithmetic throughout. The independent cover search allows overlapping terms; simply subtracting a term and minimizing the residual as a new DNF would be wrong and was not used.
- Priority command: `OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os; print("actual_nice", os.getpriority(os.PRIO_PROCESS, 0)); print("OMP_NUM_THREADS", os.environ.get("OMP_NUM_THREADS"))'`. Output: `actual_nice 20`, `OMP_NUM_THREADS 1`; the `nice` warning comes from inherited lowest priority, and the process remains safely at 20.
- First command: `OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 compute_four_variable.py > computation_output.txt 2>&1`. Exit 1 before enumeration: setting a 512 MiB RLIMIT_DATA raised `ValueError: current limit exceeds maximum limit`. Inspect inherited limits and preserve any stricter hard limit before retrying. No mathematical result from this failed launch.
- Inherited RLIMIT_DATA and RLIMIT_AS both reported `(9223372036854775807, 9223372036854775807)`; startup RSS 12,222,464 bytes. Changed the guard to lower only the soft data limit to 128 MiB while preserving the hard limit, with a documented fallback if macOS rejects it. Fixed-size arrays and periodic RSS guards also bound usage. Relaunched the exact command above; output is being saved in `computation_output.txt`.

## Completed enumeration

Command: `OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 compute_four_variable.py > computation_output.txt 2>&1`.

Exit 0. Exact output is in `computation_output.txt`; machine-readable summary in `summary.json`. Important output:

```text
cubes=81; union_DP_complete; max_minimum_terms=8
minimum_terms_histogram={0:1, 1:81, 2:1804, 3:13472, 4:28904, 5:17032, 6:3704, 7:512, 8:26}
number_of_sorted_squared_spectral_types=8
independent_minimum_cover_checks=65536
independent_fourier_checks=65536
parseval_checks=65536
envelope_witness_checks=153
actual_nice=20
peak_RSS_MiB=26.516
elapsed_seconds=1.789
PASS: complete enumeration and both independent audits
```

For term budgets 2 and 3, the exact worst-tail numerators, after retaining m=0,...,16 coefficients, are identical:

```text
[256,220,184,148,112,80,64,48,32,28,24,20,16,12,8,4,0] / 256.
```

For every term budget >=4 the exact envelope is `(16-m)/16`. The four-variable bent example given in PROOF.md attains it. All individual function Fourier numerators and minimum term counts are in `functions.csv`; all envelope values and explicit minimizing-term-count witness DNFs are in `tail_envelope.csv`. These cover every epsilon, including epsilon>1/2.

The observed envelope implies a finite corollary with the optimal constant: for n<=4, t>=2, and 0<epsilon<=1/2, sparsity at most `t^(2 log_2(1/epsilon))` suffices. This restricted epsilon range is explicit; the full-interval claim with constant 2 would be false. The corollary will be justified with exact integer inequalities, not numerical logarithm comparisons.

Next audit: independently rebuild the envelope from the saved data; check all coefficients by literal character sums; check the integer inequalities and named examples; then write the proof and report. No extrapolation beyond four relevant variables is intended.

## Independent saved-data audit

Added `audit_saved_data.py`, which does not import the enumeration program. Command:

```sh
OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_saved_data.py > audit_output.txt 2>&1
```

Exit 0; complete output in `audit_output.txt`. All 65,536 saved Fourier vectors checked by summing explicit products of +/-1 coordinates. All 153 envelope entries reconstructed from CSV with fresh tail summation. All 153 witness DNFs interpreted directly and checked against both their masks and tails. Hashes of the three primary data files matched. Actual nice 20, peak RSS 19.781 MiB, elapsed 1.264 seconds.

For m=4,...,15 the integer inequalities `(m+1)*A_m^2 <= 256^2`, needed for the constant-2 corollary, have left sides:

```text
62720,38400,28672,18432,9216,7840,6336,4800,3328,2016,960,256
```

The right side is 65,536. Direct checks of named examples: mask 0357 has minimum two terms and square numerators `36` six times and `4` ten times; mask 7888 has minimum four terms and square numerators `16` sixteen times. The first example requires four coefficients at epsilon=1/2 and proves the restricted constant 2 is optimal.

Adversarial endpoint check: extending this constant-2 claim to epsilon>1/2 fails. At epsilon=27/32, mask 0357 has best one-monomial error 55/64>27/32, while the proposed sparsity bound would be `(32/27)^2<2`. This is a counterexample only to that extension of the finite corollary, not to Mansour's conjecture with an unspecified constant. The full exact envelope remains valid for the entire interval 0<epsilon<1.

`spectral_types_by_terms.csv` records the independent spectrum-type/term-count cross-tabulation. There are eight spectral types in total. Every nonflat type occurs at term budget <=2, and no flat type occurs at budget <=3. This explains the identical envelopes for budgets 2 and 3. The flat type occurs 896 times, all with minimum term count at least 4.

## Written result and final audit (18:12 UTC)

- Wrote `PROOF.md` with the exact finite statement, exhaustive algorithm justification, independent cover recurrence, Fourier normalization and sign conversion, explicit extremizers in each part of the curve, and the constant-2 corollary with its precise epsilon restriction.
- Re-derived the maximum minimum-DNF size without enumeration: fix three variables to obtain eight assignment pairs, each coverable by at most one term; parity needs eight singleton terms. This independently verifies the maximum of eight.
- Re-derived the three kinds of envelope witnesses by algebra: disjoint width-two conjunctions have square numerators 36 six times and 4 ten times; the two disjoint width-three terms in mask 001b have square numerators 64 twice, 16 eight times, and 0 six times; a width-four conjunction has 196 once and 4 fifteen times. The four-term XOR construction has sixteen equal weights 1/16. These match the saved-data checks.
- Wrote `REPORT.md`, beginning with the required COMPUTED verdict. It records the commands, measured resources, failed limit-setting launch, endpoint countercheck, limited scope, and a concrete next step. No general conjecture claim, asymptotic improvement, or novelty claim is made.
- No new computation is needed after the two successful audits. All substantive outputs remain in this folder.

Task completed: “push this problem forward by one checkable piece” — 2026-11-14, 22:02 Asia/Tbilisi.
