# account03/B11 — complete fixed-multiplicity audit, r57

**Objective:** `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
**Run:** `20260924T131227Z-account03-B11-fixedmult-r57`  
**Pinned source:** `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
**Source path:** `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`  
**Git blob:** `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
**SHA-256:** `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
**Source size:** 47,883 bytes / 790 lines.

## Verdict

**PASS for the written 17-eigenvalue theorem in this independent worker review.** I found no theorem-breaking gap in the pinned manuscript. This is a mathematical review, not formal verification, journal peer review, or a claim that the unrestricted three-eigenvalue conjecture is solved. The source remains unchanged.

The proved candidate under review is exactly:

> independent real coordinates with densities bounded by `K`; arbitrary real symmetric `A`; arbitrary affine `b,c`; if `s_17(A)>=s>0`, then `X^T A X+b^T X+c` has an essentially bounded density with `||p||_infty<=10000 K^2/s`.

No continuity conclusion is claimed for all branches. The unrestricted `s_3` target remains open.

The repository support package is now complete at the manuscript root: `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json` are all present. The current checker reports a new finite suite passing 534 exact interpolation seeds, 18 exact volume comparisons, 240 numerical Schur threshold cases, and 30 numerical graph-weight cases. Those checks are diagnostics only and are not used as proof premises.

## End-to-end source audit

The line ranges below are those of the pinned 790-line source. `PASS` means I independently reconstructed the implication and checked the hypotheses used downstream.

| Source range / label | Status | Independent check |
|---|---|---|
| 1–80, statement / architecture | PASS | Quantifiers, scaling target, affine terms, arbitrary signs and arbitrary rough product laws are stated consistently. The proof normalizes `K=s=1` only at the final scaling step. The manuscript explicitly avoids rotated-coordinate independence. |
| 91–120, `lem:fourier` | PASS | Plancherel normalization is consistent with `fhat(t)=int e^{itx}f(x)dx`; Gaussian regularization gives `exp(-eps t^2)`. `phi in L1` yields a bounded continuous density via convolution and dominated convergence. The Gaussian identity has the correct `1/(2 sqrt(pi v))` factor. |
| 122–130, `lem:envelope` | PASS | `int min(1,(a/|t|)^p) dt = 2ap/(p-1)` and Fourier inversion gives `ap/[pi(p-1)]`. |
| 132–160, `lem:riesz` | PASS | The gamma representation of `|z|^{-1/2}` and Gaussian inversion lead to the Fourier weight `|t|^{-1/2}/sqrt(2pi)`. The power-envelope integral is `12 sqrt(u)`, hence the stated constant. Tonelli is applied only to nonnegative majorants. |
| 169–181, `lem:rank` | PASS | Both singular-value Lipschitz continuity and the rank-shift inequality follow from the Eckart–Young approximation characterization and do not require symmetry. This is important later because `D+R`, `R`, and `E` can be nonsymmetric. |
| 183–207, `lem:schur` | PASS | Detailed B11 check below. The singular-ambient continuation through `A+eps I` is valid, including the moving threshold `t-|eps|`; no eigenvalue is lost at equality in the limit. |
| 209–217, `lem:dd` | PASS | Standard strict row diagonal dominance contradiction using a largest coordinate of a kernel vector. |
| 221–255, `thm:bl` | PASS | Heat-flow derivative is `F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` by the Parseval-frame condition. Gaussian tails justify integration by parts on compact positive-time intervals. Trace gives `sum c_i=d`; the large-time limit and the `t downarrow 0` Fatou passage are valid. Truncation handles general nonnegative integrable inputs. |
| 258–282, `lem:projection` | PASS | The orthogonal-complement marginal is written in original coordinates. BL exponents `b_i=1-|U^T e_i|^2` form a frame; `f_i^{1/b_i}<=f_i` for `f_i<=1`. Entropy gives `exp(d/2)`. No independence after rotation is asserted. |
| 284–301, `lem:scalar-fourier` | PASS | `|fhat|^{2m}` is integrable because it is bounded by `|fhat|^2`. It is the characteristic function of a sum of `m` independent differences; Fourier inversion at zero and the projection lemma with coefficient norm `sqrt(2m)` give the stated `p^{-1/2}` bound. |
| 310–324, `lem:decoupling` | PASS | Cauchy–Schwarz is applied in the original `X_I` law after integrating `X_J`; expansion with an independent copy produces product Fourier factors. Jensen upgrades power two to power four. Difference coordinates remain independent and cap one. Arbitrary measurable within-bank phases are legitimately discarded only after absolute values. |
| 326–373, `thm:determinant` | PASS | The graph-frame weights satisfy the exact Parseval identity and `theta=sum d_i=sum(1-c_j)`. The BL one-dimensional scaling factors are correct. The scalar Fourier-power bound at exponent `2/d_i` cancels the `d_i` factors. With `alpha=(2pi e)^2`, the entropy factor cancels exactly. Fourth roots give determinant exponent `-1/8` and coefficient `t^2/(pi^2 e^2)`. |
| 376–400, crossing volumes / `cor:vol-fourier` | PASS | Cauchy–Binet gives the determinant coefficient `Z_k`. Retaining a single order yields exponent `k/4`. At `k=5`, exponent `5/4>1` is directly density-integrable; at `k=3`, exponent `3/4` is used only after the Riesz weight, not for density inversion. |
| 404–414, `lem:square` / profile | PASS | The inverse-branch Jacobian is correct and the interval-preimage estimate survives arbitrary translation/linear terms after completing the square. The conditional profile is used as measure domination, not as an independence claim. |
| 423–434, `lem:definite` | PASS | Deterministic orthogonal diagonalization occurs only inside a 2D change of variables for a joint density cap. Polar quadratic coordinates have Jacobian `1/(2 sqrt(det B))`; integrating angle gives `pi M/sqrt(|det B|)`. |
| 437–482, `lem:hyperbola` | PASS | Hyperbolic coordinates have absolute Jacobian `1/(2 sqrt D)`. The two tails are controlled in an original coordinate by monotonicity and the cap-one/mass-one rearrangement against `1/|y|`; the middle interval produces the logarithm. `Lambda>=2/sqrt D` converts to the stated envelope. Exceptional critical levels are handled through test functions/Tonelli. |
| 485–525, `lem:quarter` | PASS | Diagonal-heavy case gives square-root concentration. Otherwise random signs produce an original-coordinate cross block of norm at least `L/4`; one singular factor in the determinant theorem yields `|t|^{-1/4}`. Gaussian smoothing gives the quarter-power small-ball estimate. Layer cake yields the logarithmic potential. No pointwise one-dimensional van-der-Corput claim appears. |
| 528–580, `def:pivot-volume`, `lem:sampling`, `lem:completion` | PASS | Ordered disjoint minors are used consistently. Bordering gives the interpolation error exactly; singular seeds contribute zero and explain why the counting relation is an inequality. `P` need not be symmetric. The support decomposition of `R-P` gives global rank `<=3r`, while `R[L,L]=P[L,L]` gives restricted rank `<=r`; `D` vanishes on `S union T` and `E` has zero diagonal. |
| 582–619, `prop:volume` | PASS | If a volume ratio is small, `||E||<=1/16`. With `m=4k-3`, rank perturbation forces at least `r+1` diagonal entries of `D` of magnitude `>=1-eps` in `L`. The no-pivot entry bound and zero diagonal of `E` then make `R[H,H]` strictly diagonally dominant. Exact slack is `297/2800>0`; this contradicts restricted rank `<=r`. The `r=0` branch gives `||A||<1`. |
| 621–645, `lem:cut`, `cor:no-pivot` | PASS | Each ordered disjoint `k,k` minor crosses a fair cut with probability `4^{-k}`. Together with `k=3,5` volume bounds this gives the stated half-potential and density constants. |
| 654–674, `lem:kernels` | PASS | The two inverse-square-root singularities give only a logarithm. The centered-overlap argument for the logarithmic kernel is valid after layer cake; constants are conservative. |
| 676–714, `prop:pivot-H` | PASS | Scalar pivot uses Schur count to retain one nonzero quadratic direction and the square-profile/log-potential chain. Definite pair is direct. Indefinite pair uses only the proved hyperbolic envelope plus the truncated logarithmic integral. The alternatives exhaust the pivot definition. |
| 716–724, `prop:nine` | PASS | Pivot branch supplies truncated half potential `<=600`; no-pivot branch supplies the full half potential `<200`. Outside distance one the kernel is `<=1`, hence the full potential `<=601`. The distinction between truncated and full potentials is used correctly. |
| 726–749, `thm:main` | PASS | No-pivot `s17` branch closes by order five. Scalar pivot loses one Schur direction, so `s16` remains and the nine-direction half-potential theorem applies. Definite pair is direct. Indefinite pair loses two Schur directions but needs only one residual nonzero direction for the log potential. Final normalization `Y=KX`, `A/s` gives density scaling `K^2/s`. |
| 751–790, threshold accounting / limitations | PASS | The manuscript accurately identifies order five as the only place where the 17-direction count is required and does not claim continuity in all branches or solve the three-direction conjecture. |

No source range remains `UNCHECKED` in this review.

## B11 lens: Schur count, including singular matrices

For

\[
A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix},\qquad
S=D-C^TB^{-1}C,
\]
with an invertible physical pivot `B` of order `k`, the manuscript needs

\[
N_S(t)\ge N_A(t)-k.
\]

When `A` is invertible, block congruence gives `A^{-1}` with complementary principal block `S^{-1}`. Interlacing applied separately to positive and negative eigenvalues of `A^{-1}` yields

\[
\#\{|\lambda(S^{-1})|>t^{-1}\}
\le n-N_A(t),
\]
which is exactly `(n-k)-N_S(t)<=n-N_A(t)`.

For singular `A`, take `A_eps=A+eps I` through invertible values. For `|eps|<t`, every eigenvalue of `A` with modulus at least `t` gives an eigenvalue of `A_eps` of modulus at least `t-|eps|`, so

\[
N_{A_\varepsilon}(t-|\varepsilon|)\ge N_A(t).
\]

The pivot remains invertible for small `eps`; the corresponding `S_eps` converges in operator norm to `S`. Applying the invertible result at `t-|eps|` gives

\[
s_q(S_\varepsilon)\ge t-|\varepsilon|,
\qquad q=N_A(t)-k,
\]
when `q>0`. Ordered singular values are 1-Lipschitz in operator norm, hence `s_q(S)>=t`. This proves the count, including equality at the threshold. If `q<=0` the assertion is vacuous.

A useful stronger signed form also follows by the same inverse-compression argument plus Sylvester inertia:

\[
N_+(S,t)\ge N_+(A,t)-\nu_+(B),\qquad
N_-(S,t)\ge N_-(A,t)-\nu_-(B),
\]
where `N_+(H,t)=#{lambda(H)>=t}`, `N_-(H,t)=#{lambda(H)<=-t}` and `nu_±(B)` are the positive/negative inertias of `B`. The same `eps I` continuation handles singular `A`. The manuscript does not need this sharper signed statement, but it independently checks that the absolute count is conservative rather than over-optimistic.

## Threshold accounting after audit

The Schur bookkeeping is not the source of the number 17:

- scalar pivot: ambient `s_10>=1` already leaves `s_9` in the Schur complement and therefore closes by `prop:nine`;
- definite two-coordinate pivot: direct conditional density bound, no residual spectral direction is needed;
- indefinite two-coordinate pivot: ambient `s_3>=1` leaves one nonzero Schur direction, enough for the logarithmic-potential averaging;
- no-pivot branch: the present leverage-free determinant receiver needs an order-five crossing, and the interpolation theorem reaches order five from `4*5-3=17` directions.

Thus any unconditional reduction below 17 must improve the no-pivot endpoint or add a new receiver. Merely sharpening the Schur loss cannot lower the global threshold.

## Lower-threshold progress in this run

A separate immutable improvement in this run proves `QFORM-S16-TRANSVERSE-CARRIER-v1`. It strengthens the existing `s16` endpoint reduction: after replacing a volume-good crossing by its top-rank-four part, the eight same-bank near-unit modes can be forced **orthogonally to the old four-dimensional crossing carriers**, not merely somewhere inside the two same-bank blocks. This removes the previously stated possibility that the second crossing is entirely aligned with the first carrier. It still does not by itself prove the 16-eigenvalue density theorem because a product-preserving physical repartition must simultaneously retain enough of the old order-four volume and expose a fifth transverse crossing direction.

## Final review status

- Baseline 17-eigenvalue theorem: **PASS in this review**.
- Pinned source modified: **no**.
- Full three-eigenvalue conjecture: **OPEN**.
- Full continuity conclusion: **OPEN outside the branches where `phi in L1` was proved**.
- New unconditional multiplicity theorem below 17: **not claimed**.
- Two separate complete reviews required before any independent-validation/release claim: **still required by owner gate**.
