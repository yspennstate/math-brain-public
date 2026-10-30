SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-24T07:48:06Z.
attacking: the low-tetrad Schur-numerator chamber by splicing the physical-pair one-third density envelope with the global off-diagonal one-third Riesz estimate, before any tetrad/minor is selected.

# fleet03/B04 r53 — the whole overlap-two Schur packet is paid by one-third Riesz

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM / ENTIRE J2 OVERLAP-TWO BRANCH PAID / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity: the new theorem proves absolute continuity and an essential density bound. It does **not** by itself prove continuity. Full-target continuity remains OPEN.

The target is unchanged: the coordinates are independent ORIGINAL real coordinates with one-dimensional density caps one, and `A` is arbitrary real symmetric with at least three eigenvalues of modulus at least one. No Gaussian, moment, log-concavity, compact-support, connected-support, iid, diagonal-basis, post-rotation independence, arbitrary-joint coarea, fiber-supremum, or law-uniform scalar pointwise quadratic-phase decay hypothesis is introduced.


## 1. Two source-valid analytic inputs

### 1.1 Physical-pair one-third density envelope

The preceding B04 r52 report, at

`yspennstate/math-open-problems@fbc50959f73f2a66b91acacbbacc37cbf2b66720`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260924T064507Z-fleet03-B04-QFORM-auto11-r52/REPORT.md`,

records the completed B04 r51 physical-pair estimate. For two ORIGINAL independent cap-one variables, every invertible symmetric physical pair `B`, and every deterministic translation, the centered pair-quadratic output `T` has density

`p_T(u) <= C_pair |det B|^(-1/3)|u|^(-1/3)`                    (1.1)

for a.e. `u != 0`, where

`C_pair = 2+2*pi = 8.283185307179586... .`                         (1.2)

The translation may depend on coordinates conditioned outside the pair; after conditioning it is deterministic and the two physical inputs remain independent cap-one variables.

### 1.2 Global off-diagonal sub-half-Riesz theorem

The source report

`yspennstate/math-open-problems@0d074396abdd021a817f0b8dc104b826f2d7154d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260923T060557Z-fleet02-B01-qform-auto11/REPORT.md`

proves `QFORM-GLOBAL-OFFDIAG-SUBHALF-RIESZ-v1`. If

`R=Y^T C Y+b^T Y+c`,                                              (1.3)

where the `Y_j` are independent original cap-one coordinates, `C=C^T`, and

`F(C)=sum_(i!=j) C_ij^2>0`,                                       (1.4)

then for every `0<beta<1/2`,

`H_beta(R):=sup_s E|R-s|^(-beta)
 <= C_beta F(C)^(-beta/2)`,                                      (1.5)

with

`C_beta = e^(beta/2)(4*pi)^beta /
 [beta(1-2beta) Gamma(beta) cos(pi beta/2)].`                      (1.6)

Its proof is explicitly product-preserving: it first takes an ORIGINAL-coordinate random cut, then uses either a diffuse order-one determinant law or a heavy physical row and an aggregate random-slope Fourier estimate. It is an integrated/fractional-potential bound and is compatible with the phase-aligned counterexample to scalar pointwise quadratic-phase decay.

At `beta=1/3`,

`C_(1/3)
 = 6 sqrt(3) e^(1/6)(4*pi)^(1/3)/Gamma(1/3)
 = 10.654543088663740... .`                                      (1.7)

## 2. Schur numerator and the overlap-two packet

Fix any literal physical pair `H={h_1,h_2}` and write, in ORIGINAL coordinates,

`A = [[B,C^T],[C,D]],`                                             (2.1)

with `B=A[H,H]` symmetric `2 x 2`. Define the polynomial Schur numerator

`N_H := det(B)D-C adj(B)C^T`.                                     (2.2)

For distinct residual physical indices `i,j`, the bordered determinant identity is

`(N_H)_ij = det A[H union {i}, H union {j}]`                      (2.3)

up to the harmless common ordering convention. Thus the fixed-pair overlap-two third-compound packet is exactly

`J_2(H) := sum_(i!=j) (N_H)_ij^2.`                                (2.4)

When `det B != 0`, the exact Schur residual is

`S_H = D-CB^(-1)C^T = N_H/det B`.                                (2.5)

Consequently its full original-coordinate off-diagonal energy is

`F(S_H)
 = sum_(i!=j) (S_H)_ij^2
 = J_2(H)/|det B|^2.`                                              (2.6)

Equation (2.6), not a selected tetrad, is the correct currency for the one-third Riesz splice.

## 3. Main theorem — `QFORM-PAIR-SCHUR-NUMERATOR-J2-RECEIVER-v1`

### Theorem

Let `Q=X^TAX+b^TX+c` with arbitrary real symmetric `A`, arbitrary affine terms, and independent cap-one ORIGINAL input coordinates. Fix any literal physical pair `H` and define `N_H,J_2(H)` by (2.2)-(2.4). If

`J_2(H)>0`,                                                        (3.1)

then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= C_J2 J_2(H)^(-1/6),`                                          (3.2)

where

`C_J2
 = 12 sqrt(3)(1+pi)e^(1/6)(4*pi)^(1/3)/Gamma(1/3)
 = 88.25355476673130... .`                                        (3.3)

The statement includes singular physical pairs `B`. It retains all signs, all same-residual-bank curvature, all affine terms generated by conditioning, and all extra spectrum.

### Proof for `det B != 0`

Complete the actual physical pair without rotating random variables. With `Y=X_(H^c)`,

`Q=(X_H+h(Y))^T B (X_H+h(Y)) + R(Y),`                             (3.4)

where `h(Y)` is an affine physical-coordinate translation and the quadratic part of `R` is exactly `S_H` in (2.5).

Condition on `Y=y`. By the physical-pair envelope (1.1), uniformly in the translation `h(y)`,

`p_(Q|Y=y)(q)
 <= C_pair |det B|^(-1/3)|q-R(y)|^(-1/3).`                        (3.5)

Average over `Y`:

`p_Q(q)
 <= C_pair |det B|^(-1/3)
    E|q-R(Y)|^(-1/3).`                                            (3.6)

Apply the global off-diagonal theorem (1.5) at `beta=1/3` to the **whole residual quadratic polynomial** `R`, retaining every diagonal and affine term. By (2.6),

`sup_q E|q-R|^(-1/3)
 <= C_(1/3) F(S_H)^(-1/6)
 = C_(1/3)|det B|^(1/3)J_2(H)^(-1/6).`                            (3.7)

The pair determinant cancels exactly between (3.6) and (3.7):

`||p_Q||_infinity
 <= C_pair C_(1/3) J_2(H)^(-1/6).`                               (3.8)

Using (1.2) and (1.7) gives exactly (3.3).

This is the central advance over r52: no `2 x 2` tetrad of `N_H` is required. The whole overlap-two packet is aggregated as off-diagonal first-order energy **before** any reciprocal is taken.

### Singular physical pair

Assume now `B` is singular but `J_2(H)>0`. Put

`B_e=B+e I_2`,
`A_e=A+e(P_H)`,                                                    (3.9)

where `P_H` is the diagonal projector onto the two physical coordinates in `H`. Choose `e_m -> 0` avoiding the finitely many roots of `det(B_e)`. Define

`N_e=det(B_e)D-C adj(B_e)C^T`,
`J_e=sum_(i!=j)(N_e)_ij^2`.                                       (3.10)

Polynomial continuity gives `J_e -> J_2(H)>0`. The nonsingular proof gives

`||p_(Q_e)||_infinity <= C_J2 J_e^(-1/6).`                        (3.11)

For every sample point, `Q_e-Q=e(X_(h1)^2+X_(h2)^2)->0`, so the laws converge weakly. For every bounded open interval `I`, Portmanteau and (3.11) give

`P(Q in I)
 <= liminf_m P(Q_(e_m) in I)
 <= C_J2 J_2(H)^(-1/6)|I|.`                                      (3.12)

Outer regularity extends this domination to Borel sets, so the limiting law is absolutely continuous with the same essential density cap. No moment bound is used.

The argument proves essential boundedness. Continuity is not asserted from this limiting/fractional-potential route.

## 4. The previous low-tetrad chamber disappears

B04 r52 used a second-exterior receiver and reduced the overlap-two branch to

`J_2(H)>=1/144,
 D_2^disj(N_H)<J_2(H)^2/64.`                                      (4.1)

The new theorem does not use `D_2^disj` at all. Therefore (4.1), including its exact rank-one/tetrad-zero boundary, is now paid uniformly.

The completed fleet03/B20 operator-overlap funnel cited in r52 proves under the full owner hypothesis `s_3(A)>=1` that at least one of

`P_3>=1/4`, `J_2^*>=1/144`, `J_1^*>=1/144`, `J_0>=1/16`           (4.2)

holds. On its overlap-two branch choose `H` with `J_2(H)>=1/144`. The new theorem gives the explicit full-ambient bound

`boxed:
 ||p_Q||_infinity
 <= C_J2 144^(1/6)
 = 202.05020219487562... .`                                       (4.3)

Thus the global funnel's overlap-two class is closed as a density branch, without a rank-one stability theorem. In the same funnel, the `P_3` and `J_0` exits already have completed receivers. The remaining structurally distinct debt is now the overlap-one class `J_1^*` (plus whatever compatibility work the global assembler requires when combining the already-paid exits).

## 5. Genuinely rotated indefinite tetrad-zero stress test

The new theorem should be tested where r52's numerator two-volume is exactly blind. Take

`B=[[4,1/5],[1/5,-4]],`                                           (5.1)

`C=(1/100)*[[1,2],[2,3],[3,5],[5,7]],`                           (5.2)

`u=(1,2,3,4)^T/10`,
`S=2 I_4+u u^T`,                                                   (5.3)

and define

`D=S+C B^(-1) C^T`,
`A_*=[[B,C^T],[C,D]].`                                            (5.4)

The Schur complement of the first physical pair is exactly `S`. Hence

`det B=-401/25`,
`N_H=det(B)S`.                                                      (5.5)

For disjoint row/column pairs the relevant entries of `N_H` are proportional to `u_i u_j`; therefore every disjoint `2 x 2` tetrad determinant vanishes:

`boxed: D_2^disj(N_H)=0.`                                         (5.6)

Nevertheless

`J_2(H)
 =det(B)^2[(sum_i u_i^2)^2-sum_i u_i^4]
 =(401/25)^2*(273/5000)
 =43898673/3125000
 =14.04757536.`                                                     (5.7)

The new theorem therefore gives, for every admissible independent cap-one product law,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=56.81530105405861... .`                                        (5.8)

This is exactly the extreme `theta_H=0` face left unpaid by r52.

The matrix is genuinely rotated and indefinite. Every entry is nonzero. To verify the target condition without relying on a floating-point eigensolver, compare with

`A_0=diag(B,S).`                                                    (5.9)

The two eigenvalues of `B` are `+-sqrt(401)/5`, while `S` has eigenvalues `2,2,2,23/10`. Moreover

`||C||_op <= ||C||_F=sqrt(126)/100`,
`||B^(-1)||_op=5/sqrt(401)`.                                      (5.10)

Thus

`||A_*-A_0||_op
 <= sqrt(126)/100 + (126/10000)*(5/sqrt(401))
 <0.116.`                                                          (5.11)

By Weyl, every eigenvalue of `A_*` has absolute value greater than `2-0.116=1.884>1`; in particular the exact target hypothesis holds, with both signs. For density/nonzero-entry checking, the smallest raw off-diagonal term in `u u^T` is `1/50=0.02`, whereas every correction entry obeys

`|(CB^(-1)C^T)_ij|
 <= (74/10000)*(5/sqrt(401))<0.00185,`                            (5.12)

so the residual off-diagonals cannot cancel to zero. The cross entries in `C` and both entries of the physical pair are visibly nonzero.

A redundant numerical check gives

`spec(A_*) approximately
 {-4.0063306060, 1.9999872953, 1.9999983603,
   2.0000000000, 2.2978443729, 4.0074482085}.`                    (5.13)

This numerical spectrum is only a check; (5.10)-(5.11) are the rigorous spectral certificate.

## 6. Designated fleet04/B04 result applied

The newest completed designated partner remains fleet04/B04 r2:

`yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B04/20260924T001353Z-fleet04-B04-QFORM-r2/REPORT.md`.

On its high-fourth-volume carrier branch, failure of the anchored entropy gate gives a literal physical row pair with canonical fourth-volume pair mass

`eta_ab>2/75.`                                                      (6.1)

Apply the completed B04 pair-anchored fourth-volume promotion theorem

`QFORM-PAIR-ANCHORED-E4-PROMOTION-v1`

from

`yspennstate/math-open-problems@0d074396abdd021a817f0b8dc104b826f2d7154d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260924T041814Z-fleet03-B04-QFORM-auto11-r48/REPORT.md`.

Since `H_ab=eta_ab E_4(M)`, its bound gives the actual inequality

`boxed:
 ||p_Q||_infinity
 < 4*75^(1/8) E_4(M)^(-1/8)
 =6.861872579851902... E_4(M)^(-1/8).`                             (6.2)

That partner branch has a continuous `C_0` density. This is equation-level use of the newest completed designated partner result; no newer fleet04/B04 handoff was present at final partner refresh.

## 7. What changed and what remains

The r52 proposed next step was a stability theorem converting low tetrad volume into kernel-star/ridge structure. That mechanism is no longer needed for the overlap-two branch: the one-third Riesz estimate spends the raw off-diagonal Schur-numerator energy directly, including the exact tetrad-zero face.

The new first B04 structural debt is therefore

`QFORM-OVERLAP1-ZEROPIVOT-OR-E2-AGGREGATE-v1`:
from the surviving `J_1^*>=1/144` class of the global third-exterior overlap funnel, aggregate the one-anchor Schur second-exterior packet before any reciprocal scalar pivot is paid, and prove either a target-scale square-anchor currency already covered by the completed one-anchor/E2 receivers or a zero/near-zero-pivot product-preserving exit through the existing zero-pivot, hyperbola, star, ridge, or square-bank mechanisms.

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN** separately.
