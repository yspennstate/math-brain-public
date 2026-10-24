SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-23T06:13:45Z.
attacking: the first unresolved B19 rank-two-cross near-range branch, by paying a quantitative off-diagonal transverse action through an integrated L^3 bilinear receiver and reducing every survivor to an actual near-kernel source vector.

# account03/B20 r27 — null-transverse bilinear receiver and near-kernel reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Proof closure and keeper  
**Classification:** `NEW SUPPORTING THEOREM / FIRST B19 NEAR-RANGE SUB-IMPLICATION CLOSED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository reads/writes are not native receiver-memory ingestion.  
**Continuity:** proved on the new paid branch below; not proved for the unrestricted target.

## 1. Fresh source boundary and the exact debt attacked

Fresh source control at run start was `yspennstate/math-research-brain@720bec1039353e54a6929d9426fff74a4c893c62`, OWNER CONTROL revision `2026-09-22.15`, QFORM only.

The immediate proof-assembly source is account03/B19 r26:

`yspennstate/math-open-problems@82773d6d0339c8867b76c777216b6c564939f2ae`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T043056Z-account03-B19-QFORM-r26/REPORT.md`.

Its theorem `QFORM-RANK2-CROSS-TRANSVERSE-3D-CURVATURE-v1` treats two disjoint original-product banks `U,V` when the physical cross block `C` has exact rank two, all `U`-side self curvature lies in a three-dimensional physical projection `E` containing `range(C)`, and the scalar transverse Rayleigh coefficient `lambda` is nonzero. If `s1>=s2>0` are the two nonzero singular values of `C`, then

`||p_Q||_infinity < 12.01 |lambda|^(-1/4) (s1 s2)^(-3/8)`.       (1.1)

In its exact-rank-three compound-energy application,

`s1 s2 >= rho := sqrt(29/3072) = 0.0971601984...`,                 (1.2)

so `|lambda|>=1/64` is already paid by `<82`. The stated first remaining implication is the near-range / near-null transverse branch.

This report closes the complementary **off-diagonal transverse-action** subbranch. It does not assume pointwise quadratic phase decay and does not rotate the random coordinates into independent spectral coordinates.

The designated partner actually applied below is account04/B20 r4:

`yspennstate/math-open-problems@f97aa31585b7b547a116d4580f898576af4e0842`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T011956Z-account04-B20-QFORM-r4/REPORT.md`.

Its `QFORM-PARTITIONED-NEAR-NULL-HYBRID-v1` is used at equation level in Section 8.

## 2. Setup

Let `U` and `V` be disjoint banks of original independent real variables, every one-dimensional density bounded by one. Consider

`Q = U^T B U + 2 U^T C V + V^T D V + ell_U^T U + ell_V^T V`,      (2.1)

where `B,D` are real symmetric, `C` has exact rank two, and its two nonzero singular values are

`s1>=s2>0`.                                                         (2.2)

Assume there is a three-dimensional physical subspace `E` of the `U` coordinate space such that

`range(C) subset E`, `range(B) subset E`.                           (2.3)

Let `P` have two orthonormal columns spanning `range(C)`, let `r` be the unit vector spanning

`E intersect range(C)^perp`,                                       (2.4)

and choose a thin SVD

`C = P Sigma R^T`, `Sigma=diag(s1,s2)`,                             (2.5)

with `R` having two orthonormal columns in the physical `V` space. Put

`z=P^T U in R^2`, `y=r^T U`, `w=R^T V`.                            (2.6)

Because `B` is symmetric and has range in `E`, its `E`-matrix is

`[ H   d ]`
`[d^T lambda]`,                                                     (2.7)

for a symmetric `2x2` matrix `H`, a vector `d in R^2`, and

`lambda=r^T B r`.                                                   (2.8)

The new theorem treats `lambda=0` and `d!=0`. An affine term on the `U` side is allowed provided it lies in `E`; the `V`-side affine term is arbitrary. This is exactly the same affine scope as the B19 three-dimensional source receiver, and no larger scope is silently claimed.

## 3. Product-projection caps used

I use the source-valid Livshyts--Paouris--Pivovarov product-marginal estimate already used by B19: if `TX` is a rank-`k` linear image of an independent cap-one product source, then

`||p_(TX)||_infinity <= 2^(k/2)/sqrt(det(TT^T))`.                  (3.1)

Consequently the joint density `p(z,y)` of the orthogonal three-dimensional projection `(P^TU,r^TU)` satisfies

`||p||_infinity <= K3 := 2 sqrt(2)`,                               (3.2)

its `z` marginal `m(z)=int p(z,y)dy` satisfies

`||m||_infinity <= K2 := 2`,                                       (3.3)

and any scalar linear functional `d^Tz+c` has density cap

`L_d <= sqrt(2)/||d||_2`.                                          (3.4)

No independence of `(z,y)` is asserted.

On the `V` side, integrate all coordinates orthogonal to `range(R)` into the usual oscillatory amplitude `b_t(w)`. Its modulus is bounded by the positive two-dimensional marginal density of `R^TV`, hence

`||b_t||_2 <= sqrt(2)`                                              (3.5)

for every real `t`, independently of the signature and size of `D`.

## 4. A negative-moment lemma for a scalar product projection

### Lemma 4.1

If a real random variable `T` has probability density `h` with `0<=h<=L`, then

`E |T-c|^(-2/3) <= 6*2^(-1/3) L^(2/3)`                            (4.1)

for every `c in R`.

### Proof

The kernel `|x|^(-2/3)` is symmetric decreasing. Under the constraints `0<=h<=L`, `int h=1`, its integral is maximized by the centered bathtub density `L 1_{[-1/(2L),1/(2L)]}`. Thus

`int |x|^(-2/3)h(x)dx
 <=2L int_0^(1/(2L)) x^(-2/3)dx
 =6*2^(-1/3)L^(2/3)`.                                              (4.2)

Translation gives the stated form. QED.

Applying (4.1) with (3.4) gives the especially clean estimate

`E |d^T Z+c|^(-2/3) <= 6 ||d||^(-2/3)`.                            (4.3)

## 5. Hilbert-valued L^3 estimate in the null-transverse case

Assume now

`lambda=0`, `d!=0`.                                                 (5.1)

The `U`-side phase is

`z^T H z + 2 y d^T z + affine`.                                    (5.2)

If the `y`-affine coefficient is `2c`, define

`q(z)=d^Tz+c`.                                                      (5.3)

Up to a unimodular factor depending on `z`, the source amplitude is

`F_t(z)=int_R p(z,y) exp(2it y q(z))dy`.                            (5.4)

For fixed `z` with `q(z)!=0`, the unnormalized one-dimensional Hausdorff--Young inequality `L^(3/2)->L^3` gives

`||F_.(z)||_(L_t^3)
 <=(2pi)^(1/3)(2|q(z)|)^(-1/3)||p(z,.)||_(3/2)`.                   (5.5)

Because `p<=K3` and its slice mass is `m(z)`,

`||p(z,.)||_(3/2) <= K3^(1/3)m(z)^(2/3)`.                          (5.6)

For `3>=2`, Minkowski's integral inequality yields

`|| ||F_t||_(L_z^2) ||_(L_t^3)
 <= [int ||F_.(z)||_(L_t^3)^2 dz]^(1/2)`.                          (5.7)

Using (5.5)--(5.6), `m^(4/3)<=K2^(1/3)m`, and then (4.3),

`|| ||F_t||_2 ||_3^2
 <=(2pi)^(2/3)2^(-2/3)K3^(2/3)K2^(1/3)
    E|q(Z)|^(-2/3)`
 <=6(4pi)^(2/3)||d||^(-2/3)`.                                      (5.8)

Therefore

`boxed:
 || ||F_t||_2 ||_(L_t^3)
 <= N0 ||d||^(-1/3),
 N0=sqrt(6)(4pi)^(1/3)=5.6948057280... .`                           (5.9)

This is an integrated estimate. It does not imply or use any forbidden law-uniform pointwise van-der-Corput decay.

The set `q(z)=0` is a line and has two-dimensional Lebesgue measure zero because `d!=0`; it does not affect (5.7).

## 6. Rank-two bilinear Plancherel and Fourier inversion

The characteristic function can be written

`phi_Q(t)=int_R2 int_R2 F_t(z)b_t(w) exp(2it z^T Sigma w) dzdw`.    (6.1)

Put

`beta=sqrt(s1 s2)`.                                                 (6.2)

Two-dimensional Plancherel in `w`, followed by the change `xi=2t Sigma z`, gives for `t!=0`

`|phi_Q(t)|
 <= pi/(|t| beta) ||F_t||_2 ||b_t||_2
 <= pi sqrt(2)/( |t| beta) ||F_t||_2`.                             (6.3)

For any `T>0`, use `|phi_Q|<=1` on `|t|<=T`; on the tail apply Holder with exponents `3` and `3/2`, together with (5.9). Since

`|| |t|^(-1)1_(|t|>T)||_(3/2)=4^(2/3)T^(-1/3)`,                   (6.4)

we obtain

`int_R |phi_Q(t)|dt
 <=2T + A0 ||d||^(-1/3) beta^(-1) T^(-1/3)`,                      (6.5)

where

`A0=pi sqrt(2) 4^(2/3) N0
   =63.7554200285... .`                                             (6.6)

The optimizer is

`T=[A0 ||d||^(-1/3) beta^(-1)/6]^(3/4)`.                           (6.7)

At this value the tail term is `6T`, so the right side of (6.5) is `8T`. Fourier inversion then gives

`||p_Q||_infinity
 <= C0 ||d||^(-1/4) beta^(-3/4)
 = C0 ||d||^(-1/4)(s1s2)^(-3/8)`,                                 (6.8)

with

`C0=(4/pi)(A0/6)^(3/4)
   =7.4934965950... <7.5`.                                          (6.9)

Moreover `phi_Q in L^1`, so the density has a continuous representative vanishing at infinity.

This proves the main theorem.

### Theorem 6.1 — `QFORM-RANK2-CROSS-NULL-TRANSVERSE-L3-v1`

Under the hypotheses of Section 2, if

`r^TBr=0` and `d=P^TBr!=0`,                                        (6.10)

then the full two-bank quadratic form has a continuous density and

`boxed:
 ||p_Q||_infinity
 < 7.5 ||P^TBr||^(-1/4)(s1s2)^(-3/8).`                            (6.11)

Arbitrary same-bank curvature `H,D` is retained. The proof aggregates original product banks before taking absolute values; it never treats projected coordinates as independent.

## 7. Actual closure of the B19 compound-energy off-diagonal branch

Return to the exact-rank-three B19 r26 packet. There

`s1s2 >= rho=sqrt(29/3072)`.                                       (7.1)

B19 already pays

`|lambda|=|r^TBr| >=1/64`                                          (7.2)

by `<82` using (1.1). In the exact-null endpoint `lambda=0`, Theorem 6.1 pays every state with

`||d||=||P^TBr|| >=1/64`                                           (7.3)

by

`||p_Q||_infinity
 < C0*64^(1/4)*rho^(-3/8)
 =50.8067436150... <51`.                                           (7.4)

More generally, the analytic receiver (6.11) is available at any nonzero `d`; (7.4) records the fixed-threshold branch needed by the current proof tree.

Thus the previous vague `small transverse self curvature` obstruction sharpens, at the fixed `1/64` scale, to an actual **near-kernel** statement. A survivor after the B19 scalar-transverse payment and the present off-diagonal payment must obey

`|r^TBr|<1/64`, `||P^TBr||<1/64`,                                  (7.5)

hence

`boxed: ||Br|| < sqrt(2)/64 =0.0220970869... .`                    (7.6)

This is strictly stronger than small transverse Rayleigh curvature: the entire action of the source self matrix on the physical direction transverse to the rank-two cross range is now small.

For the **exact** null endpoint `r^TBr=0`, note also that in the full exact-rank-three setting of B19, `range(B)=E`; hence `B|_E` is invertible and `d=0` is impossible. Therefore Theorem 6.1 covers every exact-null state, although its universal fixed-constant payment requires the quantitative threshold (7.3). States with `0<||d||<1/64` are retained honestly in the near-kernel residue.

## 8. Required account04/B20 application

Account04/B20 r4 proves `QFORM-PARTITIONED-NEAR-NULL-HYBRID-v1`: in its exact-rank-three Parseval-frame scope, if there is a leverage row `c>=1/2`, every other physical row lies either in the longitudinal spectral direction or in its transverse plane, and the spectral Rayleigh pivot obeys `|a|<=1/2`, then

`||p_Q||_infinity
 <=103680^(1/3) 2^(7/6) |det Lambda|^(-1/3)`.                      (8.1)

In the present exact-rank-three target, the three nonzero eigenvalues satisfy `|lambda_k|>=1`, so

`|det Lambda|>=1`.                                                  (8.2)

Therefore every near-kernel survivor that lies in the partner theorem's **stated partitioned scope** is immediately paid by the actual inequality

`boxed:
 ||p_Q||_infinity
 <=103680^(1/3)2^(7/6)
 =105.4629684327... <105.463.`                                     (8.3)

No claim is made that the partition hypothesis follows from (7.6). Equation (8.3) is used only on the genuine overlap. Consequently a still-unpaid near-kernel state must either have no leverage-`>=1/2` row available for that theorem, or contain genuinely mixed residual rows that violate its longitudinal/transverse partition. This identifies the correct remaining geometry rather than extending the partner result by analogy.

## 9. What remains

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains open.

The first B19 rank-two-cross debt is now narrowed from `small transverse Rayleigh coefficient` to

`QFORM-RANK2-CROSS-NEAR-KERNEL-MIXED-ROW-PAYMENT-v1`:

- retain the compound-energy resource `s1s2>=sqrt(29/3072)`;
- retain the quantitative near-kernel vector `||Br||<sqrt(2)/64`;
- outside account04/B20's already-paid partitioned near-null overlap, exploit the genuinely mixed rows to force a ridge/grouped-coordinate/extra-bank payment.

This is the next product-preserving implication. The new theorem is also reusable independently whenever an exact null transverse Rayleigh coefficient occurs: the cross-bank bilinear phase supplies the missing integrated `L^3` smoothing through the negative `2/3` moment of an actual one-dimensional product projection.

Arbitrary-extra-spectrum descent remains a separate global debt exactly as in B19 r26.

## 10. Scope / correction audit

The proof does not use any of the live-refuted interfaces: no law-uniform pointwise quadratic decay, no arbitrary-joint 3D coarea lemma, no conditional projection-density cap, no independence after rotation, no fiber supremum, no one-good-minor extraction, and no Monte Carlo extremality claim.

The only projected-density inputs are unconditional linear images of the original independent product law, in the exact LPP scope. All randomized or spectral objects are deterministic matrix coordinates; the probability law is never rotated and then declared independent.

Exact numerical constants are reproduced by `CHECK.py` in this immutable run folder. Its terminal assertion is `QFORM_B20_R27_NULL_TRANSVERSE_CHECK_PASS`.
