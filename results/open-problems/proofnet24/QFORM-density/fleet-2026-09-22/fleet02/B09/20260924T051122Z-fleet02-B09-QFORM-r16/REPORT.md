SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-24T05:11:22Z.
attacking: the partner's pair-resource-or-routing debt by constructing a target-valid diffuse mixed-hub family on which every literal invertible physical pair/scalar-star resource collapses, while an undecoupled source-coordinate mixed-frame estimate stays universal.

# fleet02/B09 — mixed-frame routing is genuinely necessary

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid obstructions  
Run: `20260924T051122Z-fleet02-B09-QFORM-r16`  
Status: **ESSENTIAL STEP APPLIED / STRUCTURAL PAIR-RESOURCE FORCING REFUTED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

All random variables below are literal original-coordinate variables. Inputs are arbitrary independent real variables with probability densities bounded by one. No moment, support, log-concavity, Gaussianity, iid, diagonal-basis, post-rotation-independence, or small-perturbation hypothesis is used.

## 1. First unpaid implication

The latest completed designated partner is fleet03/B09 r44,

`yspennstate/math-open-problems@1d81e62c818d6b592a6a6da78870f12f533d615a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260924T044555Z-fleet03-B09-QFORM-r44/REPORT.md`.

For a literal invertible indefinite physical pair `B`, let

`D=|det B|`, `kappa=sigma_min(B)`.

After exact pair completion, if one remaining literal scalar `X` and a disjoint original-coordinate bank `Z` have remainder

`R=sX^2+2X<m,Z>+beta X+G(Z)`,

r44 proves the uniform scalar/star certificate

`||p_Q||_infinity <= 15.059181791 [D kappa (|s|+||m||)]^(-1/4)`.       (1.1)

The theorem is uniform through `s=0` and retains arbitrary `G`. Its named next debt is to force a universal-scale pair resource

`D kappa (|s|+||m||)`                                                 (1.2)

or route the small-resource survivor into a source-coordinate aggregate mechanism before reciprocal pair payment.

This run proves that the first branch is impossible under the bare owner target, even if one optimizes over **every** literal invertible physical pair and **every** remaining literal scalar. In fact the sum of the best resources over all invertible pairs can tend to zero. Hence the routing branch is logically necessary.

## 2. Construction

Let `m>=16` be a Sylvester-Walsh size and choose three flat orthonormal vectors

`c,d,w in R^m`,                                                       (2.1)

so every coordinate has absolute value `m^(-1/2)`. Let `U,V,Y_1,...,Y_m` be the original independent cap-one variables and define

`Q_m = 2 U <c,Y> + 2 V <d,Y> + <w,Y>^2`.                            (2.2)

The coefficient matrix is

`A_m = [[0,0,c^T],
        [0,0,d^T],
        [c,d,ww^T]]`.                                                (2.3)

The leaf block `ww^T` is dense in the physical coordinates.

## 3. Exact target spectrum

On the orthonormal coefficient-space basis

`U,V,c,d,w`,

the active matrix is the orthogonal direct sum of

`[[0,1],[1,0]]`, `[[0,1],[1,0]]`, and `[1]`.                        (3.1)

Therefore

`spec_nonzero(A_m)={-1,-1,1,1,1}`                                  (3.2)

for every `m`. Thus this is a genuine owner-target family, with five eigenvalues of modulus one.

## 4. Required pinned mixed-hub theorem: a universal direct inequality

Use the owner-pinned completed Theorem H from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Take the two literal hubs `H={U,V}`, the whole leaf bank `I={Y_1,...,Y_m}`, no outside bank, and one same-side leaf square `lambda=1`, `v_1=w`. The physical mixed rows are

`rho_i=(w_i,c_i,d_i)`.                                               (4.1)

Their Gram is exactly

`G=sum_i rho_i rho_i^T=I_3`,                                        (4.2)

and every normalized physical leverage is

`rho_i^T G^(-1) rho_i=3/m<=3/16<1/2`.                              (4.3)

Theorem H therefore gives directly, without decoupling or probability squaring,

`|phi_Q(t)| <= 8 pi^(5/2) |t|^(-5/2)`.                             (4.4)

Combining with `|phi_Q|<=1`,

`int_R min(1,K|t|^(-5/2)) dt = (10/3) K^(2/5)`,                    (4.5)

with `K=8pi^(5/2)`. Fourier inversion yields

`boxed:
 ||p_(Q_m)||_infinity
 <= (5/3) 2^(6/5)
 = 3.828994516656783... .`                                         (4.6)

Hence every interval `J` satisfies

`boxed: P(Q_m in J) <= 3.828995 |J|.`                              (4.7)

The characteristic function is integrable, so this branch has a continuous density. The dense same-side coupling `ww^T` is retained throughout.

## 5. Exhaustive classification of physical pairs

There are only three types of literal physical `2x2` principal blocks.

### 5.1 The hub-hub pair

`A_m[{U,V},{U,V}]=0`,                                               (5.1)

so it is singular.

### 5.2 Two leaves

For distinct leaves `i,j`,

`A_m[{i,j},{i,j}]
 = [[w_i^2,w_iw_j],[w_iw_j,w_j^2]]`,                               (5.2)

which has rank one and determinant zero.

### 5.3 One hub and one leaf

For `{U,Y_i}`,

`B_i = [[0,c_i],[c_i,1/m]]`,                                      (5.3)

and analogously for `{V,Y_i}` with `c_i` replaced by `d_i`. Since `c_i^2=d_i^2=1/m`, every such pair is invertible indefinite and

`D_i=|det B_i|=1/m`.                                                (5.4)

Its smaller singular value is the smaller absolute eigenvalue,

`kappa_m=(sqrt(4m+1)-1)/(2m)`.                                    (5.5)

These `2m` hub-leaf blocks are **all** invertible physical pairs of `A_m`.

## 6. Exact Schur complement after any invertible pair

Fix `{U,Y_i}`. Put

`alpha_i=d_i/c_i in {+1,-1}`,
`beta_i=w_i/c_i in {+1,-1}`.                                      (6.1)

Completing the pair exactly leaves the variables `(V,Y_{-i})`. A direct block calculation gives the Schur coefficient matrix

`S_i=
 [[0, (d-alpha_i c)_{-i}^T],
  [(d-alpha_i c)_{-i},
   (w-beta_i c)_{-i}(w-beta_i c)_{-i}^T ]]`.                       (6.2)

Indeed `B_i^(-1)=[[-1,1/c_i],[1/c_i,0]]`, and substitution in

`A_RR-A_RH B_i^(-1) A_HR`

gives (6.2) exactly.

Set

`d^(i)=d-alpha_i c`,
`z^(i)=w-beta_i c`.                                                (6.3)

Because `c,d,w` are orthonormal and `alpha_i,beta_i` are signs,

`d^(i)_i=z^(i)_i=0`,
`||d^(i)||=||z^(i)||=sqrt(2)`.                                    (6.4)

This lets us optimize r44's scalar/star resource over **every** remaining scalar coordinate.

### 6.1 Choose the remaining scalar to be `V`

From (6.2),

`s=0`,
`m=(d^(i))_{-i}`,                                                  (6.5)

so

`|s|+||m||=sqrt(2)`.                                               (6.6)

### 6.2 Choose any remaining scalar leaf `Y_j`, `j!=i`

Its scalar coefficient is

`s=(z^(i)_j)^2`,                                                    (6.7)

hence

`|s|<=4/m`.                                                         (6.8)

Its entire star into `(V,Y_{-i,-j})` has squared norm

`||m||^2
 = (d^(i)_j)^2
   +(z^(i)_j)^2 (||z^(i)||^2-(z^(i)_j)^2)
 <=4/m+8/m
 =12/m`.                                                           (6.9)

Therefore

`|s|+||m|| <=4/m+sqrt(12/m) < sqrt(2)`                             (6.10)

for every `m>=16`.

Combining (6.6) and (6.10), the **best possible** scalar/star resource after this pair is exactly bounded by

`max_(k outside H)
 D_i kappa_m (|s_(i,k)|+||m_(i,k)||)
 <= (sqrt(2)/m) kappa_m`.                                         (6.11)

The same proof, interchanging `c` and `d`, applies to every pair `{V,Y_i}`.

Thus globally

`boxed:
 max_(all invertible physical pairs H)
 max_(literal scalar k outside H)
 |det B_H| sigma_min(B_H)
 (|s_(H,k)|+||m_(H,k)||)
 <= sqrt(2)(sqrt(4m+1)-1)/(2m^2)
 ->0.`                                                             (6.12)

Since there are exactly `2m` invertible pairs, even the sum of their individually optimized resources satisfies

`boxed:
 sum_H max_k
 |det B_H| sigma_min(B_H)(|s_(H,k)|+||m_(H,k)||)
 <=2sqrt(2) kappa_m
 ->0.`                                                             (6.13)

The decay rates are respectively `Theta(m^(-3/2))` and `Theta(m^(-1/2))`.

## 7. Application to the latest partner theorem: a real obstruction

Equation (6.12) applies the exact r44 scalar/star resource to an actual target family. The best r44 certificate obtainable by selecting any literal invertible pair and any remaining literal scalar has coefficient

`15.059181791 [R_m]^(-1/4)`,                                       (7.1)

where

`R_m <= sqrt(2) kappa_m/m = Theta(m^(-3/2))`.                      (7.2)

Hence that certificate grows at least at the scale `m^(3/8)` along this family. This does **not** say the true density grows: Section 4 gives the uniform bound `3.829` for the same forms. It says the proposed structural closure

`three large eigenvalues => one universal-scale physical-pair scalar/star resource`

is false, even after exhaustive physical pair/scalar optimization.

The stronger sum estimate (6.13) also rules out repairing that exact statement by simply summing the same pair resources before choosing one. The smoothing credit is genuinely aggregate and lives in the three-dimensional physical mixed frame `(w,c,d)`, not in any physical pair determinant.

This is `QFORM-PAIRRESOURCE-FORCING-FALSE-MIXEDFRAME-v1`: a source-valid counterexample to an intermediate structural implication, **not** a counterexample to QFORM.

## 8. Why this is the requested bilinear-block mechanism

The direct route in Section 4 spends the two hub-to-leaf linear directions together with the dense same-side leaf square **before** any reciprocal physical minor appears. Its Fourier exponent is `5/2`, strictly integrable, so no square-root decoupling loss occurs and the final small-ball estimate is linear in interval length.

The physical-pair route does the opposite: it first localizes to a coefficient of size `m^(-1/2)`, creating `D kappa=Theta(m^(-3/2))`; the later scalar/star interpolation cannot recover that loss. The example therefore isolates the precise order-of-operations issue behind the B09 assignment.

## 9. Sharpened next debt

The first unpaid implication is now

`QFORM-SMALLPAIR-TO-MIXEDFRAME-OR-GROUPEDCROSSING-v1`:

> Starting only from the full spectral hypothesis `s_3(A)>=1`, construct in literal source coordinates a universal dichotomy: either a paid physical-pair resource is already macroscopic, or the small-pair survivor yields a mixed-hub / grouped-crossing aggregate with enough determinant/volume and sufficiently diffuse physical marginals to obtain an integrable characteristic-function envelope before reciprocal pair selection.

The family (2.2) proves that the aggregate branch is essential and supplies its model normal form. What is still missing is the general structural compiler, especially with genuinely arbitrary same-bank curvature rather than a single low-rank dense packet.

## 10. Counterexample status

The required pinned `COUNTEREXAMPLE_SEARCH.md` at `e5f71d79...` reports no valid full-target counterexample, and this run produces none. The unrestricted universal essential-density conjecture remains OPEN. The pinned source does prove the mixed-hub theorem used in Section 4 and its scope is respected exactly.
