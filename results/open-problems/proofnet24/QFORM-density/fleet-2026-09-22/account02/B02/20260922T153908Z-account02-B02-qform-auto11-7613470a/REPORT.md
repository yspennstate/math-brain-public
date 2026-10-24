# account02/B02 — ridge-extension review and square-pivot ridge effective-dimension theorem

Run: `20260922T153908Z-account02-B02-qform-auto11-7613470a`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Integrated Fourier estimate  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval was used, but no native learned-memory receiver ingestion was verified.

## 1. Full target and first unpaid implication

The full target remains: for arbitrary dimension, independent real coordinates with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues satisfying `|lambda|>=1`, prove a universal essential bound on the density of `Q=X^T A X`, or give a valid counterexample. No moments, sign restriction, connected support, diagonal basis, or independence after rotation may be assumed.

The new ridge-window theorem solves a broad diffuse spectral-window branch, but the bare spectral hypothesis does not force its ridge certificate. The first unpaid implication for this Fourier route is therefore an exhaustive product-preserving reduction that combines: (i) direct ridge effective dimension, (ii) one physical scalar pivot plus residual ridge effective dimension, and (iii) already-proved low-cross-rank coordinate-bank/star mechanisms. The live `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, and `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1` corrections prohibit replacing this by a fixed local-minor dichotomy.

## 2. Sources actually consumed

1. Ridge-window proof: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, path `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`, blob `1241fa7ba9a36a91bc75f047677f2daac764c2bf`.
2. Starting regularized-determinant proof: `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, path `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`, blob `080253f929411bfa9c7aa3254a2bdaf37be72ebb`.
3. Named partner `account03/B02`: `QFORM-SQUARE-PIVOT-EK-INTEGRATED-v1`, canonical report `yspennstate/math-open-problems@c080587ef3f1458c8d1fecff9083d5a8c0d0f6bb`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T142939Z-account03-B02-QFORM-r11b/REPORT.md`, blob `71062ff6ea33339bd22bb0509400d19afc4be746`.
4. W. Beckner, *Inequalities in Fourier analysis*, Ann. Math. 102 (1975), 159–182, DOI `10.2307/1970980`, for sharp Hausdorff–Young/Young constants.
5. G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, for the normalized rank-one geometric Brascamp–Lieb formulation used by the ridge proof.

No target-level conclusion is inferred from numerical checks or from source existence.

## 3. Independent scoped review of the free-regularizer ridge extension — PASS

Review scope requested by current control: the free-`alpha` multiplier, the frequency-dependent choice, the effective exponent, and Fourier inversion in Sections 3–5 of the ridge-window report. I did not review the separate MSS/spectral-window perturbation package assigned to account03/B04.

### 3.1 Scalar Fourier norm

For `1<=q<=2` and `0<d<=q/2`, set `h=|hat f|^q`. With Fourier exponent `q/d>=2`, the conjugate input exponent is `q/(q-d) in [1,2]`. Sharp Hausdorff–Young gives

`||h||_(1/d)=||hat f||_(q/d)^q`

`<= (2pi)^d q^(q/2-d) (q-d)^(-(q-d)/2) d^(d/2)`.

The powers of `q`, `q-d`, and `d` agree with the report. The restriction `d<=q/2` is exactly the condition putting the input exponent at most two.

### 3.2 The easily lost `alpha` multiplier

For `M=alpha I+a^2 R R^T`, define

`c_i=alpha e_i^T M^(-1)e_i`, `d_j=a^2 r_j^T M^(-1)r_j`, `theta=sum_j d_j=sum_i(1-c_i)`.

After `x=M^(-1/2)z`, the `g_i` argument has scale `sqrt(c_i/alpha)`. Its Brascamp–Lieb scalar integral therefore contributes

`alpha^(c_i/2)c_i^(-c_i/2)||g_i||_(1/c_i)`.

Keeping this factor and inserting the sharp scalar estimates yields

`det(M)^(-1/2) alpha^((m-theta)/2) (2pi)^theta prod_i G(c_i) prod_j H_q(d_j)`.

The tangent inequalities give total exponential factor `exp((1-log(2q)/2)theta)`. Since `det(M)=alpha^m det(I+a^2RR^T/alpha)`, the surviving multiplier is exactly

`[pi e sqrt(2/q)/sqrt(alpha)]^theta`.

Thus the report's

`E prod_j |hat f_j(a r_j dot D)|^q <= det(I+a^2RR^T/alpha)^(-1/2)(L_q/sqrt(alpha))^theta`,

with `L_q=pi e sqrt(2/q)`, has the correct `alpha` power and constant.

### 3.3 Frequency-dependent choice and orientation

For an original-coordinate cross block `B=A[I,J]`, the proof uses `R=B^T`, `a=2t`, and

`alpha=(2 gamma |t|)^2`.

Then

`a^2 r_i^T(alpha I+a^2R R^T)^(-1)r_i`

is the `i`th diagonal entry of

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`.

The determinant is exactly `D_gamma=det(I+BB^T/gamma^2)` by the nonzero-spectrum identity for `B^T B` and `BB^T`. Hence both the graph weights and their sum `theta=tr K_gamma` are independent of frequency. The projection/ridge operator lives on the `I` side, matching the physical coordinates whose Fourier factors appear after Cauchy–Schwarz.

### 3.4 Effective exponent and inversion

Taking the `(2q)`th root gives

`|phi(t)| <= D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q))`.

With `beta=theta/(2q)` and

`t0=L_q/(2 gamma) D^(-1/(2theta))`,

this is `|phi(t)|<=min(1,(t0/|t|)^beta)`. For `theta>2q`,

`int_R |phi(t)| dt <= 2 t0 beta/(beta-1)=2t0 theta/(theta-2q)`.

Under the convention `p=(2pi)^(-1) check(phi)`, Fourier inversion therefore gives

`||p||_infinity <= e/[sqrt(2q) gamma] * theta/(theta-2q) * D^(-1/(2theta))`.

Finally `log D=sum log(1+x_j)>=sum x_j/(1+x_j)=theta`, so the simplified factor is at most `e^(-1/2)`. All constants and inequality directions check. **Scoped review result: PASS.**

## 4. New theorem: a physical square halves the ridge effective-dimension threshold

### Theorem `QFORM-SQUARE-PIVOT-RIDGE-EFFECTIVE-DIM-v1`

Write one genuine original coordinate as

`A=[[d,a^T],[a,C]]`, with `d!=0`,

and complete the physical square

`Q=d(Z+a^T W/d)^2+R(W)`, `R(W)=W^T S W`, `S=C-aa^T/d`.

Choose disjoint original-coordinate sets `I,J` among the coordinates of `W`, put `B=S[I,J]`, and for `gamma>0` define

`K=BB^T(gamma^2 I+BB^T)^(-1)`, `theta=tr K`, `D=det(I+BB^T/gamma^2)`.

Let `1<=q<=2`. Assume

`max_i K_ii <= q/2` and `theta>q`.

Then for every

`max(1,2q/theta)<r<2`,

`Q` has an essentially bounded density and

`||p_Q||_infinity`

`<= P(r) sqrt(e) 2^(-1/4) q^(-1/4) |d|^(-1/2) gamma^(-1/2)`

`   * D^(-1/(4theta)) * sqrt(r theta/(r theta-2q))`,

where

`P(r)=4(2-r)^((r-3)/2) r^(-r/2)`.

Since `log D>=theta`, the simpler bound

`||p_Q||_infinity`

`<= P(r) e^(1/4) 2^(-1/4) q^(-1/4) |d|^(-1/2) gamma^(-1/2)`

`   * sqrt(r theta/(r theta-2q))`

also holds.

This is an essential-density statement. Continuity is not claimed from this argument.

### Proof

The reviewed ridge estimate applies to the Schur remainder `R` and gives

`|phi_R(t)|<=min(1,(t0/|t|)^beta)`,

where

`beta=theta/(2q)`, `t0=L_q/(2gamma) D^(-1/(2theta))`.

For the chosen `r`, `r beta>1`, hence

`||phi_R||_r^r <= 2 t0 * r beta/(r beta-1)`

`=2 t0 * r theta/(r theta-2q)`.

Let `p=r/(r-1)>2`. Inverse Hausdorff–Young yields an actual `L^p` density for `R` with

`M:=||p_R||_p <= (2pi)^(-1/r)||phi_R||_r`.

The named partner account03/B02 proved the dependence-safe physical-square potential estimate: from the original-coordinate independence of `Z` and `W`, without assuming the shift is independent of `R`,

`p_Q(t)<=|d|^(-1/2) int p_R(s)|t-s|^(-1/2) ds`

and therefore

`||p_Q||_infinity <= |d|^(-1/2) P(r) M^(r/2)`.

Substitute the `L^r` bound. Since

`M^(r/2) <= (2pi)^(-1/2)[2t0 r theta/(r theta-2q)]^(1/2)`,

and `L_q=pi e sqrt(2/q)`, the displayed constant follows exactly. The only threshold needed is `theta>q`, because some `r<2` with `r theta>2q` exists precisely then. QED.

### Interpretation

Direct ridge Fourier inversion requires `theta>2q`. A single genuine physical square lowers the effective-dimension threshold to `theta>q`. This is the ridge analogue of the named partner's aggregate-determinant theorem, but it remains meaningful for full-rank cross blocks with arbitrarily many small singular directions.

Equivalently, at a fixed ridge scale a sufficient certificate is: choose `q in [1,2]` with `q>=2 max_i K_ii` and `q<theta`. In the common `q=1` branch this is simply `max_i K_ii<=1/2` and `theta>1`.

## 5. Concrete rank-two ridge corollary

Assume the Schur cross block `B` has at least two singular values at least `sigma>0`. Set

`gamma=sigma/sqrt(2)`.

Then `theta>=4/3`. If also `max_i K_ii<=1/2`, choose `q=1` and `r=9/5`. The simplified theorem gives

`||p_Q||_infinity < 19.470 / sqrt(|d| sigma)`.

Indeed `r theta/(r theta-2)<=6` at the worst case `theta=4/3`, and

`P(9/5)=6.190086805899961...`.

This closes a two-cross-direction branch that the direct ridge theorem cannot close: with only two effective directions one always has `theta<2` at positive `gamma`, so direct `q=1` Fourier inversion cannot satisfy `theta>2`.

## 6. Target-class stress family showing a genuine gain

Let `m` be divisible by four. Let `U` be the `m x 2` flat orthonormal frame with columns the normalized all-ones vector and the normalized half-plus/half-minus vector, and put `B=UU^T`. Consider

`A=diag(1, [[0,B],[B^T,0]])`.

This is an exact target-class matrix: its nonzero eigenvalues are `1,+1,+1,-1,-1`. Use the first coordinate as the physical pivot `d=1`. The Schur remainder is the displayed bipartite block. At `gamma=1/sqrt(2)`,

`K=(2/3)UU^T`, `theta=4/3`, `max_i K_ii=4/(3m)<=1/2` for `m>=4`, and `D=9`.

Thus the new theorem applies although the direct ridge density criterion fails (`theta=4/3<2`). Using the actual determinant factor rather than only `log D>=theta` gives

`||p_Q||_infinity <= 16.558`

for this family at `r=9/5`. The more robust singular-value-only corollary gives `<19.470`.

This family is already covered by other bank/aggregate results, so it is not a new target subclass. Its role is decisive mechanism testing: the new square-pivot ridge theorem succeeds exactly in a rank-two effective-dimension regime excluded by direct ridge `L^1` inversion.

## 7. What remains open

No counterexample to a target-wide uniform `||phi_Q||_1` bound was found. The stronger global Fourier criterion therefore remains open, not refuted. The present theorem continues toward bounded density after direct Fourier inversion loses one effective dimension.

The first structural implication still unpaid is an exhaustive product-coordinate decomposition from only the three-large-eigenvalue hypothesis into one of:

1. a direct ridge certificate `theta>2q`;
2. a physical pivot plus residual ridge certificate `theta>q` as above; or
3. a proved low-cross-rank bank/star/hyperbolic-square branch.

The existing correction families show that neither a fixed good minor nor a universal rank-three cross cut can be assumed. Shared-coordinate provenance must be preserved throughout.

## 8. Computation and reproducibility

`checks.py` and `check_results.json` in this immutable run directory check:

- the identity between the frequency-dependent graph weights and `diag K_gamma` on random matrices/frequencies;
- the determinant identity under `alpha=(2gamma|t|)^2`;
- the exact integral `int min(1,(t0/|t|)^beta)^r dt=2t0 r beta/(r beta-1)`;
- the flat rank-two family for `m=4,8,16,32`;
- the constant `19.469104895082328`.

The output ends `ALL_CHECKS_PASS`. Maximum floating errors were approximately `1.0e-15` for the ridge-weight identity, `8.8e-11` for the determinant identity, and `3.6e-11` for numerical envelope integration. These are regression checks only; the proof above is analytic.

## 9. Status

`ESSENTIAL_STEP_APPLIED`.

The ridge-window free-regularizer/effective-exponent/inversion extension receives a scoped independent **PASS** from account02/B02. The new `QFORM-SQUARE-PIVOT-RIDGE-EFFECTIVE-DIM-v1` theorem is proved in its stated scope and directly applies the named account03/B02 square-pivot result to the fresh ridge Fourier estimate. The unrestricted three-large-eigenvalue conjecture remains OPEN and has not received a full-solution claim here.
