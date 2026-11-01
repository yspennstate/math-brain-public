# fleet03/B10 — exact null-ray bank aggregation and full-bank closure

**Run:** `20260922T171741Z-fleet03-B10-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control:** revision `2026-09-22.8`  
**Assignment:** rank-three coupled case  
**Status:** new supporting theorems proved; full QFORM target **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authorized repository transport was used; native learned-memory ingestion was not verified)

## 1. Exact target and source state

The target is the universal essential-density statement for `Q=X^TAX` when the physical coordinates are independent with densities at most one and `A` has at least three eigenvalues of modulus at least one. This report stays in the exact-rank-three core

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_j(Lambda)|>=1`,

with arbitrary orientation. No spectral coordinate is declared independent.

The previous B10 run proved the transverse-null-pair estimate

`||p_Q||_infinity < 13 [|det Lambda| ||u_i wedge u_j||^2]^(-1/3)`

for two physical zero-pivot rows that are transverse. The surviving hard geometry was a high-cardinality bank of zero/near-zero pivot rows concentrated on one spectral null ray. The completed fleet02/B10 cascade construction showed that this bank can have arbitrarily many heavy peeling stages, so a bounded-depth scalar-pivot argument cannot close it.

The exact assigned partner `fleet04/B10` still had no completed current-QFORM handoff at the fresh source read; none is invented. A completed compatible fleet04 result used below is `fleet04/B18`, canonical source

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

which proves the definite-Schur physical-triple gate

`||p_Q||_infinity <= 2 sqrt(pi) [|d det B_3|]^(-1/4)`

for a physical `3x3` block `B_3` with nonzero scalar pivot `d` and definite rank-two Schur complement.

Two additional completed inputs are used only in their stated scopes:

1. `fleet03/B09`, `math-open-problems@41fc39eccdd44a0dcae6619676bf41f5ea21bb3e`: every two-dimensional orthogonal projection of the cap-one product law has joint density at most `2`.
2. The earlier B10 theorem `QFORM-DEPENDENT-PAIR-HYPERBOLIC-SQUARE-v1`, `math-open-problems@c1af196adade03e07456c8f6e783f952b0fa0e8d`, proved a dependence-tolerant hyperbolic-square density bound when one scalar factor is genuinely independent of a two-dimensional projected pair.

The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` is enforced: a conditional scalar density cap plus a bounded pair density is not treated as independence.

## 2. Hyperbolic-square theorem with a general scalar density cap

The earlier B10 theorem assumed the isolated scalar density was at most one. The exact scaling needed for a whole coordinate bank is as follows.

### Lemma 2.1 — `QFORM-DEPENDENT-PAIR-HYPERBOLIC-SQUARE-CAPK-v2`

Let `W` be independent of `(Y,Z)`. Suppose `W` has probability density at most `K`, while `(Y,Z)` has a joint probability density `h` with `||h||_infinity<=H`. Let `a,b` be nonzero and let `F,theta:R->R` be arbitrary measurable functions. Then

`T = 2 a W Y + F(Y) + b (Z+theta(Y))^2`

has an essentially bounded density satisfying

`||p_T||_infinity <= 3*2^(2/3) (HK)^(2/3) |a|^(-2/3)|b|^(-1/3)`.       (2.1)

#### Proof

Fix an output value `t` and write its density as the integral in `y` of a contribution `j_t(y)`.

First integrate in `z`. For fixed `(w,y)`, the two roots of the square map and `h<=H` give

`int h(y,z) delta(t-2awy-F(y)-b(z+theta(y))^2) dz`

` <= H |b|^(-1/2) [sigma(t-2awy-F(y))]_+^(-1/2)`,

with `sigma=sign(b)`. For a probability density `f<=K`, the one-sided decreasing rearrangement bound is

`int f(w)[s-cw]_+^(-1/2)dw <= 2 sqrt(K/|c|)`.

Indeed the maximizing cap-`K` density occupies the interval of length `1/K` adjacent to the square-root singularity. With `c=2ay`,

`j_t(y) <= sqrt(2K) H |ab|^(-1/2)|y|^(-1/2)`.                         (2.2)

Second, integrate in `w` first. For `y!=0`, the map is affine in `w`, hence

`j_t(y) <= K m(y)/(2|a||y|)`,                                          (2.3)

where `m(y)=int h(y,z)dz` and `int m=1`.

For any `R>0`, use (2.2) on `|y|<=R` and (2.3) outside:

`p_T(t) <= 4 sqrt(2K)H |ab|^(-1/2) sqrt(R) + K/(2|a|R)`.               (2.4)

Minimizing `A sqrt(R)+B/R` gives `3*2^(-2/3) A^(2/3)B^(1/3)`. Substitution yields exactly (2.1). The bound is uniform in `t`, and the same disintegration proves absolute continuity. QED.

For `K=1`, this reduces to the previously completed B10 theorem.

## 3. Exact geometry of an arbitrary null-ray bank

### Theorem 3.1 — `QFORM-EXACT-NULL-RAY-BANK-WITT-PARSEVAL-v1`

Assume exact rank three as above. Let `r in R^3` be a Euclidean unit vector satisfying the spectral null condition

`r^T Lambda r=0`.

Let `S` be any nonempty set of physical rows lying exactly on that ray:

`u_i=alpha_i r`, `i in S`,

and put

`L=sum_{i in S} alpha_i^2`, so `0<L<=1`.

Define the original-coordinate bank variable

`W=sum_{i in S} alpha_i X_i`.

Then the following statements all hold.

### (a) The bank remains independent and has a quantitative cap

`W` is independent of all complementary physical coordinates and

`||p_W||_infinity <= sqrt(2/L)`.                                      (3.1)

Proof: `W/sqrt(L)` is a unit Euclidean linear combination of independent cap-one variables, so the Rogozin-Ball scalar projection bound gives density at most `sqrt(2)`. Rescale.

### (b) The complementary covariance has an exact rank-one deficit

Writing `C=S^c` and

`V=sum_{j in C}u_j X_j`,

the Parseval frame identity gives

`sum_{j in C}u_j u_j^T = I_3-Lrr^T`.                                  (3.2)

Put

`s=||Lambda r||`, `w=Lambda r/s`,

and choose a Euclidean unit `m` perpendicular to both `r` and `w`. Because all singular values of `Lambda` are at least one,

`s>=1`.                                                               (3.3)

In the orthonormal basis `(r,w,m)`,

`Lambda = [[0,s,0],[s,a,b],[0,b,kappa]]`,                              (3.4)

for real `a,b,kappa`, and

`det Lambda = -s^2 kappa`.                                             (3.5)

Hence

`kappa!=0`, `s^2 |kappa|=|det Lambda|>=1`.                             (3.6)

### (c) Product-preserving normal form

Put `rho=1-L`. If `rho>0`, define

`R=(r dot V)/sqrt(rho)`, `Y=w dot V`, `Z=m dot V`.

The three coefficient vectors of `(R,Y,Z)` in the complementary ORIGINAL physical coordinates are orthonormal. Indeed, from (3.2),

`sum (u_j dot r)^2=rho`, `sum (u_j dot w)^2=sum (u_j dot m)^2=1`,

and every cross sum is zero. Thus `(R,Y,Z)` is an actual three-dimensional orthogonal projection of the complementary cap-one product law; no independence of its coordinates is asserted.

The full quadratic form is exactly

`Q = 2s Y (W+sqrt(rho)R) + aY^2+2bYZ+kappa Z^2`.                       (3.7)

The bank `W` is genuinely independent of the entire projected triple `(R,Y,Z)` because their physical coordinate supports are disjoint.

If `L=1`, the `R` term disappears. Equation (3.2) then has null vector `r`; positivity of the sum of rank-one outer products forces every complementary row to be orthogonal to `r`. Consequently `(Y,Z)` is a genuine two-dimensional orthogonal projection of the complementary product law.

### (d) Exact determinant mass carried by the bank

For every `i in S` and complementary pair `j<k`, exact rank three gives

`det A_{ijk}=det(Lambda) det(U_{ijk})^2`.

In the orthonormal basis `(r,w,m)`,

`det(U_{ijk})=alpha_i[(u_j dot w)(u_k dot m)-(u_k dot w)(u_j dot m)]`.

The complementary coefficient vectors of `Y` and `Z` are orthonormal even when `L<1`, so Cauchy-Binet gives

`sum_{j<k, j,k in C} det(U_{ijk})^2=alpha_i^2`.

Therefore

`sum_{j<k, j,k in C} |det A_{ijk}|=|det Lambda| alpha_i^2`,             (3.8)

and summing over the entire bank,

`sum_{i in S} sum_{j<k, j,k in C}|det A_{ijk}|=|det Lambda| L`.         (3.9)

This is an exact physical-minor mass identity. It does not claim one minor is uniformly large; delocalized minors are explicitly allowed.

QED.

## 4. The full null-ray bank is uniformly paid

The endpoint `L=1` is exactly the geometry of the arbitrarily long isotropic cascade obstruction: the obstruction can persist locally for arbitrarily many rows, but its TOTAL null-ray bank exhausts one Parseval direction. At that endpoint it admits a dimension-free density bound.

### Theorem 4.1 — `QFORM-FULL-NULL-RAY-BANK-CLOSURE-v1`

Under Theorem 3.1, if `L=1`, then

`||p_Q||_infinity <= 3*2^(5/3)|det Lambda|^(-1/3)
                  <= 3*2^(5/3)
                  < 9.525`.                                            (4.1)

#### Proof

At `L=1`, `W` is independent of `(Y,Z)` and (3.1) gives

`||p_W||_infinity<=sqrt(2)`.                                           (4.2)

The coefficient vectors of `(Y,Z)` are orthonormal in the complementary ORIGINAL coordinates, so the completed two-dimensional projection theorem gives

`||p_(Y,Z)||_infinity<=2`.                                             (4.3)

From (3.7), complete the square only algebraically in the projected pair:

`aY^2+2bYZ+kappa Z^2
 =(a-b^2/kappa)Y^2+kappa(Z+(b/kappa)Y)^2`.                              (4.4)

Apply Lemma 2.1 with scalar cap `K=sqrt(2)`, pair cap `H=2`, hyperbolic coefficient `a_hyp=s`, and square coefficient `b_sq=kappa`. This gives

`||p_Q||_infinity
 <=3*2^(2/3)(2sqrt(2))^(2/3)s^(-2/3)|kappa|^(-1/3)`

` =3*2^(5/3)(s^2|kappa|)^(-1/3)`

` =3*2^(5/3)|det Lambda|^(-1/3)`,                                     (4.5)

using the exact invariant (3.5). Since `|det Lambda|>=1`, (4.1) follows. QED.

No post-rotation independence is used: the only independence invoked is the actual disjoint-original-coordinate independence of the whole bank `W` from its complement. The pair `(Y,Z)` may be arbitrarily dependent.

### Consequence for the live long-cascade obstruction

The fleet02/B10 construction with arbitrarily many zero-pivot rows on one null ray chooses squared ray weights whose total is exactly one. Thus it lies in Theorem 4.1 and is paid uniformly by `<9.525`, independently of the cascade length. This shows why bounded-depth peeling fails but whole-bank aggregation succeeds on the exact obstruction family.

## 5. Completed fleet04 mathematics applied to an actual gate

The exact assigned fleet04/B10 artifact is still absent, so no partner claim is fabricated. The completed compatible fleet04/B18 definite-Schur theorem supplies the following actual inequality in the same rank-three reduction.

For any scale `eta>0`, if there exists a physical triple `T` with a nonzero physical pivot `d` whose rank-two Schur complement is definite and

`|d det A_T| >= eta^4`,

then fleet04/B18 gives immediately

`||p_Q||_infinity <= 2 sqrt(pi) eta^(-1)`.                             (5.1)

The new determinant identity (3.9) sharpens what failure of all such fleet04 gates means in a null-bank branch. A bank of mass `L` carries total physical triple determinant mass exactly `|det Lambda|L`. Hence, if no fleet04-compatible triple satisfies (5.1), this entire determinant mass must be distributed among triples for which either the candidate pivot/Schur sign pattern is not definite or the pivot-times-determinant scale is below `eta^4`. The determinant resource itself cannot disappear.

This is a direct use of the completed fleet04 theorem at a concrete inequality, not a status citation.

## 6. First unpaid implication after this run

The exact full-bank endpoint `L=1` is closed. The surviving null-ray geometry is the **partial bank** `0<L<1`, where (3.7) contains

`sqrt(1-L) R`

inside the hyperbolic factor. The key extra structure is stronger than a conditional density cap: `(R,Y,Z)` is an actual THREE-DIMENSIONAL ORTHOGONAL PROJECTION of the complementary original product law, and `W` is independent of that whole triple.

The first unpaid B10 implication is therefore:

> `QFORM-PARTIAL-NULL-BANK-ORTHOGONAL-TRACE-v1`. Prove a universal density bound for
>
> `2sY(W+sqrt(rho)R)+aY^2+2bYZ+kappa Z^2`,
>
> where `0<rho<1`, `W` is an independent product-linear scalar with density cap `sqrt(2/(1-rho))`, `(R,Y,Z)` is a genuine 3-D orthogonal projection of an independent cap-one product source, `s>=1`, and `s^2|kappa|>=1`.

One must use the projection's original product-linear provenance. Replacing `W+sqrt(rho)R` merely by a variable with a bounded conditional density given `(Y,Z)` is invalid by the live `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` counterexample.

This residual is strictly narrower than the previous generic 'null-ray bank aggregation' problem: its covariance, determinant scale, independence split, and exact polynomial normal form are now fixed.

## 7. Scope and regularity

This report proves essential `L^infinity` density bounds in the stated branches. It does **not** prove continuity of the output density. Continuity remains a separate target-level question.

The full arbitrary-rank / at-least-three-large-eigenvalue QFORM conjecture remains **OPEN / NOT PROVED**.
