# account03/B13 — rational finite-fragment witness completeness for QFORM

**Programme:** QFORM-DENSITY-3EIG-20260922, owner revision 2026-09-22.5  
**Assignment:** Extremal product laws  
**Status:** PROVED TARGET-LEVEL REDUCTION / FULL QFORM OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Full target and scope

For every finite `n`, independent real `X_i` with densities `0 <= f_i <= 1`, and real symmetric `A` with at least three eigenvalues of absolute value at least one, the target is a universal finite `C` such that

`P(X^T A X in [t,t+h]) <= C h`

for all real `t` and `h>0`. No moment, support, sign, diagonal-basis, log-concavity, or identical-law hypothesis is added here.

This report does **not** prove the universal bound. It proves that for every fixed candidate constant `C`, any failure of the full target has a witness in a countable algebraic/geometric subclass with strict spectral slack. Thus arbitrary bounded one-dimensional laws, arbitrary real support endpoints, threshold eigenvalues exactly at one, and irrational matrix/interval data are not needed to witness failure.

## 2. Completed partner theorem consumed

I use the source proof

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T115714Z-account02-B13-qform-480ba28b/REPORT.md`.

Its proved results used here are:

1. **Exact one-coordinate/product bathtub purification.** For every measurable `K:R^n->[0,1]`, the supremum of `int K prod f_i` over all `0<=f_i<=1`, `int f_i=1`, equals the supremum over product indicators `f_i=1_{E_i}`, `|E_i|=1`.
2. **Finite-fragment localization.** The same supremum is obtained when every `E_i` is a bounded finite union of intervals of total length one; rational interval endpoints can be imposed with arbitrarily small loss by endpoint approximation and the product telescoping estimate.
3. **No single-interval shortcut.** A disconnected quadratic fiber can gain a factor two over every single unit interval, so disconnected fragments must remain allowed.

The fresh brain handoff for the same theorem is `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B13/20260922T115714Z-account02-B13-qform-480ba28b.md` at the current control repository. I use the full source report above as the mathematical dependency.

## 3. New theorem: fully rational strict-slack witnesses

### Theorem 3.1 — QFORM-RATIONAL-SPECTRAL-SLACK-WITNESS-v1

Fix any finite `C>=0`. The following are equivalent.

**(A)** The QFORM small-ball inequality with constant `C` holds for the full owner class: every `n`, every independent densities `0<=f_i<=1` of mass one, every real symmetric `A` with at least three eigenvalues satisfying `|lambda|>=1`, every real `t`, and every `h>0`.

**(B)** The same inequality holds for the following countable witness class only:

- every marginal density is `1_{E_i}`;
- each `E_i` is a bounded finite union of intervals with **rational endpoints** and total Lebesgue measure exactly one;
- `A` is a symmetric matrix with **rational entries** and has at least three eigenvalues with `|lambda|>1` (strict slack);
- the tested interval `[a,b]` has **rational endpoints**, `a<b`.

Equivalently, if the full inequality fails for `C`, then it fails strictly for one witness satisfying all four bullets.

This reduction has **zero loss in the candidate constant**: the witness still satisfies `P(Q in J) > C |J|`.

### Proof

`(A) => (B)` is immediate, since (B) is a subclass. We prove the contrapositive of `(B) => (A)`.

Assume (A) fails. Then for some admissible dimension, laws, symmetric `A`, interval `I=[t,t+h]` with `h>0`,

`P(Q_A(X) in I) > C h`.

Choose a positive margin `eta` with

`P(Q_A(X) in I) >= C h + eta`.  (3.1)

By the consumed exact bang-bang theorem and finite-fragment localization, for any prescribed error there are bounded finite-union unit-measure sets with rational endpoints whose product-uniform law approximates the worst slab probability from below. In particular choose such sets `E_1,...,E_n` so that, for

`K = E_1 x ... x E_n`,

`P_K(Q_A in I) >= C h + 3 eta/4`.  (3.2)

Here `P_K` is simply Lebesgue measure on `K`, since every `|E_i|=1`, hence `|K|=1`. All `E_i` already satisfy the rational finite-fragment requirement. Let

`R2 := sup_{x in K} ||x||_2^2 < infinity`,  (3.3)

which is finite because every factor is bounded.

If `C=0`, the remaining perturbations can be taken arbitrarily small and the proof below simplifies. Assume first `C>0`.

#### Step 1: create strict spectral slack without losing the violation

Choose a scalar `s>1` so close to one that

`C (s-1) h < eta/8`.  (3.4)

For `A_s=sA` and `I_s=[s t,s(t+h)]`, the event is identical:

`Q_{A_s}(x) in I_s` iff `Q_A(x) in I`.  (3.5)

Hence (3.2) and (3.4) give

`P_K(Q_{A_s} in I_s) > C |I_s| + 5 eta/8`.  (3.6)

Moreover, if the third largest singular value of `A` is at least one, then the third largest singular value of `A_s` is at least `s>1`. For a real symmetric matrix the singular values are the absolute eigenvalues, so `A_s` has the required three strict large directions.

#### Step 2: rationalize the matrix with an outward shell enlargement

Rational symmetric matrices are dense in the real symmetric matrices. Choose a rational symmetric `A'` with

`delta := ||A'-A_s||_op < (s-1)/2`  (3.7)

and also so small that

`2 C delta R2 < eta/8`.  (3.8)

By the singular-value perturbation inequality,

`s_3(A') >= s_3(A_s)-delta >= s-delta > 1`,  (3.9)

so `A'` still has at least three eigenvalues of absolute value strictly greater than one.

For every `x in K`,

`|Q_{A'}(x)-Q_{A_s}(x)| = |x^T(A'-A_s)x| <= delta ||x||^2 <= rho`,  (3.10)

where `rho=delta R2`. Therefore

`{x in K: Q_{A_s}(x) in I_s}`

is contained in

`{x in K: Q_{A'}(x) in [s t-rho, s(t+h)+rho]}`.  (3.11)

The latter interval has length `s h+2 rho`.

#### Step 3: rationalize the interval by outward approximation

Choose rational numbers `a<b` with

`a < s t-rho`, `b > s(t+h)+rho`,  (3.12)

and with extra outward widening

`[s t-rho-a] + [b-s(t+h)-rho] < eta/(8C)`.  (3.13)

Such rationals exist by density of `Q` in `R`. Then `[a,b]` contains the interval in (3.11), and

`C(b-a) < C s h + 2 C rho + eta/8`.  (3.14)

Using (3.6), (3.8), and event containment,

`P_K(Q_{A'} in [a,b])`
`>= P_K(Q_{A_s} in I_s)`
`> C s h + 5 eta/8`
`> C(b-a) + 3 eta/8`.  (3.15)

Thus the rational finite-fragment product law, rational symmetric matrix with strict three-eigenvalue slack, and rational interval give a strict violation of the same constant `C`.

When `C=0`, start from a positive-probability violating slab, take `s>1`, then choose `A'` and a rational outward interval sufficiently close; event containment preserves positive probability, while `C|J|=0`. This gives the same conclusion.

This proves the contrapositive and hence the theorem. QED.

## 4. Why this is target-relevant rather than a compact-support assumption

The bounded supports in the witness are **derived only after a strict violation is assumed**, using the proved partner extremal/localization theorem. No bounded-support hypothesis is inserted into the target. The scaling `A -> sA` does not alter the event after the interval is scaled, and the rational matrix perturbation is handled by the explicit uniform bound (3.10) on the now-bounded witness product set. Thus the spectral threshold `|lambda|>=1` is preserved correctly: a threshold witness is first moved to strict slack and only then rationalized.

The argument also preserves indefinite signs and arbitrary rotations. It uses the third singular value only to certify the number of eigenvalues with absolute value larger than one; it does not diagonalize the input variables.

## 5. Concrete consequence for the unpaid geometric implication

For each fixed candidate constant `C`, the full universal slab inequality is true **iff** it is true on a countable family of rational finite-fragment instances with strict spectral slack. Therefore any genuine counterexample to the owner conjecture admits an arbitrarily explicit finite description; conversely, a proposed proof cannot justify restricting to one interval per coordinate, since the consumed quadratic-fiber example refutes that stronger localization.

This sharpens the unpaid B13 implication from

> control arbitrary finite interval fragments with arbitrary real data

into the equivalent falsification/proof target

> control all rational finite interval fragments, rational symmetric matrices with `s_3(A)>1`, and rational intervals, uniformly in dimension and fragment count/separation.

The hard analytic inequality is still unpaid. The reduction does not make the infinite countable family finite and does not by itself furnish a universal `C`.

## 6. Dead routes and integrity checks

- **Single centered interval extremality:** REFUTED by the consumed account02/B13 two-branch quadratic fiber. Not used.
- **Pointwise law-uniform Fourier decay:** REFUTED in current QFORM state. Not used.
- **Cross-minor alone:** current correction `QFORM-CROSSMINOR-ALONE-FALSE` consumed. Not used.
- **Naive rotation to eigen-coordinates:** not used; independence remains in the original coordinates.
- **Claim that rational reduction proves QFORM:** false. The full universal bound remains OPEN.

## 7. Next attack

The rational-witness theorem makes a rigorous source-valid search possible without loss of logical generality on the falsification side. The next high-value attack is to combine it with the existing closed local-curvature branches (definite principal pair, nonsingular principal triple, and diffuse rank-three/separable-phase theorem) to prove a quantitative structural dichotomy for every rational target matrix: either one paid local/diffuse branch applies, or the matrix lies in a precisely parameterized residual leverage-heavy class. That residual can then be searched or attacked without any arbitrary-law ambiguity.

Primary next recipients: account03/B17 (sharp constants and witnesses) and account03/B19 (universal proof assembly). The consumed account02/B13 worker is a secondary recipient for extremal-law consistency.

**Full QFORM status:** OPEN / NOT PROVED.
