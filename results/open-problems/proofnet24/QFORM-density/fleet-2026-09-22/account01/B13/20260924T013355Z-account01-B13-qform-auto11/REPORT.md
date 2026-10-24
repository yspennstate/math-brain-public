# account01/B13 — exact product purification and tau-clean physical-bank reduction

Programme: `QFORM-DENSITY-3EIG-20260922`.

Run: `20260924T013355Z-account01-B13-qform-auto11`.

Status: **supporting theorem only**. The unrestricted quadratic-form bounded-density conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The separately stronger continuity conclusion remains OPEN.

This report keeps arbitrary dimension, arbitrary independent cap-one input densities, indefinite/rotated matrices, and fragmented supports. It does not assume centered uniforms, interval supports, bounded diameter, a uniform fragment count, or independence after an orthogonal rotation.

## 1. Exact witnesswise extremal-product purification

### Theorem 1 — `QFORM-EXACT-WITNESSWISE-PRODUCT-PURIFICATION-v1`

Let `K : R^n -> [0,M]` be bounded, nonnegative and measurable. Let `f_i` be probability densities satisfying

```
0 <= f_i <= 1,       integral_R f_i = 1.
```

Then there exist measurable sets `E_i subset R`, each of Lebesgue measure one, such that

```
integral K(x) prod_i 1_{E_i}(x_i) dx
    >=
integral K(x) prod_i f_i(x_i) dx.                    (1)
```

Consequently

```
sup_{0<=f_i<=1, int f_i=1} integral K prod_i f_i
 = sup_{|E_i|=1} integral_{prod_i E_i} K.              (2)
```

This is a witnesswise statement: no global maximizer is asserted.

### Proof

First prove the one-coordinate bathtub fact in exactly the form needed here. Let `h:R->[0,M]` be bounded, nonnegative and measurable, and let `0<=f<=1`, `int f=1`. Choose a threshold `t>=0` such that

```
|{h>t}| <= 1 <= |{h>=t}|,
```

with the standard convention at `t=0`: if `|{h>0}|<1`, fill the remaining measure from the zero level set. Because Lebesgue measure is nonatomic, choose a measurable `E` satisfying

```
{h>t} subset E subset {h>=t},       |E|=1.
```

Then on `E`, `h-t>=0`, while on `E^c`, `h-t<=0`. Since `0<=f<=1`,

```
(1_E-f)(h-t) >= 0
```

pointwise. Also `int(1_E-f)=0`. Hence

```
int_E h - int h f
 = int (1_E-f)(h-t) >= 0.                            (3)
```

Now start from `(f_1,...,f_n)`. Holding all but the first marginal fixed, define

```
h_1(x_1)=integral K(x_1,x_2,...,x_n) prod_{j>=2} f_j(x_j) dx_2...dx_n.
```

Because `K` is bounded and the other factors are probability densities, `0<=h_1<=M`. Apply (3) to replace `f_1` by `1_{E_1}`, `|E_1|=1`, without decreasing the objective. Repeat for coordinates `2,...,n`, each time using the already purified earlier coordinates and the unpurified later coordinates in the fiber function. There are only finitely many coordinates, so after `n` steps one obtains (1). The reverse inequality in (2) is immediate because every `1_E` with `|E|=1` is itself an admissible cap-one probability density. QED.

### QFORM consequence

For a fixed symmetric `A` and interval `J`, take

```
K(x)=1_{ {x^T A x in J} }.
```

If an actual cap-one product law has slab ratio

```
rho = P{X^T A X in J}/|J|,
```

then there are measurable unit-measure sets `E_i` such that, for the **same A and same J**,

```
| {x in prod_i E_i : x^T A x in J} | >= rho |J|.     (4)
```

Thus any strict counterexample witness can be taken to be a product-indicator witness with zero loss in the slab ratio.

### Bounded finite-union approximation, and its exact limitation

For a strict witness, each measurable finite-measure `E_i` can be approximated in symmetric difference by a bounded finite union of intervals `F_i`, and then altered on a set of arbitrarily small measure so that `|F_i|=1` exactly. For product indicators,

```
| prod_i E_i Delta prod_i F_i | <= sum_i |E_i Delta F_i|, (5)
```

so the slab volume changes by at most the right-hand side. Hence strict witnesses can be approximated arbitrarily well by bounded finite-union unit sets.

There is no uniform diameter bound and no uniform bound on the number of components. In particular this result does **not** strengthen to a centered interval or single-interval extremizer.

## 2. Designated partner result actually applied

The completed designated partner result used in this run is account02/B13 r38, canonical source

```
yspennstate/math-open-problems@3da714c7dea66b4f81087bf9637a6eac060b5b6a
proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/
20260923T235922Z-account02-B13-qform-r38/REPORT.md
```

In its exact diffuse rank-two hard branch,

```
A = D + U Lambda U^T,
U^T U = I_2,
max_i ||u_i||^2 <= 1/3,
```

with slab ratio `rho`, a physical coordinate `k` is selected with `|d_k|>=1`. For physical pairs `E={r,s}` disjoint from `k`, put

```
q_E       = det(U_E)^2,
Delta_E   = sum_{F: |F|=2, F cap (E union {k})=empty} q_F,
W_k       = sum_E q_E Delta_E,
mu_k(E)   = q_E Delta_E/W_k,
tau_{rs}  = d_k q_{rs} + d_r q_{ks} + d_s q_{kr}.
```

The partner proves

```
W_k >= 1/12.                                             (6)
```

In its hard non-rank-one branch,

```
|det Lambda| > sqrt(1536)*e*rho^{-2},                    (7)
E_{mu_k}|tau_E| < 267.630809135 rho^{-1}.                (8)
```

Therefore the good set

```
G={E: |tau_E| <= T rho^{-1}},
T=535.261618270,
```

has `mu_k(G)>=1/2`. The partner then proves there is an **original-coordinate** partition

```
C sqcup C^c = [n]\{k}
```

such that

```
Z_G(C)
 := sum_{E subset C, E in G}
      sum_{F subset C^c, |F|=2} det A[E,F]^2
 >= (det Lambda)^2/384
 > 4 e^2 rho^{-4}.                                      (9)
```

Every row pair `E` counted in (9) is tau-clean. No post-rotation independence is used.

## 3. Partner crossing hides an absolute two-sided frame lower bound

### Theorem 2 — `QFORM-TAUCLEAN-CROSSING-FRAME-BALANCE-v1`

For the physical cut `C` supplied by (9), define

```
Q_G(C) = sum_{E subset C, E in G} q_E,
Q(C^c) = sum_{F subset C^c, |F|=2} q_F.
```

Then

```
Q_G(C) Q(C^c) >= 1/384.                                 (10)
```

In particular

```
Q_G(C) >= 1/384,                                        (11)
det(U_C^T U_C) >= 1/384,                               (12)
det(U_{C^c}^T U_{C^c}) >= 1/384.                       (13)
```

Consequently

```
lambda_min(U_C^T U_C) >= 1/384,
lambda_min(U_{C^c}^T U_{C^c}) >= 1/384,                (14)
```

and therefore

```
s_2(U_C), s_2(U_{C^c}) >= 1/sqrt(384).                 (15)
```

### Proof

For disjoint physical two-sets `E,F`, the diagonal part `D` vanishes on the cross block and

```
A[E,F]=U_E Lambda U_F^T.
```

Because all three factors are `2x2`,

```
det A[E,F]^2=(det Lambda)^2 q_E q_F.                   (16)
```

Every `E subset C` and `F subset C^c` is disjoint, so (16) factorizes the entire partner sum:

```
Z_G(C)=(det Lambda)^2 Q_G(C) Q(C^c).                   (17)
```

Combining (17) with the first inequality in (9) gives (10).

By Cauchy--Binet,

```
sum_{E subset S, |E|=2} q_E = det(U_S^T U_S)           (18)
```

for every physical coordinate set `S`. Since `U^T U=I_2`,

```
0 <= U_S^T U_S <= I_2,
```

hence the determinant in (18) is at most one. Therefore each factor in (10) is at most one; this gives (11) and (13). Also `Q_G(C)` is a subsum of the full determinant sum over `C`, giving (12).

Finally, if a positive semidefinite `2x2` matrix `G` obeys `G<=I_2`, its eigenvalues satisfy `0<=lambda_2<=lambda_1<=1`, so

```
lambda_2 >= lambda_1 lambda_2 = det G.
```

Apply this to the two Gram matrices to get (14)-(15). QED.

The significance is that the partner's `rho^{-4}` physical two-volume certificate is not merely a tiny-minor statement: after cancelling the hard-branch determinant scale it forces both sides of one actual original-coordinate cut to contain quantitatively nondegenerate rank-two coefficient frames.

## 4. A rho^{-1/5} physical-bank dichotomy

We now use the tau-clean aggregate itself, before choosing or inverting any single physical minor.

Since the hard branch has `|d_k|>=1` and `|A_{kk}|=O(rho^{-2})`, for `rho` in the genuinely high-density regime the selected carrier row `u_k` is nonzero. Make a deterministic orthogonal change **only in the two-dimensional coefficient representation** so that

```
u_k=(sqrt(c),0),       c=||u_k||^2>0.                  (19)
```

This changes neither `A` nor any random coordinate. Write

```
u_i=(x_i,y_i),
s_i=y_i^2=q_{ki}/c.
```

When `s_i>0`, set `r_i=x_i/y_i`.

### Exact identities

For every `i`, the Parseval frame relation `sum_j u_j u_j^T=I_2` gives

```
sum_{j != i} q_{ij}=||u_i||^2=:c_i.                    (20)
```

Indeed, the left side is the sum of squared wedge products of `u_i` with a Parseval frame, equal to `||u_i||^2`.

For `i,j` with `s_i s_j>0`,

```
q_{ij}=s_i s_j (r_i-r_j)^2,                             (21)
```

and the transverse cancellation invariant factors exactly as

```
tau_{ij}
 = s_i s_j [ d_k(r_i-r_j)^2
             + c d_i/s_i + c d_j/s_j ].                (22)
```

These are coefficient identities, not probabilistic rotations.

### Theorem 3 — `QFORM-TAUCLEAN-PHYSICAL-BANK-ONEFIFTH-v1`

Put

```
alpha=rho^{-2/5},
H={i in C: s_i<alpha},
V=C\H,
epsilon=1/384.
```

Because `Q_G(C)>=epsilon`, at least one of the following two alternatives holds.

#### Alternative H: fixed-mass hub-strip bank

The tau-clean `q`-mass of good edges touching `H` is at least `epsilon/2`. Then

```
sum_{i in H} c_i >= 1/768,                              (23)
```

while every such physical coefficient row obeys

```
dist(u_i,span(u_k))=|y_i|<rho^{-1/5}.                   (24)
```

Thus a fixed amount of physical row leverage is trapped in a `rho^{-1/5}` tube around the selected hub line.

There is a useful further deterministic split. Since

```
sum_{i in H} c_i=sum_{i in H}(x_i^2+y_i^2)>=1/768,
```

either

```
sum_{i in H} x_i^2 >=1/1536,                           (25)
```

or

```
sum_{i in H} y_i^2 >=1/1536.                           (26)
```

In the second case, because each `y_i^2<rho^{-2/5}`,

```
|H| > rho^{2/5}/1536.                                   (27)
```

So the strip endpoint is itself either a quantitatively strong along-hub bank or a genuinely high-cardinality physical bank.

#### Alternative V: fixed-condition transverse tau-clean bank

The tau-clean `q`-mass of good edges entirely in `V` is greater than `epsilon/2`. Then

```
sum_{E subset V, E in G} q_E >1/768,                   (28)
```

hence by Cauchy--Binet

```
det(U_V^T U_V)>1/768,
lambda_min(U_V^T U_V)>1/768.                            (29)
```

For every counted good edge `E={i,j} subset V`, `s_i,s_j>=alpha`, and (22) together with `|tau_{ij}|<=T rho^{-1}` gives the uniformly paid normalized curvature estimate

```
| d_k(r_i-r_j)^2 + c d_i/s_i + c d_j/s_j |
 <= T rho^{-1} alpha^{-2}
 = 535.261618270 rho^{-1/5}.                            (30)
```

Thus one actual original-coordinate physical bank carries a fixed amount of rank-two Pluecker volume, a fixed lower frame condition, and uniformly small normalized tau curvature; no individual `q_{ij}` or `q_{ki}` is inverted.

### Proof

Let `M_H` be the sum of `q_E` over good edges `E subset C` touching `H`. If `M_H>=epsilon/2`, then by (20)

```
M_H <= sum_{i in H} sum_{j != i} q_{ij}
     = sum_{i in H} c_i,
```

which gives (23). Equation (24) is immediate from `s_i=y_i^2<alpha`. The split (25)-(27) is elementary.

If `M_H<epsilon/2`, then because the total good-edge mass is at least `epsilon`, the good edges entirely in `V` have mass greater than `epsilon/2`, giving (28). The full Cauchy--Binet sum over all pairs in `V` dominates this good subsum, proving the determinant part of (29); the eigenvalue part follows as in Theorem 2 because `U_V^TU_V<=I_2`. Finally `s_i s_j>=alpha^2`, so divide (22) by `s_i s_j` and use the good-edge tau bound to obtain (30). QED.

### Why the exponent 1/5 is natural for this split

If one uses a threshold `alpha=rho^{-a}`, the hub tube radius is `alpha^{1/2}=rho^{-a/2}`, while the normalized tau error after division by `s_i s_j>=alpha^2` is `rho^{-1+2a}`. Equalizing exponents,

```
a/2 = 1-2a,
```

gives `a=2/5` and common exponent `1/5`. Thus `rho^{-1/5}` is the balanced scale of this two-branch mechanism.

## 5. Extremal-product form of the new obstruction

Combining Theorem 1 with Theorems 2-3: if a cap-one product law in the partner r38 hard exact-rank-two chamber produces slab ratio `rho`, then a unit-measure product-indicator witness exists for the same matrix and slab, and the coefficient matrix must satisfy the following deterministic alternative on an actual physical bank:

1. a fixed aggregate leverage `>=1/768` lies within physical coefficient-line distance `<rho^{-1/5}` of the selected hub line, with the refinement (25)-(27); or
2. there is a physical bank `V` with `lambda_min(U_V^T U_V)>1/768`, good-pair Pluecker mass `>1/768`, and every counted pair obeys (30).

This is a geometric sublevel-set obstruction: a hypothetical sequence of increasingly bad product-set witnesses in this chamber must organize a fixed amount of coefficient-frame mass into one of these two increasingly rigid geometries.

## 6. Diagnostics

Finite random-matrix checks were used only as diagnostics, not as proof. For random Parseval two-frames, the following identities were checked numerically over repeated trials:

```
sum_{i<j in S} det(u_i,u_j)^2 = det(U_S^T U_S),
sum_{j != i} det(u_i,u_j)^2 = ||u_i||^2,
det A[E,F] = det Lambda det U_E det U_F   (E cap F=empty),
```

and the normalized form (22) after deterministic latent-frame alignment. All tested residuals were at floating-point roundoff. The proofs above are exact and do not depend on these checks.

## 7. Corrections explicitly retained

- Uniform lawwise pointwise quadratic oscillatory decay is false.
- Orthogonal rotations of the coefficient matrix do not preserve input independence; no random variable is rotated here.
- Projection-density bounds alone do not solve indefinite quadratic pushforward.
- The constant `pi` is only a diagonal control theorem, not a universal constant.
- The arbitrary-joint coarea and positive conditional-density moment gates are false.
- A single well-conditioned local cross minor is not forced by the three-large-eigenvalue hypothesis.
- Bounded-diameter localization and a universal finite fragment-count bathtub reduction are false.
- Small coefficient tails are not silently discarded as probabilistically small on fragmented supports.

## 8. What remains unpaid

The first unpaid implication is

`QFORM-PHYSICAL-BANK-15-TO-PRODUCT-RECEIVER-v1`:

consume Alternative H or Alternative V directly in a product-preserving density/small-ball receiver. In Alternative H, aggregate the entire near-hub strip before paying reciprocals; use either the fixed along-hub energy (25) or the high-cardinality conclusion (27). In Alternative V, exploit the fixed frame conditioning (29) together with the normalized tau identity (30), while keeping every same-bank quadratic term and every outside coupling. In the general non-exact-rank-two survivor, retain the already-proved every-physical-cut `s_5=O(rho^{-1})` tail inside the phase rather than deleting it.

No valid counterexample is produced in this run, and the full theorem is not claimed.
