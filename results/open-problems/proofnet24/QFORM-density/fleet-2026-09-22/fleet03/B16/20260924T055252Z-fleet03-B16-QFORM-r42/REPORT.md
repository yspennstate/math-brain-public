SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-24T05:52:52Z.
attacking: the small-pivot majority-sign root-numerator debt by keeping the physical hub-star coupling through an exact Plancherel estimate, then isolating the genuinely integrated residual-fiber norm that remains after the false pointwise-decay routes are removed.

# fleet03/B16 r42 — hub-star Plancherel averaging and the exact integrated residual-fiber debt

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T055252Z-fleet03-B16-QFORM-r42`  
**Role:** Projection-product interaction  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `NEW PIVOT-UNIFORM OSCILLATORY AVERAGE + EXACT MIXED-NORM REDUCTION / FULL QFORM OPEN`  
**Regularity:** the new theorem below is an oscillatory estimate and supporting reduction. It does not by itself prove an essentially bounded density or full-target continuity.

## 1. Source boundary and the first missing implication

The target remains the unrestricted owner statement: independent original-coordinate real inputs with scalar probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, smoothness, log-concavity, iid, post-rotation independence, or pointwise van-der-Corput hypothesis is introduced.


The immediate predecessor is fleet03/B16 r41:

- repository: `yspennstate/math-open-problems`;
- commit: `41659aaf9ff3d32a60c331cbde54d6c516f75029`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260924T045704Z-fleet03-B16-QFORM-r41/REPORT.md`.

For an exact-rank-three nonzero physical pivot

`A=[[a,b^T],[b,C]]`, `a!=0`, `S=C-bb^T/a`,

r41 proved, writing `b=b_R+b_0`, `rho=||b_R||`, `tau=||b_0||`, and `q_h=||P_(ran A)e_h||^2`, that

`q_h=a^2/(a^2+tau^2)`,

`a pdet(S)=q_h Delta_A`,

`rho^2 >= s^2 q_h-a^2/q_h` when all three nonzero eigenvalues have modulus at least `s`.

Hence in the live hard collar

`q_h>=63/64`, `0<|a|<=s/64`,

one has

`rho^2>=(62/63)s^2`, `tau<=|a|/sqrt(63)`, `|pdet S|>=63s^2`.

The literal-hub root formula also showed that replacing the two values of the original hub density by the crude cap one erases the order-one star `rho` completely. The first missing implication is therefore not another discriminant-only estimate. We need an interface that keeps the physical star while respecting arbitrary rough one-dimensional laws.

This run supplies exactly such an interface at the Fourier level.

## 2. Exact hub-star Plancherel identity

Let `H` be a real random variable with probability density `f_H` satisfying `0<=f_H<=1`. Let `X` be an independent random vector (for the application below, an original-coordinate product bank), let `b!=0`, and let `R(X)` be any real measurable random variable. Consider

`Q=a H^2+2H (b dot X)+R(X)`                                    (2.1)

for an arbitrary real scalar `a`; in particular `a` may be zero or arbitrarily small.

Put

`B=b dot X`                                                     (2.2)

and, for `t!=0`, define the physical-hub transform

`F_t(z)= integral_R f_H(h) exp(i t (a h^2+2zh)) dh`.            (2.3)

### Theorem `QFORM-HUB-STAR-PLANCHEREL-AVERAGE-v1`

For every `t!=0`,

`boxed: integral_R |F_t(z)|^2 dz = (pi/|t|) integral_R f_H(h)^2 dh <= pi/|t|.`   (2.4)

If `B` has a density `p_B` with cap `M_B`, then the characteristic function of (2.1) satisfies

`boxed: |phi_Q(t)| <= sqrt(pi M_B/|t|).`                          (2.5)

If, moreover, `X` has independent coordinates with density caps one, then the sharp one-dimensional product-projection theorem gives

`M_B <= sqrt(2)/||b||`,                                          (2.6)

and therefore

`boxed: |phi_Q(t)| <= sqrt(pi) 2^(1/4) ||b||^(-1/2) |t|^(-1/2).` (2.7)

No constant in (2.4)--(2.7) depends on the pivot `a`, on the signs of any quadratic coefficients, on moments, or on regularity/support of the laws.

### Proof

Let

`g_t(h)=f_H(h) exp(i t a h^2)`.

With Fourier convention

`hat g(xi)= integral g(h) exp(i xi h) dh`,

we have

`F_t(z)=hat g_t(2tz)`.

Thus, by the change of variables `xi=2tz` and Plancherel,

`integral |F_t(z)|^2 dz
 = (1/(2|t|)) integral |hat g_t(xi)|^2 dxi
 = (pi/|t|) integral |g_t(h)|^2 dh
 = (pi/|t|) integral f_H(h)^2 dh`.

Because `f_H` is a probability density and `f_H<=1`,

`integral f_H^2 <= ||f_H||_infinity integral f_H <=1`,

proving (2.4).

Now introduce the complex fiber density

`G_t(z)=p_B(z) E[ exp(i t R(X)) | B=z ]`                          (2.8)

for any regular conditional version. Equivalently, `G_t(z)dz` is the complex measure

`E[ exp(i t R(X)); B in dz ]`.

Then

`phi_Q(t)= integral F_t(z) G_t(z) dz`.                            (2.9)

Moreover

`|G_t(z)|<=p_B(z)`, so

`||G_t||_2^2 <= integral p_B(z)^2 dz <= M_B integral p_B(z)dz=M_B`.   (2.10)

Cauchy--Schwarz together with (2.4) proves (2.5).

For (2.6), normalize `u=b/||b||`. The one-dimensional marginal theorem for a unit linear projection of a cap-one product density gives `||p_(u dot X)||_infinity<=sqrt(2)`; scaling by `||b||` gives `M_B<=sqrt(2)/||b||`. Substitution into (2.5) proves (2.7). QED.

### Why this does not contradict the phase-aligned-support correction

The false statement is a **pointwise law-uniform decay for one isolated quadratic phase** `E exp(i t H^2)`. Equation (2.4) is different: it is an exact `L^2` identity in the random star-frequency variable `z`. It averages the physical-hub transform over all translations of the linear frequency. Fragmented phase-aligned supports can keep one value `F_t(z_0)` large, but Plancherel controls the entire `z`-profile and the bounded-density projection theorem controls how much probability the independent residual bank can place on that profile.

This is precisely the kind of integrated/projection-product mechanism still allowed by the live corrections.

## 3. Quantitative application to the r41 hard collar

Return to the exact-rank-three matrix of r41. With the literal original hub `H=X_h` and residual original product bank `X_J`,

`Q=aH^2+2H b^T X_J+X_J^T C X_J`.                                (3.1)

The r41 collar gives

`||b||>=rho>=s sqrt(62/63)`.                                     (3.2)

Applying (2.7) yields, for every `t!=0`,

`|phi_Q(t)|
 <= sqrt(pi) 2^(1/4) [s sqrt(62/63)]^(-1/2) |t|^(-1/2)`

and hence

`boxed:
 |phi_Q(t)| <= C_* (s|t|)^(-1/2),
 C_* = sqrt(pi) (63/31)^(1/4)
      = 2.116263055051265... .`                                  (3.3)

This estimate is uniform as the physical pivot `a->0` and is valid on both sign branches. In contrast to the positive-root majorant of r41, it preserves the order-one physical-star information instead of cancelling it.

The gain is real but not yet sufficient: `|t|^(-1/2)` is not integrable. Thus (3.3) is not presented as a density proof.

## 4. Exact residual-fiber formulation: what remains after the hub is paid

The representation (2.9) identifies the remaining debt without any fictitious conditional density bound. For the hard collar set

`R(X_J)=X_J^T C X_J`, `B=b^T X_J`,

and define `G_t` by (2.8). Its Fourier transform in the fiber coordinate is exact:

`hat G_t(xi)
 = E exp(i[t X_J^T C X_J + xi b^T X_J])`.                        (4.1)

Therefore Plancherel gives

`boxed:
 ||G_t||_2^2
 = (1/(2pi)) integral_R
   | E exp(i[t X_J^T C X_J + xi b^T X_J]) |^2 dxi.`              (4.2)

Combining (2.4), (2.9), and Cauchy--Schwarz yields the exact sufficient estimate

`boxed:
 |phi_Q(t)| <= sqrt(pi/|t|) ||G_t||_2.`                           (4.3)

Consequently a full integrated-Fourier closure of this collar would follow from the **mixed norm**

`boxed:
 integral_{|t|>=1} |t|^(-1/2) ||G_t||_2 dt <= C_res`              (4.4)

with a universal constant at the normalized spectral scale `s=1`. Indeed `|phi_Q(t)|<=1` on `|t|<=1`, while (4.3) and (4.4) give

`integral_R |phi_Q(t)|dt <=2+sqrt(pi) C_res`,                    (4.5)

so Fourier inversion would give a bounded continuous `C_0` density with

`||p_Q||_infinity <= [2+sqrt(pi) C_res]/(2pi)`.                  (4.6)

### The crucial correction-aware point

Do **not** replace (4.4) by a law-uniform pointwise decay assertion for `||G_t||_2`. That would reintroduce the phase-aligned-support error. Already in source-separated diagonal controls, a residual square can be phase-aligned at a chosen frequency. The plausible surviving object is the integrated mixed norm (4.4), or an equivalent direct small-ball estimate, not a uniform pointwise Fresnel envelope.

Thus `QFORM-HUB-STAR-PLANCHEREL-AVERAGE-v1` reduces the root-numerator problem to a sharply stated, correction-safe residual question: prove (4.4) using the rank-two Schur curvature and original-product provenance **before** taking a worst fiber supremum.

This is a stronger formulation than merely saying “use cancellation”: it specifies the exact norm, the exact affine-frequency integral (4.2), and the exact amount of decay/integrability still owed.

## 5. Relation to the latest fleet01/B16 phase-aware theorem

A fresh compatible peer result published immediately before this run is fleet01/B16

`QFORM-DENSITY-PRESERVING-SHEAR-MIXED-FRESNEL-v1`,

canonical mathematics commit `4cc097c9bc5e49f71cbb75a85a5a8b54b96ca4d5`.

It proves a full `|t|^(-3/2)` characteristic-function envelope when a source-separated projected hub `W` couples to a two-dimensional leaf frame and a real density-preserving shear solves the positive-discriminant condition. That result is fully consistent with (4.3): in the phase-aligned subbranch it supplies precisely the additional leaf-bank oscillation that the general `G_t` in (4.4) still lacks.

The remaining r41 collar includes a small same-bank transverse leakage `tau P`, with `tau<=|a|/sqrt(63)`, for which perturbative deletion is not allowed. The present run therefore does not claim the fleet01 endpoint automatically extends across that leakage. Instead, (4.4) gives a norm in which such an extension can be attacked without sacrificing the physical star.

## 6. Designated fleet04/B16 result applied to an actual strict-target inequality

The newest completed designated partner is fleet04/B16 r4:

- canonical mathematics: `yspennstate/math-open-problems@7f2bb2d330022b09a6af6e39ab09d054caeaa346`;
- theorem used here: if a disjoint original-coordinate product bank enters only through a two-dimensional orthogonal projection `(U,V)` with joint density cap at most two and a **definite** quadratic matrix `H_2`, while all outside variables contribute arbitrary affine translations and an additive term, then

`||p_Q||_infinity <= 2pi/sqrt(|det H_2|)`.                       (6.1)

Here is a new literal application, with arbitrary outside quadratic baggage retained.

Split the independent original coordinates into three disjoint banks: a single physical coordinate `H`, a product bank `Y`, and another product bank `W`. Let `(U,V)` be any orthonormal two-dimensional projection of `Y`. Let `ell_0,ell_1,ell_2` be arbitrary linear forms of `W` and let `R(W)` be an arbitrary quadratic-plus-linear form of `W`. For every real `eta`, define

`Q_eta = -H^2 + 2 eta H U + 2U^2+2V^2
         +2U ell_1(W)+2V ell_2(W)+2H ell_0(W)+R(W).`              (6.2)

Condition on `(H,W)`. The `Y` bank appears only through `(U,V)` with quadratic matrix

`H_2=diag(2,2)`, `det H_2=4`,                                   (6.3)

and an arbitrary affine translation. The partner theorem therefore gives, conditionally and hence unconditionally,

`boxed: ||p_(Q_eta)||_infinity <= pi`                             (6.4)

uniformly in `eta`, in all three product laws, and in every choice of the outside forms `ell_j,R`.

This is an actual owner-target class, not a rank-two surrogate. The orthogonal compression of the full symmetric coefficient matrix to `span{e_H,u,v}` is

`B_eta=[[-1,eta,0],[eta,2,0],[0,0,2]]`.                          (6.5)

Its eigenvalues are

`2`, `(1+sqrt(9+4eta^2))/2`, `(1-sqrt(9+4eta^2))/2`.             (6.6)

The two positive eigenvalues are at least `2`, and the negative eigenvalue has modulus at least `1`. By the min-max/interlacing theorem for orthogonal compressions, the full matrix in (6.2) therefore has at least two eigenvalues `>=1` and at least one eigenvalue `<=-1`, regardless of the outside couplings. Thus (6.4) is genuinely inside the full target.

Only essential boundedness is asserted from this partner application; no new continuity conclusion is attached to (6.4).

## 7. What this run rules out and what it leaves

The run establishes a useful distinction between three levels of information.

1. **Crude hub-root cap:** replacing the exact values of `f_H` by one destroys the large star `rho`; r41 showed this algebraically.
2. **Hub-star Plancherel averaging:** (2.4)--(3.3) retains the star and is pivot-uniform, but by itself supplies only one half-power of time decay.
3. **Full closure:** the residual rank-two curvature must be combined with the same product structure in the integrated mixed norm (4.4), or by a direct small-ball analogue. A pointwise residual quadratic-phase bound is not available under the owner hypotheses.

Thus the next exact B16 implication is

`QFORM-RANK2-SCHUR-INTEGRATED-FIBER-L2-v1`:

> In the r41 hard exact-rank-three collar, bound the correction-safe quantity
> `integral_{|t|>=1}|t|^(-1/2)||G_t||_2 dt`
> uniformly, where `G_t` is the complex density of the physical-star projection `B=b^T X_J` weighted by the residual quadratic phase. Equivalently, use (4.2) and control the joint `(t,xi)` integral of the affine-twisted residual characteristic function. The proof must retain original-product provenance and may use the source-preserving shear/phase-aligned exits when their exact hypotheses hold.

A source-matching published theorem resolving this precise scope was not found in the sources read this run. No claim of novelty is made.

## 8. Status

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains **OPEN**. The new theorem is a rigorous supporting estimate and an exact reformulation of the remaining projection-product debt; it is not a full solution.

No task, schedule, enablement, notification, email, permission, public release, paid model/API/Codex call, remote workflow, installation, or cross-account authentication was changed.
