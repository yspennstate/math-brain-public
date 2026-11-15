# T304 round 5 log

Task: “take the NEXT checkable step on this problem, building on that work.” Date: 15 November 2026, Asia/Tbilisi; exact request time was not supplied.

## Step 1 — orientation and first source search

Read the startup memory and compute-state file read-only. The current folder-only restriction rules out brain recall/logging, mesh, and checklist commands that mutate other folders. No subagents, git, or external writes. Compute state says warn / owner_away_open with CPU saturation. Only short reads and tiny standard-library checks are planned; every subsequent shell command uses `nice -n 15 env OMP_NUM_THREADS=1` (also numerical-library thread limits for Python). The sandbox refuses priority adjustment (`nice: setpriority: Operation not permitted`), as in prior rounds; no heavy computation will run.

Commands: `rg --files` to locate prior reports, proofs, logs and scripts; `cat` to read earlier work, startup memory, and compute state. First batch output was truncated, so remaining prior material will be read in bounded pieces. Original-round PROOF.md is absent.

Web search queries: exact sampling title with correction/error; Zhou Suzuki 2611.05813; subpolynomial query complexity sampling OpenAI. Returned the same November proximal-sampling follow-up and release sources; no new settlement identified yet. Sources must be opened before using claims.

## Step 2 — prior work read and update search complete

Read the round 3 proof and script, round 4 proof, full log and script, and original report/log. Original PROOF.md and scripts are absent. Opened current full HTML of arXiv:2611.05813v1 (Huanjian Zhou and Taiji Suzuki), 2611.03442v1 (Wei Guo, Bo Yuan, Ye He, Jiaming Liang, Molei Tao, Yongxin Chen), and 2611.15849v1 (Evan Dogariu), plus current original numerics.tex. No new settlement located in the bounded search, completed within five minutes. No SOLVED_ELSEWHERE.md warranted. Preserved round 4 sources and verification, and its proof/script/log/report under sources/round4. All writes are local. A read attempted /bin/sed, which is absent; corrected to /usr/bin/sed.

Choice for the single extension: Lemma 6.2 harmonic/angle RMS estimates, especially its endpoint weighted integral estimate, as explicitly requested by round 4. First independently rederive the inherited coefficient cancellation, Hermite endpoint rule, and exponent arithmetic.

## Step 3 — recheck holds; precise extension scope

Ran `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -I -B sources/round4/audit_round4.py`. All earlier exact checks pass: Gaussian completion, unequal trees, Hermite weights 3..8, cancellation for r down to 10^-30, scale bounds, 63/128 threshold and 1/12 margin. Independently read the proof: subtracting the forward starting state makes its correction exactly -r times a weighted mean sum; division by rs therefore leaves 1/s. A mean-center expression consequently costs O((r/sigma)Q D_theta+r^2), with no 1/r. The scale identities and exponent arithmetic hold. A second implementation of the interpolation weights will be included in this round's audit.

Opened current original jets.tex, divergence.tex and centering.tex with the GitHub read connector; saved the returned text in sources/. Also reopened all three candidate introductions, numerics.tex, history.md, and lean/docs/139.md. Those last six texts are retained for source comparison. No repository mutation was used. A read attempted /usr/bin/rg, which is absent; use rg from PATH henceforth.

The words “endpoint weighted integral” in Step 2 were too broad: this session's one extension is Lemma 6.2 alone, including the stationary harmonic derivative input from Lemma 5.4. Lemma 6.3's endpoint *error* remains outside this check. The inherited Hermite-weight recheck concerns round 4's structural result only.

Working observation before proof: the spatial derivative hypotheses actually supplied for T_rho-id and M_rho have R^{-(j-1)}, one power better than the weaker R^{-j} assumption used in Lemma 5.4. For constant harmonic skew matrix, a direct weighted-divergence induction appears to retain this extra R. Check this induction and then derive the angle and harmonic truncation bounds explicitly. Probability-flow accuracy (Proposition 6.1), jet bounds (Proposition 3.2), and transport spatial bounds (Lemma 5.1) remain identified inputs, not newly certified global results.

## Step 4 — proof and exact checks saved

Wrote PROOF.md. A direct integration-by-parts identity bounds weighted divergence in L2 using only the Hessian bound and Frobenius norms of the field and its first derivative. Commuting spatial derivatives past it gives an induction with exponent j+2k-1, starting from the source's j-1 spatial exponent. For the constant harmonic skew matrix this proves fixed-time RMS derivative bounds l sqrt(d) R^{-(2m-1)} and L sqrt(d) R^{-(2m-1)}. Taylor remainder plus the angle stencil gives delta^{2tm-3t}, rather than the source's weaker delta^{2tm-4t}. Harmonic interpolation gives delta^{2tm+t}, rather than delta^{2tm}. Approximate forward corrections use the probability-circuit error as an explicit hypothesis; their input errors are multiplied by O(l). No assumption of stationarity for approximate states is used.

Command: `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -I -B audit_round5.py`.

Output:
```
Inherited recheck: Hermite bases by nodal correction (orders 3..8), coefficient cancellation, 63/128 and 1/12: PASS
Weighted-divergence identity/inequality and harmonic generator: 6 translated quadratics, derivatives 1..8: PASS
Angle weights/orders 2..9: basis derivative = closed formula; first omitted moment by two methods: PASS
Derivative-exponent recursion: R^(-(j+2k-1)); weaker base loses the R gain: PASS
Delta exponents by two forms: angle 2tm-3t; harmonic 2tm+t; both gain t: PASS
Correlated-anchor failure: Var(W_pi/4)=2 versus stationary variance 1 (exact identity).
```

All arithmetic is rational. New endpoint weights use Lagrange bases corrected by the nodal product, independently of the prior matrix solve. The weighted-divergence identity is checked by direct exact Gaussian expectation and its integrated formula, including translations 10^12; the harmonic generator is computed from the vector field and weighted adjoint independently. Angle weights are checked both as derivatives of explicit basis polynomials and by their binomial formula, including the first omitted moment. Exponent propagation is recomputed by maximizing the terms in the induction, then compared with its closed formula. No simulation, numerical package, worker, compilation or heavy computation ran.

Failure checks: correct marginals with correlated harmonic anchors do not preserve stationarity (variance 2 at pi/4 instead of 1). The source's independent anchors exclude this. Using only the weaker R^{-j} spatial hypothesis loses the additional R; the stronger hypothesis used here is the source's actual stated transport/jet estimate. Fixed-order and positive-R restrictions are retained. No counterexample to the conditional result was found.

Recorded nine reopened primary-source paths and blob hashes in source_checks.json. Repository history still ends 29 October and gives no sampling withdrawal; the Lean scope note remains the fixed-error, condition-number-two joint oracle claim. These source records do not constitute a Lean build or full proof audit.

## Step 5 — reopened source audit

First blob-hash check failed on the Sobolev introduction because its original ends in two newlines and the tested variants had at most one. Saved the newly reopened text separately and ran diff: identical to the inherited snapshot. Corrected the normalization to preserve 0..4 terminal newlines. All nine current original blob hashes now match the snapshots; all three main theorem environments are exact substrings of VERIFY.md. source_checks.json records original terminal-newline counts and local SHA-256 values. No substantive source difference was found. Repaired local links in the preserved round 4 proof and inherited verification.

## Step 6 — final report and completion audit

Final REPORT.md records the conditional local PROVED result and keeps the whole-row PARTIAL-CLAIMED literature verdict. VERIFY.md retains all three exact main theorems, detailed comparisons, inherited follow-ups and the three-sentence recommended status; it adds this round’s opened sources and Spot check. Re-ran audit_round5.py after adding an explicit exact variance assertion; output remains all PASS.

Final short pathlib/re/json audit checked verdict scope, required artifacts, local links, paired Markdown/math delimiters, three-sentence recommendation, nine successful source comparisons, and both new exponent displays: PASS. Fixed interpolation orders and unverified analytic inputs are explicit. All work and scripts remain in this folder. No git, external mutation, publication, account, subagent, GPU, numerical package, simulation or Lean build was used.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026; exact request time not supplied, first logged clock reading 07:34:55 +04.
