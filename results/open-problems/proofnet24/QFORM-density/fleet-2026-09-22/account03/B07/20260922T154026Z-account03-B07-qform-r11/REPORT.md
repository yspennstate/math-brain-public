# account03/B07 — nested-heavy disjoint-bank collar after conditional Pluecker localization

**Run:** `20260922T154026Z-account03-B07-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Coordinate minor selection  
**Classification:** `PROVED SUPPORTING STRUCTURAL THEOREM / COMPLETED PARTNER APPLICATION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and fresh source discipline

The full target remains open: for every dimension, independent real coordinates `X_i` whose probability densities satisfy `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with one universal finite `L^infinity` bound, or produce a valid counterexample. A continuous representative is a separate stronger conclusion and is not proved here.

Fresh control was resolved from `yspennstate/math-research-brain` main and remained owner revision `2026-09-22.5`. The final pre-write control snapshot was `a1f27a271acad1d784c6bb6022a9f8f4983d822d`; the live correction inbox there had blob `2ee621225465e603dfd118f6bd86b1ddc853f40e`. This report does not use law-uniform pointwise quadratic Fresnel decay, post-rotation independence, a fiberwise supremum, one tiny coordinate minor as a universal certificate, or a reciprocal-minor average.

The designated partner `account04/B07` still had no completed current-QFORM canonical report or shared handoff at the fresh source check. No result is fabricated or attributed to it. The compatible completed account04 theorem actually applied below is `account04/B18`, `QFORM-SCHUR-PIVOT-SMOOTHING-v1`, canonical source

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

The preceding B07 state is source-pinned at

`yspennstate/math-open-problems@0b3ca7e927cad2a7c7805a7f2ba6b88b12d000fd`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T143620Z-account03-B07-QFORM-r12/REPORT.md`.

That run proved the conditional edge-law star/triangle theorem and reduced the nested-heavy rank-three branch to a small disjoint-edge-mass chamber. This run changes mechanism: instead of another local reciprocal-minor estimate, it diagonalizes the **residual covariance only as deterministic coefficient geometry** and selects disjoint sets of original coordinates by a dimension-free second-moment argument. No random-variable rotation is performed.

## 2. Recalled conditional Pluecker state

Assume first the exact-rank-three core

`A=R Lambda R^T`, `R^T R=I_3`, `|lambda_j(Lambda)|>=1`.

Let `r_k in R^3` denote the physical spectral rows. Choose a first leverage-heavy row `i`, write

`r_i=sqrt(c)e_1`, `c>1/2`,

and suppose the residual two-frame contains a second heavy row `j`, so in a suitable deterministic orthonormal basis of coefficient space

`r_j=rho e_1+sqrt(h)e_2`, `h>1/2`.

Let `e_3` complete the basis. For every residual physical coordinate `k notin {i,j}` write

`r_k=x_k e_1+y_k e_2+z_k e_3`.

Because `sum_k r_k r_k^T=I_3`, the covariance left after deleting the two physical rows is

`S=I-r_i r_i^T-r_j r_j^T`

and in this basis

`S = [[1-c-rho^2, -rho sqrt(h), 0],
      [-rho sqrt(h), 1-h,       0],
      [0,              0,        1]].`                           (2.1)

Put

`P=S|span(e_1,e_2)`, `Delta=det P`,

and let `lambda>=mu>=0` be the two eigenvalues of `P`. Thus

`lambda+mu=tr P`, `lambda mu=Delta`.                              (2.2)

The pair Pluecker mass is

`p_ij := det Gram(r_i,r_j)=c h`.                                  (2.3)

Indeed the conditional volume-sampling law after inclusion of `i,j` has third-coordinate probabilities exactly

`P(K=k | i,j included)=z_k^2`,                                   (2.4)

because

`det(r_i,r_j,r_k)^2=c h z_k^2`, `sum_k z_k^2=1`.                 (2.5)

Write

`d_* = max_k z_k^2`.                                              (2.6)

The completed account03/B13 nested-heavy theorem shows that along any putative unbounded-density sequence in this branch one must have simultaneously

`d_* ->0`, `Delta->0`.                                            (2.7)

The purpose of the present run is to resolve the geometry of (2.7) without selecting a single tiny final minor.

## 3. New theorem: a two-coloop or disjoint-bank collar

Diagonalize only the deterministic `2x2` matrix `P`: let `u,v` be orthonormal eigenvectors with eigenvalues `lambda,mu`. For residual physical rows write

`r_k=a_k u+b_k v+z_k e_3`.                                       (3.1)

This is a change of basis in the three-dimensional **coefficient bookkeeping space**, not a rotation of the independent random variables. From (2.1)-(2.2),

`sum a_k^2=lambda`, `sum b_k^2=mu`, `sum z_k^2=1`,                (3.2)

and the three coefficient vectors are pairwise orthogonal in `ell_2`.

### Theorem 3.1 — `QFORM-NESTED-HEAVY-DISJOINT-BANK-COLLAR-v1`

Fix `0<eta<1/4`. In the nested-heavy setup above, at least one of the following two alternatives holds.

**(C) two-coloop concentration.** If `lambda<eta`, then

`boxed( p_ij=c h > 1-4 eta. )`                                   (3.3)

Thus the two selected physical coordinates carry nearly all conditional rank-two Pluecker volume.

**(B) disjoint-bank extraction.** If `lambda>=eta`, there is a partition of the residual **original-coordinate indices**

`R0={k:k notin {i,j}} = Y disjoint_union Z`

such that

`boxed( sum_{k in Y} a_k^2 >= lambda(1-d_*)/4, )`                 (3.4)

`boxed( sum_{k in Z} z_k^2 >= (1-d_*)/4, )`                       (3.5)

while the total coefficient energy in the orthogonal minor planar direction satisfies

`boxed( sum_k b_k^2=mu=Delta/lambda <= Delta/eta. )`              (3.6)

In particular the coordinate families `(X_k)_{k in Y}` and `(X_k)_{k in Z}` remain independent, since the theorem selects disjoint physical index sets and performs no rotation of the inputs.

### Proof of (B)

Choose a random subset `Y` by putting every residual physical index into `Y` independently with probability `1/2`, and let `Z=R0\Y`. Define

`A_Y=sum_{k in Y} a_k^2`, `Z_Z=sum_{l in Z} z_l^2`.

Then

`E[A_Y Z_Z]
 = sum_{k!=l} a_k^2 z_l^2 P(k in Y,l in Z)
 = (1/4)[(sum a_k^2)(sum z_l^2)-sum a_k^2 z_k^2]`                 (3.7)

and therefore, using `z_k^2<=d_*` and (3.2),

`E[A_Y Z_Z] >= lambda(1-d_*)/4`.                                 (3.8)

Hence at least one deterministic partition satisfies

`A_Y Z_Z >= lambda(1-d_*)/4`.                                    (3.9)

Because `Z_Z<=1`, (3.9) implies (3.4). Because `A_Y<=lambda`, it implies (3.5). Finally (3.6) is exactly (2.2) with `lambda>=eta`. QED.

### Proof of (C)

If `lambda<eta`, then also `mu<=lambda<eta`, hence

`tr P=lambda+mu<2eta`.                                            (3.10)

From (2.1),

`1-h=P_22<tr P<2eta`,                                            (3.11)

so `h>1-2eta`. Also `P>=0` implies

`rho^2 <= (1-c)(1-h)`.                                           (3.12)

Using `P_11=1-c-rho^2`,

`1-c=P_11+rho^2
    <= tr P+(1-c)(1-h)`.                                         (3.13)

Rearranging gives

`(1-c)h < 2eta`.                                                  (3.14)

Therefore

`c h = h-h(1-c) > (1-2eta)-2eta=1-4eta`,                         (3.15)

which is (3.3). QED.

## 4. Concrete finite collar inside the current residual chamber

Take

`eta=1/16`.                                                       (4.1)

Then Theorem 3.1 says:

* if `lambda<1/16`, the pair Pluecker mass obeys

  `p_ij>3/4`;                                                     (4.2)

* if `lambda>=1/16` and the current B13 residual has `d_*<1/6`, there are disjoint original-coordinate banks `Y,Z` with

  `sum_Y a_k^2 >= 5/384`,                                        (4.3)

  `sum_Z z_k^2 >= 5/24`,                                         (4.4)

  and

  `sum_k b_k^2 <=16 Delta`.                                      (4.5)

Thus the formerly amorphous simultaneous `d_* small, Delta small` chamber has an explicit source-valid normal-form dichotomy: either two physical coordinates become a `>3/4` conditional two-coloop, or two disjoint independent coordinate banks carry definite dominant-plane/transverse `ell_2` mass while the third coefficient direction has total energy at most `16 Delta`.

No reciprocal local determinant has been paid in obtaining (4.2)-(4.5).

## 5. Asymptotic consequence for any putative unbounded rank-three sequence

Combine Theorem 3.1 with the completed B13 necessity (2.7). Let a nested-heavy exact-rank-three sequence have density norms tending to infinity. Passing to a subsequence in the scalar sequence `lambda_m` gives exactly one of the following structural regimes.

1. **Two-coloop limit:** `lambda_m->0`. Since Theorem 3.1(C) holds for every fixed `eta>lambda_m`,

   `p_{i_m j_m}=c_m h_m ->1`.                                    (5.1)

2. **Stable disjoint-bank limit:** for some `eta_0>0`, `lambda_m>=eta_0` along a subsequence. Theorem 3.1(B) supplies disjoint original-coordinate banks `Y_m,Z_m` satisfying

   `sum_{Y_m} a_{k,m}^2 >= eta_0(1-d_{*,m})/4 -> eta_0/4`,        (5.2)

   `sum_{Z_m} z_{k,m}^2 >= (1-d_{*,m})/4 ->1/4`,                 (5.3)

   while

   `sum_k b_{k,m}^2 <= Delta_m/eta_0 ->0`.                       (5.4)

This is a genuine compactness reduction: every surviving nested-heavy sequence either approaches a two-coordinate coloop geometry, or contains two independent physical banks carrying uniformly positive coefficient norms with a vanishing third-direction contamination.

The second regime is exactly the kind of source provenance needed by the completed high-cardinality aggregation theorems; the remaining work is to connect the coefficient-bank normal form to one of those analytic payments without discarding the other terms of the quadratic form.

## 6. Actual application of completed account04 mathematics

The preceding B07 star/triangle theorem gave, under the clean collar `rho_edge<=1/64`, either the nested-heavy branch above or a physical triple with

`W_{ijk}>=47/384`, hence

`|det B|=|det Lambda| W_{ijk}>=47/384`.                            (6.1)

On the subcase where that triple has a scalar pivot `a` with `|a|>=1/32` and definite Schur complement, the completed account04/B18 theorem applies **with all outside couplings allowed**, because conditioning is on original coordinates. It gives the concrete inequality

`||p_Q||_infinity
 <=2 sqrt(pi) (|a det B|)^(-1/4)
 <=2 sqrt(pi) [(1/32)(47/384)]^(-1/4)
 <14.255.`                                                        (6.2)

This is an actual use of the completed account04 theorem, not a citation-only mention. The complementary nonzero-pivot indefinite-Schur branch is paid by account03/B16 with the same determinant/pivot scaling but a larger constant; the exactly all-zero-diagonal invertible triple is paid by account02/B16's product-log theorem. The still-uniformly unpaid local transition is when all three diagonal pivots are quantitatively near zero but not exactly zero; no continuity-in-the-matrix coefficient theorem is silently assumed.

## 7. Exact finite checker

A small Fraction-only checker accompanies this report. Its first fixture takes four residual coordinates with

`a_k^2=lambda/4`, `z_k^2=1/4`, `lambda=3/5`, `d_*=1/4`.

Exhaustive enumeration over all sixteen partitions gives

`max_Y (sum_Y a_k^2)(sum_{Z} z_k^2)=lambda/4=3/20`,               (7.1)

while the theorem requires only

`lambda(1-d_*)/4=9/80`.                                          (7.2)

Its second fixture takes `rho=0`, `c=h=31/32`; then the residual plane has `lambda=1/32<1/16` and

`p_ij=(31/32)^2=961/1024>3/4`,                                   (7.3)

checking the concrete coloop collar exactly. The checker is diagnostic; the proof is Sections 3-5.

## 8. Smallest conditional end-to-end deduction and first unpaid implication

For the **rank-exactly-three** problem, the previous B07/B13 reductions plus Theorem 3.1 leave a much sharper endgame. A putative unbounded sequence can survive only if it approaches one of:

* `QFORM-TWO-COLOOP-PAYMENT-v1`: two physical coordinates carry conditional pair Pluecker mass tending to one while the third conditional direction remains diffuse; or
* `QFORM-DISJOINT-BANK-PERTURBATIVE-PAYMENT-v1`: two disjoint original-coordinate banks retain positive dominant-plane/transverse `ell_2` norms while the orthogonal planar contamination tends to zero.

The first implication attacked next should be the second one: apply the already completed product-preserving aggregate hyperbolic/square or signed-Fourier estimates **before** any reciprocal coordinate minor, and quantify stability under the vanishing `b`-contamination in (5.4). If that succeeds, only the two-coloop limit remains in exact rank three.

For the **full owner target**, arbitrary additional spectral components remain a separate debt. They may alter physical Schur complements and cannot be treated as independent convolution noise after spectral rotation. No full-target closure is claimed.

## 9. Status

* `QFORM-NESTED-HEAVY-DISJOINT-BANK-COLLAR-v1`: **PROVED supporting structural theorem**.
* Account04/B18 application (6.2): **PROVED on its stated definite-Schur/pivot subcase**.
* Exact-rank-three nested-heavy residual: **strictly narrowed, not fully closed**.
* Full arbitrary-matrix QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
* Continuous-density conclusion: **not proved by the new theorem**.

No scheduler state, notification state, email, Drive, public workflow, paid model/API, Codex, credentials, or cross-account native state is used or changed by this mathematical report.
