SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T23:20:13Z.
attacking: QFORM-ZEROPIVOT-CHIRP-LOGGLUE-v1 — derive a delta-uniform critical mixed-norm t^-1 estimate for the exact account02/B02 chirp kernel and combine it with the nonzero-tail Strichartz tail so the near-rank-one endpoint loss is only logarithmic rather than algebraic.

# account01/B02 r40 — delta-uniform critical mixed norm and logarithmic endpoint glue

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T232013Z-account01-B02-qform-auto11-r40`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN-NOT-REFUTED**

The exact target remains unchanged: independent ORIGINAL real coordinates with one-dimensional densities bounded by one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No moment, support, log-concavity, Gaussian, connected-support, diagonal-basis, or post-rotation independence assumption is introduced. Continuity is asserted only on branches where an actual unweighted `L1_t` characteristic-function estimate is proved.

## 1. Fresh source and correction state


The live correction package was reread. In particular this report does not use: law-uniform scalar pointwise Fresnel decay; post-rotation independence; arbitrary-joint coarea; conditional-density-as-independence; one-good-minor extraction from aggregate mass; deletion of a nonzero coefficient tail on unbounded product inputs; or the refuted one-heavy-row same-square absorption shortcut.

Designated partner result used at equation level:

- `yspennstate/math-open-problems@612be1591c1aa5edaeb29bb6eceec7963ddbef55`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T212459Z-account02-B02-qform-auto11/EARLY.md`.

The partner derives the exact nonzero-tail operator

`(T_delta f)(y)=int k_t(alpha y+beta z) exp(i 2t delta yz) f(z) dz`,       (1.1)

with `k_t(s)=hat g_t(2ts)` and `|g_t|<=f_H`, where the physical hub density satisfies `0<=f_H<=1`, `int f_H=1`. It also retains the transverse bilinear operator

`(S_sigma f)(y2)=int exp(i2t sigma y2 z2)f(z2)dz2`,                      (1.2)

whose exact `L2->L2` norm is `sqrt(pi/(|t sigma|))`. For `delta!=0`, the partner's chirp representation is exact and its pointwise `L2->L2` norm can be as large as `sqrt(pi/(|t delta|))`; this is the critical `|t|^-1` tensor barrier when one first takes the worst pointwise law.

The immediately preceding account01/B02 r39 report proves the separate integrated estimate, via one-dimensional `(4,infinity)` Strichartz,

`int_T^infinity |phi_Q(t)|dt <= B T^(-1/4)`,                            (1.3)

for positive `T`, with

`B=sqrt(M_Y M_Z) pi 3^(3/4) C_Str
    |delta|^(-1/4)|sigma|^(-1/2)|alpha beta|^(-1/4)`,                  (1.4)

whenever `delta!=0`. Here `M_Y,M_Z` are the two bank joint-density caps and `C_Str` is the universal constant in

`|| sup_eta |int g(h)e^{-i(s h^2+eta h)}dh| ||_(L4_s)
 <= C_Str ||g||_2`.                                                     (1.5)

The purpose of this run is to replace the crude bound `|phi|<=1` on the entire pre-tail interval by a delta-INDEPENDENT critical estimate.

## 2. A delta-uniform L^(4/3)->L^4 chirp operator estimate

### Lemma 2.1
For every real `delta` (including zero), every nonzero `alpha,beta,t`, and every hub amplitude `g_t` with `||g_t||_2<=1`, the operator (1.1) obeys

`boxed:
 ||T_delta||_(L^(4/3)->L^4)
 <= sqrt(pi) |alpha beta|^(-1/4)|t|^(-1/2).}`                         (2.1)

### Proof
Put `x=alpha y`, `w=-beta z` and

`mu=2t delta/(alpha beta)`.

The identity

`-mu xw=-(mu/2)x^2-(mu/2)w^2+(mu/2)(x-w)^2`                           (2.2)

shows that, after multiplying input and output by modulus-one chirps, the scaled operator is convolution by

`h(s)=k_t(s) exp(i mu s^2/2)`.                                        (2.3)

The chirp does not change the `L2` norm. Young's convolution inequality `L2 * L^(4/3) -> L4`, together with the input/output Jacobians, therefore gives

`||T_delta||_(4/3->4)
 <= |alpha beta|^(-1/4)||k_t||_2`.                                    (2.4)

With the angular Fourier convention and `k_t(s)=hat g_t(2ts)`, Plancherel gives exactly

`||k_t||_2^2
 = (pi/|t|)||g_t||_2^2
 <= pi/|t|`.                                                           (2.5)

Substitution in (2.4) proves (2.1). Notice that no estimate deteriorates as `delta->0`; in fact delta appears only in a unit-modulus chirp. QED.

This estimate is deliberately weaker in time than the exact `delta=0` `L2->L2` estimate, but it is stable through the singular algebraic endpoint.

## 3. Mixed norms supplied by an actual product-projection bank

The tensor argument needs a bank norm compatible with (2.1) and the `L2->L2` transverse operator. The following elementary bound is the key.

### Lemma 3.1
Let `rho(x,u)` be a two-dimensional probability density with

`0<=rho<=M`,

and suppose its `u`-marginal

`m(u)=int rho(x,u)dx`

satisfies `m<=m_*`. If a complex amplitude `a` satisfies `|a|<=rho`, then

`boxed:
 ||a||_(L^(4/3)_x(L2_u))
 <= ||a||_(L2_u(L^(4/3)_x))
 <= (M m_*)^(1/4).}`                                                   (3.1)

### Proof
Minkowski gives the first inequality because `4/3<=2`. For fixed `u`,

`int |a(x,u)|^(4/3)dx
 <= M^(1/3) m(u)`.                                                       (3.2)

Hence

`||a(.,u)||_(4/3)
 <= M^(1/4)m(u)^(3/4)`.                                                (3.3)

Squaring and integrating in `u`,

`||a||_(L2_u(L^(4/3)_x))^2
 <= M^(1/2) int m(u)^(3/2)du
 <= M^(1/2)m_*^(1/2) int m(u)du
 =M^(1/2)m_*^(1/2)`.                                                   (3.4)

Taking square roots proves (3.1). QED.

For the two-dimensional orthogonal bank projections used in the designated partner's rank-one/shared-hub reduction, the Livshyts--Paouris--Pivovarov projection theorem supplies `M_Y,M_Z<=2`. The determinant-one shears used to put a rank-one crossing into canonical form preserve the two-dimensional Lebesgue density cap. Their transverse coordinates are nonzero linear functionals of the original product vector with Euclidean norm at least one, so the one-dimensional projection theorem gives

`m_Y,m_Z<=sqrt(2)`.                                                     (3.5)

No independence between the two coordinates inside either projected bank is asserted or needed.

## 4. Delta-uniform critical characteristic-function estimate

### Theorem 4.1 — `QFORM-ZEROPIVOT-CHIRP-CRITICAL-MIXEDNORM-v1`
Consider the same exact three-bank zero-hub-quadratic kernel as in r39:

`2H(alpha Y1+beta Z1)+2 delta Y1Z1+2 sigma Y2Z2`,                      (4.1)

with arbitrary measurable real same-bank phases, independent banks `H,Y,Z`, scalar hub density at most one, two-dimensional bank density caps `M_Y,M_Z`, and transverse marginal caps `m_Y,m_Z`. For every real `delta`, and every nonzero `alpha,beta,sigma`,

`boxed:
 |phi_Q(t)|
 <= min{1,C0/|t|},}`                                                   (4.2)

where

`boxed:
 C0=pi (M_Y M_Z m_Y m_Z)^(1/4)
       |alpha beta|^(-1/4)|sigma|^(-1/2).}`                            (4.3)

In particular, on the product-projection/sheared banks of (3.5),

`boxed:
 C0<=pi 2^(3/4)|alpha beta|^(-1/4)|sigma|^(-1/2).}`                    (4.4)

### Proof
Absorb all same-bank phases into complex amplitudes `a_t(y)` and `b_t(z)`. Their moduli are bounded by the corresponding bank densities, so Lemma 3.1 applies.

Apply `S_sigma` first in the second coordinate. By Plancherel,

`||S_sigma||_(2->2)=sqrt(pi/(|t sigma|)).`                             (4.5)

Now apply `T_delta` in the first coordinate. The proof of Lemma 2.1 is scalar convolution by an `L2` kernel after modulus-one multipliers, hence the same Young inequality is valid for Hilbert-valued functions. Therefore

`||T_delta tensor S_sigma b_t||_(L4_(y1)(L2_(y2)))
 <= [sqrt(pi)|alpha beta|^(-1/4)|t|^(-1/2)]
    [sqrt(pi)|t sigma|^(-1/2)]
    ||b_t||_(L^(4/3)_(z1)(L2_(z2))).`                                (4.6)

Pairing with `a_t` uses the dual space `L^(4/3)_(y1)(L2_(y2))`. Lemma 3.1 on both banks gives

`|phi_Q(t)|
 <= pi (M_YM_Zm_Ym_Z)^(1/4)
    |alpha beta|^(-1/4)|sigma|^(-1/2)|t|^(-1).`                       (4.7)

Together with `|phi_Q(t)|<=1`, this is (4.2). QED.

The point is structural: unlike the partner's law-uniform `L2->L2` chirp norm, (4.2) is completely uniform in `delta`. It spends a genuine transverse one-dimensional marginal cap inherited from the original product law.

## 5. Logarithmic glue with the r39 Strichartz tail

For `delta!=0`, combine (4.2) with (1.3). Define the dimensionless ratio

`R=B C0^(-5/4)`.                                                       (5.1)

For any `U>=1`, take `T=C0 U`. On the positive half-line,

`int_0^T |phi_Q(t)|dt
 <= C0[1+log U]`,                                                      (5.2)

while (1.3) gives

`int_T^infinity |phi_Q(t)|dt
 <= B(C0U)^(-1/4)
 = C0 R U^(-1/4)`.                                                     (5.3)

If `R>=4`, optimize at `U=(R/4)^4`; if `R<4`, take `U=1`. Using `|phi(-t)|=|phi(t)|`, we obtain:

### Theorem 5.1 — `QFORM-ZEROPIVOT-CHIRP-LOGGLUE-v1`
For `delta!=0`, under the hypotheses of Theorem 4.1 and the r39 Strichartz tail,

`boxed:
 int_R |phi_Q(t)|dt
 <= 10 C0 + 8 C0 log_+(R/4),}`                                        (5.4)

where `C0` is (4.3), `B` is (1.4), and `R=B C0^(-5/4)`.

Consequently this branch has a continuous density vanishing at infinity, with

`boxed:
 ||p_Q||_infinity
 <= [5C0+4C0 log_+(R/4)]/pi.}`                                        (5.5)

The singular dependence on the near-rank-one coefficient has therefore improved from the r39 algebraic `|delta|^(-1/5)` loss to a logarithm. Explicitly, in the product-projection bank case (3.5),

`R <= 2^(1/16) 3^(3/4) pi^(-1/4) C_Str
      |delta|^(-1/4)|alpha beta|^(1/16)|sigma|^(1/8).`                 (5.6)

Thus the only remaining failure of uniform endpoint glue in this exact mechanism is logarithmic as `delta->0`.

At `delta=0`, the designated partner's exact-rank-one tensor theorem gives the stronger `|t|^(-3/2)` envelope and finite `L1_t`; (5.4) is not used there. The unresolved point is a quantitative bridge whose constant is uniform while crossing `delta=0`.

## 6. Designated partner applied to the live heavy-hub inequality

The designated account02/B02 source records the current three-bank heavy-hub packet

`D_h >= (8/3125) V1`.                                                  (6.1)

Assume, exactly as in the r39 application and without claiming it automatically, that the realized singular-core coordinates obey

`(alpha beta sigma)^2 >= theta D_h`,                                  (6.2)

for an explicit `theta>0`. From (4.4), (6.1), and (6.2),

`C0
 <= pi 2^(3/4) theta^(-1/8)(8/3125)^(-1/8)
    V1^(-1/8)|sigma|^(-1/4).`                                         (6.3)

Numerically the coefficient before `theta^(-1/8)V1^(-1/8)|sigma|^(-1/4)` is

`11.140184249677194...`.                                               (6.4)

Hence on the explicit transverse-core subbranch

`|sigma| >= kappa V1^(1/6)`,                                          (6.5)

the delta-uniform critical constant is scale-correct:

`boxed:
 C0 <= 11.140185 theta^(-1/8) kappa^(-1/4) V1^(-1/6).}`                (6.6)

Substitution into (5.4) gives an actual live integrated-Fourier exit of the form

`boxed:
 int |phi_Q|
 <= 11.140185 theta^(-1/8)kappa^(-1/4)V1^(-1/6)
    [10+8 log_+(R/4)],}`                                               (6.7)

with `R` given explicitly by (5.6). This is an equation-level use of the completed partner packet, not citation-only reuse.

For comparison, at the exact endpoint `delta=0`, the partner's exact rank-one tensor theorem and (6.1) give

`int |phi_Q|
 <= 6pi 2^(2/3)(3125/8)^(1/6)V1^(-1/6)
 <80.900 V1^(-1/6)`,                                                   (6.8)

and

`||p_Q||_infinity<12.876 V1^(-1/6)`.                                  (6.9)

Thus both sides of the endpoint are paid individually; what remains is removal of the logarithmic mismatch for arbitrarily small nonzero `delta`.

## 7. Exact remaining debt

The first unpaid local implication is now

`QFORM-ZEROPIVOT-CHIRP-UNIFORM-LOG-REMOVAL-v1`:

> exploit additional original-coordinate product provenance or the quantitative singular-core identities to remove the factor `log_+ R` in (5.4), equivalently show that the very-small-`delta` regime supplies another physical-volume or direct-density receiver before `R` can diverge.

A pointwise `L2->L2` interpolation is still ruled out by the partner's phase-aligned construction. A perturbative estimate `T_delta-T_0=O(delta)` is also unavailable without input moments because the factor `yz` is unbounded. The new mixed-norm estimate avoids that false step entirely.

No exact-target counterexample to a universal `int |phi_Q|` bound was found. Therefore target-wide Fourier-L1 remains `OPEN_NOT_REFUTED`. The full bounded-density conjecture remains OPEN. Full-target continuity remains OPEN; continuity is proved for the exact kernel branches with actual `L1_t` estimates above.

## 8. Integrity / scope checks

- No general rotation of the independent input vector is used.
- The bank rotations/shears occur only after pushing an ORIGINAL-coordinate bank to a low-dimensional joint law; no independence inside the bank is asserted.
- The transverse marginal cap in Lemma 3.1 is explicit and is verified from an actual one-dimensional product projection in the partner canonicalization.
- No moment is used; the proof is stable for fragmented/unbounded supports.
- The nonzero tail `delta` is retained exactly as a unitary chirp in Lemma 2.1.
- No fixed good physical minor is inferred from aggregate exterior mass.
- (6.2) and (6.5) are explicit subbranch hypotheses, not consequences silently attributed to the global spectral condition.
- The result is homogeneous: `C0` has inverse coefficient scale one, while `R` is dimensionless.

## 9. Sources


Designated partner: `yspennstate/math-open-problems@612be1591c1aa5edaeb29bb6eceec7963ddbef55`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T212459Z-account02-B02-qform-auto11/EARLY.md`.

Preceding integrated Strichartz source: account01/B02 r39, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260923T222129Z-account01-B02-qform-auto11-r39/REPORT.md`, read-back blob `72520e4eabbc2b62dc722f630f19b99031c93d34`.

Brain status remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval and actual equation-level receiver use occurred, but native learned-memory ingestion was not verified.
