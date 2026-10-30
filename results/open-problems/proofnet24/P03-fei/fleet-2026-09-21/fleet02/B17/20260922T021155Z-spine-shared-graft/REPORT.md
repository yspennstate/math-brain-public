# fleet02/B17 — distinguished-spine shared graft beats the full-composition tail

**Run:** `20260922T021155Z-fleet02-B17-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED` to the live all-gate adversarial programme.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository controls and mathematical sources were used, but no installed/authenticated research-brain receiver context was retrieved.

## 0. Version/change summary

The live owner target is the all-gate reformulation: find one symmetric nonnegative potential `Gamma` with finite center such that for every Boolean gate `G` and every product bias vector,

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}}.
\]

On balanced uniform gates, this contains the exact lower-bound quantity
\(R(f)=H(f)/(I(f)-1)\).

The named other-account result consumed here is fleet03/B18,
`20260922T014034Z-shared-graft-tail/REPORT.md`, blob
`e8ef3647b38fbe4301b657defe38829e2a3521a5`.
It proved that its source-valid recursive shared-graft sequence, which uses **full
fourth self-composition** before each graft, has increasing balanced excess ratio
and converges in

\[
6.5218509495504213854\ldots
<R_\infty<
6.5218509495533749375\ldots .
\]

Its exact singleton recurrence and forcing interval are valid and are used below.
The present run attacks the **construction mechanism itself**: full self-composition
preserves the excess ratio but spends far more influence than is needed merely to
raise one distinguished singleton coefficient to its fourth power.

The replacement is a one-coordinate **distinguished spine**.  It keeps the same
excess ratio and the same \(c^4\) distinguished singleton as fourth
self-composition, but its influence is only linear in the geometric sum
\(1+c+c^2+c^3\), not \(I^4\).  Feeding that cheaper gadget into the same
source-valid shared graft increases the old entire tail bound in one step and gives
a stronger convergent Boolean family.

Three FLEET_RULES moves used substantively:
- **#2 ATTACK THE NEGATION FIRST:** try to beat the B-lead's completed full-composition tail using an actual Boolean gate.
- **#12 FIND WHAT IS CONSERVED:** identify the exact invariant \(H/(I-1)\) under one-coordinate balanced substitution by a child with the same ratio.
- **#19 MAKE IT AN ALGORITHM:** iterate the spine substitution plus shared graft and prove the resulting scalar recurrences contract.

No publication-priority or novelty claim is made.

## 1. Normalization and inherited source-valid transform

For a balanced Boolean \(f:\{0,1\}^n\to\{-1,1\}\),

\[
H(f)=\sum_S \widehat f(S)^2\log_2\frac1{\widehat f(S)^2},
\qquad
I(f)=\sum_S |S|\widehat f(S)^2,
\qquad
R(f)=\frac{H(f)}{I(f)-1}.
\]

The inherited 162-variable balanced monotone shared-graft gate \(F_1\) has

\[
I_1=\frac{68013}{32768},\qquad
c_1=\frac{14593}{65536},
\]
where \(c_1\) is the Fourier singleton of a designated monotone coordinate, and

\[
R_1\in[
6.521850083658612443633672199029299526203969334,\,
6.521850083658612443633672199029299526203969335].
\tag{1.1}
\]

The source shared-core transform \(T(h,b)\), for any balanced monotone gadget
\(h\) with designated singleton coefficient \(b\), has exact formulas

\[
H(T(h,b))=K(b)+\alpha H(h),\qquad
I(T(h,b))-1=q+\alpha\,[I(h)-1],
\tag{1.2}
\]
where

\[
\alpha=\frac9{256},\qquad q=\frac{133}{128},
\tag{1.3}
\]

\[
K(b)=H_{\rm core}(b)+\frac9{256}
\{-\phi(b^2)+16(1-b^2)\},
\quad
\phi(x)=-x\log_2 x.
\tag{1.4}
\]

The designated output singleton is

\[
c'=\frac{57+b}{256}.
\tag{1.5}
\]

Booleanity, balance and monotonicity of \(T(h,b)\) are inherited from the
published free-edge construction; the transform shares the gadget's designated
input with the physical core pivot rather than introducing an independent
coordinate.

## 2. New lemma: one-coordinate balanced substitution

Let \(f\) and \(g\) be balanced Boolean functions on disjoint variables.  Fix
coordinate \(j\) of \(f\), and form \(f\circ_j g\) by replacing \(x_j\) by
\(g\).  Then

\[
\boxed{
H(f\circ_j g)=H(f)+\operatorname{Inf}_j(f)H(g)
}
\tag{2.1}
\]

and

\[
\boxed{
I(f\circ_j g)=I(f)+\operatorname{Inf}_j(f)[I(g)-1].
}
\tag{2.2}
\]

### Proof

Because \(g\) is balanced, \(\widehat g(\varnothing)=0\).  Hence there is no
Fourier collision between outer coefficients containing \(j\) and those not
containing \(j\).  A coefficient indexed by \(S\ni j\) and an inner support
\(T\ne\varnothing\) is

\[
\widehat f(S)\widehat g(T)
\]

on the labelled support \((S\setminus\{j\})\sqcup T\).
Thus the spectral law over all \(S\ni j\) is refined by an independent sample
from the spectral law of \(g\).  The chain rule gives an entropy increment
\(H(g)\) times

\[
\sum_{S\ni j}\widehat f(S)^2=\operatorname{Inf}_j(f),
\]

proving (2.1).  For influence, \(|S|\) is replaced by
\(|S|-1+|T|\), so the expected degree increment is
\((I(g)-1)\operatorname{Inf}_j(f)\), proving (2.2).  QED.

If \(f=g=h\) is balanced monotone and the designated coordinate has singleton
coefficient \(c\), monotonicity gives
\(\operatorname{Inf}_j(h)=c\).  Also the deepest designated singleton after one
substitution is the product of the two singleton coefficients.

Define the depth-\(r\) **distinguished spine** \(P_r(h)\) recursively by
\(P_1(h)=h\) and by replacing only the designated coordinate of a fresh outer
copy of \(h\) by \(P_{r-1}(h)\).  Induction in (2.1)-(2.2) gives

\[
H(P_r(h))=H(h)\sum_{s=0}^{r-1}c^s,
\tag{2.3}
\]

\[
I(P_r(h))-1=(I(h)-1)\sum_{s=0}^{r-1}c^s,
\tag{2.4}
\]

and the deepest singleton is \(c^r\).  Therefore

\[
\boxed{R(P_r(h))=R(h)}
\tag{2.5}
\]

exactly.

This is the conserved quantity the full self-composition step was spending too
much influence to preserve.

## 3. The spine-graft recurrence

Use \(r=4\), set

\[
S(c)=1+c+c^2+c^3,
\tag{3.1}
\]

and define recursively

\[
F_{t+1}=T(P_4(F_t),c_t^4).
\tag{3.2}
\]

Every \(F_t\) is a finite balanced monotone Boolean gate.  If \(F_t\) has arity
\(n_t\), then \(P_4(F_t)\) has arity \(4n_t-3\), so the nine-host graft has

\[
n_{t+1}=9+9(4n_t-4)=36n_t-27.
\tag{3.3}
\]

Thus no infinite object is being used as a gate.

From (1.5) and (2.3)-(2.4),

\[
\boxed{c_{t+1}=\frac{57+c_t^4}{256}}
\tag{3.4}
\]

(the same singleton recurrence as the inherited full-composition construction),

\[
\boxed{
I_{t+1}
=\frac{261}{128}
+\frac9{256}(I_t-1)S(c_t),
}
\tag{3.5}
\]

and, writing \(R_t=H(F_t)/(I_t-1)\),

\[
\boxed{
R_{t+1}
=
\frac{K(c_t^4)
+\frac9{256}R_t(I_t-1)S(c_t)}
{\frac{133}{128}
+\frac9{256}(I_t-1)S(c_t)}.
}
\tag{3.6}
\]

Define

\[
T(c)=\frac{128}{133}K(c^4)
\tag{3.7}
\]

and

\[
\lambda_t
=
\frac{133/128}
{\frac{133}{128}+\frac9{256}(I_t-1)S(c_t)}.
\tag{3.8}
\]

Then (3.6) is the exact convex update

\[
\boxed{
R_{t+1}=(1-\lambda_t)R_t+\lambda_t T(c_t).
}
\tag{3.9}
\]

The inherited full-composition recurrence has the **same** forcing value
\(T(c_t)\), but its denominator contains \(I_t^4\), driving its update weight to
zero.  The spine recurrence retains a uniformly large update weight.

## 4. One exact step already beats the inherited entire tail

For \(F_1\), the four-spine has

\[
I(P_4(F_1))
=
2.380301610934986174966145056064448226607055403292\ldots
\]

rather than \(I_1^4\).  Its nine-host graft \(F_2\) has

\[
I_2=
2.087588728509433107713653537127265757966654291522\ldots
\]

and exact rational-log interval evaluation gives

\[
\boxed{
6.5218511190811741401649047123071878637276611493668
<
R_2
<
6.5218511190811741401649047123167742489206633278087.
}
\tag{4.1}
\]

The inherited fleet03/B18 full-composition tail satisfies

\[
R_\infty^{\rm full}
<
6.5218509495533749374651456092951.
\]

Therefore the **first** spine-graft step obeys

\[
\boxed{
R_2-R_\infty^{\rm full}
>
1.6952779920269975910301208786\times10^{-7}.
}
\tag{4.2}
\]

This is an actual finite Boolean construction, not a relaxation.  It refutes
only the implicit construction-level idea that full fourth self-composition is
the efficient way to create the \(c^4\) input needed by this shared-core
transform.  It does not refute FEI.

Balanced disjoint self-composition of this finite \(F_2\) already yields ordinary
Boolean functions whose \(H/I\) ratios approach \(R_2\).

## 5. All-tail convergence of the new Boolean family

The singleton map

\[
F(c)=\frac{57+c^4}{256}
\tag{5.1}
\]

maps \([0,1/4]\) into itself and satisfies

\[
0\le F'(c)=\frac{c^3}{64}\le\frac1{4096}.
\tag{5.2}
\]

Hence it has a unique fixed point \(c_*\), and \(c_t\to c_*\).
The inherited B-lead interval is recomputed by the checker:

\[
0.22266585228<c_*<0.22266585229.
\tag{5.3}
\]

Indeed \(c_3\) is already inside this interval and its two endpoints map strictly
inward.

The source core satisfies

\[
\max|A_S|=114,\quad
\max|Q_S|=18,\quad
\sum_S|Q_S|=1584.
\tag{5.4}
\]

The B-lead derivative argument gives, throughout the corresponding
\(b=c^4\) interval,

\[
|K'(b)|<19.
\tag{5.5}
\]

For completeness, the bound comes from \(g(z)=\phi(z^2)\),
\(|g'(z)|<6\) for \(|z|\le1\), and
\(\sum|Q_S|/512=1584/512\), plus less than \(0.215\) from the explicit
scalar term in (1.4).

Using exact rational atanh-series logarithm enclosures at
\(b_0=0.00245818450862\), followed by (5.5), the checker proves

\[
\boxed{
6.5218511673423727025654896282010361877746102003501
<
T(c_*)
<
6.5218511673532720920534233991583790594494969981239.
}
\tag{5.6}
\]

It remains to prove that \(R_t\) actually reaches that forcing level rather than
freezing below it.

First, \(I_1<21/10\).  If \(I_t\le21/10\) and \(c_t\le1/4\), then

\[
S(c_t)\le\frac{85}{64},
\]

and (3.5) gives

\[
I_{t+1}
\le
\frac{261}{128}
+\frac9{256}\frac{11}{10}\frac{85}{64}
=
\frac{68499}{32768}
<\frac{21}{10}.
\tag{5.7}
\]

Thus \(I_t<21/10\) for every \(t\).  Consequently

\[
\lambda_t
\ge
\frac{34048}{35731}
=
0.95289804371554112675\ldots,
\tag{5.8}
\]

so

\[
1-\lambda_t
\le
\frac{1683}{35731}
<
0.048.
\tag{5.9}
\]

Since \(c_t\to c_*\), continuity gives \(T(c_t)\to T(c_*)\).
Subtract \(T(c_*)\) from (3.9):

\[
|R_{t+1}-T(c_*)|
\le
\frac{1683}{35731}|R_t-T(c_*)|
+
|T(c_t)-T(c_*)|.
\tag{5.10}
\]

The second term tends to zero and the first coefficient is strictly below one.
The standard contraction recursion therefore yields

\[
\boxed{R_t\longrightarrow T(c_*).}
\tag{5.11}
\]

This is an analytic all-tail theorem; no extrapolation from a finite table is
used.

## 6. Consequence for the FEI lower floor

Each \(F_t\) is balanced.  For a fixed \(t\), balanced disjoint
self-composition gives a sequence of finite Boolean functions whose ordinary
\(H/I\) ratios converge to \(R_t\).  Therefore the universal FEI constant
(if finite) must satisfy

\[
C_{\rm FEI}\ge R_t\quad\text{for every }t.
\]

Taking \(t\to\infty\) and using (5.6)-(5.11),

\[
\boxed{
C_{\rm FEI}
>
6.5218511673423727025654896282010361877746102003501.
}
\tag{6.1}
\]

The strict displayed endpoint is safe because (5.6) is a strict enclosure for
the limiting forcing value.

Compared with the inherited full-composition tail upper endpoint, the new
certified asymptotic floor is higher by more than

\[
2.17788997765100344018905936\times10^{-7}.
\tag{6.2}
\]

This is a **lower bound / adversarial construction result only**.  It does not
supply a dimension-independent upper bound and does not prove full FEI.

For the old read-once center \(C_0=6.4548\), the balanced-uniform scalar
quadratic lift would now need at least

\[
4(6.5218511673423727\ldots-6.4548)
>
0.2682046693694908.
\tag{6.3}
\]

More importantly, the lesson is structural: a potential or code that prices
overlap using the total influence of a full recursive copy is vulnerable to a
thin distinguished spine carrying the same Fourier singleton product and the
same excess ratio at much lower influence cost.

## 7. Relation to the all-gate candidate and last three B17 mechanisms

The last three substantive B17 stages were:

1. `20260921T215432Z-selector-phase-low-plaquette`: exact factorization was
   defeated by a weak phase connector; replacement was approximate low-plaquette
   factorization.
2. `20260921T231240Z-recursive-majority-hierarchical-code`: recursive majority
   defeated the global one-level code; replacement was nested branch-surplus
   coding.
3. `20260922T004442Z-gate-composition-cocycle`: owner convergence moved the work
   to the exact all-gate inequality; disjoint composition was proved unable to
   amplify normalized gate margin, reducing any fixed-potential obstruction to
   a composition-prime factor.

Since then, fleet03/B12 and fleet01/B16 produced an explicit
composition-prime 10-input gate that already refutes AND/decomposable
extremality, while fleet03/B18 proved the complete full-composition shared-graft
tail.  This run does not repeat either result.  It changes the construction
mechanism from full disjoint self-composition to a one-coordinate conserved
spine and proves a stronger all-tail Boolean lower-bound family.

**FULL-PROBLEM CHANGE:** none; full FEI remains OPEN / NOT PROVED.

**MECHANISM CHANGE:** yes; the new recurrence pays only the influence necessary
to transport one distinguished Fourier singleton through four nested copies.

**Remaining universal implication:** construct a finite-center all-gate
potential satisfying (G) for every gate and every product bias, or an equivalent
dimension-independent upper bound, that survives the entire spine-graft family
and other known Boolean obstructions.  A scalar center below (6.1) is impossible.

## 8. Literature/applicability check

O'Donnell--Tan's 2013 composition theorem supplies the established
disjoint-variable Fourier-composition framework.  It does not state the
shared-coordinate graft or the distinguished-spine lower-bound construction
above.  The 2026 plateaued-function theorem proves FEI with sharp constant four
on that class, and the May 2026 restriction/stopping work proves additional
classes/frameworks; neither is a universal FEI proof.  No publication-priority
claim is made for the present internal construction.

## 9. Verification scope

`CHECKER.py` uses integer Walsh transforms and `Fraction` arithmetic for the
nine-bit source core.  It recomputes the source invariants
\(\max|A|=114\), \(\max|Q|=18\), \(\sum|Q|=1584\), and
\(\sum Q^2=9216\); computes the exact first spine influence; encloses every
needed logarithm by an atanh series with an explicit rational tail; proves
(4.1)-(4.2); verifies the fixed-point interval; recomputes (5.6); and checks
the exact contraction constants (5.7)-(5.9).

The checker returned `PASS`.  It validates the stated finite arithmetic and
source-core identities only.  The universal spine and convergence statements
are proved analytically in sections 2, 3 and 5.

Scoped privacy review: this report/checker/output contain only mathematical
formulas, sanitized logical account/slot provenance, repository-relative source
references, and public-literature attribution.  They contain no credentials,
scheduler identifiers, machine paths, raw transcripts, benchmark gold, unrelated
private data, email/Drive actions, paid-model calls, remote-workflow commands, or
permission changes.
