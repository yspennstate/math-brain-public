# T324 work log

Task: “push this problem forward by one checkable piece.” Session date: 14 November 2026 (Asia/Tbilisi).

## 1. Orientation and literature check

Read the local task folder, the startup memory, and the compute governor state. The folder initially contained only PROMPT.md. The governor reported CPU saturation, so no numerical sweep is planned. The task's folder-only rule supersedes the general instructions to write to the shared brain, checklist, or mesh; none of those external stores was changed. No subagents or git commands were used.

Web searches (within the first ten minutes):

- `"metastable" "transformers" merging clusters 2025 2026`
- `"2410.23228" metastable clustering`
- `"transformer" "metastability" "noise" clustering`
- `"Bruno" "Pasqualotto" "Multiscale" transformers`
- `transformer metastable clustering coarsening merging 2026 arxiv`

Opened arXiv pages 2410.23228, 2512.01868, 2610.08755, and 2605.10931. Search found a potentially decisive omitted follow-up: Giuseppe Bruno, Federico Pasqualotto, Andrea Agazzi, *A multiscale analysis of mean-field transformers in the moderate interaction regime*, arXiv:2509.25040 (2025). The abstract claims rigorous limiting dynamics for the fast collapse, intermediate clustering, and slow sequential merging phases. Next: inspect the actual theorem hypotheses and conclusions before deciding whether the requested literature-stop condition applies.

No proof or computation has been claimed at this stage.

## 2. Literature outcome and choice

Inspected the actual PDF of arXiv:2509.25040, especially Proposition 3.9, Proposition 3.11, Appendix C, and the discussion. Proposition 3.11 assumes atomic, equal-weight initial clusters and a unique closest pair, and proves rescaled convergence only before the first collapse. Proposition 3.9 is a vanishing-residual statement for an assumed smooth heat solution; it is not a complete proof from generic initialization through all mergers. The paper itself identifies joining phases as further work. Inspected arXiv:2410.06833 (2024), which already proves deterministic exponentially long persistence for separated data. Inspected Sayan Banerjee's arXiv:2610.08755v2, Section 3.3.1: its noisy-transformer consequences are conditional, use unnormalized attention, and distinguish logit sharpness from inverse noise strength. These are substantial relevant partial results, but all predate the supplied November 2026 status. No later resolution was found. The requested post-status literature-stop condition is therefore not established. Search ended within ten minutes; no SOLVED_ELSEWHERE.md is warranted.

Choice: prove the exact two-token normalized-attention reduction on the circle, including the joint low-temperature/small-noise logarithmic mean merging time. For fixed initial gap x and target gap delta, the proposed exponent is min{1-cos(x), r} when angular noise diffusivity nu satisfies -log(nu)/beta -> r>0. This treats one concrete special case of both deterministic and noisy dynamics, and tests whether deterministic exponential waiting survives independent token noise. It does not address generic cluster counts. The claim will be proved from an exact one-dimensional hitting-time formula; no general Freidlin–Wentzell theorem will be invoked.

Potential failure to test: noise can visit gaps larger than the initial gap, where deterministic attraction is weaker. A local drift estimate alone cannot bound the mean hitting time. The proof must control that outward excursion term explicitly. Also check the factor 2 in the difference diffusion, the reflecting boundary at pi, and the exceptional exactly antipodal initial state.

## 3. Proof written

Wrote PROOF.md. The exact gap drift is -2 sin(s)/(1+exp(beta(1-cos(s)))); its diffusion generator is 2 nu d^2/ds^2. A reflecting/absorbing boundary-value calculation gives an exact double-integral mean entrance time. Bounding its near-diagonal and outward-excursion parts separately proves the claimed minimum exponent, including equality of the two scales. The deterministic prefactor is exp(beta(1-cos(x)))/(2 beta sin(x)^2).

Added verify.py using only the Python standard library. It checks the deterministic integral in two coordinates and compares the noisy integrating-factor formula against a separate finite-difference boundary-value solve. A refined mesh table checks the crossover numerically; the proof does not depend on this table.

## 4. First audit run and numerical correction

Command: `env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py`

Initial output: `nice: setpriority: Operation not permitted`; then an assertion failed for the most stiff crossover mesh comparison. A diagnostic run of the same launcher printed `effective nice: 20`: the process already inherits lower scheduling priority than requested, so the nice warning does not mean it ran at normal priority. No heavy computation was attempted. Diagnostic maximum mesh discrepancy was 0.003127 at r=0.8, beta=160; the original code used a trapezoidal integral across a sharp derivative layer. Replaced that final integration by the exact cell integral for the piecewise constant drift, using an expm1/series expression to avoid cancellation. Kept the original mesh tolerance rather than loosening it. The proof and exact formula were unchanged.

## 5. Successful verification and attempts to break the result

Reran the exact command above. Exit code 0; elapsed time reported by the execution tool was 0.405 seconds. The program uses standard-library arrays of at most 65537 entries and one thread; its memory demand is far below 1 GB. No GPU or worker process is used.

Exact output:

```text
nice: setpriority: Operation not permitted
Deterministic coordinate checks: max relative difference = 1.071e-11
Deterministic exact/asymptotic ratios: beta=4: 1.607466, beta=20: 1.053957, beta=80: 1.011037, beta=160: 1.005362
Noisy kernel versus independent finite-difference BVP: max relative difference = 3.143e-07
Crossover: r, beta, log(mean)/beta, predicted limit
0.3, 20, 0.281058, 0.300000
0.3, 40, 0.286241, 0.300000
0.3, 80, 0.291745, 0.300000
0.3, 160, 0.295431, 0.300000
0.8, 20, 0.562036, 0.637642
0.8, 40, 0.532985, 0.637642
0.8, 80, 0.576100, 0.637642
0.8, 160, 0.602503, 0.637642
All checks passed. Wrote verification.json and crossover.csv.
```

Data: verification.json contains both coordinate integrals, both noisy methods at two mesh sizes, and all crossover values; crossover.csv is the crossover subset. The asymptotic exponent convergence can be slow and nonmonotone (r=0.8, beta=20 versus 40). The table is a consistency check, not a proof or a certified numerical bound.

Analytic audit: rederived the deterministic equation directly for c=x_1 dot x_2, giving c'=2(1-c^2)/(1+exp(beta(1-c))). Derived the same prefactor in the cosine coordinate. Checked the difference noise factor both by independent Brownian variances and by the two-angle generator; checked the cosine Ito correction -2 nu c independently. Differentiated an explicit logarithmic primitive of the drift to check the sign and factor in the exact kernel. Added all these derivations to PROOF.md.

Cases searched for: exactly antipodal deterministic data never merge; exact deterministic collision takes infinite time; unequal cluster masses change the scalar drift; independent noise inside a group does not preserve atomic groups. All these are excluded explicitly. The threshold equality r=1-cos(x) is covered by the lower bound and the diffusion upper bound. Noise with subexponential inverse diffusivity has exponent zero. The upper estimate (5) handles the feared rare outward excursions; ignoring them would not have justified the mean-time theorem.

## 6. Deliverables

Wrote LITERATURE.md and REPORT.md. The verdict is PARTIAL: a fully proved two-token special case, not a resolution of the original mean-field cluster-count problem. All artifacts remain in this folder. No external stores, repositories, or services were modified.
