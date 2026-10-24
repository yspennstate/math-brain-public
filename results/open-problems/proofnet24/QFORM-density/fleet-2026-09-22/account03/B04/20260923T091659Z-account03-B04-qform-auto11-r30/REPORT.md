# QFORM account03/B04 r30 — soft-ridge third-volume product-Fourier gate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement.  
Status: `NEW SUPPORTING THEOREM / FULL TARGET OPEN`.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and scope

The global target is unchanged: for every dimension, every independent real input coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix A with at least three eigenvalues of absolute value at least one, prove a universal L-infinity bound for the density of Q=X^T A X, or give a valid counterexample. No moment, support, Gaussian, log-concave, iid, or post-rotation independence assumptions are used below.

This run proves a new sufficient product-Fourier certificate for an ORIGINAL-coordinate cross block M. It preserves arbitrary quadratic curvature inside both banks, arbitrary outside-coordinate conditioning, and arbitrary affine terms. The conclusion in this branch is a bounded continuous density vanishing at infinity.

Fresh corrections consumed include: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no arbitrary-joint rank-three coarea shortcut; no naive fiber-supremum dimension-free bound; no claim that one good physical minor is forced. The full theorem remains open.

## 2. Sources actually used at equations

1. The q-dependent fractional third-volume Fourier theorem and exact volume-marginal matrix W are from

`yspennstate/math-open-problems@96ef944654c4056cc75bba6256e600eb791fb2d1:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its theorem says: if E3(M)>0 and all row third-volume inclusion marginals alpha_i satisfy alpha_i<=q/2 for some 1<=q<3/2, then

`||p_Q||inf <= [3e/((3-2q)sqrt(q))] E3(M)^(-1/6)`,

with a continuous C0 density, for arbitrary same-bank phases and outside-conditioned affine terms.

2. The scheduled peer identity actually applied here is account01/B20

`yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f:proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260922T234545Z-account01-B20-QFORM-auto11/REPORT.md`:

`T2 E2 <= 3 E3`, where T2=sum_(j>=3) s_j(M)^2 and Ek=e_k(s_1(M)^2,s_2(M)^2,...).

The designated account04/B04 partner still had no completed current-QFORM canonical math archive subtree, no current-QFORM shared handoff, and no recovery subtree at the fresh direct lookups made in this run, so no account04/B04 theorem is fabricated. The account01/B20 result above is the completed peer result consumed at an equation.

## 3. Exact third-volume marginal matrix

Let the squared singular values of M be

`lambda_1>=lambda_2>=...>=0`,

and assume rank(M)>=3, equivalently T2>0 and E3>0. Write an SVD M=U diag(s_j)V^T. Under the canonical squared-3x3-minor probability law, the row inclusion marginals satisfy

`alpha_i=W_ii`,

where

`W=U diag(p_j) U^T`,

`p_j=lambda_j e2(lambda without j)/E3`.

The exact formula is part of the completed source above. Since

`E3=lambda_j e2(lambda without j)+e3(lambda without j)`,

we have `0<=p_j<=1`. Also `e2(lambda without j)<=E2`, hence the account01/B20 identity gives

`p_j <= lambda_j E2/E3 <= 3 lambda_j/T2`.

Therefore

`p_j <= min(1,3 lambda_j/T2)`.                                      (1)

This is the only place where the peer identity is used, and it is used before Fourier inversion.

## 4. New theorem: QFORM-SOFT-RIDGE-THIRDVOLUME-GATE-v1

For theta>0 define the row-side ridge-leverage matrix at the intrinsic tail scale

`K_theta = M M^T (M M^T + theta T2 I)^(-1)`

and

`L_theta=max_i (K_theta)_ii`,

`A_theta=(1+3 theta)L_theta`.

Then for every theta>0,

`boxed: W <= (1+3 theta) K_theta`.                              (2)

Consequently, if `A_theta<3/4`, define

`q_theta=max(1,2 A_theta)`,

so `1<=q_theta<3/2`. Then every alpha_i<=A_theta<=q_theta/2, and the completed fractional-volume theorem yields

`boxed: ||p_Q||inf <= C(A_theta) E3(M)^(-1/6)`,                (3)

where

`C(A)=3e` for `A<=1/2`,

and

`C(A)=3e/[(3-4A)sqrt(2A)]` for `1/2<A<3/4`.                  (4)

The density has a continuous representative in C0(R).

Because

`E3(M)>=s1(M)^2 s2(M)^2 T2`,

(3) also gives

`||p_Q||inf <= C(A_theta)[s1(M)^2 s2(M)^2 T2]^(-1/6)`.       (5)

### Proof of the operator inequality

Set x=lambda_j. We claim, for every x>=0,

`min(1,3x/T2) <= (1+3theta)x/(x+theta T2)`.                  (6)

If `x<=T2/3`, the left side is `3x/T2`; after dividing by x when x>0, (6) is equivalent to

`3(x+theta T2)<=T2(1+3theta)`,

which is exactly `3x<=T2`. The x=0 case is immediate.

If `x>=T2/3`, the left side is one; (6) is equivalent to

`x+theta T2 <= (1+3theta)x`,

which is exactly `T2<=3x`.

Thus (6) holds for every singular mode. Combining it with (1) and diagonalizing in the common left-singular basis gives (2). The diagonal bound `alpha_i<=A_theta` is immediate. Equations (3)-(4) are then a direct application of the q-dependent product-Fourier theorem. No pointwise oscillatory envelope is used.

## 5. Fixed-scale robust dichotomy: Fourier exit or an aggregate physical hub

Take `theta=1/3`, and write

`K = M M^T(M M^T + (T2/3)I)^(-1)`.

Then (2) becomes `W<=2K`.

If `max_i K_ii<=1/3`, then `alpha_i<=2/3`, so q=4/3 is admissible and

`boxed: ||p_Q||inf <= (9 sqrt(3)e/2) E3(M)^(-1/6)`.           (7)

If instead `max_i K_ii>1/3`, then there is a physical row i with an aggregate star-energy lower bound

`boxed: ||M^T e_i||_2^2 > T2/9`.                              (8)

Indeed the scalar inequality `x/(x+T2/3)<=3x/T2` implies the operator bound

`K <= (3/T2) M M^T`.

Thus `K_ii>1/3` forces `(M M^T)_ii>T2/9`.

Applying the same statement to M^T yields a two-sided version: either one orientation pays (7), or failure of both row and column soft-ridge gates produces an actual physical row and an actual physical column, each carrying more than `T2/9` of aggregate squared cross energy. This is a concrete double-hub survivor and avoids selecting a tiny individual entry.

This does not by itself pay the double-hub case; it sharpens the remaining structural obligation.

## 6. Strict extension of the preceding hard-projection certificate on an explicit matrix

The previous tail extension used an orthogonal projection P and required simultaneously

`max_i P_ii<=1/2`,

`||(I-P)M||op <= sqrt(T2)/15`.

The new soft-ridge certificate can succeed when no such P exists.

Let H_64 be a Sylvester Hadamard matrix and put `V=H_64/8`, so V is orthogonal and every entry is +/-1/8. Let

`D=diag(2,2,1,...,1)`

with 62 trailing ones, and define

`M=D V`.

Then M is dense in physical coordinates: its first two rows have all entries +/-1/4 and its other 62 rows have all entries +/-1/8. Its singular values are

`2,2,1,...,1`.

Hence

`T2=62`,

and at theta=1/3,

`K=M M^T(M M^T+(62/3)I)^(-1)`

is diagonal with first two entries

`4/(4+62/3)=6/37`,

and the remaining entries

`1/(1+62/3)=3/65`.

Therefore

`L_theta=6/37`,

`A_theta=2L_theta=12/37<1/2`,

so the sharp q=1 branch of (3) applies.

The third singular volume is exactly

`E3=C(62,3)+8 C(62,2)+16*62=53940`.

Thus, for every admissible independent cap-one product input law and arbitrary measurable same-bank phases allowed by the source theorem,

`boxed: ||p_Q||inf <= 3e * 53940^(-1/6)`

`                       = 1.326673068190509...`.               (9)

The density is continuous and vanishes at infinity.

Now verify that the previous hard-projection tail certificate fails for every P on this same M. Its residual threshold is

`sqrt(T2)/15=sqrt(62)/15=0.5249338582...<1=s_min(M)`.

If P is any orthogonal projection different from I, choose a unit vector y in range(I-P). Since `||M^(-1)||op=1`, the unit vector

`x=M^(-1)y/||M^(-1)y||`

satisfies

`||(I-P)Mx||=1/||M^(-1)y||>=1`.

Hence every P!=I has `||(I-P)M||op>=1`, violating the residual threshold. The only projection meeting the residual threshold is P=I, but then `max_i P_ii=1`, violating the leverage gate. Therefore the old hard-projection certificate fails for every P, while the new soft-ridge volume certificate gives (9).

This is a strict extension of that certificate, not a claim that no other theorem in the fleet controls this family.

## 7. Genuinely rotated indefinite target

Set

`A = [[0,M],[M^T,0]]`,

an explicit real symmetric 128-by-128 matrix in the original product coordinates. Its eigenvalues are the signed singular values of M:

`+2,+2,+1 (62 times), -2,-2,-1 (62 times)`.

Thus A is indefinite and satisfies the original target hypothesis by a very large margin. It is not diagonal in the independent coordinates, and every one of its 64-by-64 cross-bank physical coefficients is nonzero.

For `Q=X^T A X=2 X_L^T M X_R`, equation (9) gives the explicit universal-over-input-laws estimate

`boxed: ||p_Q||inf <= 1.326673068190509...`,

with a continuous C0 density.

No Gaussianity, compact support, moments, log-concavity, connected support, or independence after diagonalizing A is used.

## 8. Application to the account01/B20 R-packet

Account01/B20's substantial-third-volume branch had `E3(D)>=2^(-18)`. Apply the fixed-scale theorem above to that actual physical cross block D.

If one of D or D^T has soft ridge leverage `max diag K<=1/3` at theta=1/3, then (7) yields

`||p_Q||inf <= (9 sqrt(3)e/2) * (2^(-18))^(-1/6)`

`             = 36 sqrt(3)e`

`             = 169.495282...`,

with continuity. This slightly sharpens the older 172.726 diffuse-volume constant in that packet.

If both orientations fail, the packet now comes with an explicit physical double-hub certificate: one row and one column each carry more than `T2(D)/9` aggregate squared cross energy. This is a stronger structural endpoint than merely saying a third-volume marginal is concentrated.

The rank-two-tube/small-total-tail and the resulting double-hub payment remain open.

## 9. What changed and what remains

New proved content in this run:

1. `QFORM-SOFT-RIDGE-THIRDVOLUME-GATE-v1`, equations (2)-(5).
2. The fixed-scale soft-ridge-or-aggregate-hub dichotomy, equations (7)-(8), and its two-sided version.
3. A dense, genuinely rotated indefinite 128-dimensional target for which every hard projection certificate of the preceding tail theorem fails, while the new theorem gives the explicit bound 1.326673068190509.
4. An equation-level application of the scheduled account01/B20 identity to the new marginal domination, plus a sharpened routing of its R-packet.

Full QFORM remains OPEN. The next B04 obligation is:

`QFORM-SOFT-RIDGE-DOUBLE-HUB-PAYMENT-v1` — start from the survivor in which both row and column intrinsic ridge leverages exceed 1/3, hence there are physical row/column hubs carrying >T2/9 aggregate tail energy, and combine that aggregate hub information with the already-paid physical-pair / half-Riesz / grouped-bank endpoints without inverting a vanishing individual coefficient.

Continuity is proved in the soft-ridge Fourier branch only; no continuity statement is claimed for the full target.
