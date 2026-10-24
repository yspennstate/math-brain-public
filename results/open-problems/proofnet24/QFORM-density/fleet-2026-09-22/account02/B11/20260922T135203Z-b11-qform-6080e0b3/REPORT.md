# account02/B11 — heavy-coordinate minority-Rayleigh reduction for indefinite rank three

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Control revision:** 2026-09-22.5  
**Run:** 20260922T135203Z-b11-qform-6080e0b3  
**Assignment:** Indefinite signatures  
**Status:** ESSENTIAL_STEP_APPLIED / FULL CONJECTURE OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## First unpaid implication attacked

The previous B11 run proved a uniform bound for a heavy-Walsh family but left arbitrary heavy-row exact-rank-three frames unpaid because the two null factors of the opposite-sign plane need not split across disjoint original-coordinate banks. The first missing implication was therefore to identify a dimension-free branch in an arbitrary genuinely rotated heavy-row frame, without assuming post-rotation independence or selecting one well-conditioned physical principal triple.

This report closes the **minority-Rayleigh heavy-coordinate branch away from the null cone** and shows that the only remaining minority-heavy obstruction is quantitatively near-isotropic and necessarily exports a macroscopic physical cross row.

## Sources and live corrections consumed

1. Assigned partner account03/B11, canonical report `yspennstate/math-open-problems@860d849b7f2e0198bf7c3531a71b14e59f03e430`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T121353Z-account03-B11-QFORM-r11/REPORT.md`. I use its dependence-safe Abel smoothing principle and retain its warning that the opposite-sign binary law may have logarithmically unbounded density while its one-sided half-potential is bounded.
2. account01/B08 fractional-frame Brascamp--Lieb handoff, canonical report `yspennstate/math-open-problems@ee1aca0375b477075657b02ab0e2096c`, supplying the same sharp Hausdorff--Young / geometric Brascamp--Lieb normalization used below. (The linear-projection lemma is reproved here.)
3. Regularized-determinant supporting theorem `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`; it closes diffuse entire-range geometry but not the heavy-coordinate bridge.
4. Live correction inbox at brain control commit `da63bbaba29461947597c208482f78df70fb4e59`, including `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`. No conditional-cap claim for a conjugate rotated pair is used below.

## 1. A two-dimensional projection-density lemma

### Lemma 1 — isotropic two-dimensional linear projections

Let `X_i` be independent real random variables with densities `f_i<=1`. Let `b_i in R^2` satisfy

`sum_i b_i b_i^T = I_2`,

and put `W=sum_i b_i X_i`. Then `W` has a density satisfying

`||p_W||_infinity <= e`.

The statement is invariant under an orthogonal rotation of the target plane; no rotation of the independent input coordinates is performed.

### Proof

First record the one-dimensional companion: if `Y=sum_i a_i X_i` and `sum_i a_i^2=1`, then

`||p_Y||_infinity <= sqrt(e)`.

If one coefficient has `a_k^2>1/2`, condition on all other variables; `a_k X_k` has density at most `1/|a_k|<sqrt(2)<sqrt(e)`. If all `c_i=a_i^2<=1/2`, use the `2pi`-normalized Fourier transform. Sharp Hausdorff--Young with `p_i=1/c_i`, `q_i=1/(1-c_i)` gives

`int |fhat_i(s)|^(1/c_i) ds <= c_i^(1/2) (1-c_i)^(-(1-c_i)/(2c_i))`.

After the scaling `s -> sqrt(c_i)s`, weighted Holder with weights `c_i` gives

`int |phihat_Y(t)| dt <= product_i (1-c_i)^(-(1-c_i)/2)`.

Since `-(1-c)log(1-c)<=c` and `sum c_i=1`, the product is at most `sqrt(e)`. Fourier inversion proves the one-dimensional claim.

Now write nonzero `b_i=sqrt(c_i)u_i`, `||u_i||=1`, so `sum c_i u_i u_i^T=I_2` and `sum c_i=2`.

If every `c_i<=1/2`, geometric Brascamp--Lieb with weights `c_i`, combined with exactly the same sharp Hausdorff--Young calculation, yields

`int_{R^2} |phihat_W(t)| dt <= product_i (1-c_i)^(-(1-c_i)/2) <= exp((1/2)sum_i c_i)=e`.

Hence `||p_W||_infinity<=e`.

If instead some `c_1>1/2`, rotate the two-dimensional target so `b_1=sqrt(c_1)e_1`. Write `W=(U,V)`. The second coordinate `V` depends only on `X_i,i>1` and its coefficient squares sum to one, so the preceding one-dimensional result gives `||p_V||_infinity<=sqrt(e)`. Given `V=v`, `X_1` remains independent of the conditional residual variables, and

`U=sqrt(c_1)X_1 + (residual translation)`.

Thus the conditional density of `U|V=v` is a mixture of translations of the density of `sqrt(c_1)X_1`, hence at most `1/sqrt(c_1)<sqrt(2)`. Therefore

`p_{U,V}(u,v)<=sqrt(2e)<e`.

This proves the lemma. QED.

The point of the high-leverage case is that conditioning is only on a function of the *other original coordinates*; it does not assert any bounded conditional density for a conjugate sum/difference pair.

## 2. Heavy-coordinate minority-Rayleigh theorem

Let the ambient quadratic form have exact rank three,

`A=R Lambda R^T`, `R^T R=I_3`,

where `Lambda` has inertia `(2,1)` or `(1,2)` and all three nonzero eigenvalues satisfy `|lambda_j|>=1`. Let row `r_0` of `R` have leverage

`c=||r_0||^2 >= 1/2`.

Choose an orthogonal change of coordinates **inside the three-dimensional spectral space only** so that `r_0=sqrt(c)e_1`; write the conjugated spectral matrix as

`H = [[a,h^T],[h,C]]`.

This changes no original input coordinate and hence makes no independence claim. Call `a` a *minority-sign Rayleigh quotient* when `a<0` in inertia `(2,1)`, or `a>0` in inertia `(1,2)`.

### Theorem 2 — minority-heavy branch away from the null cone

For every `delta>0`, if `a` has the minority sign and `|a|>=delta`, then for arbitrary independent input densities bounded by one,

`||p_{X^TAX}||_infinity <= 2 sqrt(2 pi e) delta^(-1/4)`.

In particular, with `delta=1/4`,

`||p_{X^TAX}||_infinity <= 4 sqrt(pi e) < 11.690`.

The order-dual signature `(1,2)` follows by replacing `A` by `-A`, so it suffices to prove inertia `(2,1)` and `a<0`.

### Proof

Let the rotated spectral linear coordinates be `(Z_1,W)` with `W in R^2`. Since the first physical row is exactly `sqrt(c)e_1`,

`Z_1 = sqrt(c) X_0 + L_0(X_{i>0})`.

The transverse row vectors of the remaining coordinates satisfy

`sum_{i>0} b_i b_i^T=I_2`.

Hence Lemma 1 gives

`||p_W||_infinity <= e`.

Because `a<0` is the minority sign, Sylvester inertia additivity makes the Schur complement

`S=C-hh^T/a`

positive definite. Completing the square in the spectral first coordinate gives

`Q = a V^2 + W^T S W`,

where

`V = Z_1 + h^T W/a`.

Conditional on `W`, the random variable `V` is a mixture of translations of `sqrt(c)X_0`; therefore

`||p_{V|W}||_infinity <= c^(-1/2) <= sqrt(2)`.

This is exactly the dependence-safe conditioning pattern in the assigned partner's Abel-smoothing lemma. Since `R_0=W^T S W>=0`, its density is bounded by a direct polar-coordinate/coarea calculation. Set `U=S^(1/2)W`; then

`||p_U||_infinity <= e/sqrt(det S)`,

and for `r>0`,

`p_{R_0}(r) <= pi e/sqrt(det S)`.

For any probability density `g<=M`, decreasing rearrangement of the one-sided inverse-square-root kernel gives

`sup_t int_t^infinity (r-t)^(-1/2) g(r) dr <= 2 sqrt(M)`.

Therefore

`sup_t E[(R_0-t)_+^(-1/2)] <= 2 sqrt(pi e) (det S)^(-1/4)`.

Apply the partner's conditional Abel smoothing with coefficient `a<0` and conditional density cap `c^(-1/2)`:

`||p_Q||_infinity <= 2 sqrt(pi e) c^(-1/2) |a|^(-1/2) (det S)^(-1/4)`.

Now `det H = a det S`, so

`|a|^(-1/2)(det S)^(-1/4)=(|a| |det H|)^(-1/4)`.

Because all three eigenvalue magnitudes of `H` are at least one, `|det H|>=1`. Using `c>=1/2` yields

`||p_Q||_infinity <= 2 sqrt(2 pi e) |a|^(-1/4) <= 2 sqrt(2 pi e) delta^(-1/4)`.

QED.

## 3. What remains in the minority-heavy branch

The theorem shows that any sequence of exact-rank-three indefinite examples with a heavy row and unbounded output-density norm cannot stay in a minority-sign region with `|a|>=delta` for any fixed `delta>0`. A putative bad sequence in this branch must drive the heavy spectral direction to the indefinite null cone:

`a -> 0`.

This is not weak coupling. Since every eigenvalue of `H` has magnitude at least one,

`H^2 >= I_3`.

Hence, writing `H e_1=(a,h)`,

`a^2+||h||^2=(H^2)_{11}>=1`.

Thus if `|a|<1/4`,

`||h||^2>15/16`.

Moreover the physical cross row from the heavy coordinate obeys

`sum_{j!=0} A_{0j}^2 = (A^2)_{00}-A_{00}^2
 = c (H^2)_{11}-c^2 a^2
 >= c(1-ca^2)`.

For `c>=1/2` and `|a|<1/4`, this is at least `31/64`. Therefore the unresolved near-null heavy branch necessarily carries an original-coordinate cross vector of Euclidean norm at least `sqrt(31)/8`.

This is the first unpaid implication after this run: exploit that **macroscopic one-row bilinear export plus the two-dimensional isotropic residual frame** without assuming bounded conditional density for a conjugate residual pair, and without requiring a rank-three physical cross cut (which the live correction already refutes as an exhaustive dichotomy).

## 4. Exact null-cone construction: the residual chamber is real

Heavy leverage alone does not keep the minority Rayleigh quotient away from zero. For any `c in (1/2,1)`, take

`H0=[[0,0,1],[0,1,0],[1,0,0]]`,

whose eigenvalues are `1,1,-1`, and the physical frame rows

`t0=(sqrt(c),0,0)`,
`t1=(sqrt(1-c),0,0)`,
`t2=(0,1,0)`,
`t3=(0,0,1)`.

The columns are orthonormal and the heavy row has leverage `c`, but its Rayleigh quotient is exactly zero. The resulting form is

`Q=2( sqrt(c)X0 + sqrt(1-c)X1 ) X3 + X2^2`.

This retains the mandatory opposite-sign rank-two logarithmic control: deleting the `X2^2` term leaves a saddle/product law that can have a logarithmically unbounded density for bounded-density uniforms. The third direction is exactly the square `X2^2`; in this simple banked construction it removes the singularity by the assigned partner's half-potential/Abel mechanism. In a general high-projective-complexity frame, the residual square direction and the saddle factor are entangled across the same original coordinates, which is precisely the unresolved near-null problem.

For `c=3/4`, the physical matrix is

`[[0,0,0,sqrt(3)/2],
  [0,0,0,1/2],
  [0,0,1,0],
  [sqrt(3)/2,1/2,0,0]]`,

with spectrum `{-1,0,1,1}` and heavy-row cross squared norm `3/4`.

This construction is a counterexample only to the stronger structural shortcut "heavy leverage forces a minority pivot bounded away from the null cone". It is not a QFORM counterexample.

## 5. Exact checker

`verify_heavy_minority.py` algebraically checks 2000 seeded random conjugates with eigenvalue magnitudes in `[1,5]`: 577 minority-sign cases satisfy positive-definite Schur complement, the determinant identity, `H^2>=I`, and the near-null cross inequality; 71 of those are in `|a|<1/4`. It also checks the exact `c=3/4` null-cone construction. Terminal marker:

`QFORM_HEAVY_MINORITY_RAYLEIGH_CHECK_PASS`.

Checker SHA-256: `9f03056ea6ae5aa5cedaeac835b0a58c1f0003e5d4a0a2f3bce5d21d68edf3c1`.  
Captured-output SHA-256: `0f4cb44c10663b5d6ba1514614d4b05e925ab85aa286eb004de0cc13f97a9646`.

This is regression of the algebraic inequalities, not finite-census closure.

## 6. Relation to the full target

Paid here: an arbitrary-size, arbitrary-law, genuinely rotated exact-rank-three indefinite branch with a heavy coordinate, minority-sign spectral Rayleigh quotient, and fixed separation from the null cone. No moments, support bounds, centering, continuity, or rotated-coordinate independence are used.

Still unpaid:

1. the heavy **majority-sign** branch, where the Schur complement is indefinite and the rank-two logarithmic singularity is the central issue;
2. the **minority near-null** branch `a≈0`, now known to have macroscopic heavy-row cross coupling;
3. arbitrary extra spectrum outside the selected three large eigenvalues, whose nonseparable contribution cannot simply be conditioned away.

Thus the full QFORM conjecture remains open. A next useful mechanism is a source-valid inequality for the canonical near-null form `2 Z_1 Z_3 + Z_2^2` under an arbitrary three-dimensional Parseval projection of product densities, retaining original-coordinate provenance throughout.
