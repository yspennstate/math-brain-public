# account02/B08 — diffuse extraction obstruction and local-payment branch

**Run:** `B08-20260922T163551Z-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Live owner revision used:** `2026-09-22.7`  
**Assignment:** `Diffuse eigenvector case`  
**Classification:** `ESSENTIAL_STEP_APPLIED / REFUTED_INTERMEDIATE_MECHANISM`  
**Result name:** `QFORM-DIFFUSE-APPROX-BLOCK-EXTRACTION-ALONE-FALSE-v1`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**

## 0. Target, sources, and first unpaid implication

The target is the full arbitrary-product-law statement: independent real coordinates with probability densities at most one, and a real symmetric matrix with at least three eigenvalues of modulus at least one. No moment, support, centering, identical-law, or independence-after-rotation hypothesis is available.

This run starts from the preceding B08 theorem `QFORM-DIFFUSE-APPROX-BLOCK-STABILITY-v1`, source

`yspennstate/math-open-problems@c1c6ffe8c742cbba7611b5a3f1d73cf71019f47b`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T153820Z-r12/REPORT.md`.

That theorem pays an arbitrary dense remainder perturbation provided, after conditioning original coordinates, the surviving remainder is close in operator norm to a block-diagonal matrix whose whitened selected-frame block masses are small. Its unpaid structural implication was to extract such an approximate block decomposition from delocalization, or replace it by another genuine product-preserving smoothing certificate.

The latest completed named-partner result actually applied below is account03/B08 `QFORM-FRACTIONAL-RIDGE-DIFFUSE-SPECTRAL-GAP-v1`, source

`yspennstate/math-open-problems@cf67f10cc3b6687e6c1bcd1a6f8075adb1057924`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T154922Z-account03-B08-qform-diffuse-r12/REPORT.md`.

For local physical-coordinate payment I use the already completed account01/B05 conditional definite-principal-pair theorem, source

`yspennstate/math-open-problems@8b471bfd0ff8df0ce71ed0fcf49bcbd94531b1b5`

at

`qform/fleet-2026-09-22/account01/B05/20260922T1136Z-qform-principal2d-B05-r1/REPORT.md`.

The first implication attacked here is deliberately sharp: **does arbitrarily strong delocalization of the selected three-eigenspace force the approximate-block hypothesis of the preceding B08 theorem after source-valid physical-coordinate conditioning?** The answer is no, even for an explicit target-valid family whose output density is nevertheless bounded by `pi` by a different physical-coordinate mechanism.

## 1. The flat three-bank family

Fix `m>=2`, let `n=3m`, and partition the original coordinates into three disjoint groups `G_1,G_2,G_3`, each of size `m`. Put

`r_j = m^(-1/2) 1_{G_j}`, `j=1,2,3`,

and let `R=[r_1 r_2 r_3]`. Then `R^T R=I_3`, while every row of `R` has squared leverage exactly `1/m`. Thus the selected three-frame is arbitrarily delocalized as `m -> infinity`.

Take

`Lambda=diag(1,1,-1)`,
`P=R R^T`,
`C=I-P`,
`A=R Lambda R^T + C`.

Since `CR=0`, this is a genuine spectral decomposition. In fact

`A = I - 2 r_3 r_3^T`.

Hence `A` has eigenvalue `-1` on `r_3` and eigenvalue `+1` on its orthogonal complement. It therefore satisfies the target hypothesis very strongly: every eigenvalue has modulus one.

No input laws are specialized below: `X_1,...,X_n` remain arbitrary independent variables with densities bounded by one.

## 2. Exact obstruction to approximate-block extraction

Condition an arbitrary set `H` of original coordinates and put `T=H^c`. Write

`h_j=|H cap G_j|`,
`d_j=(m-h_j)/m`,
`eta=||R_H^T R_H||_op=max_j h_j/m`.

Assume `eta<1`, as required by the preceding B08 whitening theorem. Then every `d_j>=1-eta>0`. The surviving selected Gram matrix is

`M=R_T^T R_T=diag(d_1,d_2,d_3)`.

After whitening, `W=R_T M^(-1/2)`. On the residual part of group `G_j`, every row of `W` equals `e_j/sqrt(m-h_j)`. Consequently, for any partition of `T` into physical blocks `B_k`,

`||W_{B_k}^T W_{B_k}||_op
 = max_j |B_k cap G_j cap T|/(m-h_j)`.

Let

`mu=max_k ||W_{B_k}^T W_{B_k}||_op`

and suppose `mu<1/3`, which is necessary for the preceding stability theorem. Fix any group `j`. The normalized block weights

`w_k=|B_k cap G_j cap T|/(m-h_j)`

sum to one and each is at most `mu<1/3`. By greedily adding whole blocks until the sum first reaches `1/3`, there is a union `S` of whole blocks for which

`1/3 <= s:=sum_{k in S} w_k < 2/3`.

Now let `C_0` be **any** matrix block diagonal on the same blocks and put

`E=C[T,T]-C_0`, `tau=||E||_op`.

Because `S` is a union of whole blocks, `C_0[S,T\S]=0`; hence

`E[S,T\S]=C[S,T\S]`.

The identity part of `C=I-P` has no cross block. Restricting the cross block to the chosen bank `G_j` therefore gives the rank-one rectangular matrix

`-(1/m) 1_{S cap G_j} 1_{(T\S) cap G_j}^T`.

Its operator norm is

`d_j sqrt(s(1-s))`.

Since `s in [1/3,2/3]`,

`sqrt(s(1-s)) >= sqrt(2)/3`.

Also `d_j>=1-eta`. Therefore every such block approximation obeys the exact lower bound

`tau >= (1-eta) sqrt(2)/3`.                                   (2.1)

This is independent of `m`, although the selected-frame row leverage is `1/m -> 0`.

### Consequence for the preceding B08 stability criterion

That theorem uses

`alpha=(1-sqrt(3 mu))/2 <= 1/2`,
`rho=alpha(1-eta)-tau`.

If `rho<=0`, its hypothesis already fails. If `rho>0`, (2.1) implies

`rho <= (1-eta)(1/2-sqrt(2)/3)`

and hence

`sqrt(6) tau/rho
 >= [sqrt(6) sqrt(2)/3]/[1/2-sqrt(2)/3]
 = 40.3805276...`.

The stability theorem requires

`(sqrt(mu/alpha)+sqrt(6) tau/rho)^2 <= 1/2`,

but the second term alone has square `>1630`. Therefore:

> **For this target-valid family, for every source-valid conditioning set with `eta<1`, for every physical block partition with whitened block mass `mu<1/3`, and for every block-diagonal approximant on that partition, the preceding approximate-block stability certificate is impossible.**

Thus selected-eigenspace delocalization alone cannot force the approximate-block branch, even at leverage `1/m -> 0`.

This refutes an intermediate extraction mechanism only. It is not a counterexample to the QFORM conjecture.

## 3. The same family is uniformly safe by localized physical smoothing

The obstruction above is not pathological output behavior. Because

`A=I-2r_3r_3^T`,

the principal block on the entire first bank `G_1` is exactly the identity and has no internal off-diagonal entries. Pick any two coordinates `i != j` in `G_1`. Their `2 x 2` principal block is `I_2`, which is positive definite with determinant one.

Apply the completed account01/B05 conditional definite-principal-pair theorem: condition all coordinates except `X_i,X_j`; the conditional joint density of this original-coordinate pair remains at most one, and the planar elliptic-shell estimate gives

`P(Q in I | other coordinates) <= pi |I|`

for every interval `I`. Averaging the conditioning yields

`||p_Q||_infinity <= pi`.                                    (3.1)

This uses no moments or support assumptions and no rotated independence. Hence the flat three-bank family proves that a correct all-delocalized reduction needs a **second physical-local payment branch**; approximate block extraction cannot be the sole bridge.

## 4. Applying the latest account03/B08 theorem to an actual neighboring inequality

The named partner theorem also controls a nontrivial perturbative neighbor of the same construction. Take `m=16` and

`A_epsilon = R Lambda R^T + epsilon (I-P)`,
`epsilon=1/64`.

The selected frame has

`r=3`, `mu=max_i ||r_i||^2=1/16`,

and the spectral remainder has operator norm `eta=1/64`. In the partner notation,

`alpha=(1-sqrt(3/16))/2=0.28349364905389035...`,
`sigma=alpha-1/64=0.26786864905389035...`.

With `q=1`,

`kappa=[sqrt((1/16)/alpha)+sqrt(6)(1/64)/sigma]^2
      =0.3750535589... < 1/2`,

and `18/7>2`. Therefore the partner theorem gives the actual target-level inequality

`||p_{X^T A_epsilon X}||_infinity
 <= (9/2) sqrt(3e) / sigma
 =47.9731785823... <48`.                                    (4.1)

For comparison, the completed local definite-principal-pair theorem applied to two coordinates in `G_1` sees the principal determinant

`det B = epsilon [epsilon+2(1-epsilon)/16] = 71/32768`

and gives only

`pi/sqrt(det B)=67.49096935...`.

Thus the partner's diffuse spectral-gap theorem is quantitatively active on this explicit family; it is not cited merely as background.

## 5. What is closed and what remains

### Closed in this run

1. `QFORM-DIFFUSE-APPROX-BLOCK-EXTRACTION-ALONE-FALSE-v1`: arbitrarily small selected-frame row leverage does **not** force the approximate-block hypothesis of `QFORM-DIFFUSE-APPROX-BLOCK-STABILITY-v1`, even after arbitrary physical-coordinate conditioning of selected mass `<1`.
2. The obstruction is exact and source-valid: the lower bound (2.1) holds against every block-diagonal approximant on every small-whitened-mass partition.
3. The same family is target-safe with the dimension-free bound `pi` by localized two-coordinate physical smoothing.
4. The latest completed named-partner theorem gives the explicit neighboring bound `<48` in (4.1).

### First remaining implication

The prior extraction-only route must be replaced by

`QFORM-DIFFUSE-APPROXBLOCK-OR-LOCAL-PAYMENT-v1`:

> Given a delocalized selected three-large-eigenvector frame and arbitrary spectral remainder `CR=0`, prove a quantitative source-valid dichotomy: after conditioning a set carrying controlled selected mass, either (a) the remainder admits an approximate block decomposition satisfying the B08 stability theorem, or (b) one can extract a uniformly nondegenerate **physical-coordinate smoothing object** (for example a definite `2 x 2` principal block, or a dependence-safe bank/ridge certificate) that directly bounds the full conditional quadratic form.

The flat three-bank construction proves branch (b) is logically necessary. The current run does **not** prove this dichotomy for arbitrary remainder and therefore does not prove the full conjecture.

## 6. Verification notes

A deterministic checker stored beside this report verifies the numerical partner hypotheses, the `<48` bound, the local principal determinant, and the quantitative impossibility constant in Section 2. All structural identities in Sections 1–3 are proved symbolically above and do not rely on numerical experimentation.

**Status:** `ESSENTIAL_STEP_APPLIED / REFUTED_INTERMEDIATE_MECHANISM`.  
**Full target:** `OPEN`.
