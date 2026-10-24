# Independent audit: heterogeneous terminal rows over a three-vertex core

Date: 2026-10-02. Auditor: independent `antivoter_audit` agent.

**Verdict: PASS for the stated matching/matching pair.** I read the
entire `forest_twin_matching_heterogeneous_core3_proof.md`, the author
exact verifier, and its results. I independently derived the partition
function by classifying bridges across the initial core components, and
independently enumerated original-graph forests at heterogeneous rational
activities. The theorem is valid with arbitrary nonnegative row
activities, provided the four marked endpoint rows are positive. No gap
was found; no author file or Git state was modified. Novelty and external
peer review are not certified.

## 1. Independent partition function

With \(d_j=1+3a_j\), \(u_j=a_j^2/d_j\), and
\(v_j=a_j^3/d_j\), the complete core-component classification gives
\[
 A=\prod_jd_j\left[S+L\sum_ju_j+\sum_jv_j
                              +6\sum_{i<j}u_iu_j\right],
\]
where \(S=1+X+t\), \(L=3+2X\), \(X=p+q+r\), and
\(t=pq+pr+qr\). A core tree admits no terminal bridge; a one-edge
core forest admits at most one bridge with two spoke-pair choices; an
empty core admits one pair bridge with three choices, one triple bridge,
or two pair bridges with six choices for each specified terminal pair.
More bridges would form a cycle. This is a full enumeration, independent
of the author's transfer operators.

Now let
\(\alpha(x)=x^2/(1+3x)\) and
\(\gamma(x)=x^3/(1+3x)^2\). The identity
\(v_j=\gamma(a_j)+3\alpha(a_j)^2\) converts the bracket into
\[
 F=S+LU+\Gamma+3U^2,
 \qquad U=\sum_j\alpha(a_j),\quad
 \Gamma=\sum_j\gamma(a_j).
\]
Thus the exponential-transfer expression in the author proof is exact:
its finite nilpotent exponential includes the required
\(3\alpha^2Q\) term, rather than inadvertently replacing
\(x^3/d\) by \(x^3/d^2\).

## 2. Exact contraction and normalization

Contracting a marked edge on rows \(a,b\) replaces them by one row
of activity \(a+b\), since parallel spoke activities aggregate. The
two marked edges are disjoint, so both contractions can be applied
independently. Define
\[
 c_i=\frac{1+3(a+b)}{(1+3a)(1+3b)},\quad
 \delta_i=\alpha(a+b)-\alpha(a)-\alpha(b),\quad
 \epsilon_i=\gamma(a+b)-\gamma(a)-\gamma(b).
\]
The common product normalization \(D=\prod_j(1+3a_j)\) changes to
\(Dc_i\). Put
\(J_i=\delta_i(L+6U)+\epsilon_i+3\delta_i^2\). The four coefficients
are therefore
\[
 A=DF,\quad B_e=Dc_e(F+J_e),\quad
 B_f=Dc_f(F+J_f),\quad
 C=Dc_ec_f(F+J_e+J_f+6\delta_e\delta_f).
\]
No terminal symmetry is assumed: generally \(B_e\ne B_f\).
Retaining the scalar factors gives exactly
\[
 R_{ef}=B_eB_f-AC
       =D^2c_ec_f[J_eJ_f-6\delta_e\delta_fF].
\]
The prefactors of the two subtraction terms coincide. No negative
term has been omitted during this cancellation.

## 3. Strict sign at every finite activity

For \(x>0\), both
\(\alpha(x)/x=x/(1+3x)\) and
\(\gamma(x)/x=[x/(1+3x)]^2\) are strictly increasing. Hence
\(\delta_i,\epsilon_i>0\) when both endpoint rows are positive.
The author's explicit formula
\[
 \delta_i=\frac{ab[2+3(a+b)]}
                 {(1+3a)(1+3b)(1+3(a+b))}
\]
is correct. Also
\[
 \alpha(x)/3-\gamma(x)
       =\frac{x^2}{3(1+3x)^2}\ge0,
\]
including \(x=0\). Thus \(\Gamma\le U/3\). Because
\(L+6U>0\), discarding the nonnegative extra terms within each
\(J_i\) preserves the product inequality. It yields
\[
\begin{aligned}
 J_eJ_f-6\delta_e\delta_fF
 &\ge\delta_e\delta_f[L^2-6S+6LU+18U^2-6\Gamma]\\
 &\ge\delta_e\delta_f[L^2-6S+(6L-2)U+18U^2]>0.
\end{aligned}
\]
Here \(L\ge3\), \(U\ge0\), and
\[
 L^2-6S=3+6X+4(p^2+q^2+r^2)+2(pq+pr+qr)>0.
\]
This proves the strict Rayleigh difference at every activity choice
in the statement. Zero unmarked rows simply add isolated terminals and
contribute \(d=1,\alpha=\gamma=0\); they cause no limiting argument.
Missing core edges are likewise covered directly. If a marked endpoint
row were zero, the strict claim would require reexamination: the draft
correctly imposes positivity at all four endpoints.

## 4. Code audit and independent checks

The author verifier directly enumerates original edge subsets and tests
the mixed marked coefficient using connectivity; it also uses an
explicit five-state frontier transition, without the nilpotent
exponential formula, for larger terminal counts. Its tests and results
are consistent with the proof. The direct cases include \(B_e\ne B_f\),
so they genuinely check the heterogeneous normalization.

New independent files are
`three_core_heterogeneous_ant_independent_check.py` and
`three_core_heterogeneous_ant_independent_checks.json`. They have no
imports from the author verifier. A recursive original-graph enumeration
records integer monomials in each separate row activity and in the
three core activities. The two marks are actually inserted successively
to test the mixed coefficient. Rational evaluation uses a common
denominator and exact integer arithmetic.

Forty direct heterogeneous rational cases at \(m=4,5\) verify all four
coefficients against the independent component formula and the exact
Rayleigh expression. Cases include an empty core, missing core edges,
unequal row weights, and rows spanning \(1/100\) to 100. Thirty further
exact formula cases cover terminal counts through 100. All pass. The
analytic enumeration and inequalities, rather than those finite checks,
prove the unrestricted terminal-count theorem.

## 5. Scope

For positive marked activities the covariance is
\(-z_ez_fR_{ef}/Z^2<0\), as the draft states. Marked activities cancel
from \(R_{ef}\) by multiaffinity. Core parallel edges aggregate exactly
because a forest cannot contain both edges of a parallel pair.

The theorem has one common spoke activity within each terminal row,
with arbitrary variation across rows. It does not permit arbitrary
three-by-\(m\) edge weights. Only the two added disjoint matching edges
are covered; there are no other terminal edges in this theorem. No
assertion about all graph edge pairs, unrestricted cores, negative
association, or the general forest conjecture follows from this audit.
