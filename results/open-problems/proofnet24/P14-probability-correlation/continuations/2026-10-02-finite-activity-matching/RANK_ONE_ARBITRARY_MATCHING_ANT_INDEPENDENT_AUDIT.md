# Independent audit: rank-one spokes and arbitrary terminal matching

Date: 2026-10-02. Auditor: independent `antivoter_audit` agent.

**Verdict: PASS for every pair of matching edges under the stated
hypotheses.** I read the full final
`forest_rank_one_core3_arbitrary_matching_proof.md`, the entire author
verifier `forest_rank_one_core3_arbitrary_matching_exact.py`, and its
`forest_rank_one_core3_arbitrary_matching_exact_results.json`. I
independently rederived the weighted core enumeration, integration of
other matching edges, response formula, and primitive-variable positive
certificate. No mathematical gap was found. No author file or Git state
was modified. This is an internal mathematical audit, not certification
of novelty or external peer review.

## 1. Weighted terminal enumeration and nilpotent rules

Let \(B=b_1+b_2+b_3>0\), \(J=b_1b_2b_3>0\), with all three
column weights positive. A terminal of row weight \(x\ge0\) has
three spoke activities \(xb_i\). Zero or one spoke contributes
\(d(x)=1+Bx\) and leaves the core partition unchanged. Two spokes
are permitted precisely when they meet different core components;
their weights are \(x^2b_ib_j\). Three spokes are permitted only
from the three-singleton core state, with weight \(x^3J\).

The weighted pair-merger operator \(P\) and triple-merger operator
\(Q\), with the latter including its weight \(J\), therefore satisfy
\[
 P^2=2BQ,\qquad PQ=QP=Q^2=0.
\]
Indeed only the three-singleton state permits two pair mergers. Their
total weight is
\(\sum_{\{i,j\}}b_ib_jb_k(b_i+b_j)=2BJ\), exactly \(2B\)
times the corresponding \(Q\) entry. From any other state, two
mergers are forbidden by acyclicity. This proves the operator identity
on every state, rather than only after taking a scalar product.

Writing \(\alpha=x^2/d\) and \(\gamma=x^3/d^2\), the exponential
terminates after the quadratic term, whose \(Q\) coefficient is
\(B\alpha^2\). Hence
\[
 d\exp(\alpha P+\gamma Q)
 =dI+x^2P+d(\gamma+B\alpha^2)Q
 =dI+x^2P+x^3Q.
\]
The weighted factor \(B\), not the unweighted value three, is required
and is present throughout the final proof. All transfer polynomials
commute, so arbitrary group order is legitimate.

## 2. Independent core-component partition formula

Put \(X=p_{12}+p_{13}+p_{23}\),
\(t=p_{12}p_{13}+p_{12}p_{23}+p_{13}p_{23}\), and \(S=1+X+t\).
The core triangle's three-edge set is cyclic and contributes nothing.
From the empty core, one weighted pair merge has total weight
\(e_2(b)=b_1b_2+b_1b_3+b_2b_3\). From a one-edge core forest
containing \(i,j\), the only possible pair bridge has total weight
\(b_k(b_i+b_j)\). Thus
\[
 L=e_2(b)+\sum_{\{i,j\}}p_{ij}b_k(b_i+b_j),
 \qquad r1=S,\quad rP1=L,\quad rQ1=J.
\]

Independently of the exponential notation, classify terminal bridges
across the initial core components. A core tree admits no terminal
bridge. A one-edge core forest admits one pair bridge. An empty core
admits one pair bridge, one triple bridge, or two pair bridges. A
specified unordered terminal pair has total two-bridge weight
\(2BJ\). No other case is acyclic. Therefore, for terminals alone,
\[
 A=\prod_jd_j\left[
 S+L\sum_j\alpha_j+J\sum_j\frac{a_j^3}{d_j}
                  +2BJ\sum_{i<j}\alpha_i\alpha_j\right].
\]
Using \(a_j^3/d_j=\gamma_j+B\alpha_j^2\) gives
\(A=D[S+LU+J\Gamma+BJ U^2]\). More generally,
\(D\exp(UP+\Gamma Q)\) has exactly this scalar forest sum. This is
a complete unrooted-forest enumeration, not a rooted-forest determinant
or an activity expansion.

## 3. Integrating all other matching edges

For a disjoint terminal pair of row weights \(a,b\) and its edge
activity \(w\ge0\), deletion/contraction gives exactly
\[
 H=T(a)T(b)+wT(a+b).
\]
Contraction aggregates the parallel spokes to \((a+b)b_i\), with
no additional factor. Because every terminal belongs to at most one
matching pair, group interiors are disjoint; their only shared boundary
is the three-vertex core. Multiplying their transfer operators still
tests cycles through the changing core partition. It does not assume
probabilistic independence of group edge sets.

Let \(k_0=d(a)d(b)\), \(k_1=d(a+b)\),
\(K=k_0+wk_1>0\), and \(\theta=wk_1/K\in[0,1]\). If the deletion
and contraction branches have coefficients \((u_0,g_0)\) and
\((u_1,g_1)\), then direct expansion in \(I,P,Q\) gives
\[
 U_H=(1-\theta)u_0+\theta u_1,
 \quad
 \Gamma_H=(1-\theta)g_0+\theta g_1
                 +B\theta(1-\theta)(u_1-u_0)^2.
\]
This is the correct sign and coefficient of the variance correction.
For example the averaged raw \(Q\) coefficient is
\(\mathbb E[g+B u^2]\), whereas an exponential with averaged
\(U_H\) has raw coefficient \(\Gamma_H+B(\mathbb Eu)^2\).
Their difference is precisely \(B\operatorname{Var}(u)\).
Dropping this correction would be incorrect; the final proof retains it.

## 4. Preservation of the margin, including zero rows

Set \(k_x=x/d(x)\). Then
\[
 \alpha(x)/B-\gamma(x)=k_x^2/B\ge0.
\]
For \(s=a+b\), the merge gap has the useful independent identity
\[
 \delta=\alpha(s)-\alpha(a)-\alpha(b)
        =\frac{k_a+k_b-k_s}{B}
        =\frac{ab(2+Bs)}{d(a)d(b)d(s)}\ge0.
\]
Monotonicity of \(k_x\) gives
\(\delta\le k_a/B\), \(\delta\le k_b/B\), and also
\(\delta\le k_s/B\). Consequently both branches have margin
at least \(B\delta^2\):
\[
 u_0/B-g_0=(k_a^2+k_b^2)/B\ge B\delta^2,
 \qquad u_1/B-g_1=k_s^2/B\ge B\delta^2.
\]
Thus the mixture correction is controlled, with the explicit bound
\[
 U_H/B-\Gamma_H
 \ge B\delta^2[1-\theta(1-\theta)]\ge0.
\]
Every term defining \(\Gamma_H\) is nonnegative as well. Multiplying
groups adds \(U_H,\Gamma_H\) and multiplies their positive scalars;
therefore the base graph with the two selected marks deleted satisfies
\(D>0\), \(U\ge0\), \(0\le\Gamma\le U/B\).

These statements hold when one or both rows in an unselected pair are
zero, when its matching activity is zero, and for singleton zero rows.
For instance a zero row paired with a positive row has \(\delta=0\)
and \(H=(1+w)T(b)\), consistent with an independently selectable
bridge. No limiting argument is needed for these cases.

## 5. Selected contractions and common scalar normalization

The four endpoints of two selected matching edges remain singleton
groups in the base graph, since the entire terminal-edge set is a
matching. For each selected pair define
\(\delta_i,\epsilon_i,c_i\) as in the proof. Positive endpoint rows
give \(\delta_i>0\) by the explicit formula. The author identity
\(\gamma''(x)=6x/(1+Bx)^4>0\) is correct and proves
\(\epsilon_i>0\). An independent alternative is that
\(\gamma(x)/x=[x/(1+Bx)]^2\) is strictly increasing.

Contracting a selected pair changes \(D,U,\Gamma\) to
\(Dc_i,U+\delta_i,\Gamma+\epsilon_i\). Other matching groups are
unchanged. With
\[
 F=S+LU+J\Gamma+BJ U^2,
 \quad X_i=\delta_i(L+2BJ U)+J\epsilon_i+BJ\delta_i^2,
\]
the four forest coefficients are exactly
\[
 A=DF,\quad B_e=Dc_e(F+X_e),\quad B_f=Dc_f(F+X_f),
 \quad C=Dc_ec_f(F+X_e+X_f+2BJ\delta_e\delta_f).
\]
Hence
\[
 R_{ef}=D^2c_ec_f[X_eX_f-2BJ\delta_e\delta_fF].
\]
Both products in the Rayleigh subtraction have the same positive
normalization. No symmetry between the two marked pairs is required.

## 6. Primitive core polynomial and final sign

The constant term of \(L^2-2BJ S\) is
\(e_2(b)^2-2BJ=\sum_{i<j}b_i^2b_j^2>0\). The coefficient of
\(p_{ij}\) is
\(2b_k^2(b_i^2+b_ib_j+b_j^2)\), the coefficient of
\(p_{ij}^2\) is \(b_k^2(b_i+b_j)^2\), and the coefficient of
\(p_{ij}p_{ik}\) is \(2b_j^2b_k^2\). These follow by expanding
\(L=e_2+\sum p_{ij}b_k(b_i+b_j)\); they agree with every coefficient
in the written certificate. There are no higher core-activity terms.
Thus the full primitive-variable polynomial is strictly positive for
all nonnegative core activities. Also \(BL>J\), already from the
positive column weights and \(L\ge e_2(b)\).

Put \(K_0=L+2BJ U>0\). Keeping the subtraction exactly and using
the preserved margin gives
\[
\begin{aligned}
 K_0^2-2BJ F
 &=L^2-2BJ S+2BJ LU+2B^2J^2U^2-2BJ^2\Gamma\\
 &\ge L^2-2BJ S+2J(BL-J)U+2B^2J^2U^2>0.
\end{aligned}
\]
Since \(X_i\ge\delta_iK_0\) and the selected gaps are positive,
the Rayleigh bracket is at least
\(\delta_e\delta_f(K_0^2-2BJ F)>0\). This proves the strict
claim for any two matching edges, after integrating every other
matching activity, at every stated finite activity.

If a selected endpoint row is zero, its corresponding
\(\delta_i=\epsilon_i=X_i=0\), \(c_i=1\), and the same exact
formula gives \(R_{ef}=0\). In particular the draft's weaker
nonnegative conclusion by continuity is valid. If a selected edge
activity itself is zero, \(R_{ef}\) remains independent of it but
the probability covariance is zero because of the activity prefactor.

## 7. Code audit and independent exact checks

The author frontier routine explicitly enumerates the eight spoke
subsets, rejects repeated existing core components, and sums the
deletion/contraction branches for every other matching edge. It does
not compute its coefficients using \(\alpha,\gamma,U,\Gamma\).
Its initial core states and weight ordering are correct. The original
subset routine also correctly tests the two marks by connectivity.
The reported exact values agree with these calculations. The author
direct subset cases contain only the two selected marks; its additional
matching-edge tests use explicit frontier enumeration.

To independently test that latter integration on the actual original
graph, I wrote `rank_one_matching_ant_independent_check.py` and
`rank_one_matching_ant_independent_checks.json`, with no author imports.
The recursive enumeration inserts the two selected edges successively
and includes an unselected third matching edge among the unmarked
original edges. Two six-terminal cases enumerate respectively 165,056
and 36,352 acyclic subsets and yield exact Rayleigh values
\[
 658564909074680544,
 \qquad 2491856304025/322486272.
\]
They agree with the author frontier results, the response formula, and
an independently coded polynomial-basis product calculation. The second
case has rational row/column/core activities, a zero unselected row,
and a missing core edge.

The new checker also tests 36 rational examples through 100 terminals
using direct \((I,P,Q)\)-basis multiplication, without exponential
logarithms or the preserved-margin bound to calculate the coefficients.
It includes zero unselected rows and matching activities. Four further
examples set each selected endpoint row to zero in turn and confirm the
exact zero Rayleigh difference. All checks pass. Finite checks support
the complete analytic argument; they do not establish its unbounded
range by extrapolation.

## 8. Scope and status

The theorem covers rank-one spoke activities \(a_jb_i\), three positive
column weights, nonnegative core activities, and a terminal-terminal
matching. Only pairs of matching edges are asserted. It does not cover
arbitrary three-by-terminal spoke weights, overlapping terminal edges,
spoke/core pairs, the full forest Rayleigh conjecture, or negative
association. Core parallel classes aggregate by summing activities
because a forest cannot use two edges from such a class.

For positive selected activities,
\(\Pr(e)\Pr(f)-\Pr(e,f)=z_ez_fR_{ef}/Z^2>0\), so their covariance
is strictly negative. The sign and normalization in the probability
statement are correct. This full-activity result on the stated unbounded
family is internally verified; historical priority and external peer
review remain separate questions.
