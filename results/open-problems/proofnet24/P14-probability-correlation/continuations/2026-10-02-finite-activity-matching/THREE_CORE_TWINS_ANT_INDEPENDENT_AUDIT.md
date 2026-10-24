# Independent audit: arbitrary-terminal three-core matching family

Date: 2026-10-02. Auditor: independent `antivoter_audit` agent.

**Verdict: PASS for the stated marked pair at all activities.** I read
`TWIN_MATCHING_CORE3_ALL_TERMINAL_COUNTS.md`, the entire author verifier,
its results, and the separate queueing-agent derivation. I then derived
the forest partition function by a direct core-component classification,
without using the author's transfer matrices. The exact contraction
coefficients, cancellation, strict sign, and endpoints \(m=4,5\) all
check. No mathematical gap was found. No author file or Git state was
modified.

## 1. Independent complete enumeration by core components

For this step allow terminal \(j\) to have a common activity \(a_j\)
on its three spokes; the theorem is the special case \(a_j=a\). Set
\[
 d_j=1+3a_j,\quad u_j=\frac{a_j^2}{d_j},\quad
 v_j=\frac{a_j^3}{d_j},\quad
 X=p+q+r,\quad t=pq+pr+qr,\quad
 S=1+X+t,\quad L=3+2X.
\]
A terminal with zero or one spoke contributes \(d_j\) and does not
merge core components. A terminal using two or three spokes must meet
distinct current core components, or it creates a cycle. Classifying
by the initial core forest gives a complete enumeration:

* A core tree has total weight \(t\). No terminal may merge core
  components, giving \(t\prod_jd_j\).
* A one-edge core forest has total weight \(X\), with two core
  components of sizes two and one. At most one terminal can bridge
  them; there are two possible spoke pairs. Its contribution is
  \(X\prod_jd_j(1+2\sum_j u_j)\).
* An empty core forest starts with three components. It admits no
  bridge, one two-spoke bridge with three choices, one three-spoke
  bridge with one choice, or two two-spoke bridges on distinct
  terminals. For a specified unordered terminal pair, there are six
  choices of distinct core pairs that form a tree. No further bridge
  is possible after the three core components have merged. Its
  contribution is
  \(\prod_jd_j[1+3\sum_j u_j+\sum_jv_j+
  6\sum_{i<j}u_iu_j]\).

Thus the unmarked forest partition function is exactly
\[
 \mathcal Z(a_1,\ldots,a_k)
 =\prod_jd_j\left[S+L\sum_ju_j+\sum_jv_j
                       +6\sum_{i<j}u_iu_j\right].       \tag{A}
\]
This independently explains the multiplicity six. The author's five
partition-state transfer is equivalent: \(P^2=6Q\), and all the other
displayed products vanish because no further merger is possible. The
initial contractions \(r1=S\), \(rP1=L\), \(rQ1=1\) also follow
from this enumeration.

## 2. Marked coefficients and contraction multiplicities

The only terminal-terminal edges are the two disjoint marked matching
edges. Their four-coefficient expansion is
\(Z=A+(z_e+z_f)B+z_ez_fC\). Terminal symmetry gives equal single-mark
coefficients. A forest containing a marked edge is in weight-preserving
bijection, after removing its marked activity, with a forest in its
contracted graph. Its two parallel spokes to a given core vertex have
total effective activity \(2a\): a forest may use either one, and may
not use both. The marked edge itself causes no additional factor in
the derivative coefficient.

Consequently (A) gives
\[
 A=\mathcal Z(a,\ldots,a),\quad
 B=\mathcal Z(2a,a,\ldots,a),\quad
 C=\mathcal Z(2a,2a,a,\ldots,a),
\]
with respectively \(m,m-1,m-2\) terminals. These are exactly
\(rT(a)^m1\), \(rT(2a)T(a)^{m-2}1\), and
\(rT(2a)^2T(a)^{m-4}1\). Both marks are contracted on disjoint
terminal pairs, so there is no residual marked loop. Direct
differentiation gives \(R_{ef}=B^2-AC\), independently of either
marked activity.

## 3. Complete cancellation and positive certificate

Put \(d=1+3a\), \(h=1+6a\),
\(u=a^2/d\), \(v=a^3/d\), \(w=4a^2/h\), and
\(z=8a^3/h\). Applying (A) reproduces exactly all three normalized
quantities \(U_A,U_B,U_C\) in the author proof. Define
\[
 \delta=w-2u=\frac{2a^2}{dh},\qquad
 \kappa=\frac{6a^3(1+2ma)}{d^2h}.
\]
The first difference is
\[
 U_B-U_A=\delta L+
 [z-2v+(-12m+18)u^2+6(m-2)uw]
 =\delta L+\kappa.
\]
The second difference cancels all linear terms; its quadratic part is
\(24u^2-24uw+6w^2=6(w-2u)^2\). Therefore
\[
 U_C-2U_B+U_A=6\delta^2,\qquad
 U_B^2-U_AU_C=\delta^2[(L+\kappa/\delta)^2-6U_A].
\]
The subtraction \(-6U_A\) is retained, rather than assumed harmless.
Since \(\kappa/\delta=3a(1+2ma)/d\), its exact simplification is
\[
\begin{aligned}
 d^2[(L+\kappa/\delta)^2-6U_A]
 ={}&d^2(L^2-6S)+6ad(1+ma)L\\
    &+9a^2+30ma^3+18m^2a^4.
\end{aligned}
\]
For example the cubic and quartic contributions before simplification
are \(9a^2(1+2ma)^2-6ma^3d-18m(m-1)a^4\), which give exactly the
last three terms. Restoring \(h^2d^{2m-4}\) yields
\[
 R_{ef}=4a^4d^{2m-8}
 [d^2(L^2-6S)+6ad(1+ma)L+9a^2+30ma^3+18m^2a^4].
\]
Finally
\[
 L^2-6S=3+6(p+q+r)+4(p^2+q^2+r^2)+2(pq+pr+qr)>0
\]
for \(p,q,r\ge0\). All remaining terms are nonnegative; \(a>0\)
makes the prefactor strictly positive. This proves strict positivity
at every finite parameter choice of the stated form, including missing
core edges. At \(m=4\) and \(m=5\), the apparently concerning
\((m-4)(m-5)\) term is zero. The direct contracted-terminal counts
are nonnegative; no negative-count transfer is invoked.

## 4. Probability, multigraphs, and exact scope

The forest measure satisfies
\(\Pr(e)\Pr(f)-\Pr(e,f)=z_ez_fR_{ef}/Z^2\). Thus the covariance is
strictly negative when both marked activities are positive. Parallel
core edges aggregate by adding activities because selecting two members
of a parallel class forms a cycle. This preserves every coefficient.

The theorem covers only the two added disjoint matching edges, under
the stated equal-spoke activity model. It does not assert the Rayleigh
property for every edge pair of these graphs, arbitrary terminal edges,
arbitrary cores, or the full forest conjecture. Its analytic validity is
separate from historical novelty and external peer review, neither of
which is certified here.

## 5. Independent exact original-graph checks

New files are `three_core_twins_ant_independent_check.py` and
`three_core_twins_ant_independent_checks.json`. The checker has no
imports from the author code. It enumerates all acyclic unmarked edge
subsets, records their exact integer monomial multiplicities, and
actually inserts the two marks successively to test the mixed
coefficient. It does not use a connectivity transfer to calculate the
original-graph coefficients.

Forty rational parameter cases at \(m=4,5\) check all four coefficients
against (A) and the closed certificate. Parameters include all-zero
core weights, one and two missing core edges, nonuniform positive core
weights, and spoke activities \(1/10,2/3,1,3\). Every case passes.
Forty-two additional exact formula checks cover terminal counts through
250 and activity scales \(1/100,2/3,7\). These checks support the proof;
the complete component enumeration and algebra establish its unbounded
range.
