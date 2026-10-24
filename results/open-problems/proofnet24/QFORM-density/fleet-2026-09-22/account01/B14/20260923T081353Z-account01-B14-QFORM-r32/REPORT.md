SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T08:13:53Z.
attacking: fixed-mass subprobability localization before reciprocal payment; preserve exact mass homogeneity while removing support, tail, fragment-geometry and translation restrictions.

# QFORM-FIXED-MASS-EXTREME-LOCALIZATION-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account01/B14`  
Run: `20260923T081353Z-account01-B14-QFORM-r32`  
Status: **PROVED SUPPORTING SUBPROBABILITY LOCALIZATION THEOREM + TARGET-VALID PARTNER APPLICATION; FULL QFORM OPEN.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source-pinned partner inputs

The full target remains open: independent real inputs with densities at most one, arbitrary real symmetric `A`, at least three eigenvalues of modulus at least one, and no support, moment, centering, connectedness, log-concavity, identical-law or post-rotation-independence assumption.

This run changes mechanism from the preceding unit-mass probability localization to **fixed-mass subprobability localization**. That is the right interface for reciprocal-volume and fragment estimates: it removes arbitrary support geometry without changing the subprobability masses that carry the analytic homogeneity.

Two completed account02/B14 results are used at equations:

1. `QFORM-DK-SUBPROBABILITY-HOMOGENEITY-v1`, account02/B14 r27, canonical source `yspennstate/math-open-problems@8f29d24c80043bd45bcd1c6e8957760f048c98ff`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T070336Z-account02-B14-QFORM-r27/REPORT.md`.
2. Newest completed partner result `QFORM-DIAGONAL-TWISTED-SCHUR-BANK-v1`, account02/B14 r31, canonical source `yspennstate/math-open-problems@57f120e5d7ea0f9c885bf6286d5227812357a382`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T080010Z-account02-B14-QFORM-r31/REPORT.md`.

No uniform pointwise quadratic Fourier decay, arbitrary-joint coarea bound, positive moment of a worst conditional projection cap, bounded-diameter localization, fixed fragment-count localization, or post-rotation independence is used.

## 2. One-dimensional fixed-mass extreme localization

For `m in (0,1]`, define

`D_m={f in L1(R): 0<=f<=1 a.e., integral f=m}`.

Let `F_m` be the class of subdensities `1_E` where `E` is a bounded finite union of intervals and `|E|=m`.

### Theorem 2.1

For every `f in D_m` and every `epsilon>0`, there exist finitely many weights

`theta_s>=0,   sum_s theta_s=1`,

and sets `E_s in F_m` such that

`boxed( ||f-sum_s theta_s 1_(E_s)||_1 < epsilon. )`              (2.1)

The mass `m` is preserved in every extreme component. There is no common support-radius, fragment-count, fragment-separation, tail or moment parameter.

### Proof

Choose `R` so that

`tau=int_(|x|>R) f(x)dx < epsilon/8`.                            (2.2)

Choose a bounded interval `J` of length `tau`, disjoint from `[-R,R]`, and put

`g=f 1_[-R,R]+1_J`.                                               (2.3)

If `tau=0`, omit `J`. Then `0<=g<=1`, `integral g=m`, `g` has bounded support, and

`||f-g||_1 <= 2 tau < epsilon/4`.                                (2.4)

Fix a large integer `N` and set `delta=m/N`. Average `g` on the uniform grid of cells of length `delta`. Because `g` is compactly supported, the resulting step function has only finitely many nonzero cells,

`s_N=sum_(r=1)^M a_r 1_(I_r),   0<=a_r<=1`,                      (2.5)

and

`delta sum_r a_r = integral s_N =m`, hence `sum_r a_r=N`.         (2.6)

Uniform-grid conditional expectations converge to `g` in `L1`; choose `N` so that `||s_N-g||_1<3epsilon/4`.

Now

`a=(a_1,...,a_M)` lies in `P={a in [0,1]^M: sum a_r=N}`.          (2.7)

Every extreme point of `P` is a `0-1` vector with exactly `N` ones: two fractional coordinates admit a small opposite perturbation, while exactly one fractional coordinate is incompatible with the integer sum. Thus

`a=sum_s theta_s v^(s)`                                          (2.8)

with each `v^(s)` selecting exactly `N` cells. Let

`E_s=union_(r:v_r^(s)=1) I_r`.                                  (2.9)

Then `|E_s|=N delta=m` and

`s_N=sum_s theta_s 1_(E_s)`.                                    (2.10)

Equations (2.4)-(2.10) prove (2.1). QED.

The construction is translation-covariant: translating `f` only translates the chosen compact approximation and the final sets. Therefore arbitrary shifts cost zero.

## 3. Product fixed-mass theorem and exact small-ball envelope

Fix masses `m_1,...,m_d in (0,1]`. For arbitrary `f_i in D_(m_i)`, apply Theorem 2.1 coordinatewise. Since every factor has `L1` norm at most one, the telescoping product estimate gives

`||prod_i f_i-prod_i g_i||_1 <= sum_i ||f_i-g_i||_1`.            (3.1)

Expanding `prod_i g_i` is a finite convex mixture of product submeasures

`prod_i 1_(E_i)(x_i) dx`, with `|E_i|=m_i` for every component.  (3.2)

Let `F_theta:R^d->R` be any measurable parameter family and define

`SB(mu)=sup_(theta,t,h>0) mu{F_theta in [t,t+h]}/h`.              (3.3)

For each fixed `(theta,t,h)`, the quotient is continuous in total variation; hence `SB` is lower semicontinuous and convex. Therefore

`boxed(
 sup_(0<=f_i<=1, int f_i=m_i) SB(prod_i f_i dx)
 =sup_(E_i bounded finite-union, |E_i|=m_i)
   SB(prod_i 1_(E_i) dx).
)`                                                                  (3.4)

Equality holds in the extended nonnegative reals and preserves the optimal constant exactly.

### Consequence: exact mass-homogeneity preservation

Suppose a theorem on the extreme side has the form

`mu{F_theta in J} <= C H(m_1,...,m_d) |J|`                         (3.5)

uniformly in all translations and all finite-union geometries. Then (3.4) gives the identical estimate for **every** cap-one product subdensity with those masses, with exactly the same function `H`.

Thus localization can remove arbitrary tails, remote fragments and support geometry while preserving every mass exponent exactly. The only remaining fragment tax is the tax caused by **splitting the masses themselves** and summing separate analytic certificates. This cleanly separates support geometry from analytic subprobability homogeneity.

The same argument permits an arbitrary random outside environment `omega` and measurable affine parameters generated by conditioning: include `omega` in the outer probability space and apply the mixture only to the active original-coordinate product measure.

## 4. Equation-level application of account02/B14 r27

Use its `D_5` specialization with original-coordinate cross block `M=I_5`. Let the five row subdensity masses be `m_i` and the five column subdensity masses be `n_j`. Here `k=5`, `q=2`, `Z_5=1`, and the volume marginals are `alpha_i=beta_j=1`. The completed partner theorem gives

`boxed(
 ||p_(Q#nu)||_infinity
 <=5 sqrt(2e)
   prod_(i=1)^5 m_i^(4/5)
   prod_(j=1)^5 n_j^(4/5),
)`                                                                  (4.1)

for

`Q(u,v)=2 u^T v +` arbitrary self-block and affine terms allowed by the partner theorem.                 (4.2)

The new Theorem 3.4 shows that (4.1), including every exponent `4/5`, can be checked on bounded finite-union indicator subdensities of measures exactly `m_i,n_j` and then transferred to arbitrary unbounded/remote-fragment subdensities with **zero additional factor**.

This does not erase the partner's genuine `N^2` fragment-first obstruction. If every active coordinate is split into `N` pieces of mass `1/N`, summing (4.1) over all cells still creates the exact `N^2` loss proved in r27. What Theorem 3.4 proves is that, at each fixed mass vector, support geometry itself contributes no further loss.

## 5. Actual target-valid inequality from the newest completed partner r31

Let `U=(U_1,U_2)` and `V=(V_1,...,V_N)` be original independent cap-one coordinates, let `Z` be any disjoint block of additional independent cap-one coordinates, and let `a in R^N` satisfy

`||a||_2=1,   c=max_i a_i^2 <=1/2`.                              (5.1)

Let `D` be arbitrary diagonal with `||D||_op<=1/20`, and let `G,H,K` be arbitrary matrices of compatible sizes with `K=K^T`. Consider

`Q=4 U_1 U_2 + V^T(D+2aa^T)V`
`  +2 U^T G Z +2 V^T H Z + Z^T K Z`                              (5.2)

(and arbitrary additional affine/constant terms).

The corresponding physical pair block is

`B=[[0,2],[2,0]]`, so `|det B|=4` and `sigma_min(B)=2`.          (5.3)

Because the raw `U-V` block is zero, the `V-V` block of the Schur complement is exactly

`D+2aa^T`.                                                       (5.4)

Thus partner r31 applies with `lambda=2`, `s=2`, and `eta(c)=1`. Its constant

`C_*=4 sqrt(2 C0)=17.9359917518...`                              (5.5)

therefore yields, after conditioning on the arbitrary outside original coordinates `Z`,

`boxed( ||p_Q||_infinity <= C_*/2 < 8.969. )`                    (5.6)

This is uniform in `N`, all cap-one laws, arbitrary translations, arbitrarily distant fragments, unbounded supports, and all moments.

The family is genuinely inside the exact target. The principal `U,V` block is the direct sum of `B` and `D+2aa^T`. It has eigenvalues `+2,-2` from `B`, while Weyl gives

`lambda_max(D+2aa^T) >= 2-1/20 >1`.                              (5.7)

Hence that principal block already has three eigenvalues of modulus greater than one. Cauchy interlacing preserves the existence of the required positive/negative large eigenvalues after the completely arbitrary outside couplings `G,H,K` are added. Equation (5.6) is therefore a target-valid full-ambient inequality, not merely a rank-three toy model.

## 6. Localization conclusion and remaining debt

This run pays a sharper law-level debt than the preceding unit-mass localization:

- probability localization can be done **at each prescribed subprobability mass vector**;
- every analytic mass exponent survives unchanged;
- support truncation, arbitrary translations, unbounded tails, remote fragment geometry and fragment count cost zero;
- mass splitting itself can still be expensive, and r27's exact `N^2` loss remains a genuine proof-order obstruction.

The safe order is therefore:

`whole active mass / aggregate certificate -> reciprocal curvature or volume payment -> outside conditioning / averaging -> only then optional law decomposition`.

The full QFORM conjecture is still OPEN. The first unpaid implication is matrix/analytic: from bare `s_3(A)>=1`, expose before active-mass splitting either a whole-law D'/D5/near-diffuse volume certificate, a diagonal-plus-capped-leverage Schur-bank certificate of r31, a ridge/mixed-hub/core certificate, or a new mass-restoring estimate. Arbitrary dense nonseparable Schur curvature and the absence of a uniformly good physical pair remain outside the theorems above.

Independent end-to-end review of the full conjecture is not claimed; this is a supporting localization theorem plus a target-valid application of completed partner results.
