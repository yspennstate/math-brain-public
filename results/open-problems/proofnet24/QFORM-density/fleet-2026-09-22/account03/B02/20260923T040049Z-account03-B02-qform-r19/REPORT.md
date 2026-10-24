SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T04:00:49Z.
attacking: aggregate a full physical three-column cross packet before reciprocal-minor payment; combine Cauchy--Schwarz removal of arbitrary self-curvature with determinant-weighted Pluecker entropy to obtain an actual L1 characteristic-function bound.

# account03/B02 QFORM r19 — balanced-Pluecker three-column integrated Fourier theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T040049Z-account03-B02-qform-r19`  
**Assignment:** Integrated Fourier estimate  
**Fresh owner control at start:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport is not native brain ingestion.  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** proved on the new packet branch below because its full characteristic function is in `L1`; full-target continuity remains OPEN.

## 1. Exact target and the unpaid Fourier issue

The target remains: for every finite `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal finite bound on the essential supremum of the density of `Q=X^T A X`, or give a valid target-class counterexample. No Gaussian, moment, log-concavity, support, diagonal-basis, or post-rotation-independence assumption is added.

The live correction that law-uniform pointwise one-dimensional quadratic-phase decay is false is retained. This run does **not** use such a scalar estimate. Instead it proves an integrated Fourier theorem for a physical cross packet by first removing arbitrary within-bank curvature through one Cauchy--Schwarz step and then aggregating all physical row minors of that packet through a determinant-weighted basis law.

I still do not have a valid exact-target counterexample to the stronger target-wide statement `int |phi_Q(t)| dt <= C`. Accordingly that target is not declared false. The result below proves it on a new source-valid branch.

## 2. Source input actually used

The analytic input is account02/B07 `QFORM-PLUCKER-ENTROPY-BL-v1`, canonical proof

`yspennstate/math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T123512Z-b07-qform-minors-11/REPORT.md`.

Let `U` be an `m x k` orthonormal-column frame, let

`w_R=det(U_R)^2`, `|R|=k`,

be its Pluecker basis law, and let `pi` be a probability law on nonzero bases with coordinate-inclusion marginals `p_i<=1/2`. The source theorem proves

`int_(R^k) prod_i |hat f_i(u_i^T xi)| dxi
 <= exp(D(pi||w)/2) (2pi)^k e^(k/2)`                       (2.1)

for arbitrary scalar probability densities `f_i<=1`. This is the phase-zero specialization of the source's stronger separable-phase statement, so the source's nonseparable-residual limitation is irrelevant after the Cauchy--Schwarz reduction below.

The source also proves that if

`delta=P(R cap S = empty)` for iid `R,S~w`,                         (2.2)

then, for `delta>0`, the first marginal of `(R,S)` conditioned on disjointness satisfies `p_i<=1/2` and

`D(pi||w)<=log(1/delta)`.                                            (2.3)

No individual coordinate minor is selected or inverted in (2.1)--(2.3).

## 3. Main theorem: arbitrary self-curvature plus a balanced physical k-column packet

### Theorem 3.1 — `QFORM-BALANCED-PLUCKER-CROSSPACKET-L1-v1`

Let `I,J,K` be a partition of original coordinate indices with `|J|=k>=3`; `I` may have arbitrary cardinality. Condition on the original coordinates in `K`. Suppose the physical cross block

`C=A[I,J] in R^(|I| x k)`

has full column rank `k`. Let

`C=U Sigma V^T`                                                     (3.1)

be a thin SVD, where `U^T U=I_k`, `V` is a square orthogonal `k x k` matrix, and

`Delta=prod_(j=1)^k sigma_j(C)=sqrt(det(C^T C))>0`.                  (3.2)

Let `w_R=det(U_R)^2` be the Pluecker law on physical row bases. Assume there is a basis law `pi` supported where `w_R>0` whose inclusion marginals satisfy `p_i<=1/2`; put

`D=D(pi||w)`.

Then, for the **full ambient quadratic form**, with arbitrary within-`I`, within-`J`, outside, and affine couplings,

`|phi_Q(t)| <= min{1,
 pi^(k/2) exp((D+k)/4) Delta^(-1/2) |t|^(-k/2)}.`                   (3.3)

Consequently `phi_Q in L1`, the law of `Q` has a bounded continuous density vanishing at infinity, and

`boxed(
 ||p_Q||_infinity
 <= [k/(k-2)] sqrt(e) exp(D/(2k)) Delta^(-1/k).
)`                                                                  (3.4)

The estimate is uniform in all values of the conditioned outside original coordinates, so it survives unconditional averaging.

### Proof

After fixing the outside bank `K`, write the remaining form as

`Q=q_I(X)+q_J(Y)+2 X^T C Y+c`,                                      (3.5)

where `X=(X_i)_(i in I)` and `Y=(X_j)_(j in J)` remain mutually independent original-coordinate product banks. The functions `q_I,q_J` may contain **all** within-bank quadratic and affine terms; their exact coefficients will not be used.

For fixed `t`, integrate first in `Y` and apply Cauchy--Schwarz in the probability measure of `X`. If `Y'` is an independent copy of `Y`, expansion of the square and the triangle inequality give

`|phi_(Q|K)(t)|^2
 <= E_(Y,Y') prod_(i in I)
       |hat f_i(2t [C(Y-Y')]_i)|.`                                  (3.6)

The phase `q_I` disappears in Cauchy--Schwarz, while `q_J(Y)-q_J(Y')` has modulus one and disappears only after the triangle inequality. Thus (3.6) is valid for arbitrary nonseparable self-curvature on **both** active physical banks. No rotated variables are declared independent.

Put `D_Y=Y-Y'`. Its coordinates are independent, with scalar difference densities

`g_j=f_j*tilde f_j`, `0<=g_j<=1`, `int g_j=1`.                       (3.7)

Because `|J|=k` and the right singular matrix `V` in (3.1) is square orthogonal, the variable

`Z=V^T D_Y`

has a joint density bounded pointwise by one: it is just the orthogonal image, with Jacobian one, of the product density `prod_j g_j`. Hence (3.6) and `C=U Sigma V^T` give

`|phi_(Q|K)(t)|^2
 <= int_(R^k) prod_(i in I)
       |hat f_i(2t u_i^T Sigma z)| dz`.                              (3.8)

For `t!=0`, set `xi=2t Sigma z`. The Jacobian is

`dz=(2|t|)^(-k) Delta^(-1) dxi`.                                   (3.9)

Apply the source inequality (2.1) to the last integral. This yields

`|phi_(Q|K)(t)|^2
 <= (2|t|)^(-k) Delta^(-1)
    exp(D/2)(2pi)^k e^(k/2)
 = pi^k exp((D+k)/2) Delta^(-1)|t|^(-k).`                           (3.10)

Taking square roots and combining with the trivial `|phi|<=1` proves (3.3). Since the bound is uniform in the outside conditioning, averaging over `K` preserves it.

Set

`A_k=pi^(k/2) exp((D+k)/4) Delta^(-1/2)`.

The crossover in `min(1,A_k |t|^(-k/2))` is

`t_0=A_k^(2/k)=pi exp((D+k)/(2k)) Delta^(-1/k)`.                    (3.11)

For `k>2`, direct integration gives

`||phi_Q||_1
 <=2 t_0 [1+2/(k-2)]
 =2pi [k/(k-2)] exp((D+k)/(2k)) Delta^(-1/k).`                       (3.12)

Fourier inversion therefore gives a continuous density and, dividing (3.12) by `2pi`, exactly (3.4). QED.

The pointwise envelope (3.3) is **not** a law-uniform scalar van-der-Corput claim. It is a whole-packet consequence of Cauchy--Schwarz, product difference densities, and a determinant-weighted multidimensional Fourier integral.

## 4. Canonical k=3 disjoint-basis corollary

For the assigned three-direction situation take `k=3`. If the exact disjoint-basis mass `delta` in (2.2) is positive, (2.3) inserted into (3.3)--(3.4) gives

`boxed(
 |phi_Q(t)|
 <= min{1,
 pi^(3/2)e^(3/4) delta^(-1/4) Delta^(-1/2)|t|^(-3/2)}
)`                                                                  (4.1)

and

`boxed(
 ||phi_Q||_1 <=6pi sqrt(e) delta^(-1/6) Delta^(-1/3),
)`                                                                  (4.2)

`boxed(
 ||p_Q||_infinity <=3 sqrt(e) delta^(-1/6) Delta^(-1/3)
 <4.946164 delta^(-1/6) Delta^(-1/3).
)`                                                                  (4.3)

The density is continuous on this branch.

This replaces a single-minor reciprocal by a determinant-weighted aggregate. Indeed Cauchy--Binet gives

`G=det(C^T C)=sum_(|R|=3) det(C_R)^2=Delta^2`.                       (4.4)

Moreover

`w_R=det(C_R)^2/G`.                                                  (4.5)

Define the disjoint-pair minor mass

`S_dis=sum_(R cap S=empty) det(C_R)^2 det(C_S)^2`.                   (4.6)

Then exactly

`delta=S_dis/G^2`,                                                   (4.7)

so (4.3) is equivalently

`boxed(
 ||p_Q||_infinity
 <=3 sqrt(e) [ G/S_dis ]^(1/6).
)`                                                                  (4.8)

Thus no individual `3 x 3` row minor of the fixed physical three-column packet has to be macroscopically large. Many individually tiny row minors can pay collectively, provided their determinant weight is not concentrated on mutually intersecting bases.

The strict finite-core obstruction is also represented honestly: if all nonzero Pluecker bases meet each other, then `delta=0` and this theorem deliberately gives no bound rather than silently dividing by a tiny selected minor.

## 5. Actual application of the designated partner account04/B02

The completed designated partner theorem is account04/B02 `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`, canonical proof

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`.

On any overlap where the full quadratic matrix also contains a nonsingular physical principal `3 x 3` block `P` with a zero diagonal entry, the partner gives the genuine global Fourier inequality

`int |phi_Q(t)|^2 dt
 <= L_P :=6pi 2^(2/3)|det P|^(-1/3).`                                (5.1)

Apply (5.1) to low frequencies and the new disjoint-basis tail (4.1) to high frequencies. For every `T>0`,

`int_(|t|<=T)|phi_Q(t)|dt <=(2T L_P)^(1/2)`,                         (5.2)

while, with

`A=pi^(3/2)e^(3/4)delta^(-1/4)Delta^(-1/2)`,

`int_(|t|>T)|phi_Q(t)|dt <=4A T^(-1/2)`.                             (5.3)

Optimizing at `T=4A/sqrt(2L_P)` yields

`||phi_Q||_1 <=4 A^(1/2)(2L_P)^(1/4)`.                              (5.4)

Therefore the partner theorem has been used at an actual new equation-level inequality:

`boxed(
 ||p_Q||_infinity
 <=2^(5/3) 3^(1/4)e^(3/8)
   delta^(-1/8) Delta^(-1/4)|det P|^(-1/12)
 <6.079354
   delta^(-1/8) Delta^(-1/4)|det P|^(-1/12).
)`                                                                  (5.5)

This hybrid is not claimed to dominate either source in every parameter regime; its role is to show a valid interpolation of two independently completed Fourier resources without inventing independence.

## 6. Relation to the exact three-large-eigenvalue target

The theorem is a genuine advance on the aggregate-before-inversion debt because, for a **fixed three-column physical bank**, it uses the entire determinant mass of all physical row triples before any reciprocal determinant is paid. It also tolerates arbitrary self-curvature on both active banks and arbitrary outside spectrum/couplings; those phases are eliminated by the Cauchy--Schwarz step, not assumed separable.

It is not yet an exhaustive consequence of `s_3(A)>=1`. Known source corrections rule out claiming that the spectral hypothesis forces one uniformly good physical fixed minor or one uniformly good rank-three cut. In the present language, a target-wide proof still needs a dimension-free routing statement that produces either

1. a physical three-column packet with `delta` and `Delta` jointly at a paid scale;
2. a corresponding transpose packet;
3. a paid localized principal/zero-diagonal/indefinite-pair/hub/grouped-square branch; or
4. one of the completed diffuse/ridge/high-cardinality aggregate exits.

The theorem especially removes one source of dimension loss: once a three-column packet has substantial **total** three-volume and nontrivial disjoint Pluecker mass, no largest-minor argument is needed.

The stronger full-target unweighted `L1` Fourier criterion remains OPEN rather than refuted. Full QFORM essential boundedness remains OPEN, and full-target continuity remains OPEN.

## 7. Deterministic checks

The companion checker verifies on seeded random full-column-rank `m x 3` matrices that

`sum_R det(U_R)^2=1`,

`delta=S_dis/det(C^T C)^2`,

and the direct/hybrid constants simplify to the displayed numerical values. These checks are regression tests only; Sections 3--5 are the proof.

## 8. Classification and next B02 implication

**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

The first unpaid B02 implication is now `QFORM-THREECOLUMN-PACKET-OR-LOCALIZED-ROUTING-v1`: from the global three-large-eigenvalue hypothesis, aggregate Cauchy--Binet three-volume across physical **column triples** and prove that a constant fraction routes either to a packet with quantitatively nonnegligible disjoint row-basis mass (paid by Theorem 3.1), or to the already-paid localized/hub/pair/grouped branches. The mechanism must aggregate before selecting a tiny column triple and must retain arbitrary extra spectrum.

No scheduler, task identity, cadence, notification, email/Drive, public-release, paid-model/API, Codex, credential, cross-account-authentication, or permission state is changed by this run.
