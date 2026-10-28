SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-22T23:29:32Z.
attacking: intersecting-Pluecker support—classify the zero-disjoint-mass branch and retain an original independent scalar through the curved rank-two projection trace.

# account02/B16 — intersecting Pluecker bases and a null-coloop projection-to-curvature theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Math repository head observed before write:** `yspennstate/math-open-problems@3709de1a3f1ed1a498dcadd7d85d8de143331a36`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** `NEW SUPPORTING THEOREM + STRUCTURAL REDUCTION / FULL QFORM OPEN`.

## 1. Target and correction boundary

The full target remains open: for arbitrary independent real inputs with one-dimensional densities at most one and arbitrary symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal essential bound for the density of `X^T A X`, or give a valid counterexample.

This report uses independence only between disjoint sets of ORIGINAL input coordinates. It does not use independence after spectral rotation, the refuted arbitrary-joint coarea inequality, normalized conditional projection-height moments or suprema, law-uniform pointwise quadratic-phase decay, or a near-zero replacement of an exact null pivot. In particular, the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` is respected: a mere conditional scalar cap after an arbitrary nonlinear shear is not treated as independence.

The exact branch attacked is the zero-disjoint-Pluecker-mass obstruction left by the preceding B16 two-bank theorem. The main new analytic lemma pays the exact null-coloop case while keeping a genuinely independent physical scalar and allowing the remaining two projected coordinates to be dependent.

## 2. Source-valid inputs actually applied

### 2.1 Designated partner account03/B16: two-bank crossblock theorem

Latest completed designated-partner result read for this run:

`yspennstate/math-open-problems@a8103979d7666d4087a23134adf547ab0232c653`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T215409Z-account03-B16-QFORM-r18/REPORT.md`.

Its zero-residual-cross-block specialization, combined with the preceding B16 Pluecker half-partition identity, gives for an exact-rank-three form

`A=U Lambda U^T`, `U^T U=I_3`,

with Pluecker weights `w_S=det(U_S)^2` and disjoint-pair mass

`D_disj=sum_{S cap T=emptyset} w_S w_T`,

the already established branch

`||p_Q||_infinity <= 6 e |det Lambda|^(-1/3) D_disj^(-1/6)`            (2.1)

whenever `D_disj>0`. The partner theorem uses independent ORIGINAL-coordinate groups; no spectral-coordinate independence is asserted.

### 2.2 Designated-partner physical-triple theorem

From account03/B16:

`yspennstate/math-open-problems@b94cc7446401c02727c42024274c002e2f4e0cab`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T202347Z-account03-B16-QFORM-r15/REPORT.md`,

for any invertible original-coordinate physical `3 x 3` block `B`, after conditioning arbitrary outside original coordinates,

`||p||_infinity <= C_3 |det B|^(-1/3)`,                              (2.2)

where

`C_3=16 sqrt(30) 2^(1/4)=104.21688998922089...`.                     (2.3)

### 2.3 Weighted product-projection density theorem

From account02/B06:

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`,

if `V` has `k` orthonormal columns and `Y=V^T X` is the projection of independent cap-one inputs, then

`||p_Y||_infinity <= exp(k/2)`.                                      (2.4)

For `k=2`,

`||p_Y||_infinity <= e`.                                             (2.5)

This is a weighted Brascamp--Lieb fiber integral of the original product law, not an unrestricted fiber supremum.

### 2.4 Rank-two half-Riesz estimate

From

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

for an orthonormal two-dimensional product projection `Y=V^T X` and invertible symmetric `S`,

`sup_t E |Y^T S Y-t|^(-1/2) <=16 sqrt(30)|det S|^(-1/4)`.             (2.6)

### 2.5 Two-base packing criterion

For the finite rank-three vector matroid of nonzero physical rows I use Edmonds' base-packing criterion in the form

`two disjoint bases exist iff |E\X| >= 2(3-r(X)) for every X subset E`. (2.7)

Equivalently, if no two disjoint bases exist then some `X` satisfies

`|E\X|+2r(X)<=5`.                                                     (2.8)

This is the `k=2`, `r(M)=3` case of the classical matroid base-packing theorem (Jack Edmonds, *Lehman's switching game and a theorem of Tutte and Nash-Williams*, J. Res. Nat. Bur. Standards Sect. B 69B (1965), 73--77). Only the elementary consequences of (2.8) are used below.

## 3. Structural theorem for `D_disj=0`

Let `E` be the set of indices of the nonzero rows `r_i` of `U`. A triple is a vector-matroid basis exactly when its Pluecker weight is positive. Hence

`D_disj=0`                                                           (3.1)

is equivalent to saying that the row matroid has no two disjoint bases.

Apply (2.8). Put `r=r(X)`. Because the full row family has rank three, `r` is `0`, `1`, or `2` and:

- `r=0`: at most five nonzero rows exist;
- `r=1`: all but at most three nonzero rows lie on one spectral line;
- `r=2`: all but at most one nonzero row lie in one spectral plane.   (3.2)

The third case is much more rigid for a Parseval frame.

### Lemma 3.1 — plane witness implies an exact coloop

Assume all rows except `r_i` lie in a plane `P`, while the rows span `R^3`. Then

`||r_i||=1`, `P=r_i^perp`.                                           (3.3)

**Proof.** Parseval gives

`I_3-r_i r_i^T=sum_{j!=i} r_j r_j^T`.                                (3.4)

The right side has range in `P`, hence rank at most two. By the matrix determinant lemma,

`det(I_3-r_i r_i^T)=1-||r_i||^2=0`.                                  (3.5)

Every Parseval row has norm at most one, so `||r_i||=1`. Then `I-r_i r_i^T` is exactly the orthogonal projection onto `r_i^perp`; its range is two-dimensional and is contained in `P`, proving `P=r_i^perp`. QED.

Thus the difficult exact-intersection support does not merely contain a heavy row: in the plane-witness branch it contains a genuine leverage-one ORIGINAL coordinate, and the remaining source coordinates project into its orthogonal spectral plane.

## 4. Immediate payments for the first two structural cases

### 4.1 At most five nonzero rows

Cauchy--Binet gives `sum_S w_S=1`. With at most five nonzero rows there are at most `binom(5,3)=10` nonzero triples, so some `w_S>=1/10`. Since

`|det A[S,S]|=|det Lambda| w_S`,                                    (4.1)

and `|det Lambda|>=1`, the physical-triple theorem gives

`||p_Q||_infinity <= C_3 10^(1/3)
                   =224.52848308001404...`.                          (4.2)

### 4.2 One line plus at most three exceptional rows

All nonzero rows then occupy at most four spectral line directions. Apply the previously proved B16 theorem `QFORM-FINITE-LINE-BANK-COMPRESSION-v1`, whose canonical report is

`yspennstate/math-open-problems@b9e19e2c19ecd6f6ede282cd3c73ad014c449e9f`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T220011Z-account02-B16-QFORM-auto11/REPORT.md`.

With `K<=4` it yields

`||p_Q||_infinity <=2 C_3 binom(4,3)^(1/3)
                   =330.8680016034867...`.                            (4.3)

The line-bank variables are normalized sums over disjoint ORIGINAL coordinate sets, so their independence is genuine.

## 5. New analytic theorem: an independent scalar plus a dependent projected pair

The plane-witness branch gives an original scalar independent of the remaining two-dimensional product projection. The next theorem pays its exact null quadratic pivot without ever declaring the projected pair independent.

### Theorem 5.1 — `QFORM-NULL-SCALAR-DEPENDENT-PAIR-v1`

Let `X` be a real random variable with density `f<=1`. Let `(C,D)` be independent of `X` and have an arbitrary joint probability density `g` with

`||g||_infinity<=M`.                                                  (5.1)

For real `alpha,delta` and nonzero `beta,gamma`, put

`Q=2 beta X C + alpha C^2+2 delta C D+gamma D^2`.                    (5.2)

Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity
 <=3 (2M)^(2/3) |beta^2 gamma|^(-1/3).`                              (5.3)

Equivalently, for the symmetric matrix

`B=[[0,beta,0],[beta,alpha,delta],[0,delta,gamma]]`,                  (5.4)

whose determinant is `-beta^2 gamma`,

`boxed: ||p_Q||_infinity <=3(2M)^(2/3)|det B|^(-1/3).`               (5.5)

The theorem needs independence only between the scalar `X` and the PAIR `(C,D)`. The coordinates `C,D` may be arbitrarily dependent.

### Proof

Fix `t`. Since `(C,D)` has a density, `P(C=0)=0`. Conditional on `(C,D)=(c,d)`, the map in `X` is affine with slope `2 beta c`; therefore the output density is

`p_Q(t)=int g(c,d) K_t(c,d) dc dd`,                                  (5.6)

where

`K_t(c,d)= [1/(2|beta c|)]
 f( [t-alpha c^2-2 delta c d-gamma d^2]/[2 beta c] )`.               (5.7)

We prove a weak-`L^(3/2)` bound for this exact kernel. For `s>0`, if `K_t(c,d)>s`, then

`f(x_t(c,d))>2|beta|s|c|`,                                          (5.8)

so necessarily

`|c|<1/(2|beta|s)`.                                                   (5.9)

Fix such a nonzero `c` and put

`m=2|beta|s|c|`, `E_m={x:f(x)>m}`.                                  (5.10)

Probability normalization of `f` gives

`|E_m|<=1/m`.                                                         (5.11)

For fixed `c`, the function of `d`

`x_t(c,d)= [t-alpha c^2-2 delta c d-gamma d^2]/[2 beta c]`           (5.12)

is a quadratic with leading coefficient

`A_c=-gamma/(2 beta c)`.                                             (5.13)

For any quadratic `A(d-d_0)^2+v`, `A!=0`, and any measurable set `E` of finite length `L`,

`|{d:A(d-d_0)^2+v in E}| <=2 sqrt(L/|A|)`.                           (5.14)

Indeed, the two inverse branches have total Jacobian

`|A|^(-1/2) u^(-1/2)`

at distance `u` from the vertex value, and among sets of measure `L` the integral of `u^(-1/2)` is maximized on `[0,L]`, where it equals `2 sqrt(L)`.

Applying (5.14) with (5.11)--(5.13), the `d`-measure of the superlevel set at fixed `c` is at most

`2 sqrt( [1/(2|beta|s|c|)] [2|beta c|/|gamma|] )
 =2/(sqrt(|gamma|) sqrt(s)).`                                        (5.15)

Integrating over the `c` interval in (5.9), whose total length is `1/(|beta|s)`, gives

`|{(c,d):K_t(c,d)>s}|
 <= [2/(|beta|sqrt(|gamma|))] s^(-3/2).`                              (5.16)

Now use both the density cap and probability normalization of `g`:

`int_{K_t>s} g <= min(1, M |{K_t>s}|)`.                              (5.17)

Layer cake and (5.16) therefore give, with

`A_0=2M/(|beta|sqrt(|gamma|))`,

`p_Q(t)
 <=int_0^infinity min(1,A_0 s^(-3/2)) ds
 =3 A_0^(2/3).`                                                       (5.18)

Because `|beta|sqrt(|gamma|)=sqrt(|beta^2 gamma|)`, (5.18) is exactly (5.3). The bound is uniform in `t`, proving essential boundedness. QED.

### Why this does not violate the live conditional-cap correction

The correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` gives a dependent triple with `S=-Z^2/(2Y)+U` so that `2SY+Z^2=2YU` has a logarithmically unbounded density even though the pair and conditional scalar densities are capped. The cancellation uses a nonlinear singular shift depending on `(Y,Z)`.

Theorem 5.1 never performs such a shear: `X` remains genuinely independent of `(C,D)` and is integrated first in the original scalar coordinate. The surviving quadratic `d`-curvature produces the weak-`L^(3/2)` estimate (5.16).

## 6. Application to the exact coloop/null-pivot branch

Return to exact rank three

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_j|>=1`,                     (6.1)

and suppose the plane witness of Lemma 3.1 holds at index `i`. Put `u=r_i`, so `||u||=1`; choose an orthonormal basis `(p,q)` for `u^perp`. Because every other row lies in `u^perp`,

`U^T X = u X_i + p C+q D`,                                           (6.2)

where `(C,D)=V^T X_{-i}` for a matrix `V` with two orthonormal columns. The physical scalar `X_i` is independent of the whole pair `(C,D)`.

The weighted product-projection theorem (2.5) gives

`||p_(C,D)||_infinity<=e`.                                           (6.3)

Let `B` be the matrix of `Lambda` in the orthonormal basis `(u,p,q)`. Then

`det B=det Lambda`.                                                    (6.4)

Assume the physical coloop pivot is exactly null,

`a=A_ii=u^T Lambda u=0`.                                              (6.5)

Because `B` is invertible, its first row has a nonzero plane component. Rotate `(p,q)` orthogonally so that this component is `(beta,0)`. The plane rotation preserves (6.3), and `B` has the form (5.4). Invertibility gives `beta gamma!=0` and

`|beta^2 gamma|=|det B|=|det Lambda|`.                               (6.6)

Theorem 5.1 with `M=e` yields the source-valid curved-pushforward bound

`boxed: ||p_Q||_infinity
 <=3(2e)^(2/3)|det Lambda|^(-1/3)
 <=3(2e)^(2/3)
 =9.275505197173393... .`                                            (6.7)

This is `QFORM-NULL-COLOOP-PROJECTION-TRACE-v1`.

It is exactly the projection-product interaction requested by this slot: the two projected coordinates are allowed to be dependent; only their proved joint density cap is used, while the isolated physical scalar remains genuinely independent and the curved `D^2` direction is retained to the end.

## 7. Nonzero coloop pivot and the remaining exact endpoint gap

If instead `a=A_ii!=0`, complete the square only in the independent scalar `X_i`. The two-dimensional Schur matrix satisfies

`det S=det Lambda/a`.                                                  (7.1)

Conditional on `(C,D)`, the translated scalar still has density cap one. Applying (2.6) to the genuine two-dimensional product projection gives

`||p_Q||_infinity
 <=16 sqrt(30) |a det Lambda|^(-1/4).`                               (7.2)

Thus, for example, whenever `|a|>=1/16`,

`||p_Q||_infinity<=175.27121840165316...`.                            (7.3)

The exact null endpoint (6.7) is also uniformly paid. What remains unpaid by this synthesis is the **near-null but nonzero** coloop regime `0<|a|<1/16` (or, invariantly, the limit `a->0` in (7.2)) when the plane rows are not already captured by the finite-line branch. The live correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` is precisely why (7.2) may not simply be declared uniform at `a=0` by continuity of the proof mechanism.

This is now a sharply localized exact-rank-three debt, rather than an undifferentiated failure of projection methods.

## 8. Explicit many-direction stress family for the null-coloop theorem

The null-coloop branch is not secretly a finite-line-bank case. Let

`Lambda=diag(1,1,-1)`,
`u=(1,0,1)/sqrt(2)`,
`p=(1,0,-1)/sqrt(2)`,
`q=(0,1,0)`.                                                          (8.1)

Then `(u,p,q)` is orthonormal and in this basis

`Lambda` has quadratic matrix

`[[0,1,0],[1,0,0],[0,0,1]]`.                                         (8.2)

For any `m>=3`, take physical rows

`r_0=u`,
`r_k=sqrt(2/m)[cos(2 pi k/m) p+sin(2 pi k/m) q]`, `1<=k<=m`.         (8.3)

The trigonometric identities give

`sum_k r_k r_k^T=I_3`,                                               (8.4)

so this is a valid Parseval spectral frame. Every basis must contain the coloop row `r_0`; consequently `D_disj=0`. The plane rows have `m` distinct directions (up to the obvious antipodal identifications), so no bounded-line-complexity explanation is available as `m` grows.

In the `(u,p,q)` coordinates the full quadratic form is exactly

`Q=2 X_0 C+D^2`,                                                     (8.5)

where

`C=sqrt(2/m) sum_k cos(2 pi k/m) X_k`,
`D=sqrt(2/m) sum_k sin(2 pi k/m) X_k`.                               (8.6)

The pair `(C,D)` is generally dependent because it reuses the same original inputs, yet (6.7) gives

`||p_Q||_infinity<=9.276`                                            (8.7)

for every choice of independent cap-one input laws. This is a target-valid supporting family, not a counterexample.

## 9. Synthesis and first unpaid implication

For an exact-rank-three frame:

1. `D_disj>0`: the latest account03/B16 two-bank theorem gives (2.1), quantitatively in `D_disj`.
2. `D_disj=0`: Edmonds' two-base packing criterion yields one of the three structures (3.2).
3. The rank-zero witness is paid by one physical triple, (4.2).
4. The rank-one witness is paid after legitimate finite line-bank compression, (4.3).
5. The rank-two witness is an exact leverage-one coloop. Its exact null pivot is paid by the new dependent-pair theorem, (6.7), and a quantitatively nonzero pivot is paid by (7.2).

The first unpaid exact-rank-three implication is therefore a **near-null coloop interpolation**, robust for `0<|A_ii|<<1`, which must use the surviving original scalar/pair product provenance rather than the refuted near-zero half-Riesz-only shortcut. A quantitative stability version of the base-packing reduction is also required when `D_disj` is small but nonzero rather than exactly zero.

For arbitrary higher-rank `A`, the latest account03/B16 augmented-bank theorem remains the compatible exit when residual cross singular directions are quantitatively transverse. The present exact-rank-three coloop proof cannot delete an arbitrary complementary quadratic form on the same original coordinates; that full-matrix synthesis remains unpaid.

**Full QFORM status: OPEN / NOT PROVED / NOT DISPROVED.**
