# account02/B18 — strict safe-ray zero set and exact dual bypass

**Run:** `B18-20260922T090632Z-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SAFE_RAY_COERCIVITY_REDUCTION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Version/change summary

Later owner control revision `2026-09-22.2` supersedes the older Campaign-C half-band assignment and converges FEI work on the all-gate potential formulation. I therefore do not revive the retired positive-current/R16-only route.

The previous B18 mechanism was `CENTER-BANK-DUAL-TRADEOFF-v1`: a center-retaining positive dual showed that a shaped repair which *spends* the charged AND bank obeys an affine center-versus-bank frontier. account02/B16 then evaluated the genuine nonuniform 35-pair AND bank and found the aggregate obstruction disappears, but did not construct a universal repair.

This run consumes and applies the completed **OTHER-account** result

`account03/B12/20260922T074537Z-tilted-quartic-universal-repair`, commit `0663f1942a3b3f9f04b2b9f6fe80841d7cc5efae`.

That report proves the universally gate-safe direction

\[
F_*(m)=1-m^4-\frac1{36}(1-m^2)^2,
\qquad
\eta_*(u)=\frac{F_*(1-2u)}8,
\tag{0.1}
\]

and exhibits the replacement potential

\[
\Gamma^*(u)=\Gamma^\dagger(u)+\frac{34877}{250000}\eta_*(u),
\tag{0.2}
\]

which repairs the source-certified 18-input Numaro prime witness while never decreasing any gate defect.

The new work below does three things not contained in that source report:

1. proves the **exact equality/zero set** of the safe direction at every interior product bias;
2. turns the full FEI problem along this safe ray into one explicit coercivity quotient, with no invisible zero-denominator nonliteral gate;
3. combines the new direction with B18's center-retaining 35-AND dual and computes the exact positive AND-bank increment, showing that this repair bypasses rather than spends the old bank.

## 1. Source-exact all-gate target and compact conditional deduction

For a Boolean gate `G` at product bias `p`, write

\[
D_\Gamma(G;p)=
\sum_i \alpha_i\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad
\alpha_i=\frac{\operatorname{It}_i(G;p)}{V_{p_i}}.
\tag{1.1}
\]

The inherited all-gate theorem says that one finite symmetric nonnegative `Gamma` with `D_Gamma>=0` for every finite Boolean gate and every product bias implies full FEI with finite dimension-independent center constant `Gamma(1/2)`.

Set

\[
E_*(G;p):=
\sum_i\alpha_i\eta_*(p_i)-\eta_*(p_{\rm out}).
\tag{1.2}
\]

The consumed account03/B12 theorem proves

\[
E_*(G;p)\ge0
\tag{1.3}
\]

for every gate and bias. Hence on the ray

\[
\Gamma_T=\Gamma^\dagger+T\eta_*,\qquad T\ge0,
\]

we have the exact affine identity

\[
D_{\Gamma_T}(G;p)=D_{\Gamma^\dagger}(G;p)+T E_*(G;p).
\tag{1.4}
\]

Therefore a complete sufficient condition for FEI is the single signed implication

\[
\boxed{
D_{\Gamma^\dagger}(G;p)\ge -T E_*(G;p)
\quad\text{for all Boolean gates and all interior product biases}
}
\tag{1.5}
\]

for one finite `T`. The resulting center is

\[
\Gamma_T(1/2)=6.521851214+\frac{35}{288}T.
\tag{1.6}
\]

The rest of this report proves that the denominator in this formulation vanishes only on the exact all-gate equality objects (constants and literals), so (1.5) is noncircular and has no hidden nonliteral zero-energy branch.

## 2. Main theorem: the safe direction has only constant/literal equality cases

The factorization

\[
F_*(m)=(1-m^2)\left(\frac{35}{36}+\frac{37}{36}m^2\right)
\tag{2.1}
\]

shows

\[
F_*(m)>0\quad\text{for }|m|<1.
\tag{2.2}
\]

### Theorem 2.1 — strict interior zero set

Let every input bias satisfy `0<p_i<1`. Then

\[
\boxed{
E_*(G;p)=0
\iff
G\text{ is constant or is a literal }\pm x_j
\text{ (dummy variables allowed).}
}
\tag{2.3}
\]

In particular every Boolean gate depending essentially on at least two coordinates has

\[
E_*(G;p)>0
\tag{2.4}
\]

at every interior product bias.

### Proof

Use exactly the induction and notation of the consumed account03/B12 proof. Split the last coordinate, of bias `t in (0,1)`, with `q=1-t`. Let the two restrictions have means `a,b`, disagreement probability `delta`, and parent mean

\[
c=qa+tb.
\]

The parent energy decomposes **exactly** as

\[
E_*(G;p)=qE_*(G_0;p')+tE_*(G_1;p')+\frac18 S(a,b,\delta,t),
\tag{2.5}
\]

where

\[
S=qF_*(a)+tF_*(b)-F_*(c)+\delta F_*(q-t).
\tag{2.6}
\]

All three terms on the right of (2.5) are nonnegative by the consumed theorem. It remains to identify when `S=0`.

Assume `b>=a` and put `d=b-a in [0,2]`. Boolean realizability gives

\[
\delta\ge d/2.
\tag{2.7}
\]

If `0<d<2`, account03/B12 proves that the value at the smallest allowed disagreement is

\[
S(a,b,d/2,t)=dtq\,B(c,d,t),
\tag{2.8}
\]

where `B` is concave in `c` on the feasible interval and its endpoint minima satisfy

\[
36B=(2-d)P(d,t),\qquad P(d,t)>0.
\tag{2.9}
\]

Thus `B>0`, hence `S(a,b,d/2,t)>0`. Since `F_*(q-t)>0` by (2.2), increasing `delta` only increases `S`; therefore

\[
0<d<2\implies S>0.
\tag{2.10}
\]

If `d=0`, then the convexity part vanishes and

\[
S=\delta F_*(q-t).
\]

Again `F_*(q-t)>0`, so `S=0` iff `delta=0`. Full support of the product law then forces `G_0=G_1` pointwise: the split variable is irrelevant.

If `d=2`, the two means are `-1,+1` (up to order). Full support forces the restrictions themselves to be opposite constants, `delta=1`, and direct substitution gives `S=0`. The parent is exactly the last literal (up to sign), with all earlier variables dummy.

Hence a zero parent energy has either an irrelevant last coordinate and two identical zero-energy children, or is already a literal in the last coordinate. Induction on the essential arity gives precisely constants and literals. The converse follows by direct substitution. QED.

## 3. Exact safe-ray coercivity reformulation

For nonconstant nonliteral gates define

\[
\tau(G;p):=
\frac{[-D_{\Gamma^\dagger}(G;p)]_+}{E_*(G;p)}.
\tag{3.1}
\]

Theorem 2.1 makes this well-defined at every interior bias. Constants and literals have `D_{Gamma^dagger}=E_*=0` by direct substitution, so they are harmless.

Define the universal ray threshold

\[
T_*:=\sup_{G,p}\tau(G;p),
\tag{3.2}
\]

where the supremum ranges over finite nonliteral Boolean gates and interior product biases. Then

\[
\boxed{
T_*<\infty
\iff
\text{some finite member }\Gamma^\dagger+T\eta_*
\text{ satisfies the all-gate inequality.}
}
\tag{3.3}
\]

Indeed, if `T_*<infty`, (1.4) gives `D_{Gamma_{T_*}}>=0`; conversely any successful `T` bounds every quotient by `T`.

Thus the first missing universal implication is now the single named statement

`SAFE-RAY-COERCIVITY-v1`:

\[
\boxed{
\sup_{G,p}
\frac{[-D_{\Gamma^\dagger}(G;p)]_+}
{\sum_i\alpha_i\eta_*(p_i)-\eta_*(p_{\rm out})}
<\infty.
}
\tag{3.4}
\]

A counterexample to this exact statement must be a genuine Boolean gate/bias sequence with this quotient tending to infinity. There is no longer a possibility of hiding a negative defect at an interior nonliteral zero of the repair direction.

For each fixed arity `n` and each `epsilon>0`, the quotient is automatically bounded on `p_i in [epsilon,1-epsilon]`: there are finitely many truth tables, the numerator and denominator are continuous, and Theorem 2.1 makes the denominator strictly positive on every nonliteral table. Consequently any failure of (3.4) must escape by **unbounded essential arity, boundary degeneration, or both**.

## 4. Exact compatibility with B18's 35-AND positive dual

The preceding B18 center-retaining dual and account02/B16 actual-bank evaluation use the exact coefficient

\[
\beta=\frac{23156036957147}{44712962557360}
\tag{4.1}
\]

and, for every symmetric perturbation `psi`,

\[
\sum_{j=1}^{35}\lambda_j[-L_j(\psi)]
=
\frac{57}{256}\psi(3/8)-\psi(967/2048)+\beta\psi(1/2).
\tag{4.2}
\]

For the Numaro prime witness the full perturbation response is

\[
P(\psi)=
\frac{57}{256}\psi(3/8)+\frac{465}{256}\psi(1/2)-\psi(967/2048).
\tag{4.3}
\]

For `eta_*`, exact evaluation gives

\[
\eta_*(3/8)=\frac{995}{8192},\qquad
\eta_*(1/2)=\frac{35}{288},\qquad
\eta_*(967/2048)=
\frac{38489330046971}{316659348799488}.
\tag{4.4}
\]

Hence the prime repair per unit scale is

\[
\boxed{
P_*=
\frac{39974940944389}{316659348799488}
=0.12623957289099823558\ldots
}
\tag{4.5}
\]

and the **aggregate 35-AND defect increment** is

\[
\boxed{
B_*:=\sum_j\lambda_j L_j(\eta_*)
=
\frac{5586911653540898590992293}
{176984720078868840129232896}
=0.03156719772786730018\ldots>0.
}
\tag{4.6}
\]

The sign in (4.6) is important: the universal repair direction does not spend the old AND bank; it *increases* the weighted AND slack. The exact identity tying this to B18's center-bank frontier is

\[
\boxed{
P_*+B_*
=
\left(\frac{465}{256}-\beta\right)\eta_*(1/2).
}
\tag{4.7}
\]

At the account03/B12 scale

\[
T_0=\frac{34877}{250000},
\]

we obtain

\[
T_0P_*=0.01761143033487738185\ldots,
\tag{4.8}
\]

which exceeds the certified witness deficit upper bound `0.017611420` by more than `1.03e-8`, while simultaneously

\[
T_0B_*=0.00440387662061931131\ldots>0
\tag{4.9}
\]

and

\[
T_0\eta_*(1/2)=\frac{244139}{14400000}
=0.01695409722222222222\ldots .
\tag{4.10}
\]

Therefore the previous center-bank theorem remains correct at its stated scope, but its bank-spending architecture is no longer the decisive repair mechanism. The new universally safe ray bypasses that bottleneck by paying a finite center increment while improving, not consuming, every AND constraint.

## 5. Application of account01/B12's Boolean endpoint theorem

A second compatible **OTHER-account** result is account01/B12 `20260922T081900Z-balanced-poincare-bellman`, commit `3a03960af4b07d1b38b418c3a0430360c272c0ac`. It proves that for a balanced Boolean `f` with

\[
I(f)=1+\delta,
\]

some actual singleton Fourier atom has mass at least

\[
1-(3+\sqrt3)\delta.
\tag{5.1}
\]

On precisely this balanced uniform slice, the safe energy has the exact closed form

\[
\boxed{
E_*(f;1/2^n)
=\eta_*(1/2)(I(f)-1)
=\frac{35}{288}\delta.
}
\tag{5.2}
\]

Thus the new ray sees every noncharacter balanced Poincare excess linearly and vanishes exactly at the character endpoint. Combining (5.1) and (5.2) localizes any putative balanced low-energy blow-up of (3.4) to genuine near-character Boolean sources, not the non-Boolean multi-singleton Gibbs optimizer.

This does **not** yet prove a bounded quotient. The same account01/B12 report correctly shows that sparse balanced defects forbid a quadratic leakage claim; its current KL lower bound still pays a coarse `h_2((3+sqrt(3))delta)` term. Hence the exact remaining near-character task is to use the *degree/price structure* of that leakage to prove

\[
[-D_{\Gamma^\dagger}(f;1/2^n)]_+=O(\delta)
\tag{5.3}
\]

with a dimension-independent constant, or exhibit a genuine Boolean sequence violating it. Equation (5.2) shows that (5.3) is exactly the balanced endpoint instance of `SAFE-RAY-COERCIVITY-v1`, not a renamed residual.

## 6. Last-three-run comparison and target-level status

The last three substantive B18 mechanisms were:

1. random-block Poincare currency / proposed block deficit criterion;
2. correction of the circular terminal criterion and exact signed depthwise barycenter/front-loading;
3. center-retaining 35-AND dual tradeoff for shaped repairs of the first biased prime witness.

None proved a universal all-gate potential. The present run executes a materially different mechanism: a **universally gate-safe additive ray**, with an exact strict zero-set theorem and an exact coercivity quotient.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No finite universal `T_*` is proved.

**MECHANISM CHANGE:** `bank-spending shaped repair -> universally safe monotone repair ray`.

**Old missing implication:** construct or rule out a shaped repair while respecting the charged 35 AND constraints.

**New proved inference:** the account03 tilted-quartic direction repairs the known prime witness without decreasing any gate defect; its interior zero set consists only of constants/literals; it adds strictly positive weighted slack to the old 35-AND dual; and the full ray succeeds iff the explicit quotient (3.4) is uniformly bounded.

**New first essential missing implication:** `SAFE-RAY-COERCIVITY-v1`, especially its two possible escape regimes isolated above: boundary degeneration and unbounded essential arity. This is the named unresolved statement to attack next rather than returning to the retired half-band current or another fixed-center AND-bank LP.

## 7. Verification and scope

The adjacent exact checker uses only rational arithmetic to verify (4.4)--(4.10), including the dual identity (4.7) and the strict repair gap against the certified decimal upper bound on the known prime deficit. The equality theorem is analytic; the checker is only arithmetic falsification support.

No benchmark gold, credentials, scheduler identifiers, machine paths, raw transcripts, email/Drive material, public posting, paid API/model/Codex call, remote workflow, permission change, or unrelated private data is included. No production truth state is promoted. Full FEI remains open.
