SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T18:58:27Z.
attacking: combine the new marginal-free physical three-volume crossing theorem with the target-level first-volume floor and weighted physical-pivot completion, optimizing the V2 split to force a finite-hub zero-diagonal twist of order rho^{-3/2}.

# account03/B13 r32 — finite-hub rho^{-3/2} normal form

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: extremal product laws. Execution: `WITHOUT_VERIFIED_BRAIN`.

Status: **NEW PROVED TARGET-LEVEL STRUCTURAL THEOREM / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, post-rotation independence, single-interval extremality, support-diameter bound, or perturbative deletion of a small quadratic tail is used.

## 1. Source-pinned premises and exact scopes

Let

`rho = P{X^T A X in J}/|J|`

for a nonempty interval `J`, and assume the target spectral hypothesis `s_3(A)>=1`.

### 1.1 Designated account04/B13 extremal-product theorem

The completed account04/B13 theorem states that every cap-one mass-one marginal is an `L1` limit of convex mixtures of indicators of bounded finite unions of intervals of total measure one. Consequently, for every bounded nonnegative product kernel (in particular a slab indicator),

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i`
` = sup_{|E_i|=1} int_{prod E_i} K`,

with the right side unchanged if each `E_i` is a bounded finite union of intervals. No optimizer, common diameter, or fragment-count bound is asserted.

Source: `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

### 1.2 Marginal-free physical three-volume crossing

For an actual original-coordinate cut `I|Jc`, put `M=A[I,Jc]` and

`Z_3(M)=e_3(M^T M)`.

The new account02/B03 theorem proves, with arbitrary same-side quadratic terms, arbitrary affine terms and arbitrary additional cross rank retained,

`||p_Q||_infinity <= C_3 Z_3(M)^(-1/6)`,

where

`C_3 = 3*2^(4/3)*e^(1/3) = 10.5501688311648...`.

Equivalently every actual slab witness obeys

`Z_3(M) <= (C_3/rho)^6`.                                      (1.1)

Source: `yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`, account02/B03 marginal-free `Z3` crossing report. The interactive continuation records a second check of the crucial heavy-row promotion cases.

### 1.3 First exterior-volume spectral floor

Write

`V_r(A)=sum det A[S,T]^2`,

where the sum runs over ordered disjoint physical `r`-sets `S,T`. Thus

`V_1(A)=sum_{i!=j} a_ij^2`.

The completed account01/B13 target-level floor gives, for

`c_0=6 sqrt(pi)=10.6347231054331...`

and every `rho>c_0`,

`sqrt(V_1) >= (1-c_0/rho)/2`,

hence, with

`eta = 1-c_0/rho >0`,

`V_1 >= eta^2/4`.                                              (1.2)

Source: `yspennstate/math-open-problems@d46798d03befd93be417b47527c369fc9d8195bc`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T182826Z-account01-B13-qform-auto11/REPORT.md`, Lemma 2.1.

### 1.4 Weighted physical-pivot complement completion

The preceding account03/B13 run proved: if `V_r>0`, then some nonsingular disjoint physical `r x r` pivot, with at most `2r` original hub coordinates removed, leaves complement `K` satisfying

`A[K,K]=D+R+E`,

where `D` is diagonal, `R` is symmetric of rank at most `2r`, `E` is symmetric zero-diagonal, and

`||E||_F <= (r+1) sqrt(V_{r+1}/V_r)`.                         (1.3)

The result is an exact bordered-determinant/deletion-counting theorem in the original coordinates. No random variable is rotated and no residual is discarded.

Source: `yspennstate/math-open-problems@14ceede15c310637139375332c84f4d8620b5599`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T183034Z-account03-B13-qform-r31/REPORT.md`, Theorem 2.1.

## 2. New global third-volume estimate with the improved crossing constant

### Lemma 2.1 — `QFORM-MARGINALFREE-GLOBAL-V3-v1`

Every target-class slab witness satisfies

`boxed: V_3(A) <= 64 C_3^6 rho^(-6).`                           (2.1)

#### Proof

Choose a fair Bernoulli physical cut: every original coordinate is placed independently in `I` or `Jc` with probability `1/2`. For a fixed ordered disjoint pair of physical triples `(S,T)`, the event `S subset I, T subset Jc` has probability `2^(-6)=1/64`. Cauchy--Binet therefore gives the exact expectation

`E_cut e_3(A[I,Jc]^T A[I,Jc]) = V_3(A)/64`.                     (2.2)

For every realized cut, (1.1) gives

`e_3(A[I,Jc]^T A[I,Jc]) <= (C_3/rho)^6`.                        (2.3)

Average (2.3) and use (2.2). QED.

This replaces the earlier aggregate constant based on a row-marginal-gated crossing theorem by the currently stronger marginal-free theorem.

## 3. Main result: optimized V2 split gives a finite-hub rho^{-3/2} twist

Define

`T(rho) = 6 C_3^3 eta rho^(-3)`,

where `eta=1-c_0/rho`.

### Theorem 3.1 — `QFORM-FINITE-HUB-RHO32-NORMAL-FORM-v1`

For every target-class matrix and every actual slab ratio `rho>c_0`, there is a set `H` of at most four **original coordinates**, with complement `K`, such that

`boxed: A[K,K]=D_K+R_K+E_K,`                                    (3.1)

where `D_K` is diagonal, `R_K` is symmetric with `rank R_K<=4`, and `E_K` is symmetric zero-diagonal, with

`boxed:
 ||E_K||_F <= K_* eta^(-1/2) rho^(-3/2),`                        (3.2)

where

`K_* = 4 sqrt(6) C_3^(3/2)`
`    = 335.756733349986... .`                                    (3.3)

More precisely:

- if `V_2 >= T(rho)`, one may take at most four hubs and `rank R_K<=4`;
- if `V_2 < T(rho)`, one may take at most two hubs and `rank R_K<=2`.

For the convenient uniform regime `rho>=2c_0=12 sqrt(pi)=21.2694462108662...`,

`boxed: ||E_K||_F <= 474.831725961637 rho^(-3/2).}`               (3.4)

In particular every hypothetical sequence with `rho_m -> infinity` admits finite physical hub sets `|H_m|<=4` for which

`boxed: rho_m ||E_m||_F ->0.`                                    (3.5)

#### Proof

**Case A: `V_2 >= T(rho)`.** Apply the weighted pivot theorem (1.3) with `r=2`. It leaves at most four original hubs and `rank R_K<=4`, with

`||E_K||_F <= 3 sqrt(V_3/V_2)`.

Using (2.1) and the Case A lower bound,

`||E_K||_F`
` <=3 sqrt(64 C_3^6 rho^(-6)/(6 C_3^3 eta rho^(-3)))`
` = [24 C_3^3/sqrt(6 C_3^3 eta)] rho^(-3/2)`
` =4 sqrt(6) C_3^(3/2) eta^(-1/2) rho^(-3/2).`                   (3.6)

**Case B: `V_2 < T(rho)`.** The first-volume floor (1.2) implies `V_1>0`. Apply (1.3) with `r=1`; after at most two physical hubs,

`rank R_K<=2`, and

`||E_K||_F <=2 sqrt(V_2/V_1)`
` <2 sqrt( [6 C_3^3 eta rho^(-3)]/[eta^2/4] )`
` =4 sqrt(6) C_3^(3/2) eta^(-1/2) rho^(-3/2).`                   (3.7)

The same constant appears on both sides because `T(rho)` was chosen to balance the two pivot levels. This proves (3.1)-(3.3). If `rho>=2c_0`, then `eta>=1/2`, so multiplying `K_*` by `sqrt(2)` gives (3.4). Finally (3.5) follows directly because `eta->1`. QED.

### Why the exponent matters

The previous finite-hub result had only `||E||_F=O(rho^-1)`. The separate rank-sixteen exterior bootstrap improved the exponent to `rho^-5/4` but did not retain a finite physical hub set. Theorem 3.1 simultaneously retains at most four named physical hubs, rank at most four on the complementary carrier, and obtains the strictly smaller density-scale twist

`||E||_F=O(rho^-3/2)`.

This is a coefficient normal form, not a claim that `E` may be deleted on arbitrary unbounded fragmented supports.

## 4. New pivotwise tradeoff

The preceding weighted-pivot proof also gives, for **every** nonsingular disjoint physical `2 x 2` pivot `B=A[S,T]`, with `K=(S union T)^c`,

`|det B| dist_F(A[K,K], Diag+SymRank<=4) <= sqrt(V_3(A)).`        (4.1)

Combining with (2.1),

`boxed:
 |det B| dist_F(A[K,K], Diag+SymRank<=4)
 <= 8 C_3^3 rho^(-3)`                                           (4.2)

and

`8 C_3^3 = 9394.38199915446... .`                               (4.3)

Thus any moderately large physical two-pivot forces its complementary self-curvature to be extremely close to diagonal plus rank four at the stronger `rho^-3` weighted scale.

## 5. Actual use of the designated account04/B13 result

The conclusions above can be proved directly for rough cap-one laws because the analytic inputs already have that scope. To apply the designated partner theorem at an **actual inequality**, proceed instead from unit-product indicators and then transfer the two deterministic currency inequalities used in Theorem 3.1.

Let arbitrary cap-one product densities give slab ratio `rho`. For every `epsilon>0`, account04/B13 purification supplies a bounded finite-union unit-product indicator witness for the same `A,J` with slab ratio at least `rho-epsilon`. Applying Lemma 2.1 and the first-volume floor to that witness yields

`V_3(A) <=64 C_3^6 (rho-epsilon)^(-6)`,

`V_1(A) >= (1/4)(1-c_0/(rho-epsilon))^2`

whenever `rho-epsilon>c_0`. The currencies depend only on `A`, so letting `epsilon downarrow0` gives exactly (2.1) and (1.2) for the original rough law. The deterministic pivot optimization then gives Theorem 3.1 with **zero constant loss**. No interval, centered-uniform, support-radius, or bounded-fragment extremality is used.

## 6. What remains open

The unrestricted QFORM conjecture remains **OPEN / not proved / not disproved**. Global continuity also remains **OPEN**.

The new first B13 obligation is

`QFORM-FINITE-HUB-RANK4-SUBDENSITY-TWIST-GLUE-v1`:

use the fact that in every hypothetical high-ratio sequence the retained zero-diagonal twist now satisfies `rho ||E||_F ->0`, while only four original hubs and a rank-four complementary carrier remain. The twist must not simply be deleted: arbitrarily separated product supports can magnify tiny coefficients. A valid closure must either absorb the twist into a grouped/projected-crossing receiver, or prove a product-geometric stability estimate that is uniform under translations and arbitrary fragmentation.

The exact `V_3=0` endpoint from r31 remains available: after at most four physical hubs the complement is exactly diagonal plus rank at most two (or lower), but that exact endpoint alone does not settle the positive-small-`V_3` chamber.

## 7. Computation check

The constants are algebraic consequences of

`C_3=3*2^(4/3)*e^(1/3)`, `c_0=6*sqrt(pi)`,

`K_*=4*sqrt(6)*C_3^(3/2)`, and `8*C_3^3`.

A sibling deterministic check records their decimal values and verifies that the two Case A/Case B constants coincide symbolically under the optimized threshold.