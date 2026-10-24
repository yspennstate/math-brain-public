SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T14:39:44Z.
attacking: the exact zero-diagonal common-hub survivor, using orientation-free rank-two half-Riesz smoothing and a translation-uniform two-bank product estimate before any tiny physical minor is inverted.

# Zero-diagonal common-hub packet: nonzero-hub half-Riesz closure and a rigid grouped endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T143944Z-account01-B01-qform-auto11`  
Role: account01/B01 — Oscillatory replacement  
Status: **NEW SUPPORTING ANALYTIC CLOSURE + STRICT-N3 STRESS FAMILY / FULL QFORM OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source and correction boundary

Fresh prepublication control was `yspennstate/math-research-brain@93ddfe864ffb68a24e7b4c258e1388a8e0dae5e3`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only, with no B01 pause or stop. The live correction inbox was reread at that ref. In particular, this report does **not** use:

- law-uniform pointwise `|t|^{-1/2}` decay for scalar quadratic phases;
- independence after a spectral rotation;
- an arbitrary-joint rank-three coarea theorem;
- a worst conditional projection-density cap or positive moment of such a cap;
- a uniformly good single physical minor.

The unrestricted owner target remains OPEN. Full-target continuity remains OPEN.

The preceding B01 endpoint is the common-hub rank-one-leaf packet obtained after the diagonal leaf curvature has collapsed to zero. The exact setup is: one ORIGINAL physical hub `h`, an ORIGINAL-coordinate leaf bank `L`,

`A[L,L]=lambda z z^T`, `lambda!=0`,

`b=A[L,h]`, and

`E=det([b,z]^T[b,z])
  =||b||^2||z||^2-(b.z)^2>0`.

Arbitrary outside ORIGINAL coordinates may be conditioned on. They contribute arbitrary affine terms to the packet and arbitrary conditioned constants; no product structure is claimed after any rotation.

The source-valid orientation-free rank-two affine half-Riesz theorem used below is

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`:

for an orthonormal two-frame `U`, invertible symmetric `2x2` matrix `Lambda`, and **arbitrary** original-coordinate affine vector,

`sup_s E |(U^T X)^T Lambda(U^T X)+linear-s|^(-1/2)
 <=128 |det Lambda|^(-1/4).`                                      (1.1)

The newest completed designated partner actually used in this run is account02/B01 r44,

`yspennstate/math-open-problems@31608e4193b3ba491084081cb7c000e254c01a82`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T142922Z-account02-B01-qform-r44/REPORT.md`.

Its volume-marginal compiler is applied quantitatively in Section 7.

## 2. The phase-aligned pointwise counterexample remains intact

Fix a scalar frequency `s>0` and `0<delta<pi/2`. The phase-aligned set

`E_infty={x: dist(s x^2,2 pi Z)<=delta}`

has infinite Lebesgue measure: the component lengths around `sqrt(2 pi k/s)` are comparable to `k^(-1/2)`. Choose a finite union `E subset E_infty` of total measure one and take the admissible density `f=1_E`. Then

`Re int exp(i s x^2) f(x) dx >=cos(delta).`                         (2.1)

Thus no positive-power law-uniform pointwise scalar decay can hold. Nothing in this report contradicts (2.1): the replacements are fractional-potential averaging and product projection.

## 3. A nonzero physical hub closes the exact zero-diagonal leaf packet

Let

`a=A_hh !=0`.                                                       (3.1)

After conditioning outside the packet, write the affine hub coefficient as `2 beta`. Completing only this ORIGINAL physical coordinate gives

`Q=a(X_h+(b.X_L+beta)/a)^2+R(X_L)`,                                (3.2)

where the quadratic part of the exact residual is

`B=lambda z z^T-a^(-1)b b^T`.                                      (3.3)

Since `E>0`, `b,z` are linearly independent, so `B` has rank exactly two. Its two nonzero eigenvalues have product

`boxed: det_2(B)=-(lambda/a) E.`                                   (3.4)

This follows by restricting (3.3) to `span{b,z}` and taking the Gram determinant.

The arbitrary affine term left in `R` is permitted by (1.1), hence

`sup_s E |R-s|^(-1/2)
 <=128 (|lambda|E/|a|)^(-1/4).`                                    (3.5)

For every fixed leaf realization, the conditional law of

`a(X_h+t)^2`

has density bounded by

`|a|^(-1/2)|y|^(-1/2)`.                                            (3.6)

Averaging (3.6) against the residual and using (3.5) gives the main scalar-hub receiver:

### Theorem 3.1 — `QFORM-ZERODIAG-HUB-RANK2-HALF-RIESZ-v1`

In the exact zero-diagonal common-hub packet above, if `a!=0`, then for arbitrary cap-one product laws and arbitrary outside couplings/affine terms,

`boxed:
 ||p_Q||_infinity
 <=128 (|a lambda| E)^(-1/4).`                                     (3.7)

This is an essential-boundedness conclusion. The present square-kernel/half-Riesz composition does not by itself prove a continuous representative.

Thus exact zero leaf diagonal curvature is no longer an analytic obstruction merely because the hub curvature is small but nonzero. What remains is quantitative structural control of the homogeneous currency `|a lambda|E`, or a different grouped receiver when it becomes small.

## 4. Translation-uniform two-bank product half-Riesz estimate

The next lemma is useful precisely when the Schur residual factors into two independent ORIGINAL-coordinate banks.

### Lemma 4.1 — two-bank product half-Riesz

Let `Y=(Y_i)_(i in P)` and `Z=(Z_j)_(j in N)` be disjoint ORIGINAL-coordinate product banks, each coordinate having density at most one. Let `u,v` be nonzero vectors, `c!=0`, and allow arbitrary affine vectors `d,e` and constant `gamma`. Put

`T=c(u.Y)(v.Z)+d.Y+e.Z+gamma`.                                     (4.1)

Let `C_proj` be the one-dimensional product-projection constant; Rogozin--Ball gives

`C_proj<=sqrt(2)`, `||p_(r.X)||_infinity<=C_proj/||r||_2`.          (4.2)

Then

`boxed:
 sup_s E |T-s|^(-1/2)
 <=8 C_proj (|c| ||u||_2 ||v||_2)^(-1/2).`                         (4.3)

#### Proof

Condition on `Y`, put `U=u.Y`, and absorb `d.Y+gamma` into the target translation. The coefficient of the untouched `Z` bank is

`c U v+e`.

With

`u_0=-<e,v>/(c||v||^2)`,

projection onto `v/||v||` gives

`||cUv+e|| >= |c| ||v|| |U-u_0|`.                                 (4.4)

A one-dimensional probability density capped by `M` satisfies the exact bathtub estimate

`sup_s int |x-s|^(-1/2)f(x)dx <=2 sqrt(2M)`.                       (4.5)

By (4.2), conditional on `Y` the linear `Z`-form has density cap at most

`C_proj/(|c| ||v|| |U-u_0|)`.

Equations (4.4)-(4.5) therefore give

`sup_s E_Z |T-s|^(-1/2)
 <=2 sqrt(2 C_proj)(|c|||v||)^(-1/2)|U-u_0|^(-1/2).`                (4.6)

The variable `U` itself has density cap `C_proj/||u||`. Applying (4.5) once more and multiplying gives exactly (4.3). The single value `U=u_0` has probability zero; the right side of (4.6) is integrable by the second bathtub estimate. QED.

This is a distribution-function replacement for pointwise oscillatory decay. It remains uniform under all translations generated by outside conditioning.

## 5. Rigid endpoint: every physical hub-leaf pair determinant is zero

Assume, in addition to `A[L,L]=lambda z z^T`, that

`a lambda z_i^2-b_i^2=0` for every leaf coordinate `i`.             (5.1)

Because `E>0`, (5.1) forces `a lambda>0`; moreover `b_i=0` whenever `z_i=0`, and on the nonzero support

`b_i=s_i sqrt(a lambda) z_i`, `s_i in {+1,-1}`.                    (5.2)

The signs cannot all agree, otherwise `b` would be parallel to `z` and `E=0`. Split the nonzero leaf support into the two nonempty ORIGINAL-coordinate banks

`P={i:s_i=+1}`, `N={i:s_i=-1}`,

and define

`U=z_P.X_P`, `V=z_N.X_N`,
`r=||z_P||_2`, `s=||z_N||_2`.                                     (5.3)

Complete the physical hub exactly as in Section 3, retaining all induced affine terms. The quadratic residual collapses to

`boxed: R_quad=4 lambda U V.`                                      (5.4)

Indeed `lambda(U+V)^2-a^(-1)[sqrt(a lambda)(U-V)]^2=4lambda UV`.

Lemma 4.1 with `c=4lambda` yields

`H_(1/2)(R)
 <=4 C_proj (|lambda| r s)^(-1/2).`                                (5.5)

Combining with the outer physical-square kernel gives

`boxed:
 ||p_Q||_infinity
 <=4 C_proj / sqrt(|a lambda| r s).`                               (5.6)

Again this is essential boundedness; continuity is not asserted by this proof.

There is an exact spectral interpretation. On the grouped span generated by the hub, `z_P/r`, and `z_N/s`, after harmless sign conjugation and overall sign normalization the packet matrix is

`M=[[A,sqrt(A L)r,-sqrt(A L)s],
    [sqrt(A L)r,L r^2,L r s],
    [-sqrt(A L)s,L r s,L s^2]]`,                                  (5.7)

where `A=|a|`, `L=|lambda|`. Its inverse is exactly

`M^(-1)=
 [[0,1/(2sqrt(AL)r),-1/(2sqrt(AL)s)],
  [1/(2sqrt(AL)r),0,1/(2Lrs)],
  [-1/(2sqrt(AL)s),1/(2Lrs),0]].`                                 (5.8)

If

`sigma=min{|mu|: mu is a nonzero eigenvalue of M}`,                 (5.9)

then every entry of `M^(-1)` has modulus at most `1/sigma`. Hence

`sqrt(AL)r>=sigma/2`, `sqrt(AL)s>=sigma/2`,

and therefore

`AL r s>=sigma^2/4`.                                               (5.10)

Substitution into (5.6) gives the scale-stable endpoint

### Theorem 5.1 — `QFORM-ZERODIAG-PAIRMINORZERO-GROUPED-v1`

Under (5.1),

`boxed:
 ||p_Q||_infinity <=8 C_proj/sigma <=8 sqrt(2)/sigma.`              (5.11)

In particular, if this exact rank-three packet has all three nonzero eigenvalues of modulus at least one, then

`boxed: ||p_Q||_infinity <=8 sqrt(2).`                              (5.12)

The value of (5.11) stays controlled even when the physical scalar `a` itself tends to zero, provided the grouped packet remains spectrally nondegenerate.

## 6. A strict-N3 stress family with tiny hub curvature, all physical pair determinants zero, and no rank-three cross cut

Let `P,N` be disjoint banks of equal size `m`, and let `u,v` be their flat unit vectors. Put

`z=(u+v)/sqrt(2)`, `b=u-v`.                                       (6.1)

For `0<epsilon<=1`, choose

`a=epsilon`, `lambda=2/epsilon`,                                  (6.2)

and define the full rank-three physical matrix

`A_(epsilon,m)=
 [[epsilon,b^T],
  [b,(2/epsilon) z z^T]].`                                        (6.3)

On the grouped span `{hub,u,v}`, (6.3) is

`M_epsilon=
 [[epsilon,1,-1],
  [1,epsilon^(-1),epsilon^(-1)],
  [-1,epsilon^(-1),epsilon^(-1)]].`                               (6.4)

Its eigenvalues are exactly

`2/epsilon`,
`(epsilon+sqrt(epsilon^2+8))/2`,
`(epsilon-sqrt(epsilon^2+8))/2`.                                  (6.5)

For every `0<epsilon<=1`, all three have modulus at least one. Thus this is a bona fide target matrix.

At the same time every physical hub-leaf principal determinant is zero:

`epsilon*(1/(epsilon m))-(1/sqrt(m))^2=0`,                         (6.6)

and every leaf-leaf principal determinant is zero because the leaf block is rank one. Its largest physical diagonal is

`max(epsilon,1/(epsilon m))`.                                     (6.7)

Hence for every fixed no-pivot threshold `tau in (0,1]`, choosing

`epsilon<tau`, `m>1/(epsilon tau)`                                 (6.8)

places the family in strict N3 while preserving the three target eigenvalues.

Every physical coordinate cut has cross rank at most two: the hub star contributes cross rank at most one and the leaf square contributes cross rank at most one. Thus a proof relying on the existence of a rank-three physical cross cut cannot pay this family.

Here `r=s=1/sqrt(2)` and `|a lambda|=2`, so (5.6) gives the uniform bound

`boxed:
 ||p_(X^T A_(epsilon,m) X)||_infinity
 <=4 C_proj <=4 sqrt(2)=5.65685424949...`                         (6.9)

for every admissible cap-one product law, uniformly as `epsilon->0` and `m->infinity` subject to (6.8).

The deterministic checker in this run verifies (6.5), the exact physical pair determinants, cross-rank at most two, and the exterior-three identity on a finite physical instance. For `epsilon=1/2,m=3` it obtains

`(W0,W1,W2,W3)=(0,256/9,256/9,64/9)`,

whose sum is `64=16/epsilon^2=e_3(A^2)`, and it ends `STATUS=PASS`. These finite checks are diagnostics only; the proofs above are algebraic.

## 7. Latest designated partner r44 applied to an actual inequality

Account02/B01 r44 proves the following volume-marginal routing for an ORIGINAL-coordinate cross block `M` with

`Z=e_3(M^T M)>0`.                                                  (7.1)

With threshold `h=43/64`:

- if the constrained-side volume marginals are all at most `43/64`, then

  `||p_Q||_infinity <22.512 Z^(-1/6)`;                             (7.2)

- if at least three row marginals (or, after transposition, column marginals) are at least `43/64`, then

  `||p_Q||_infinity <8.486 Z^(-1/6)`.                              (7.3)

Both conclusions have continuous `C_0` densities.

Apply this completed partner theorem at the target-scale threshold

`Z>=1/64`.                                                         (7.4)

Then (7.2) becomes the concrete universal inequality

`boxed: ||p_Q||_infinity <45.024`,                                 (7.5)

while (7.3) becomes

`boxed: ||p_Q||_infinity <16.972`.                                 (7.6)

Thus any target-scale rank-three cross packet on which either r44 paid test fires is closed **before** the present zero-diagonal hub analysis is needed. If both paid tests fail, r44 proves that each orientation has only one or two `43/64`-heavy volume coordinates; that `<=2 x <=2` survivor remains a structural routing problem. This is an equation-level application of the newest completed designated-partner result, not a copied citation.

The stress family in Section 6 lies deliberately outside (7.1)-(7.4): every physical cross block has rank at most two and hence `Z=0` for every cut. It is therefore a complementary endpoint rather than a duplicate of r44.

## 8. Owner-supplied volume-stability theorem applied as a second early exit

The owner-supplied volume-stability theorem at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`

states that if an ORIGINAL-coordinate cross block has

`M=M0+E0`, `s3(M0)>=eta>0`,
`max_i (P_range(M0))_ii<=1/2`, `||E0||op<=eta/16`,                  (8.1)

then

`||p_Q||_infinity<23/eta`,                                        (8.2)

with a continuous `C_0` density and arbitrary self-blocks/outside couplings retained.

Thus whenever `eta>=1/4`, (8.2) gives the explicit universal exit

`boxed: ||p_Q||_infinity<92.`                                     (8.3)

Again the Section 6 stress family has cross rank at most two, so it does not satisfy a rank-three stability certificate and is genuinely complementary.

## 9. Compact conditional proof map after this run

The first relevant routes can now be ordered without circularity:

1. A stable rank-three diffuse cross block satisfying (8.1) with `eta>=1/4` is paid by (8.3), continuously.
2. A target-scale rank-three volume packet `Z>=1/64` satisfying either completed partner r44 gate is paid by (7.5) or (7.6), continuously.
3. In the common-hub rank-one-leaf route, the preceding B01 curvature/pivot currencies are paid first. If they collapse to the exact zero leaf diagonal packet and `a!=0`, Theorem 3.1 supplies essential boundedness.
4. If, additionally, every physical hub-leaf pair determinant is zero, Theorem 5.1 converts grouped spectral nondegeneracy directly into a universal bound, uniformly through tiny `a`.

The first unproved structural implication is therefore sharpened to

`QFORM-W1-ZERODIAG-ZEROHUB-OR-PAIRMINOR-STABILITY-v4`:

starting from a global overlap-one-heavy state, localize dimension-free to a common-hub rank-one-leaf packet or route higher leaf rank into an already-paid volume/pair/ridge/grouped branch; inside the common-hub zero-diagonal packet, when the hub scalar is zero or quantitatively tiny **and** the hub-leaf pair determinants are not in the rigid all-zero state of Section 5, route to a mixed-hub/bilinear-square/pair receiver without reciprocating one tiny physical minor. The r44 `<=2 x <=2` heavy-volume survivor is a compatible parallel structural obligation.

This run does **not** prove that every matrix with three large eigenvalues enters one of the paid branches above. Therefore the full conjecture remains OPEN.

## 10. Regularity, scaling, and review status

- Theorem 3.1: essential boundedness proved; continuity not claimed.
- Lemma 4.1: fractional-potential estimate, not itself a density theorem.
- Theorem 5.1: essential boundedness proved; continuity not claimed.
- Partner r44 branches and the volume-stability branch: continuous `C_0` densities at their exact scopes.
- Full-target continuity: OPEN.
- Independent end-to-end reviews of the full target: not supplied by this run.

All new bounds have the correct homogeneity under `A->cA`. No Gaussianity, log-concavity, moment bound, compact support, connected support, identical-law assumption, or diagonalization of the product law has been introduced.
