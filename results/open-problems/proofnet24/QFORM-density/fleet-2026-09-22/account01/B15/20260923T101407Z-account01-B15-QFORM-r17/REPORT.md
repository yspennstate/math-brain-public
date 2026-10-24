SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T10:14:07Z.
attacking: target-level Gaussian boundary regularity and a product-preserving fractional majority-cover inequality for the surviving rough-law/two-sheet obstruction.

# QFORM B15 r17 — exact Gaussian boundary criterion and fractional ruled-cover compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** absolute continuity and regularity  
**Run:** `20260923T101407Z-account01-B15-QFORM-r17`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / GAUSSIAN-BOUNDARY-COMPILER / FRACTIONAL-RULED-COVER / FULL_TARGET_OPEN`

The unrestricted QFORM conjecture remains **OPEN**. This run proves two target-level interfaces. First, universal raw density height is *exactly equivalent* to a fixed-scale Gaussian heat-height estimate, and the implication from heat height to a rough `L^infinity` density requires neither prior absolute continuity nor continuity. Second, the completed `account02/B15` rough one-sheet theorem can be combined across original-coordinate physical blocks through a pointwise fractional majority cover, yielding a direct raw-law density bound before any reciprocal-minor inversion. Continuity is then characterized separately by norm convergence of the Gaussian boundary regularization.

## 1. Sources and corrections actually consumed

Fresh owner control remained on QFORM only, OWNER CONTROL revision `2026-09-22.15`, with no later B15 stop observed. The current B15 delivery obligation is to supply a precise rough-law limit or trace justification used by a new density estimate, with continuity kept separate from the central height problem.

Completed partner results used at equations below:

1. **Rough ambient ruled/majority theorem**, `account02/B15`, report
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T083434Z-account02-B15-QFORM-auto11/REPORT.md` (read from current master). For every invertible indefinite **original-coordinate** physical `3x3` block `B`, with `kappa=sigma_min(B)`, after conditioning on arbitrary outside original coordinates and completing the square, the resulting majority/ruled-side output submeasure satisfies
   
   `P(Q in I, M_B) <= (pi sqrt(2)/kappa) |I|`
   
   for every interval `I`. The source proves the rough-input passage by cap-preserving mollification and total variation. It retains arbitrary outside quadratic coefficients and cross couplings and does not invoke continuity or independence after rotation.

2. **Fixed-instance regularity theorem**, `account02/B15`, `math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`. At its stated scope, every fixed symmetric `A` with `rank(A)>=3` and every cap-one product source has an instance-dependent bounded density with a representative in `C_0(R)`. Its constants are matrix-dependent and do **not** prove the universal-height conjecture.

Corrections preserved throughout: no law-uniform pointwise quadratic Fourier decay; no independence after spectral rotation; no arbitrary-joint coarea shortcut; no projection/X-ray-only replacement of the product-sensitive curved trace; no assumption that one physical minor is uniformly conditioned.

## 2. Gaussian boundary lemma: bounded density is exactly uniform heat height

For a finite positive Borel measure `mu` on `R`, set

`gamma_eps(x)=(2 pi)^(-1/2) eps^(-1) exp(-x^2/(2 eps^2))`,

and

`H_eps(y)=(gamma_eps*mu)(y)`.

### Theorem 2.1 (rough boundary domination)

For any `M>=0` and any fixed `eps_0>0`, the following are equivalent:

1. `mu=p dx` with `p in L^infinity(R)` and `||p||_infinity<=M`;
2. `||H_eps||_infinity<=M` for every `0<eps<=eps_0`.

Consequently

`||p||_infinity = sup_{eps>0} ||gamma_eps*p||_infinity = sup_{0<eps<=eps_0} ||gamma_eps*p||_infinity`.

#### Proof

`1=>2` is positivity/Young:

`H_eps(y)=int gamma_eps(y-x)p(x)dx <= M int gamma_eps=M`.

For `2=>1`, let `f>=0` be in `C_c(R)`. Fubini gives

`int f(y) H_eps(y)dy = int (f*gamma_eps)(x) dmu(x)`.

Because `f*gamma_eps -> f` uniformly as `eps downarrow0`, finiteness of `mu` yields

`int f dmu = lim_{eps downarrow0} int f H_eps <= M int f dx`.

Thus `mu<=M dx` as positive Borel measures (first for nonnegative compactly supported continuous test functions, then by regularity), so `mu=p dx` with `0<=p<=M` a.e. This proves the equivalence without assuming in advance that `mu` is absolutely continuous.

For the sharp norm identity, the upper bound was just proved; the reverse inequality follows at any Lebesgue point of `p`, where `gamma_eps*p(y)->p(y)`, and then by approaching the essential supremum. QED.

### Why this is the correct rough-law interface

A universal heat-height estimate already *creates* absolute continuity and the raw `L^infinity` bound. There is no need to first construct a continuous density, no uniform desmoothing rate is required, and there is no hidden Fourier `L^1` premise.

## 3. Continuity is exactly a stronger boundary-norm conclusion

### Theorem 3.1 (Gaussian `C_0` boundary criterion)

For a finite positive Borel measure `mu`, the following are equivalent:

1. `mu=p dx` for some `p in C_0(R)`;
2. `H_eps=gamma_eps*mu` converges in `L^infinity(R)` as `eps downarrow0`;
3. `{H_eps}_{eps downarrow0}` is Cauchy in `L^infinity(R)`.

When these hold, the uniform limit is exactly `p`.

#### Proof

If `p in C_0`, the Gaussian approximate identity converges uniformly: `gamma_eps*p->p` in `L^infinity`.

Conversely suppose `H_eps->g` uniformly. For each `eps>0`, `H_eps in C_0(R)`: continuity follows from translation continuity of the Gaussian kernel, and vanishing at infinity follows by splitting the finite measure into a compact part plus a small tail. Since `C_0(R)` is closed under the uniform norm, `g in C_0(R)`.

For `f in C_c(R)`,

`int f dmu = lim_{eps downarrow0} int f H_eps dx = int f g dx`,

where the first equality is the same approximate-identity argument as in Theorem 2.1 and the second uses uniform convergence. Hence `mu=g dx`. The equivalence with the Cauchy condition follows from completeness of `L^infinity`. QED.

This is the precise separation requested by the assignment:

- **uniform bounded heat extension** `=>` raw `L^infinity` density;
- **uniform norm convergence at the boundary** `=>` continuous `C_0` representative.

The stronger continuity property is not the mechanism that produces the central height bound.

## 4. Exact fixed-scale Gaussian normal form for the full QFORM constant

For a symmetric target matrix `A`, write

`s(A)=s_3(A)`,

its third largest absolute eigenvalue, and `Q_A=X^TAX`. Let

`C_* = sup s(A) ||p_{Q_A}||_infinity`,

where the supremum ranges over the full target class and is allowed to be `+infinity`. Define the fixed-height Gaussian constant

`C_G = sup s(A) ||gamma_1 * mu_{Q_A}||_infinity`

over the same target class.

### Theorem 4.1 (exact fixed-scale equivalence)

`C_*=C_G` (with equality also when either side is infinite).

#### Proof

If raw densities satisfy the bound, Gaussian convolution is an `L^infinity` contraction, so `C_G<=C_*`.

For the converse, assume `C_G<infinity` and fix an arbitrary target `(A,X)`, with `s=s(A)>=1`. For `0<eps<=1`, define

`A_eps=A/eps`.

Then `A_eps` remains a target and `s(A_eps)=s/eps`. Since `Q_{A_eps}=Q_A/eps`, for every `y`,

`(gamma_1*mu_{Q_A/eps})(y/eps) = eps (gamma_eps*mu_{Q_A})(y)`.

Therefore

`s (gamma_eps*mu_{Q_A})(y)
 = (s/eps)(gamma_1*mu_{Q_A/eps})(y/eps)
 <= C_G`.

Thus for every `0<eps<=1`,

`||gamma_eps*mu_{Q_A}||_infinity <= C_G/s`.

Theorem 2.1 now yields directly

`mu_{Q_A}=p_A dx`, `||p_A||_infinity<=C_G/s`.

Taking the supremum gives `C_*<=C_G`. QED.

Hence the entire universal bounded-density conjecture is exactly equivalent to the single fixed-scale positive-kernel estimate

`sup_{target,y} s_3(A) E gamma_1(X^TAX-y) < infinity`.

This is a target-level regularity lemma tailored to the newest Gaussian heat-mode work: scaling absorbs the whole `eps downarrow0` family, while Theorem 2.1 handles the rough boundary measure.

## 5. Instancewise continuity after the height theorem

The completed partner fixed-matrix theorem gives, for each fixed rank-`>=3` target, a bounded representative `p_A in C_0(R)`. Therefore Theorem 3.1 gives the instancewise desmoothing statement

`||gamma_eps*p_A-p_A||_infinity -> 0`.

No law/matrix-uniform rate is asserted. The universal height constant is established, if at all, by Theorem 2.1/4.1; the fixed-instance `C_0` theorem only says that after a raw universal bound is obtained, it can be represented pointwise continuously with the same height for each fixed instance.

## 6. Applying the completed partner ruled theorem to an actual inequality

Let `B_1,...,B_N` be invertible indefinite **original-coordinate** physical principal `3x3` blocks of the same ambient target. Put

`kappa_j=sigma_min(B_j)>0`.

For each block let `M_j` be the measurable majority/ruled event supplied by the completed partner construction after conditioning on the outside original coordinates and completing the square. Define the positive output submeasure

`nu_j^+(E)=P(Q in E, M_j)`.

The partner theorem gives for every interval `I`

`nu_j^+(I) <= C_j |I|`, `C_j=pi sqrt(2)/kappa_j`.

By regularity/monotone-class extension,

`nu_j^+ <= C_j dx`

as measures. Consequently, for every nonnegative Borel kernel `K` with `int K dx=1`,

`E[K(Q) 1_{M_j}] <= pi sqrt(2)/kappa_j`.       (6.1)

This is the partner result applied directly to a quantitative source-level inequality; no continuity and no post-rotation independence are used.

## 7. New fractional majority-cover compiler

### Theorem 7.1 (fractional ruled cover with residual)

Let `lambda_j>=0`, let `delta>0`, and let `E` be any measurable residual event such that pointwise on the original probability space

`sum_{j=1}^N lambda_j 1_{M_j} >= delta 1_{E^c}`.       (7.1)

Then every nonnegative normalized kernel `K` satisfies

`E K(Q)
 <= (pi sqrt(2)/delta) sum_j lambda_j/kappa_j
    + E[K(Q)1_E]`.                                  (7.2)

#### Proof

Multiply (7.1) by `K(Q)>=0` and integrate:

`delta E[K(Q)1_{E^c}]
 <= sum_j lambda_j E[K(Q)1_{M_j}]`.

Apply (6.1) term by term and then add the residual contribution `E[K(Q)1_E]`. QED.

This is an **aggregate-before-inversion** statement: the block estimates are combined at the event/measure level before a reciprocal conditioning cost is paid.

### Corollary 7.2 (fractional cover gives a raw density bound)

If `E` is empty and (7.1) holds, then for every `eps>0`, `y in R`, taking `K(z)=gamma_eps(z-y)` gives

`(gamma_eps*mu_Q)(y)
 <= (pi sqrt(2)/delta) sum_j lambda_j/kappa_j`.

Theorem 2.1 therefore gives directly

`boxed{ ||p_Q||_infinity
 <= (pi sqrt(2)/delta) sum_j lambda_j/kappa_j. }`       (7.3)

Define the fractional ruled-cover cost

`tau(A,X)=inf { sum_j lambda_j/kappa_j : lambda_j>=0,
                sum_j lambda_j 1_{M_j} >=1 a.s. }`,

where the infimum may range over any chosen finite physical-block bank. Then

`boxed{ ||p_Q||_infinity <= pi sqrt(2) tau(A,X). }`    (7.4)

Thus a structural theorem of the form

`s_3(A) tau(A,X) <= C_0`

on the surviving class would close that class with universal constant `pi sqrt(2) C_0`.

### Corollary 7.3 (weighted-conditioning bank certificate)

Suppose a bank satisfies the pointwise weighted coverage

`sum_j kappa_j 1_{M_j} >= theta sum_j kappa_j`          (7.5)

for some `theta>0`. Taking

`lambda_j=kappa_j/[theta sum_l kappa_l]`

gives a unit fractional cover, and hence

`||p_Q||_infinity <= pi sqrt(2) N/[theta sum_j kappa_j]`. (7.6)

If additionally

`(1/N) sum_j kappa_j >= c s_3(A)`,

then

`boxed{ s_3(A)||p_Q||_infinity <= pi sqrt(2)/(c theta). }` (7.7)

Unlike a posterior-average certificate, (7.5) is a pointwise original-space coverage statement, so (7.7) already yields the raw-law bound through Theorem 2.1.

### Corollary 7.4 (hybrid residual exit)

If the residual output submeasure

`rho_E(F)=P(Q in F,E)`

has a density bounded by `R/s_3(A)`, then (7.2) with Gaussian kernels and Theorem 2.1 give

`boxed{
 s_3(A)||p_Q||_infinity
 <= [pi sqrt(2) s_3(A)/delta] sum_j lambda_j/kappa_j + R.
}`                                                         (7.8)

This makes the remaining hybrid obligation explicit: cover the ruled portions fractionally at bounded reciprocal cost and send only the uncovered minority/two-sheet event into another **product-sensitive** theorem.

## 8. Why this does not yet prove N3 or the full target

Nothing here proves that an arbitrary N3/full-target matrix admits a physical-block bank satisfying (7.1) at universally bounded scaled cost. Near-singular physical blocks can make `1/kappa_j` arbitrarily large. Also, the newest partner report gives a source-valid diagonal exact-target family whose Gaussian heat modes can lie arbitrarily deep on the minority/two-sheet side. Thus one cannot replace (7.1) by an assertion that one majority event automatically contains the relevant high-density region.

The unpaid structural implication is now:

> Construct, on each surviving N3/high-leverage class, either (i) a fractional family of original-coordinate indefinite blocks for which `s_3(A) sum lambda_j/kappa_j / delta=O(1)` and the majority events cover pointwise, or (ii) such a cover outside a residual event whose output submeasure is paid by one of the existing product-sensitive volume/ridge/null-coloop/two-sheet exits.

This preserves the central corrections. Generic X-ray bounds cannot pay the residual two-sheet trace; no spectral rotation is treated as preserving independence; no law-uniform pointwise quadratic Fourier decay is used.

## 9. Regularity ledger

The resulting hierarchy is precise:

1. **Absolute continuity:** much weaker; the completed partner fixed-matrix report proves it already for any nonzero symmetric `A` under an absolutely continuous joint input law.
2. **Fixed-instance bounded `C_0` density:** completed partner result for every fixed rank-`>=3` matrix and cap-one product source; constant may depend badly on `A`.
3. **Universal `L^infinity` height:** exactly equivalent to a universal fixed-scale Gaussian heat-height bound by Theorems 2.1 and 4.1. This is the central owner target.
4. **Continuity:** a separate stronger boundary property, equivalent to instancewise `L^infinity` convergence of Gaussian regularizations by Theorem 3.1. It is not required to turn a universal heat bound into the raw density bound.

## 10. Status and next step

**Status:** supporting target-level implication proved; full QFORM remains OPEN. Independent review of this new compiler has not yet been performed.

The most useful next mathematical step for the proof graph is to test the fractional-cover obligation (7.1)/(7.5) on the known no-pivot bank survivors and determine whether a deterministic weighted majority cover follows from their original-coordinate Schur geometry. If not, the failure should identify exactly which residual minority event must be routed to the existing volume/ridge/null-coloop/two-sheet machinery.

No schedule, enabled/quiet state, task identity, email/push setting, account binding, permission, paid/remote workflow, or public visibility was changed in this run.
