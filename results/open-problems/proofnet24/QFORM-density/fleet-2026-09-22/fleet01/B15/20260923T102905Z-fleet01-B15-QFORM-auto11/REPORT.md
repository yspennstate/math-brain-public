SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-23T10:29:05Z.
attacking: the newest fleet02/B15 random-critical-value posterior bridge; replace worst-minor inversion by the exact ruled-side cost and compile the whole family of gap inequalities into one soft posterior certificate.

# QFORM B15 — harmonic ruled capacity and soft critical-shadowing compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** absolute continuity and regularity  
**Run:** `20260923T102905Z-fleet01-B15-QFORM-auto11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / HARMONIC-RULED-CAPACITY / SOFT-SHADOWING-COMPILER / FULL_TARGET_OPEN`

The unrestricted QFORM conjecture remains **OPEN**. This report applies the latest completed `fleet02/B15` random-critical-value posterior bridge to the exact one-sheet constant rather than the coarse `pi sqrt(2)/sigma_min` bound. The result is a scale-correct harmonic bank parameter and a single bounded soft-gap statistic whose excess above the Gaussian benchmark gives a universal heat-height, hence raw-density, bound. Continuity remains separate.

## 1. Fresh control and premises actually used


The completed assigned-partner result actually applied is `fleet02/B15`, current report

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260923T090720Z-fleet02-B15-QFORM-auto11/REPORT.md`.

Its ambient theorem is as follows. Let `S` be three ORIGINAL coordinates, let `B=A_SS` be invertible indefinite, and condition on the outside original coordinates `W`. Completing the square in the three active original coordinates gives

`Q = c_B(W) + Z^T B Z`,

where the conditional translation preserves the three independent cap-one marginal densities. If `G_B` is the majority/one-sheet event and `mu_B^+` its output submeasure, then

`mu_B^+ <= C_B dx`.                                                   (1.1)

At a global Gaussian heat mode of width `epsilon`, with height `M`, Gibbs posterior `nu`, residual `U=(Q-y_*)/epsilon`, and normalized critical gap

`D_B=(y_*-c_B(W))/epsilon`,

the partner proves, for every `d>0`,

`boxed( nu(D_B>=d) <= C_B/M + exp(-d^2/2). )`                        (1.2)

The same report proves the rough-law passage, so (1.1)-(1.2) do not assume output continuity.

The exact one-sheet source used by the partner gives, for signature `(2,1)` with majority-sign eigenvalue magnitudes `a,b>0` and minority magnitude `r>0`,

`C_B = (a b r)^(-1/2) int_0^(2pi)
       [sin^2(theta)/a + cos^2(theta)/b + 1/r]^(-1/2) dtheta`.       (1.3)

The sign-reversed signature `(1,2)` is identical after replacing `B` by `-B`.

For target-level heat regularity I use the already completed same-slot Gaussian boundary lemma from the immediately preceding actual run: the sharp scaled raw-density constant equals the sharp fixed-unit Gaussian heat-height constant. I do not re-prove it here. Thus it is enough to bound, at `epsilon=1`,

`s_3(A) max_y E gamma_1(Q-y)`.                                       (1.4)

## 2. Exact simplification of the ruled-side cost

Assume without loss that `a<=b`. Multiplying the denominator in (1.3) by `a b r` gives the exact identity

`boxed(
 C_B = int_0^(2pi)
       [a b + a r cos^2(theta) + b r sin^2(theta)]^(-1/2) dtheta.
)`                                                                   (2.1)

Indeed

`a b r [sin^2/a + cos^2/b + 1/r]
 = b r sin^2 + a r cos^2 + a b`.

This exposes the correct homogeneous scale much better than `sigma_min(B)`. Since `b r>=a r`,

`a b + a r cos^2 + b r sin^2 >= a(b+r)`,

hence

`boxed( C_B <= 2 pi / sqrt(a(b+r)). )`                               (2.2)

Define the **ruled conductance**

`rho(B):=sqrt(a(b+r))`.                                               (2.3)

It is homogeneous of degree one in `B`. Equation (2.2) says

`boxed( C_B <= 2 pi/rho(B). )`                                       (2.4)

This strictly refines the coarse partner inequality in anisotropic regimes. If `kappa=min(a,r)` (since `a<=b`), then `rho(B)>=sqrt(2) kappa`, so (2.4) recovers

`C_B <= pi sqrt(2)/kappa`.

When `a=b`, (2.2) is exact: the denominator in (2.1) is the constant `a(a+r)`, so

`C_B=2 pi/sqrt(a(a+r))`.

In particular for `a=b=r=kappa` this is exactly `pi sqrt(2)/kappa`. Thus `rho(B)`, rather than `kappa`, is the natural elementary conditioning scale for the ruled theorem.

A still sharper object is the exact reciprocal cost

`h(B):=1/C_B`.                                                       (2.5)

It is also homogeneous of degree one. From (2.4),

`h(B)>=rho(B)/(2 pi)`.                                                (2.6)

## 3. Harmonic bank aggregation of the newest partner inequality

Let `B_1,...,B_N` be any finite bank of invertible indefinite ORIGINAL-coordinate physical `3x3` blocks in one ambient target. Let

`C_j=C_{B_j}`, `h_j=1/C_j`, `D_j=(y_*-c_j(W_j))/epsilon`.

At one global heat mode, (1.2) holds simultaneously for every block:

`nu(D_j>=d) <= C_j/M + g(d)`,  `g(d)=exp(-d^2/2)`.                  (3.1)

Multiply (3.1) by arbitrary weights `w_j>=0`, `sum w_j=1`, and sum:

`boxed(
 A_w(d):=sum_j w_j nu(D_j>=d)
 <= C_w/M + g(d),
 C_w:=sum_j w_j C_j.
)`                                                                   (3.2)

The optimal algebraic choice for this family is the reciprocal-cost weighting

`w_j=h_j/H`, `H:=sum_j h_j`.                                         (3.3)

Then

`C_w = sum_j (h_j/H) C_j = N/H`.                                    (3.4)

Therefore

`boxed(
 A_h(d) <= N/(M H) + exp(-d^2/2).
)`                                                                   (3.5)

If the bank has mean exact ruled conductance

`H/N >= c s`, `s=s_3(A)`,                                           (3.6)

then

`boxed(
 A_h(d) <= 1/(c s M) + exp(-d^2/2).
)`                                                                   (3.7)

This is an aggregate-before-inversion inequality. It never selects a worst `sigma_min`; weak physical blocks receive proportionally less weight. Using only the elementary parameter (2.3), (2.6) shows that the sufficient bank condition

`(1/N) sum_j rho(B_j) >= 2 pi c s`                                  (3.8)

implies (3.6).

Conversely, if for some `d>0` and `delta>0`

`A_h(d) >= exp(-d^2/2)+delta`,                                      (3.9)

then

`boxed( s M <= 1/(c delta). )`                                      (3.10)

At the fixed unit Gaussian scale, the completed boundary lemma turns (3.10), if established uniformly at every target heat mode, directly into the same universal raw-density bound. No continuity is involved.

## 4. New soft critical-shadowing compiler

The pointwise-in-`d` criterion (3.9) is useful but still asks one to choose a threshold. The entire family can be compressed into a single bounded statistic.

Let `h(d)>=0` be any integrable function on `(0,infinity)`. Define

`Phi_h(z)=int_0^(z_+) h(d) dd`,

and the Gaussian benchmark

`G_h=int_0^infinity h(d) exp(-d^2/2) dd`.                            (4.1)

Integrating (3.2) in `d` and using Tonelli gives

`boxed(
 E_nu sum_j w_j Phi_h(D_j)
 <= (C_w/M) int_0^infinity h(d)dd + G_h.
)`                                                                   (4.2)

Thus every nonnegative `h` supplies a soft gap certificate. The particularly natural choice is

`h_0(d)=d exp(-d^2/2)`,                                              (4.3)

for which

`int_0^infinity h_0(d)dd=1`,

`Phi_{h_0}(z)=1-exp(-(z_+)^2/2)`,

and

`G_{h_0}=int_0^infinity d exp(-d^2) dd = 1/2`.                      (4.4)

Therefore (4.2) becomes the compact inequality

`boxed(
 S_w:=E_nu sum_j w_j [1-exp(-(D_j^+)^2/2)]
 <= 1/2 + C_w/M.
)`                                                                   (4.5)

With the exact harmonic weights (3.3),

`boxed(
 S_h <= 1/2 + N/(M H).
)`                                                                   (4.6)

Under the mean-capacity condition (3.6),

`boxed(
 S_h <= 1/2 + 1/(c s M).
)`                                                                   (4.7)

Consequently, any structural statement forcing the harmonic-weighted soft critical-gap score above the Gaussian benchmark,

`S_h >= 1/2 + delta`,                                                (4.8)

immediately yields

`boxed( s M <= 1/(c delta). )`                                      (4.9)

This is the main new compiler of this run. It reduces the latest partner's continuum of threshold inequalities to one bounded `[0,1]` statistic with the exact benchmark `1/2`. A putative blow-up sequence with `sM->infinity` and nondegenerate mean ruled capacity is forced into the precise **soft-shadowing regime**

`S_h <= 1/2 + o(1)`.                                                 (4.10)

The statistic is source-level and retains the random conditional critical values of the ORIGINAL-coordinate blocks. No projected density or rotated-coordinate independence is substituted.

## 5. Exact-rank-three deterministic-critical-value corollary

For an exact-rank-three affine-completed indefinite law the critical value is deterministic, so `D=(y_*-c)/epsilon` is constant. Equation (4.5) for the single block gives

`1-exp(-(D_+)^2/2) <= 1/2 + C_B/M`.                                 (5.1)

Hence whenever

`D > sqrt(2 log 2)`,                                                 (5.2)

we obtain the explicit total heat-height bound

`boxed(
 M <= C_B / [1/2-exp(-D^2/2)].
)`                                                                   (5.3)

As `D->infinity`, the factor tends to `2`, so a heat mode lying well inside the majority side has total height at most approximately `2 C_B`, despite the unresolved minority/two-sheet raw trace. Therefore any sequence with `M/C_B->infinity` must have its Gaussian mode on the minority side or within `sqrt(2 log2) epsilon` of the cone vertex, consistent with but quantitatively softer than the partner's pointwise trapping theorem.

## 6. Regularity ledger

The logical hierarchy remains:

1. **Absolute continuity:** for any nonzero symmetric `A` and any absolutely continuous joint input law, `X^TAX` is absolutely continuous. Coarea away from the critical subspace `ker A` proves this; independence and the cap are unnecessary.
2. **Bounded density:** the central owner target is quantitative. The immediately preceding B15 Gaussian-boundary result shows it is exactly equivalent, with the same sharp scaled constant, to bounding one fixed unit Gaussian heat height. The present report gives a new sufficient bank criterion for that fixed-height problem.
3. **Regularized smoothness:** for every output law, `gamma_1*mu_Q` is automatically `C^infinity cap C_0`; this is free smoothing, not raw-output continuity.
4. **Raw continuity:** the completed fixed-matrix B15 theorem at its stated source scope gives an instance-dependent bounded `C_0` representative for rank `>=3`. This is a separate stronger qualitative statement and is not used to prove the universal height. The shared CLAIMS projection still lists the global continuity claim as OPEN, so no shared claim status is edited here.

## 7. Exact remaining implication

The full theorem would follow from a structural result of the following form at each fixed-unit global Gaussian mode:

- build a finite bank of original-coordinate indefinite physical `3x3` blocks for which the mean exact ruled capacity satisfies `(1/N) sum_j h(B_j) >= c s_3(A)` for a universal `c>0`; and
- prove the harmonic-weighted soft critical-gap score satisfies `S_h>=1/2+delta` for a universal `delta>0`, OR route the complementary `S_h<=1/2+delta` shadowing class into an already-paid product-sensitive ridge/volume/grouped-coordinate exit.

The elementary sufficient capacity condition is `(1/N) sum rho(B_j) >= 2 pi c s_3(A)`, with `rho(B)=sqrt(a(b+r))`. Near-singular `sigma_min` alone no longer forces the ruled cost to be large when the other two curvature scales compensate.

What remains genuinely unpaid is the structural control of the shadowing class. The live two-sheet X-ray correction prevents replacing it by a generic projection estimate; product provenance must remain in the argument.

**Full QFORM status: OPEN / NOT PROVED / NOT DISPROVED.**
