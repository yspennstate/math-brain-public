SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B15, 2026-09-23T05:27:13Z.
attacking: quantitative regularity of the newest integrated-Fourier volume branches, after testing and rejecting high-order puncture cancellation as a standalone cure for the free-center two-sheet obstruction.

# account03/B15 auto13 — quantitative Holder/heat regularity compiler for the current volume branches

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Absolute continuity and regularity  
**Status:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE_HOLDER_HEAT_COMPILER / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted universal-height conjecture is **not proved** here. This run deliberately changes mechanism after the preceding annular/punctured-positive-heat runs. It first shows why the quartic zero cannot by itself cure the free-center minority/two-sheet obstruction, then switches to the current original-coordinate integrated-Fourier volume mechanism and extracts a quantitative Holder modulus and an explicit finite-heat-scale approximation rate. No moments, compact support, connected support, log-concavity, Gaussian input, identical-law assumption, or independence after spectral rotation is used.

## 1. Current sources actually applied

The required current volume-stability source is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its q-dependent theorem says: for an ORIGINAL-coordinate cross block `M=A[I,J]`, put

`Z=E3(M)=e3(M^T M)>0`.

If every determinant-volume row marginal satisfies `alpha_i<=q/2`, `1<=q<3/2`, then the actual full quadratic-plus-affine form obeys

`|phi_Q(t)| <= min(1,K |t|^(-b))`,

`b=3/(2q)`,

`K=[e^3 q^(-3/2) pi^3 Z^(-1/2)]^(1/(2q))`,                 (1.1)

and hence has a bounded continuous density. The source keeps all same-bank quadratic terms, outside couplings and affine terms.

The newest three-sample extension actually consumed is

`yspennstate/math-open-problems@d6730c301e46e6337bc3b32e30eb3d04f07dc90b`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T050831Z-account02-B02-QFORM-auto11-f98b4bb5/REPORT.md`.

For the determinant-weighted row-triple law `mu`, if three iid triples have empty common intersection with probability `delta_3>0`, conditioning on that event gives row marginals at most `2/3` and relative entropy at most `log(1/delta_3)`. At `q=4/3` its entropy-tilted version of (1.1) is

`|phi_Q(t)| <= min(1,K_delta |t|^(-9/8))`,                    (1.2)

with

`K_delta <= e^(9/8) (4/3)^(-9/16) pi^(9/8)
             (delta_3 Z)^(-3/16)`.                             (1.3)

The assigned partner result actually applied below is account04/B15:

`yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

For every probability law `nu`, with `H_epsilon=nu*gamma_epsilon` and `M_epsilon=sup_y H_epsilon(y)`, it proves

`sup_(epsilon>0) M_epsilon = ||p_nu||_infinity`,                (1.4)

with value `+infinity` if no bounded density exists; if `p in C_0`, then `M_epsilon` increases to `max p` as `epsilon downarrow0`.

## 2. First attempted missing implication: quartic puncturing does not remove the free-center trace

The previous B15 run produced the exact punctured hierarchy. Test the first stronger member

`kappa_(2,h)(u) = ((u/h)^4/3) gamma_h(u)`.

Let `J=(a,a+h)` be **any** interval and choose the allowed output center

`y=a-h`.

For `z in J`,

`1 < (z-y)/h < 2`.

On `[1,2]` the function `v^4 exp(-v^2/2)` is nondecreasing because its derivative is

`v^3 exp(-v^2/2)(4-v^2)>=0`.

Hence

`kappa_(2,h)(z-y)
 >= exp(-1/2)/(3 sqrt(2 pi) h)`.

Therefore every probability law satisfies the exact lower comparison

`boxed{
 (nu*kappa_(2,h))(a-h)
 >= exp(-1/2)/(3 sqrt(2 pi) h) nu((a,a+h)).
}`                                                               (2.1)

Equivalently,

`nu((a,a+h))
 <= 3 sqrt(2 pi e) h (nu*kappa_(2,h))(a-h)`.                    (2.2)

So the quartic zero at `Q=y` cannot by itself cancel a bad minority/two-sheet interval trace: because `y` is free, any dangerous interval can be moved into the physical region `h<Q-y<2h`, where the quartic punctured kernel is uniformly positive of order `1/h`. This is consistent with the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction. Any cure of that branch must retain product provenance or use another aggregate mechanism. I therefore do **not** spend this run iterating higher puncture orders.

## 3. Fourier envelope implies a quantitative Holder modulus

### Lemma 3.1 — `QFORM-FOURIER-ENVELOPE-HOLDER-v1`

Let `nu` be a probability law with characteristic function satisfying

`|phi(t)| <= min(1,K |t|^(-b))`, `b>1`.                         (3.1)

Then `nu` has a density `p in C_0(R)`. For every

`0<alpha<min(1,b-1)`,

`boxed{
 [p]_(C^(0,alpha))
 <= [2^(1-alpha)/pi]
    [1/(alpha+1)+1/(b-alpha-1)]
    K^((alpha+1)/b).
}`                                                               (3.2)

#### Proof

The envelope is integrable because `b>1`, so Fourier inversion gives a continuous density vanishing at infinity:

`p(x)=(1/(2pi)) int exp(-itx) phi(t) dt`.

For `0<=alpha<=1`,

`|exp(-iu)-1| <= min(2,|u|) <= 2^(1-alpha)|u|^alpha`.

Thus

`|p(x+h)-p(x)|
 <= (2^(1-alpha)/(2pi)) |h|^alpha
    int |t|^alpha |phi(t)| dt`.                                (3.3)

Put `T=K^(1/b)`. Since `alpha<b-1`,

`int_R |t|^alpha min(1,K|t|^-b) dt
 =2 K^((alpha+1)/b)
   [1/(alpha+1)+1/(b-alpha-1)].`                                (3.4)

Substitution in (3.3) proves (3.2). QED.

This is a genuine regularity implication of the **joint integrated-Fourier mechanism**. It does not assert a law-uniform scalar stationary-phase bound.

## 4. New quantitative regularity for the current q=4/3 volume branch

Take `q=4/3`. Then

`b=9/8`.

Choose the explicit exponent

`alpha=1/16 < b-1=1/8`.

Equation (3.2) becomes

`[p]_(C^(0,1/16))
 <= [288*2^(15/16)/(17 pi)] K^(17/18).`                         (4.1)

For the un-tilted current volume theorem, (1.1) gives

`K=e^(9/8)(4/3)^(-9/16)pi^(9/8) Z^(-3/16)`.

Hence

`boxed{
 [p_Q]_(C^(0,1/16))
 <= C_vol Z^(-17/96),
}`                                                               (4.2)

where

`C_vol
 =(288*2^(15/16)/17)
   e^(17/16)(4/3)^(-17/32) pi^(1/16)
 <86.56.`                                                        (4.3)

This strengthens the current source's `C_0` conclusion on the same scope to an explicit positive Holder exponent.

### Near-diffuse stability corollary

In the current volume-stability hypothesis

`M=M0+E`, `s3(M0)>=a`, `max diag(P_range(M0))<=1/2`,
`||E||op<=a/16`,

one has `kappa=s3(M)>=15a/16` and therefore

`Z>=kappa^6`.

So (4.2) yields

`boxed{
 [p_Q]_(C^(0,1/16))
 < 92.70 a^(-17/16).
}`                                                               (4.4)

All arbitrary same-bank and outside quadratic terms allowed by the source remain present.

## 5. New regularity for the three-sample volume compiler

Apply Lemma 3.1 to (1.2)-(1.3). Because `(alpha+1)/b=17/18`, the entropy factor and the volume scale combine exactly to

`boxed{
 [p_Q]_(C^(0,1/16))
 <= C_vol (delta_3 E3(M))^(-17/96)
 <86.56 (delta_3 E3(M))^(-17/96).
}`                                                               (5.1)

Thus the newest three-sample compiler does more than bound height: every branch with `delta_3>0` has a quantitatively Holder continuous density. The blow-up as `delta_3 E3(M)->0` is essential to the scope and makes no claim of a target-uniform modulus over all QFORM instances.

## 6. Equation-level application of the assigned account04/B15 heat theorem

Let `p in C_0` obey a Holder estimate

`|p(x)-p(y)|<=L|x-y|^alpha`.

Since `p` is nonnegative, integrates to one and lies in `C_0`, it attains its maximum at some `y_*`. Let

`M=||p||infinity`,
`M_epsilon=sup_y (p*gamma_epsilon)(y)`.

The assigned account04/B15 theorem gives the exact identity

`M=sup_(r>0) M_r`.                                               (6.1)

Also convolution contraction gives `M_epsilon<=M`, while at `y_*`,

`M-M_epsilon
 <= p(y_*)-(p*gamma_epsilon)(y_*)
 <= L int |u|^alpha gamma_epsilon(u) du`.                        (6.2)

Writing `G~N(0,1)`,

`int |u|^alpha gamma_epsilon(u)du
 =m_alpha epsilon^alpha`,

`m_alpha=E|G|^alpha
 =2^(alpha/2) Gamma((1+alpha)/2)/sqrt(pi)`.                      (6.3)

Combining (6.1)-(6.3) is the actual partner application:

`boxed{
0 <= sup_(r>0) M_r - M_epsilon
   <= m_alpha L epsilon^alpha.
}`                                                               (6.4)

For `alpha=1/16`,

`m_(1/16)=2^(1/32) Gamma(17/32)/sqrt(pi)<0.964`.

Therefore the current q=4/3 volume branch satisfies

`boxed{
0 <= ||p_Q||infinity-M_epsilon(Q)
 <83.39 Z^(-17/96) epsilon^(1/16).
}`                                                               (6.5)

For the near-diffuse stability hypothesis of Section 4,

`boxed{
0 <= ||p_Q||infinity-M_epsilon(Q)
 <89.30 a^(-17/16) epsilon^(1/16).
}`                                                               (6.6)

And the three-sample compiler gives

`boxed{
0 <= ||p_Q||infinity-M_epsilon(Q)
 <83.39 (delta_3 E3(M))^(-17/96) epsilon^(1/16).
}`                                                               (6.7)

This is a quantitative finite-scale heat closure on those live branches, not merely qualitative `C_0` convergence.

## 7. Logical ledger and remaining gap

This run does **not** prove a target-uniform Holder modulus. Such a statement is false even for fixed `A=I_3` by the earlier phase-aligned B15 construction; the constants in (4.2) and (5.1) are allowed to deteriorate as the volume certificate degenerates. There is no conflict.

The full universal height remains open because the bare three-large-eigenvalue hypothesis does not force a uniformly nondegenerate `Z`, a positive uniform `delta_3`, or the near-diffuse cross certificate. The first unpaid structural branches are precisely the low-volume/high-leverage endpoint classes identified by the current volume programme, including coloop/four-row concentration and the product-provenance-sensitive minority/two-sheet geometry.

The new mathematical currency is:

`integrated Fourier exponent 9/8  =>  C^(0,1/16) output regularity
 => explicit heat-height convergence rate epsilon^(1/16)`.

This can be attached to any future proof branch that supplies the same q=4/3 envelope, without repeating a separate output-continuity proof.

The current corrections are respected throughout: no arbitrary-joint rank-three coarea theorem, no conditional projection-density moment, no fiber supremum, no post-rotation independence, no uniformly good single physical minor, and no law-uniform pointwise quadratic-phase decay is used.

## 8. Constants check

The exact numerical constants used above are

`C_vol = (288*2^(15/16)/17) e^(17/16)(4/3)^(-17/32) pi^(1/16)
       = 86.5556132185...`,

`m_(1/16)=0.9633185095...`,

`C_vol*m_(1/16)=83.3806243179...`,

`C_vol*(16/15)^(17/16)=92.6991509523...`,

`C_vol*m_(1/16)*(16/15)^(17/16)=89.2988079308...`.

No numerical computation is used as a substitute for any analytic inequality; these are only evaluations of the displayed exact constants.
