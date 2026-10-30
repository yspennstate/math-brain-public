SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-23T21:19:04Z.
attacking: QFORM-INDEFINITE-NEARNULL-ANCHORED-K-RECEIVER-v1; spend a physical diagonal of the anchored third-curvature bank by a determinant-only three-coordinate receiver, uniformly through det(H)->0-, and combine the residual diffuse-normal branch with fleet04/B06.

# fleet03/B06 r45 — determinant-only physical-triple receiver for anchored curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: `2026-09-22.15`; programme revision `2026-09-22.5`  
Assignment: curved fiber integration  
Status: `NEW SUPPORTING THEOREM + ACTUAL ANCHORED-K APPLICATION / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, post-rotation independence, or finite-rank hypothesis is added. The new theorem uses only literal original coordinates. It proves absolute continuity and an essential density bound, not continuity.

## 1. Fresh source state and exact predecessor

The immediate B06 predecessor is

`yspennstate/math-open-problems@eb5cd7bd244d799988b7fa618280b46713bd13c8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T205344Z-fleet03-B06-qform-r44/REPORT.md`.

There, for a physical two-hub block `H` and environment coupling matrix `E`, the full anchored third-curvature matrix was identified as

`K_H = det(H) Cenv - E^T adj(H) E`,                              (1.1)

with the exact identity

`(K_H)_{jk}=det A[{hub1,hub2,j},{hub1,hub2,k}]`.                 (1.2)

Thus every diagonal `(K_H)_{kk}` is exactly the determinant of a literal ORIGINAL-coordinate principal triple. The remaining r44 debt was the indefinite near-null collar, where a moving hyperbolic critical value prevents treating the completed environment remainder as arbitrary.

Two completed analytic inputs are used below at their proved scopes.

1. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, full source

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For two independent cap-one coordinates and an invertible symmetric `2 x 2` matrix `S`, arbitrary affine terms satisfy

`sup_t E |Y^T S Y + ell^T Y + c - t|^(-1/2)
 <=16 sqrt(30) |det S|^(-1/4)`.                                 (1.3)

The sharper constant applies because in two physical dimensions every affine vector lies in the full two-dimensional range.

2. `QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1`, full source

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite physical pair `B`, with `D=|det B|`, `kappa=sigma_min(B)`, and a residual `R` satisfying

`sup_t P(|R-t|<rho) <= H sqrt(rho)`,                             (1.4)

the full pair-plus-residual form has

`||p_Q||_infinity <=4 sqrt(2H) (D kappa)^(-1/4)`.                (1.5)

The physical-pair shifts may depend arbitrarily on the residual/environment.

A recent physical-three-core theorem was also checked to avoid duplicate work:

`yspennstate/math-open-problems@c46d60b27a443ae41a51ce9aaec12a1aab6243f9`

`proofnet24/QFORM-density/interactive/20260923T191724Z-physical-three-core/REPORT.md`.

It gives `<17/sigma_min(M)>`. The theorem below is different: it depends only on `|det M|^(1/3)`, and therefore remains uniform for highly anisotropic triples such as `diag(R,R,R^(-2))`, where the earlier minimum-singular-value bound grows like `R^2`.

## 2. Determinant-only three-physical-coordinate receiver

### Theorem 2.1 — `QFORM-PHYSICAL-TRIPLE-DETERMINANT-RECEIVER-v1`

Let `Z_1,Z_2,Z_3` be independent real random variables with densities at most one. Let `M=M^T` be any invertible real `3 x 3` matrix, and let `ell in R^3`, `c in R` be arbitrary. Then

`Q_3 = Z^T M Z + ell^T Z + c`                                   (2.1)

has an essentially bounded density satisfying

`boxed: ||p_(Q_3)||_infinity < 102 |det M|^(-1/3).`              (2.2)

No sign restriction is imposed on `M`.

### Proof

By scaling the whole polynomial it is enough to prove the result when

`|det M|=1`.                                                      (2.3)

Write

`M=[[a,b,c1],[b,d,e],[c1,e,f]]`.                                 (2.4)

Set the exact thresholds

`tau=109/200`, `m=11/20`.                                        (2.5)

There are two exhaustive cases.

### Case A: a physical diagonal pivot has size at least `tau`

After permuting the three ORIGINAL coordinates, suppose `|a|>=tau`. Write

`M=[[a,v^T],[v,N]]`,
`S=N-vv^T/a`.                                                     (2.6)

Since `M` is invertible,

`det S = det M/a`, hence `|det S|=1/|a|`.                         (2.7)

Complete the square only in the literal scalar `Z_1`:

`Q_3 = a[Z_1+psi(Z_2,Z_3)]^2
       + Y^T S Y + beta^T Y + c0`,                               (2.8)

where `Y=(Z_2,Z_3)` and `beta,c0` are arbitrary. Conditioning on `Y`, the translated `Z_1` still has conditional density cap one. The square pushforward formula gives, for almost every output `t`,

`p_(Q_3)(t)
 <= |a|^(-1/2)
    E |Y^T S Y+beta^T Y+c0-t|^(-1/2)`.                           (2.9)

Apply (1.3) to the two original independent coordinates in `Y`:

`||p_(Q_3)||_infinity
 <=16 sqrt(30) |a|^(-1/2)|det S|^(-1/4)
 =16 sqrt(30) |a|^(-1/4)
 <=16 sqrt(30) (200/109)^(1/4).`                                 (2.10)

The last constant is `101.9956111...<102`. An exact check is

`[16 sqrt(30)(200/109)^(1/4)]^4
 =11796480000/109
 <102^4`,                                                        (2.11)

with positive gap `2030544/109` after putting both fourth powers over the common denominator.

### Case B: all three physical diagonals are smaller than `tau`

Assume

`|a|,|d|,|f|<109/200`.                                           (2.12)

If also all three off-diagonal entries had modulus at most `11/20`, the determinant formula would give

`|det M|
 <= |adf|+2|bc1e|+|a|e^2+|d|c1^2+|f|b^2`
` < tau^3+2m^3+3 tau m^2`
` =7913729/8000000 <1`,                                         (2.13)

contradicting (2.3). Therefore some off-diagonal entry, say `|b|`, satisfies

`|b|>11/20`.                                                     (2.14)

The physical pair

`B=[[a,b],[b,d]]`                                                 (2.15)

is indefinite because `b^2>|ad|`. Compare it with `[[0,b],[b,0]]`. The diagonal perturbation has operator norm `<109/200`, so both eigenvalue moduli of `B` exceed

`|b|-109/200 > 1/200`.                                          (2.16)

Hence

`kappa=sigma_min(B)>1/200`.                                      (2.17)

Complete the physical pair. The remaining scalar quadratic coefficient is its Schur coefficient `lambda`; the determinant identity gives

`|lambda|=|det M|/|det B|=1/D`, `D=|det B|`.                     (2.18)

For the remaining original scalar `Z_3`, an arbitrary affine perturbation of `lambda Z_3^2` obeys the elementary interval estimate

`sup_t P(|lambda Z_3^2+u Z_3+v-t|<rho)
 <=2 sqrt(2) sqrt(rho/|lambda|)
 =2 sqrt(2D) sqrt(rho)`.                                         (2.19)

Indeed, after completing the scalar square, the inverse image of an interval of length `2rho/|lambda|` under `x^2` has total Lebesgue length at most `2 sqrt(2rho/|lambda|)`; the input density is at most one.

Thus (1.4) holds with

`H=2 sqrt(2D)`.                                                   (2.20)

Insert this into the hyperbolic pair-log receiver (1.5):

`||p_(Q_3)||_infinity
 <=4 sqrt(4 sqrt(2) D^(1/2)) (D kappa)^(-1/4)`
` =8*2^(1/4) kappa^(-1/4)`
` <8*2^(1/4)*200^(1/4)`
` =35.77708764... <36`.                                          (2.21)

The entire determinant `D` cancels. Thus Case B is substantially cheaper than Case A. Combining (2.10) and (2.21) proves (2.2) under normalization (2.3).

For general `M`, put `s=|det M|^(1/3)` and divide the whole polynomial by `s`. The normalized matrix has determinant modulus one, while density rescales by `s^(-1)`. This proves (2.2). QED.

### Scope

This is a genuine determinant receiver, not a minimum-singular-value estimate. It is also product preserving: every conditioning step is on literal original coordinates. The two analytic branches integrate either the full rank-two half-Riesz kernel or the full hyperbolic pair-log kernel before taking an output supremum. No rotated coordinate is declared independent and no unrestricted spectral-fiber supremum appears.

Continuity is not asserted by the proof; the theorem establishes absolute continuity and an essential `L^infinity` bound.

## 3. Anchored-curvature corollary: a diagonal of `K_H` pays uniformly through the hyperbolic null limit

Let an arbitrary full symmetric matrix be partitioned around two literal physical hubs as

`A=[[H,E],[E^T,Cenv]]`,                                          (3.1)

and let `K_H` be (1.1). Fix an environment original coordinate `k`. By (1.2),

`(K_H)_{kk}=det A[{hub1,hub2,k},{hub1,hub2,k}]`.                  (3.2)

Condition on every original coordinate outside this physical triple. The conditional polynomial in the three retained independent variables has quadratic matrix exactly that principal triple and arbitrary affine terms. Theorem 2.1 therefore gives the target-level implication

`boxed:
 |(K_H)_{kk}|>=eta>0
 => ||p_(X^T A X)||_infinity <=102 eta^(-1/3).`                   (3.3)

This estimate is independent of `det H`, `sigma_min(H)`, the size/rank/sign of `Cenv`, and every outside coupling. In particular it is uniform as an indefinite hub tends to rank one through `det H ->0-`. This directly spends genuine third curvature instead of hiding it in an arbitrary completed remainder, which r44 proved impossible.

The genuinely unpaid near-null chamber is therefore narrower:

`all diagonal anchored curvatures |(K_H)_{kk}| are small`,        (3.4)

while a nontrivial off-diagonal/aggregate `K_H` currency may remain. That aggregate-before-diagonal-extraction problem is the next curved-fiber step.

## 4. Actual designated-partner splice

The completed designated partner theorem is

`yspennstate/math-open-problems@f24c8db8946d54f4da2d11898697913af766ad32`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B06/20260923T184145Z-fleet04-B06-QFORM-r1/REPORT.md`,

`QFORM-BANKWISE-TRIPLE-CURVATURE-v1`.

In its live exact-rank-three chamber, an indefinite physical pair `B` satisfies

`D |lambda|>=1/4`,                                                (4.1)

and three disjoint original-coordinate banks have normal masses `W_b` with

`W_1 W_2 W_3>61/1728`.                                           (4.2)

Choose the maximal-normal-mass bank `b_*`. Then

`W_(b_*)>(61/1728)^(1/3)=0.3280414319...`.                       (4.3)

The exact anchored curvature on this bank is rank one:

`K_(B,b_*)=det(B) lambda h_(b_*) h_(b_*)^T`.                     (4.4)

Hence every physical diagonal there is

`|(K_B)_{kk}|=D|lambda| h_k^2`.                                  (4.5)

There is now an explicit combined trichotomy.

1. If some `k in b_*` has `h_k^2>=1/64`, then (4.1) and (4.5) give

`|(K_B)_{kk}|>=1/256`.                                           (4.6)

The new physical-triple determinant receiver (3.3) yields

`boxed: ||p_Q||_infinity <102*256^(1/3)
       =647.6596293... <647.660.`                                (4.7)

2. Otherwise every normal atom in the maximal bank obeys

`h_k^2<1/64`.                                                     (4.8)

If that same bank satisfies the partner's normalized leverage gate `ell_k<=1/2` and transversality gate

`det G_(b_*)>=W_(b_*)/64`,                                       (4.9)

the partner theorem applies at the actual inequality

`||p_Q||_infinity
 <=12[D|lambda|det G_(b_*)]^(-1/3)`
` <12[(1/4)(61/1728)^(1/3)/64]^(-1/3)`
` =110.4803398469... <110.481`,                                  (4.10)

with a continuous `C_0` density.

3. Therefore the still-unpaid maximal bank simultaneously satisfies the strong normal diffuseness (4.8) and at least one of the two partner failures:

`max_k ell_k>1/2`                                                 (4.11)

or

`det G_(b_*)<W_(b_*)/64`.                                        (4.12)

This is strictly sharper than retaining an unspecified nonzero anchored-curvature matrix: a large physical diagonal is paid by (3.3), a diffuse/transverse bank is paid by the designated partner, and only diffuse-normal/heavy-leverage or diffuse-normal/shear-flat geometry survives.

## 5. Checks and integrity

Exact arithmetic used above:

`tau^3+2m^3+3tau m^2 = 7913729/8000000 = 0.989216125`,           (5.1)

`16 sqrt(30)(200/109)^(1/4)=101.9956111228...`,                  (5.2)

`8*2^(1/4)*200^(1/4)=35.7770876400...`,                          (5.3)

`102*256^(1/3)=647.6596292030...`.                               (5.4)

A finite random sanity check on 200,000 symmetric Gaussian matrices normalized to determinant modulus one found 7,451 instances in Case B, no violation of the forced `max offdiag>11/20` condition, and no violation of `sigma_min(B)>1/200` for the selected maximum-offdiagonal pair. The minimum observed `sigma_min(B)` was about `0.1721`. This computation is not part of the proof.

The existing physical-three-core theorem `<17/sigma_min(M)>` was explicitly checked before publication. The present determinant-only theorem is not a duplicate of that scope: neither bound dominates the other uniformly, and the determinant theorem is the useful one for the anchored `K_H` currency.

## 6. Remaining implication

The first B06 debt is now

`QFORM-INDEFINITE-NEARNULL-OFFDIAGONAL-K-AGGREGATION-v1`.

Assume the indefinite hub is near rank one and all physical principal anchored curvatures `(K_H)_{kk}` are below the chosen target scale, while `K_H` still carries substantial off-diagonal/Frobenius curvature. The next step must aggregate that off-diagonal third-curvature bank against the original product law before taking any reciprocal minor or curved-fiber supremum. In the exact-rank-three partner chamber, the surviving maximal bank is additionally normal-diffuse and either triple-frame-heavy or shear-flat by (4.8)-(4.12). A valid closure may route these two failures into a grouped crossing/promotion theorem, but every gate must be checked on the actual matrix.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.** Continuity is proved here only on the separately scoped designated-partner branch (4.10); the new determinant-only receiver proves essential boundedness/absolute continuity.
