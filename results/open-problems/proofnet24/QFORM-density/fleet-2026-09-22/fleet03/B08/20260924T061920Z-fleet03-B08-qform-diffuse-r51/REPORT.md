SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-24T06:19:20Z.
attacking: the r52 nonzero punctured aligned-star collar by a physical balanced cut, a new exterior-algebra third-compound inequality, and the designated fleet04/B08 child-window receiver.

# fleet03/B08 — punctured cross-star double-alignment router

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T061920Z-fleet03-B08-qform-diffuse-r51`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN / NOT A COUNTEREXAMPLE**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Regularity: every new paid branch below is `C_0`; the inherited exact aligned endpoint has only an essential bound in full generality.

No Gaussian, log-concavity, moment, compact-support, connected-support, identical-law, post-rotation-independence, arbitrary-joint coarea, conditional projection-height, fiber-supremum, or pointwise quadratic-phase decay assumption is used. Every partition below is a partition of the original independent coordinates. A small coefficient tail is never discarded as a small random perturbation.

## 1. Source-pinned starting point

The immediate same-slot source is fleet03/B08 r52:

`yspennstate/math-open-problems@52036281c7ee40217ef26829631c5fdd59aebef7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260924T055811Z-fleet03-B08-qform-diffuse-r52/REPORT.md`.

Its surviving aligned-star collar has one original physical coordinate, called the hub, and a child matrix `C`. Writing

`A = [[a,b^T],[b,C]]`,                                              (1.1)

let `V in R^(m x 2)` be an orthonormal frame for the two largest absolute child eigenvalues and

`C = V Lambda V^T + E`,                                             (1.2)

where

`m_2 := s_2(C) = min(|Lambda_11|,|Lambda_22|)`,
`r := s_3(C) = ||E||_op`.                                           (1.3)

The live r51/r52 survivor has

`max_i ||V_{i,*}||_2^2 <= 1/16`,                                   (1.4)

`m_2 >= sqrt(47/48) L`,                                             (1.5)

`dist(b,range(V)) < ||b||/4`,                                       (1.6)

`0 <= r < L/64`,                                                    (1.7)

and the exact point `(dist(b,range(V)),r)=(0,0)` is already paid by r52. In the exact aligned rank-two-child endpoint r52 gives

`||p_Q||_infinity < 362.039/L`                                      (1.8)

as an essential bound; the exact-null-hub subcase has the stronger continuous bound `<7.560/L`.

The present run attacks the genuinely punctured state and makes no continuity-in-coefficients argument from (1.8).

Two completed analytic receivers are used at their exact scope.

**Marginal-free third-compound crossing.** For any original-coordinate crossing block `B=A[I,J]`, with `I,J` disjoint and exhausting the variables after grouping same-bank terms into arbitrary measurable phases,

`E_3(B):=e_3(BB^T)>0`

implies

`||p_Q||_infinity <= 6^(4/3) E_3(B)^(-1/6)`,                       (1.9)

and `p_Q in C_0(R)`. This is `QFORM-THIRDCOMPOUND-CROSS-PROMOTION-v1` from fleet01/B04.

**Designated fleet04/B08 deletion-child receiver.** If the literal deletion child `C` has three eigenvalues of modulus at least `rho`, and the child spectral projection onto `|lambda(C)|>=rho/64` has every physical leverage at most `1/32`, then

`||p_Q||_infinity < 64/rho`,                                       (1.10)

with `p_Q in C_0(R)`. This is `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`, canonical source

`yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`.

The first new implication is to spend (1.4) before any rotation of the random inputs and obtain a literal two-bank child crossing with two uniformly large singular values.

## 2. A physical balanced cut for a diffuse two-frame

### Lemma 2.1 — `QFORM-TWOFRAME-BERNOULLI-BALANCE-v1`

Let `V in R^(m x 2)` satisfy `V^T V=I_2`, and put

`mu=max_i ||V_{i,*}||_2^2`.

There is a partition of the original child coordinates

`[m]=J disjoint_union K`                                           (2.1)

such that, for

`G_J=V_J^T V_J`, `G_K=V_K^T V_K`,                                 (2.2)

one has

`G_J, G_K >= (1/2-sqrt(mu/2)) I_2`.                               (2.3)

#### Proof

Choose independent Bernoulli variables `delta_i in {0,1}` with mean `1/2` and let `J={i:delta_i=1}`. Then

`G_J-I_2/2 = sum_i (delta_i-1/2) v_i v_i^T`,                      (2.4)

where `v_i=V_{i,*}^T`. Independence and centering give

`E ||G_J-I_2/2||_F^2`
` = (1/4) sum_i ||v_i v_i^T||_F^2`
` = (1/4) sum_i ||v_i||_2^4`
` <= (mu/4) sum_i ||v_i||_2^2`
` = mu/2`,                                                        (2.5)

because `sum_i ||v_i||^2=tr(V^T V)=2`. Therefore some physical cut satisfies

`||G_J-I_2/2||_op <= ||G_J-I_2/2||_F <= sqrt(mu/2)`.              (2.6)

Since `G_K=I_2-G_J`, the same bound holds for `G_K`, proving (2.3). QED.

At the live gate `mu<=1/16`, set

`g := 1/2 - 1/(4 sqrt(2))`
`   = 0.32322330470336313...`.                                    (2.7)

Then the chosen original-coordinate partition satisfies

`G_J,G_K >= g I_2`.                                               (2.8)

## 3. Two robust child crossing directions survive a thin puncture

For the cut of Lemma 2.1 write

`D=C[J,K]`,                                                        (3.1)

`D_0=(V Lambda V^T)[J,K]=V_J Lambda V_K^T`,                       (3.2)

`F=E[J,K]`.                                                        (3.3)

The nonzero singular values of `D_0` are bounded from below by the smallest singular values of the two restricted frames:

`s_2(D_0)`
` >= sigma_min(V_J) sigma_min(Lambda) sigma_min(V_K)`
` >= g m_2`.                                                       (3.4)

Restriction cannot increase operator norm, so `||F||_op<=r`. Weyl gives

`boxed: s_2(D) >= g m_2-r.`                                       (3.5)

Also `rank(D_0)<=2`, hence

`boxed: s_3(D) <= r.`                                             (3.6)

The designated partner now gives a useful preliminary sharpening of the puncture size.

### Proposition 3.1 — partner payment or a localized child row

If

`r >= L/4096`,                                                    (3.7)

apply fleet04/B08 with `rho=r`. If its child window is diffuse, then

`boxed: ||p_Q||_infinity < 64/r <= 262144/L, p_Q in C_0.`         (3.8)

If the window is not diffuse, there is an original child coordinate `k` with

`P_kk>1/32`, `P=1_{|C|>=r/64}`.                                  (3.9)

Spectral energy then gives

`||C e_k||_2 >= (r/64) sqrt(P_kk) > r/(256 sqrt(2))`.             (3.10)

Since

`||C e_k||_2^2=|C_kk|^2+||C[k,-k]||_2^2`,                        (3.11)

at least one component is larger than `||Ce_k||/sqrt(2)`, so

`boxed: max{|C_kk|,||C[k,-k]||_2} > r/512 >= L/2^21.`             (3.12)

Thus an unpaid, nonlocalized punctured survivor may be assumed to obey

`0<r<L/4096`.                                                      (3.13)

In this thin branch, (1.5), (2.7), and (3.5) imply

`s_2(D) >= s_0 L`,                                                 (3.14)

where

`s_0 := g sqrt(47/48)-1/4096`
`     = 0.31959453358755213...`.                                  (3.15)

This is already a literal rank-two crossing at target scale. A rank-two crossing alone has the familiar logarithmic endpoint, so one more physical direction must be spent rather than discarded.

## 4. Exterior-algebra star promotion

The key new quantitative inequality is purely deterministic.

### Lemma 4.1 — `QFORM-STAR-OVER-R2-THIRDCOMPOUND-v1`

Let `D` be any real `p x q` matrix with singular values

`sigma_1>=sigma_2>=...`,                                          (4.1)

and let `R_2` be its top-two right singular subspace. For a row vector `z in R^q`, form

`B=[z^T; D]`.                                                      (4.2)

Then

`boxed: E_3(B) >= sigma_1(D)^2 sigma_2(D)^2 dist(z,R_2)^2.`        (4.3)

The transpose analogue holds with the top-two left singular subspace:

`E_3([w^T;D^T]) >= sigma_1(D)^2 sigma_2(D)^2 dist(w,L_2)^2`.       (4.4)

#### Proof

Take an SVD and apply orthogonal changes to the `D` rows and to all columns. These operations preserve `E_3(B)=e_3(BB^T)` and preserve the stated distance. In the new coordinates the first two singular rows of `D` are

`sigma_1 e_1^T`, `sigma_2 e_2^T`.                                (4.5)

Write the transformed star row as `z'`. Cauchy--Binet gives `E_3(B)` as a sum of squares of all `3 x 3` minors. Keep only the minors using the star row, the first two singular rows, and column triples `{1,2,k}` for `k>=3`. Their squared determinants sum to

`sigma_1^2 sigma_2^2 sum_{k>=3} |z'_k|^2`
` = sigma_1^2 sigma_2^2 dist(z,R_2)^2`.                           (4.6)

Every omitted term is nonnegative, proving (4.3). The transpose statement is identical. QED.

This lemma is exactly product-safe for QFORM: it promotes an actual physical star row together with an actual physical rank-two crossing into the completed marginal-free third-compound receiver. No single `3 x 3` minor is selected and no reciprocal-minor cost appears.

## 5. Main punctured cross-star router

Let `R_2(D)` and `L_2(D)` be the top-two right and left singular subspaces of the literal child crossing `D=C[J,K]`. Split the original physical star accordingly:

`b=(b_J,b_K)`.                                                     (5.1)

Define

`d_K=dist(b_K,R_2(D))`,
`d_J=dist(b_J,L_2(D))`.                                           (5.2)

Consider the two literal full-QFORM crossing blocks

`B_K=A[{hub} union J,K]=[b_K^T;D]`,                               (5.3)

`B_J=A[{hub} union K,J]=[b_J^T;D^T]`.                             (5.4)

These are partitions of the original independent coordinates; all terms internal to either bank remain arbitrary same-bank phases in (1.9).

### Theorem 5.1 — `QFORM-PUNCTURED-CROSSSTAR-DOUBLEALIGN-ROUTER-v1`

Assume the r52 live survivor (1.1)--(1.7), including `m_2>=sqrt(47/48)L` and `max_i||V_i||^2<=1/16`, and assume the puncture is nonzero. Then at least one of the following holds.

**A. Designated-partner payment.**

`||p_Q||_infinity < 262144/L`, with `p_Q in C_0`.                 (5.5)

**B. Quantitative localized child row.** There is an original child coordinate `k` with

`max{|C_kk|,||C[k,-k]||_2} > L/2^21`
` = 4.76837158203125e-7 L`.                                      (5.6)

**C. Cross-star third-compound payment.**

`boxed: ||p_Q||_infinity < 93.296/L, p_Q in C_0.`                (5.7)

**D. Simultaneous double alignment tube.** There is an original-coordinate partition `J union K` satisfying (2.8), for which

`s_2(D)>=0.3195945335 L`, `s_3(D)<L/4096`,                       (5.8)

and both augmented literal crossing blocks lie close to rank two:

`boxed: dist_op(B_K,{rank<=2}) < eps_* L,`                       (5.9)

`boxed: dist_op(B_J,{rank<=2}) < eps_* L,`                       (5.10)

where

`eps_* := sqrt((1/64)^2+(1/4096)^2)`
`       = 0.015626907232231698...`.                              (5.11)

More precisely, on branch D,

`d_K<L/64`, `d_J<L/64`.                                          (5.12)

#### Proof

If `r>=L/4096`, Proposition 3.1 gives A or B. Hence suppose `0<r<L/4096`, so (3.14) holds.

If `d_K>=L/64`, Lemma 4.1 and `sigma_1(D)>=sigma_2(D)>=s_0L` imply

`E_3(B_K)`
` >= (s_0 L)^4 (L/64)^2`.                                       (5.13)

Applying the marginal-free third-compound receiver (1.9),

`||p_Q||_infinity`
` <= 6^(4/3) [ (s_0 L)^4 (L/64)^2 ]^(-1/6)`
` = 6^(4/3) (64/s_0^2)^(1/3) L^(-1)`
` = 93.29580081768943.../L`,                                     (5.14)

and the density is `C_0`. The same proof with `B_J` applies if `d_J>=L/64`. Thus failure of C forces (5.12).

Let `D_2` be the top-two SVD truncation of `D`, and let `P_R,P_L` be the orthogonal projections onto `R_2(D),L_2(D)`. From (3.6),

`||D-D_2||_op=s_3(D)<=r<L/4096`.                                 (5.15)

Define rank-at-most-two matrices

`tilde B_K=[(P_R b_K)^T;D_2]`,                                   (5.16)

`tilde B_J=[(P_L b_J)^T;D_2^T]`.                                 (5.17)

Their ranks are at most two because every row in (5.16) lies in the same two-dimensional right singular plane, and analogously for (5.17). Moreover

`||B_K-tilde B_K||_op^2`
` <= ||(I-P_R)b_K||_2^2 + ||D-D_2||_op^2`
` < (L/64)^2+(L/4096)^2`,                                       (5.18)

because for a vertical block `[u^T;F]`,

`||[u^T;F]||_op^2=||uu^T+F^TF||_op <= ||u||^2+||F||_op^2`.       (5.19)

This proves (5.9); the transpose proof gives (5.10). QED.

## 6. What the new theorem changes

The r52 first unpaid implication was a generic nonzero overlapping-leakage collar. Theorem 5.1 makes that collar much more rigid.

A surviving state must simultaneously satisfy all of the following:

1. the third child spectral scale is extremely thin, `0<r<L/4096`;
2. a literal physical half-cut of the diffuse top-two child frame has a two-direction crossing with `s_2(D)>0.31959L`;
3. both pieces of the parent star are within `L/64` of the corresponding top-two singular planes of that **actual** crossing;
4. both hub-augmented physical crossings are within `0.015627L` in operator norm of rank two;
5. nevertheless the full parent still has the inherited three-large-eigenvalue requirement and all arbitrary same-bank curvature.

The point is not that the `L/4096` tail is a small random error. It is not. The tail was used only in deterministic singular-value and rank-tube inequalities, while every density estimate was applied to the literal full crossing and hence retained the tail exactly.

The double alignment is also substantially stronger than the original global statement `dist(b,range(V))<||b||/4`: it aligns each physical star half with the singular geometry of the actual cross bank produced by the diffuse frame.

## 7. Designated partner applied at an actual inequality

For clarity, the fleet04/B08 result is not merely cited as background. It is applied to the literal deletion child `C` at the concrete scale

`rho=r=s_3(C)`.                                                   (7.1)

When `r>=L/4096`, the partner's conclusion gives exactly

`||p_Q||_infinity<64/r<=262144/L`.                               (7.2)

When its leverage gate fails, the partner window itself gives the quantitative physical row (3.12), hence

`max{|C_kk|,||C[k,-k]||_2}>L/2^21`.                              (7.3)

Therefore the new cross-star analysis is required only below `L/4096`; it does not duplicate the partner's completed scope.

## 8. Continuity bookkeeping

- Branch A: continuous `C_0` density by the fleet04/B08 affine-uniform ridge-window theorem.
- Branch C: continuous `C_0` density because the marginal-free third-compound theorem proves an `L^1` characteristic function.
- Branch B and branch D are structural exits, not density conclusions.
- The inherited exact endpoint `r=0` is essentially bounded by r52 in full generality; continuity there is known only in its exact-null-hub subcase. Hence this run does **not** claim global continuity.

## 9. Exact next implication

The first remaining B08 implication is

### `QFORM-PUNCTURED-DOUBLEALIGNED-RANK2-TUBE-INTERPOLATION-v1`

> In the branch D geometry of Theorem 5.1, consume the simultaneous left/right star alignment with the target-scale rank-two physical crossing while retaining the genuine nonzero `E` tail and arbitrary same-bank curvature. Either obtain a uniform endpoint density bound independent of `r -> 0`, or force an already-paid physical scalar/pair, determinant-star, incident-volume, ridge-window, or localized-child receiver.

A valid proof may not condition on a dependent projected scalar, replace the product source by an arbitrary bounded joint density, rotate the random coordinates and retain independence, or treat `||E||_op<L/4096` as a small random perturbation. The exact endpoint `r=0` and every state with a transverse star component at least `L/64` relative to the actual crossing are already paid.

## 10. Source ledger

- Same-slot r52: `math-open-problems@52036281c7ee40217ef26829631c5fdd59aebef7`, B08 r52 report.
- Designated partner fleet04/B08: `math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`, `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`.
- Marginal-free third-compound crossing: fleet01/B04 `QFORM-THIRDCOMPOUND-CROSS-PROMOTION-v1`, report on the current master ancestry; its receiver is pinned to `math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401` and the canonical compound-promotion theorem at `d5e114f4a9f515344575756615fce3a754195b13`.
- Owner/control and live corrections are refreshed again immediately before publication and recorded separately in `SOURCE_REFRESH.md`.

Full QFORM remains **OPEN**. This report is a supporting theorem, not a full proof and not a counterexample. Two independent end-to-end reviews required for a full candidate have not occurred.
