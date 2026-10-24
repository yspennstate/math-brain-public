# B13 — prime-gate reduction, and descent of the n=18 counterexample

**Run:** `20260922T002604Z-account01-B13-r11`  
**Outcome:** **CANDIDATE_REFUTED** for the current read-once-\(\Gamma\) all-gate candidate.  
**Full FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Candidate binding and change during this invocation

The owner-selected candidate at the start of this invocation was the all-gate inequality from

`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`,
blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`:

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i {\rm It}_i(G;p)\,
{\Gamma(p_i)+h(V_{p_i})\over V_{p_i}},
\qquad V_u=4u(1-u).
\tag{G}
\]

The equivalence between full FEI and the existence of **some** finite-cap symmetric
nonnegative \(\Gamma\) satisfying (G) remains the global target.

The specific candidate under test was the read-once value-iteration potential
`cert_vi_h96k40_f4`, with \(\Gamma(1/2)=C_0=6.4548\).  The prior missing implication
was that this same \(\Gamma\) satisfies (G) for every Boolean gate, equivalently that
no gate asks for a larger margin than the two-input AND obstruction.

During this invocation I consumed the newer exact account03/B15 result

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T002607Z-readonce-gamma-counterexample/REPORT.md`,
blob `e49efe403698395b700278d067c245c12a7b15eb`.

It gives a source-valid balanced 18-variable Boolean gate with
\[
I={261\over128}
\]
and certified
\[
6.776605309005978082519790221891882314787235038
\le H\le
6.776605309005978082519790221891882314787235039,
\]
hence at the uniform bias
\[
c_G
=
4\left({H\over I-1}-C_0\right)
\ge
0.2681828436921863026325758917943138734666491688421\ldots .
\tag{1}
\]
This is more than 60 times the current AND-margin scale quoted in the gate report.
Therefore the universal read-once-\(\Gamma\) candidate is **refuted**.  This does not
refute (G), the existence of some other finite-cap \(\Gamma\), or FEI.

The rest of this report applies that counterexample to the exact structural question
assigned to B13.

## 1. Exact slack for a gate

For any candidate \(\Gamma\), define
\[
A_\Gamma(u):={\Gamma(u)+h(V_u)\over V_u}
\]
and
\[
D_\Gamma(G;p)
:=
\sum_i {\rm It}_i(G;p)A_\Gamma(p_i)
-H_t(G;p)-\Gamma(p_{\rm out}).
\tag{2}
\]
Thus (G) is exactly \(D_\Gamma(G;p)\ge0\).

Also put
\[
\phi(u)=u(1-u)={V_u\over4},\qquad
K(G;p):={I(G;p)\over4}-\phi(p_{\rm out})\ge0
\tag{3}
\]
by Poincare.  Replacing \(\Gamma\) by \(\Gamma+c\phi\) gives
\[
D_{\Gamma+c\phi}(G;p)=D_\Gamma(G;p)+cK(G;p).
\tag{4}
\]
When \(K>0\), the required correction margin is
\[
c_G(p)=-{D_\Gamma(G;p)\over K(G;p)}.
\tag{5}
\]
The dangerous extremum is therefore the **maximum/supremum** of \(c_G\), not the
minimum.

## 2. Other-account composition theorem consumed and applied

I also consume account04/B14's exact result

`proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260921T151112Z-mass-weighted-erasure-composition/REPORT.md`,
blob `2b18eff89d4603663218d0ce9b31d876c17993b5`.

For a disjoint composition
\[
F(x^{(1)},\ldots,x^{(m)})
=
H(G_1(x^{(1)}),\ldots,G_m(x^{(m)})),
\tag{6}
\]
its Theorem 2.1 proves the exact hierarchical spectral sampler: first draw the
biased spectral subset \(A\) of the outer gate \(H\), and for each \(j\in A\) draw
an independent nonempty spectral set of \(G_j\), normalized by its nonconstant
spectral mass \(V_{q_j}\), where \(q_j=\Pr[G_j=1]\).  It also proves
\[
{\rm It}_i(F)
=
{\alpha_j\over V_{q_j}}{\rm It}_i(G_j),
\qquad
i\in{\rm block}\ j,
\qquad
\alpha_j=\Pr[j\in A]={\rm It}_j(H).
\tag{7}
\]

Applying that sampler to Shannon entropy gives a new exact identity needed here.
Let \(r_j\) denote the normalized nonempty spectral law of \(G_j\).  Since
\[
H_t(G_j)=h(V_{q_j})+V_{q_j}H(r_j),
\tag{8}
\]
the entropy chain rule for the hierarchical sampler gives
\[
H_t(F)
=
H_t(H)+
\sum_j{\alpha_j\over V_{q_j}}
\bigl(H_t(G_j)-h(V_{q_j})\bigr).
\tag{9}
\]

Substituting (7)-(9) into (2) yields the exact **gate-slack composition law**
\[
\boxed{
D_\Gamma(F)
=
D_\Gamma(H)
+
\sum_j{\alpha_j\over V_{q_j}}D_\Gamma(G_j).
}
\tag{10}
\]
There is no FEI assumption, sign deletion, arbitrary non-Boolean relaxation, or
unpaid coordinate label in (10).

Applying the same identity to \(\Gamma+c\phi\) and comparing the coefficient of \(c\)
gives
\[
\boxed{
K(F)
=
K(H)+
\sum_j{\alpha_j\over V_{q_j}}K(G_j).
}
\tag{11}
\]

Hence, whenever the displayed \(K\)'s are positive,
\[
\boxed{
c_F=
{K(H)c_H+
 \sum_j{\alpha_j\over V_{q_j}}K(G_j)c_{G_j}
 \over
 K(H)+\sum_j{\alpha_j\over V_{q_j}}K(G_j)}.
}
\tag{12}
\]
So a disjoint functional composition has a required margin equal to a nonnegative
weighted average of its component margins.  The division-free form is even cleaner:
for every fixed \(c\), if every component obeys
\(D_{\Gamma+c\phi}\ge0\), then the composition obeys it.

## 3. Exact functional-decomposition criterion

Let \(G:\{0,1\}^k\to\{0,1\}\), and let \(A\subset[k]\) be proper with
\(2\le |A|\le k-1\).  For each \(a\in\{0,1\}^A\), form the cofactor
\[
R_a(x_{A^c})=G(a,x_{A^c}).
\]

**Lemma.**
There are Boolean gates \(g\) on \(A\) and \(H\) on one new bit plus \(A^c\) such that
\[
G(x)=H(g(x_A),x_{A^c})
\tag{13}
\]
if and only if the family \(\{R_a\}\) contains at most two distinct cofactor
functions.

**Proof.**
If (13) holds, \(R_a\) depends on \(a\) only through the one bit \(g(a)\), hence
there are at most two rows.  Conversely, label the at-most-two distinct rows by
0 and 1, let \(g(a)\) be the row label, and let \(H(label,b)\) equal that row's
value at \(b\).  This reconstructs \(G\) exactly.  The one-row case is block
degeneracy. \(\square\)

After deleting dummy coordinates, call \(G\) **composition-prime** when every proper
block \(A\) with \(2\le|A|\le k-1\) has at least three distinct cofactors.

Any nontrivial disjoint functional decomposition contains such an inner block.
Therefore (10) proves by induction on arity:

\[
\boxed{
\text{For a fixed }\Gamma,\text{ (G) holds for all Boolean gates}
\iff
\text{it holds for all composition-prime gates (plus the trivial unary base).}
}
\tag{14}
\]

This is a dimension-free structural reduction for **any** replacement potential, not
only for the now-refuted read-once candidate.

## 4. Apply the reduction to the account03/B15 n=18 counterexample

Let \(G_{18}\) be the balanced source-valid gate from account03/B15.  For the
read-once candidate, (1) implies
\[
D_\Gamma(G_{18};1/2,\ldots,1/2)<0.
\tag{15}
\]

Suppose \(G_{18}\) has a nontrivial functional decomposition.  Equation (10) says its
negative slack is a sum of nonnegative scalar multiples of the component slacks.
Therefore at least one strictly lower-arity component has negative slack.  If that
component is decomposable, repeat.  Degenerate coordinates can simply be deleted.
Since arity strictly decreases at every nontrivial step, the descent terminates.

Thus:

\[
\boxed{
\text{There exists a composition-prime Boolean gate of arity }\le18
\text{ that violates the read-once-}\Gamma\text{ gate inequality.}
}
\tag{16}
\]

The margin statement can be sharpened.  If no zero-\(K\) component has negative
slack, then (11)-(12) imply at each decomposition step that some child or outer
component has required margin at least the parent's.  Hence the descent yields a
composition-prime gate \(P\), at its induced product bias vector, satisfying
\[
\boxed{
c_P\ge
0.2681828436921863026325758917943138734666491688421\ldots .
}
\tag{17}
\]
If instead a zero-\(K\) component has negative slack, then no finite quadratic
\(c\phi\) correction repairs that component, which is an even stronger failure of
this candidate family.

Therefore the B15 counterexample cannot be dismissed as an artifact of a large
decomposable gate.  A genuinely composition-prime obstruction exists somewhere at
arity at most 18.

This directly kills the stronger current hope that the worst all-gate margin for the
read-once \(\Gamma\) is inherited from a decomposable/AND gate.

## 5. Small exact calculation: the old arity-three “GENUINE” worst was not prime

The inherited classifier called a gate `READONCE` only when it was assembled from
two-input AND/OR gates.  It therefore classified some arbitrary Boolean compositions
as `GENUINE`.

An exact NPN enumeration of all 256 ternary truth tables gives 14 classes:
4 degenerate, 5 functionally decomposable under criterion (13), and 5
composition-prime, with canonical representatives
\[
22,\ 23,\ 24,\ 25,\ 27.
\tag{18}
\]

The gate report's numerically worst ternary `GENUINE` truth table is `tt=6`.
For \(A=\{0,1\}\), its four cofactors as functions of \(x_2\) are
\[
(0,\neg x_2,\neg x_2,0),
\]
hence
\[
\boxed{
G_6(x_0,x_1,x_2)
=
(x_0\oplus x_1)\wedge\neg x_2 .
}
\tag{19}
\]
So it is functionally decomposable, even though it lies outside the old AND/OR-only
read-once bucket.

If \(r=p_0+p_1-2p_0p_1\) is the XOR output bias and \(s=1-p_2\), (10) gives
\[
D(G_6)=D({\rm AND};r,s)+s\,D({\rm XOR};p_0,p_1),
\tag{20}
\]
and (11) gives the analogous identity for \(K\).  Thus its observed collapse to the
binary AND boundary is explained analytically by exact composition, rather than by a
numerical coincidence.

The exact finite checker beside this report uses no floating point and makes no FEI
claim; it only verifies (18)-(19).

## 6. Boundary inheritance for any future potential

For completeness, a second structural reduction is available for any admissible
candidate \(\Gamma\) continuous on \([0,1]\) with terminal values
\(\Gamma(0)=\Gamma(1)=0\).  Fix all biases except \(p_i\).  As \(p_i\to0\) or \(1\),

- the biased spectral law converges to the corresponding cofactor's spectral law;
- spectral mass involving \(i\) vanishes;
- finite-alphabet spectral entropy converges;
- \({\rm It}_i=V_{p_i}\Pr(G_0\ne G_1)\to0\);
- every other biased influence and the output bias converge;
- the \(i\)-term in (2) equals
  \(\Pr(G_0\ne G_1)[\Gamma(p_i)+h(V_{p_i})]\to0\).

Therefore
\[
D_\Gamma(G;p)\to D_\Gamma(G|_{x_i=b};p_{-i}),
\qquad
K(G;p)\to K(G|_{x_i=b};p_{-i}).
\tag{21}
\]
So, after lower arities are established, a genuinely new obstruction can be sought
among composition-prime gates at interior biases.  Boundary collapse only inherits a
lower-arity obstruction.

## 7. Exact old/new missing implications

**Old missing implication (now false):**
the read-once fixed-point \(\Gamma\) at \(C_0=6.4548\) satisfies (G) for every gate,
or equivalently the AND/decomposable gate controls the all-arity margin.

**Exact failure:**
account03/B15's source-valid n=18 gate violates it with
\(c_G\ge0.268182843692\ldots\).  Equations (10)-(12) further imply existence of a
composition-prime violating descendant of arity at most 18.

**New missing implication for full FEI:**
construct or characterize **some** symmetric nonnegative finite-cap potential
\(\Gamma\) satisfying (G) for all composition-prime gates and all interior bias
vectors.  By (14) and (21), that would automatically extend to every gate, every
functional decomposition and every boundary case.  Conversely, any proposed
replacement potential can be falsified by searching only the prime gates.

This run does not supply such a replacement potential.

**Run classification: `CANDIDATE_REFUTED`.**  
The prime-gate reduction (14) is an essential structural theorem for the replacement
search, but the selected read-once-\(\Gamma\) candidate itself is decisively dead.
**Full FEI remains OPEN / NOT PROVED.**
