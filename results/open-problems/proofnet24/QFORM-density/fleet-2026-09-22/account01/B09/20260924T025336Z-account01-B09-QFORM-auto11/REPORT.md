# account01/B09 — singular-pair transverse-curvature forcing

Status: **NEW SUPPORTING STRUCTURAL THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

Programme: `QFORM-DENSITY-3EIG-20260922`, owner-control revision observed `2026-09-22.15`.

Target remains: independent real inputs with one-dimensional densities bounded by one, arbitrary real symmetric `A`, at least three singular/eigenvalue magnitudes at least one; prove a universal density bound or give a valid counterexample. No rotated-coordinate independence is used below.

## 1. Setup: exact singular physical pair and rank-one star

Let `H={h1,h2}` be a literal original-coordinate pair and `L=H^c`. Assume

`B=A[H,H]=tau ell ell^T`,

where `ell in R^2` is unit and `tau != 0`, and assume the physical pair-to-leaf block has exact rank one,

`A[H,L]=g r^T`.

Let `k` be the unit vector in `R^2` perpendicular to `ell`, and write

`alpha=k^T g`, `beta=ell^T g`, `R=||r||_2`, `u=r/R`

when `R>0`. The interesting singular-star branch has `alpha R>0`; put

`s=|alpha|R`.

Rotating only the two-dimensional hub coefficient space by the orthogonal basis `(ell,k)` is an algebraic change inside the hub block; no independence of the rotated hub coordinates is asserted. In that basis the matrix is

```
A = [ tau   0    beta r^T ]
    [  0    0   alpha r^T ]
    [ beta r alpha r    D  ],
```

where `D=A[L,L]` is completely arbitrary symmetric.

Let

`P=I-u u^T`, `E=P D P`.

Thus `E` is the part of the leaf curvature acting fully inside the subspace transverse to the star direction `u`.

## 2. Theorem: the three-large-eigenvalue hypothesis forces transverse leaf curvature

### QFORM-SINGULARPAIR-TRANSVERSE-CURVATURE-v1

Under the setup above,

`boxed: s_3(A) <= |tau| + ||E||_op.`

Consequently, if the owner's target hypothesis `s_3(A)>=1` holds, then

`boxed: ||PDP||_op >= 1-|tau|.`

In particular, whenever `|tau|<1`, a nontrivial transverse leaf-curvature operator is forced. This is stronger than the earlier statement `||D||_op >=1-|tau|`: curvature aligned with the star direction does not count.

### Proof

Decompose

`D = delta u u^T + u h^T + h u^T + E`,

where

`delta=u^T D u`, `h=P D u`, `h perpendicular to u`.

Let `A0` be obtained from `A` by replacing `D` with

`D0=delta u u^T+u h^T+h u^T=D-E`.

Embed `u` in the full hub-plus-leaf space as

`e=(0,0,u)`

and set

`v=(beta R, alpha R, h+(delta/2)u)`.

Then exactly

`A0 - tau e_ell e_ell^T = e v^T + v e^T`,

where `e_ell=(1,0,0_L)` in the rotated hub basis. The right-hand side has rank at most two. Therefore the distance in operator norm from `A0` to a rank-at-most-two matrix is at most `|tau|`. By Eckart–Young,

`s_3(A0) <= |tau|`.

Since

`A-A0 = diag(0_H,E)`,

singular-value Lipschitz continuity gives

`s_3(A) <= s_3(A0)+||E||_op <= |tau|+||E||_op`.

This proves the theorem. No probability argument is used and no leaf curvature is discarded.

## 3. Exact mixed third-compound identity

For each unordered leaf pair `I={i,j}`, define

`v_I = u_j e_i - u_i e_j`.

These vectors form a Parseval frame on `u^perp`:

`boxed: sum_I v_I v_I^T = P.`

Indeed, for every `x`,

`sum_{i<j}(u_j x_i-u_i x_j)^2 = ||x||_2^2-(u^T x)^2`.

Let `k` denote the rotated kernel hub coordinate. For unordered leaf pairs `I={i,j}` and `J={p,q}`, define the grouped-hub third minor

`M_{I,J}=det A[{k,i,j},{k,p,q}]`.

A direct determinant expansion gives

`boxed: M_{I,J} = -s^2 v_I^T E v_J.`

(The aligned pieces `delta uu^T+u h^T+h u^T` vanish because every `v_I` is orthogonal to `u`.) Hence

`sum_{I,J} M_{I,J}^2
 = s^4 sum_{I,J}(v_I^T E v_J)^2
 = s^4 tr(E P E P)
 = boxed: s^4 ||E||_F^2.`

This is an exact identity, not an inequality or a random-partition estimate.

## 4. Diffuse star: principal pair-pair terms cannot dominate

Let

`q=max_i u_i^2 = max_i r_i^2/||r||_2^2`.

For one leaf pair `I`,

`||v_I||_2^2=u_i^2+u_j^2 <=2q`.

Therefore, by Cauchy–Schwarz,

`(v_I^T E v_I)^2 <= ||v_I||_2^2 v_I^T E^2 v_I`.

Summing and using the Parseval identity,

`sum_I M_{I,I}^2
 <= 2q s^4 tr(E^2 P)
 = 2q s^4 ||E||_F^2`.

Thus the **off-diagonal leaf-pair currency** obeys

`boxed:
 sum_{I!=J} M_{I,J}^2
 >= (1-2q)s^4||E||_F^2.`

So, in the diffuse-star branch `q<1/16`, at least `7/8` of this grouped third-compound mass comes from *different* leaf pairs. This eliminates the possibility that all forced transverse curvature hides only in grouped principal triples.

## 5. Return to literal physical coordinates

For fixed leaf pairs `I,J`, form the physical `2x2` minor matrix

`C_{I,J}(a,b)=det A[{h_a} union I,{h_b} union J]`, `a,b in {1,2}`.

Under the orthogonal two-hub basis change, this matrix transforms by left/right orthogonal multiplication. In particular, the grouped kernel-kernel minor `M_{I,J}` is one entry of the transformed `2x2` matrix, so

`||C_{I,J}||_F^2 >= |M_{I,J}|^2`.

When `I!=J`, none of the corresponding physical row and column triples are identical. Hence their overlaps have size at most two. Therefore the literal physical third-compound sectors satisfy

`boxed:
 Omega_0(A)+Omega_1(A)+Omega_2(A)
 >= (1-2q)s^4||PDP||_F^2`

within this singular-pair/rank-one-cross branch, where `Omega_r` is the sum of squared `3x3` minors over physical row/column triples with intersection size `r`.

This inequality is source-coordinate valid: the hub rotation is used only to prove an invariant lower bound on the Frobenius sum of literal physical minors.

## 6. Quantitative target corollary for the previously unpaid tiny-pivot diffuse collar

The preceding account01/B09 identity for the anchored overlap-two packet gives, for an exact rank-one pair,

`P_H+Omega_(2,H)=tau^2 alpha^4 ||r||_2^4 = (|tau|s^2)^2`.

Hence, if

`Omega_(2,H)>=1/4`, `q<1/16`, `|tau|<1/8`,

then

`|tau|s^2 >=1/2`, hence `s>2`.

If in addition the full owner target `s_3(A)>=1` holds, Theorem 2 gives

`||PDP||_op >7/8`, hence `||PDP||_F>7/8`.

Substituting into the off-diagonal mixed-volume bound yields

`Omega_0+Omega_1+Omega_2
 > (7/8)*16*(7/8)^2
 = boxed: 343/32
 = 10.71875.`

Thus the exact singular-pair, diffuse-star, tiny-pivot endpoint cannot remain a curvature-invisible collar. It forces a **macroscopic nonprincipal physical third-compound packet**. Equivalently, at least one of the literal overlap sectors `Omega_0,Omega_1,Omega_2` exceeds

`343/96 = 3.572916...`.

This is a structural reduction, not yet a full density theorem: the disjoint `Omega_0` sector is compatible with completed bilinear crossing receivers, while the one-/two-shared sectors still require aggregate-before-inversion payment. The result identifies precisely where the arbitrary same-leaf curvature must reappear.

## 7. Designated account02/B09 result applied to an actual target inequality

Use account02/B09 r15, canonical source

`yspennstate/math-open-problems@57b57dc6fa114b1c782a91599bdfbe94a358b2cb`

which proves the square–hyperbola receiver

`||p_(aU^2+2bVW)||_infinity
 <= 3*2^(2/3) M^(2/3)S^(2/3)|a|^(-1/3)|b|^(-2/3)`

when `(U,V)` has joint density at most `M` and `W` is independent with density at most `S`.

Take three original independent coordinates with cap-one densities and

`Q=2X_1^2+6X_2X_3`.

Here `(U,V)=(X_1,X_2)` has joint density at most one, `W=X_3` has density at most one, `a=2`, `b=3`. The symmetric matrix is

`diag(2) direct_sum [[0,3],[3,0]]`,

with eigenvalues `{2,3,-3}`; it is an exact owner-target instance. The partner theorem gives the concrete inequality

`boxed: ||p_Q||_infinity <= 6^(1/3) = 1.8171205928...`,

and therefore

`boxed: P{Q in I} <= 6^(1/3)|I|`

for every interval `I`. I do not claim continuity here beyond the exact conclusion recorded in the partner theorem.

## 8. What remains

The new first unpaid implication is

`QFORM-SINGULARPAIR-NONPRINCIPAL-VOLUME-PAYMENT-v1`:

starting from the forced physical nonprincipal third-compound currency above, aggregate the `Omega_1/Omega_2` sectors without selecting a single tiny minor or inverting a vanishing pair pivot; alternatively show that a universally positive share must enter an already-paid disjoint crossing receiver. Any valid argument must retain arbitrary same-bank curvature and original-coordinate product provenance.

The unrestricted QFORM conjecture remains **OPEN**. No counterexample is produced. Full-target continuity is also **OPEN**.
