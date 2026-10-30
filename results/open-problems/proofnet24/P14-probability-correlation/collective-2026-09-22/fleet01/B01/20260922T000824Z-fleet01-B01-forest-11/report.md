# FOREST / fleet01-B01 — universal Simpson reversal, matching structure of all violations, and a quantitative correlation bound

**Outcome:** `ESSENTIAL_STEP_APPLIED`. The Grimmett–Winkler uniform-all-forests pairwise negative-correlation conjecture remains **OPEN**.

**Source scope:** finite simple graph `G`; `Phi` is uniform on all acyclic edge subsets, including the empty forest and disconnected forests. For distinct present edges `e,f`, the target is

\[
\Pr(e,f\in\Phi)\le \Pr(e\in\Phi)\Pr(f\in\Phi).
\]

No rooted-forest, spanning-tree, fixed-size, or weighted-parent statement is substituted for the source target.

## 1. Inputs consumed rather than rebuilt

This run consumed the current collective FOREST material already present in the shared archive:

1. `fleet01/B03`'s exact addability/overlap reduction. For `K=G-{e,f}`, addability indicators `(X,Y)`, cell counts `n_ij`, total `N`, and overlap reservoir `q`,
   \[
   \Delta_G(e,f)=n_{10}n_{01}-n_{00}n_{11}+Nq,
   \]
   so the source inequality is exactly
   \[
   n_{00}n_{11}\le n_{10}n_{01}+Nq.
   \]
2. `fleet03/B02`'s exact deletion/contraction identity and its observation that a lexicographically minimal source counterexample forces same-sign correlations with every third edge.
3. `fleet03/B03`'s overlap-aware three-terminal response work, including the additive reconnection coordinate `eta`; this rules out throwing away the overlap state or compressing arbitrary three-terminal pieces to only three virtual edge weights.
4. The latest authoritative P14 handoff and its restored fixed-graph Cocks scope: a simple graph known to satisfy the unit source inequality is independence-correlated under positive external fields. This is the theorem gate that makes contraction minors with parallel classes safe after simplification to positive edge weights. The same handoff preserves the 3-connected minimal-counterexample reduction and the complete source metric through nine vertices.

Primary literature behind that gate was rechecked at the bibliographic level: Semple–Welsh, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), DOI `10.1017/S0963548307008978`; Cocks, *Correlated Matroids*, CPC 17 (2008), DOI `10.1017/S0963548308009152`. Cocks' paper states equivalence of the Grimmett–Winkler graphic conjecture with the correlated-graphic-matroid formulation. No new priority claim is made here.

## 2. Minimal-counterexample conditioning gate

Assume for contradiction that the source conjecture fails, and choose a counterexample `G` lexicographically minimal in `(number of vertices, number of edges)`. Let

\[
X_h=\mathbf 1_{\{h\in\Phi\}},\qquad
C_{ij}=\operatorname{Cov}(X_i,X_j),\qquad
\rho_{ij}=\operatorname{Corr}(X_i,X_j).
\]

Every edge has nonzero variance: the empty forest omits it and its singleton forest contains it.

Fix three distinct edges `e,f,g`. Conditioning on `X_g=0` gives the uniform forest measure on `G\setminus g`. Conditioning on `X_g=1`, after deleting the compulsory edge, gives the graphic contraction `G/g`. Contraction may create loops and parallel classes. Loops never occur in a forest; a parallel class of multiplicity `k` simplifies to one edge of positive weight `k`. If the marked edges collapse into one parallel class their conditional covariance is automatically nonpositive. Otherwise the inherited fixed-graph Cocks gate plus minimality gives

\[
\operatorname{Cov}(X_e,X_f\mid X_g=0)\le0,
\qquad
\operatorname{Cov}(X_e,X_f\mid X_g=1)\le0.
\tag{2.1}
\]

This is the only place the weighted-minor theorem is used.

## 3. The universal Simpson inequality

For a binary conditioning variable, the law of total covariance is exact:

\[
C_{ef}
=(1-p_g)C_{ef\mid g=0}+p_g C_{ef\mid g=1}
+\frac{C_{eg}C_{fg}}{\operatorname{Var}(X_g)}.
\tag{3.1}
\]

Indeed, writing
`alpha_s=P(e in Phi | X_g=s)` and
`beta_s=P(f in Phi | X_g=s)`, the final term is
`p_g(1-p_g)(alpha_1-alpha_0)(beta_1-beta_0)`.

Therefore, whenever `(e,f)` is a violating pair, so `C_ef>0`, (2.1) and (3.1) imply for **every** third edge `g`

\[
\boxed{
\frac{C_{eg}C_{fg}}{\operatorname{Var}(X_g)}\ge C_{ef}>0.
}
\tag{3.2}
\]

After standardization,

\[
\boxed{
\rho_{eg}\rho_{fg}\ge \rho_{ef}>0.
}
\tag{3.3}
\]

Thus a lexicographically minimal counterexample is a universal Simpson-reversal object: conditioning on any third edge leaves the marked pair nonpositively correlated inside each stratum, while the change of conditional means across the two strata is strong enough to reverse the sign after mixing.

This recovers the sign part of the fleet03/B02 identity, but (3.3) will be used quantitatively below.

## 4. New consequence: positive-correlation classes have size at most two

Define `e ~ f` for distinct edges when `C_ef>0`, and put each edge in its own class by reflexivity.

First, the positive-correlation relation is transitive. If `C_ef>0` and `C_fg>0`, apply (3.2) to the violating pair `(e,f)` with conditioner `g`. Since `C_fg>0`, it follows that `C_eg>0`.

The current collective handoff stopped at the conclusion that the bad classes are cliques. The quantitative inequality (3.3) rules out every clique of order at least three.

Suppose distinct `e,f,g` belonged to one positive class. Put

\[
a=\rho_{ef},\qquad b=\rho_{eg},\qquad c=\rho_{fg}.
\]

All three lie strictly between `0` and `1`; strictness at `1` follows because singleton forests `{e}` and `{f}` show that distinct edge indicators are not almost surely identical. Applying (3.3) cyclically gives

\[
a\le bc,\qquad b\le ac,\qquad c\le ab.
\]

Multiplying,

\[
abc\le (abc)^2.
\]

But `0<abc<1`, a contradiction. Hence:

\[
\boxed{\text{Every nontrivial positive-correlation class has exactly two edges.}}
\tag{4.1}
\]

Equivalently, in a lexicographically minimal source counterexample the graph on `E(G)` whose edges are the violating edge-pairs is a **matching**. In particular every physical edge participates in at most one source violation.

For a violating pair `{e,f}`, every third edge `g` is therefore outside its class. By (3.2), `C_eg` and `C_fg` have the same nonzero sign; if that sign were positive then `g` would join the positive class. Consequently

\[
\boxed{
C_{eg}<0\quad\text{and}\quad C_{fg}<0
\quad\text{for every }g\notin\{e,f\}.
}
\tag{4.2}
\]

So a minimal counterexample pair is self-reinforcing but strictly suppresses, and is strictly suppressed by, every other edge.

## 5. New quantitative bound from Gram packing

Let `m=|E(G)|`, and let `{e,f}` be a violating pair. Set

\[
a=\rho_{ef}>0.
\]

For each external edge `g`, write

\[
x_g=-\rho_{eg}>0,\qquad y_g=-\rho_{fg}>0.
\]

By (3.3),

\[
x_g y_g\ge a.
\tag{5.1}
\]

Represent the correlation matrix as the Gram matrix of the standardized centered indicators

\[
U_h=\frac{X_h-\mathbb E X_h}{\sqrt{\operatorname{Var}(X_h)}}
\]

in `L^2`. Thus `||U_h||=1` and `<U_i,U_j>=rho_ij`.

Put

\[
t=-\frac{U_e+U_f}{\sqrt{2+2a}}.
\]

Then `||t||=1`, and by AM-GM and (5.1), for every external edge `g`,

\[
\langle t,U_g\rangle
=\frac{x_g+y_g}{\sqrt{2+2a}}
\ge \sqrt{\frac{2a}{1+a}}
=:c.
\tag{5.2}
\]

By (4.1), all positive-correlation classes among the `m-2` external edges have size at most two. Select one representative from every such class (singletons included). This gives

\[
r\ge \left\lceil\frac{m-2}{2}\right\rceil
\]

unit vectors `U_1,...,U_r` with pairwise inner products at most zero. Hence

\[
\left\|\sum_{i=1}^r U_i\right\|^2
=r+2\sum_{i<j}\langle U_i,U_j\rangle\le r.
\tag{5.3}
\]

On the other hand, projecting onto `t` and using (5.2),

\[
\left\|\sum_{i=1}^r U_i\right\|
\ge \left\langle t,\sum_{i=1}^r U_i\right\rangle
\ge rc.
\tag{5.4}
\]

Combining (5.3) and (5.4) yields `c^2<=1/r`. Since `c^2=2a/(1+a)`,

\[
\boxed{
\rho_{ef}=a\le \frac{1}{2r-1},
\qquad
r\ge\left\lceil\frac{m-2}{2}\right\rceil.
}
\tag{5.5}
\]

In particular,

\[
\rho_{ef}\le
\frac{1}{2\lceil(m-2)/2\rceil-1}.
\tag{5.6}
\]

Using the preserved P14 structural reduction, a vertex-minimal source counterexample is 3-connected. Complete source coverage through order nine gives `|V(G)|>=10`, hence minimum degree at least three and

\[
m\ge15.
\]

Therefore every violating pair in a minimal counterexample must satisfy the concrete universal bound

\[
\boxed{0<\rho_{ef}\le\frac1{13}.}
\tag{5.7}
\]

The bound becomes smaller automatically for denser candidate graphs.

## 6. Relation to the current overlap candidate

The fleet01/B03 reduction says a source violation is exactly

\[
n_{00}n_{11}>n_{10}n_{01}+Nq.
\tag{6.1}
\]

The present result adds two global constraints that were absent from that five-number inequality:

1. the violating pair is the **only** positive-correlation neighbor of either marked edge;
2. every third edge is strictly negatively correlated with both marked edges, and the marked positive Pearson correlation is at most `1/13` in a minimal counterexample.

This sharpens the next proof obligation. An overlap-aware switching or separator argument no longer has to control arbitrary sign patterns. To close the source conjecture it is enough to show that any strict failure of (6.1), in the minimal 3-connected setting, forces **one** third edge to have positive covariance with at least one marked edge, or forces a marked correlation larger than (5.6). Either conclusion contradicts the source-safe minimal-counterexample geometry above.

This is compatible with the fleet03/B03 `K_{3,m}` regression: that family has positive Rayleigh gap for the tested pair and therefore never enters the violating-pair regime used here.

## 7. Exact checker

The archived stdlib checker `simpson_exact_checker.py` verifies the exact binary total-covariance identity (3.1) over every labelled simple graph on two through five vertices, every unordered triple of present edges, and all three choices of conditioner. It uses exact `Fraction` arithmetic.

Archived output:

```text
graphs_checked=1098
marked_conditionings_checked=46563
law_total_covariance_failures=0
positive_pair_instances_n_le_5=0
ALL_EXACT_CHECKS_PASSED
```

The absence of positive pair instances through five vertices is expected from the inherited source baseline and is **not** used as proof of the new structural theorem. The theorem is algebraic once the minimal-minor gate (2.1) is admitted.

## 8. Status

- Parent Grimmett–Winkler conjecture: **OPEN**.
- Result proved here: universal Simpson inequality (3.2)/(3.3); positive-violation graph is a matching; every external edge is strictly negatively correlated with both members of a violating pair; quantitative bound (5.5), hence `rho<=1/13` for a preserved minimal 3-connected candidate.
- Outcome label: **`ESSENTIAL_STEP_APPLIED`**.
- External novelty/priority of the matching and `1/13` deductions: **UNVERIFIED**. Repository search did not locate these deductions, but search absence is not a priority claim.
- Next exact target: combine the overlap/reconnection state `(n_ij,q)` or the five-state/`eta` separator response with (4.2) to force a third positive covariance or violate (5.6).
