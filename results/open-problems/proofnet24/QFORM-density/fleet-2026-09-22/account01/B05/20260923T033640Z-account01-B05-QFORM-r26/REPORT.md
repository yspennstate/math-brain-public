SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T03:36:40Z.
attacking: diffuse Schur-direction grouping; derive an exact ratio-variance packet decomposition, close the exact rank-one packet by three-scalar coarea, and isolate the singular product-projection transition that remains.

# account01/B05 QFORM r26 — ratio-variance packets and exact parallel-group closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound.  
**Startup control:** `yspennstate/math-research-brain@970d23e14326fecdce987acffe8a4ed8f2a641b1`; OWNER CONTROL revision `2026-09-22.15`, QFORM only.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval was used; repository transport is not native learned-memory ingestion).  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_REDUCTION_PROVED / EXACT_ENDPOINT_CLOSED / PRECISE_MISSING_FACTOR_IDENTIFIED`.  
**Full QFORM:** `OPEN_NOT_PROVED`.  
**Continuity:** `NOT_PROVED`; the endpoint theorem below gives only absolute continuity and an essential-supremum bound.

## 1. Compact conditional end-to-end argument

The preceding B05 report reduced the punctured double-zero branch of the exact-rank-three aggregate geometry to the following data. One original-coordinate bank `G1` carries a two-dimensional Parseval projection

```
L=(U,T)=C^T X_G1,        C^T C=I_2,
```

and two disjoint rank-one banks give independent normalized scalar projections `Y,Z`, each with density cap at most `sqrt(2)`. In a basis in the first bank chosen along the rank-one Schur direction, the compressed quadratic matrix is

```
K = [[C0, P],
     [P^T, B]],
B = [[a,c],[c,d]],
```

and, whenever `B` is invertible,

```
C0-P B^(-1) P^T = lambda e1 e1^T,
mu = |det B| |lambda|.                                                (1.1)
```

The hard regime is `mu` bounded below, `||B||op ->0`, and the physical Schur direction

```
u=C e1
```

diffuse, so `max_i u_i^2 ->0`. Report r25 paid the complementary heavy-coordinate branch by retaining one original coordinate `X_i`; its exact three-scalar determinant is `mu u_i^2`.

The present run does not select one coordinate. Instead it groups a **constant fraction of the total Schur-direction mass** before taking any reciprocal determinant. The grouping has an exact one-parameter description: on every packet the second first-bank coefficient equals a common slope times the Schur coefficient plus an orthogonal residual. The residual norm is exactly the square root of a weighted ratio variance.

The exact rank-one endpoint of this packet decomposition is completely paid: if the residual vanishes, the whole packet collapses to one genuine scalar projection of an original-coordinate product block, independent of `Y,Z`, and r25's determinant-normalized three-scalar coarea theorem gives a bound depending on the packet mass, not on its cardinality or any individual `u_i`.

The generic packet has a nonzero orthogonal residual. It is then a genuine two-dimensional **product projection** with a joint density cap `e`, but its two coordinates are generally dependent. Conditioning on that residual is forbidden: the live correction stream contains explicit cap blow-up after conditioning conjugate projections. This leaves one very specific singular transition: prove a uniform coarea bound as the second product-projection coefficient tends to zero, without conditioning it and without replacing its product provenance by an arbitrary bounded joint density.

## 2. Sources actually consumed

### 2.1 Own predecessor r25 — determinant-normalized three independent scalars

Canonical source:

`yspennstate/math-open-problems@3e8704eead81b6fef2d305978ec89abb307d899a`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T025431Z-account01-B05-QFORM-r25/REPORT.md`.

It proves: if `X1,X2,X3` are independent scalar variables with density caps `L1,L2,L3`, `M` is real symmetric invertible `3x3`, and the affine part is arbitrary, then

```
||p_(X^T M X+ell^T X+c)||inf
 <= C3 (L1 L2 L3)^(2/3) |det M|^(-1/3),
C3=8 sqrt(2) 3^(3/4)<25.8.                                         (2.1)
```

The proof is product-preserving and does not use the refuted arbitrary-joint 3D coarea lemma.

### 2.2 Assigned partner account02/B05 — scalar-Schur coarea

Canonical source:

`yspennstate/math-open-problems@e06922bfa31bbd225cdce6ee6aea563254e62563`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T122133Z-b05-qform-5c41e5bb/REPORT.md`.

For three independent cap-one scalar variables, nonsingular symmetric `3x3` matrix `M`, arbitrary affine terms, and a nonzero diagonal pivot `alpha`, its theorem gives

```
||p_Q||inf <= K0 |alpha det M|^(-1/4),
K0=8*3^(3/4).                                                        (2.2)
```

Section 6 below applies (2.2) to the actual grouped packet, including the density-cap normalization.

The latest completed account02/B05 report was also read:

`yspennstate/math-open-problems@b6ded18bee0fe20353530653ce654308cac0631c`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T225232Z-account02-B05-QFORM-37473ccc/REPORT.md`.

Its reverse-conditioned bank-leakage theorem and random-slope half-Riesz theorem confirm that arbitrary leakage can be paid when genuinely independent scalar resources survive. They do not permit conditioning a correlated second coordinate of the same first-bank projection, so they do not by themselves close the transition isolated here.

### 2.3 Product-projection affine-fiber theorem

Canonical source:

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

If an `n x k` matrix `R` has orthonormal columns and `X` has independent cap-one coordinates, the projection `R^T X` has joint density bounded by `exp(k/2)`. In particular every two-dimensional orthonormal product projection has density cap `e`. This is used in Section 7 only after the exact packet columns have been orthogonalized inside their original-coordinate support.

## 3. Exact ratio-variance identity

Write the two orthonormal columns of `C` as

```
u=(u_i)_(i in G1),   t=(t_i)_(i in G1),
||u||_2=||t||_2=1,    <u,t>=0.                                      (3.1)
```

For a nonempty subset `G subset G1` with

```
m_G = sum_(i in G) u_i^2 >0,                                        (3.2)
```

define its weighted slope

```
r_G = [sum_(i in G) u_i t_i]/m_G                                   (3.3)
```

and residual coefficients

```
e_i=t_i-r_G u_i,   i in G,
sigma_G^2=sum_(i in G) e_i^2.                                       (3.4)
```

Then, by construction,

```
sum_(i in G) u_i e_i=0.                                             (3.5)
```

Let `C_G` be the `|G| x 2` row submatrix with rows `(u_i,t_i)`. Its Gram matrix is

```
C_G^T C_G = [[m_G, s_G],
             [s_G, q_G]],
s_G=sum_G u_i t_i,  q_G=sum_G t_i^2.                                (3.6)
```

### Lemma 3.1 — exact packet determinant

```
boxed(
 det(C_G^T C_G)=m_G sigma_G^2.
)                                                                    (3.7)
```

#### Proof

From `r_G=s_G/m_G`,

```
sigma_G^2
 =sum_G (t_i-r_G u_i)^2
 =q_G-2 r_G s_G+r_G^2 m_G
 =q_G-s_G^2/m_G.                                                      (3.8)
```

Multiplying by `m_G` gives

```
m_G sigma_G^2=m_G q_G-s_G^2=det(C_G^T C_G).                         (3.9)
```

QED.

Thus `sigma_G=0` if and only if all first-bank rows in the packet with nonzero `u_i` are exactly parallel to `(1,r_G)` (and any `u_i=0` in the packet must also have `t_i=0`). The quantity `sigma_G/sqrt(m_G)` is precisely the normalized distance from this rank-one endpoint.

When all `u_i` in `G` are nonzero, writing `rho_i=t_i/u_i`, (3.8) becomes the weighted variance identity

```
sigma_G^2
 = sum_(i in G) u_i^2 (rho_i-r_G)^2.                                (3.10)
```

No probabilistic assumption enters (3.7)--(3.10).

## 4. A constant-mass near-parallel packet always exists

The preceding identity becomes useful because the ratios cannot all escape to infinity with substantial `u`-mass.

Define a probability measure on indices with `u_i!=0` by

```
P{i}=u_i^2.                                                          (4.1)
```

It has total mass one. For `rho_i=t_i/u_i`, orthogonality and normalization give

```
E rho = sum_i u_i t_i =0,
E rho^2 = sum_(u_i!=0) t_i^2 <=1.                                   (4.2)
```

Hence Chebyshev gives

```
P(|rho|<=2)>=3/4.                                                    (4.3)
```

### Lemma 4.1 — quantitative ratio packet

For every `0<h<=1` there is a subset `G` consisting only of indices with `u_i!=0` such that

```
boxed(
 m_G >= 3h/20,
 max_(i,j in G)|rho_i-rho_j| <= h,
 sigma_G^2 <= (h^2/4) m_G.
)                                                                    (4.4)
```

In particular, taking `h=1`,

```
m_G>=3/20,\qquad sigma_G/sqrt(m_G)<=1/2.                            (4.5)
```

(A slightly sharper fixed partition gives `m_G>=3/16` when `h=1`; the uniform `3h/20` form is convenient for all `h<=1`.)

#### Proof

Cover `[-2,2]` by `N=ceil(4/h)` intervals of length at most `h`. Since `h<=1`,

```
N<=4/h+1<=5/h.                                                       (4.6)
```

By (4.3), one interval contains `u`-mass at least

```
(3/4)/N >= 3h/20.                                                    (4.7)
```

Take `G` to be the indices in that interval. Its weighted mean `r_G` lies in the same interval. A random variable supported in an interval of length `h` has variance at most `h^2/4` (Popoviciu's inequality), hence by (3.10)

```
sigma_G^2/m_G <= h^2/4.                                             (4.8)
```

QED.

This is the first useful aggregate-before-inversion statement for the r25 diffuse Schur direction: **even when every individual `u_i^2` is tiny, a packet carrying a fixed fraction of the total `u`-mass is always quantitatively close to one spectral ray.** The price is not cardinality but the residual product-projection direction measured by `sigma_G`.

## 5. Exact grouped normal form

Fix the packet `G` from Section 4 and condition all original coordinates of `G1\G` and every coordinate outside the three active banks. Define

```
S = m_G^(-1/2) sum_(i in G) u_i X_i.                                (5.1)
```

If `sigma_G>0`, also define

```
R = sigma_G^(-1) sum_(i in G) e_i X_i.                              (5.2)
```

By (3.5), the coefficient vectors in (5.1),(5.2) are orthonormal in the original coordinate space supported on `G`. Therefore `(S,R)` is a genuine two-dimensional orthonormal projection of the original product law. The product-projection affine-fiber theorem gives

```
||p_(S,R)||inf <= e.                                                 (5.3)
```

No independence between `S` and `R` is claimed.

The contribution of the packet to the first-bank spectral coordinates is exactly

```
U_G = sqrt(m_G) S,
T_G = r_G sqrt(m_G) S + sigma_G R.                                  (5.4)
```

Thus, after conditioning the complement, the entire active quadratic form is a polynomial of `(S,R,Y,Z)` whose homogeneous coefficient matrix is obtained from `K` by the column map

```
d_S=(sqrt(m_G), r_G sqrt(m_G),0,0)^T,
d_R=(0,sigma_G,0,0)^T,
d_Y=e_3,
d_Z=e_4.                                                            (5.5)
```

Because the Schur remainder of `K` over the scalar pair `B` is `lambda e1 e1^T`, the Schur remainder of this packet over the same pair is exactly

```
lambda [[m_G,0],[0,0]]                                               (5.6)
```

in the `(S,R)` coordinates. In particular, the second packet direction is a true **null direction of the Schur curvature**, not a small error inserted by approximation.

Equation (5.6) is the exact normal form of the remaining transition.

## 6. Exact parallel-packet endpoint is closed

Assume now

```
sigma_G=0.                                                           (6.1)
```

Then (5.4) contains only the scalar `S`; the packet is spectrally rank one. Since `S` is a normalized linear projection of the independent coordinates in `G`, the one-dimensional product-projection theorem gives

```
||p_S||inf <= sqrt(2).                                               (6.2)
```

The scalar variables `S,Y,Z` depend on three disjoint original-coordinate blocks, so they are genuinely independent, each with density cap at most `sqrt(2)`.

Let `M_G` be their `3x3` homogeneous quadratic coefficient matrix. Schur complementation of `B` gives

```
det M_G
 = det B * lambda * m_G.                                             (6.3)
```

Using (1.1),

```
boxed(
 |det M_G| = mu m_G.
)                                                                    (6.4)
```

Apply r25's theorem (2.1). Since the three density caps are all at most `sqrt(2)`,

```
(L1 L2 L3)^(2/3)
 <= (2 sqrt(2))^(2/3)=2.                                             (6.5)
```

Therefore

```
boxed(
 ||p_Q||inf
 <= 2 C3 (mu m_G)^(-1/3)
 <51.6 (mu m_G)^(-1/3).
)                                                                    (6.6)
```

This bound is uniform in the number of coordinates in `G`, in every individual `u_i`, in the scalar-pair condition number, and in the scalar-pair scale. Arbitrary affine terms from the conditioned complement are allowed.

### Assigned-partner theorem applied to this actual packet

To record the designated account02/B05 dependency at an actual inequality rather than only through r25, normalize the three cap-`sqrt(2)` variables by multiplying them by `sqrt(2)`. The new variables have cap at most one, while the quadratic core becomes `M_G/2`; hence

```
|det(M_G/2)|=mu m_G/8.                                               (6.7)
```

Suppose one diagonal pivot `alpha` of `M_G` obeys

```
|alpha| >= (mu m_G)^(1/3)/4.                                        (6.8)
```

Its normalized pivot is `alpha/2`. Applying the partner scalar-Schur theorem (2.2) gives

```
||p_Q||inf
 <= K0 |(alpha/2)(mu m_G/8)|^(-1/4)
 =2 K0 |alpha mu m_G|^(-1/4)
 <=2 sqrt(2) K0 (mu m_G)^(-1/3)
 =2 C3 (mu m_G)^(-1/3),                                             (6.9)
```

which is precisely the first branch of (6.6). The complementary all-small-diagonal branch is the pair-log branch already audited in r25. Thus the assigned partner result is spent directly on the grouped packet.

For the fixed packet from `h=1`, exact parallelity would give `m_G>=3/20` and hence

```
||p_Q||inf <51.6 (20/(3 mu))^(1/3).                                 (6.10)
```

In the structural packet where `mu` already has a universal positive lower bound, this is a universal number.

## 7. Why the near-parallel packet is not yet the endpoint theorem

If `sigma_G>0`, equations (5.1)--(5.5) give a two-dimensional orthonormal product projection `(S,R)`, not two independent scalars. The quantitative packet lemma can make

```
epsilon_G := sigma_G/sqrt(m_G) <= h/2                               (7.1)
```

as small as desired, at the cost `m_G>=3h/20`, but **small coefficient norm does not license conditioning on `R`**.

The live correction `QFORM-UV-CONDITIONAL-CAP-FALSE` already gives the elementary obstruction: conjugate linear projections of independent uniforms can have conditional density caps that diverge near the edge of the conditioning variable. Therefore one cannot pass from the joint cap (5.3) to an independent-scalar version of (6.6) by conditioning `R` and claiming the cap of `S` is preserved.

Nor can one discard the product provenance and retain only `||p_(S,R)||inf<=e`: the live correction `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1` shows that a bounded arbitrary joint density is insufficient for an indefinite quadratic pushforward. The missing theorem must use the fact that `(S,R)` is an **orthonormal projection of the original coordinate product measure**.

The packet construction quantifies this debt exactly. It reduces the diffuse-Schur branch to the family

```
(S,R) = orthonormal 2D product projection,
Y,Z    = independent scalar product projections on disjoint banks,
Schur_B(K_packet)=lambda [[m,0],[0,0]],
mu=|det B||lambda|,
0<sigma/sqrt(m)<=h/2,
m>=3h/20.                                                             (7.2)
```

The exact endpoint `sigma=0` is bounded by (6.6). What is missing is a bound that stays finite as `sigma ->0` **without** conditioning `R` and without paying a reciprocal physical coordinate.

## 8. Precise next implication

The first unpaid implication is now

`QFORM-NEAR-PARALLEL-PRODUCT-PROJECTION-TRANSITION-v1`:

> In the normal form (7.2), prove a coarea/small-ball bound
> `||p_Q||inf <= C (mu m)^(-1/3) Phi(sigma/sqrt(m))`
> with `Phi(epsilon)` bounded on some interval `0<=epsilon<=epsilon_0`, using the original-coordinate product provenance of `(S,R)`. Equivalently, prove direct continuity of the exact parallel-packet density estimate through the singular rank-one-to-rank-two packet transition.

A proof with `Phi` bounded for `epsilon<=1/2` would combine with the fixed `h=1` packet `m>=3/20` and close the r25 diffuse Schur-direction grouping debt for the punctured double-zero packet. A theorem that instead first conditions `R`, takes an unrestricted fiber supremum, or replaces `(S,R)` by an arbitrary bounded joint density is invalidated by existing corrections.

This is a strictly narrower obstruction than r25's phrase "aggregate many coordinates": the aggregation and its quantitative mass are now explicit, and the only unpaid factor is the **near-parallel product-projection singular transition**.

## 9. Scope and status

This report proves the ratio-variance packet identity, the constant-mass near-parallel packet lemma, the exact packet normal form, and the full exact-parallel endpoint estimate. It does **not** prove the generic `sigma_G>0` transition, the unrestricted exact-rank-three theorem, or the arbitrary-higher-rank target. It does not prove continuity of the target density.

No Gaussianity, log-concavity, moment bound, support bound, connected-support assumption, or post-rotation independence is used. No Monte Carlo statement is used. Full QFORM remains `OPEN_NOT_PROVED`.
