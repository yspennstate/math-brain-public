SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B05, 2026-09-23T02:54:31Z.
attacking: the punctured double-zero scalar-pair branch; replace the vanishing pair scale by a determinant-normalized three-independent-scalar coarea theorem and isolate only diffuse Schur-direction aggregation.

# fleet01/B05 QFORM r25 — determinant-normalized three-scalar coarea and the heavy-Schur closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval was used; repository transport is not native learned-memory ingestion).  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / PRECISE_REMAINING_FACTOR_IDENTIFIED`.  
**Full QFORM:** `OPEN_NOT_PROVED`.  
**Continuity:** `NOT_PROVED`; only absolute continuity and an essential-supremum estimate are asserted in the proved scopes.

## 1. Compact conditional end-to-end argument

The preceding B05 run reduced the exact-rank-three aggregate packet to one spectral-rank-two original-coordinate bank `G1` and two spectral-rank-one banks `G2,G3`. In normalized aggregate coordinates `(L1,L2,Y,Z)`,

```
K = [[C0, p, q],
     [p^T, a, c],
     [q^T, c, d]],
```

where `L=C^T X_G1`, `C^T C=I_2`, while `Y,Z` are independent normalized scalar projections of the two disjoint rank-one banks. The scalar pair is

```
B=[[a,c],[c,d]].
```

For the positive determinant packet

```
mu=sum_(i in G1,j in G2,k in G3) |det A_{ijk}|,
```

completing an invertible scalar pair leaves a rank-one Schur matrix

```
S=lambda v v^T,
```

with the exact identity

```
|det B| |lambda| = mu.                                             (1.1)
```

Run r24 removed the blow-up in the *condition number* of `B`, proving a bound depending only on `mu ||B||_op`, but it still deteriorates in the punctured double-zero regime `||B||_op ->0`, `mu` fixed. In that regime `|lambda|=mu/|det B|` explodes.

The present run proves a scale-invariant local theorem for **every nonsingular quadratic form of three genuinely independent scalar variables**:

```
||p_Q||_infinity
 <= C3 (L1 L2 L3)^(2/3) |det M|^(-1/3),
C3=8 sqrt(2) 3^(3/4)<25.8.                                        (1.2)
```

Here `Li` are the three scalar density caps and `M` is the 3x3 quadratic coefficient matrix. This removes all dependence on `sigma_min(M)`, on a selected diagonal pivot, and on the signature.

Applying (1.2) to one physical first-bank coordinate and the two normalized scalar banks gives a `B`-free bound whenever the exploding Schur direction has a heavy physical coordinate. Thus the punctured double-zero obstruction is sharpened to one exact factor only: **diffuse Schur-direction aggregation inside the rank-two bank**.

## 2. Sources actually consumed

### 2.1 Assigned partner fleet02/B05 — scalar-Schur coarea

Canonical source:

`yspennstate/math-open-problems@e06922bfa31bbd225cdce6ee6aea563254e62563`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T122133Z-b05-qform-5c41e5bb/REPORT.md`.

Its Theorem 6.1 proves the following for three independent cap-one scalar inputs and arbitrary affine terms. If `M` is nonsingular and some diagonal pivot `alpha!=0`, then

```
||p_Q||_infinity
 <= K0 |alpha det M|^(-1/4),
K0=8*3^(3/4).                                                       (2.1)
```

This is the assigned-partner result actually applied in Section 4 below.

The latest completed assigned-partner report was also read in full:

`yspennstate/math-open-problems@b6ded18bee0fe20353530653ce654308cac0631c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T225232Z-fleet02-B05-QFORM-37473ccc/REPORT.md`.

Its `QFORM-RANDOM-SLOPE-HALF-RIESZ-v1` states that, if `X` is independent of an environment `E`, `||p_X||_infinity<=L_X`, `T(E)` has density cap `L_T`, and `R=K(E)+2XT(E)`, then

```
sup_q E|q-R|^(-1/2) <=4 sqrt(2 L_X L_T).                           (2.2)
```

An independent translated square with coefficient `a` then gives an output-density bound `4 sqrt(2L_XL_T)|a|^(-1/2)`. Section 6 records an actual determinant-scaled application of (2.2).

### 2.2 Two-coordinate logarithmic smoothing

Canonical source:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite physical pair `P`, write

```
D=|det P|,  kappa=sigma_min(P).
```

Its general logarithmic-envelope theorem, combined with the source's scalar rank-one small-ball bound for a remainder having coefficient `lambda`, gives

```
||p_Q||_infinity
 <=8 sqrt(5) (D kappa |lambda|)^(-1/4).                            (2.3)
```

It permits arbitrary affine terms and both pair diagonals may vanish. No post-rotation independence is used.

### 2.3 Previous B05 aggregate identity

Canonical source:

`yspennstate/math-open-problems@a1e27348ad252fe1a4014c41d024368dff651cda`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B05/20260923T023137Z-fleet01-B05-QFORM-r24/REPORT.md`.

It proves (1.1), the rank-one Schur factorization, and the identity used in Section 7 that the physical triple `(X_i,Y,Z)` has determinant magnitude `mu u_i^2`, where `u=Cv` is the physical Schur direction.

## 3. Scaling reduction for three independent scalar inputs

Let `X_1,X_2,X_3` be independent real variables with positive probability density caps `L_1,L_2,L_3` and let

```
Q=X^T M X + ell^T X + c,
```

where `M` is a real symmetric invertible `3x3` matrix.

Put `D_L=diag(L_1,L_2,L_3)` and `U=D_L X`. Then the `U_i` are still independent and each has density cap one. In the new variables,

```
M' = D_L^(-1) M D_L^(-1),
|det M'| = |det M|/(L_1 L_2 L_3)^2.                                (3.1)
```

Affine terms remain arbitrary. Therefore it suffices to prove the cap-one theorem

```
||p_Q||_infinity <= C3 |det M|^(-1/3).                             (3.2)
```

The general formula (1.2) then follows from (3.1).

## 4. Main theorem: determinant-normalized three-scalar coarea

### Theorem 4.1 — `QFORM-THREE-SCALAR-DETERMINANT-COAREA-v1`

Let `X_1,X_2,X_3` be independent real random variables with probability densities bounded by one. Let `M` be any real symmetric invertible `3x3` matrix, with arbitrary affine perturbation. Then the quadratic polynomial has an essentially bounded density satisfying

```
boxed(
 ||p_(X^T M X+ell^T X+c)||_infinity
 <= C3 |det M|^(-1/3),
 C3=8 sqrt(2) 3^(3/4)<25.8.
)                                                                    (4.1)
```

All signatures and all zero/nonzero diagonal patterns are included.

### Proof

Write

```
M=[[a,p,q],
   [p,b,r],
   [q,r,c]],
```

put

```
d=|det M|>0,
delta=d^(1/3).                                                       (4.2)
```

We split according to the largest diagonal entry.

#### Case I: a diagonal has scale at least delta/4

Suppose, after relabeling,

```
|a|>=delta/4.                                                       (4.3)
```

Apply the assigned-partner scalar-Schur theorem (2.1) to this actual matrix and this actual scalar pivot. It gives

```
||p_Q||_infinity
 <=K0 |a d|^(-1/4)
 <=K0 4^(1/4) d^(-1/4) delta^(-1/4)
 =K0 sqrt(2) d^(-1/3).                                             (4.4)
```

Since `K0=8*3^(3/4)`, this is exactly the constant in (4.1).

No rotated variables have been declared independent: the partner theorem completes one of the three original independent scalars and controls the binary Schur remainder directly in the other two original independent scalars.

#### Case II: every diagonal is smaller than delta/4

Assume

```
|a|,|b|,|c|<delta/4.                                                (4.5)
```

I first claim that at least one off-diagonal entry has magnitude at least `delta/2`. If instead

```
|p|,|q|,|r|<delta/2,
```

then the exact determinant expansion

```
det M=abc+2pqr-a r^2-b q^2-c p^2                                (4.6)
```

would imply

```
|det M|
 <delta^3(1/64+1/4+3/16)
 =(29/64) delta^3
 <delta^3=d,                                                        (4.7)
```

a contradiction.

Thus, after relabeling,

```
|p|>=delta/2.                                                       (4.8)
```

Take the physical pair

```
P=[[a,p],[p,b]].                                                    (4.9)
```

It is automatically indefinite because

```
det P=ab-p^2<delta^2/16-delta^2/4<0.                              (4.10)
```

Moreover, comparing `P` with `[[0,p],[p,0]]` and using singular-value perturbation,

```
kappa=sigma_min(P)
 >=|p|-max(|a|,|b|)
 >=delta/4.                                                         (4.11)
```

Let `lambda` be the scalar Schur coefficient after completing `P`. Since `M` is invertible,

```
D |lambda|=d,
D=|det P|.                                                         (4.12)
```

Apply the source-pinned two-coordinate logarithmic smoothing theorem (2.3):

```
||p_Q||_infinity
 <=8 sqrt(5) (D kappa |lambda|)^(-1/4)
 =8 sqrt(5) (kappa d)^(-1/4)
 <=8 sqrt(10) d^(-1/3).                                            (4.13)
```

Finally

```
8 sqrt(10) < 8 sqrt(2) 3^(3/4),                                   (4.14)
```

so Case II also satisfies (4.1). This proves the theorem. QED.

### Remarks on scope

1. The exponent `1/3` is forced by scalar dilation: replacing `M` by `sM` multiplies an output density by `s^(-1)`, while `|det(sM)|^(-1/3)=s^(-1)|det M|^(-1/3)`.
2. This is not the refuted arbitrary-joint three-dimensional coarea claim. Independence of the **three scalar source variables** is spent in (2.1) and (2.3).
3. No support, moment, centering, Gaussian, log-concavity, or connected-support hypothesis is used.
4. The theorem gives absolute continuity and an essential bound. It does not prove continuity of the density.

## 5. General density caps

Undoing the scaling in Section 3 gives the form needed for aggregate-bank applications.

### Corollary 5.1

If the three independent scalar inputs have density caps `L_1,L_2,L_3`, then

```
boxed(
 ||p_Q||_infinity
 <=C3 (L_1 L_2 L_3)^(2/3) |det M|^(-1/3).
)                                                                    (5.1)
```

This remains valid with arbitrary affine perturbations.

## 6. Latest-partner theorem applied to an actual determinant-scaled subcase

To apply the newest completed fleet02/B05 result (2.2), let `X,Y,S` be independent cap-one variables and consider the genuine quadratic form

```
Q=a S^2 + b Y^2 + 2 alpha X Y + linear terms,                       (6.1)
```

with `a alpha!=0`. Take the partner theorem's pivot `X`, environment `E=Y`, and slope

```
T(Y)=alpha Y+beta,
```

where `beta` is the coefficient contributed by the arbitrary linear term in `X`. Its density cap is at most `1/|alpha|`. The third variable `S` is an independent square with coefficient `a`. Equation (2.2) and the independent-square lift therefore give the actual inequality

```
boxed(
 ||p_Q||_infinity <=4 sqrt(2) |a alpha|^(-1/2).
)                                                                    (6.2)
```

The homogeneous quadratic core is

```
M=[[0,alpha,0],
   [alpha,b,0],
   [0,0,a]],
```

so

```
|det M|=|a| alpha^2.                                                 (6.3)
```

Hence (6.2) is exactly

```
4 sqrt(2) |det M|^(-1/4)|a|^(-1/4).                                (6.4)
```

If `|a|>=|det M|^(1/3)/4`, this becomes

```
||p_Q||_infinity <=8 |det M|^(-1/3).                               (6.5)
```

Thus the latest partner result independently recovers the determinant-normalized scale on this hyperbolic-square sector. The universal theorem in Section 4 is stronger because it also pays the complementary all-small-diagonal sector and arbitrary `3x3` couplings.

## 7. Application to the r24 punctured double-zero aggregate

Return to the aggregate geometry of Section 1. Let

```
u=Cv in R^(G1),  ||u||_2=1.                                       (7.1)
```

Fix a physical coordinate `i in G1`. Keep only `X_i` random from the first bank and condition on all other original coordinates of `G1` and on all coordinates outside the three active banks. Keep the normalized scalar-bank variables `Y,Z` random. Then:

- `X_i,Y,Z` are genuinely independent;
- their density caps are at most `1,sqrt(2),sqrt(2)`, respectively;
- the conditioned quadratic polynomial in `(X_i,Y,Z)` has arbitrary affine terms, which Corollary 5.1 allows.

The exact determinant of its `3x3` quadratic core is obtained by Schur complementation of the same scalar pair `B`. The scalar Schur entry in the physical coordinate `i` is

```
lambda u_i^2.
```

Therefore, using (1.1),

```
boxed(
 |det M_i|=|det B| |lambda| u_i^2=mu u_i^2.
)                                                                    (7.2)
```

This is an exact identity; no small-`B` approximation is used.

Apply Corollary 5.1 with cap product

```
1*sqrt(2)*sqrt(2)=2.
```

For every `i` with `u_i!=0`, uniformly in the conditioned coordinates,

```
||p_(Q | conditioning)||_infinity
 <=C3 2^(2/3) (mu u_i^2)^(-1/3).                                  (7.3)
```

Averaging the conditioning preserves the same bound. Thus, if

```
max_(i in G1) u_i^2 >= eta,                                         (7.4)
```

then

```
boxed(
 ||p_Q||_infinity
 <=8*2^(7/6)*3^(3/4) (mu eta)^(-1/3)
 <41 (mu eta)^(-1/3).
)                                                                    (7.5)
```

Most importantly, **(7.5) contains no factor involving `B`, `det B`, `sigma_min(B)`, or `||B||_op`.** Therefore the entire punctured double-zero scalar-pair regime is paid whenever the exploding Schur direction has a fixed positive physical leverage.

## 8. Exact remaining factor

The remaining B05 obligation in this aggregate packet is now

**`QFORM-DOUBLEZERO-DIFFUSE-SCHUR-GROUPING-v1`**:

> In the one-rank-two/two-rank-one aggregate geometry, assume `mu` is bounded below, the scalar pair may approach zero, and the unit physical Schur direction `u=Cv` is diffuse: `max_i u_i^2 ->0`. Prove a product-preserving grouping/coarea estimate that spends the total identity `sum_i u_i^2=1` **before** paying the local reciprocal factor `(u_i^2)^(-1/3)`, or produce a valid target-level counterexample.

The missing factor is therefore no longer the scalar-pair condition number, no longer the scalar-pair scale in the heavy-Schur subbranch, and no longer a local three-independent-scalar coarea estimate. It is specifically **aggregation across many small first-bank Schur coordinates while retaining the second first-bank aggregate that controls pair translations**.

One cannot simply replace the diffuse bank by the scalar projection `u dot X_G1` and declare the problem three-dimensional: the orthogonal aggregate in `G1` remains correlated with `u dot X_G1` and enters the pair translations. Conditioning on that orthogonal aggregate can destroy the density cap. Any next proof has to aggregate the original product bank jointly, or use an orientation-free theorem that retains that dependence.

## 9. Relation to the full conjecture

This run does not prove the full target. Even the exact-rank-three aggregate argument still has the diffuse-Schur grouping debt above, and the unrestricted matrix problem also has arbitrary additional spectral directions. No statement here turns a bounded projection density into an indefinite quadratic pushforward bound, and no post-rotation independence is assumed.

The result is nevertheless a strict local strengthening: **every nonsingular three-scalar independent quadratic core has a density bound controlled only by the determinant, at the scale forced by dilation.** In the r24 packet this converts the previously unpaid double-zero scalar-pair scale into a pure leverage/grouping problem.

## 10. Integrity audit

- The proof uses only independent scalar/source variables at the points where product density caps are required.
- The refuted arbitrary-joint rank-three coarea lemma is not used.
- The refuted law-uniform pointwise van-der-Corput estimate is not used.
- No moment, support, Gaussian, log-concavity, or eigenbasis-independence assumption is introduced.
- All signs and all zero-diagonal patterns of an invertible `3x3` scalar core are included by the two-case argument.
- No numerical simulation is used as proof.
- Continuity is not claimed.
- The full QFORM conjecture remains open.
