SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T05:02:59Z.
attacking: remove continuity entirely from the sharp reduction; replace the two-sided annulus by one fixed one-sided unit window / smooth positive probe arbitrarily far from the quadratic critical value, then apply the completed account02/B15 ambient one-sheet bound to that exact functional.

# account01/B15 auto11 — exact one-sided fixed-window and smooth-probe normal forms without continuity

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** absolute continuity and regularity  
**Run:** `20260923T050259Z-account01-B15-QFORM-auto11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_ONE_SIDED_FIXED_WINDOW / CONTINUITY_REMOVED_FROM_SHARP_REDUCTION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope

Let

`Q_A = X^T A X`,

where the original coordinates of `X` are independent and have probability densities `0<=f_i<=1`. Let

`s(A)=s_3(A)`

be the third largest eigenvalue modulus. The owner target is the class `s(A)>=1` and asks whether

`C_* := sup ||p_A||_infinity < infinity`

for one universal finite constant.

This run proves a sharper exact normal form than my preceding fixed-annulus result. The sharp constant can be tested on **one fixed unit interval lying arbitrarily far on the positive side**, and the proof uses only absolute continuity plus Lebesgue differentiation. The fixed-target `C_0` theorem is therefore not needed for the sharp reduction at all; continuity remains a genuinely separate stronger conclusion.

A smooth fixed positive probe supported inside that same unit interval gives the identical sharp constant. This gives a target-level regularity interface with no shrinking scale, no cone vertex, no discontinuous indicator kernel, and no continuity premise.

The full universal height theorem remains OPEN.

## 2. Completed account02/B15 premises actually used

### 2.1 Absolute continuity at the exact minimal qualitative threshold

Completed `account02/B15`, run

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T170424Z-account02-B15-qform-r5/REPORT.md`

proves:

> if `A!=0` and the input law is absolutely continuous on `R^n`, then `X^TAX` is absolutely continuous.

Its proof is local inverse-function/coarea away from `ker A`; no boundedness or continuity is inferred. Since the owner target has rank at least three, this applies to every target instance.

### 2.2 Ambient physical-three-block one-sheet theorem

Completed assigned partner `account02/B15`, run

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T030440Z-account02-B15-QFORM-auto11/REPORT.md`, Theorem 6.1,

states the following. If an ORIGINAL-coordinate physical principal block `B=A[I,I]`, `|I|=3`, is invertible of signature `(2,1)` or `(1,2)`, and

`kappa=sigma_min(B)`,

then after conditioning on the outside original coordinates and completing the square only in `X_I`, the majority-sign one-sheet submeasure has interval density at most

`pi sqrt(2)/kappa`,

uniformly in every outside quadratic coefficient and cross coupling.

I apply that theorem below to the exact one-sided unit-window and smooth-probe inequalities.

## 3. Spectral homogeneity of the sharp constant

For `a>0`,

`Q_(aA)=aQ_A`,
`p_(aA)(t)=a^(-1)p_A(t/a)`,
`s(aA)=a s(A)`.

Hence

`boxed{ C_* = sup_(target A,f) s(A) ||p_A||_infinity. }`             (3.1)

Indeed, if `s=s(A)>=1`, then `B=A/s` has `s(B)=1` and

`||p_B||_infinity=s||p_A||_infinity`.

Thus the supremum over the normalized subclass `s(A)=1` already equals `C_*`.

No continuity is used here.

## 4. Main theorem: one fixed one-sided unit interval is exact

For `R>0`, define

`W_R(A,f,y)=s(A) P{ y+1 < Q_A < y+2 },   y>=R`.

### Theorem 4.1 — `QFORM-ONE-SIDED-FIXED-WINDOW-v1`

For every fixed `R>0`,

`boxed{
 C_* = sup_(target A,f; y>=R)
       s(A) P{ y+1 < X^TAX < y+2 }.
}`                                                                  (4.1)

The equality is in `[0,+infinity]` and uses only absolute continuity of each target output.

In particular, taking `R=4`, every tested output value lies in `(5,infinity)`: the full sharp theorem is exactly equivalent to a unit-window small-ball bound uniformly separated from the unique critical output value `0` of the homogeneous quadratic map.

### Proof: upper bound

By the account02/B15 absolute-continuity theorem every target output has a density `p_A`. Therefore

`P{y+1<Q_A<y+2} <= ||p_A||_infinity`.

Multiplying by `s(A)` and using (3.1),

`s(A)P{y+1<Q_A<y+2} <= C_*`.

So the right side of (4.1) is at most `C_*`.

### Proof: reverse bound by one-sided Lebesgue differentiation

It is enough to work in the normalized class `s(A)=1`.

Fix one normalized target density `p`. Let `M=||p||_infinity`, allowing `M=+infinity`. For every finite `L<M`, the set

`E_L={t:p(t)>L}`

has positive Lebesgue measure. Almost every point is a Lebesgue point of `p`, and the singleton `{0}` has measure zero, so choose a nonzero Lebesgue point `t in E_L`.

If `t<0`, replace `A` by `-A`. This preserves `s(A)=1`, and the reflected density satisfies `p_-(u)=p(-u)`, so `-t>0` is a Lebesgue point with the same value. Thus assume `t>0`.

At a Lebesgue point,

`(1/r) int_(t+r)^(t+2r) p(u)du -> p(t)`                             (4.2)

as `r downarrow0`. Indeed,

`(1/r) int_(t+r)^(t+2r) |p(u)-p(t)|du`
` <= (1/r) int_t^(t+2r) |p(u)-p(t)|du`
` = 2 * [(1/(2r)) int_t^(t+2r)|p(u)-p(t)|du] ->0`.

Choose `r<min(1,t/R)`, set

`A_r=A/r`, `y=t/r`.

Then `s(A_r)=1/r>=1`, `y>=R`, and

`s(A_r) P{y+1<Q_(A_r)<y+2}`
` = (1/r) P{t+r<Q_A<t+2r}`
` = (1/r) int_(t+r)^(t+2r) p(u)du`
` -> p(t)>L`.                                                       (4.3)

Thus the right side of (4.1) is at least every `L<M`. Taking `L up to M`, then taking the supremum over normalized target instances, proves (4.1). If `C_*=+infinity`, apply the same argument with arbitrarily large finite `L`.

QED.

### Consequence

My preceding two-sided annulus theorem

`(s/2) P{1<|Q-y|<2}`

is not needed. A single one-sided unit interval already carries the exact sharp constant. More importantly, the earlier use of the partner's `C_0` theorem to move an attained maximum away from zero is unnecessary: a near-maximal nonzero Lebesgue point always exists at the essential-supremum level.

This is the cleanest separation obtained so far between the central `L^infinity` problem and the stronger continuity statement.

## 5. Smooth fixed-probe normal form, still with the same sharp constant

The same proof gives a regularized version with no indicator discontinuity.

Fix once and for all any nonnegative `psi in C_c^infinity((1,2))` satisfying

`int_R psi(u)du=1`.

For a target instance define

`F_psi(A,f,y)=s(A) E psi(Q_A-y)`.

### Theorem 5.1 — `QFORM-FIXED-SMOOTH-FAR-PROBE-v1`

For every fixed `R>0`,

`boxed{
 C_* = sup_(target A,f; y>=R)
       s(A) E psi(X^TAX-y).
}`                                                                  (5.1)

In particular, for `R=4` the probe only sees outputs in `(5,6)` translated by the free far center: if `psi(Q-y)!=0`, then `Q in (y+1,y+2) subset (5,infinity)`.

### Proof

The upper bound is immediate from absolute continuity and `int psi=1`:

`E psi(Q-y)=int psi(u-y)p(u)du <= ||p||_infinity`.

For the reverse direction use the same normalized target and nonzero positive Lebesgue point `t`. With `A_r=A/r`, `y=t/r`,

`s(A_r) E psi(Q_(A_r)-y)`
` = (1/r) int psi((u-t)/r)p(u)du`
` = int psi(v)p(t+rv)dv`.                                          (5.2)

Because `psi` is bounded and supported in `(1,2)`, the Lebesgue-point property gives

`int psi(v)p(t+rv)dv -> p(t) int psi(v)dv = p(t)`.                 (5.3)

Explicitly,

`|int psi(v)(p(t+rv)-p(t))dv|`
` <= ||psi||infinity (1/r) int_(t+r)^(t+2r)|p(u)-p(t)|du ->0`.

The same essential-supremum argument as in Theorem 4.1 proves (5.1).

QED.

### Interpretation

The exact universal height problem can therefore be attacked with one **fixed, positive, smooth, compactly supported test function at one fixed output scale**. The shrinking-scale parameter has been absorbed into the matrix homogeneity `A -> A/r`; the center can simultaneously be forced arbitrarily far from the critical value.

No target-uniform approximate-identity convergence is asserted or needed. This is consistent with account02/B15's fresh obstruction showing that annular/Gaussian approximate identities do not converge uniformly over the target class.

## 6. Actual application of the completed account02/B15 one-sheet theorem

Let an admissible ambient matrix contain an invertible ORIGINAL-coordinate `3 x 3` principal block `B` of signature `(2,1)` or `(1,2)`, and put

`kappa=sigma_min(B)`.

As in the completed partner theorem, condition on the outside original coordinates `W` and complete the square only in the three physical coordinates. Let `Maj` denote the resulting conditional majority-sign one-sheet event and `Min` its complement.

The partner theorem gives an averaged majority submeasure `nu_Maj` satisfying

`nu_Maj(I) <= (pi sqrt(2)/kappa)|I|`

for every interval `I`; equivalently it has an essential density bounded by `pi sqrt(2)/kappa`.

### Unit-window application

Taking `I=(y+1,y+2)` gives the actual inequality

`boxed{
 s(A) P{y+1<Q_A<y+2}
 <= pi sqrt(2) s(A)/kappa
    + s(A)P{y+1<Q_A<y+2, Min}.
}`                                                                  (6.1)

Thus if `kappa>=c s(A)`, the entire majority contribution to the **exact sharp fixed-window functional** is paid by `pi sqrt(2)/c`.

### Smooth-probe application

Since `psi>=0`, `int psi=1`, and `d nu_Maj/dt <= pi sqrt(2)/kappa`,

`E[psi(Q_A-y) 1_Maj]`
` = int psi(t-y) dnu_Maj(t)`
` <= pi sqrt(2)/kappa`.

Hence

`boxed{
 s(A) E psi(Q_A-y)
 <= pi sqrt(2) s(A)/kappa
    + s(A) E[psi(Q_A-y)1_Min].
}`                                                                  (6.2)

This is an equation-level application of the assigned partner result to the new exact smooth normal form. It preserves arbitrary outside curvature/cross couplings and never rotates the product law.

For a definite physical `3 x 3` block, the earlier completed local B15 theorem instead pays the full probe by its matrix-dependent density certificate; no minority branch appears.

## 7. Exact regularity ledger after this run

The source-valid implications are now especially clean.

1. **Absolute continuity:** `A!=0` and an absolutely continuous input law suffice. Under the owner target this is automatic. No height is paid.
2. **Fixed-instance bounded `C_0` density:** for rank `>=3` cap-one products, the completed B15 theorem proves this with a matrix-dependent constant. This is a stronger qualitative conclusion than absolute continuity but still not the owner theorem.
3. **Universal height:** remains OPEN. Its sharp constant is nevertheless exactly the fixed one-sided unit-window supremum (4.1), and exactly the fixed smooth-probe supremum (5.1).
4. **Continuity is not a premise for either exact sharp reduction.** Lebesgue differentiation at a near-maximal nonzero point is sufficient.
5. Therefore a future proof of the universal bound can work entirely with the positive fixed-window or smooth-probe inequality. The already-proved fixed-target `C_0` theorem may then be appended as a separate stronger regularity conclusion; it need not participate in the height argument.

This directly respects the assignment requirement to separate continuity from the central `L^infinity` problem.

## 8. Corrections preserved

Nothing here uses:

- law-uniform pointwise quadratic Fourier decay;
- independence after diagonalizing `A`;
- arbitrary-joint rank-three coarea;
- projection-only X-ray control of the minority/two-sheet trace;
- worst conditional spectral-density caps or their positive moments;
- a uniformly good single physical minor.

The only analytic input in Theorems 4.1 and 5.1 is the completed target absolute-continuity statement plus the ordinary one-dimensional Lebesgue differentiation theorem. Equation (6.1)/(6.2) uses original-coordinate conditioning exactly inside the completed account02/B15 scope.

## 9. First unpaid implication

A strictly simpler exact target than the preceding annular formulation is now

`boxed{
 sup_(s(A)>=1, f_i<=1, y>=4)
 s(A) P{y+1<X^TAX<y+2} < infinity.
}`                                                                  (9.1)

Equivalently, for one fixed nonnegative smooth `psi` supported in `(1,2)` with integral one,

`boxed{
 sup_(s(A)>=1, f_i<=1, y>=4)
 s(A) E psi(X^TAX-y) < infinity.
}`                                                                  (9.2)

Either statement proves the full universal density theorem with **exactly the same optimal constant**.

For a well-conditioned indefinite physical triple, the majority sheet of these exact functionals is already paid by (6.1)/(6.2). The remaining local branch is the minority/two-sheet contribution; globally one must still aggregate original-coordinate product structure before paying reciprocal near-singular physical minors, or exit through one of the completed diffuse/volume/ridge/definite branches.

The live X-ray-only and conditional-cap corrections show why this final step cannot be replaced by generic projected-density regularity.

## 10. Source status


Completed account02/B15 sources applied:

- absolute continuity: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T170424Z-account02-B15-qform-r5/REPORT.md`;
- ambient one-sheet: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T030440Z-account02-B15-QFORM-auto11/REPORT.md`.

Fresh partner continuation `account02/B15/20260923T040456Z-account02-B15-qform-auto11/REPORT.md` independently confirms that continuity is not needed for the annular height interface and that no target-uniform annular approximate-identity limit is available; the present one-sided/smooth fixed-scale theorem is consistent with that obstruction because it uses homogeneity and instancewise Lebesgue differentiation, not a class-uniform limit.

Full QFORM remains OPEN.
