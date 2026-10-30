SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B05, 2026-09-23T02:31:37Z.
attacking: the near-rank-one scalar-pair transition in the one-rank-two/two-rank-one aggregate-bank geometry; replace the reciprocal smallest-singular-value loss by an exact post-pivot pseudodeterminant identity and isolate the true double-zero endpoint.

# fleet01/B05 QFORM r24 — kappa-free invertible scalar-pair coarea via post-pivot pseudodeterminant

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; repository transport is not native learned-memory ingestion).  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / PRECISE_REMAINING_FACTOR_IDENTIFIED`.  
**Full QFORM:** `OPEN_NOT_PROVED`.  
**Continuity:** `NOT_PROVED` by the theorem below; only essential boundedness is asserted.

## 1. Compact conditional end-to-end argument

The exact-rank-three aggregate geometry already obtained by fleet03/B05 consists of one spectral-rank-two original-coordinate bank `G1` and two spectral-rank-one banks `G2,G3`. In normalized aggregate coordinates `(L1,L2,Y,Z)`,

```
K = [[C0, p, q],
     [p^T, a, c],
     [q^T, c, d]],
```

where `L=C^T X_G1`, `C^T C=I_2`, while `Y,Z` are independent normalized scalar projections of the two disjoint rank-one banks and each has density cap `sqrt(2)`. The compressed matrix `K` has rank three. Let

```
B=[[a,c],[c,d]]
```

be the scalar-pair block, and let

```
mu=sum_(i in G1,j in G2,k in G3) |det A_{ijk}| >0
```

be the aggregate principal-triple determinant mass.

The previous endpoint results were:

* if `B` is invertible indefinite, fleet03/B05 r19 gives a bound proportional to `(kappa*mu)^(-1/4)`, where `kappa=sigma_min(B)`;
* if `rank B=1`, fleet01/B05 r23 gives the uniform endpoint bound `16 mu^(-1/3)`;
* if `B=0`, then `mu=0`, so the positive-packet branch never has scalar-pair rank zero.

The apparent gap was therefore the invertible regime `kappa ->0`, because the r19 estimate diverges although the exact rank-one endpoint is bounded.

This run proves that the divergence in `kappa` is not intrinsic. If `L_B=||B||_op` is the *large* singular value of `B`, then for **every invertible** `B`, all signs included,

```
boxed( ||p_Q||_infinity <= 256 (mu L_B)^(-1/4). )                 (1.1)
```

Thus the entire condition-number transition `kappa/L_B ->0` is paid uniformly. Combined with the exact rank-one theorem, the only scalar-pair endpoint not yet uniformly paid by these local estimates is the punctured **double-zero** regime

```
B invertible,   ||B||_op ->0,   mu bounded below.                  (1.2)
```

In that regime the aggregate Schur curvature necessarily explodes:

```
|lambda_S| = mu/|det B| >= mu / ||B||_op^2.                       (1.3)
```

So the next mechanism must spend this large first-bank curvature jointly with the tiny scalar pair rather than paying a reciprocal scalar-pair scale first.

## 2. Sources actually consumed

### 2.1 fleet03/B05 r19 aggregate Schur geometry

Canonical source:

`yspennstate/math-open-problems@70f181cf738aa51ee6fb7043a329ac9e8b22c4ec`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260922T223741Z-fleet03-B05-QFORM-r19/REPORT.md`.

Its Cauchy--Binet/Schur argument identifies the rank-one Schur remainder after completing an invertible scalar pair and gives

```
|det B| |lambda_S| = mu.                                           (2.1)
```

Although r19 then assumes the pair is indefinite to invoke the pair-log theorem, identity (2.1) itself uses only invertibility of `B`, rank `K=3`, and the exact-rank-three common-sign principal-minor identity. I reproduce the relevant algebra below, so no sign extension is being silently assumed.

### 2.2 orientation-free rank-two affine half-Riesz theorem

Canonical source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For independent cap-one original coordinates, an orthonormal two-dimensional projection `U`, any invertible symmetric `Lambda`, and **any** original-coordinate affine term `b`,

```
sup_t E |(U^T X)^T Lambda(U^T X)+b^T X-t|^(-1/2)
 <= 128 |det Lambda|^(-1/4).                                      (2.2)
```

No leverage, sign, or affine-range condition is needed.

### 2.3 assigned partner fleet02/B05 — scalar-Schur coarea

Canonical source:

`yspennstate/math-open-problems@e06922bfa31bbd225cdce6ee6aea563254e62563`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T122133Z-b05-qform-5c41e5bb/REPORT.md`.

The actual inequality used in Section 5 is its square-kernel step: after completing one independent cap-one scalar pivot of coefficient `alpha!=0`,

```
p_Q(t) <= |alpha|^(-1/2) E |t-R|^(-1/2).                           (2.3)
```

This is applied below to the normalized scalar-bank pivot, not merely cited.

### 2.4 newest assigned-partner result

The latest completed fleet02/B05 report read this run is

`yspennstate/math-open-problems@b6ded18bee0fe20353530653ce654308cac0631c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T225232Z-fleet02-B05-QFORM-37473ccc/REPORT.md`.

Its `QFORM-RANDOM-SLOPE-HALF-RIESZ-v1` states

```
R=K(E)+2X T(E),   X independent of E,
||p_X||_infinity<=L_X, ||p_T||_infinity<=L_T

=> sup_q E|q-R|^(-1/2) <=4 sqrt(2 L_X L_T).                        (2.4)
```

Section 7 applies (2.4) to the exact singular limit as an independent check and to show precisely what the new invertible theorem improves.

## 3. Geometry and normalization

Write the aggregate matrix as

```
K = [[C0, p, q],
     [p^T, a, c],
     [q^T, c, d]],                                                   (3.1)
```

with `C0` symmetric `2 x 2`, `p,q in R^2`, and scalar pair

```
B=[[a,c],[c,d]].                                                      (3.2)
```

The underlying aggregate variables have genuine product provenance:

* `L=C^T X_G1`, `C^T C=I_2`;
* `Y` is a normalized scalar projection of `X_G2` and `||p_Y||_infinity<=sqrt(2)`;
* `Z` is a normalized scalar projection of `X_G3` and `||p_Z||_infinity<=sqrt(2)`;
* the three banks are disjoint, hence the blocks `L,Y,Z` are mutually independent.

The combined map from original coordinates in `G1 union G3` to `(L1,L2,Z)` is an isometry on its three aggregate columns: the two columns of `C` are orthonormal, the coefficient vector defining `Z` has norm one, and the supports are disjoint. This observation is what permits (2.2) to be applied to a rank-two residual in `(L,Z)` without asserting independence of the two components of `L`.

All original coordinates outside the active set may be conditioned. They create only affine terms and constants in `(L,Y,Z)`. The rank-two theorem (2.2) allows arbitrary affine terms, and every bound below is uniform in this conditioning.

## 4. Exact post-pivot pseudodeterminant identity

Choose one scalar-bank coordinate with nonzero quadratic pivot; initially assume `a!=0`. Complete the `Y` square. Define

```
C1 = C0 - p p^T/a,
theta = q - (c/a)p,
delta = d-c^2/a.                                                      (4.1)
```

The quadratic Schur residual on `(L,Z)` is

```
R_a = [[C1, theta],
       [theta^T, delta]].                                             (4.2)
```

Since `rank K=3` and the scalar pivot has rank one,

```
rank R_a=2.                                                           (4.3)
```

Let `pdet(R_a)` denote the product of the two nonzero eigenvalues of this symmetric rank-two matrix.

### Lemma 4.1 — invertible scalar pair

Assume `det B!=0`; equivalently `delta!=0`. Let

```
S=C1-theta theta^T/delta.                                             (4.4)
```

Then `rank S=1`. Write

```
S=lambda v v^T,  ||v||=1.                                            (4.5)
```

Let `w` be the unit vector orthogonal to `v` in `R^2` and decompose

```
theta = alpha v + beta w.                                             (4.6)
```

Then

```
boxed(
 |pdet(R_a)|
 = (mu/|a|) [1+beta^2/delta^2]
 >= mu/|a|.
)                                                                     (4.7)
```

#### Proof

First, `rank S=1`: Schur complementation of the nonzero scalar `delta` in the rank-two matrix `R_a` gives

```
rank R_a =1+rank S,
```

so (4.3) implies rank one.

Next reproduce the aggregate determinant identity without using the sign of `B`. Completing the entire invertible scalar pair in (3.1) leaves the `2 x 2` Schur matrix

```
S_full=C0-[p,q] B^(-1) [p,q]^T.                                      (4.8)
```

Sequential Schur complementation gives exactly `S_full=S` from (4.4). Because `K` has rank three and `B` rank two, `S` has rank one as above. For each compressed first-bank coordinate `L_ell`, the principal `3 x 3` minor on `(L_ell,Y,Z)` equals

```
det B * S_(ell,ell).                                                  (4.9)
```

For an exact-rank-three spectral representation every physical principal triple has the common-sign form

```
det M * det(r_i,r_j,r_k)^2.
```

Cauchy--Binet and `C^T C=I_2` therefore identify the sum of the absolute values of the two compressed minors (4.9) with the bank packet `mu`. Since a rank-one symmetric matrix `S=lambda vv^T` has diagonal entries all of the sign of `lambda`,

```
mu=|det B| |tr S|=|det B| |lambda|.                                  (4.10)
```

Now (4.2) and (4.4) give the exact rank-one-sum factorization

```
R_a
 = lambda [v;0][v;0]^T
   +(1/delta)[theta;delta][theta;delta]^T.                            (4.11)
```

For a sum `rho uu^T+sigma zz^T` of two rank-one symmetric matrices, the product of the two nonzero eigenvalues equals

```
rho sigma (||u||^2 ||z||^2-(u dot z)^2).                              (4.12)
```

Apply (4.12) to (4.11). Since `||v||=1` and the component of `theta` orthogonal to `v` is `beta w`,

```
pdet(R_a)= (lambda/delta)(beta^2+delta^2).                            (4.13)
```

Taking absolute values and using `det B=a delta` plus (4.10),

```
|lambda delta|=mu/|a|,
```

which yields (4.7). QED.

### Lemma 4.2 — singular rank-one scalar pair

Assume `det B=0`, `rank B=1`, and choose labels with `a!=0`. Then the preceding r23 identity gives

```
mu=|a| ||theta||^2.                                                    (4.14)
```

Moreover

```
boxed( |pdet(R_a)| >= mu/|a|. )                                      (4.15)
```

#### Proof

Now `delta=0`. Put `r=||theta||>0`, rotate only the two-dimensional notation for `L` so `theta=r e1`, and write

```
C1=[[alpha,beta],[beta,gamma]].
```

Then

```
R_a=[[alpha,beta,r],
     [beta,gamma,0],
     [r,0,0]].                                                        (4.16)
```

Its determinant is `-r^2 gamma`. Rank `R_a=2` forces `gamma=0`. For a rank-two `3 x 3` symmetric matrix, the product of its two nonzero eigenvalues is the second elementary symmetric polynomial, i.e. the sum of its three principal `2 x 2` minors. In (4.16) with `gamma=0`,

```
pdet(R_a)= -beta^2-r^2.                                               (4.17)
```

Therefore `|pdet(R_a)|=beta^2+r^2>=r^2=mu/|a|` by (4.14). QED.

Lemma 4.1 is the new quantitative information for the invertible transition. It shows that after a nonzero scalar pivot the residual rank-two determinant never becomes smaller than `mu/|a|`; transverse shear `beta/delta` can only increase it.

## 5. Assigned-partner application and the new pivot bound

Normalize the scalar-bank pivot by

```
Y'=sqrt(2) Y.                                                         (5.1)
```

Then `Y'` has density cap one. Its quadratic coefficient is `a/2`, while its cross coefficients are divided by `sqrt(2)`. Completing `Y'` leaves **exactly the same** residual matrix `R_a`: for example

```
(p/sqrt(2))(p/sqrt(2))^T/(a/2)=pp^T/a,
```

and similarly for `theta` and `delta`.

Apply the assigned-partner scalar-Schur inequality (2.3):

```
p_Q(t)
 <= |a/2|^(-1/2)
    E |t-[quadratic residual + affine]|^(-1/2)
 = sqrt(2)|a|^(-1/2)
    E |t-[quadratic residual + affine]|^(-1/2).                       (5.2)
```

The residual acts on the aggregate variables `(L1,L2,Z)`. As observed in Section 3, these three aggregate columns form an orthonormal projection of the underlying original-coordinate product source. Since `R_a` has rank two, diagonalize `R_a` **inside this three-dimensional aggregate space** and apply (2.2) to the resulting two-dimensional orthonormal active subspace. This does not declare the rotated aggregate coordinates independent; theorem (2.2) is expressly orientation-free. It gives

```
sup_t E |t-[quadratic residual + affine]|^(-1/2)
 <=128 |pdet(R_a)|^(-1/4).                                           (5.3)
```

Combine (5.2), (5.3), and Lemma 4.1 (or Lemma 4.2):

```
boxed(
 ||p_Q||_infinity
 <=128 sqrt(2) (mu |a|)^(-1/4).
)                                                                     (5.4)
```

This estimate is uniform in arbitrary affine terms generated by outside conditioning. It imposes no sign condition on the scalar pair and has no reciprocal `sigma_min(B)` factor.

The exact transverse version in the invertible case is slightly stronger:

```
||p_Q||_infinity
 <=128 sqrt(2) (mu |a|)^(-1/4)
      [1+beta^2/delta^2]^(-1/4).                                     (5.5)
```

The new currency is therefore the **large scalar pivot times the aggregate determinant packet**, supplemented by any transverse post-pivot shear; the small singular value of the original scalar pair is not itself a required denominator.

## 6. Kappa-free theorem for every invertible scalar pair

Let

```
L_B=||B||_op,
kappa=sigma_min(B)>0.                                                  (6.1)
```

### Theorem 6.1 — `QFORM-RANK2BANK-INVERTIBLE-SCALARPAIR-KAPPA-FREE-v1`

Under the aggregate exact-rank-three geometry of Section 3, if `B` is invertible and `mu>0`, then for arbitrary outside affine terms and for either signature,

```
boxed(
 ||p_Q||_infinity <=256 (mu L_B)^(-1/4).
)                                                                     (6.2)
```

#### Proof: definite `B`

If `B` is positive or negative definite, its diagonal entries have the same sign and

```
|a+d|=|lambda_1(B)+lambda_2(B)|=L_B+kappa.
```

Hence one of the two scalar labels satisfies

```
max(|a|,|d|)>=(L_B+kappa)/2 >=L_B/2.                                 (6.3)
```

Use that label as pivot in (5.4):

```
||p_Q||_infinity
 <=128 sqrt(2) (mu L_B/2)^(-1/4)
 =128*2^(3/4) (mu L_B)^(-1/4)
 <216 (mu L_B)^(-1/4).                                                (6.4)
```

#### Proof: indefinite `B`, small condition ratio

Suppose `B` is indefinite and `kappa<=L_B/2`. Its two eigenvalues have opposite signs, so

```
|tr B|=L_B-kappa >=L_B/2.                                             (6.5)
```

Therefore

```
max(|a|,|d|)>=|tr B|/2>=L_B/4.                                       (6.6)
```

Use the larger diagonal pivot in (5.4):

```
||p_Q||_infinity
 <=128 sqrt(2)(mu L_B/4)^(-1/4)
 =256 (mu L_B)^(-1/4).                                                (6.7)
```

#### Proof: indefinite `B`, well-conditioned

If instead `kappa>L_B/2`, use the completed fleet03/B05 r19 pair-log theorem

```
||p_Q||_infinity
 <=8*2^(3/4)*sqrt(5) (kappa mu)^(-1/4).                               (6.8)
```

Since `kappa>L_B/2`,

```
||p_Q||_infinity
 <8*2*sqrt(5) (mu L_B)^(-1/4)
 =16sqrt(5)(mu L_B)^(-1/4)
 <36 (mu L_B)^(-1/4).                                                  (6.9)
```

The largest of (6.4), (6.7), and (6.9) is 256, proving (6.2). QED.

### Consequence

The previous r19 denominator `kappa^(-1/4)` was a proof-mechanism loss in the fixed-scale near-rank-one transition. The actual uniform branch is controlled by the *dominant* scalar-pair scale `L_B`, not by its smallest singular value.

In particular, for every fixed `ell0>0`,

```
L_B>=ell0  =>
||p_Q||_infinity <=256 (mu ell0)^(-1/4)                               (6.10)
```

uniformly as `kappa` tends all the way to zero. At `kappa=0`, the previous rank-one endpoint theorem gives the different but finite estimate

```
||p_Q||_infinity <=16 mu^(-1/3).                                     (6.11)
```

Thus there is no genuine singularity caused solely by a degenerating scalar-pair condition number.

## 7. Newest assigned-partner theorem applied at the singular boundary

To keep the partner interface explicit, recover the partner's random-slope inequality on the exact rank-one boundary.

At `rank B=1`, r23 gives after the nonzero pivot

```
Q=a[Y+eta Z+delta(L)]^2 + H(L)Z+K0(L),
H(L)=2 theta dot L+h0,
mu=|a|r^2,
r=||theta||.                                                          (7.1)
```

The normalized linear form `(theta/r) dot L` is a unit original-product projection, so Rogozin--Ball gives density cap `sqrt(2)`. Hence `H/2` has density cap at most

```
L_T<=sqrt(2)/(2r)=1/(sqrt(2)r).                                      (7.2)
```

The scalar bank variable `Z` has cap `L_X=sqrt(2)`. Applying the newest partner theorem (2.4) to

```
R=K0(L)+2 Z [H(L)/2]
```

gives the actual inequality

```
sup_q E|q-R|^(-1/2)
 <=4 sqrt(2*sqrt(2)/(sqrt(2)r))
 =4sqrt(2) r^(-1/2).                                                  (7.3)
```

Normalize the independent square variable `Y'=sqrt(2)Y`, whose square coefficient is `a/2`. The partner square lift then gives

```
||p_Q||_infinity
 <= |a/2|^(-1/2) * 4sqrt(2)r^(-1/2)
 =8 |a|^(-1/2)r^(-1/2)
 =8 |a|^(-1/4) mu^(-1/4).                                            (7.4)
```

(The earlier r23 report used a slightly looser normalization constant; (7.4) is the same scaling and the exact constants here follow directly from the stated caps.) The two-regime direct coarea theorem r23 improves this further to `16 mu^(-1/3)` by paying the far-slope `1/|H|` branch before averaging.

This partner application is important conceptually: it confirms that the exact singular endpoint is already product-preservingly smooth. The new theorem in this report shows that the neighboring invertible states do not require `kappa^(-1/4)` either; only collapse of the *entire* scalar pair is still unpaid.

## 8. Exact remaining factor: punctured double-zero scalar pair

Combine all scalar-pair ranks for a positive packet `mu>0`:

1. `rank B=2`: Theorem 6.1 gives `256 (mu ||B||_op)^(-1/4)`.
2. `rank B=1`: r23 gives `16 mu^(-1/3)`.
3. `rank B=0`: impossible, because every compressed `(one G1 coordinate,G2,G3)` principal triple vanishes, so `mu=0`.

Therefore the first unpaid local implication is no longer “near rank one” and no longer “small `sigma_min(B)`.” It is

**`QFORM-RANK2BANK-PUNCTURED-DOUBLEZERO-SCALARPAIR-v1`**:

> In the same positive aggregate packet, control the invertible states with `L_B=||B||_op ->0` by spending the simultaneously exploding first-bank Schur curvature and the scalar-pair output scale jointly, before any uniform pair-density or reciprocal-gradient bound is taken.

The forced curvature ledger is exact:

```
mu=|det B| |lambda_S|,
|det B|<=L_B^2,

therefore

boxed( |lambda_S| >= mu/L_B^2. )                                     (8.1)
```

So the bad-looking small scalar pair is accompanied by a very good-looking rank-one curvature of size at least `mu/L_B^2` inside the genuine rank-two product bank. A proof that still loses a negative power of `L_B` has failed to couple those two scales sharply enough.

A useful normal form to attack next is obtained after completing the scalar pair (when invertible):

```
Q = [shifted scalar-pair quadratic with matrix B]
    + lambda_S (v dot L)^2
    + affine(first-bank variables)+constant,                          (8.2)
```

where `v dot L` is a unit original-product projection, but the translations of the scalar pair depend on the same first-bank variables. Thus the remaining obstacle is not lack of one-dimensional anti-concentration; it is a **translation-uniform joint trace** that retains the dependence between the huge Schur square and the scalar-pair shifts. Replacing that dependence by a supremum reintroduces exactly the false fiber mechanisms recorded in the live correction stream.

## 9. Relation to the global QFORM target

This report proves a scoped analytic theorem in the exact-rank-three one-rank-two/two-rank-one bank packet. It does not prove that every matrix with three large eigenvalues admits this packet, does not resolve configurations with multiple spectral-rank-two resource banks, and does not handle arbitrary additional spectral directions by itself.

The global conjecture therefore remains open. Even within the present packet, (8.1)--(8.2) leave the punctured double-zero scalar-pair transition unpaid. The result should be used as a routing simplification: future workers do **not** need to solve a generic `kappa ->0` problem here. They only need to address the much sharper `||B||_op ->0` state, in which a compensating rank-one Schur curvature is forced to diverge quadratically.

Continuity is not claimed. The argument constructs an essentially bounded density through the square-kernel and rank-two half-Riesz estimates. Additional work is required to justify a continuous representative under only measurable cap-one input densities.

## 10. Algebra audit

The only new matrix identity is (4.7). In the basis `(v,w,Z)`, the two rank-one summands in (4.11) are

```
lambda (1,0,0)(1,0,0)^T
```

and

```
(1/delta)(alpha,beta,delta)(alpha,beta,delta)^T.
```

The nonzero eigenvalue product is their `2 x 2` Gram determinant,

```
(lambda/delta)[(alpha^2+beta^2+delta^2)-alpha^2]
=(lambda/delta)(beta^2+delta^2),
```

exactly (4.13). The singular formula (4.17) follows by summing the principal `2 x 2` minors. These are exact symbolic identities; no numerical experiment is used as proof.

No current correction read before publication contradicts the argument: it uses no post-rotation independence, no arbitrary-joint coarea bound, no conditional projection-density cap, no pointwise van-der-Corput estimate, and no unrestricted fiber supremum.
