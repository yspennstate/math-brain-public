# account03/B17 — full pinned-manuscript audit

Run: `20260924T141823Z-account03-B17-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Verdict

**PASS for the stated 17-direction theorem, with one nonfatal presentation GAP.** I found no mathematical defect that invalidates the theorem

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

under independent arbitrary real coordinate densities bounded by `K`. This is an end-to-end mathematical audit of the pinned 790-line source, not formal verification or journal peer review. The full three-eigenvalue conjecture is not proved by this manuscript.

The nonfatal presentation GAP is in the final indefinite-pair paragraph: the notation `\|A/B\|` is used without defining `A/B`. The surrounding sentence and the immediately preceding Schur-complement construction make clear that the intended object is the pair Schur complement. Replacing the notation by that named Schur complement would remove the ambiguity without changing the proof.

## Source-range ledger

| Source range | Component | Verdict | Audit note |
|---|---|---|---|
| 47–80 | theorem, normalization, architecture | PASS | Quantifiers and `K^2/s` scaling agree with density scaling; no rotated-independence assertion. |
| 91–160 | Fourier inversion, power envelope, negative half moments | PASS | Constants and Tonelli/Gaussian regularization are consistent with the stated Fourier convention. |
| 169–217 | singular values, Schur count, diagonal dominance | PASS | Rank perturbation is used for nonsymmetric auxiliaries only. The singular Schur limit is valid: apply the invertible result at `t-|eps|` and pass an ordered singular value to the limit. |
| 221–301 | geometric BL, product projections, scalar Fourier powers | PASS | Projection argument uses deterministic orthogonal coordinates only inside an integral; it does not declare projected random coordinates independent. |
| 310–400 | decoupling, regularized crossing determinant, volume envelopes | PASS | Independent copies are introduced only for original-coordinate banks. The fourth-root exponent `-1/8` and order-5/order-3 conclusions are consistent. |
| 404–525 | square, definite pair, hyperbolic pair, quarter-power concentration | PASS | Measure domination handles rough densities; the indefinite-pair logarithmic envelope is not misused as a pointwise quadratic-phase decay theorem. |
| 528–645 | volume sampling, completion, spectral-to-volume, random cut | PASS | Border determinant counting is an inequality when singular seeds have nonsingular extensions. `rank R<=3r` and `rank R[L,L]<=r` are used in the correct places; diagonal-dominance slack is positive. |
| 654–724 | singular kernels, pivot half potential, nine-direction half potential | PASS | Truncated/full half-potential distinction is maintained and the outside tail contributes at most one. |
| 726–749 | main proof | PASS + presentation GAP | Four pivot/no-pivot branches exhaust the normalized problem. Undefined `A/B` should be replaced by the already-defined pair Schur complement. |
| 751–790 | threshold accounting, limits, references | PASS | Correctly does not claim continuity for all branches or a three-direction theorem. |

## Reproducibility/support-file check

I also read `README.md`, `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`, and the historical author `AUDIT.md`. The delivered checker is source-pinned and reports PASS on its finite exact/numerical diagnostics, but its own limitations correctly state that it is not a universal proof certificate. I used the symbolic manuscript proof, not those finite tests, as the basis for the verdict.

## Lower-threshold state after audit

The strongest complete improvement currently present in the repository is multiplicity nine: several workers independently reconstructed a full `s_9` proof, and a later constant ledger gives `<2600 K^2/s`. Multiplicity eight is not yet proved. The current sharp structural reduction in the no-pivot `s_8` chamber is the account03/B04 two-sided collar alternative. My separate improvement for this run derives a new dimension-free robust two-anchor consequence from that collar and closes its exact-zero anchor subcase; see the sibling improvement artifact for this same run.
