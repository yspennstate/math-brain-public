# fleet01/B20 r14 — release-gate audit and threshold synthesis

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T144935Z-fleet01-B20-fixedmult-auto11-r14`  
Pinned baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob on fresh master read: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256 from source manifest/checker: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Execution class: `WITHOUT_VERIFIED_BRAIN`.

## Verdict

**Baseline 17-eigenvalue manuscript: PASS mathematically, with minor presentation repairs only.** I reconstructed the full 790-line proof rather than inheriting a peer verdict. I found no fatal mathematical gap in the stated theorem

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for arbitrary real symmetric `A`, arbitrary independent real coordinate densities bounded by `K`, arbitrary dimension/signature/remaining spectrum, and arbitrary affine terms.

This is not a claim about the unrestricted three-eigenvalue conjecture. The support package `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` is present on the fresh read and its checker output is consistent with the pinned source; those diagnostics are not substitutes for proof.

## End-to-end classifications

| source range | item | verdict | reconstruction / reason | downstream |
|---|---|---|---|---|
| 1–90 | theorem, normalization, density conventions | PASS with presentation repair | Scaling `Y=KX`, `A/s` gives output scaling `K^2/s`; all affine terms are retained. Choose Borel representatives clipped into `[0,K]` when a pointwise representative is needed. | no theorem change |
| 91–173 | Fourier convention, scalar powers, convolution, Riesz half-potential | PASS | Plancherel is `int |hat f|^2=2pi int |f|^2`; inversion has `1/(2pi)`; the Riesz normalization and the `|t|^{-1/2}` weight match. Difference densities keep cap one after normalization. | constants consistent |
| 174–216 | sign-independent Schur spectral count | PASS | Invertible case follows from inverse compression/min–max for `A^{-1}` and `-A^{-1}`. For singular `A`, shift `A+eps I`; the moving threshold `t-|eps|` controls an ordered modulus from below and converges to `t`, so Weyl continuity closes the limit. | scalar/pair pivot counts sound |
| 221–255 | geometric Brascamp–Lieb heat flow | PASS | Differentiation and integration by parts give `partial_t F-Delta F=F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` by the frame contraction. Gaussian regularization/tails justify the integrations and monotone/approximation passage. | product projection input sound |
| 256–282 | product-projection density | PASS with wording repair | Orthogonal changes occur only inside deterministic integration geometry, not as rotations of the random product law. Entropy proof should write `sum_{b_i>0}(1-b_i)<=d`, rather than literally summing `1-b_i` over zero weights; this is stronger than needed and preserves the `e^{d/2}` cap. | no constant worsens |
| 283–400 | two-copy decoupling, graph determinant, regularizer, `-1/8` exponent | PASS | Only the designated bank is duplicated; pure phases cancel or are discarded by modulus. Weighted BL/Jacobian determinant and `alpha=(2pi e)^2` give the stated determinant power. Fourth-root accounting yields exponent `-1/8`. | order-five density/order-three half-potential valid |
| 404–525 | square profile, definite/hyperbolic pairs, logarithmic and square-root kernels | PASS | Both signs and both hyperbola branches are retained; changes of variables use original coordinates. The hyperbolic logarithm is averaged against a genuine Schur remainder, not a fictitious conditional density cap. | pivot branches valid |
| 526–581 | nonsymmetric interpolation/completion | PASS | `P=A_{.,T}B^{-1}A_{S,.}` need not be symmetric. Exact row-`S`/column-`T` interpolation implies `R-P` is supported in rows `T` or columns `S`; hence global `rank R<=3r`. On `LxL`, `R=P`, hence restricted rank `<=r`. `D` is diagonal on `L` and exactly zero on the seed. | resolves the most delicate rank bookkeeping |
| 582–619 | spectral-to-volume conversion | PASS | From global rank `3r`, `s_{m-3r}(D)>=1-eps`. With `m=4r+1` this forces `r+1` large diagonal entries, all outside the seed because `D=0` on the seed. Restricted rank `<=r` then contradicts strict diagonal dominance using the stated numerical slack. | `4k-3` threshold is justified |
| 620–790 | no-pivot/pivot assembly, full vs truncated half potentials, scaling | PASS | Baseline pivot lemma first gives a truncated half-potential; the nine-eigenvalue intermediate theorem explicitly adds the outside-unit tail `<=1` before using it as a full potential. The main scalar-pivot step invokes that full version. Pair and no-pivot branches exhaust the alternatives. | s17 theorem closes |

No portion of the pinned manuscript remains `UNCHECKED` in this B20 reconstruction.

## Release issues that are nonfatal

1. State once that density representatives are chosen Borel and clipped into `[0,K]` pointwise when the proof evaluates them pointwise.
2. In the product-projection entropy line replace the ambiguous full sum `sum_i(1-b_i)=d` by `sum_{b_i>0}(1-b_i)<=d` (or explicitly restrict to positive weights).
3. Keep regularity scope explicit: the no-pivot Fourier branches produce `C_0` densities; the global theorem only claims essential boundedness because pivot branches are proved by domination.

## Fresh threshold synthesis

The strongest complete replacement proof currently visible is **multiplicity nine**, not seventeen. Two independently authored reconstructions were inspected:

- fleet02/B14, commit `30525aa82e000f8673dc62e0cd000ed6c9770da4`, gives a rough-law-safe grouped product-Fourier compiler with explicit Gaussian regularization and a complete `s_9` assembly;
- fleet01/B02, commit `de66db60d643a9d2366ba542afb8ea295957438a`, independently gives the same threshold and sharpens the global height constant to `4880`.

I independently checked the dependency-critical parts: complex pushforward domination, Plancherel scaling, approximate-identity limit, weighted Holder exponents, physical product-projection determinant, entropy cancellation, heavy-marginal promotion tree, order-three density, order-two full half-potential, Schur direction counts, pivot constants, and scaling. I found no hidden Gaussian/moment/support/iid/log-concavity, exact-rank, sign, or rotated-independence assumption.

The release-gate statement I support mathematically is therefore:

\[
\boxed{s_9(A)\ge s>0\implies \|p_Q\|_\infty\le 4880\,K^2/s.}
\]

I do **not** self-award an owner-level `independently validated/released` label merely from review counts; that remains a repository governance status distinct from the mathematical PASS above.

## Why nine is the current architectural threshold

The new marginal-free physical order-three receiver pays any literal crossing `M` by

\[
\|p_Q\|_\infty\le C_3 E_3(M)^{-1/6},\qquad C_3=14.818337662843\ldots .
\]

The baseline no-pivot spectral-to-volume theorem produces `V_3(A)>=kappa^3` from `s_{4*3-3}=s_9>=1`; a fair physical cut then supplies `E_3>=4^{-3}kappa^3`. Thus the no-pivot branch is exactly where the present proof architecture spends nine large singular directions. Scalar and pair pivot branches require fewer.

## Multiplicity eight status

**OPEN.** Recent exact work has substantially localized the endpoint rather than solved it. In the unpaid no-pivot `s_8>=1`, `V_3<kappa^3` chamber, determinant-squared completion forces positive invertible overlap-one mass and a dimension-free five-role entropy currency. A stronger recent reduction extracts one literal two-coordinate pair `H_*` with outside-cross determinant

\[
\det(A[H_*,H_*^c]A[H_*,H_*^c]^T)\ge 0.3649442658\ldots,
\]

while the self-block is near singular. The exact-zero self-block is paid continuously (`<5.318`). For an invertible near-singular self-block, the Schur order-two half-potential already cancels the moving logarithmic singularity; the remaining method debt is the nonlogarithmic `6|det K_*|^{-1/2}` term, plus the singular rank-one transition. Therefore neither `E_2`/two-sided collar currency alone nor a critical `|phi(t)|<=U/|t|` estimate proves bounded density.

The precise next obligation is a **uniform near-singular two-anchor receiver** that uses the fixed robust outside-cross determinant while remaining uniform through `det K_*=0`, with arbitrary complement curvature and rough product laws retained. I did not close that endpoint in this run.

## Keeper result

A fresh native inventory showed exactly fleet01 B01–B20, all enabled, hourly-valid, objective-aligned and quiet; no B21/B22 and no duplicate. The 14Z fleet01 lease was acquired create-only. No scheduler mutation was needed. Native assignment, actual worker login evidence and mathematical results remain separate; missing login evidence is not an outage.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN`. Provider thinking usage: `null`/unexposed.
