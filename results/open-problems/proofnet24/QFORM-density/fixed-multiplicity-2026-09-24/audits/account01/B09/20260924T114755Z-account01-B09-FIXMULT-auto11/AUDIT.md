# account01/B09 independent audit — QFORM-FIXED-MULTIPLICITY-AUDIT-20260924

Run: `20260924T114755Z-account01-B09-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned manuscript source: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`

## Verdict

**Mathematical verdict: PASS on the complete pinned 790-line proof, with no fatal or theorem-changing gap found.**

This is one independent end-to-end review, not a self-awarded release certificate. The owner requires two genuinely separate complete reviews before independent-validation status. I do **not** claim the unrestricted three-eigenvalue conjecture. I also do not claim that 17 is optimal.

The theorem checked is exactly: independent real coordinate densities `<=K`; arbitrary real symmetric `A`; arbitrary affine `b,c`; if `s_17(A)>=s>0`, then `X^T A X+b^T X+c` has an essentially bounded density with

`||p||_infinity <= 10000 K^2/s`.

The no-pivot branch actually produces a continuous density by integrable Fourier inversion; the pivot branches are proved as measure/density domination statements and the manuscript correctly refrains from asserting global continuity.

## Repository/reproducibility status

At the fresh manuscript root inspected during this run, `manuscript.tex`, `README.md`, `AUDIT.md`, and peer audit directories were present. The files named by the README/current objective as `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` were **not present**. Therefore the finite checker claimed by the authoring self-audit could not be independently rerun from this repository root in this run. This is a packaging/reproducibility GAP, not a mathematical dependency gap: the complete specialized proof is in `manuscript.tex`.

## End-to-end audit matrix

| Source range | Statement / dependency | Verdict | Independent check |
|---|---|---|---|
| 1–83 | definitions, theorem quantifiers, normalization architecture | PASS | `s_j` is singular value; for symmetric `A` this matches absolute eigenvalues. The target scaling in `K,s` is consistent with the final rescaling. |
| 84–151 | Fourier normalization, Gaussian inversion, power envelope, Riesz half potential | PASS | Constants match the stated Fourier convention. The Riesz gamma calculation gives the displayed `(2pi)^(-1/2)` coefficient and the `12 sqrt(u/(2pi))` envelope. |
| 152–220 | singular-value perturbation, Schur spectral count, diagonal dominance | PASS | Rank perturbation is valid for nonsymmetric auxiliaries. The Schur count is correctly obtained from the principal compression `S^{-1}` of `A^{-1}` and then by a singular limiting argument. |
| 221–300 | geometric Brascamp--Lieb heat flow, projection densities, scalar Fourier powers | PASS | Heat-flow sign and limiting Gaussian normalization are correct. Product-projection proof never asserts rotated independence. In the `b_i=0` case the displayed `sum_i(1-b_i)=d` is read over all rows; the omitted rows have `-b log b=0<=1-b`, so the bound remains exact as written. |
| 301–399 | decoupling, regularized crossing determinant, volume envelopes | PASS | Both decoupling powers have correct independence provenance. The graph-BL Jacobian/scales and `alpha=(2pi e)^2` cancel exactly, yielding determinant exponent `-1/8`; k=5 gives exponent `5/4`, k=3 gives the weighted `3/4` half-potential exponent. |
| 401–535 | scalar square, definite pair, hyperbolic pair, quarter-power concentration | PASS | All coordinate conditioning is on original variables. Hyperbolic tails use a physical coordinate only after deterministic diagonalization of the level-set geometry. Quarter-power bound correctly switches between a diagonal pivot and a random physical cut. |
| 536–630 | disjoint volumes, sampled interpolation, completion, spectral-to-volume proposition | PASS | Detailed B09 audit below. The nonsymmetric support bookkeeping, global `rank R<=3r`, restricted `rank R[L,L]<=r`, zero diagonal of `E`, and `D=0` on the seed are all used correctly. |
| 631–730 | random cut, no-pivot analytic consequences, singular kernels, pivot half-potential | PASS | Ordered disjoint-minor expectation gives exactly `4^{-k}`. Full versus truncated half potentials are kept distinct. Pair/scalar pivot bounds use the exact surviving Schur spectral count. |
| 731–790 | nine-eigenvalue half potential, main theorem branches, general scaling, limitations | PASS | Scalar-pivot branch uses `s_16` of the Schur complement and hence the proved nine-direction bound; pair branch leaves 15 directions. Rescaling `Y=KX` gives `Q=(s/K^2) Qtilde`, hence `10000 K^2/s`. |
| bibliography / priority attribution | classical antecedent descriptions | UNCHECKED | Not a dependency of the self-contained proof. This run did not perform a primary-source novelty/priority audit. |
| external compilation / advertised finite suite | LaTeX build and `verify.py` checks | UNCHECKED | Supplementary checker/source-manifest files were absent from the inspected repository root. |

## B09 lens: spectral rank perturbation and diagonal-dominance contradiction

The critical argument in `prop:volume` is source-valid.

Assume a bad ratio at order `r`, `1<=r<=4`. The sampled completion gives

`A=D+R+E`,

with

`rank R<=3r`, `rank R[L,L]<=r`, `D=0` on the seed, `diag(E)=0`, and

`epsilon:=||E||_F <= (r+1) sqrt(kappa) <= 1/16`, because `kappa=1/80^2`.

For `m=4k-3`, singular-value perturbation and the rank shift give

`s_m(D+R)=s_m(A-E)>=1-epsilon`,

and hence

`s_{m-3r}(D)>=1-epsilon`.

Since `r<=k-1`,

`m=4k-3 >= 4r+1`,

so `m-3r>=r+1`. Therefore at least `r+1` diagonal entries of `D` have modulus at least `1-epsilon`; because `D` vanishes on `S union T`, all these entries lie in `L`.

On an `(r+1)`-set `H` of such coordinates,

`|R_ii| >= 1-epsilon-eta >= 371/400`,

while no-pivot entry control and `|E_ij|<=||E||_F` give

`|R_ij| < 1/7+1/16 = 23/112` for `i!=j`.

As `r<=4`, every row has off-diagonal sum

`< 4*(23/112)=23/28`,

and the exact strict slack is

`371/400 - 23/28 = 297/2800 > 0`.

Thus `R[H,H]` is strictly diagonally dominant and invertible, so its rank is `r+1`; but `H subset L` and `rank R[L,L]<=r`, contradiction. No symmetry of `R` or `E` is used or needed. The proof uses singular values of the nonsymmetric `A-E`, exactly as required.

The `r=0` branch is also correct: `V_1=||off(A)||_F^2<kappa`, so

`||A|| <= ||diag A||+||off A|| < 1/100+1/80 < 1`,

contradicting any singular value at least one.

## Why the nonsymmetric rank bounds cannot simply be improved

A direct algebraic witness shows that the completion lemma's pair of bounds is simultaneously sharp already at `r=1`.

Take seed `S={1}`, `T={2}`, `L={3}` and a symmetric matrix

`A=[[0,b,c],[b,0,d],[c,d,a]]`

with `b c d !=0`. Then `B=A[S,T]=b` and

`P=A[:,T] B^{-1} A[S,:]`.

Because `L` is one-dimensional, `F=off(A[L,L]-P[L,L])=0`, so `E=0`. The completion gives

`R=[[0,b,c],[b,0,d],[c,d,dc/b]]`.

Its determinant is exactly `b c d`, hence `rank R=3`, while

`R[L,L]=[dc/b]`

has rank one. Direct sums give equality `rank R=3r` and `rank R[L,L]=r` for arbitrary `r`. Therefore a threshold reduction cannot come merely from replacing the two displayed rank bounds by `2r` and `r-1` using the same support argument. Additional spectral/no-pivot structure or a different analytic receiver would be required.

This witness is a sharpness statement for the interpolation algebra only; it is not a counterexample to the density theorem and does not prove the threshold 17 optimal.

## Threshold-reduction audit

The present proof's order-five no-pivot density branch has a precise terminal obstruction at `r=4`.

- With `s_17(A)>=1`, global rank `<=12` leaves at least `17-12=5` large diagonal directions. Five exceed restricted rank four, and diagonal dominance closes the contradiction.
- With only `s_16(A)>=1`, the same argument guarantees only `16-12=4` large diagonal directions. A `4x4` diagonally dominant block has rank four, which is **compatible** with `rank R[L,L]<=4`; the contradiction disappears.

Thus **no 17 -> 16 improvement is proved in this run**. More strongly, the current B09 interpolation/rank argument cannot obtain it by a numerical tightening of `eta`, `kappa`, or the diagonal-dominance slack alone. A 16-eigenvalue theorem needs new structure in this terminal `r=4` saturation chamber, a stronger analytic conclusion from lower crossing order, or a different decomposition.

A potentially promising but not completed route is to replace the fourth-power decoupling in the determinant theorem by second-power decoupling on a low-leverage cross frame. That would double the determinant exponent from `-1/8` to `-1/4` and make order-three crossing volume integrable. However a bare no-pivot entry bound does not itself control the requisite ridge leverages, so this is **not** recorded as an improvement theorem.

## Final dependency status

No proof step in the pinned 17-eigenvalue manuscript depends on the refuted arbitrary-joint coarea claims, on post-rotation independence, on bounded support/moments/log-concavity, or on a pointwise van-der-Corput estimate for arbitrary rough densities. The proof remains within the stated product-law hypotheses.

**Release status after this review:** one complete independent PASS from account01/B09, but not enough by itself to satisfy the owner's two-separate-full-review gate. Full three-eigenvalue target remains OPEN.
