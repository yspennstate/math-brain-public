# T096 work log

Task received: 2026-11-14, approximately 21:16 Asia/Tbilisi (local clock at first command: 21:16:17 +04).
User's task: “push this problem forward by one checkable piece.”

## 21:16 — startup and scope

Read the local startup memory and compute state. The governor reports status `ok`, mode `owner_away_open`; this session will nevertheless use only one thread and nice 15 for numerical programs. The directory initially contains PROMPT.md and runner logs, with no previous mathematical work.

The task-specific restriction “work only inside this folder” takes precedence over the global requests to mutate the shared mesh, checklist, and brain. No shared-state registration scripts are run, no git is used, and no subagents are started. This file is the local task record.

Started the literature search at 21:16, with a ten-minute maximum. Initial web searches: `SK Glauber dynamics rapid mixing beta Sherrington Kirkpatrick 2026 Wang Boban Li Oveis Gharan` and `arxiv 2608.22159 2609.13138 2610.09882`. Search results point to the stated papers and additional September/October claims; these will be checked against primary sources before any conclusion.

## Piece chosen — before the calculation

Find and prove an explicit three-spin obstruction to the proposed shortcut “zero external field is always the slowest field for a fixed interaction matrix.” Work with an antiferromagnetic triangle of interaction strength K, and compare zero field with uniform field K. Derive the zero-field gap exactly and use an explicit test function at nonzero field; verify independently by constructing both 8-by-8 transition matrices. If successful, this gives a concrete obstacle to extending the newly located zero-field result to arbitrary fields. It will not settle the asymptotic random-disorder problem, and no such claim will be made.

Reason for this choice: the remaining gap in the literature is precisely external fields. A small exact example can test a potential field-comparison reduction without assuming the correctness of the recent long zero-field preprint.

## 21:20 — first computation and independent checks

Wrote `check_triangle.py`. It enumerates all eight states, constructs rates from differences of full Gibbs log weights, diagonalizes the reversible symmetric generator, checks the analytic invariant subspaces, and computes characteristic polynomials with exact rational arithmetic at K=log(2). These are independent of the conditional-mean derivation used for the proof.

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 check_triangle.py > triangle_output.txt 2>&1
```

Exit code 0; elapsed approximately 0.48 seconds. The sandbox reports `nice: setpriority: Operation not permitted`, but the child explicitly verifies its inherited effective nice value is 20 (lower priority than requested). No priority increase was attempted. All arrays are at most 8 by 8. The script sets a 60-second CPU limit.

Output that matters:

```text
K                 zero gap       field gap      Rayleigh upper
   0.000000000000 1.000000000000 1.000000000000 1.714285714286
   0.100000000000 0.901312339888 0.902059543159 1.586423682478
   0.250000000000 0.768941421370 0.773308641627 1.380924638084
   0.500000000000 0.619202922022 0.592440464037 1.038017037749
   0.693147180560 0.558823529412 0.461355337305 0.799739921977
   1.000000000000 0.517986209962 0.286548019965 0.498306747347
   2.000000000000 0.500335350130 0.044755842535 0.079984579573
   3.000000000000 0.500006144175 0.006177717752 0.011108507849
   5.000000000000 0.500000002061 0.000113493384 0.000204284227
field_zero: lambda*(lambda - 3)*(17*lambda - 49)*(17*lambda - 32)*(34*lambda - 53)**2*(34*lambda - 19)**2/386201104
field_K: lambda*(lambda - 3)*(65*lambda**2 - 297*lambda + 328)*(325*lambda**2 - 720*lambda + 263)**2/6865625
max_zero_spectrum_residual: 1.7763568394002505e-15
PASS: full spectra, invariant subspaces, stationary laws, and exit rates
```

Full stdout is in `triangle_output.txt`; data are in `triangle_data.csv` and `triangle_exact.json`.

The small-K rows matter: adding this field initially *increases* the gap. No claim of monotone degradation in K, or of degradation at every positive K, is justified. At K=log(2) the strict comparison is exact.

## Literature check completed within the ten-minute limit

Search began at 21:16; substantive literature work ended at approximately 21:21. Opened arXiv abstract pages 2608.22159, 2609.13138, 2610.17717, 2607.06813; opened full HTML of 2609.13138 and 2610.17717. Also opened the original OpenAI repository and the spectral-gap manuscript's original citation README and PDF hosting page. The web tool could not extract the original PDF; a shell download failed immediately because shell DNS/network access is restricted. No PDF was downloaded. This limitation is recorded in SOLVED_ELSEWHERE.md.

The main new lead is the September 24 OpenAI zero-field spectral-gap claim, discussed explicitly in Section 1.2 of Du–Huang–Mohanty–Rajaraman (2610.17717). It does not cover arbitrary fields. The latter paper proves simulated-annealing sampling, not fixed-temperature worst-start Glauber mixing. Boban–Li–Oveis Gharan's Theorem 1.5 and model definition explicitly concern zero field. The July high-field paper is another omitted special regime. No complete resolution of the stated arbitrary-field problem was found. Continue with the chosen mathematical piece.

## 21:24 — proof and adversarial audit

Wrote PROOF.md. It derives the complete spectra at zero field and at uniform field K by decomposing all eight spin monomials. The latter calculation identifies the exact gap, rather than merely finding a small eigenvalue. A separate singleton bottleneck gives γ(K,K)<9/[2(1+exp(2K))], while γ(K,0)≥1/2, proving that their ratio tends to zero exponentially in K. The no-jump probability also supplies a direct total-variation mixing lower bound.

Strengthened `check_triangle.py` to compare all eight eigenvalues in both fields, not just the smallest ones; added exact symbolic asymptotics and peak-memory accounting. Repeated the exact command above; exit code 0 in approximately 0.56 seconds. The nine numerical rows and exact characteristic polynomials were unchanged. New final output:

```text
field_gap_series_q_exp_minus_2K: 5*q/2 - 25*q**2/8 + O(q**3)
max_full_spectrum_residual: 1.9984014443252818e-15
PASS: full spectra, invariant subspaces, stationary laws, and exit rates
Data: triangle_data.csv; triangle_exact.json
peak RSS bytes: 68583424
```

The final complete output, including the inherited nice=20 verification, is `triangle_output.txt`. Peak memory was 68.6 MB in decimal units, below 1 GB. The compute governor still reported `ok` at 21:24.

Checks made to try to break the result:

- Re-derived the zero-field spectrum by monomial actions, then compared it with independently constructed full matrices (maximum error below 2×10⁻¹⁵).
- Re-derived the field spectrum in two invariant sectors; independently factored the full rational 8-by-8 characteristic polynomial at K=log(2).
- Checked that all remaining eigenvalues exceed the proposed gap; finding an eigenvalue alone would not have established the exact gap.
- Recomputed the partition function by magnetization multiplicities, the singleton mass by state enumeration, and each exit rate from Gibbs weight ratios.
- Verified stationarity, detailed balance through the symmetric similarity transform, and generator row sums.
- Checked K=0, where both chains are independent spins with gap 1, and small positive K, where this particular field actually increases the gap. The theorem does not claim a comparison for every K.
- Checked the factor of three between per-site continuous time and discrete uniform-site updates.
- Checked that a point in Gaussian support is a probability-zero point; the strict finite-dimensional comparison persists on an open neighborhood, giving positive probability only for fixed n=3. No asymptotic SK failure probability follows.
- Checked the K→∞ limit separately from the SK n→∞, fixed-β limit. They are different. No β-threshold improvement is claimed.

The attempted general field-monotonicity shortcut fails. A new SK high-probability bound was not obtained. Novelty of the triangle calculation is not established; the contribution is a self-contained exact obstruction and reproducible finite computation for subsequent work.

REPORT.md records the result and the remaining task.

Final artifact audit: `head -1 REPORT.md` confirms the required `VERDICT: PROVED ...` first line. `ls -lh` confirms that the proof, report, literature update, script, stdout, CSV and exact JSON all exist inside this directory. No external state was changed.
