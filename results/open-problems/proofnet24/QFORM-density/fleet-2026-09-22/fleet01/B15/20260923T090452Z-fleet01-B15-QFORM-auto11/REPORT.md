SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-23T09:04:52.956233Z.
attacking: absolute-continuity versus L-infinity separation at a fixed regularization scale; use the latest fleet02/B15 ruled-side Gaussian-mode estimate inside an actual source-level inequality and isolate exactly what continuity can and cannot supply.

# B15 — ambient ruled-bank compiler and exact essential/continuous-height equivalence

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Role:** absolute continuity and regularity  
**Run:** 20260923T090452Z-fleet01-B15-QFORM-auto11  
**Execution:** WITHOUT_VERIFIED_BRAIN  
**Status:** ESSENTIAL_STEP_APPLIED / AMBIENT-RULED-BANK-COMPILER / FULL_TARGET_OPEN

The unrestricted QFORM conjecture remains **OPEN**. This report proves a target-level regularity/rough-law compiler that is safe under arbitrary outside couplings and random conditional critical values. It also shows that, once the separately completed fixed-instance C0 theorem is accepted at its stated scope, the optimal universal essential-density constant and the optimal pointwise continuous-density constant are exactly the same. Continuity is therefore not a second quantitative loss.

## 1. Sources and corrections actually used


The following completed mathematical sources are applied below.

1. **Latest assigned partner fleet02/B15:** `yspennstate/math-open-problems@67477971f11369e3ce0bdb54f6c7ddbf18812fa5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260923T083434Z-fleet02-B15-QFORM-auto11/REPORT.md`. It independently checks the rough one-sheet theorem and proves that for an invertible indefinite original-coordinate 3x3 physical block B, after conditioning on arbitrary outside original coordinates and completing the square, the majority-side output submeasure has density at most `pi sqrt(2)/kappa`, where `kappa=sigma_min(B)`. Its exact-rank-three Gaussian heat-mode estimate cannot simply be averaged over conditioned blocks because the conditional critical value is random.

2. **Completed fixed-instance regularity source:** fleet02/B15 `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T200544Z-fleet02-B15-qform-r11/REPORT.md`, together with its consumed fleet03/B15 nonzero-diagonal theorem `d73760eb784a86c356c64f05dd92f84655618f02`. At its stated source scope it proves: for every fixed symmetric A with rank(A)>=3 and every cap-one product source, the output density has an instance-dependent bounded representative in C0(R). The shared CLAIMS.json has not been consolidated to this source theorem and still labels the global continuous-representative claim OPEN; I therefore do not edit shared claim status here.

The proof below uses none of the refuted interfaces: no law-uniform pointwise quadratic Fourier decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea height theorem, no conditional projection-cap positive moment, no fiber-supremum shortcut, and no projection/X-ray-only estimate for the two-sheet side.

## 2. Absolute continuity is qualitatively much weaker

For completeness, let A be any nonzero real symmetric matrix and let X have any absolutely continuous joint law; independence and the density cap are unnecessary here. Put q(x)=x^T A x. If N is a Lebesgue-null subset of R, apply coarea on

`E_k={x: |x|<=k, |grad q(x)|>=1/k}`.

Then

`int_{E_k cap q^{-1}(N)} |grad q(x)| dx
 = int_N H^{n-1}(E_k cap q^{-1}(t)) dt = 0`,

so `Leb(E_k cap q^{-1}(N))=0`. The complement of the union of E_k is contained, up to a null set, in the critical space `ker A`, which is a proper subspace. Hence `q^{-1}(N)` is null and `q(X)` is absolutely continuous.

This establishes only existence of a density. It contains no L-infinity information.

## 3. Exact essential-height / continuous-height equivalence

Assume the completed fixed-instance C0 theorem at the source scope above. For every owner-target instance, let p_Q denote its continuous C0 representative. A continuous function has

`sup_t p_Q(t) = ess sup_t p_Q(t)`.

Indeed, if `p_Q(t0)>C`, continuity makes `p_Q>C` on an interval of positive measure. Therefore, defining over the full owner target class

`C_ess = sup ||p_Q||_{L^infinity(ess)}`

and

`C_cont = sup max_t p_Q(t)`,

we obtain the exact identity, allowing `+infinity`,

`boxed( C_ess = C_cont. )`                                      (3.1)

The same statement holds in the scale-invariant normalization:

`sup s_3(A)||p_Q||_{L^infinity(ess)}
 = sup s_3(A) max_t p_Q(t)`.

Thus the qualitative continuity theorem and the quantitative universal-height theorem are logically separate, but **there is no extra quantitative constant to pay for continuity**. Once the universal essential bound is proved, the already-available C0 representative automatically obeys the same pointwise bound. Conversely a pointwise continuous bound trivially gives the essential one.

This is the correct way to combine continuity with the target: continuity is a post-processing/representative theorem, not the mechanism that generates the universal height.

## 4. Original-coordinate physical block and its random critical value

Let S be an ORIGINAL-coordinate set of three indices such that

`B=A_{S,S}`

is invertible indefinite. Put

`kappa_S=sigma_min(B)>0`.

Write `W=X_{S^c}`. Conditional on `W=w`, the full quadratic form is

`Q = X_S^T B X_S + 2 X_S^T A_{S,S^c} w + w^T A_{S^c,S^c} w`.

Complete the square only in the original active coordinates:

`Z_S = X_S + B^{-1}A_{S,S^c}w`,

`Q = c_S(w) + Z_S^T B Z_S`,

where

`c_S(w)=w^T[A_{S^c,S^c}-A_{S^c,S}B^{-1}A_{S,S^c}]w`.

Conditional translation preserves independence and each density cap one. Let `sigma_S` be the multiplicity-two sign of B (`+1` for signature (2,1), `-1` for signature (1,2)) and define the majority event

`M_S={ sigma_S (Q-c_S(W)) >= 0 }`.

Define the majority output submeasure

`nu_S^+(E)=P(Q in E, M_S)`.

The completed fleet02/B15 rough one-sheet theorem applies conditionally for every w and survives averaging. Hence, for every interval I,

`boxed( nu_S^+(I) <= C_S |I|,   C_S <= pi sqrt(2)/kappa_S. )`   (4.1)

Equivalently, `nu_S^+ <= C_S dx` as measures. This is a rough-law statement; no output continuity is used.

## 5. New ambient tent inequality — safe with random critical values

For `eps>0` and center t define the normalized triangular kernel

`K_{eps,t}(u)=eps^{-2}(eps-|u-t|)_+`.

It is nonnegative and integrates to one. Measure domination (4.1) immediately gives

`boxed( E[K_{eps,t}(Q) 1_{M_S}] <= pi sqrt(2)/kappa_S. )`       (5.1)

Therefore

`boxed(
 E K_{eps,t}(Q)
 <= pi sqrt(2)/kappa_S
    + E[K_{eps,t}(Q) 1_{M_S^c}].
)`                                                            (5.2)

Multiplying by `s=s_3(A)` gives the scale-invariant form

`boxed(
 s E K_{eps,t}(Q)
 <= pi sqrt(2) s/kappa_S
    + s E[K_{eps,t}(Q) 1_{M_S^c}].
)`                                                            (5.3)

This is the promised actual application of the completed partner result to the live density functional. It is stronger in ambient scope than trying to average the partner's exact-rank-three global-heat-mode inequality: here the random conditional critical value `c_S(W)` is harmless because the one-sheet domination is applied **before** averaging. No statement that a global mode is a conditional mode is required.

The first unpaid local quantity after choosing B is now exactly the product-provenance-sensitive minority/two-sheet tent term on the right of (5.3).

## 6. New weighted bank compiler: aggregate before reciprocal payment

The same argument can be averaged over many physical blocks before paying their inverse conditioning constants.

Let `S_1,...,S_N` be any finite collection of invertible indefinite original-coordinate three-blocks, with

`kappa_j=sigma_min(A_{S_j,S_j})`,

majority events `M_j` as in Section 4, and arbitrary weights `w_j>=0`, `sum_j w_j=1`. Set

`F_{eps,t}=E K_{eps,t}(Q)`.

When `F_{eps,t}>0`, introduce the positive tent posterior

`dP_{eps,t}=K_{eps,t}(Q)dP/F_{eps,t}`

and its weighted majority coverage

`alpha_bar_{eps,t}=sum_j w_j P_{eps,t}(M_j)`.

Averaging (5.1) gives the exact inequality

`boxed(
 F_{eps,t} alpha_bar_{eps,t}
 <= pi sqrt(2) sum_j w_j/kappa_j.
)`                                                            (6.1)

Consequently, whenever the bank has posterior majority coverage

`alpha_bar_{eps,t} >= delta > 0`,

we obtain

`boxed(
 F_{eps,t}
 <= (pi sqrt(2)/delta) sum_j w_j/kappa_j.
)`                                                            (6.2)

This already avoids selecting one worst physical minor. A particularly useful choice is

`w_j = kappa_j / Kappa`,  `Kappa=sum_j kappa_j`.

Then

`sum_j w_j/kappa_j = N/Kappa`,

so

`boxed(
 F_{eps,t} <= pi sqrt(2) N/(delta sum_j kappa_j).
)`                                                            (6.3)

If the bank has aggregate conditioning

`(1/N) sum_j kappa_j >= c s_3(A)`

and posterior majority coverage at least delta, then

`boxed(
 s_3(A) F_{eps,t} <= pi sqrt(2)/(c delta).
)`                                                            (6.4)

Equation (6.4) is a genuine **aggregate-before-inversion certificate**. It converts two structural statements — average physical conditioning and average majority coverage — into a universal density-scale tent bound. It is compatible with arbitrary outside self-blocks/couplings and arbitrary rough/unbounded cap-one marginals.

A stronger deterministic sufficient condition is pointwise weighted majority coverage

`sum_j w_j 1_{M_j}(x) >= delta` for every relevant x.

Then `alpha_bar>=delta` for every positive output kernel automatically, so (6.2) holds at every center and scale. A weaker posterior-only coverage statement is sufficient and may be more realistic.

The full conjecture is not closed because the bare three-large-eigenvalue hypothesis has not yet been shown to force a bank satisfying both aggregate conditioning and nontrivial majority coverage. The N3 corrections also rule out simply asserting one uniformly conditioned physical block.

## 7. Pointwise regularity compiler from the tent inequality

Now use the separately completed C0 theorem only as a qualitative representative result. Since `p_Q` is continuous,

`lim_{eps downarrow0} E K_{eps,t}(Q)=p_Q(t)` for every t.

Thus (5.2) yields the pointwise inequality

`boxed(
 p_Q(t)
 <= pi sqrt(2)/kappa_S
    + limsup_{eps downarrow0} E[K_{eps,t}(Q)1_{M_S^c}].
)`                                                            (7.1)

Likewise, if a fixed bank has `liminf_{eps downarrow0} alpha_bar_{eps,t}>=delta`, then (6.2) gives the same pointwise bound at t. Continuity is used only to identify the every-point representative with the approximate-identity limit. The numerical height still comes entirely from the rough one-sheet measure domination and the remaining minority estimate.

For a whole exact rank-three affine-completed law, `c_S(W)` is deterministic (`c`). Then the majority and minority submeasures live on opposite sides of c. The partner's essential one-sheet bound plus C0 continuity therefore upgrades to

`boxed( p_Q(t) <= pi sqrt(2)/kappa  for every t on the majority closed half-line, including t=c. )`  (7.2)

Hence an exact-rank-three sequence whose normalized density heights diverge cannot blow up at the cone vertex or anywhere on the majority side; any such divergence must occur strictly on the minority/two-sheet side. This is an every-point conclusion, but it does not remove the two-sheet problem.

## 8. Why this does not smuggle in a uniform continuity modulus

The completed fleet02/B15 high-frequency construction at fixed `A=I_3` gives smooth cap-one inputs with uniformly bounded output heights yet no target-uniform continuity/translation/Besov modulus. Therefore (3.1) and (7.1) must not be misread as a quantitative continuity estimate. The C0 theorem is instancewise; it merely chooses the canonical continuous representative.

In particular, a proof of the full universal height should continue to target the positive source-level tent/small-ball quantity directly. There is no need, and in general no possibility, to derive a law-uniform output modulus first.

## 9. Precise remaining implication

This run changes the local proof obligation as follows.

For any surviving class admitting a bank of invertible indefinite original-coordinate 3-blocks, it is enough to establish one of:

1. a uniform lower bound on weighted majority coverage under the tent posterior together with a lower bound on the bank's mean `kappa_j/s_3(A)`; or
2. a direct universal bound on the weighted minority/two-sheet term in (5.3)/(6.1), while retaining original-coordinate product provenance.

Existing diffuse-volume/ridge exits can be used before this bank step. The difficult low-tail/high-leverage/N3 survivors still need structural glue. The X-ray-only correction remains active: generic projected line-density control cannot replace the product-sensitive minority term.

**Full QFORM status: OPEN / NOT PROVED.**
