SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T11:11:38Z.
attacking: a rank-two cross / one-dimensional kernel-curvature frequency-averaged compiler, using account02/B01's scalar L4 square-phase theorem and two-dimensional original-coordinate Plancherel.

# Rank-two cross plus kernel curvature: an L4/L1 compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T111138Z-account01-B01-qform-auto11`  
Role: account01/B01, Oscillatory replacement  
Status: **PROVED SUPPORTING TARGET-LEVEL ANALYTIC THEOREM / FULL QFORM OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction boundary

The unrestricted conjecture remains OPEN: for every dimension, arbitrary independent real input coordinates with probability densities bounded by one, and every real symmetric matrix A with at least three eigenvalues of modulus at least one, prove one universal essential-supremum bound for the density of X^T A X, or give a valid counterexample. No moments, support, Gaussianity, log-concavity, connected support, identical laws, or independence after spectral rotation is assumed.

The phase-aligned fragmented-support correction remains fully in force. This report does **not** assert a law-uniform pointwise scalar estimate of the form

`|E exp(it a X^2)| <= C |t|^(-1/2)`.

The replacement is frequency-averaged: one ORIGINAL scalar coordinate contributes a uniform `L^4(dt)` square-phase budget, while a separate rank-two physical cross packet contributes a `|t|^-1` two-dimensional Plancherel factor. Hölder in frequency makes the product integrable.

Fresh current sources consumed in this run:

* owner/current proof map: math-research-brain main, control revision 2026-09-22.15; newest-Claude continuation and volume-stability handoff;
* newest Claude/Fourier package `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md}`;
* volume-stability package `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/`;
* designated partner account02/B01, bundle tip `yspennstate/math-open-problems@91dbcb0e8b3f6faa4af9629aaaff2f69d385695a`, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T100534Z-account02-B01-qform/REPORT.md`.

The partner result actually used below is its scalar product-preserving L4 square-phase lemma.

## 2. Partner input, extended to subprobability amplitudes

The designated partner proves the following for every cap-one probability density f, every a!=0 and every affine coefficient ell:

`integral_R | integral f(z) exp(it(a z^2+ell z)) dz |^4 dt <= 27 pi/(2|a|).`   (2.1)

The same proof gives the precise subprobability form needed after a triangular shear.

### Lemma 2.1 — subprobability L4 square-phase bound

Let `0<=g<=1` be integrable with mass `m=int g<=1`. Then, uniformly in `ell,c`,

`boxed: integral_R | integral g(z) exp(it(a z^2+ell z+c)) dz |^4 dt
        <= [27 pi/(2|a|)] m^2.`                                      (2.2)

Proof. Complete the square and translate g. If h is the pushforward density of z^2, then h(w)<=w^(-1/2), `int h=m`, and

`int h^(4/3) <= int h(w)w^(-1/6)dw = int |z|^(-1/3)g(z)dz.`

By the one-dimensional bathtub inequality for a cap-one mass-m function,

`int |z|^(-1/3)g(z)dz <= int_(-m/2)^(m/2)|z|^(-1/3)dz
                       =3*2^(-2/3)m^(2/3).`

Hausdorff-Young in the partner convention therefore gives

`int |hat h|^4 <=2pi [3*2^(-2/3)m^(2/3)]^3=(27pi/2)m^2`,

and scaling t by a gives (2.2). QED.

This is the first equation-level application and strengthening of the completed partner result.

## 3. Physical three-row setup

Choose three ORIGINAL physical coordinates `H={1,2,3}` and a disjoint original-coordinate bank J. Condition on all remaining original coordinates W. Write

`U=(X_1,X_2)`, `Z=X_3`, `Y=X_J`.

Let

`B=A[H,H] = [[B_2,d],[d^T,a]]`,                                    (3.1)

where `B_2` is 2x2 and `d in R^2`. Let the H-to-J cross block be

`M=A[H,J] = [K; c^T]`,                                             (3.2)

where `K=A[{1,2},J]` is 2 by |J|. Assume

`rank(M)=rank(K)=2.`                                                (3.3)

Then there is a unique `alpha in R^2` such that

`c^T=alpha^T K.`                                                    (3.4)

Let

`v=(-alpha_1,-alpha_2,1)^T`, `n=v/||v||_2`;                       (3.5)

thus n is the unit vector spanning the left kernel of M:

`M^T n=0.`                                                          (3.6)

Define the physical kernel curvature

`kappa_0 = |n^T B n|.`                                              (3.7)

The new theorem assumes `kappa_0>0`. No assumption is made on the signs or sizes of the other eigenvalues of B, on the J-J block, on W-W or H-W/J-W couplings, or on affine terms induced after conditioning W.

Define the aggregate rank-two cross volume

`V_2(M)=e_2(MM^T)=sigma_1(M)^2 sigma_2(M)^2`,                       (3.8)

where the third singular value is zero because rank(M)=2.

## 4. Exact structural identity under the product-preserving shear

Because of (3.4), the cross phase is

`2 U^T K Y + 2 Z c^T Y = 2 (U+alpha Z)^T K Y.`                     (4.1)

Make the triangular shear

`U'=U+alpha Z`, `Z'=Z`.                                             (4.2)

This has Jacobian one. It is **not** treated as a new independent coordinate system: the original product density is retained exactly as

`m(U'-alpha Z) f_3(Z)`,                                             (4.3)

where `m(u)=f_1(u_1)f_2(u_2)<=1` and `f_3<=1`.

The H-H quadratic part becomes

`U'^T B_2 U' + 2 Z (d-B_2 alpha)^T U' + a_eff Z^2`,               (4.4)

with

`a_eff = a - 2 d^T alpha + alpha^T B_2 alpha = v^T B v.`           (4.5)

Since `n=v/||v||`,

`|a_eff| = ||v||^2 kappa_0.`                                       (4.6)

Also, because row 3 of M equals `alpha_1 row_1(K)+alpha_2 row_2(K)`, Cauchy-Binet on the three row pairs gives

`V_2(M)=det(KK^T)(1+||alpha||^2)=det(KK^T)||v||^2.`                (4.7)

Therefore the key homogeneous currency is exactly invariant:

`boxed: det(KK^T)|a_eff| = V_2(M) kappa_0.`                         (4.8)

No reciprocal physical minor is selected.

## 5. Frequency-averaged amplitude estimate after the shear

Fix the conditioned value w of X_W. All remaining W-dependent terms are affine or constant in `(U',Z,Y)` and are harmless below.

For each fixed `u'`, define

`g_(u')(z)=m(u'-alpha z) f_3(z).`                                   (5.1)

Then `0<=g_(u')<=1`, and its mass

`m_0(u')=int g_(u')(z) dz <=1.`                                    (5.2)

Moreover, by Fubini and the Jacobian-one shear,

`int_R2 m_0(u')du' =1.`                                            (5.3)

After absorbing the U'-only phase into a unimodular multiplier, define

`h_(t,w)(u')=int g_(u')(z) exp(it[a_eff z^2 + ell_w(u') z]) dz
             * exp(it q_w(u')).`                                   (5.4)

By Lemma 2.1,

`int_R |h_(t,w)(u')|^4 dt <= [27pi/(2|a_eff|)] m_0(u')^2.`         (5.5)

Set

`A_w(t)=||h_(t,w)||_(L2(du')).`                                    (5.6)

Use Minkowski on `A_w^2`:

`||A_w||_4^2
 = || int |h_(t,w)(u')|^2 du' ||_(L2(dt))
 <= int ||h_(.,w)(u')||_4^2 du'
 <= [27pi/(2|a_eff|)]^(1/2) int m_0(u')du'.`                        (5.7)

By (5.3),

`boxed: ||A_w||_4 <= [27pi/(2|a_eff|)]^(1/4).`                     (5.8)

Average over W and put `A(t)=E_W A_w(t)`. Minkowski again yields the same bound:

`||A||_4 <= [27pi/(2|a_eff|)]^(1/4).`                              (5.9)

This is the central frequency-averaged replacement. No scalar pointwise decay was invoked.

## 6. Rank-two leaf projection and two-dimensional Plancherel

The untouched J variables are still the original independent product bank. Put

`L=2 K Y in R^2`, `Delta=sigma_1(K)sigma_2(K)=det(KK^T)^(1/2).`    (6.1)

The standard product-projection bound used in the partner report gives

`||p_(KY)||_infinity <=2/Delta`,

hence by two-dimensional scaling

`||p_L||_infinity <=1/(2Delta).`                                   (6.2)

Disintegrate the full arbitrary J-phase over L. Its complex density `eta_(t,w)` satisfies `|eta|<=p_L`, so

`||eta_(t,w)||_2 <=(2Delta)^(-1/2).`                               (6.3)

The remaining cross phase is exactly `exp(it u'.L)`. Cauchy-Schwarz in u' and two-dimensional Plancherel give, for t!=0,

`|phi_w(t)|
 <= ||h_(t,w)||_2 [int |hat eta_(t,w)(t u')|^2du']^(1/2)
 <= sqrt(2) pi Delta^(-1/2)|t|^(-1) A_w(t).`                       (6.4)

Averaging over W,

`|phi_Q(t)| <= min{1, sqrt(2)pi Delta^(-1/2)|t|^(-1) A(t)}.`       (6.5)

## 7. Main theorem and exact constant

For every `T>0`, Hölder with exponents 4 and 4/3 gives

`int_R |phi_Q(t)|dt
 <= 2T + sqrt(2)pi Delta^(-1/2)||A||_4
           [int_(|t|>T)|t|^(-4/3)dt]^(3/4)`
` = 2T + D_0 T^(-1/4),`                                           (7.1)

where

`D_0 = sqrt(2)pi Delta^(-1/2)[27pi/(2|a_eff|)]^(1/4) 6^(3/4).`    (7.2)

The minimum occurs at

`T=(D_0/8)^(4/5)`,                                                  (7.3)

and the minimum value is `10(D_0/8)^(4/5)`. Fourier inversion therefore gives

`||p_Q||_infinity
 <= (5/pi)(D_0/8)^(4/5)
 = (15/4) 12^(1/5) Delta^(-2/5)|a_eff|^(-1/5).`                   (7.4)

Using (4.8):

### Theorem 7.1 — `QFORM-RANK2-CROSS-KERNEL-CURVATURE-L4-v1`

Under (3.1)-(3.8), if rank(A[H,J])=2 and the unit left-kernel vector n satisfies `kappa_0=|n^T A[H,H]n|>0`, then the full ambient quadratic form has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= C_* [ V_2(A[H,J]) * |n^T A[H,H] n| ]^(-1/5),`                 (7.5)

where

`C_*=(15/4)12^(1/5)=6.164069360689596... .`                        (7.6)

All signs, arbitrary same-bank J curvature, outside couplings, and affine terms are retained. The proof uses original-coordinate product structure throughout; the shear is triangular and its induced dependent density is never replaced by an arbitrary joint-density cap.

Scaling check: `V_2` has matrix scale four and `kappa_0` scale one, so the bracket in (7.5) has scale five and the `-1/5` exponent gives the correct density scale `|lambda|^-1` under `A->lambda A`.

## 8. Why this advances the current no-pivot proof map

The current volume-stability theorem at `c2414ef...` pays two substantial cross singular directions plus a collective tail `T2=sum_(j>=3)s_j^2`, but is silent for an exact rank-two cross packet because `T2=0`. Theorem 7.1 pays exactly such a packet when its one-dimensional physical left-kernel retains curvature.

Quantitatively, if

`V_2(A[H,J]) * |n^T A[H,H]n| >= eta^5`,                            (8.1)

then

`boxed: ||p_Q||_infinity <= 6.165/eta`,                            (8.2)

with a continuous C0 density, even when the J-J block is fully dense and nonseparable.

Thus the rank-two branch can now be separated into:

1. cross rank >=3: paid by the existing three-hub projected-slope / volume routes when their quantitative volume is available;
2. cross rank exactly 2 with nonzero kernel curvature: paid by Theorem 7.1;
3. cross rank exactly 2 with zero/near-zero kernel curvature: the remaining genuinely null/near-null branch, to be joined to the exact-null-coloop and near-null workers;
4. cross rank <=1: lower-rank hub/grouped branches remain.

The newest Claude D5 theorem is complementary rather than duplicative: it pays any disjoint cross block with nontrivial fifth volume, whereas every exact-rank-two block in Theorem 7.1 has `e_5=0` identically. The two mechanisms therefore cover disjoint structural currencies.

## 9. Actual designated-partner application to its strict-N3 family

The designated partner constructs, for small epsilon and large Hadamard order N,

`K=sigma [v1^T;v2^T]`, `sigma=epsilon^(-1/2)`,                    (9.1)

with a dense arbitrary leaf self-curvature retained and two source-disjoint scalar square coordinates of coefficients `epsilon` and `-epsilon`. Its full theorem uses both squares to obtain `||p_Q||_infinity<=9/2`.

Apply Theorem 7.1 instead to the physical triple

`H=(U1,U2,Z1)`                                                     (9.2)

and condition on `Z2` together with the ordinary outside variables. Then

`A[H,J]=[K;0]`, `rank=2`, `n=e_3`,

`V_2(A[H,J])=sigma^4=epsilon^(-2)`,

`|n^T A[H,H]n|=epsilon.`                                          (9.3)

Therefore

`boxed:
 ||p_Q||_infinity
 <= C_* epsilon^(1/5)
 <= C_*=6.1640693607`                                              (9.4)

for every `0<epsilon<=1`, uniformly in N and in every admissible cap-one product law. This is an actual equation-level use of the partner construction and its L4 lemma. More importantly, the argument shows that **the second scalar square is unnecessary for boundedness**: the same rank-two cross packet plus just one source-disjoint square already yields an integrable full characteristic function.

The partner's stronger `9/2` constant on the two-square family is preserved; (9.4) is not claimed as a numerical improvement for all epsilon. Its value is structural: one frequency-averaged square is enough.

## 10. Exact algebra sanity check

For 500 seeded random rank-two packets of the form

`M=[K; alpha^T K]`

and random symmetric B, the identity

`det(KK^T)|v^T Bv| = e_2(MM^T)|n^T Bn|`

had maximum normalized error `1.15e-14`. Symbolic simplification of the Fourier-inversion constant gives exactly

`C_* = 15*2^(2/5)*3^(1/5)/4 = (15/4)12^(1/5)`.

These finite checks are sanity checks only; the identities and inequality are proved analytically above.

## 11. Remaining gap and next mechanism

The unrestricted conjecture is **not solved**. The first structural implication left by this run is:

`QFORM-RANK2-CROSS-NEAR-NULL-KERNEL-ROUTING-v1`.

Starting only from the global three-large-eigenvalue hypothesis (or the current strict-N3 reduction), one must show that every rank-two-cross survivor either has dimension-free currency

`V_2(M)|n^T Bn|`

for Theorem 7.1, enters a rank-three/fifth-volume/diffuse exit, or routes quantitatively to an already-paid exact-null/near-null coloop, grouped-square, hub/star, ridge, or pair mechanism. The difficult subcase is now precisely when the cross block has substantial aggregate rank-two volume but its physical cross-kernel curvature is zero or very small.

Continuity: **proved** in the scope of Theorem 7.1 because `phi_Q in L1`.  
Full target continuity: **open**.

Independent review status: no independent end-to-end review of Theorem 7.1 is claimed in this run.
