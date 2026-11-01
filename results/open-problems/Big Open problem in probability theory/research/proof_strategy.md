# Proof strategy

## Main target

Prove:

\[
    p_c(G)<p_{2\to 2}(G)
\]

for every connected, locally finite, quasi-transitive, nonamenable graph \(G\).
This implies \(p_c(G)<p_u(G)\).

## Starting point: Hutchcroft's criterion

Let \(T_p(x,y)=\tau_p(x,y)=\mathbb P_p(x\leftrightarrow y)\), and let
\[
    \bar\chi_p=\sup_x\sum_y \tau_p(x,y).
\]

Hutchcroft gives a criterion reducing \(p_c<p_{2\to 2}\) to two near-critical
conditions:

1. mean-field susceptibility upper bound:
   \[
      \limsup_{p\uparrow p_c}(p_c-p)\bar\chi_p<\infty;
   \]
2. finite-set escape:
   \[
      \lim_{p\uparrow p_c}\sup_{K\subset V\text{ finite}}
      \frac{\sum_{x,y\in K}\tau_p(x,y)}{\bar\chi_p |K|}=0.
   \]

The second condition says that a uniformly chosen amount of two-point mass
cannot remain trapped inside an arbitrary finite set near criticality.

## Working conjectural bridge

The missing global bridge is:

> Nonamenability plus quasi-transitivity forces finite-set escape for the
> critical two-point kernel.

This is true in several known geometric settings by specialized methods. The
research task is to prove it without assuming hyperbolicity, planarity,
nonunimodularity, or product structure.

## Route A: normalized-kernel escape

Define the normalized kernel
\[
    Q_p(x,y)=\frac{\tau_p(x,y)}{\bar\chi_p}.
\]

The finite-set condition is
\[
    \sup_K |K|^{-1}\sum_{x,y\in K}Q_p(x,y)\to0.
\]

This resembles a vanishing Folner-type condition for the sub-Markov kernels
\(Q_p\). The immediate goal is to show that if this fails, then one can extract
finite sets that are almost invariant for a natural symmetrized kernel, and
then convert those sets into Folner sets for the graph, contradicting
nonamenability.

## Route A2: finite-volume/boundary dichotomy

Round 002 added a BK-based last-exit decomposition. For a finite set \(K\), let
\(\tau_p^K\) be the two-point function restricted to the induced subgraph on
\(K\), let
\[
  \chi_p^K(x)=\sum_{y\in K}\tau_p^K(x,y),
\]
and let \(\partial^+K\) be the oriented edge boundary from \(K\) to
\(V\setminus K\). Then
\[
  \sum_{x,y\in K}\tau_p(x,y)
  \le
  \sum_{x,y\in K}\tau_p^K(x,y)
  +
  p^2
  \sum_{\substack{(a,b)\in\partial^+K\\(d,c)\in\partial^+K}}
  \chi_p^K(a)\tau_p(b,c)\chi_p^K(d).
\]

Consequently, if normalized trapped mass persists, either:

1. the finite induced graph on \(K\) has susceptibility comparable to the
   ambient \(\bar\chi_p\); or
2. the boundary susceptibility weights have large interaction through the
   ambient graph under the normalized kernel \(Q_p\).

Important correction: in the last-exit proof, the middle path between the
first exit and last re-entry need not stay outside \(K\). It may make
additional excursions through \(K\). The correct middle connection is therefore
the ambient \(\tau_p(b,c)\), not a complement-restricted two-point function.

The boundary alternative can be rewritten using the boundary weight
\[
  \mu_{p,K}(z)=\sum_{\substack{a\in K\\a\sim z}}\chi_p^K(a),
  \qquad z\notin K.
\]
Since \(Q_p\) is an \(\ell^2\)-contraction,
\[
  p^2\langle \mu_{p,K},Q_p\mu_{p,K}\rangle
  \le p^2\|\mu_{p,K}\|_2^2.
\]
Thus the boundary alternative forces
\[
  \|\mu_{p,K}\|_2^2\gtrsim |K|.
\]

This is now the sharpest local bottleneck. A future proof should rule out both
alternatives uniformly near \(p_c\) using nonamenability.

## Route A3: killed-SAW interior criterion

Round 004 added an interior criterion based on killed self-avoiding path
counts.  Let \(c_n^K(x)\) be the number of length-\(n\) self-avoiding paths
starting at \(x\) and staying in \(K\), and let
\[
  A_n(K)=|K|^{-1}\sum_{x\in K}c_n^K(x).
\]
The union bound gives
\[
  S_p(K)/|K|\le \sum_{n\ge0}p^n A_n(K).
\]
Therefore, if \(A_n(K)\le C\theta^n\) uniformly over finite \(K\), with
\(\theta<1/p_c\), then
\[
  \sup_K S_p(K)/(\bar\chi_p|K|)\to0
\]
as \(p\uparrow p_c\). This rules out the interior alternative.

## Route A4: deterministic boundary norms

Round 004 also added deterministic bounds for the boundary weight
\(\mu_{p,K}\). If \(G\) has maximum degree \(\Delta\), then
\[
  \|\mu_{p,K}\|_1\le \Delta B_p(K),\qquad
  \|\mu_{p,K}\|_\infty\le \Delta M_p(K),
\]
and
\[
  \|\mu_{p,K}\|_2^2\le \Delta^2 M_p(K)B_p(K)\le \Delta^2M_p(K)S_p(K).
\]
Thus the boundary alternative forces
\[
  M_p(K)B_p(K)\gtrsim |K|.
\]

This exposes a limitation: nonamenability alone gives a lower bound on
boundary size, while the needed estimate must control susceptibility-weighted
boundary concentration or the energy
\(\langle\mu_{p,K},Q_p\mu_{p,K}\rangle\).

## Route A5: combined finite-set escape criterion

Round 005 packages Routes A3 and A4 into a theorem. Define
\[
  \kappa_{\rm kill}(G)
  =
  \limsup_{n\to\infty}
  \left(\sup_{K\subset V\text{ finite}} A_n(K)\right)^{1/n}
\]
and
\[
  \mathcal E_p(K)=p^2|K|^{-1}
  \langle\mu_{p,K},Q_p\mu_{p,K}\rangle.
\]
If
\[
  \kappa_{\rm kill}(G)<1/p_c(G)
\]
and
\[
  \sup_K\mathcal E_p(K)\to0\quad\text{as }p\uparrow p_c,
\]
then finite-set escape follows.  With Hutchcroft's mean-field susceptibility
input, this gives \(p_c<p_{2\to2}\le p_u\).

This criterion is now the best theorem-shaped intermediate target.  The next
research task is not to restate finite-set escape, but to verify the two
inputs in a natural graph class not already covered by known results.

## Route A6: killed growth calibration on regular trees

For the \(d\)-regular tree \(T_d\), the killed connective constant is
\[
  \kappa_{\rm kill}(T_d)=\sqrt{d-1}.
\]
The upper bound uses the spherical operator \(R_n\) on \(T_d\):
\[
  R_nf(x)=\sum_{y:d(x,y)=n}f(y),
  \qquad
  \|R_n\|_{2\to2}\le C_d(n+1)(d-1)^{n/2}.
\]
For every finite \(K\), killed self-avoiding paths of length \(n\) inside
\(K\) are bounded by the number of pairs of vertices of \(K\) at ambient
distance \(n\), hence
\[
  A_n(K)\le C_d(n+1)(d-1)^{n/2}.
\]
The lower bound comes from balls of radius \(m\): pairs of vertices on
different principal branches at depth \(m\) give
\[
  A_{2m}(B_m)\gtrsim (d-1)^m.
\]
Since \(p_c(T_d)=1/(d-1)\), the killed-growth hypothesis
\(\kappa_{\rm kill}<1/p_c\) holds on regular trees.

The same estimate proves finite-set escape directly on \(T_d\).  Since
\[
  \tau_p(x,y)=p^{d(x,y)}
\]
and
\[
  \bar\chi_p=1+d\sum_{n\ge1}(d-1)^{n-1}p^n,
\]
we get
\[
  \sup_K |K|^{-1}\sum_{x,y\in K}Q_p(x,y)
  \le
  \frac{C_d}{\bar\chi_p}
  \sum_{n\ge0}(n+1)(p\sqrt{d-1})^n
  \to0
\]
as \(p\uparrow p_c\).

For the general criterion, this still does not settle the boundary-energy
estimate
\[
  \sup_K\mathcal E_p(K)\to0.
\]

Round 045 verifies this boundary-energy estimate on regular trees.  The proof
uses \(\sup_{p\le p_c}\|T_p\|_{2\to2}<\infty\), bounds the boundary
susceptibility vector by \(T_p\mathbf 1_K\), obtains
\(\|\mu_{p,K}\|_2^2=O(|K|)\), and then gains the normalizing factor
\(\|Q_p\|_{2\to2}=O(1/\bar\chi_p)\).  This calibrates the condition but is
circular as a general proof strategy, since the desired open theorem is itself
an \(L^2\)-boundedness statement.

The tree calculation suggests looking for Haagerup-type \(L^2\) radial bounds,
SAW-sphere operator bounds, or median decompositions as a route to finite-set
escape in broader classes.

## Route A7: global SAW operator gap

Define \(C_n(x,y)\) to be the number of length-\(n\) self-avoiding paths from
\(x\) to \(y\), and set
\[
  \gamma_{\rm SAW,2}(G)=
  \limsup_{n\to\infty}\|C_n\|_{2\to2}^{1/n}.
\]
If
\[
  \gamma_{\rm SAW,2}(G)<1/p_c(G),
\]
then the union bound
\[
  T_p(x,y)\le \sum_{n\ge0}p^nC_n(x,y)
\]
implies \(\|T_p\|_{2\to2}<\infty\) for some \(p>p_c\).  Hence
\[
  p_c(G)<p_{2\to2}(G).
\]
If \(\bar\chi_p\to\infty\), the same uniform bound gives finite-set escape:
\[
  \sup_K |K|^{-1}\sum_{x,y\in K}Q_p(x,y)
  \le \|T_p\|_{2\to2}/\bar\chi_p\to0.
\]

This route is stronger than the conditional boundary-energy criterion.  It is
unlikely to hold in full generality, but it is a clean sufficient condition
and may capture tree-like or Haagerup-radial classes.

Round 008 adds the amenable guardrail.  If \(G\) is connected, transitive,
amenable, and bounded degree, then
\[
  \gamma_{\rm SAW,2}(G)=\mu(G),
\]
where \(\mu(G)\) is the usual connective constant.  Since the standard
self-avoiding-path bound gives \(p_c(G)\ge1/\mu(G)\), the strict gap
\(\gamma_{\rm SAW,2}<1/p_c\) cannot hold on amenable transitive graphs.  Thus
Route A7 uses nonamenability in a real way: on amenable graphs, Folner sets
turn the \(L^2\) operator norm back into row-sum growth.

Next A7 stress test: products \(T_d\times H\).  The unknown is whether the
tree factor lowers the \(L^2\) SAW growth enough to beat \(1/p_c\), or whether
mixed self-avoiding paths make the global operator gap too strong for product
graphs.

Round 009 adds the product lower bound.  For connected infinite bounded-degree
graphs,
\[
  \gamma_{\rm SAW,2}(G\square H)
  \ge
  \gamma_{\rm SAW,2}(G)+\gamma_{\rm SAW,2}(H).
\]
The proof shuffles a SAW in \(G\) with a SAW in \(H\), giving the binomial
factor
\[
  C_n^{G\square H}\ge \binom nk C_k^G\otimes C_{n-k}^H.
\]
For \(T_d\square H\) with \(H\) amenable transitive,
\[
  \gamma_{\rm SAW,2}(T_d\square H)\ge \sqrt{d-1}+\mu(H).
\]
Therefore Route A7 can only prove the product case if
\[
  p_c(T_d\square H)<\frac{1}{\sqrt{d-1}+\mu(H)}.
\]
This is a necessary condition, not a disproof of the route.  It gives a
concrete comparison to make against known or numerical estimates for product
critical probabilities.

Round 010 adds a coarse positive product theorem.  Let \(T_d\) be the
\(d\)-regular tree, \(q=d-1\), and let \(H\) have adjacency operator \(A_H\).
Since every SAW is a walk,
\[
  \gamma_{\rm SAW,2}(T_d\square H)
  \le 2\sqrt q+\|A_H\|_{2\to2}.
\]
The product contains \(T_d\), so \(p_c(T_d\square H)\le1/q\).  Therefore, if
\[
  2\sqrt q+\|A_H\|_{2\to2}<q,
\]
then
\[
  p_c(T_d\square H)<p_{2\to2}(T_d\square H).
\]
It is enough to assume \(2\sqrt{d-1}+\Delta_H<d-1\).  This proves Route A7 is
not empty on products, but it leaves low-branching products such as
\(T_3\square\mathbb Z\) untouched.

Round 011 improves the product estimate using nonbacktracking walks.  If
\(X\) is \(D\)-regular with adjacency norm \(\rho\), the length-\(n\)
nonbacktracking kernels satisfy a Chebyshev-type operator bound with exponent
\[
  \beta(D,\rho)
  =
  \begin{cases}
    \sqrt{D-1}, & \rho\le2\sqrt{D-1},\\
    \dfrac{\rho+\sqrt{\rho^2-4(D-1)}}{2}, & \rho>2\sqrt{D-1}.
  \end{cases}
\]
For \(T_d\square H\), with \(q=d-1\) and \(H\) \(\Delta\)-regular,
\[
  D=d+\Delta,\qquad
  \rho\le2\sqrt q+\|A_H\|_{2\to2}.
\]
Thus Route A7 proves
\[
  p_c(T_d\square H)<p_{2\to2}(T_d\square H)
\]
whenever
\[
  \beta(d+\Delta,2\sqrt{d-1}+\|A_H\|_{2\to2})<d-1.
\]
For \(H=\mathbb Z\), this holds for \(d\ge7\).  The low-branching cases
\(d=3,4,5,6\) remain outside this method.

Round 012 extracts a lattice-factor family.  For \(H=\mathbb Z^r\),
\[
  \Delta=2r,\qquad \|A_H\|_{2\to2}=2r.
\]
Writing \(s=\sqrt{d-1}\), the nonbacktracking condition becomes
\[
  s+r+\sqrt{r(2s+r-2)}<s^2.
\]
A simple sufficient condition is
\[
  s\ge2+\sqrt{2r},
\]
or equivalently
\[
  d\ge (2+\sqrt{2r})^2+1.
\]
Thus
\[
  p_c(T_d\square\mathbb Z^r)<p_{2\to2}(T_d\square\mathbb Z^r)
\]
in this high-branching lattice-factor regime.  This is still far from the
known product technology, but it sharpens the diagnostic scope of Route A7.

Round 013 packages the same calculation as a general spectral-factor
criterion.  If \(H\) is an infinite connected \(\Delta\)-regular graph and
\(\alpha=\|A_H\|_{2\to2}\), then Route A7 proves
\[
  p_c(T_d\square H)<p_{2\to2}(T_d\square H)
\]
whenever
\[
  \sqrt{d-1}\ge 2+\max\{\sqrt\alpha,\Delta^{1/4}\}.
\]
This criterion is weaker than the exact nonbacktracking inequality but easier
to read and apply.

Round 014 audited the nonbacktracking recurrence directly.  The recurrence
\[
  N_n=A_XN_{n-1}-(D-1)N_{n-2}\qquad n\ge3
\]
comes from prepending one edge to a length-\(n-1\) nonbacktracking path and
subtracting the \(D-1\) immediate-backtrack choices associated to each
length-\(n-2\) tail.  Small finite regular graph checks on \(C_4\), \(K_4\),
and the cube matched the recurrence through length six.

The same round extracted a clean amenable-factor consequence.  If \(H\) is an
infinite connected amenable \(\Delta\)-regular graph, then
\(\|A_H\|_{2\to2}=\Delta\) by testing \(A_H\) on Folner sets.  Hence Route A7
proves
\[
  p_c(T_d\square H)<p_{2\to2}(T_d\square H)
\]
whenever
\[
  \sqrt{d-1}\ge2+\sqrt\Delta.
\]
This packages the high-branching tree-times-amenable-factor regime without
requiring a factor-specific spectral calculation.

Round 015 improves the regular amenable-factor threshold by returning to the
exact nonbacktracking root inequality rather than using the crude
spectral-factor corollary.  If \(H\) is infinite, connected, amenable, and
\(\Delta\)-regular, then \(\|A_H\|_{2\to2}=\Delta\), so the criterion is
\[
  \beta(d+\Delta,2s+\Delta)<s^2,\qquad s=\sqrt{d-1}.
\]
This is forced by the simpler condition
\[
  s\ge1+\sqrt\Delta.
\]
Indeed, writing \(a=\sqrt\Delta\), the two inequalities needed in the larger
root case are
\[
  s^2-s-\Delta/2\ge a(a+2)/2>0
\]
and
\[
  s^2((s-1)^2-\Delta)+\Delta\ge\Delta>0.
\]
Thus Route A7 proves
\[
  p_c(T_d\square H)<p_{2\to2}(T_d\square H)
\]
for every infinite connected amenable \(\Delta\)-regular factor whenever
\[
  \sqrt{d-1}\ge1+\sqrt\Delta.
\]
For \(H=\mathbb Z\), this recovers the earlier \(d\ge7\) threshold from the
general amenable-factor statement.

Round 016 improves the specific line-factor result by pairing the
nonbacktracking SAW bound with a better upper bound on
\(p_c(T_d\square\mathbb Z)\).  In one vertical fiber, the open cluster size
\(M\) has generating function
\[
  \mathbb E[t^M]=\frac{t(1-p)^2}{(1-pt)^2}.
\]
Thus a forward tree child is reached from a vertical cluster with averaged
probability
\[
  \psi(p)=\mathbb E[1-(1-p)^M]
  =
  1-\frac{(1-p)^3}{(1-p+p^2)^2}.
\]
The forward-tree exploration dominates a Galton-Watson process with mean
\[
  (d-1)\psi(p).
\]
Consequently \(p_c(T_d\square\mathbb Z)<p_0\) whenever
\((d-1)\psi(p_0)>1\).

For the nonbacktracking exponent
\[
  t=\sqrt{d-1}+1+\sqrt{2\sqrt{d-1}-1},
\]
one checks algebraically that \((d-1)\psi(1/t)>1\) for every \(d\ge5\).
Therefore
\[
  p_c(T_d\square\mathbb Z)<p_{2\to2}(T_d\square\mathbb Z)
  \qquad d\ge5.
\]
The unresolved line-factor cases for this route are now \(d=3,4\).

Round 017 removes the \(d=4\) line-factor obstruction by using a two-step
vertical-cluster branching comparison.  For a fixed parent-child-grandchild
line in the oriented tree, let \(\Phi(p)\) be the probability that the
available parent vertical cluster connects to the grandchild through the child
fiber after exposing all child-fiber vertical components touched by source
edges.  A component generating-function calculation gives
\[
  \Phi(p)=1-(1-p)^2H'(p),
\]
where, with \(b=1-p\), \(c=b/(1-p+p^2)\),
\[
  A_k(z)=\frac{(1+c^k)bz}{1-pbz}-\frac{c^kb^2z}{1-pb^2z},
  \qquad
  H(z)=A_2(z)+\frac{bA_1(z)^2}{1-bA_0(z)}.
\]
The two-generation process has mean \((d-1)^2\Phi(p)\).  For \(d=4\), exact
rational arithmetic at \(p_0=23/100\) gives
\[
  9\Phi(p_0)>1.
\]
Also
\[
  \sqrt3+1+\sqrt{2\sqrt3-1}<100/23,
\]
so \(p_c(T_4\square\mathbb Z)<p_0<1/\beta_4\).  Therefore
\[
  p_c(T_d\square\mathbb Z)<p_{2\to2}(T_d\square\mathbb Z)
  \qquad d\ge4.
\]
The only remaining line-factor case for this route is \(T_3\square\mathbb Z\).

Round 018 separates the reusable part of the vertical-fiber argument.  For any
infinite connected transitive factor \(H\), define
\[
  \varphi_H(p)=\mathbb E_p[1-(1-p)^{|C_H(o)|}],
\]
where \(C_H(o)\) is the \(p\)-open cluster of \(o\) inside \(H\).  The oriented
tree-fiber exploration proves
\[
  (d-1)\varphi_H(p)>1
  \quad\Longrightarrow\quad
  p_c(T_d\square H)\le p,
\]
with a strict bound if the inequality holds at \(p\).  The earlier
\(\mathbb Z\) vertical-cluster lemma is the specialization
\[
  \varphi_{\mathbb Z}(p)
  =
  1-\frac{(1-p)^3}{(1-p+p^2)^2}.
\]

The same round tested deeper fixed-ray vertical comparisons for the remaining
case \(T_3\square\mathbb Z\).  At the nonbacktracking comparison point
\[
  p=1/\beta(5,2\sqrt2+2)\approx0.265505,
\]
Monte Carlo estimates of \(2^kP_k(p)\), where \(P_k(p)\) is the probability
that a fixed descendant at tree distance \(k\) is reached through the vertical
fibers along that ray, stay below one and decrease for the tested range.  This
suggests that a fixed-depth vertical branching comparison alone is unlikely to
close the \(d=3\) case; a sharper SAW operator bound or a different
percolation comparison is probably needed.

Round 019 audits the branching language and the tempting susceptibility
shortcut.  The tree-fiber explorations should be viewed as Galton-Watson
processes whose offspring variables count the reached forward fibres; sibling
events need not be independent, but the offspring distribution has the stated
mean and different individuals use disjoint forward fibres.  This is enough
for the mean-greater-than-one survival criterion.

The same audit rules out a naive susceptibility-only corollary from the
cluster-branching proposition.  For a general integer-valued random variable
\(M\ge1\) with fixed mean \(\mu\), the quantity
\[
  \mathbb E[1-(1-p)^M]
\]
can be made arbitrarily close to \(p\) by putting almost all mass at \(M=1\)
and a tiny amount at a very large value.  Thus a lower bound on
\(\varphi_H(p)\) needs distributional information about factor clusters, such
as explicit one-dimensional cluster laws or usable tail estimates, not merely
\(\chi_H(p)\).

Round 020 tests finite-length SAW operator bounds for the remaining
\(T_3\square\mathbb Z\) case.  Since the kernels \(C_m\) are submultiplicative,
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)\le \|C_m\|_{2\to2}^{1/m}.
\]
For \(T_3\square\mathbb Z\), \(C_m\) is radial in the tree coordinate and
translation-invariant in the line coordinate.  Exact enumeration of endpoint
coefficients, combined with the tree sphere norms, gives the following
rigorous finite-length bounds:
\[
  \|C_{12}\|^{1/12}\le 3.683286,\qquad
  \|C_{13}\|^{1/13}\le 3.669978,\qquad
  \|C_{14}\|^{1/14}\le 3.657847.
\]
For \(m=12\), the exact norm is
\[
  \|C_{12}\|=3110764+2209048\sqrt2.
\]
These finite-length bounds improve the nonbacktracking exponent
\(\beta(5,2\sqrt2+2)\approx3.766408\), but not nearly enough to combine with
the current vertical-branching \(p_c\) upper bounds.  The computation is
reproducible with `scripts/saw_spherical_bound.py`.

Round 022 replaces the direct labelled-tree DFS by a quotient-state dynamic
program.  The state is the finite rooted visited tree decorated by the visited
height set in each fiber and by the current fiber/height.  Children are treated
as unordered, while a move to a new child carries multiplicity \(3\) at the root
and \(2\) elsewhere.  This still counts labelled SAWs exactly, but it reaches
one additional length:
\[
  \|C_{15}\|_{2\to2}
  =
  134618428+95108784\sqrt2,
  \qquad
  \|C_{15}\|_{2\to2}^{1/15}\le3.647512.
\]
The computation is reproducible with `scripts/saw_quotient_bound.py`.  The
improvement confirms that finite-length self-avoidance is moving in the right
direction, but the root remains far above the later decorated-strip target
\(20000/5863\).

Round 035 tests a simpler finite-memory operator-side diagnostic.  A
memory-\(m\) walk is forbidden to step onto any of its previous \(m\) vertices;
every SAW is such a walk.  The row-sum growth of this finite-state class gives
a crude upper bound for \(\gamma_{\rm SAW,2}\).  Quotienting recent tree
coordinates by permutations of the three tree generators gives
\[
\begin{array}{c|cccccccccc}
m&1&2&3&4&5&6&7&8&9&10\\
\hline
\rho_{\rm row}(m)&5&4&4&3.87971935539&3.87971935539&
3.84797493536&3.84797493536&3.83468427516&
3.83468427516&3.82813327169.
\end{array}
\]
The first improvement occurs when elementary squares are forbidden.  Even at
memory \(10\), however, the row-growth bound is far above
\(20000/5863\approx3.41122\).  Thus a successful operator-side estimate must
use \(L^2\) radial/cancellation structure, not just local connective-growth
constraints.

Round 036 adds exactly that spherical evaluation for finite-memory walks.  The
script `memory_walk_spherical_bound.py` aggregates memory-\(m\) endpoints by
tree radius and height and applies the tree spherical norm.  Validation gives
the unrestricted operator scale \(2\sqrt2+2\) for memory \(1\), length \(6\).
The longer diagnostics are
\[
\begin{array}{c|cccccc}
(m,n)&(4,12)&(4,16)&(6,12)&(6,16)&(8,12)&(8,14)\\
\hline
\|D_n^{(m)}\|_{2\to2}^{1/n}
&3.72912495963039&3.69947391546724&3.69916541538674&
3.66431090701598&3.68832795340348&3.66622361402831.
\end{array}
\]
These are much better than row sums but still only comparable to, and weaker
than, the exact SAW finite-length bound \(3.64751153264\).  Finite-memory
overcounts therefore do not currently supply the missing operator-side gap.

Round 037 audits Yamamoto's 2017 and 2018 \(T_d\Box\mathbb Z\) papers as
possible external inputs.  The 2017 paper proves
\[
  p_c(T_d\Box\mathbb Z)\le 1/d
\]
for \(d\ge3\), plus \(p_c(T_4\Box\mathbb Z)<0.225\); the 2018 paper proves the
fixed-direction characterization
\[
  p_c(T_d\Box\mathbb Z)=\alpha^{-1}(1/(d-1)).
\]
For \(d=3\), the explicit 2017 bound \(1/3\) is weaker than the current
decorated-strip certificates.  Thus the external audit confirms the
\(\alpha(p)\) framework but does not improve the remaining
\(T_3\Box\mathbb Z\) bottleneck.

Round 038 pushes the depth-one decorated-strip computation to height \(11\).
Two code changes make this practical.  First,
`scripts/decorated_strip_float_scan.py` now has a specialized depth-one ladder
transfer and uses a weighted zeta transform for the subset summation in
matrix-vector multiplication.  Second,
`scripts/decorated_strip_fixedp_certificate.py` checks one rational \(p\) at a
time by propagating exact integer numerators, avoiding the full open-edge
polynomial.  The fixed-rational checker reproduces the known height-nine
certificate and then gives, for the height-eleven strip,
\[
  p=\frac{5883}{20000},\qquad
  \min_A \frac{2(M(p)v)_A}{v_A}>1.000116.
\]
Thus Yamamoto's criterion now yields
\[
  p_c(T_3\square\mathbb Z)<\frac{5883}{20000}=0.29415,
\]
and the current SAW target becomes
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<\frac{20000}{5883}
  \approx3.39963.
\]

Round 039 adds transition caching to the depth-one ladder routines and pushes
the same fixed-rational decorated-strip certificate to height \(12\).  The
floating scan brackets the crossing by
\[
  \rho_{\rm lower}(0.2930)=0.499793285995,\qquad
  \rho_{\rm lower}(0.2935)=0.501033137927.
\]
At the rational value
\[
  p=\frac{5863}{20000}=0.29315,
\]
the exact checker gives matrix size \(4095\), edge count \(34\), and
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.000320.
\]
Thus the current decorated-strip certificate is
\[
  p_c(T_3\square\mathbb Z)<\frac{5863}{20000}=0.29315,
\]
and the current SAW target is
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<\frac{20000}{5863}
  \approx3.41122.
\]

Round 040 closes the line-factor bottleneck by a direct two-point-operator
argument from Yamamoto's \(\alpha(p)\) machinery.  Let \(b=d-1\), and for a
fixed tree vertex \(x_n\) at distance \(n\), put
\[
  I_n(p)=\sum_{k\in\mathbb Z}
  \mathbb P_p((o,0)\leftrightarrow (x_n,k)).
\]
Yamamoto proves that for \(p<p_u(T_d\square\mathbb Z)\), \(I_n(p)\) is finite,
submultiplicative, and
\[
  \lim_n I_n(p)^{1/n}=\alpha(p)<b^{-1/2}.
\]
Thus \(I_n(p)\le C\theta^n\) for some \(\theta<b^{-1/2}\).  Decomposing the
two-point kernel as
\[
  T_p=\sum_{n,k}a_{n,k}(p)R_n\otimes S^k,\qquad
  \sum_k a_{n,k}(p)=I_n(p),
\]
and using \(\|R_n\|_{2\to2}\le C_d(n+1)b^{n/2}\), gives
\[
  \|T_p\|_{2\to2}
  \le C'\sum_n(n+1)(\theta\sqrt b)^n<\infty.
\]
Hence \(p_{2\to2}(T_d\square\mathbb Z)\ge p_u(T_d\square\mathbb Z)\).  Since
the reverse inequality is general, \(p_{2\to2}=p_u\).  Hutchcroft's
\(p_c<p_u\) theorem for \(T_d\square\mathbb Z\), \(d\ge3\), then gives
\[
  p_c(T_d\square\mathbb Z)<p_{2\to2}(T_d\square\mathbb Z)
  \qquad(d\ge3).
\]
Thus the \(T_3\square\mathbb Z\) case is no longer a bottleneck for the product
stress test; the next target is to abstract this mechanism beyond line
factors.

Round 041 extracts that abstraction as a fiber-summed tree criterion.  For a
transitive factor \(H\), define
\[
  I_n(p)=\sum_{y\in V(H)}
  \mathbb P_p((o_T,o_H)\leftrightarrow (x_n,y)).
\]
If \(I_0(p)<\infty\) and \(\limsup_n I_n(p)^{1/n}< (d-1)^{-1/2}\), then the
tree-distance decomposition of \(T_p\), Schur's test on the \(H\)-fiber
kernels, and \(\|R_n\|_{2\to2}\le C_d(n+1)(d-1)^{n/2}\) imply
\[
  \|T_p\|_{2\to2}<\infty.
\]
The next genuinely general step is therefore to produce such transverse
summed-mass decay without relying on the special one-dimensional Yamamoto
theory.

Round 042 compares this criterion with Hutchcroft--Pan's 2024 theorem.  Their
dimension-jump paper already proves the stronger identity
\[
  p_{2\to2}(G)=p_u(G)
\]
for \(G=T\times H\), where \(H\) is any infinite amenable Cayley graph, and for
the lamplighter graph over \(T\); in fact they identify this value with the
nonunimodular tilted and heaviness thresholds for the natural end-fixing group.
Thus the line-factor theorem in this draft should be treated as a transparent
special derivation from Yamamoto's one-dimensional exponent, not as a new
product theorem.

The mechanism to abstract is Hutchcroft--Pan's nonunimodular
Hammersley--Welsh route.  They compare slab connection probabilities \(P_p(n)\)
with slab expected masses \(E_p(n)\) by subgroup relativization and relative
sharpness, prove a backscattering lower bound that forces the directional
exponent to be at least \(1/2\) below \(p_u\), and then use a
Hammersley--Welsh inequality to make \(\chi_{p,1/2}\) finite.  The next serious
generalization target is therefore not another amenable-product proof, but a
version of this relative/tilted mechanism for nonamenable graphs with a
nontrivial quotient or normal amenable direction beyond the exact models
covered by their theorem.

The broader nonunimodular class is already handled for the stronger target:
Hutchcroft's nonunimodular theorem gives \(p_c<p_t\), while the standard
tilted-to-\(L^2\) comparison gives \(p_t\le p_{2\to2}\).  Thus the residual
global problem consists of graphs with no available nonunimodular
quasitransitive action.  Any attempt to copy the Hutchcroft--Pan product proof
into this residual setting must replace the modular height and tilted
mass-transport principle with a new intrinsic height, separator, or
probabilistic escape mechanism.

Round 046 removes an unnecessary product assumption from the operator endpoint.
Suppose the vertices of \(G\) are partitioned into fibers \((F_u)_{u\in T_d}\)
over a regular tree and define
\[
  J_n(p)=
  \sup_{\operatorname{dist}_{T_d}(u,v)=n}
  \max\left\{
    \sup_{a\in F_u}\sum_{c\in F_v}\tau_p(a,c),
    \sup_{c\in F_v}\sum_{a\in F_u}\tau_p(a,c)
  \right\}.
\]
If \(J_0(p)<\infty\) and
\[
  \limsup_n J_n(p)^{1/n}< (d-1)^{-1/2},
\]
then \(T_p\) is \(\ell^2\)-bounded.  This quotient-tree criterion is the
operator endpoint needed for graph bundles and lamplighter-type quotients; the
remaining hard part is proving the inter-fiber row/column decay in a setting
not already covered by nonunimodular or product theorems.

Round 047 generalizes the same operator endpoint to arbitrary base graphs.  If
\[
  V(G)=\bigsqcup_{u\in V(B)}F_u
\]
and \(S_n^B\) is the distance-\(n\) sphere kernel of \(B\), the block-Schur
argument gives \(L^2\)-boundedness whenever
\[
  \sum_{n\ge0}J_n(p)\|S_n^B\|_{2\to2}<\infty.
\]
In exponential form, it is enough that
\[
  \limsup_n J_n(p)^{1/n}
  <
  \left(\limsup_n\|S_n^B\|_{2\to2}^{1/n}\right)^{-1}.
\]
Thus the real operator input is not the tree structure itself but the
\(\ell^2\)-growth of distance spheres in the quotient/base graph.  This opens a
search direction through hyperbolic bases, graph bundles, and other quotients
with Haagerup-type radial estimates.

Round 048 packages two practical special cases.  With singleton fibers,
\[
  \tau_p^{\max}(n)=
  \sup_{\operatorname{dist}_G(x,y)=n}\tau_p(x,y)
\]
and the criterion becomes
\[
  \sum_{n\ge0}\tau_p^{\max}(n)\|S_n^G\|_{2\to2}<\infty
  \quad\Longrightarrow\quad
  p\le p_{2\to2}(G).
\]
For uniformly bounded fibers over a base \(B\), the same conclusion follows
from pointwise inter-fiber decay because finite fiber size only changes the
row/column sums by a constant factor.  The next proof target can therefore be
stated as an off-diagonal decay problem: prove that two-point probabilities
decay across shells faster than the \(L^2\)-growth of the corresponding sphere
kernels.

Round 049 shows that this decay only needs to be established at \(p_c\).  If
\(T_{p_0}\) is \(L^2\)-bounded for some \(p_0<1\), Russo's formula and BK give,
in finite volume,
\[
  \frac{d}{dp}T_p\le T_pAT_p,
\]
and hence
\[
  \|T_q\|_{2\to2}
  \le
  \frac{\|T_{p_0}\|_{2\to2}}
       {1-\Delta\|T_{p_0}\|_{2\to2}(q-p_0)}
\]
for \(q>p_0\) sufficiently close.  Therefore, when \(p_c<1\), boundedness of
\(T_{p_c}\) already implies \(p_c<p_{2\to2}\).  Combining this with the
pointwise shell criterion gives the new concrete target
\[
  \sum_{n\ge0}\tau_{p_c}^{\max}(n)\|S_n^G\|_{2\to2}<\infty
  \quad\Longrightarrow\quad
  p_c<p_{2\to2}.
\]

Round 050 packages this summability condition into a purely exponential
critical-shell test.  Define
\[
  \rho_{\mathrm{sph},2}(G)
  =
  \limsup_{n\to\infty}\|S_n^G\|_{2\to2}^{1/n},
  \qquad
  \alpha_c^{\max}(G)
  =
  \limsup_{n\to\infty}\tau_{p_c}^{\max}(n)^{1/n}.
\]
If
\[
  \alpha_c^{\max}(G)\rho_{\mathrm{sph},2}(G)<1,
\]
then the critical shell sum converges and hence \(p_c<p_{2\to2}\).  The next
compact target is therefore to prove
\(\alpha_c^{\max}(G)<\rho_{\mathrm{sph},2}(G)^{-1}\).  This target uses actual
critical two-point decay rather than a union bound over self-avoiding paths, so
it is weaker in favorable geometries than demanding a global SAW operator gap.

Round 051 gives a combinatorial way to attack the Round 050 target without
returning to the full global SAW operator norm.  Let \(C_m(x,y)\) be the number
of length-\(m\) self-avoiding paths from \(x\) to \(y\), and define
\[
  U_n^{\mathrm{SAW}}(p)
  =
  \sup_{\operatorname{dist}(x,y)=n}\sum_{m\ge n}p^m C_m(x,y),
  \qquad
  \beta_c^{\mathrm{SAW,end}}
  =
  \limsup_{n\to\infty}
  \bigl(U_n^{\mathrm{SAW}}(p_c)\bigr)^{1/n}.
\]
The endpoint SAW shell criterion says that
\[
  \beta_c^{\mathrm{SAW,end}}\rho_{\mathrm{sph},2}(G)<1
  \quad\Longrightarrow\quad
  p_c<p_{2\to2}.
\]
This follows because an open connection contains at least one open
self-avoiding witness, so
\(\tau_{p_c}^{\max}(n)\le U_n^{\mathrm{SAW}}(p_c)\).  The condition remains a
union-bound route, but it is shell-resolved and fixed-endpoint rather than a
global \(\ell^2\) SAW growth condition.

Round 052 extracts a more checkable excess-length version.  Let
\[
  E_{n,k}^{\mathrm{SAW}}
  =
  \sup_{\operatorname{dist}(x,y)=n} C_{n+k}(x,y),
\]
so \(k\) records the detour length beyond a geodesic.  If
\[
  E_{n,k}^{\mathrm{SAW}}\le A a^n r^k,\qquad p_c r<1,
  \qquad p_c a\,\rho_{\mathrm{sph},2}(G)<1,
\]
then \(p_c<p_{2\to2}\).  This turns the endpoint shell route into two
separate deterministic counting targets: the exponential cost of moving
distance \(n\), and the exponential cost of adding detours.

Round 053 adds the parallel nonbacktracking version.  Let
\[
  E_{n,k}^{\mathrm{NB}}
  =
  \sup_{\operatorname{dist}(x,y)=n} N_{n+k}(x,y),
\]
where \(N_m(x,y)\) counts length-\(m\) nonbacktracking walks from \(x\) to
\(y\).  Since every self-avoiding walk is nonbacktracking, the same conditions
\[
  E_{n,k}^{\mathrm{NB}}\le A a^n r^k,\qquad p_c r<1,
  \qquad p_c a\,\rho_{\mathrm{sph},2}(G)<1
\]
imply \(p_c<p_{2\to2}\).  This gives a standard transfer-matrix target while
preserving the fixed-endpoint and excess-length resolution that the global
nonbacktracking operator route loses.

Round 054 weakens the separable \(a^n r^k\) target to a shell generating
function.  Define
\[
  V_n^{\mathrm{NB}}(p)
  =
  \sup_{\operatorname{dist}(x,y)=n}
  \sum_{k\ge0}p^kN_{n+k}(x,y),
  \qquad
  \delta_c^{\mathrm{NB,end}}
  =
  \limsup_{n\to\infty}
  \bigl(V_n^{\mathrm{NB}}(p_c)\bigr)^{1/n}.
\]
Then
\[
  p_c\,\delta_c^{\mathrm{NB,end}}\rho_{\mathrm{sph},2}(G)<1
  \quad\Longrightarrow\quad
  p_c<p_{2\to2}.
\]
This is the more natural computational target: estimate the whole
\(p_c\)-weighted detour series for fixed endpoints at distance \(n\), rather
than forcing a product-form bound in \(n\) and \(k\).

Round 055 translates the same target into nonbacktracking bridge probabilities
on \(D\)-regular graphs.  If \((X_m)\) is nonbacktracking random walk and
\[
  B_n^{\mathrm{NB}}(s)
  =
  \sup_{\operatorname{dist}(x,y)=n}
  \sum_{k\ge0}s^k\mathbf P_x^{\mathrm{NB}}(X_{n+k}=y),
\]
define
\[
  \lambda_c^{\mathrm{NB,br}}
  =
  \limsup_{n\to\infty}
  \bigl(B_n^{\mathrm{NB}}(p_c(D-1))\bigr)^{1/n}.
\]
Since
\[
  N_m(x,y)=D(D-1)^{m-1}\mathbf P_x^{\mathrm{NB}}(X_m=y),
\]
the Round 054 criterion becomes
\[
  p_c(D-1)\lambda_c^{\mathrm{NB,br}}\rho_{\mathrm{sph},2}(G)<1
  \quad\Longrightarrow\quad
  p_c<p_{2\to2}.
\]
This is now a large-deviation bridge estimate for nonbacktracking random walk,
which is a more standard probabilistic object than raw path counts.

Round 056 adds two calibrations.  First, if
\(\mathcal P_{\mathrm{NB}}\) is the nonbacktracking transition operator on
directed edges of a \(D\)-regular graph and
\[
  \sigma_{\mathrm{NB},2}
  =
  \limsup_m\|\mathcal P_{\mathrm{NB}}^m\|_{2\to2}^{1/m},
\]
then the bridge criterion follows from the stronger global conditions
\[
  p_c(D-1)\sigma_{\mathrm{NB},2}<1,\qquad
  p_c(D-1)\sigma_{\mathrm{NB},2}\rho_{\mathrm{sph},2}(G)<1.
\]
This is convenient but coarse: it bounds endpoint probabilities by a global
directed-edge \(L^2\) norm.  Second, on the \(D\)-regular tree,
\[
  \lambda_c^{\mathrm{NB,br}}(T_D)=\frac1{D-1}.
\]
The bridge criterion then gives
\[
  p_c(T_D)(D-1)\lambda_c^{\mathrm{NB,br}}(T_D)
  \rho_{\mathrm{sph},2}(T_D)=\frac1{\sqrt{D-1}}<1.
\]
Thus the bridge-resolved target recovers the tree model exactly, while global
spectral control should be treated only as a diagnostic sufficient condition.

Round 057 gives a finite-state certificate format for the bridge target.  For
a \(D\)-regular graph, put \(s_c=p_c(D-1)\).  If a finite nonnegative transfer
matrix \(M\) and vectors \(a,b\) satisfy
\[
  B_n^{\mathrm{NB}}(s_c)\le a^TM^nb
  \qquad(n\ge1),
\]
then
\[
  p_c(D-1)\rho(M)\rho_{\mathrm{sph},2}(G)<1
  \quad\Longrightarrow\quad
  p_c<p_{2\to2}.
\]
This provides a concrete output format for future radial, automaton, or
finite-quotient computations: produce a matrix majorant for weighted
nonbacktracking bridges and check its Perron root against the sphere-kernel
growth.

Round 058 removes the need to know \(p_c\) exactly when producing such a
certificate.  If \(q\ge p_c(G)\), \(s_q=q(D-1)\), and
\[
  B_n^{\mathrm{NB}}(s_q)\le a^TM^nb\qquad(n\ge1),
\]
then
\[
  q(D-1)\rho(M)\rho_{\mathrm{sph},2}(G)<1
  \quad\Longrightarrow\quad
  p_c<p_{2\to2}.
\]
This is the practical certificate: combine any independent upper bound
\(p_c\le q\) with a finite-state bridge overcount at \(q(D-1)\).

Round 059 turns the certificate into an exact-checking format.  If
\(R\ge\rho_{\mathrm{sph},2}(G)^2\), \(Mv\le\lambda v\) coordinatewise for
some \(v>0\), and
\[
  \bigl(q(D-1)\lambda\bigr)^2R<1,
\]
then \(\rho(M)\le\lambda\), so the Round 058 certificate applies.  The script
`scripts/bridge_certificate_verify.py` checks this Collatz--Wielandt part of a
certificate using exact rational arithmetic.  The bridge-majorization
inequality \(B_n^{\mathrm{NB}}(q(D-1))\le a^TM^nb\) remains the
problem-specific part that a radial or automaton computation must justify.

Round 060 hardens the verifier workflow.  The command
`python scripts/bridge_certificate_verify.py --self-test` now checks both the
valid toy \(T_3\) certificate and the expected failures for negative matrix
entries, nonpositive Collatz vectors, failed \(Mv\le\lambda v\), and failed
final strict inequalities.  The file `research/certificates/README.md`
documents the JSON schema and explicitly separates the exact algebra check
from the graph-specific bridge-majorization proof.

Round 061 adds collection-level certificate checking.  The command
`python scripts/bridge_certificate_verify.py --directory research\certificates`
verifies every JSON certificate in the directory and reports the exact final
value for each one.  This makes the algebraic audit scalable once there are
families of finite-state bridge certificates, while preserving the same
separation from the graph-specific bridge-majorization proof.

Round 062 adds a guardrail connecting global nonbacktracking growth to the
spherical \(L^2\) growth term.  If \(\mathcal P_{\mathrm{NB}}\) is the
nonbacktracking transition operator on directed edges of a \(D\)-regular graph,
then
\[
  \rho_{\mathrm{sph},2}(G)
  \le (D-1)\sigma_{\mathrm{NB},2}(G).
\]
The proof dominates the distance-\(n\) sphere kernel by the length-\(n\)
nonbacktracking-walk count kernel and factors that count kernel through
\(\mathcal P_{\mathrm{NB}}^{n-1}\).  Consequently the earlier directed-edge
criterion follows from the stronger square condition
\[
  p_c(G)\bigl((D-1)\sigma_{\mathrm{NB},2}(G)\bigr)^2<1.
\]
This is useful as a diagnostic but not as the main route: on regular trees the
global criterion is at the critical boundary, while the bridge-resolved
certificate has the strict margin.

Round 063 tightens the JSON certificate schema to match the finite-state
bridge theorem more closely.  The theorem's majorization uses boundary vectors
\(a,b\) in
\[
  B_n^{\mathrm{NB}}(q(D-1))\le a^TM^nb.
\]
The checker now requires `left_vector` and `right_vector`, verifies that they
have the same dimension as \(M\), verifies nonnegativity, and rejects all-zero
boundary vectors.  This is still not a check of the graph-specific
majorization, but it prevents malformed algebra certificates from passing the
Collatz--Wielandt audit.

Round 064 closes the regular-tree certificate example end to end.  The checker
now supports the graph-specific mode `regular_tree_one_state`, which proves
the exact \(D\)-regular tree bridge calculation
\[
  B_n^{\mathrm{NB}}(s)=\frac{1}{D(D-1)^{n-1}}
\]
against the one-state finite-state bound \(aM^nb\) for every \(n\ge1\).  For
the repository certificate \(D=3\), \(M=(1/2)\), \(a=b=1\), this gives
\[
  \frac{1}{3\cdot2^{n-1}}\le\left(\frac12\right)^n.
\]
This gives one fully checkable graph-specific calibration while leaving all
non-tree radial or automaton majorizations as separate mathematical
obligations.

Round 065 extracts a general adjacency-spectrum square criterion from the
existing nonbacktracking polynomial bound.  For a \(D\)-regular graph with
adjacency operator norm \(\rho_A\), let
\[
  \beta(D,\rho_A)
  =
  \begin{cases}
    \sqrt{D-1}, & \rho_A\le2\sqrt{D-1},\\
    \dfrac{\rho_A+\sqrt{\rho_A^2-4(D-1)}}2, & \rho_A>2\sqrt{D-1}.
  \end{cases}
\]
If
\[
  p_c(G)\beta(D,\rho_A)^2<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).  The proof uses the operator bound
\(\|N_m\|_{2\to2}\le C\theta^m\) for nonbacktracking count kernels, gives
\(\alpha_c^{\max}\le p_c\theta\), and also bounds
\(\rho_{\mathrm{sph},2}\le\theta\).  This is a useful coarse diagnostic, but
on regular trees it gives equality \(p_c\beta^2=1\), so it cannot replace the
bridge-resolved route.

Round 066 adds a nonhomogeneous block certificate.  The finite-state bridge
criterion asks for a homogeneous bound \(B_n^{\mathrm{NB}}(q(D-1))\le a^TM^nb\),
but radial or first-descent computations will often produce a product of
level-dependent nonnegative matrices
\[
  \mu_{x,y}^TK_{1,x,y}\cdots K_{n,x,y}h_{x,y}.
\]
If \(\mu_{x,y}\le a\), \(h_{x,y}\le b\), and every block satisfies
\(K_{r,x,y}\le M\) coordinatewise, then the product is bounded by \(a^TM^nb\).
Thus the same finite-state criterion applies.  This makes the graph-specific
bridge-majorization obligation more modular: one only has to prove local block
dominance and a uniform finite-state envelope.

Round 067 expands the graph-specific side into a path-sum transfer
certificate.  A bridge trajectory from \(x\) to \(y\), with
\(\operatorname{dist}(x,y)=n\), may be injectively decomposed into \(n\)
finite-state phases
\[
  \sigma_0,f_1,\sigma_1,\ldots,f_n,\sigma_n.
\]
If its weighted contribution \(s_q^k\mathbb P_x^{\mathrm{NB}}(\gamma)\) is
bounded by
\[
  \mu_{x,y}(\sigma_0)\prod_{r=1}^n w_{r,x,y}(f_r)h_{x,y}(\sigma_n),
\]
and the phase sums define matrices \(K_{r,x,y}\le M\), then summing over all
encoded trajectories gives the nonhomogeneous block certificate.  This is the
formal template for radial, first-descent, or automaton computations: prove an
injective decomposition and local phase bounds, then hand off to finite
matrix algebra.

Round 068 broadens the finite-state route beyond regular graphs.  The
regular bridge-probability certificate is convenient, but the open problem is
for bounded-degree quasi-transitive graphs.  The count-kernel detour criterion
already works at this level.  If \(q\ge p_c(G)\) and a finite-state matrix
\(M\) satisfies
\[
  \sup_{\operatorname{dist}(x,y)=n}\sum_{k\ge0}q^kN_{n+k}(x,y)
  \le a^TM^nb
  \qquad(n\ge0),
\]
then \(\delta_c^{\mathrm{NB,end}}\le\rho(M)\).  Hence
\[
  q\rho(M)\rho_{\mathrm{sph},2}(G)<1
  \quad\Longrightarrow\quad
  p_c(G)<p_{2\to2}(G).
\]
This is now the most general finite-state certificate target in the draft:
regularity is needed only when rewriting the same data as nonbacktracking
transition probabilities.

Round 069 makes the bounded-degree count-kernel certificate exact-checkable.
The manuscript now has a Collatz form: if \(M v\le\lambda v\), \(R\ge
\rho_{\mathrm{sph},2}(G)^2\), and
\[
  (q\lambda)^2R<1,
\]
then the Round 068 certificate implies \(p_c(G)<p_{2\to2}(G)\).  The checker
now has an explicit `criterion` field.  `regular_bridge` checks
\(\bigl(q(D-1)\lambda\bigr)^2R<1\), while `bounded_degree_detour` checks
\((q\lambda)^2R<1\).  A second regular-tree calibration file,
`regular_tree_D3_detour.json`, exercises the bounded-degree mode and verifies
the exact count-kernel one-state majorization \(V_n^{\mathrm{NB}}(q)=1\).

Round 070 adds the bounded-degree path-sum detour certificate.  This is the
raw-count analogue of the regular path-sum transfer certificate: for each
nonbacktracking walk from \(x\) to \(y\) of length \(n+k\), one injectively
encodes the walk by \(n\) phases
\[
  \sigma_0,f_1,\sigma_1,\ldots,f_n,\sigma_n
\]
and proves
\[
  q^k\le \mu_{x,y}(\sigma_0)\prod_{r=1}^n w_{r,x,y}(f_r)h_{x,y}(\sigma_n).
\]
If the phase-sum matrices satisfy \(K_{r,x,y}\le M\), summing over all encoded
walks gives
\[
  \sum_{k\ge0}q^kN_{n+k}(x,y)\le a^TM^nb.
\]
Thus the Round 068 bounded-degree detour certificate applies.  This is now
the cleanest graph-specific template for the full quasi-transitive setting:
prove an injective phase decomposition and local finite-state domination for
raw nonbacktracking counts.

Round 071 applies the bounded-degree raw-count certificate to semiregular
trees.  For the \((a,b)\)-semiregular tree, with
\(r=(a-1)(b-1)>1\), the two-type branching threshold gives
\(p_c=r^{-1/2}\).  A two-type Schur estimate for distance-sphere kernels gives
\(\rho_{\mathrm{sph},2}\le r^{1/4}\), so
\[
  p_c\rho_{\mathrm{sph},2}\le r^{-1/4}<1.
\]
Tree detours have \(V_n^{\mathrm{NB}}(p_c)=1\), so the bounded-degree detour
certificate applies with \(M=(1)\).  The exact rational \((2,3)\)-semiregular
calibration uses \(q=3/4\), \(R=3/2\), \(M=(1)\), and final check
\((q\lambda)^2R=27/32<1\).

Round 072 packages the tree calculation for universal covers of finite graphs.
If \(H\) is finite and the directed nonbacktracking matrix \(B\) is irreducible
with Perron radius \(\beta>1\), then the universal-cover tree \(T=\widetilde H\)
has
\[
  p_c(T)=\beta^{-1},
  \qquad
  \rho_{\mathrm{sph},2}(T)\le\sqrt\beta.
\]
The \(p_c\) equality is the multitype branching threshold for the open
nonbacktracking descendant process.  The spherical estimate uses a
Perron-weight Schur test with
\(\phi(x)=u_{\operatorname{type}(\epsilon_x)}\beta^{-d(o,x)/2}\).  Since
trees have no non-geodesic nonbacktracking detours, \(M=(1)\) and
\(p_c\rho_{\mathrm{sph},2}\le\beta^{-1/2}<1\).  This closes the finite-type
tree calibration; cycles remain the source of the real detour problem.

Round 073 adds a deliberately coarse cyclic calibration: finite-fiber
high-branching tree bundles.  For a graph on \(V(T_d)\times F\) with vertical
finite-fiber adjacency \(A_0\) and symmetric horizontal coupling matrix \(P\),
the adjacency operator is
\[
  A_{T_d}\otimes P+I\otimes A_0.
\]
If \(b=d-1\), \(P(i_0,i_0)=1\), and
\[
  2\sqrt b\,\|P\|+\|A_0\|<b,
\]
then the graph contains a copy of \(T_d\), so \(p_c\le1/b\), while the SAW
operator exponent is at most the displayed adjacency norm.  Hence
\(p_c<p_{2\to2}\).  Concrete cyclic consequences are
\(T_d\square K_2\) for \(d\ge7\) and \(T_d\square C_m\) for \(d\ge9\).  This
does not touch low-branching products, but it is the first explicit
finite-fiber cyclic bundle calibration in the manuscript.

Round 074 sharpens the finite cyclic examples by observing that the
nonbacktracking product theorem works equally well for finite regular factors.
For a finite connected \(\Delta\)-regular factor \(H\),
\(\|A_H\|_{2\to2}=\Delta\), and Proposition `nb-product` gives the condition
\[
  \beta(d+\Delta,2\sqrt{d-1}+\Delta)<d-1.
\]
Checking the quadratic root explicitly improves the cyclic thresholds to
\[
  T_d\square K_2:\ d\ge5,\qquad
  T_d\square C_m:\ d\ge7.
\]
This is still high branching and still runs through the strong SAW operator
gap, but it is a genuine improvement over the adjacency-walk cyclic
calibration.

Round 075 combines the finite-factor nonbacktracking exponents with a
finite-factor version of the cluster-branching \(p_c\) upper bound.  The
cluster-branching proposition now allows finite transitive factors.  For
\(K_2\),
\[
  \varphi_{K_2}(p)=p+p^2-p^3,
\]
so at \(p=3/10\), \(3\varphi_{K_2}(p)>1\).  Since
\(\beta(5,2\sqrt3+1)<10/3\), this closes \(T_4\square K_2\).  For \(C_m\),
the two root incident fibre edges give the uniform lower bound
\[
  \varphi_{C_m}(p)\ge1-(1-p)(1-p^2)^2.
\]
At \(p=1/5\) this closes \(T_5\square C_m\), and at \(p=19/100\) it closes
\(T_6\square C_m\).  Together with Round 074, the cyclic finite-factor class is
now
\[
  T_d\square K_2:\ d\ge4,\qquad
  T_d\square C_m:\ d\ge5.
\]

Round 076 closes the remaining two-layer finite factor \(T_3\square K_2\).
The \(p_c\)-upper side uses a two-type reached-subset branching process in the
fibres of \(K_2\).  At \(p=39/100\), the singleton/doubleton mean matrix has a
Collatz lower vector \(v=(1,7/4)\), with \(Mv>v\), so
\[
  p_c(T_3\square K_2)<39/100.
\]
The operator side uses an exact length-15 self-avoiding endpoint enumeration
on \(T_3\square K_2\), quotienting tree labels.  The certificate gives
\[
  \|C_{15}\|_{2\to2}\le639862+452048\sqrt2
  <(100/39)^{15}.
\]
Submultiplicativity yields
\(\gamma_{\rm SAW,2}(T_3\square K_2)<100/39<1/p_c\), hence
\[
  p_c(T_d\square K_2)<p_{2\to2}(T_d\square K_2)\qquad d\ge3.
\]
The exact arithmetic is reproduced by `scripts/k2_saw_certificate.py`.

Round 077 closes \(T_4\square C_m\) for all finite cycles \(C_m\), \(m\ge3\).
The proof again combines finite-fibre cluster branching with finite-length SAW
operator certificates.  The cluster side uses \(p=6/25\) for \(C_3\),
\(p=19/80\) for \(C_4\), and \(p=47/200\) for all \(m\ge5\).  For \(m\ge7\),
a uniform local lower bound exposing three fibre edges in each direction gives
\(3\varphi_{C_m}(47/200)>1\).  The length-11 SAW certificates are
\[
\begin{aligned}
  C_3:&\quad \|C_{11}\|\le2649944+1532806\sqrt3<(25/6)^{11},\\
  C_4:&\quad \|C_{11}\|\le3554176+2043694\sqrt3<(80/19)^{11},\\
  m\ge5:&\quad \|C_{11}\|\le4074050+2347722\sqrt3<(200/47)^{11}.
\end{aligned}
\]
Together with Round 075, this proves
\[
  p_c(T_d\square C_m)<p_{2\to2}(T_d\square C_m)
  \qquad d\ge4,\ m\ge3.
\]
The quotient enumeration and arithmetic are reproduced by
`scripts/cycle_saw_certificate.py`.

Round 078 audits the remaining \(d=3\) finite-cycle stress test
\(T_3\square C_m\), \(m\ge3\).  This family is already covered by the known
hyperbolic-graph theorem, since it is quasi-isometric to a regular tree, but it
is a useful diagnostic for the elementary certificate route.  The scalar
cycle-cluster bound has threshold tending to \(p\approx0.3276217564\), far too
high for the current SAW roots.  A new floating-point reached-subset branching
scan, `scripts/cycle_subset_branching_scan.py`, improves the \(p_c\)-upper
diagnostics to
\[
\begin{array}{c|c|c}
m& p_{\rm subset}&1/p_{\rm subset}\\
\hline
3&0.317132230751&3.153258808\\
4&0.305160759915&3.276961298\\
5&0.300234054466&3.330734756\\
6&0.298002864821&3.355672438\\
7&0.296940367281&3.367679542\\
8&0.296420873959&3.373581579 .
\end{array}
\]
The operator side remains too large: the length-\(11\) quotient-SAW roots are
\[
\begin{array}{c|c}
m&\|C_{11}\|_{2\to2}^{1/11}\\
\hline
3&3.510460092\\
4&3.630232944\\
5&3.674388421\\
6&3.691848908\\
7&3.697288328\\
8&3.699063401,
\end{array}
\]
and even the length-\(13\) \(C_3\) root is \(3.462720635\), still far above the
subset-branching target.  Thus exact rationalization of the current finite-SAW
data is not the next useful move for \(T_3\square C_m\); any elementary proof
would need a different \(p_{2\to2}\)-side mechanism.

Round 079 returns to the finite-set escape abstraction and adds a
separator-convolution criterion.  If a finite set \(K\) is partitioned into
pieces \(K_i\), and \(W_{ij}\) separates every path from \(K_i\) to \(K_j\),
then BK gives, for \(i\ne j\),
\[
  \sum_{x\in K_i,y\in K_j}\tau_p(x,y)
  \le
  \sum_{z\in W_{ij}}
  \Bigl(\sum_{x\in K_i}\tau_p(x,z)\Bigr)
  \Bigl(\sum_{y\in K_j}\tau_p(y,z)\Bigr).
\]
Thus finite-set escape follows if the same-piece mass is \(o(\chi_p|K|)\) and
the separator convolution on the right is also \(o(\chi_p|K|)\), uniformly for
near-critical \(p\).  This is a more faithful abstraction of the hyperbolic
half-space mechanism than the earlier scattering definition: the graph-specific
input is no longer a raw separator size but a weighted two-point convolution
through the separator.  The manuscript now states the corresponding uniform
critical separator-convolution property and the conditional theorem
\[
  \text{separator-convolution property}+\text{MF}
  \Longrightarrow
  p_c(G)<p_{2\to2}(G).
\]

Round 080 audits that abstraction and fixes an endpoint degeneracy.  If
separators may contain endpoints, the singleton partition with \(W_{xy}=\{x\}\)
makes the convolution term exactly \(\tau_p(x,y)\), so the property merely
restates finite-set escape.  The manuscript now uses a buffered partition
\[
  K=K_0\sqcup K_1\sqcup\cdots\sqcup K_m
\]
and requires proper separators
\[
  W_{ij}\cap(K_i\cup K_j)=\varnothing
\]
for \(i,j\ge1\).  The buffer has its own normalized mass term
\[
  \mathcal B_p(K_0;K)=
  \frac{2}{\chi_p|K|}\sum_{x\in K_0,y\in K}\tau_p(x,y).
\]
The corrected criterion says that if the buffer mass, same-piece mass, and
proper separator-convolution mass are all \(o(1)\) uniformly near criticality,
then finite-set escape follows.  This makes the separator-convolution property
a non-tautological target for future geometric or group-theoretic arguments.

Round 081 removes a second tautology from the separator target.  Even with
proper separators, the abstract property can hide all work in one piece
\(K_1=K\).  The manuscript now defines a local separator-convolution property:
for every \(\delta>0\), near criticality every finite \(K\) must admit a
buffered partition with non-buffer pieces of uniformly bounded diameter
\[
  \operatorname{diam}(K_i)\le R(\delta),
\]
small buffer mass, and small proper separator-convolution mass.  Bounded
diameter makes the same-piece term automatic: if the maximum degree is
\(\Delta\), then each piece has at most
\[
  V_R=1+\Delta\sum_{\ell=0}^{R-1}(\Delta-1)^\ell
\]
vertices, so
\[
  \sum_i\sum_{x,y\in K_i}\tau_p(x,y)\le V_R|K|.
\]
Since \(\chi_p\to\infty\) as \(p\uparrow p_c\), this normalized same-piece term
is \(o(1)\).  The new conditional theorem is therefore
\[
  \text{local separator-convolution property}+\text{MF}
  \Longrightarrow
  p_c(G)<p_{2\to2}(G).
\]
This is a sharper intermediate target: a future proof must really build
bounded-diameter pieces, a low-mass buffer, and weighted proper separators.

Round 082 calibrates the local separator-convolution property on regular
trees.  Root \(T_d\), choose a large integer \(L\), and let
\[
  S_r=\{x:\operatorname{dist}(o,x)\equiv r\pmod L\}.
\]
For a finite \(K\), choose \(r\) with \(|K\cap S_r|\le |K|/L\), set
\(K_0=K\cap S_r\), and let the non-buffer pieces be the intersections of
\(K\setminus K_0\) with components of \(T_d\setminus S_r\).  Their diameters
are at most \(2L\), and \(S_r\) is a proper separator between distinct pieces.
The buffer mass is at most \(2/L\).  The separator convolution is controlled by
the tree's uniform critical \(L^2\) bound:
\[
  \chi_p |K|\,\mathcal C_p
  \le
  \sum_{z\in S_r}(T_p\mathbf 1_{K\setminus K_0}(z))^2
  \le
  \sup_{s\le p_c}\|T_s\|_{2\to2}^2 |K|.
\]
Since \(\chi_p\to\infty\), this proves the local
separator-convolution property on \(T_d\).  This is only a calibration, not a
new proof mechanism for the general problem, because it uses the very
\(L^2\)-boundedness that the main conjecture seeks to obtain.

Round 083 abstracts the tree-layer geometry in that calibration, and checks
the same periodic-grid construction over products with Euclidean factors.
Suppose \(G\) admits a finite-fiber, 1-Lipschitz projection
\(\pi:G\to\mathbb T\square\mathbb Z^s\), where \(\mathbb T\) is a
bounded-degree tree:
\[
  \sup_u|\pi^{-1}(u)|<\infty,\qquad
  x\sim y\Rightarrow
  d_{\mathbb T\square\mathbb Z^s}(\pi x,\pi y)\le1.
\]
Tree and Euclidean residue hyperplanes pull back to separators
\(S_{\mathbf a}=\pi^{-1}(\Sigma_{\mathbf a})\).  The finite-fiber hypothesis
makes the components of \(G\setminus S_{\mathbf a}\) uniformly finite when
\(L\) is fixed, hence their intersections with \(K\) have bounded diameter.
Averaging over residue vectors gives a single \(\mathbf a\) for which both the
buffer mass and the separator square mass are small, provided
\[
  \limsup_{p\uparrow p_c}
  \frac{\|T_p\|_{2\to2}^2}{\bar\chi_p}<\infty.
\]
This yields the local separator-convolution property for such finite-fiber
tree-grid projections.  The note is deliberately diagnostic: when
\(\bar\chi_p\to\infty\), the same analytic bound already implies finite-set
escape by the elementary spectral estimate.  The real missing ingredient is a
way to control square two-point mass on separating grids without assuming a
conclusion-like global \(L^2\) bound.

Round 084 makes that missing ingredient explicit.  For the tree-grid
separators \(S_{\mathbf a}\), the buffer term is already small on average over
shifts.  The needed product-like estimate is
\[
  \lim_{L\to\infty}\limsup_{p\uparrow p_c}
  \sup_K
  \min_{\mathbf a}
  \frac{1}{\bar\chi_p|K|}
  \sum_{z\in S_{\mathbf a}}
    (T_p\mathbf 1_K(z))^2
  =0.
\]
This is a two-replica square-mass bound.  Hutchcroft--Pan's backscattering
argument has the same structure in \(T\times H\): if the directional exponent
is below \(1/2\), two parallel downward connections create a supercritical
embedded branching process, forcing large fiber intersections below \(p_u\).
The general separator route therefore needs a local backscattering principle
that rules out persistent square mass on separating grids without relying on a
global nonunimodular tilt.

Round 085 stress-tests the layer-square target on the amenable line.  On
\(\mathbb Z\), \(\tau_p(x,y)=p^{|x-y|}\) and
\(\bar\chi_p=(1+p)/(1-p)\).  For \(K=\{1,\ldots,N\}\) with
\(N\gg(1-p)^{-1}\), every periodic separator \(S_a=L\mathbb Z+a\) has many
interior points \(z\) with \(T_p\mathbf 1_K(z)\asymp\bar\chi_p\).  Hence
\[
  \frac{1}{\bar\chi_p|K|}
  \sum_{z\in S_a}(T_p\mathbf 1_K(z))^2
  \gtrsim
  \frac{\bar\chi_p}{L},
\]
which diverges as \(p\uparrow1\) for fixed \(L\).  Thus the layer-square
estimate is not a formal consequence of periodic separators; it must use a
genuine nonamenable/backscattering mechanism.

Round 086 adds a restricted-shell reduction for the layer-square term.  In
the setup of the base-sphere fibre criterion
\[
  V(G)=\bigsqcup_{u\in V(B)}F_u,
\]
with fibre row/column sums \(J_n(p)\), let \(M_\Sigma\) be multiplication by a
base separator \(\Sigma\subset V(B)\).  If
\[
  A_\Sigma(p)=\sum_{n\ge0}J_n(p)\|M_\Sigma S_n^B\|_{2\to2},
\]
then every finite \(K\subset V(G)\) satisfies
\[
  \sum_{z\in \cup_{u\in\Sigma}F_u}(T_p\mathbf 1_K(z))^2
  \le A_\Sigma(p)^2|K|.
\]
Thus the layer-square target follows if
\[
  \chi_p^{-1}\min_a A_{\Sigma_a}(p)^2\to0
\]
for the separator family.  This separates the problem into a percolation
input \(J_n(p)\) and a deterministic restricted-sphere estimate for
\(M_\Sigma S_n^B\).  It is the most concrete current formulation of the
backscattering route.

Round 087 records a limitation of that deterministic operator route.  For
periodic tree-level separators in a \(d\)-regular tree, with \(q=d-1\),
\[
  S_r^{(L)}=\{x:d(o,x)\equiv r\pmod L\},
\]
the distance-\(n\) sphere kernel satisfies
\[
  \|M_{S_r^{(L)}}R_n\|_{2\to2}\ge q^{n/2}
\]
for every \(L,r\), and \(n\ge1\).  The test vector is a delta mass at a
non-root vertex \(y\) whose \(n\)-descendants all land in the chosen residue
class.  Since the full tree sphere bound is
\[
  \|R_n\|_{2\to2}\le C_d(n+1)q^{n/2},
\]
periodic restrictions can remove at most the Haagerup polynomial factor in a
pure operator-norm estimate.  They cannot produce a density gain tending to
zero with \(L\).  The next route must therefore use finite-test-set averaging
over shifts or a genuinely percolative two-replica/backscattering input,
rather than relying on sparse separator operator norms alone.

Round 088 formulates that replacement as a two-replica finite-set profile.
Define
\[
  \mathcal R_p(K)
  =
  \frac{\|T_p\mathbf 1_K\|_2^2}{\bar\chi_p|K|}
  =
  \frac{1}{\bar\chi_p|K|}
  \sum_z\left(\sum_{x\in K}\tau_p(x,z)\right)^2,
  \qquad
  \mathcal R_p^*=\sup_K\mathcal R_p(K).
\]
If
\[
  \limsup_{p\uparrow p_c}\mathcal R_p^*<\infty,
\]
then finite-set escape follows immediately by Cauchy--Schwarz:
\[
  \frac{\langle\mathbf 1_K,T_p\mathbf 1_K\rangle}{\bar\chi_p|K|}
  \le
  \left(\frac{\mathcal R_p(K)}{\bar\chi_p}\right)^{1/2}.
\]
Together with the mean-field susceptibility input, this gives a new
intermediate theorem implying \(p_c<p_{2\to2}\).  For finite-fiber
tree-grid projections, the same two-replica bound also supplies the
layer-square estimate by averaging over the actual finite set \(K\):
\[
  \frac{1}{L^{s+1}}\sum_{\mathbf a}
  \frac{1}{\bar\chi_p|K|}
  \sum_{z\in S_{\mathbf a}}(T_p\mathbf 1_K(z))^2
  \le
  \frac{s+1}{L}\mathcal R_p(K).
\]
This is now the cleanest target for a nonamenable/backscattering mechanism:
prove bounded \(\mathcal R_p^*\), not a false density improvement for
restricted sphere operator norms.

Round 089 connects \(\mathcal R_p(K)\) back to standard percolation objects.
If \(\omega_1,\omega_2\) are independent percolation configurations and
\(C_i(z)\) is the cluster of \(z\) in \(\omega_i\), then
\[
  \bar\chi_p|K|\mathcal R_p(K)
  =
  \sum_z
  \mathbb E_p^{\otimes2}
  \bigl[
    |K\cap C_1(z)|\,|K\cap C_2(z)|
  \bigr].
\]
Thus \(\mathcal R_p(K)\) really is a same-root two-replica quantity.  Russo's
formula and BK also give a finite-set differential inequality: if the maximum
degree is \(\Delta\), then
\[
  \frac{S_q^{\rm amb}(K)}{|K|}
  \le
  \frac{S_p^{\rm amb}(K)}{|K|}
  +
  \Delta\int_p^q \bar\chi_s\mathcal R_s(K)\,ds .
\]
The proof uses finite-volume matrices and
\[
  \frac{d}{dp}T_p^W\le T_p^W A_WT_p^W.
\]
This makes the two-replica target a percolation-specific object accessible to
sharpness, backscattering, or differential-inequality tools, not merely an
operator proxy.

Round 090 calibrates \(\mathcal R_p^*\).  On the regular tree \(T_d\),
\[
  \lim_{p\uparrow p_c(T_d)}\mathcal R_p^*=0,
\]
because \(\sup_{p\le p_c}\|T_p\|_{2\to2}<\infty\) while
\(\bar\chi_p\to\infty\).  Indeed
\[
  \mathcal R_p(K)
  \le
  \frac{\sup_{s\le p_c}\|T_s\|_{2\to2}^2}{\bar\chi_p}
  \qquad(K\subset T_d\text{ finite}).
\]
On the amenable line \(\mathbb Z\), the opposite happens:
\[
  \lim_{p\uparrow1}\mathcal R_p^*=\infty.
\]
For \(K_N=\{1,\ldots,N\}\), \(N\asymp(1-p)^{-1}\), a positive fraction of
interior points have \(T_p\mathbf 1_{K_N}(z)\asymp\bar\chi_p\), giving
\(\mathcal R_p(K_N)\gtrsim\bar\chi_p\).  Thus the two-replica profile has the
right qualitative behavior on the basic positive and negative models.

Round 091 records that the two-replica target is also necessary for the
desired \(L^2\) gap.  If \(\bar\chi_p\to\infty\) and \(T_q\) is bounded on
\(\ell^2\) for some \(q>p_c\), then monotonicity gives \(T_p\le T_q\) for
\(p<p_c\), so
\[
  \mathcal R_p(K)
  \le
  \frac{\|T_q\|_{2\to2}^2}{\bar\chi_p}
  \qquad(K\text{ finite}).
\]
Hence \(\mathcal R_p^*\to0\).  Bounded \(\mathcal R_p^*\) is therefore not a
cheap replacement for \(p_c<p_{2\to2}\); it is a finite-indicator, two-replica
form of a necessary consequence of the target theorem.

Round 092 fixes the exact normalization.  For any positive symmetric
substochastic kernel \(Q\),
\[
  \eta(Q)=\sup_K |K|^{-1}\langle 1_K,Q1_K\rangle,\qquad
  \rho(Q)=\sup_K |K|^{-1}\|Q1_K\|_2^2
\]
satisfy
\[
  \eta(Q)^2\le \rho(Q)\le \sqrt{6\eta(Q)}.
\]
For \(Q_p=T_p/\bar\chi_p\), this means
\[
  \eta(Q_p)\to0
  \quad\Longleftrightarrow\quad
  \mathcal R_p^*/\bar\chi_p\to0.
\]
Thus finite-set escape is exactly sublinear two-replica growth, bounded
\(\mathcal R_p^*\) is a stronger backscattering target, and the desired
\(L^2\) gap would force the still stronger vanishing
\(\mathcal R_p^*\to0\).  The manuscript now includes the corresponding
sublinear two-replica criterion: mean-field susceptibility together with
\(\mathcal R_p^*/\bar\chi_p\to0\) implies \(p_c<p_{2\to2}\).

Round 093 records the equivalent squared-kernel form.  Since
\[
  \eta(Q^2)=\sup_K |K|^{-1}\|Q1_K\|_2^2,
\]
Round 092 gives
\[
  \eta(Q)^2\le\eta(Q^2)\le\sqrt{6\eta(Q)}.
\]
Thus finite-set escape for a positive symmetric substochastic kernel is
stable under squaring.  For \(Q_p=T_p/\bar\chi_p\),
\[
  \eta(Q_p^2)=\mathcal R_p^*/\bar\chi_p.
\]
The two-replica obstruction is therefore ordinary finite-set trapping for the
squared normalized two-point kernel.

Round 094 adds the local-negligibility observation for the squared kernel.  If
the degree is bounded and \(V_R=\sup_x |B(x,R)|\), then for \(i=1,2\)
\[
  \sup_K |K|^{-1}
  \sum_{\substack{x,y\in K\\ d(x,y)\le R}}Q_p^i(x,y)
  \le \frac{V_R}{\bar\chi_p}.
\]
Indeed \(Q_p(x,y)\le\bar\chi_p^{-1}\) and
\[
  Q_p^2(x,y)
  =
  \bar\chi_p^{-2}\sum_z\tau_p(x,z)\tau_p(z,y)
  \le \bar\chi_p^{-1}.
\]
Thus any failure of \(\eta(Q_p^2)\to0\), equivalently any failure of
\(\mathcal R_p^*/\bar\chi_p\to0\), must be witnessed by pairs at graph
distances tending to infinity.  The remaining task is therefore genuinely a
large-scale separator/backscattering problem, not a local clustering problem.

Round 095 opens the long-range square kernel through its common root.  If
\(\eta(Q_{p_n}^2)\ge\epsilon>0\), then there are finite \(K_n\) such that for
every fixed \(R\),
\[
  \liminf_n |K_n|^{-1}\sum_z
  \left(\sum_{\substack{x\in K_n\\ d(x,z)>R}}Q_{p_n}(x,z)\right)
  \left(\sum_{y\in K_n}Q_{p_n}(z,y)\right)
  \ge \epsilon/4.
\]
This follows because \(d(x,y)>2R\) implies that, for every intermediate root
\(z\), at least one of \(d(x,z)>R\) and \(d(y,z)>R\) holds.  Thus the
obstruction contains a same-root two-replica backscatter with one leg escaping
every fixed scale.

Round 096 strengthens the mixed far-leg product to genuine far-root square
mass.  Define
\[
  \mathcal R_p^{>R}(K)
  =
  \frac1{\bar\chi_p|K|}
  \sum_z
  \left(
    \sum_{\substack{x\in K\\d(x,z)>R}}\tau_p(x,z)
  \right)^2.
\]
If \(\eta(Q_{p_n}^2)\ge\epsilon>0\), the same witnesses may be chosen so that
for every fixed \(R\),
\[
  \liminf_n
  \frac{\mathcal R_{p_n}^{>R}(K_n)}{\bar\chi_{p_n}}
  \ge \epsilon^2/16.
\]
This is the correct far-tail statement: ordinary one-replica tail mass is
mostly automatic near criticality, while this preserves the two-replica
\(L^2\) structure after deleting every bounded neighborhood of \(K_n\).

Round 097 makes this a necessary-and-sufficient criterion.  Let
\[
  \Theta_p(R)=\sup_K\mathcal R_p^{>R}(K)/\bar\chi_p .
\]
Then
\[
  \mathcal R_p^*/\bar\chi_p\to0
\]
is equivalent to: for every \(\delta>0\), some fixed \(R\) and near-critical
window satisfy \(\Theta_p(R)\le\delta\).  The proof writes
\(Q_p1_K=u_{\le R}+u_{>R}\); the far part is \(\Theta_p(R)\), while the near
part obeys
\[
  |K|^{-1}\|u_{\le R}\|_2^2\le V_R^3/\bar\chi_p^2.
\]
Thus the remaining problem is exactly uniform tightness of the two-replica
square mass in leg length.

Round 098 packages the previous paragraph as a direct \(L^2\)-gap criterion:
under the mean-field susceptibility bound and \(\bar\chi_p\to\infty\), the
uniform far-leg estimate
\[
  \forall\delta>0\ \exists R<\infty,\ p_0<p_c:
  \sup_K\mathcal R_p^{>R}(K)/\bar\chi_p\le\delta
  \quad(p\in[p_0,p_c))
\]
implies \(p_c(G)<p_{2\to2}(G)\).  This isolates the final missing estimate in
a single citable statement.

Round 099 rewrites the same condition as the tail limit
\[
  \lim_{R\to\infty}\limsup_{p\uparrow p_c}\Theta_p(R)=0.
\]
This is equivalent to \(\mathcal R_p^*/\bar\chi_p\to0\) because
\(\Theta_p(R)\) is monotone decreasing in \(R\).  The order of limits is now
explicit: first take a near-critical limsup at a fixed leg cutoff, then send
the cutoff to infinity.

Round 100 adds the probabilistic interpretation of the far-leg tail.  For two
independent clusters \(C_1(z),C_2(z)\),
\[
  \bar\chi_p |K|\mathcal R_p^{>R}(K)
  =
  \sum_z
  \mathbf E_p^{\otimes2}
  \bigl[
    |(K\setminus B(z,R))\cap C_1(z)|
    |(K\setminus B(z,R))\cap C_2(z)|
  \bigr].
\]
Thus \(\Theta_p(R)\) is the normalized same-root two-cluster overlap after
discarding all legs of length at most \(R\).

Round 101 adds a stronger but simpler operator-tail criterion.  If
\[
  \lim_{R\to\infty}\limsup_{p\uparrow p_c}
  \|T_p^{>R}\|_{2\to2}/\bar\chi_p=0,
\]
where \(T_p^{>R}(x,y)=\tau_p(x,y)\mathbf 1\{d(x,y)>R\}\), then
\[
  \Theta_p(R)\le \|T_p^{>R}\|_{2\to2}^2/\bar\chi_p^2
\]
and hence \(p_c(G)<p_{2\to2}(G)\) under the mean-field input.  This is not the
final theorem, but it gives a clean spectral form of the far-leg estimate.

Round 102 decomposes this operator target into exact-distance shells.  With
\[
  H_{p,n}(x,y)=\tau_p(x,y)\mathbf 1\{d(x,y)=n\},
\]
the estimate
\[
  \lim_{R\to\infty}\limsup_{p\uparrow p_c}
  \bar\chi_p^{-1}\sum_{n>R}\|H_{p,n}\|_{2\to2}=0
\]
implies the operator-tail criterion and hence the \(L^2\) gap under
mean-field.  This links the far-leg program to shell-growth and
self-avoidance estimates already present elsewhere in the manuscript.

Round 103 records that the existing \(L^2\)-self-avoiding-walk gap gives
uniform exact-shell tails.  If
\(\gamma_{\mathrm{SAW},2}(G)<1/p_c(G)\), then for some
\(\theta<1/p_c\) and \(A<\infty\),
\[
  \|C_m\|_{2\to2}\le A\theta^m.
\]
Since a connection between vertices at distance \(n\) contains an open
self-avoiding path of length \(m\ge n\),
\[
  \|H_{p,n}\|_{2\to2}
  \le A\sum_{m\ge n}(p\theta)^m.
\]
Therefore
\[
  \sup_{p<p_c}\sum_{n>R}\|H_{p,n}\|_{2\to2}
  \le A\sum_{m>R}(m-R)(p_c\theta)^m\to0.
\]
Thus the far-leg/shell-tail route truly extends the old SAW route rather than
conflicting with it.

Round 104 adds an annular form of the far-leg criterion that treats cross
terms correctly.  For annuli \(I_j\) partitioning \((R,\infty)\) and weights
\(a_j>0\) with \(A=\sum_j a_j^{-1}<\infty\),
\[
  \Theta_p(R)\le A\sum_j a_j\Theta_p(I_j).
\]
This is just weighted Cauchy--Schwarz applied to
\(\sum_j u_j(z)\), but it is important because annular pieces are positive
and not orthogonal.  A dyadic sufficient condition follows: if for some
\(\alpha>0\),
\[
  \lim_{J\to\infty}\limsup_{p\uparrow p_c}
  \sum_{j\ge J}2^{\alpha(j-J)}
  \Theta_p((2^j,2^{j+1}])=0,
\]
then \(\mathcal R_p^*/\bar\chi_p\to0\).

Round 105 converts the annular criterion into an operator target.  For
\[
  T_p^I(x,y)=\tau_p(x,y)\mathbf 1\{d(x,y)\in I\},
\]
one has
\[
  \Theta_p(I)\le \|T_p^I\|_{2\to2}^2/\bar\chi_p^2.
\]
Consequently, a dyadic square-summability estimate
\[
  \lim_{J\to\infty}\limsup_{p\uparrow p_c}
  \sum_{j\ge J}2^{\alpha(j-J)}
  \left(\|T_p^{(2^j,2^{j+1}]}\|_{2\to2}/\bar\chi_p\right)^2=0
\]
implies \(\mathcal R_p^*/\bar\chi_p\to0\), and with the mean-field input gives
\(p_c<p_{2\to2}\).  This is a useful middle target between exact-shell
\(\ell^1\) control and full operator-tail control.

Round 106 connects the annular operator target to pointwise two-point decay
and spherical operator growth.  For every annulus \(I\),
\[
  \|T_p^I\|_{2\to2}
  \le
  \sum_{n\in I\cap\mathbb N}\tau_p^{\max}(n)\|S_n^G\|_{2\to2}.
\]
Consequently, under the mean-field input, it is enough to prove the normalized
dyadic tail
\[
  \lim_{J\to\infty}\limsup_{p\uparrow p_c}
  \sum_{j\ge J}2^{\alpha(j-J)}
  \left(
    \bar\chi_p^{-1}
    \sum_{2^j<n\le2^{j+1}}\tau_p^{\max}(n)\|S_n^G\|_{2\to2}
  \right)^2=0
\]
for some \(\alpha>0\).  Unlike the old critical-shell summability criterion,
this condition is normalized by \(\bar\chi_p\), so it can remain plausible in
settings where \(T_{p_c}\) is not known to be bounded.

Round 107 records that the older critical shell summability route is contained
in the new far-leg framework.  If
\[
  \sum_n \tau_{p_c}^{\max}(n)\|S_n^G\|_{2\to2}<\infty,
\]
then, uniformly in \(p<p_c\),
\[
  \|T_p^{>R}\|_{2\to2}
  \le
  \sum_{n>R}\tau_{p_c}^{\max}(n)\|S_n^G\|_{2\to2}\to0.
\]
Thus the far-leg tail is tight and
\(\mathcal R_p^*/\bar\chi_p\to0\).  The old critical-shell criterion is
therefore a strong special case of the current far-leg program.

Round 108 records the contrapositive annular obstruction.  If the normalized
far-leg term does not vanish, then for some \(\epsilon>0\) every dyadic tail
has a same-witness annular lower bound: for every \(\alpha>0\), every large
starting scale \(2^J\), and every \(p_0<p_c\), one can choose
\(p\in[p_0,p_c)\) and a finite set \(K\) such that
\[
  \sum_{j\ge J}2^{\alpha(j-J)}
  \frac{\mathcal R_p^{(2^j,2^{j+1}]}(K)}{\bar\chi_p}
  \ge (1-2^{-\alpha})\epsilon .
\]
Thus any failure of far-leg tightness must concentrate through a persistent
weighted annular profile, not merely through a loose tail supremum.

Round 109 pushes the same obstruction through the annular operator estimates.
If the normalized two-replica term does not vanish, then for some
\(\epsilon>0\) and every \(\alpha>0\),
\[
  \liminf_J\limsup_{p\uparrow p_c}
  \sum_{j\ge J}2^{\alpha(j-J)}
  \left(\frac{\|T_p^{(2^j,2^{j+1}]}\|_{2\to2}}{\bar\chi_p}\right)^2
  \ge (1-2^{-\alpha})\epsilon .
\]
For connected locally finite graphs this also forces the corresponding
pointwise shell-growth upper envelope
\[
  \sum_{j\ge J}2^{\alpha(j-J)}
  \left(
    \frac{\sum_{2^j<n\le 2^{j+1}}
      \tau_p^{\max}(n)\|S_n^G\|_{2\to2}}{\bar\chi_p}
  \right)^2
\]
to stay bounded away from zero along \(p\uparrow p_c\).  Therefore, under the
mean-field susceptibility input, any equality case \(p_c=p_{2\to2}\) must
exhibit persistent normalized annular operator mass on arbitrarily remote
dyadic tails.

Round 110 adds the elementary size control behind these witnesses.  For every
annulus \(I\) and finite \(K\),
\[
  \frac{\mathcal R_p^I(K)}{\bar\chi_p}
  \le \min\{1, |K|/\bar\chi_p\}.
\]
Consequently, the same-witness obstruction from Round 108 may be chosen with
\[
  \mathcal R_p^{>2^J}(K)/\bar\chi_p>2\epsilon,
  \qquad |K|>2\epsilon\bar\chi_p.
\]
Thus a counterexample cannot be witnessed by bounded or sub-susceptibility
sets; the obstruction is necessarily macroscopic at the near-critical
susceptibility scale.

Round 111 extracts actual remote root layers from annular square mass.  For
an interval \(I\) and threshold \(\lambda\), define
\[
  Z_p^I(K,\lambda)=
  \left\{z:\sum_{\substack{x\in K\\d(x,z)\in I}}\tau_p(x,z)
  \ge \lambda\bar\chi_p\right\}.
\]
Then
\[
  \mathcal R_p^I(K)/\bar\chi_p
  \le \lambda+|Z_p^I(K,\lambda)|/|K|.
\]
Combining this with the dyadic obstruction shows that, if far-leg tightness
fails, then for every \(0<\alpha<\beta\) and every tail start \(J\) there are
near-critical \(p\) and macroscopic \(K\) such that the weighted sum
\[
  \sum_{j\ge J}2^{\alpha(j-J)}
  \frac{|Z_p^{(2^j,2^{j+1}]}(K,\lambda_j)|}{|K|}
\]
is bounded below, with
\(\lambda_j\asymp 2^{-\beta(j-J)}\).  The remaining obstruction is therefore
geometric: large finite sets must generate many remote annular root layers
carrying susceptibility-scale mass.

Round 112 rewrites those root layers as a first-moment crossing obstruction.
For
\[
  \mathcal B_p^I(K,Z)=
  |K|^{-1}\sum_{z\in Z}\sum_{\substack{x\in K\\d(x,z)\in I}}Q_p(x,z),
\]
failure of far-leg tightness forces, for every \(0<\alpha<\beta\),
near-critical \(p\), macroscopic \(K\), and sets \(Z_j\) such that
\[
  \sum_{j\ge J}2^{(\alpha+\beta)(j-J)}
  \mathcal B_p^{(2^j,2^{j+1}]}(K,Z_j)
  \ge
  \frac{\epsilon^2}{4}(1-2^{-\alpha})^2(1-2^{\alpha-\beta}).
\]
This moves the target from quadratic annular mass to weighted first-moment
connections between one large test set and many remote receiving layers.

Round 113 removes the percolation weights from the layer-size obstruction.
Define the deterministic annular incidence layer
\[
  \mathcal N^I(K,m)=
  \{z:|\{x\in K:d(x,z)\in I\}|\ge m\}.
\]
Since \(\tau_p(x,z)\le1\),
\[
  Z_p^I(K,\lambda)\subseteq \mathcal N^I(K,\lambda\bar\chi_p).
\]
Thus, if far-leg tightness fails, the macroscopic \(K\) from Round 111 also
has many remote annular incidence layers:
\[
  \sum_{j\ge J}2^{\alpha(j-J)}
  \frac{|\mathcal N^{(2^j,2^{j+1}]}(K,m_j)|}{|K|}
  \ge
  \frac{\epsilon}{2}(1-2^{-\alpha}),
\]
where \(m_j\asymp 2^{-\beta(j-J)}\bar\chi_p\).  A final contradiction could
therefore come from a deterministic theorem saying that nonamenable
quasi-transitive graphs do not allow macroscopic finite sets to have so many
remote high-incidence annular centers at every tail scale.

Round 114 separates the deterministic incidence obstruction into a finite
window alternative.  Fix a dyadic tail start \(J\), a finite window length
\(H\), and \(\alpha>0\).  If far-leg tightness fails, then for near-critical
\(p\) and macroscopic \(K\), either the weighted annular square mass has
already moved beyond the window,
\[
  \sum_{j>J+H}2^{\alpha(j-J)}
  \mathcal R_p^{(2^j,2^{j+1}]}(K)/\bar\chi_p
  \ge c/2,
\]
or the first \(H+1\) annuli contain high-incidence centers:
\[
  \sum_{j=J}^{J+H}2^{\alpha(j-J)}
  \frac{|\mathcal N^{(2^j,2^{j+1}]}(K,\lambda_j\bar\chi_p)|}{|K|}
  \ge c/4,
\]
with \(\lambda_j\asymp_{H,\alpha,\epsilon}2^{-\alpha(j-J)}\).  Since
\(\bar\chi_p\to\infty\), the thresholds in the finite-window alternative can
be made arbitrarily large.  This cleanly splits the remaining proof into an
escaping-tail case and a fixed-window high-incidence case.

Round 115 eliminates the fixed-window alternative by deterministic
double-counting.  If
\[
  V(I)=\sup_x|\{z:d(x,z)\in I\}|,
\]
then
\[
  |\mathcal N^I(K,m)|/|K|\le V(I)/m.
\]
For fixed \(J,H,\alpha\), the finite-window incidence alternative from Round
114 would imply
\[
  c/4\le
  \frac{4(H+1)}{c\bar\chi_p}
  \sum_{j=J}^{J+H}2^{2\alpha(j-J)}V((2^j,2^{j+1}]),
\]
which is impossible sufficiently close to \(p_c\).  Thus, for every fixed
dyadic window, the same-witness obstruction must eventually escape beyond
that window.  The remaining problem is now an iterated escaping-tail
phenomenon rather than a bounded-window high-incidence phenomenon.

Round 116 extracts a single remote annulus from the escaping tail.  For every
\(\alpha,\gamma>0\), every starting scale \(J\), and every fixed window
length \(H\), failure of far-leg tightness gives near-critical \(p\),
macroscopic \(K\), and some \(j>J+H\) such that
\[
  \mathcal R_p^{(2^j,2^{j+1}]}(K)/\bar\chi_p
  \gtrsim_{\alpha,\gamma,\epsilon}
  2^{-(\alpha+\gamma)(j-J)}.
\]
Applying the root-layer and incidence extractions to this single annulus
produces at least a comparable fraction of remote centers, each incident to a
comparable multiple of \(\bar\chi_p\) times the same exponential factor.  The
obstruction is now localized at one annular scale, though the scale may escape
with \(p\uparrow p_c\).

Round 117 converts the single-annulus incidence obstruction into a lower bound
on annular volume.  If \(V(I)=\sup_x|\{z:d(x,z)\in I\}|\), then the annulus
from Round 116 satisfies
\[
  V((2^j,2^{j+1}])
  \ge
  \frac{\epsilon^2}{16}
  (1-2^{-\alpha})^2(1-2^{-\gamma})^2
  2^{-2(\alpha+\gamma)(j-J)}\bar\chi_p.
\]
Equivalently, for every \(\eta>0\), failure of far-leg tightness forces some
escaping annulus with
\[
  V((2^j,2^{j+1}])
  \gtrsim_{\epsilon,\eta}
  2^{-2\eta(j-J)}\bar\chi_p.
\]
The obstruction is now a scale relation: near-critical susceptibility must fit
inside the volume of an annulus arbitrarily far out, up to a subexponential
penalty chosen in advance.

Round 118 converts this volume obstruction into a radius lower bound using
only bounded degree.  If the maximum degree is at most \(\Delta\ge2\), then the
same escaping annular witness may be chosen so that
\[
  2^j\ge \frac14\log_\Delta \bar\chi_p,
\]
while still satisfying the penalized volume lower bound from Round 117.  Thus
the obstruction is not merely outside each fixed window; near criticality it
must escape beyond the logarithmic susceptibility scale.  This is still far
from a contradiction on exponential-growth graphs, but it turns the remaining
problem into a correlation-length/backscattering estimate at distances at
least \(c\log\bar\chi_p\).

Round 119 keeps the witnesses in the logarithmic obstruction instead of
discarding them after taking a volume bound.  Failure of far-leg tightness
forces a finite set \(K\), a root \(x\in K\), and a remote annular set \(Z\)
such that, for
\[
  \sigma_j=\frac{\epsilon}{2}(1-2^{-\eta/2})^2 2^{-\eta(j-J)},
\]
we have \(2^j\ge \frac14\log_\Delta\bar\chi_p\),
\[
  |Z|\ge \frac{\sigma_j^2}{4}\bar\chi_p,
  \qquad d(x,z)\in(2^j,2^{j+1}]\quad(z\in Z),
\]
and every \(z\in Z\) receives annular two-point mass at least
\((\sigma_j/2)\bar\chi_p\) from \(K\).  Equivalently, the obstruction contains
a one-root fan into many remote centers, each of which backscatters
susceptibility-scale mass into \(K\).  This is the sharpest current target for
a nonamenability or two-replica decay argument.

Round 120 adds the deterministic packing step needed before any independence
or separator estimate can be used.  A finite set \(Z\) contains a
\(2r\)-separated subset of size at least \(|Z|/V_{2r}\), where
\(V_{2r}=\sup_v|B(v,2r)|\).  Applying this to the Round 119 fan with
\[
  r_p=\lfloor \theta\log_\Delta\bar\chi_p\rfloor,\qquad 0<\theta<1/2,
\]
gives a separated fan \(Z_\theta\) satisfying
\[
  |Z_\theta|
  \ge
  \frac{\sigma_j^2}{4\Delta}\bar\chi_p^{1-2\theta}.
\]
The balls \(B(z,r_p)\), \(z\in Z_\theta\), are disjoint, while every selected
center still backscatters annular mass \((\sigma_j/2)\bar\chi_p\) into the
same \(K\).  Thus the obstruction can no longer be hidden in one tight remote
cluster; it persists across polynomially many separated logarithmic-scale
regions.

Round 121 turns the separated fan obstruction into an exact criterion.  Define
an \((\epsilon,\eta,\theta,J,H)\)-separated fan to be the tuple
\((K,x,j,Z)\) produced by Round 120, with all constants and thresholds kept
explicit.  If for every \(0<\epsilon\le1\) one can find
\(\eta>0\), \(0<\theta<1/2\), \(J,H\), and a near-critical interval on which
no such fan exists, then
\[
  \mathcal R_p^*/\bar\chi_p\longrightarrow0.
\]
With the mean-field susceptibility input this gives
\(p_c(G)<p_{2\to2}(G)\).  This is now the cleanest local target: prove a
uniform exclusion of separated logarithmic fans, rather than estimating the
original two-replica square mass directly.

Round 122 strengthens the fan target by retaining root-to-fan two-point
weight.  The weighted greedy packing lemma says that if \(a_z\ge0\) on a
finite set \(Z\), then one can choose a \(2r\)-separated subset with total
weight at least \(V_{2r}^{-1}\sum_{z\in Z}a_z\).  Applying this with
\(a_z=\tau_p(x,z)\) gives a root-weighted separated fan satisfying
\[
  \sum_{z\in Z_\theta}\tau_p(x,z)
  \ge
  \frac{\sigma_j^2}{4\Delta}\bar\chi_p^{1-2\theta},
\]
while every selected \(z\) still backscatters
\((\sigma_j/2)\bar\chi_p\) annular mass from \(K\).  Therefore it is enough
to exclude root-weighted separated logarithmic fans.  This shifts the target
from a purely geometric crowding obstruction to a weighted remote two-point
sum from one root across many separated regions.

Round 123 packages the root-weighted fan as a bilinear fan energy
\[
  \mathcal W_p^I(x,K,Z)
  =
  \sum_{z\in Z}\tau_p(x,z)
  \sum_{\substack{y\in K\\d(y,z)\in I}}\tau_p(y,z).
\]
The Round 122 obstruction satisfies
\[
  \mathcal W_p^{(2^j,2^{j+1}]}(x,K,Z_\theta)
  \ge
  \frac{\sigma_j^3}{8\Delta}\bar\chi_p^{2-2\theta}.
\]
Thus it is enough to exclude separated fans with this bilinear energy lower
bound.  This is the most analytic current form of the obstruction: one has to
control a two-point convolution through polynomially many separated remote
centers at logarithmic scale.

Round 124 pushes the fan energy through spherical gates.  For \(r<2^j\), every
connection from the root \(x\) to a remote center \(z\), and every connection
from an annular \(y\in K\) to \(z\), must cross the sphere
\(\{a:d(a,z)=r\}\).  BK gives
\[
  \mathcal W_p^I(x,K,Z)\le \mathcal G_{p,r}^I(x,K,Z),
\]
where \(\mathcal G\) is the corresponding product of root-to-gate and
\(K\)-to-gate sums weighted by the gate-to-center probabilities.  Taking
\(r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor\) with \(\theta<1/4\) keeps
the gates inside the annulus and gives a gated obstruction
\[
  \mathcal G_{p,r_p}^{(2^j,2^{j+1}]}(x,K,Z_\theta)
  \ge
  \frac{\sigma_j^3}{8\Delta}\bar\chi_p^{2-2\theta}.
\]
The next analytic target can therefore be stated as a gate-energy exclusion
problem over disjoint logarithmic balls.

Round 125 removes the remaining spherical averaging in the gate obstruction.
For each remote center \(z\), the \(r_p\)-sphere has at most
\(\Delta^{r_p+1}\le \Delta\bar\chi_p^\theta\) vertices, so a single ordered
pair of gate vertices \(a_z,b_z\) captures at least the average contribution
of the gated product.  This defines a point-gated energy
\[
  \mathcal H_{p,r}^I(x,K,Z,a,b)
  =
  \sum_{z\in Z}\tau_p(x,a_z)\tau_p(a_z,z)\tau_p(b_z,z)
  \sum_{\substack{y\in K\\d(y,z)\in I}}\tau_p(y,b_z),
\]
and the obstruction becomes
\[
  \mathcal H_{p,r_p}^{(2^j,2^{j+1}]}(x,K,Z_\theta,a,b)
  \ge
  \frac{\sigma_j^3}{8\Delta^3}\bar\chi_p^{2-4\theta}.
\]
Thus any counterexample must exhibit one high-energy gate pair in each of
polynomially many disjoint logarithmic balls.  The next target is no longer a
spherical estimate but exclusion of these point-gated pairs.

Round 126 coalesces each ordered gate pair to one gate.  If \(a_z\) and
\(b_z\) lie on the same \(r\)-sphere around \(z\), then
\(d(a_z,b_z)\le2r\).  FKG applied to the event that a fixed geodesic from
\(b_z\) to \(a_z\) is open gives
\[
  \sum_{\substack{y\in K\\d(y,z)\in I}}\tau_p(y,a_z)
  \ge
  p^{2r}
  \sum_{\substack{y\in K\\d(y,z)\in I}}\tau_p(y,b_z).
\]
Since the internal factors \(\tau_p(a_z,z)\tau_p(b_z,z)\le1\), the
point-gated obstruction implies a one-gate obstruction
\[
  \mathcal J_{p,r_p}^{(2^j,2^{j+1}]}(x,K,Z_\theta,a)
  \ge
  p^{2r_p}
  \frac{\sigma_j^3}{8\Delta^3}\bar\chi_p^{2-4\theta},
\]
where
\[
  \mathcal J_{p,r}^I(x,K,Z,a)
  =
  \sum_{z\in Z}\tau_p(x,a_z)
  \sum_{\substack{y\in K\\d(y,z)\in I}}\tau_p(y,a_z).
\]
The obstruction now says that the same boundary gate in each disjoint
logarithmic ball must be simultaneously visible from the root and from a large
annular part of \(K\).

Round 127 thresholds the one-gate product.  If
\[
  \mathcal J_{p,r_p}^{I_j}(x,K,Z_\theta,a)
  \ge
  L=
  \frac{p^{2r_p}\sigma_j^3}{8\Delta^3}\bar\chi_p^{2-4\theta},
\]
then the disjointness of the gate balls gives
\(\sum_z\tau_p(x,a_z)\le\bar\chi_p\).  Therefore the subcollection
\[
  Z^\sharp=
  \left\{z:
    \sum_{\substack{y\in K\\d(y,z)\in I_j}}\tau_p(y,a_z)
    \ge \frac{L}{2\bar\chi_p}
  \right\}
\]
satisfies
\[
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)\ge
  \kappa_j(p),
  \qquad
  \sum_{\substack{y\in K\\d(y,z)\in I_j}}\tau_p(y,a_z)
  \ge \kappa_j(p),
\]
where
\[
  \kappa_j(p)=
  \frac{p^{2r_p}\sigma_j^3}{16\Delta^3}
  \bar\chi_p^{1-4\theta}.
\]
The obstruction is now a high one-gate layer: many root-visible disjoint
boundary gates, each also receiving polynomially large annular mass from \(K\).

Round 128 moves the high one-gate layer from center-annuli to gate-annuli.  If
\(d(a_z,z)=r_p\) and \(d(x,z),d(y,z)\in(2^j,2^{j+1}]\), then
\[
  d(x,a_z),d(y,a_z)\in
  I_{j,p}^{\rm gate}:=(2^j-r_p,2^{j+1}+r_p].
\]
Thus the high one-gate obstruction implies
\[
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)\ge\kappa_j(p),
\]
and every selected gate satisfies the direct gate-annulus lower bound
\[
  \sum_{\substack{y\in K\\d(y,a_z)\in I_{j,p}^{\rm gate}}}\tau_p(y,a_z)
  \ge\kappa_j(p).
\]
The remote centers now serve only as separated anchors for the selected gates;
the two-point mass itself is read at the gate vertices.

Round 129 replaces the gate-annulus two-point mass by deterministic incidence.
Since \(\tau_p\le1\), the lower bound
\[
  \sum_{\substack{y\in K\\d(y,a_z)\in I_{j,p}^{\rm gate}}}\tau_p(y,a_z)
  \ge\kappa_j(p)
\]
implies
\[
  |\{y\in K:d(y,a_z)\in I_{j,p}^{\rm gate}\}|
  \ge\kappa_j(p).
\]
Thus the remaining obstruction can be phrased as a root-weighted gate-incidence
configuration: the root has two-point mass at least \(\kappa_j(p)\) into
selected gate vertices, and every selected gate sees at least \(\kappa_j(p)\)
vertices of \(K\) in the expanded annulus.  This is the most combinatorial
form so far; only the root-to-gate weights remain probabilistic.

Round 130 removes even the root weights from the obstruction.  The
root-weighted gate-incidence layer satisfies
\[
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)\ge\kappa_j(p),
\]
and each summand is at most one, hence
\[
  |Z^\sharp|\ge\kappa_j(p).
\]
Consequently a counterexample forces a deterministic anchored gate-incidence
configuration: at least \(\kappa_j(p)\) selected gates in the expanded annulus
of one root \(x\), each anchored to a separated remote center and each incident
to at least \(\kappa_j(p)\) vertices of \(K\) in its expanded annulus.  The
current clean target is therefore purely combinatorial, apart from the
near-critical scale parameter \(\kappa_j(p)\).

Round 131 removes the explicit \(p^{2r_p}\) factor from the deterministic
target.  The bounded-degree union bound gives
\[
  p_c(G)\ge\frac1{\Delta-1}\ge\frac1\Delta.
\]
Taking \(p_0\) close enough to \(p_c\), every obstructing \(p\ge p_0\) has
\(p\ge1/\Delta\).  Hence, at
\(r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor\),
\[
  p^{2r_p}\ge \Delta^{-2r_p}\ge\bar\chi_p^{-2\theta}.
\]
The deterministic anchored gate-incidence obstruction therefore holds with the
uniform threshold
\[
  \widehat\kappa_j(p)=
  \frac{\sigma_j^3}{16\Delta^3}\bar\chi_p^{1-6\theta},
  \qquad 0<\theta<1/6.
\]
This is the current cleanest target: exclude a purely combinatorial anchored
gate-incidence pattern of size \(\widehat\kappa_j(p)\), with a positive power
of susceptibility and no hidden \(p\)-dependent factor.

Round 132 localizes that combinatorial target and removes the ambient witness
set \(K\).  From the deterministic gate-incidence obstruction, take
\[
  A=\{a_z:z\in Z^\sharp\}
\]
and let \(Y\) be the union of the \(K\)-vertices incident to the selected
gates in \(I_{j,p}^{\rm gate}\).  The anchor separation implies
\(z\mapsto a_z\) is injective, so \(|A|\ge\widehat\kappa_j(p)\), and the
pointwise incidence lower bound gives \(|Y|\ge\widehat\kappa_j(p)\).  Moreover,
if \(y\in Y\), then for some selected gate \(a_z\),
\[
  d(x,y)\le d(x,a_z)+d(a_z,y)\le 2^{j+2}+2r_p.
\]
Thus any counterexample forces a localized finite metric configuration:
separated anchors \(Z\), gates \(A\) in the expanded annulus of one root,
and a finite set \(Y\subseteq B(x,2^{j+2}+2r_p)\), with every selected gate
incident to at least \(\widehat\kappa_j(p)\) vertices of \(Y\).  The original
large finite set \(K\) is no longer part of the target.

Round 133 improves the logarithmic lower bound on the obstructing scale using
the localized gate set \(A\).  Since
\[
  |A|\ge
  \frac{\sigma_j^3}{16\Delta^3}\bar\chi_p^{1-6\theta}
\]
and \(A\subseteq B(x,2^{j+1}+r_p)\), bounded degree rules out
\[
  2^j<a\log_\Delta\bar\chi_p
\]
whenever \(0<a<(1-7\theta)/2\), after taking \(p\) sufficiently close to
\(p_c\).  Thus the localized obstruction can be chosen with
\[
  2^j\ge a\log_\Delta\bar\chi_p
  \qquad
  \text{for every }a<(1-7\theta)/2.
\]
This upgrades the old \(1/4\)-logarithmic radius obstruction to an
almost-\(1/2\) logarithmic radius obstruction when \(\theta\) is small.

Round 134 extracts a matched finite configuration from the localized incidence
obstruction.  View the gates \(A\) and localized vertices \(Y\) as a bipartite
graph, with an edge \(a y\) when
\[
  d(a,y)\in I_{j,p}^{\rm gate}.
\]
Every left vertex has degree at least \(\widehat\kappa_j(p)\), and
\(|A|\ge\widehat\kappa_j(p)\).  Since degrees and cardinalities are integers,
setting
\[
  m=\left\lceil\widehat\kappa_j(p)\right\rceil
\]
gives \(|A|\ge m\) and left degree at least \(m\).  Hall's theorem then gives
a matching of size \(m\).  Thus any counterexample forces \(m\) distinct
anchors \(z_i\), distinct gates \(a_i\), and distinct localized vertices
\(y_i\), with
\[
  d(x,z_i)\in(2^j,2^{j+1}],\quad d(a_i,z_i)=r_p,\quad
  d(x,a_i),d(a_i,y_i)\in(2^j-r_p,2^{j+1}+r_p],
\]
the anchors \(2r_p\)-separated, and \(2^j\ge a\log_\Delta\bar\chi_p\) for
every \(a<(1-7\theta)/2\).  The remaining obstruction is now a matched
collection of finite metric quadrilaterals, with no ambient witness set and no
unmatched incidence cloud.

Round 135 separates the matched configuration.  Starting from the matched
triples of Round 134, greedily pack the anchor coordinates at radius \(4r_p\),
then greedily pack the matched \(Y\)-coordinates at radius \(2r_p\).  Bounded
degree gives the loss
\[
  \Delta^{4r_p+1}\Delta^{2r_p+1}\le \Delta^2\bar\chi_p^{6\theta}.
\]
Thus the obstruction still contains
\[
  n=\left\lceil
  \frac{\sigma_j^3}{16\Delta^5}\bar\chi_p^{1-12\theta}
  \right\rceil
\]
matched triples with
\[
  d(z_i,z_k)>4r_p,\qquad d(a_i,a_k)>2r_p,\qquad
  d(y_i,y_k)>2r_p
  \quad(i\ne k).
\]
The gate separation follows from anchor separation and
\(d(a_i,z_i)=r_p\).  This is the cleanest finite obstruction so far:
a large collection of pairwise separated anchored annular quadrilaterals at
scale \(2^j\ge a\log_\Delta\bar\chi_p\), with only the exponent reduced from
\(1-6\theta\) to \(1-12\theta\).

Round 136 makes the short gate-to-anchor tubes explicit.  In the separated
matched obstruction, choose a geodesic \(\gamma_i\) from each gate \(a_i\) to
its anchor \(z_i\).  Since \(d(a_i,z_i)=r_p\), each \(\gamma_i\) has length
\(r_p\) and lies in \(B(z_i,r_p)\).  The anchor separation
\[
  d(z_i,z_k)>4r_p
\]
implies that these geodesics are pairwise vertex-disjoint.  Thus the same
obstruction can be stated with \(n\) disjoint local tubes, each of length
\(r_p\), attached to the annular gate points.  This formulation preserves the
Round 135 size
\[
  n=
  \left\lceil
  \frac{\sigma_j^3}{16\Delta^5}\bar\chi_p^{1-12\theta}
  \right\rceil
\]
and the improved logarithmic scale bound.  The point of the tube formulation is
that the local gate-opening events along the \(\gamma_i\)'s are independent
once a deterministic configuration is fixed.

Round 137 cross-separates the gate and matched endpoint coordinates.  Starting
from the disjoint gate-tube obstruction, put a conflict edge between two
indices \(i\ne k\) if either
\[
  d(a_i,y_k)\le2r_p
  \qquad\text{or}\qquad
  d(a_k,y_i)\le2r_p .
\]
For each fixed \(i\), at most \(\Delta^{2r_p+1}\) matched \(Y\)-vertices can
lie in \(B(a_i,2r_p)\), and at most \(\Delta^{2r_p+1}\) gates can lie in
\(B(y_i,2r_p)\).  The conflict graph therefore has maximum degree at most
\(2\Delta^{2r_p+1}\), and a greedy independent set loses only another factor
\(3\Delta^{2r_p+1}\).  The obstruction still has size
\[
  q=
  \left\lceil
  \frac{\sigma_j^3}{48\Delta^6}\bar\chi_p^{1-14\theta}
  \right\rceil .
\]
Requiring \(a>3\theta\) guarantees the paired separation
\[
  d(a_i,y_i)>2r_p
\]
from the lower bound \(d(a_i,y_i)>2^j-r_p\) and the improved scale
\(2^j\ge a\log_\Delta\bar\chi_p\).  Thus the current obstruction has
pairwise separated gates, pairwise separated matched endpoints, and
cross-separated gate-endpoint coordinates:
\[
  d(a_i,y_k)>2r_p\qquad(1\le i,k\le q).
\]
This makes the \(r_p\)-balls around all gate and matched endpoint coordinates
disjoint from the opposite family, a useful form for any later local
independence or mass-transport argument.

Round 138 further separates the anchor tubes from all matched endpoints.
Starting from the cross-separated tube obstruction, put a conflict edge between
two distinct indices \(i,k\) if either
\[
  d(z_i,y_k)\le2r_p
  \qquad\text{or}\qquad
  d(z_k,y_i)\le2r_p .
\]
Again the conflict degree is at most \(2\Delta^{2r_p+1}\), so a greedy
independent set loses only \(3\Delta^{2r_p+1}\).  This leaves
\[
  s=
  \left\lceil
  \frac{\sigma_j^3}{144\Delta^7}\bar\chi_p^{1-16\theta}
  \right\rceil
\]
triples.  The paired anchor-endpoint separation follows from
\[
  d(z_i,y_i)\ge d(a_i,y_i)-d(a_i,z_i)>2^j-2r_p,
\]
the scale bound \(2^j\ge a\log_\Delta\bar\chi_p\), and the strengthened
condition \(a>4\theta\).  The obstruction therefore has
\[
  d(z_i,y_k)>2r_p
  \qquad(1\le i,k\le s)
\]
in addition to the gate-endpoint cross-separation of Round 137.  Consequently
every selected matched endpoint is \(r_p\)-separated not only from all gates
but also from every anchor tube \(B(z_i,r_p)\).  The size is still a positive
power of \(\bar\chi_p\) for \(\theta<1/16\).

Round 139 upgrades anchor-endpoint separation to a buffer from the whole
gate-to-anchor tube.  Starting from Round 138, put a conflict edge between
distinct indices \(i,k\) if either
\[
  d(z_i,y_k)\le3r_p
  \qquad\text{or}\qquad
  d(z_k,y_i)\le3r_p .
\]
The conflict degree is at most \(2\Delta^{3r_p+1}\), so greedy thinning loses
a factor at most \(3\Delta^{3r_p+1}\).  This leaves
\[
  t=
  \left\lceil
  \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-19\theta}
  \right\rceil .
\]
The paired case follows from
\[
  d(z_i,y_i)>2^j-2r_p
\]
and the stronger condition \(a>5\theta\).  Hence \(d(z_i,y_k)>3r_p\) for all
selected \(i,k\).  Since every vertex \(v\in\gamma_i\) has \(d(v,z_i)\le r_p\),
the obstruction now has the buffered tube-endpoint separation
\[
  d(v,y_k)>2r_p
  \qquad(1\le i,k\le t,\ v\in\gamma_i).
\]
This turns the selected \(Y\)-endpoints into points separated from all local
gate-opening tubes by a full \(2r_p\) margin, while retaining a positive-power
size for \(\theta<1/19\).

Round 140 starts using the percolation randomness on the buffered tubes.  The
selected paths \(\gamma_i\) are pairwise edge-disjoint and each has length
\(r_p\), so the number
\[
  N_{\rm open}=\#\{i:\gamma_i\text{ is open}\}
\]
is binomial with mean \(t p^{r_p}\).  Near criticality the bounded-degree lower
bound on \(p_c\) lets us choose \(p\ge1/\Delta\), and hence
\[
  p^{r_p}\ge\Delta^{-r_p}\ge\bar\chi_p^{-\theta}.
\]
Combining this with the Round 139 size gives
\[
  \mathbf E_p N_{\rm open}
  \ge
  \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-20\theta}.
\]
Thus, with
\[
  \lambda_j^{\rm open}(p)
  =
  \frac{\sigma_j^3}{864\Delta^8}\bar\chi_p^{1-20\theta},
\]
a Chernoff bound gives
\[
  \mathbf P_p\bigl(N_{\rm open}\ge\lambda_j^{\rm open}(p)\bigr)
  \ge
  1-\exp[-\lambda_j^{\rm open}(p)/4].
\]
This is the first post-localization step that uses independence rather than
only metric packing.  It says that a counterexample forces a deterministic
buffered configuration in which a positive-power number of local gate tubes
open with high probability whenever \(\lambda_j^{\rm open}(p)\) is large.

Round 141 records the deterministic two-point counterpart of the open-tube
count.  Every buffered path \(\gamma_i\) has length \(r_p\) and runs from
\(a_i\) to \(z_i\), hence
\[
  \tau_p(a_i,z_i)\ge p^{r_p}.
\]
Near criticality \(p\ge1/\Delta\), so
\[
  \sum_i \tau_p(a_i,z_i)
  \ge
  t\Delta^{-r_p}
  \ge
  \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-20\theta}
  =:\kappa_j^{\rm tube}(p).
\]
Equivalently, \(\kappa_j^{\rm tube}(p)=2\lambda_j^{\rm open}(p)\).  This gives
a deterministic buffered tube-mass obstruction: a counterexample forces a
large sum of two-point mass across the short gate-to-anchor tubes, while the
matched endpoints remain buffered away from those tubes.  The corresponding
criterion says that excluding such a geometric configuration with this
two-point mass implies the \(L^2\)-gap criterion.

Round 142 turns the open-tube estimate into a scale dichotomy.  Fix
\[
  b>0,\qquad \rho=1-20\theta-3\eta b>0.
\]
If the obstructing scale satisfies \(2^j\le\bar\chi_p^b\), then
\[
  j\le b\log_2\bar\chi_p,
\]
and hence
\[
  \sigma_j^3
  \ge
  \left[\frac{\epsilon}{2}(1-2^{-\eta/2})^2\right]^3
  2^{3\eta J}\bar\chi_p^{-3\eta b}.
\]
The Round 140 parameter therefore satisfies
\[
  \lambda_j^{\rm open}(p)
  \ge
  c_{\epsilon,\eta,J,\Delta}\bar\chi_p^\rho.
\]
Consequently every counterexample forces either a polynomially remote
obstructing annulus,
\[
  2^j>\bar\chi_p^b,
\]
or a buffered configuration in which at least
\[
  c_{\epsilon,\eta,J,\Delta}\bar\chi_p^\rho
\]
short gate tubes are open with probability
\[
  1-\exp[-c_{\epsilon,\eta,J,\Delta}\bar\chi_p^\rho/4].
\]
This separates the next attack into two concrete cases: a very remote annular
geometry case and a many-open-local-tubes case.

Round 143 adds a logarithmic-scale endpoint-anchor alternative.  Fix
\[
  5\theta<a<B<\frac{1-21\theta}{2}
\]
and write \(L=\log_\Delta\bar\chi_p\).  If the buffered obstruction satisfies
\[
  2^j\le BL,
\]
then each matched endpoint \(y_i\) is connected to its anchor \(z_i\) by a
deterministic path of length at most
\[
  2^{j+1}+2r_p\le (2B+2\theta)L.
\]
Near criticality this gives
\[
  \tau_p(y_i,z_i)
  \ge
  \bar\chi_p^{-2B-2\theta}.
\]
At the same time, the logarithmic upper scale improves the threshold through
\[
  \sigma_j^3\gtrsim L^{-3\eta}\bar\chi_p^0.
\]
Thus a counterexample forces either
\[
  2^j>B\log_\Delta\bar\chi_p
\]
or
\[
  \sum_i\tau_p(y_i,z_i)
  \ge
  c_{\epsilon,\eta,J,\Delta,B}
  (\log_\Delta\bar\chi_p)^{-3\eta}
  \bar\chi_p^{1-21\theta-2B}.
\]
This is useful because the second alternative restores two-point mass on the
long endpoint-anchor pairs, while the first isolates a genuinely super-
logarithmic annular geometry.

Round 144 localizes the Round 143 endpoint-anchor mass.  In the logarithmic
case \(2^j\le B\log_\Delta\bar\chi_p\), the buffered geometry gives
\[
  d(y_i,a_i)\in(2^j-r_p,2^{j+1}+r_p],
  \qquad d(a_i,z_i)=r_p,
\]
so every diagonal endpoint-anchor pair lies in
\[
  I_{j,p}^{\rm ea}=(2^j-2r_p,2^{j+1}+2r_p].
\]
Consequently the lower bound
\[
  \sum_i\tau_p(y_i,z_i)
  \ge
  c_{\epsilon,\eta,J,\Delta,B}
  (\log_\Delta\bar\chi_p)^{-3\eta}
  \bar\chi_p^{1-21\theta-2B}
\]
is not merely a raw two-point-mass statement: it is supported on a controlled
annular window.  The missing step is still an amplification from this
diagonal annular mass to a normalized annular operator obstruction strong
enough to force the \(L^2\) gap.

Round 145 gives a stronger logarithmic scale amplification directly from the
number of buffered anchors.  The buffered obstruction supplies
\[
  t\ge \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-19\theta}
\]
distinct anchors \(z_i\) with \(d(x,z_i)\le 2^{j+1}\).  If
\[
  2^j\le B\log_\Delta\bar\chi_p,
\]
then \(\sigma_j^3\) loses only \(O((\log\bar\chi_p)^{-3\eta})\), whereas
bounded degree gives
\[
  t\le |B(x,2^{j+1})|\le \Delta\bar\chi_p^{2B}.
\]
Hence the small-logarithmic case is impossible whenever
\[
  2B<1-19\theta.
\]
Equivalently, every counterexample forces the buffered tube scale to satisfy
\[
  2^j>B\log_\Delta\bar\chi_p
  \qquad
  \left(5\theta<a<B<\frac{1-19\theta}{2}\right).
\]
This collapses the endpoint-anchor logarithmic alternative below the
\((1-19\theta)/2\) scale; the remaining annular geometry is now pushed to the
largest logarithmic scales compatible with the current buffered-anchor count.

Round 146 improves the logarithmic amplification by applying the same volume
argument before the thinning losses.  The matched anchored incidence stage has
\[
  m\ge
  \frac{\sigma_j^3}{16\Delta^3}\bar\chi_p^{1-6\theta}
\]
distinct anchors \(z_i\) in \(B(x,2^{j+1})\).  Thus
\[
  2^j\le B\log_\Delta\bar\chi_p
\]
would imply, up to the same polylogarithmic loss,
\[
  \bar\chi_p^{1-6\theta}
  \lesssim
  \bar\chi_p^{2B},
\]
which is impossible when \(2B<1-6\theta\).  The deterministic thinning steps
from matched incidence to buffered tubes keep the same \(p,x,j\), so the final
buffered tube obstruction inherits
\[
  2^j>B\log_\Delta\bar\chi_p
  \qquad
  \left(5\theta<B<\frac{1-6\theta}{2}\right).
\]
This is currently the strongest purely volumetric logarithmic-scale output:
the obstruction is pushed to just below the half-susceptibility logarithmic
radius, with only the initial matched-incidence exponent loss.

Round 148 makes the same argument sensitive to the actual ball-growth upper
bound.  If
\[
  |B(u,R)|\le C_{\rm vol}\omega^R
\]
uniformly in \(u\), then the matched-count contradiction below the scale
\[
  2^j\le B\log_\Delta\bar\chi_p
\]
uses
\[
  |B(x,2^{j+1})|
  \le C_{\rm vol}\bar\chi_p^{2B\log_\Delta\omega}
\]
instead of the cruder \(\Delta\bar\chi_p^{2B}\).  Consequently every
counterexample forces
\[
  2^j>B\log_\Delta\bar\chi_p
  \qquad
  \text{whenever}\qquad
  2B\log_\Delta\omega<1-6\theta .
\]
For the universal tree-volume estimate in maximum degree \(\Delta\ge3\), this
allows
\[
  B<\frac{1-6\theta}{2\log_\Delta(\Delta-1)}.
\]
This pushes the logarithmic scale beyond the half-susceptibility radius for
every finite \(\Delta\), with the largest gain at small degree.

Round 149 moves the volume-sensitive scale forcing earlier, to the raw
backscatter fan where the original finite set \(K\) and the annular
two-point mass are still present.  The fan extraction gives a set \(Z\) with
\[
  |Z|\ge c\,2^{-2\eta(j-J)}\bar\chi_p,
\]
each \(z\in Z\) receiving \((\sigma_j/2)\bar\chi_p\) two-point mass from
\(K\) across the annulus \(I_j\).  If \(2^j\le B\log_\Delta\bar\chi_p\), then
the ball-growth estimate gives
\[
  |Z|\le C_{\rm vol}\bar\chi_p^{2B\log_\Delta\omega}.
\]
The two bounds are incompatible near criticality whenever
\[
  2B\log_\Delta\omega<1.
\]
Thus the annular backscatter obstruction itself can be forced to live beyond
\[
  2^j>B\log_\Delta\bar\chi_p
\]
throughout this volume-sensitive range.  This is stronger than only pushing
the final buffered tubes, because it preserves the finite set \(K\) and the
weighted backscatter lower bounds that later operator arguments need.

Round 150 extracts a separated subfan without discarding the volume-sensitive
gain.  With
\[
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor
\]
and the same ball-growth bound, the packing denominator is
\[
  V_{2r_p}\le C_{\rm vol}\omega^{2r_p}
  \le C_{\rm vol}\bar\chi_p^{2\theta\log_\Delta\omega}.
\]
Thus the Round 149 fan has a \(2r_p\)-separated subfan satisfying
\[
  |Z_\theta|
  \ge
  \frac{\sigma_j^2}{4C_{\rm vol}}
  \bar\chi_p^{1-2\theta\log_\Delta\omega},
\]
while retaining \(2^j>B\log_\Delta\bar\chi_p\), the annular relation
\(d(x,z)\in I_j\), and the pointwise backscatter mass from \(K\).  This is the
right object for the next gate-decomposition step: it gives separated anchors
at the improved logarithmic scale with the exact volume-growth loss tracked.

Round 151 carries the volume-sensitive fan through the weighted and gated
layers.  The weighted extraction must be redone, rather than inferred from the
unweighted separated fan, because the later gate energy depends on the root
weights \(\tau_p(x,z)\).  The resulting separated fan satisfies
\[
  \sum_{z\in Z_\theta}\tau_p(x,z)
  \ge
  \frac{\sigma_j^2}{4C_{\rm vol}}
  \bar\chi_p^{1-2\theta\log_\Delta\omega},
\]
and hence
\[
  \mathcal W_p^{I_j}(x,K,Z_\theta)
  \ge
  \frac{\sigma_j^3}{8C_{\rm vol}}
  \bar\chi_p^{2-2\theta\log_\Delta\omega}.
\]
When \(\theta<B\), the scale condition
\[
  2^j>B\log_\Delta\bar\chi_p
\]
puts the gate radius \(r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor\) inside
the annulus, so Lemma~\(\ref{lem:gate-decomposition}\) gives the matching
lower bound for the gated fan energy.  This prepares the improved obstruction
for gate-pair selection and coalescence.

Round 152 applies gate-pair selection in the volume-sensitive setting.  The
old maximum-degree loss \(M_{r_p}^2\le\Delta^2\bar\chi_p^{2\theta}\) is
replaced by
\[
  M_{r_p}^2
  \le
  C_{\rm vol}^2\bar\chi_p^{2\theta\log_\Delta\omega}.
\]
Thus the point-gated fan energy satisfies
\[
  \mathcal H_{p,r_p}^{I_j}(x,K,Z_\theta,a,b)
  \ge
  \frac{\sigma_j^3}{8C_{\rm vol}^3}
  \bar\chi_p^{2-4\theta\log_\Delta\omega}.
\]
This keeps the improved scale and transfers the obstruction to explicit gate
pairs \((a_z,b_z)\), setting up the coalescence step with an exact
volume-growth exponent.

Round 153 performs this coalescence.  Lemma~\(\ref{lem:gate-coalescence}\)
turns the point-gated energy into a one-gate energy without adding any
volume-growth loss:
\[
  \mathcal J_{p,r_p}^{I_j}(x,K,Z_\theta,a)
  \ge
  p^{2r_p}\mathcal H_{p,r_p}^{I_j}(x,K,Z_\theta,a,b).
\]
Consequently the volume-sensitive one-gate obstruction satisfies
\[
  \mathcal J_{p,r_p}^{I_j}(x,K,Z_\theta,a)
  \ge
  p^{2r_p}
  \frac{\sigma_j^3}{8C_{\rm vol}^3}
  \bar\chi_p^{2-4\theta\log_\Delta\omega}.
\]
The next deterministic extraction should therefore use the threshold
\[
  \kappa_j^{\rm vol}(p)
  =
  \frac{p^{2r_p}\sigma_j^3}{16C_{\rm vol}^3}
  \bar\chi_p^{1-4\theta\log_\Delta\omega},
\]
the direct volume-sensitive analogue of the older high one-gate threshold.

Round 154 carries out that extraction.  In the useful parameter range
\[
  \theta<B,\qquad 1-4\theta\log_\Delta\omega>0,
\]
the one-gate obstruction yields a non-empty high layer \(Z^\sharp\subseteq
Z_\theta\) with
\[
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)\ge\kappa_j^{\rm vol}(p)
\]
and pointwise gate incidence
\[
  \sum_{\substack{y\in K\\d(y,z)\in I_j}}\tau_p(y,a_z)
  \ge \kappa_j^{\rm vol}(p)\qquad(z\in Z^\sharp).
\]
The only input needed beyond Round 153 is the separated-fan disjointness:
since \(a_z\in B(z,r_p)\) and the balls \(B(z,r_p)\) are disjoint, the gates
are distinct and their root weights sum to at most \(\bar\chi_p\).  The next
step is to push this high layer from annuli centered at \(z\) to annuli around
the chosen gate \(a_z\), preserving the volume-sensitive threshold.

Round 155 performs that push.  Define
\[
  I_{j,p}^{\rm gate}=(2^j-r_p,2^{j+1}+r_p].
\]
Since \(d(a_z,z)=r_p\), every point counted by the old \(z\)-annulus is counted
by the expanded gate annulus:
\[
  d(y,z)\in I_j
  \quad\Longrightarrow\quad
  d(y,a_z)\in I_{j,p}^{\rm gate}.
\]
The root location satisfies the same enlargement,
\[
  d(x,a_z)\in I_{j,p}^{\rm gate}.
\]
Hence the high one-gate layer gives the direct gate-annulus mass lower bound
\[
  \sum_{\substack{y\in K\\d(y,a_z)\in I_{j,p}^{\rm gate}}}
  \tau_p(y,a_z)
  \ge\kappa_j^{\rm vol}(p)\qquad(z\in Z^\sharp),
\]
with no further exponent loss.  The next step is the volume-sensitive analogue
of Round 129: replace this two-point mass lower bound by deterministic
incidence using \(\tau_p\le1\).

Round 156 makes that replacement.  Since \(\tau_p(y,a_z)\le1\), the direct
gate-annulus mass lower bound implies
\[
  |\{y\in K:d(y,a_z)\in I_{j,p}^{\rm gate}\}|
  \ge\kappa_j^{\rm vol}(p)\qquad(z\in Z^\sharp).
\]
The root-weighted part is unchanged:
\[
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)\ge\kappa_j^{\rm vol}(p).
\]
Thus the volume-sensitive chain has reached the same mostly combinatorial
form as the older Round 129 obstruction, but with
\[
  \kappa_j^{\rm vol}(p)
  =
  \frac{p^{2r_p}\sigma_j^3}{16C_{\rm vol}^3}
  \bar\chi_p^{1-4\theta\log_\Delta\omega}.
\]
The next natural move is the volume-sensitive analogue of Round 130: extract a
deterministic non-empty subcollection of gates from the aggregate
root-to-gate weight.

Round 157 performs this extraction.  Since every root-to-gate two-point
function is at most one,
\[
  |Z^\sharp|
  \ge
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)
  \ge\kappa_j^{\rm vol}(p).
\]
Together with Round 156, this gives a deterministic anchored gate-incidence
configuration:
\[
  |Z^\sharp|\ge\kappa_j^{\rm vol}(p),
  \qquad
  |\{y\in K:d(y,a_z)\in I_{j,p}^{\rm gate}\}|
  \ge\kappa_j^{\rm vol}(p)
  \quad(z\in Z^\sharp),
\]
with \(d(a_z,z)=r_p\), \(d(x,a_z)\in I_{j,p}^{\rm gate}\), and the original
separated anchors still present.  This is the volume-sensitive version of the
Round 130 combinatorial obstruction.  The next step is the analogue of
Round 131, replacing the remaining \(p^{2r_p}\) factor by a uniform
susceptibility power using the bounded-degree lower bound \(p_c\ge1/\Delta\).

Round 158 makes this threshold uniform in the near-critical window.  Taking
\(p_0\) sufficiently close to \(p_c\) and using
Lemma~\(\ref{lem:bounded-degree-pc-lower}\), we may assume \(p\ge1/\Delta\).
Then
\[
  p^{2r_p}\ge \Delta^{-2r_p}\ge \bar\chi_p^{-2\theta}.
\]
Thus the deterministic anchored gate-incidence configuration exists with
\[
  \widehat\kappa_j^{\rm vol}(p)
  =
  \frac{\sigma_j^3}{16C_{\rm vol}^3}
  \bar\chi_p^{1-2\theta-4\theta\log_\Delta\omega}
\]
in place of \(\kappa_j^{\rm vol}(p)\), provided
\[
  \theta<B,\qquad
  1-2\theta-4\theta\log_\Delta\omega>0.
\]
The remaining obstruction is now purely deterministic: many separated anchors
carry gates in a root annulus, and each selected gate has many incidences with
\(K\) in its expanded annulus.  The next step is to localize the gates inside
one bounded root-centered ball, as in the old Round 132--133 chain, while
tracking the improved volume exponent.

Round 159 performs the first localization step and removes the ambient witness
set \(K\).  Let
\[
  A=\{a_z:z\in Z^\sharp\}
\]
and let \(Y\) be the union of the \(K\)-vertices incident to the selected gates
in \(I_{j,p}^{\rm gate}\).  The separation of the anchors makes \(z\mapsto
a_z\) injective, so
\[
  |A|\ge\widehat\kappa_j^{\rm vol}(p),
  \qquad
  |Y|\ge\widehat\kappa_j^{\rm vol}(p).
\]
Moreover, for every \(y\in Y\),
\[
  d(x,y)\le d(x,a_z)+d(a_z,y)\le 2^{j+2}+2r_p
\]
for a gate \(a_z\) incident to \(y\).  Thus the obstruction is now a localized
finite metric incidence configuration:
\[
  Y\subseteq B(x,2^{j+2}+2r_p),
\]
with each selected gate incident to at least
\(\widehat\kappa_j^{\rm vol}(p)\) points of \(Y\).  The next step is to use
the lower bound on \(|A|\) and the volume growth bound to improve the
logarithmic lower bound on the annular scale \(2^j\) in the volume-sensitive
setting.

Round 160 applies that volume comparison.  If \(2^j<aL\), then every selected
gate lies in \(B(x,2^{j+1}+r_p)\), and the volume-growth assumption gives
\[
  |A|
  \le
  C_{\rm vol}\omega^{2^{j+1}+r_p}
  <
  C_{\rm vol}\bar\chi_p^{(2a+\theta)\log_\Delta\omega}.
\]
This contradicts the lower bound
\[
  |A|
  \ge
  \frac{\sigma_j^3}{16C_{\rm vol}^3}
  \bar\chi_p^{1-2\theta-4\theta\log_\Delta\omega}
\]
near criticality whenever
\[
  (2a+\theta)\log_\Delta\omega
  <
  1-2\theta-4\theta\log_\Delta\omega.
\]
Thus the localized obstruction can be chosen with \(2^j\ge aL\) throughout
that parameter range.

Round 161 applies the Hall matching extraction to the localized bipartite
incidence graph.  Put an edge between a selected gate \(a_z\in A\) and
\(y\in Y\) when
\[
  d(y,a_z)\in I_{j,p}^{\rm gate}.
\]
The localized obstruction gives
\[
  |A|\ge\widehat\kappa_j^{\rm vol}(p),
  \qquad
  \deg(a_z)\ge\widehat\kappa_j^{\rm vol}(p)
  \quad(z\in Z).
\]
Therefore, with
\[
  m=\left\lceil\widehat\kappa_j^{\rm vol}(p)\right\rceil,
\]
Hall's theorem gives matched triples
\[
  (z_i,a_i,y_i)_{i=1}^m
\]
with the \(z_i\)'s, \(a_i\)'s, and \(y_i\)'s all separately distinct, with the
same anchor separation, with
\[
  d(x,z_i)\in(2^j,2^{j+1}],
  \qquad
  d(a_i,z_i)=r_p,
  \qquad
  d(x,a_i),d(y_i,a_i)\in I_{j,p}^{\rm gate},
\]
and with \(y_i\in B(x,2^{j+2}+2r_p)\).  This removes the set-valued incidence
ambiguity and leaves a finite metric matching obstruction at the improved
volume-sensitive logarithmic scale.

Round 162 packages this as
Proposition~\(\ref{prop:volume-sensitive-matched-anchored-incidence-criterion}\).
If one can rule out all near-critical configurations with
\[
  m=\left\lceil\widehat\kappa_j^{\rm vol}(p)\right\rceil
\]
and with the above metric constraints, then
\[
  \lim_{p\uparrow p_c}\frac{\mathcal R_p^*}{\bar\chi_p}=0,
\]
and under the standard quasi-transitive finite-critical-window hypothesis this
implies \(p_c(G)<p_{2\to2}(G)\).

Round 163 updates the later volume-sensitive matched-count scale amplification
to use this new matched count.  The old amplification compared
\[
  \widehat\kappa_j(p)
  =
  \frac{\sigma_j^3}{16\Delta^3}\bar\chi_p^{1-6\theta}
\]
against the volume upper bound \(C_{\rm vol}\omega^{2^{j+1}}\).  The new
version compares
\[
  \widehat\kappa_j^{\rm vol}(p)
  =
  \frac{\sigma_j^3}{16C_{\rm vol}^3}
  \bar\chi_p^{1-2\theta-4\theta\log_\Delta\omega}
\]
instead, so the scale contradiction holds under
\[
  2B\log_\Delta\omega
  <
  1-2\theta-4\theta\log_\Delta\omega.
\]
After the matched stage, the deterministic thinning to a buffered-tube
configuration loses at most \(27\Delta^{13r_p+5}\).  Hence the thinned count is
bounded below by
\[
  \frac{\sigma_j^3}{432C_{\rm vol}^3\Delta^5}
  \bar\chi_p^{1-15\theta-4\theta\log_\Delta\omega}.
\]
The assumption \(\omega<\Delta\) gives the exponent margin
\[
  4\theta(1-\log_\Delta\omega)>0
\]
needed to dominate the older buffered-tube threshold
\[
  \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-19\theta}
\]
near criticality.

Round 164 propagates this sharper scale amplification into the endpoint-anchor
range.  If
\[
  0<\theta<1/31,
  \qquad
  5\theta<a<B<\frac{1-21\theta}{2},
\]
and \(1\le\omega<\Delta\), then with
\(\alpha=\log_\Delta\omega<1\),
\[
  2B\alpha<2B<1-21\theta
  <
  1-2\theta-4\theta\alpha,
\]
and
\[
  (2a+\theta)\alpha<2a+\theta<2B+\theta<1-20\theta
  <
  1-2\theta-4\theta\alpha.
\]
Thus the Round 163 volume-sensitive amplification applies throughout the
endpoint-anchor parameter range and gives a buffered tube configuration with
\[
  2^j>B\log_\Delta\bar\chi_p
\]
without invoking the older bounded-degree matched-count amplification.  The
older no-volume-growth endpoint-anchor collapse remains in the draft as a
separate stronger-context-free statement.

Round 165 packages the volume-sensitive collapse as a direct exclusion
criterion.  In the presence of volume growth
\[
  |B(u,R)|\le C_{\rm vol}\omega^R,\qquad 1\le\omega<\Delta,
\]
it is enough to rule out near-critical buffered tube configurations satisfying
the usual buffered-tube geometry and
\[
  2^j>B\log_\Delta\bar\chi_p
\]
for endpoint-anchor parameters
\[
  0<\theta<1/31,\qquad
  5\theta<a<B<\frac{1-21\theta}{2}.
\]
If such large-scale buffered tubes are excluded, then
\[
  \lim_{p\uparrow p_c}\frac{\mathcal R_p^*}{\bar\chi_p}=0,
\]
and the standard quasi-transitive finite-window hypothesis gives
\(p_c(G)<p_{2\to2}(G)\).  This is now the cleanest theorem-shaped remaining
target in the volume-sensitive branch.

Round 166 opens the short gate tubes inside that large-scale configuration.
The paths \(\gamma_i\) are vertex-disjoint, hence their opening events are
independent.  Taking \(p\) close enough to \(p_c\) gives \(p\ge1/\Delta\), so
with
\[
  N_{\rm open}
  =
  \#\{i:\gamma_i\text{ is open}\},
\]
the large-scale obstruction also satisfies
\[
  \mathbb P_p\!\left(N_{\rm open}\ge
  \frac{\sigma_j^3}{864\Delta^8}\bar\chi_p^{1-20\theta}\right)
  \ge
  1-\exp\!\left[
    -\frac{\sigma_j^3}{3456\Delta^8}\bar\chi_p^{1-20\theta}
  \right].
\]
Thus the remaining object is not merely a deterministic family of tubes: with
high probability, polynomially many of the short gate tubes open at a scale
\(2^j>B\log_\Delta\bar\chi_p\).  The next useful comparison is against annular
crossing/operator bounds for the opened endpoints.

Round 167 adds the scale dichotomy for this large-scale open-tube obstruction.
For any \(b>0\) with
\[
  \rho=1-20\theta-3\eta b>0,
\]
the same obstruction can be chosen with \(2^j>B\log_\Delta\bar\chi_p\) and
either
\[
  2^j>\bar\chi_p^b,
\]
or
\[
  \mathbb P_p\!\left(
    N_{\rm open}\ge c_{\epsilon,\eta,J,\Delta}\bar\chi_p^\rho
  \right)
  \ge
  1-\exp\!\left[
    -\frac{c_{\epsilon,\eta,J,\Delta}}4\bar\chi_p^\rho
  \right].
\]
Thus the obstruction has been split into a genuinely polynomial annular scale
or a polynomial number of independently opened short tubes at logarithmic-to-
polynomial scale.

Round 168 records the deterministic two-point counterpart in the same
volume-sensitive large-scale branch.  With the same parameter
\[
  \rho=1-20\theta-3\eta b>0,
\]
the obstruction can be chosen with \(2^j>B\log_\Delta\bar\chi_p\) and either
\[
  2^j>\bar\chi_p^b,
\]
or
\[
  \sum_{i=1}^t \tau_p(a_i,z_i)
  \ge
  d_{\epsilon,\eta,J,\Delta}\bar\chi_p^\rho .
\]
The proof uses only that each gate-to-anchor tube has length \(r_p\) and that,
near criticality, \(p^{r_p}\ge\Delta^{-r_p}\ge\bar\chi_p^{-\theta}\).  Thus
the volume-sensitive large-scale obstruction now has both a probabilistic
open-count formulation and a deterministic tube-mass formulation.  The latter
is the more convenient object for the next comparison with annular
operator/crossing estimates.

Round 169 makes the first such comparison, but only at the local gate shell.
For any distinct source and target families with \(d(u_i,v_i)\in I\),
\[
  \|T_p^I\|_{2\to2}
  \ge
  \frac1m\sum_i\tau_p(u_i,v_i),
  \qquad
  \Theta_p(I)
  \ge
  \frac{1}{\bar\chi_p^2m}\sum_i\tau_p(u_i,v_i)^2 .
\]
Applying this to the gate-to-anchor pairs in the volume-sensitive large-scale
buffered tube obstruction, with \(I=\{r_p\}\), gives
\[
  \|T_p^{\{r_p\}}\|_{2\to2}\ge\bar\chi_p^{-\theta},
  \qquad
  \Theta_p(\{r_p\})\ge\bar\chi_p^{-2-2\theta}.
\]
This is intentionally recorded as a limitation as much as a tool: separated
matching mass controls the exact-shell operator only through average mass, so
it does not by itself create the remote dyadic annular operator obstruction at
scale \(2^j\).  The missing step remains an amplification from local opened
or massive gate tubes to long annular crossing mass.

Round 170 converts the exact-shell obstruction into a pointwise shell-growth
target.  By the pointwise annular operator estimate,
\[
  \|T_p^{\{r_p\}}\|_{2\to2}
  \le
  \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}.
\]
Combining this with Round 169 gives the necessary lower bound
\[
  \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}
  \ge
  \bar\chi_p^{-\theta},
  \qquad
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor .
\]
Consequently, under the volume-sensitive hypotheses, if for some
\(0<\theta<1/31\)
\[
  \limsup_{p\uparrow p_c}
  \bar\chi_p^\theta
  \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}<1,
\]
then \(\mathcal R_p^*/\bar\chi_p\to0\), and the usual mean-field
quasi-transitive input yields \(p_c<p_{2\to2}\).  This gives a concrete
logarithmic shell-growth target for closing the volume-sensitive branch.

Round 171 rewrites the same target as an exponential threshold.  Since
\[
  r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor,
\]
the lower bound from Round 170 implies that any volume-sensitive counterexample
must satisfy, for every \(0<\theta<1/31\),
\[
  \limsup_{p\uparrow p_c}
  \left(
    \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}
  \right)^{1/r_p}
  \ge
  \Delta^{-1}.
\]
Conversely, if this limsup is strictly less than \(\Delta^{-1}\) for one such
\(\theta\), then \(\mathcal R_p^*/\bar\chi_p\to0\), hence the usual
quasi-transitive mean-field input gives \(p_c<p_{2\to2}\).  The remaining
analytic target can therefore be stated as a strict logarithmic-scale shell
exponent bound below \(\Delta^{-1}\).

Round 172 factors the Round 171 product into pointwise decay and sphere growth.
If, for \(r_p=\lfloor\theta\log_\Delta\bar\chi_p\rfloor\),
\[
  \limsup_{p\uparrow p_c}\tau_p^{\max}(r_p)^{1/r_p}<\alpha,
  \qquad
  \limsup_{p\uparrow p_c}\|S_{r_p}^G\|_{2\to2}^{1/r_p}<\rho,
\]
with \(\alpha\rho<\Delta^{-1}\), then the volume-sensitive branch collapses.
The volume-growth hypothesis gives
\[
  \|S_n^G\|_{2\to2}\le C_{\rm vol}\omega^n,
\]
so it is enough to prove the pointwise logarithmic-scale decay
\[
  \limsup_{p\uparrow p_c}\tau_p^{\max}(r_p)^{1/r_p}
  <
  \frac{1}{\Delta\omega}.
\]
Thus the current target has been reduced to a strict two-point decay exponent
at distance comparable to \(\log\bar\chi_p\).

Round 173 sharpens the threshold.  The earlier \(\Delta^{-1}\) came only from
the crude bound \(p\ge1/\Delta\) along the short gate paths.  In a near-critical
obstruction one may fix any \(q<p_c\), choose \(p_0\ge q\), and force the
selected \(p\in[p_0,p_c)\).  Thus each length-\(r_p\) gate path gives
\[
  \tau_p(a_i,z_i)\ge q^{r_p},
\]
and after letting \(q\uparrow p_c\), any volume-sensitive counterexample must
satisfy
\[
  \limsup_{p\uparrow p_c}
  \left(
    \tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}
  \right)^{1/r_p}
  \ge p_c .
\]
Consequently, a strict product exponent bound below \(p_c\) implies
\(\mathcal R_p^*/\bar\chi_p\to0\), and the factored target becomes
\[
  \limsup_{p\uparrow p_c}\tau_p^{\max}(r_p)^{1/r_p}<\alpha,\qquad
  \limsup_{p\uparrow p_c}\|S_{r_p}^G\|_{2\to2}^{1/r_p}<\rho,\qquad
  \alpha\rho<p_c.
\]
Using the volume-growth bound on sphere operators, the current clean target is
\[
  \limsup_{p\uparrow p_c}\tau_p^{\max}(r_p)^{1/r_p}
  <
  \frac{p_c}{\omega}.
\]
This supersedes the previous \(1/(\Delta\omega)\) threshold.

Round 174 replaces the coarse volume-growth constant by the actual spherical
\(L^2\)-growth invariant
\[
  \rho_{\mathrm{sph},2}(G)
  =
  \limsup_{n\to\infty}\|S_n^G\|_{2\to2}^{1/n}.
\]
Since \(r_p\to\infty\), the Round 173 product obstruction implies the
pointwise necessary condition
\[
  \limsup_{p\uparrow p_c}
  \tau_p^{\max}(r_p)^{1/r_p}
  \ge
  \frac{p_c}{\rho_{\mathrm{sph},2}(G)}
\]
in the volume-sensitive counterexample branch.  Conversely, a strict upper
bound below \(p_c/\rho_{\mathrm{sph},2}(G)\) collapses that branch and yields
\(\mathcal R_p^*/\bar\chi_p\to0\), hence \(p_c<p_{2\to2}\) under the
quasi-transitive mean-field input.  This is sharper than the \(p_c/\omega\)
target whenever the actual spherical operator growth is smaller than the
Schur volume-growth rate.  Round 175 below audits this pointwise formulation
and shows that, although formally correct as a conditional criterion, it is
vacuous on infinite graphs.

Round 175 records the geodesic lower-bound audit.  For every infinite
connected locally finite graph,
\[
  \tau_p^{\max}(n)\ge p^n,\qquad \|S_n^G\|_{2\to2}\ge1 .
\]
Thus at any logarithmic radius \(r_p\to\infty\),
\[
  \limsup_{p\uparrow p_c}\tau_p^{\max}(r_p)^{1/r_p}\ge p_c,
  \qquad
  \limsup_{p\uparrow p_c}
  \left(\tau_p^{\max}(r_p)\|S_{r_p}^G\|_{2\to2}\right)^{1/r_p}
  \ge p_c.
\]
The strict product criterion below \(p_c\), and the derived pointwise targets
below \(p_c/\rho_{\mathrm{sph},2}\) or \(p_c/\omega\), therefore cannot be
satisfied.  This demotes the Round 173--174 pointwise-sup criteria to
negative calibrations: the next route has to retain the structured endpoint
data from the obstruction, such as averaged mass over the matched pairs,
localized gate geometry, or a restricted submatrix norm, instead of passing to
the worst endpoint pair.

Round 176 returns to the volume-sensitive expanded gate-annulus obstruction,
before the deterministic count and pointwise-sup losses.  A general
mass-to-operator lemma says that finite sets \(A,Y\) carrying annular mass
\[
  M=\sum_{a\in A}\sum_{\substack{y\in Y\\ d(y,a)\in I}}\tau_p(y,a)
\]
force
\[
  \|T_p^I\|_{2\to2}\ge M/\sqrt{|A||Y|}.
\]
In the expanded gate-annulus obstruction, the root mass lower bound gives
\(|A|\ge\kappa_j^{\rm vol}(p)\), and the per-gate \(K\)-mass lower bound gives
total \(Y\)-to-\(A\) mass at least \((\kappa_j^{\rm vol}(p))^2\).  Volume
growth bounds \(A\) and \(Y\) inside balls of radii \(2^{j+1}+r_p\) and
\(2^{j+2}+2r_p\).  Therefore, for every cap \(U>B\), a counterexample forces
either
\[
  2^j>U\log_\Delta\bar\chi_p
\]
or
\[
  \|T_p^{I_{j,p}^{\rm gate}}\|_{2\to2}
  \ge
  C_{\epsilon,\eta,J,U,C_{\rm vol}}
  (\log_\Delta\bar\chi_p)^{-6\eta}
  \bar\chi_p^{\beta(\theta,U,\omega)},
\]
with
\[
  \beta(\theta,U,\omega)
  =
  2-4\theta-8\theta\log_\Delta\omega
  -3U\log_\Delta\omega
  -\frac32\theta\log_\Delta\omega .
\]
This is the current non-vacuous operator target: control either
super-logarithmic gate scales or the restricted gate-annular operator mass
created by the root/K two-sided incidence.

Round 177 packages that target as a direct criterion.  For chosen obstruction
parameters and a logarithmic cap \(U>B\), it is enough to prove both:
\[
  \text{no expanded gate-annulus obstruction has }
  2^j>U\log_\Delta\bar\chi_p,
\]
and, for every capped gate interval,
\[
  \|T_p^{I_{j,p}^{\rm gate}}\|_{2\to2}
  <
  C_{\epsilon,\eta,J,U,C_{\rm vol}}
  (\log_\Delta\bar\chi_p)^{-6\eta}
  \bar\chi_p^{\beta(\theta,U,\omega)}.
\]
The first statement is deliberately about scales that carry the full
expanded gate-annulus obstruction data, not about the existence of large
integers \(j\).  This is the current two-part non-vacuous route: a geometric
large-obstruction exclusion plus an operator upper bound on capped gate
annuli.

Round 178 calibrates this two-part route.  The Schur bound gives
\[
  \|T_p^I\|_{2\to2}\le \bar\chi_p
\]
for every annulus \(I\).  Hence the capped operator lower bound from
Round 176 is impossible near criticality whenever
\[
  \beta(\theta,U,\omega)>1.
\]
In that parameter regime, a counterexample must therefore realize the
large-data branch
\[
  2^j>U\log_\Delta\bar\chi_p
\]
with the full expanded gate-annulus obstruction data.  The capped operator
upper-bound problem is only meaningful in the complementary regime
\(\beta\le1\); above exponent \(1\), Schur already rules out the operator
branch.

Round 179 optimizes the Schur-calibrated range.  With
\(\alpha_\omega=\log_\Delta\omega\), the condition
\(\beta(\theta,U,\omega)>1\) can be met with arbitrarily small \(\theta>0\)
exactly when
\[
  3U\alpha_\omega<1 .
\]
Thus, if \(\alpha_\omega>0\), the expanded gate-annulus obstruction can be
forced beyond every logarithmic cap
\[
  2^j>U\log_\Delta\bar\chi_p
  \qquad
  \left(U<\frac{1}{3\alpha_\omega}\right).
\]
If \(\alpha_\omega=0\), every finite \(U>0\) is allowed.  The present barrier
for this Schur-calibrated operator argument is therefore
\(1/(3\log_\Delta\omega)\): beyond that, the capped operator branch may no
longer contradict the global Schur bound by exponent alone.  This is not the
best pure scale barrier in the manuscript after Round 186; the anchor-count
argument below reaches \(1/(2\alpha_\omega)\).

Round 180 extracts the corresponding normalized annular square-profile
obstruction from the same expanded gate data.  On the capped branch
\(2^j\le U\log_\Delta\bar\chi_p\), let
\[
  A=\{a_z:z\in Z^\sharp\},\qquad
  Y=\{y\in K:\exists a\in A,\ d(y,a)\in I_{j,p}^{\rm gate}\}.
\]
The gate lower bounds give total \(Y\)-to-\(A\) mass at least
\(|A|\kappa_j^{\rm vol}(p)\), while \(|A|\ge\kappa_j^{\rm vol}(p)\).
Cauchy--Schwarz in the \(Y\)-variable and the definition of \(\Theta_p(I)\)
therefore give
\[
  \Theta_p(I_{j,p}^{\rm gate})
  \ge
  \frac{(\kappa_j^{\rm vol}(p))^3}{\bar\chi_p^2|Y|}.
\]
Using \(|Y|\le C_{\rm vol}\omega^{2^{j+2}+2r_p}\) yields the explicit lower
bound
\[
  \Theta_p(I_{j,p}^{\rm gate})
  \ge
  D_{\epsilon,\eta,J,U,C_{\rm vol}}
  L^{-9\eta}
  \bar\chi_p^{\,1-6\theta-14\theta\alpha_\omega-4U\alpha_\omega}.
\]
Since \(\Theta_p(I)\le1\), this gives a separate square-profile escape range
\[
  U<\frac{1}{4\alpha_\omega}
\]
after optimizing \(\theta\downarrow0\).  This does not beat the
Schur-calibrated \(1/(3\alpha_\omega)\) barrier, but it records the obstruction
inside the normalized two-replica profile and may be the better interface for
future finite-set escape arguments.

Round 181 checks whether the square-profile branch can be improved merely by
using weighted gate profiles.  It cannot.  A layer-cake argument over the
level sets \(K_t=\{x:w(x)>t\}\) proves that every finitely supported weight
\(w\ge0\) satisfies
\[
  \sum_z
  \left(
    \sum_{\substack{x\\d(x,z)\in I}}w(x)\tau_p(x,z)
  \right)^2
  \le
  \bar\chi_p^2\|w\|_1\|w\|_\infty\Theta_p(I).
\]
Consequently, if \(w:A\to[0,1]\), \(S=\sum_Aw\), and every weighted gate has
annular mass at least \(m\) into a support set \(Y\), then
\[
  \Theta_p(I)\ge\frac{m^2S}{\bar\chi_p^2|Y|}.
\]
Using \(w=\mathbf 1_A\) gives the Round 180 estimate.  Using root weights
\(w(a_z)=\tau_p(x,a_z)\) gives no better worst-case exponent because the
available total root weight is only
\[
  \sum_z\tau_p(x,a_z)\ge\kappa_j^{\rm vol}(p),
\]
the same lower order already available from \(|A|\ge\kappa_j^{\rm vol}(p)\).
Thus a better square-profile threshold requires new information: a larger
selected gate count, a larger total selected root weight, or a smaller support
set \(Y\).  Reweighting alone is a lossless reformulation, not an improvement.

Round 182 isolates the support-size loss before the ball-volume estimate is
used.  On the capped branch \(2^j\le U\log_\Delta\bar\chi_p\), the gate data
already force
\[
  |Y|\Theta_p(I_{j,p}^{\rm gate})
  \ge
  E_{\epsilon,\eta,J,U,C_{\rm vol}}
  L^{-9\eta}
  \bar\chi_p^{\,1-6\theta-12\theta\alpha_\omega}.
\]
Round 180 is obtained from this by substituting the crude support bound
\[
  |Y|\le C_{\rm vol}\bar\chi_p^{(4U+2\theta)\alpha_\omega}.
\]
Thus the normalized-profile route has a clean diagnostic bottleneck: the
Cauchy step itself is not the main loss; the loss is replacing the actual
support \(Y\) by the whole ambient ball.  Improving the square-profile barrier
requires either a genuine profile-decay input at the gate annulus or a
support-spread theorem that bounds \(Y\) more sharply than the ball-volume
estimate.

Round 183 combines the Round 182 product with the profile size bound for the
specific gate set \(A\).  Since
\[
  \frac{\mathcal R_p^{I_{j,p}^{\rm gate}}(A)}{\bar\chi_p}
  \ge
  \frac{(\kappa_j^{\rm vol}(p))^3}{\bar\chi_p^2|Y|}
  \qquad\text{and}\qquad
  \frac{\mathcal R_p^{I_{j,p}^{\rm gate}}(A)}{\bar\chi_p}
  \le \frac{|A|}{\bar\chi_p},
\]
the capped branch also forces
\[
  |Y|\ge\frac{(\kappa_j^{\rm vol}(p))^3}{\bar\chi_p|A|}.
\]
Using the volume bounds on \(A\) and \(Y\), the capped branch is impossible
whenever
\[
  \delta(\theta,U,\omega)
  =
  2-6\theta-15\theta\alpha_\omega-6U\alpha_\omega
  >0.
\]
Optimizing \(\theta\downarrow0\) again gives
\[
  U<\frac1{3\alpha_\omega}.
\]
This recovers the Schur-calibrated threshold from a finite two-replica
support-volume contradiction.  The shared \(1/(3\alpha_\omega)\) threshold is
therefore structural for the support-profile diagnostic, not merely an
artifact of the global Schur estimate.  Round 186 shows separately that the
raw anchor count already forces pure scale escape up to
\(1/(2\alpha_\omega)\); improving the support-profile diagnostic beyond
\(1/(3\alpha_\omega)\) would require sharper information about \(Y\), \(A\), or
the extracted mass.

Round 184 records the optimized support-profile version explicitly.  If
\(\alpha_\omega>0\), the finite support-profile route forces
\[
  2^j>U\log_\Delta\bar\chi_p
  \qquad
  \left(U<\frac1{3\alpha_\omega}\right),
\]
with the full expanded gate-annulus data.  If \(\alpha_\omega=0\), every
finite \(U>0\) is allowed.  This is the same numerical range as
Round 179, but it is now proved without appealing to the global Schur bound:
the contradiction uses only the specific gate set \(A\), the support set \(Y\),
the profile bound
\(\mathcal R_p^I(A)/\bar\chi_p\le |A|/\bar\chi_p\), and the volume bounds on
\(A\) and \(Y\).

Round 185 makes the remaining capped-branch feasibility condition explicit.
For fixed admissible \(\eta,B,U,\theta,J,H\), if the expanded gate-annulus data
continue to satisfy \(2^j\le U\log_\Delta\bar\chi_p\), then they must obey
\[
  G_{\epsilon,\eta,J,U,C_{\rm vol}}
  L^{-9\eta}
  \bar\chi_p^{\,\delta(\theta,U,\omega)}
  \le1,
  \qquad
  L=\log_\Delta\bar\chi_p,
\]
where
\[
  \delta(\theta,U,\omega)
  =
  2-6\theta-15\theta\alpha_\omega-6U\alpha_\omega .
\]
Thus capped data arbitrarily close to criticality force
\(\delta(\theta,U,\omega)\le0\).  This is the exact exponent budget that any
remaining counterexample branch must saturate.

Round 186 records the stronger pure scale constraint supplied by the anchor
count before the support-profile step.  For the expanded gate-annulus data,
the selected anchors \(A=\{a_z:z\in Z^\sharp\}\) satisfy
\[
  |A|\ge\kappa_j^{\rm vol}(p).
\]
If the same data remain capped by \(2^j\le U\log_\Delta\bar\chi_p\), then
\[
  A_{\epsilon,\eta,J,U,C_{\rm vol}}
  L^{-3\eta}\bar\chi_p^{\,\rho(\theta,U,\omega)}
  \le1,
  \qquad
  \rho(\theta,U,\omega)
  =
  1-2\theta-5\theta\alpha_\omega-2U\alpha_\omega .
\]
Thus a capped anchor-count branch arbitrarily close to criticality forces
\(\rho(\theta,U,\omega)\le0\), and optimizing \(\theta\downarrow0\) gives pure
scale escape for every \(U<1/(2\alpha_\omega)\).  This supersedes the
support-profile \(1/(3\alpha_\omega)\) range as a scale statement, while the
support-profile branch remains the more informative two-replica diagnostic of
the support set \(Y\).

Round 188 packages this as a criterion.  If, for every obstruction constant
\(\epsilon\), one can choose admissible parameters with
\[
  \rho(\theta,U,\omega)
  =
  1-2\theta-5\theta\alpha_\omega-2U\alpha_\omega>0
\]
and exclude all expanded gate-annulus obstruction data satisfying
\[
  2^j>U\log_\Delta\bar\chi_p
\]
near criticality, then \(\mathcal R_p^*/\bar\chi_p\to0\).  Under the
quasi-transitive mean-field susceptibility input, this gives
\(p_c(G)<p_{2\to2}(G)\).  Thus in the positive anchor-count exponent range the
remaining task is a genuine large-scale geometric exclusion; there is no
separate capped operator estimate left to prove.

Round 189 rewrites the same scale forcing in residual form.  If
\(\alpha_\omega>0\), then for every \(\delta>0\) the expanded gate-annulus
obstruction can be chosen with
\[
  2^j>
  \left(\frac{1}{2\alpha_\omega}-\delta\right)
  \log_\Delta\bar\chi_p .
\]
If \(\alpha_\omega=0\), it can be chosen beyond every finite multiple of
\(\log_\Delta\bar\chi_p\).  Thus any remaining counterexample branch is
already half-logarithmic in the volume-growth scale; the next substantive
target is to exploit geometry at or beyond that scale.

Round 190 packages this residual form as a direct criterion.  If
\(\alpha_\omega>0\) and, for every obstruction constant \(\epsilon\), one can
exclude expanded gate-annulus data above
\[
  \left(\frac{1}{2\alpha_\omega}-\delta\right)
  \log_\Delta\bar\chi_p
\]
for some \(\delta>0\), then \(\mathcal R_p^*/\bar\chi_p\to0\).  Under the
usual quasi-transitive mean-field susceptibility input this yields
\(p_c(G)<p_{2\to2}(G)\).  For \(\alpha_\omega=0\), it is enough to exclude
expanded gate data beyond some fixed finite multiple of
\(\log_\Delta\bar\chi_p\).  This is now the clean residual geometric target of
the anchor-count route.

Round 191 refines that target by capping slightly above the half-log scale.
For
\[
  U_\lambda=\frac{1}{2\alpha_\omega}+\lambda
  \qquad(\lambda>0),
\]
any surviving finite-set obstruction must produce expanded gate-annulus data
with either
\[
  2^j>U_\lambda\log_\Delta\bar\chi_p
\]
or, if \(2^j\le U_\lambda\log_\Delta\bar\chi_p\), selected anchors
\(A=\{a_z:z\in Z^\sharp\}\) satisfying the density lower bound
\[
  \frac{|A|}{|B(x,2^{j+1}+r_p)|}
  \gtrsim
  L^{-3\eta}
  \bar\chi_p^{-2\lambda\alpha_\omega-2\theta-5\theta\alpha_\omega},
  \qquad L=\log_\Delta\bar\chi_p.
\]
Thus the residual geometry can now be attacked in two pieces: rule out
super-half-log expanded gate-annulus data, or rule out the near-half-log
anchor-density saturation inside the containing root ball.

Round 192 removes the constructed anchor set from the second branch.  The
selected anchors in Round 191 also carry root mass
\[
  \sum_{a\in A}\tau_p(x,a)\ge \kappa_j^{\rm vol}(p),
\]
and \(A\subseteq B(x,2^{j+1}+r_p)\).  Hence, under the same cap
\[
  2^j\le
  \left(\frac{1}{2\alpha_\omega}+\lambda\right)
  \log_\Delta\bar\chi_p,
\]
the obstruction forces the intrinsic ball-average lower bound
\[
  \frac{1}{|B(x,2^{j+1}+r_p)|}
  \sum_{a\in B(x,2^{j+1}+r_p)}\tau_p(x,a)
  \gtrsim
  L^{-3\eta}
  \bar\chi_p^{-2\lambda\alpha_\omega-2\theta-5\theta\alpha_\omega}.
\]
Thus the current residual target can be phrased without \(A\): exclude
super-half-log expanded gate-annulus data and exclude near-half-log balls with
this polynomially large average root two-point mass.

Round 193 localizes the second branch from the containing ball to the exact
expanded annulus.  Since every selected anchor satisfies
\[
  d(x,a_z)\in I_{j,p}^{\rm gate}
  =
  (2^j-r_p,2^{j+1}+r_p],
\]
the same lower bound gives
\[
  \frac{\sum_{a:\ d(x,a)\in I_{j,p}^{\rm gate}}\tau_p(x,a)}
       {|\{a:\ d(x,a)\in I_{j,p}^{\rm gate}\}|}
  \gtrsim
  L^{-3\eta}
  \bar\chi_p^{-2\lambda\alpha_\omega-2\theta-5\theta\alpha_\omega}
\]
whenever the super-half-log alternative fails.  Thus the current residual
target is an annular one: rule out super-half-log expanded gate-annulus data
or rule out near-half-log root annuli whose average two-point function from
the center is polynomially large.

Round 194 records the immediate pointwise consequence of this annular-average
branch.  If the super-half-log alternative fails, there must be a vertex
\(a\) in the expanded root annulus with
\[
  \tau_p(x,a)
  \gtrsim
  L^{-3\eta}
  \bar\chi_p^{-2\lambda\alpha_\omega-2\theta-5\theta\alpha_\omega}.
\]
Consequently, excluding both super-half-log expanded gate-annulus data and
such pointwise near-half-log pairs would close the finite-set obstruction.
This pointwise form is deliberately marked as a diagnostic rather than the
preferred target, since the geodesic lower-bound audit shows that global
\(\tau_p^{\max}\)-style strict decay criteria can be vacuous.  The averaged
annular formulation from Round 193 retains more structure.

Round 195 adds the missing averaged intermediate between Rounds 193 and 194.
The expanded root annulus is the disjoint union of exact spheres around \(x\),
so a large annular average forces at least one radius
\[
  n\in I_{j,p}^{\rm gate}\cap\mathbb N
\]
with
\[
  \frac{\sum_{a:\ d(x,a)=n}\tau_p(x,a)}
       {|\{a:\ d(x,a)=n\}|}
  \gtrsim
  L^{-3\eta}
  \bar\chi_p^{-2\lambda\alpha_\omega-2\theta-5\theta\alpha_\omega}.
\]
This exact-sphere average is now the clean localized residual target: it keeps
averaged information, unlike the pointwise diagnostic, while reducing the
annular branch to one graph distance.

Round 196 packages that exact-sphere average into the intrinsic profile
\[
  \bar\tau_p^{\rm sph}(n)
  =
  \sup_{x:\ S_n(x)\ne\varnothing}
  \frac{1}{|S_n(x)|}\sum_{a\in S_n(x)}\tau_p(x,a).
\]
with the value \(0\) if no such sphere exists.
Thus the residual branch can be stated without naming the obstructing root:
if the super-half-log alternative fails, then for some
\[
  n\in I_{j,p}^{\rm gate}\cap\mathbb N
\]
the spherical-average profile obeys
\[
  \bar\tau_p^{\rm sph}(n)
  \gtrsim
  L^{-3\eta}
  \bar\chi_p^{-2\lambda\alpha_\omega-2\theta-5\theta\alpha_\omega}.
\]
The current named target is therefore a near-half-log spherical-profile
exclusion, together with exclusion of the super-half-log expanded gate data.

Round 197 records a scale-window correction.  The expanded gate-annulus data
inherit the lower bound
\[
  2^j>B\log_\Delta\bar\chi_p
\]
from the weighted separated-fan extraction, while the near-half-log cap gives
\[
  2^j\le
  \left(\frac{1}{2\alpha_\omega}+\lambda\right)
  \log_\Delta\bar\chi_p .
\]
Thus the exact-sphere and spherical-profile upper-bound criteria should only
be imposed in this live window.  Since \(r_p\le\theta L\), every obstructing
radius lies in the dyadic-free interval
\[
  (B-\theta)L<n\le
  \left(\frac{1}{\alpha_\omega}+2\lambda+\theta\right)L.
\]
The current residual target is therefore a remote spherical-profile bound on
this interval, not a bound at bounded graph distances.

Round 198 turns the remote profile target into an exponent condition.  Define
\[
  \Phi_p(B,\lambda,\theta)
  =
  \sup\left\{\bar\tau_p^{\rm sph}(n):
  (B-\theta)L<n\le
  \left(\frac{1}{\alpha_\omega}+2\lambda+\theta\right)L\right\}.
\]
If the super-half-log expanded gate data are excluded and
\[
  \limsup_{p\uparrow p_c}
  \frac{\log_\Delta \Phi_p(B,\lambda,\theta)}
       {\log_\Delta\bar\chi_p}
  <
  -2\lambda\alpha_\omega-2\theta-5\theta\alpha_\omega,
\]
then the constants and \(L^{-3\eta}\) loss are absorbed by the strict exponent
margin, and the dyadic-free spherical-profile criterion closes the
two-replica obstruction.

Round 199 specializes this to a cleaner window.  Taking
\[
  \lambda=\theta=s,
  \qquad
  B=\frac{1}{2\alpha_\omega}-2s,
  \qquad
  0<s<\frac{1}{6\alpha_\omega},
\]
the profile window becomes
\[
  \left(\frac{1}{2\alpha_\omega}-3s\right)L<n\le
  \left(\frac{1}{\alpha_\omega}+3s\right)L,
\]
and the exponent target is
\[
  \limsup_{p\uparrow p_c}
  \frac{\log_\Delta \sup \bar\tau_p^{\rm sph}(n)}
       {\log_\Delta\bar\chi_p}
  <
  -(2+7\alpha_\omega)s
\]
over that window, together with exclusion of gate data beyond
\((1/(2\alpha_\omega)+s)L\).

Round 200 checks this target against the unavoidable geodesic lower bound.
Since \(\bar\tau_p^{\rm sph}(n)\ge p^n\), the Round 199 exponent target can
only be compatible if
\[
  (2+7\alpha_\omega)s
  <
  -\left(\frac{1}{2\alpha_\omega}-3s\right)\log_\Delta p_c.
\]
For nonamenable quasi-transitive graphs \(p_c<1\), so this inequality holds
for all sufficiently small \(s>0\).  The half-to-full spherical-average target
therefore avoids the immediate geodesic-vacuity problem of global pointwise
supremum criteria.

Round 201 normalizes by that geodesic baseline.  Put
\[
  c_s=\frac{1}{2\alpha_\omega}-3s,
  \qquad
  \mathfrak E_p^{\rm sph}(s)
  =
  \sup_{c_sL<n\le(1/\alpha_\omega+3s)L}
  \frac{\bar\tau_p^{\rm sph}(n)}{p^n}.
\]
Since \(p^n\le p^{c_sL}\) throughout the window, it is enough to prove
\[
  \limsup_{p\uparrow p_c}
  \frac{\log_\Delta \mathfrak E_p^{\rm sph}(s)}
       {\log_\Delta\bar\chi_p}
  <
  -c_s\log_\Delta p_c-(2+7\alpha_\omega)s.
\]
The live target can therefore be interpreted as a polynomial bound on the
excess over geodesic connections in the half-to-full logarithmic window.

Round 202 inserts a self-avoiding envelope for that excess.  Define
\[
  \mathfrak S_p^{\rm saw,sph}(n)
  =
  \sup_x
  \frac1{|S_n(x)|}\sum_{a\in S_n(x)}
  \sum_{\gamma:x\to a\ {\rm SAW}}p^{|\gamma|-n}.
\]
The union bound over open self-avoiding paths gives
\[
  \bar\tau_p^{\rm sph}(n)/p^n
  \le
  \mathfrak S_p^{\rm saw,sph}(n).
\]
Therefore it is enough to prove the Round 201 exponent bound for the
half-to-full-window supremum of this deterministic self-avoiding path-count
envelope.

Round 203 decomposes that envelope by excess path length.  Let
\[
  \mathfrak N_{n,k}^{\rm saw,sph}
  =
  \sup_x \frac1{|S_n(x)|}\sum_{a\in S_n(x)}
  \#\{\gamma:x\to a\ {\rm SAW}:|\gamma|=n+k\}.
\]
Because the supremum over roots is outside the sum over excess lengths, the
usable statement is
\[
  \mathfrak S_p^{\rm saw,sph}(n)
  \le
  \sum_{k\ge0}p^k\mathfrak N_{n,k}^{\rm saw,sph}.
\]
Thus any \(q>p_c\) weighted bound
\[
  \sup_{c_sL<n\le(1/\alpha_\omega+3s)L}
  \sum_{k\ge0}q^k\mathfrak N_{n,k}^{\rm saw,sph}
\]
with the Round 202 exponent margin is enough.  The remaining object is now an
exact-sphere, excess-length self-avoiding path-count profile.

Round 204 splits the last target into finite excess and long-excess tail
pieces.  For a cutoff
\[
  K_{\rho,p}=\lfloor \rho\log_\Delta\bar\chi_p\rfloor
\]
define
\[
  \mathfrak A_{q,\rho}^{\rm saw}(s,p)
  =
  \sup q^k\mathfrak N_{n,k}^{\rm saw,sph}
\]
over the half-to-full window and \(0\le k\le K_{\rho,p}\), and define
\[
  \mathfrak T_{q,\rho}^{\rm saw}(s,p)
  =
  \sup_{c_sL<n\le(1/\alpha_\omega+3s)L}
  \sum_{k>K_{\rho,p}}q^k\mathfrak N_{n,k}^{\rm saw,sph}.
\]
The finite-excess sum has only \(O(L)\) terms, so its logarithmic
\(\bar\chi_p\)-exponent is the same as that of
\(\mathfrak A_{q,\rho}^{\rm saw}\).  Hence the live target can be split into
two independent estimates: a weighted maximum for \(k=O(L)\), and a genuine
long-excess tail bound for \(k>\rho L\).

Round 205 expands the finite-excess maximum into excess-slope bins.  For
\(\delta>0\), set
\[
  m_{\rho,\delta}=\lfloor\rho/\delta\rfloor+1
\]
and let \(\mathfrak B_{i,\delta}^{\rm saw}(s,p)\) be the supremum of
\(\mathfrak N_{n,k}^{\rm saw,sph}\) over the half-to-full window and
\[
  i\delta L\le k<(i+1)\delta L .
\]
Since \(q<1\), a path in the \(i\)th bin gains the deterministic exponent
\(i\delta\log_\Delta q\).  It is therefore enough to prove, for each fixed
bin \(i\), that
\[
  \limsup_{p\uparrow p_c}
  \frac{\log_\Delta\mathfrak B_{i,\delta}^{\rm saw}(s,p)}
       {\log_\Delta\bar\chi_p}
  +i\delta\log_\Delta q
\]
lies below the Round 203 margin, together with the Round 204 long-excess tail
bound.  This separates the finite-excess task into finitely many unweighted
counting exponents.

Round 206 records a useful negative audit for the long-excess tail.  The raw
bounded-degree estimate
\[
  \mathfrak N_{n,k}^{\rm saw,sph}
  \le \Delta(\Delta-1)^{n+k-1}
\]
would control the \(q\)-weighted tail only if \(q(\Delta-1)<1\).  This is
incompatible with the required \(q>p_c\), since the standard susceptibility
bound gives \(p_c\ge1/(\Delta-1)\).  The long-excess estimate must therefore
use fixed-endpoint or exact-sphere structure, not just ambient path growth.

Round 207 introduces a radial-defect refinement of the exact-sphere SAW
counts.  For a path \(\gamma\) started at \(x\), let \(I_x(\gamma)\) count
steps that decrease the distance from \(x\), and let \(H_x(\gamma)\) count
steps that stay in the same sphere around \(x\).  If \(\gamma\) ends in
\(S_n(x)\), then
\[
  |\gamma|-n=2I_x(\gamma)+H_x(\gamma).
\]
Writing \(\mathfrak M_{n,b,h}^{\rm rad,saw,sph}\) for the spherical average
of self-avoiding paths with \(I_x=b\) and \(H_x=h\), the exact excess profile
satisfies
\[
  \mathfrak N_{n,k}^{\rm saw,sph}
  \le
  \sum_{2b+h=k}\mathfrak M_{n,b,h}^{\rm rad,saw,sph}.
\]
Thus the \(q\)-weighted target is implied by a radial-defect target with
weights \(q^{2b+h}\).  This separates the two sources of excess: inward
radial backtracking and same-sphere wandering.

Round 208 uses this separation to split the long-excess tail.  With
\(K_{\rho,p}=\lfloor\rho L\rfloor\), if
\[
  2b+h>K_{\rho,p},
\]
then either \(b>K_{\rho,p}/4\) or \(h>K_{\rho,p}/2\).  Consequently the
Round 204 long-excess tail is bounded by the sum of an inward-backtracking
tail
\[
  \sum_{b>K_{\rho,p}/4,\ h\ge0}q^{2b+h}
  \mathfrak M_{n,b,h}^{\rm rad,saw,sph}
\]
and a same-sphere tail
\[
  \sum_{b\ge0,\ h>K_{\rho,p}/2}q^{2b+h}
  \mathfrak M_{n,b,h}^{\rm rad,saw,sph}.
\]
Thus the remaining tail task has two separate geometric components:
many inward radial returns, or many steps tangent to distance spheres.

Round 209 sharpens the second component.  Once the inward tail has covered
\(b>K_{\rho,p}/4\), the same-sphere tail only needs to cover the complementary
low-inward sector.  Thus the horizontal tail is reduced to
\[
  \sum_{0\le b\le K_{\rho,p}/4,\ h>K_{\rho,p}/2}
  q^{2b+h}\mathfrak M_{n,b,h}^{\rm rad,saw,sph}.
\]
Paths with both many inward steps and many same-sphere steps are charged to
the inward tail, so the tangential estimate can be attempted under the
additional constraint \(b=O(L)\) with a fixed small constant.

Round 210 records the bipartite simplification.  If \(G\) is bipartite, then
for every root \(x\), adjacent vertices have distances from \(x\) of opposite
parity.  Hence no path has a same-sphere step:
\[
  H_x(\gamma)=0.
\]
Thus
\[
  \mathfrak M_{n,b,h}^{\rm rad,saw,sph}=0\qquad(h\ge1),
\]
and the horizontal tail in Round 209 vanishes.  In the bipartite case the
radial long-excess program reduces to the finite-excess estimate plus the
inward-return tail.

Round 211 explains why the bipartite focus is not a loss of generality at the
level of the \(p_c<p_{2\to2}\) target.  Let \(\operatorname{Sub}(G)\) be the
graph obtained by subdividing every edge of \(G\) once.  Then
\[
  p_c(\operatorname{Sub}(G))=\sqrt{p_c(G)}
\]
and
\[
  p_{2\to2}(\operatorname{Sub}(G))=\sqrt{p_{2\to2}(G)}.
\]
The first identity comes from replacing each original edge by two independent
open half-edges, so the effective old-edge parameter is \(p^2\).  The second
uses the same old-vertex identity
\(\tau_p^{\operatorname{Sub}(G)}(x,y)=\tau_{p^2}^G(x,y)\) and bounds the
old--midpoint and midpoint--midpoint blocks using the incidence operator
between \(V(G)\) and \(E(G)\).  Thus
\[
  p_c(G)<p_{2\to2}(G)
  \quad\Longleftrightarrow\quad
  p_c(\operatorname{Sub}(G))<
  p_{2\to2}(\operatorname{Sub}(G)).
\]
Since subdivision is bipartite and preserves quasi-transitivity and
nonamenability in bounded degree, a bipartite proof for all such subdivisions
would imply the general target.

Round 212 packages this into a usable criterion.  The subdivision
susceptibilities satisfy, for \(H=\operatorname{Sub}(G)\) and \(q=p^2\),
\[
  \bar\chi_q^G\le \bar\chi_p^H
  \le C_\Delta(1+\bar\chi_q^G).
\]
Thus the mean-field input
\[
  \limsup_{q\uparrow p_c(G)}(p_c(G)-q)\bar\chi_q^G<\infty
\]
transfers to \(H\), because
\[
  p_c(G)-p^2=(p_c(H)-p)(p_c(H)+p).
\]
Consequently, if the bipartite inward-tail criterion is verified for the
subdivision \(H\), then \(p_c(H)<p_{2\to2}(H)\), and the Round 211 threshold
identity transfers this back to \(p_c(G)<p_{2\to2}(G)\).  The current global
target can therefore be phrased as a radial finite-excess plus inward-return
estimate on canonical bipartite subdivisions.

Round 213 removes a slack factor from the bipartite inward tail.  The generic
radial split used \(b>K_{\rho,p}/4\), but in a bipartite graph \(h=0\), so
the excess is exactly
\[
  k=2b.
\]
Thus the true long-excess tail begins at
\[
  b>K_{\rho,p}/2,
\]
not \(K_{\rho,p}/4\).  Define the exact bipartite inward tail
\[
  \mathfrak L_{q,\rho}^{\rm in,saw}(s,p)
  =
  \sup_n\sum_{b>K_{\rho,p}/2}q^{2b}
  \mathfrak M_{n,b,0}^{\rm rad,saw,sph}.
\]
The subdivision criterion can now use this sharper tail.  The remaining
global target on \(\operatorname{Sub}(G)\) is finite-excess control plus this
exact inward-return tail.

Round 214 applies the same bipartite identity to the finite-excess side.  In
a bipartite graph, \(0\le k\le K_{\rho,p}\) is equivalent to
\[
  0\le b\le K_{\rho,p}/2
\]
for the radial inward count, so the old finite profile
\(\mathfrak A_{q,\rho}^{\rm saw}\) is implied by the one-parameter inward
profile
\[
  \mathfrak F_{q,\rho}^{\rm in,saw}(s,p)
  =
  \sup_n\sup_{0\le b\le K_{\rho,p}/2}
  q^{2b}\mathfrak M_{n,b,0}^{\rm rad,saw,sph}.
\]
Together with the exact tail
\(\mathfrak L_{q,\rho}^{\rm in,saw}\), this gives a fully inward-return
criterion for bipartite graphs.  After subdivision, the current remaining
target is therefore a pair of inward-return estimates on
\(\operatorname{Sub}(G)\): finite inward profile plus inward tail.

Round 215 bins the finite inward profile.  For \(\delta>0\), set
\[
  m_{\rho,\delta}^{\rm in}
  =
  \left\lfloor\frac{\rho}{2\delta}\right\rfloor+1
\]
and define \(\mathfrak C_{i,\delta}^{\rm in,saw}\) by restricting
\(\mathfrak M_{n,b,0}^{\rm rad,saw,sph}\) to
\[
  i\delta L\le b<(i+1)\delta L .
\]
Since \(q<1\), the \(i\)th bin contributes a weight no larger than
\(q^{2i\delta L}\).  Thus finite inward control follows from finitely many
exponent inequalities
\[
  \limsup_{p\uparrow p_c}
  \frac{\log_\Delta\mathfrak C_{i,\delta}^{\rm in,saw}(s,p)}
       {\log_\Delta\bar\chi_p}
  +2i\delta\log_\Delta q
  <
  -c_s\log_\Delta p_c-(2+7\alpha_\omega)s.
\]
The remaining unbinned piece is the inward tail
\(\mathfrak L_{q,\rho}^{\rm in,saw}\).

Round 216 identifies the exact old-root even-sphere subdivision projection.
If \(H=\operatorname{Sub}(G)\) and \(\pi\) is a self-avoiding path in \(G\)
from an old root \(x\), then its canonical lift satisfies
\[
  I_x^H(\widehat\pi)=2I_x^G(\pi)+H_x^G(\pi).
\]
Moreover \(S_{2n}^H(x)=S_n^G(x)\), and old-to-old subdivision SAWs are in
bijection with original SAWs.  Hence the old-root even-sphere subdivision
profile with inward count \(B\) is bounded by
\[
  \sum_{2i+h=B}\mathfrak M_{n,i,h}^{G,{\rm rad,saw,sph}}.
\]
The remaining subdivision bookkeeping is to extend this comparison to odd
spheres and midpoint roots with only bounded shifts in radius and inward
count.

Round 217 handles the old-root odd spheres under a local no-dead-end
assumption.  The odd sphere \(S_{2n+1}^{\operatorname{Sub}(G)}(x)\) consists
of midpoints whose nearer endpoint lies in \(S_n^G(x)\).  If every vertex of
\(S_n^G(x)\) has an edge to \(S_{n+1}^G(x)\), this midpoint sphere has
cardinality at least both \(|S_n^G(x)|\) and \(|S_{n+1}^G(x)|\).  Deleting
the final half-edge from an old-root subdivision SAW ending at a midpoint
projects to an original SAW ending in either \(S_n^G(x)\) or
\(S_{n+1}^G(x)\).  The final half-edge contributes \(0\) or \(1\) inward
subdivision steps, giving the bound
\[
  \Delta\sum_{2i+h=B}\mathfrak M_{n,i,h}^{G,{\rm rad,saw,sph}}
  +
  \Delta\sum_{2i+h=B-1}\mathfrak M_{n+1,i,h}^{G,{\rm rad,saw,sph}}.
\]
Thus old-root subdivision profiles are now controlled by original radial
profiles, modulo no-dead-end or bounded-dead-end bookkeeping.  Midpoint roots
remain the next comparison to isolate.

Round 218 isolates midpoint roots.  If \(r\) is a midpoint adjacent to old
vertices \(u_0,u_1\), deleting the first half-edge of a SAW from \(r\) gives a
SAW from one of the \(u_j\).  For an endpoint in \(S_m^H(r)\), the distance
from \(u_j\) is \(m-1\) or \(m+1\), and bipartiteness gives
\[
  I_{u_j}(\gamma')=I_r(\gamma)
  \quad\text{or}\quad
  I_{u_j}(\gamma')=I_r(\gamma)-1 .
\]
Thus midpoint-root averages are bounded by adjacent old-root profiles at
radii \(m-1\) and \(m+1\), provided the shifted sphere comparison
\[
  |S_{m-1}^H(u_j)|,\ |S_{m+1}^H(u_j)|\le C|S_m^H(r)|
\]
holds.  The full subdivision comparison is now reduced to this sphere
comparability, plus the no-dead-end or bounded-dead-end issue in the old-root
odd sector.

Round 219 records the key parameter match.  If the subdivision criterion uses
parameter \(q\) and \(Q=q^2\), then the even-sphere identity
\[
  B=2i+h
\]
gives
\[
  q^{2B}=Q^{2i+h}.
\]
Thus subdivision inward weights are exactly the original radial-defect
weights.  In the odd old-root sector the possible final inward half-step gives
\(B=2i+h+1\), and in the midpoint-root sector deleting the first half-edge can
lower the old-root inward count by one; both effects only improve the
\(q\)-weight since \(q<1\).  The subdivision comparison therefore loses
constants and neighbouring radii, but not exponent through the weight.

Round 220 shows that nonamenability supplies the missing sphere denominator
comparisons.  For old-root odd spheres, the midpoint sphere in the subdivision
contains the edge boundary of \(B_n^G(x)\), so
\[
  |S_{2n+1}^{\operatorname{Sub}(G)}(x)|
  \ge h(G)|S_n^G(x)|.
\]
Together with the geodesic predecessor bound for \(S_{n+1}^G(x)\), this
removes the local no-dead-end assumption from Round 217, at cost
\(\Delta/h(G)\).  For midpoint roots, a general bounded-degree Cheeger
estimate gives
\[
  |S_{m-1}^X(a)|,\ |S_{m+1}^X(a)|
  \le \frac{D^4}{h(X)}|S_m^X(b)|
  \qquad(a\sim b),
\]
so the shifted-sphere comparison from Round 218 holds automatically in every
bounded-degree nonamenable subdivision.  The subdivision profile comparison
is now limited mainly by translating the resulting shifted old-root estimates
into the exact finite-window and tail profiles without losing the exponent
margin.

Round 221 packages these estimates into restricted subdivision profiles.  With
\(\mathfrak M_{\ell,B}^{H,{\rm old}}\) and
\(\mathfrak M_{\ell,B}^{H,{\rm mid}}\) denoting the old-root and midpoint-root
parts of the subdivision profile,
\[
  \mathfrak M_{\ell,B,0}^{H,{\rm rad,saw,sph}}
  =
  \max\{\mathfrak M_{\ell,B}^{H,{\rm old}},
        \mathfrak M_{\ell,B}^{H,{\rm mid}}\}.
\]
The old-root even and odd bounds reduce to original radial profiles, while
the midpoint-root bound is
\[
  \mathfrak M_{m,B}^{H,{\rm mid}}
  \le
  2C_H\left(
    \mathfrak M_{m-1,B}^{H,{\rm old}}
    +
    \mathfrak M_{m+1,B-1}^{H,{\rm old}}
  \right),
  \qquad C_H=D_H^4/h(H).
\]
Thus the subdivision count comparison is no longer circular: midpoint roots
reduce to old roots, and old roots reduce to the original two-coordinate
radial profiles.

Round 222 turns the count comparison into a weighted profile comparison.  The
collapsed original radial profile is
\[
  \mathfrak R_{n,d}^{G,{\rm rad,saw,sph}}
  =
  \sum_{2i+j=d}\mathfrak M_{n,i,j}^{G,{\rm rad,saw,sph}}.
\]
For \(Q=q^2\),
\[
  q^{2B}\mathfrak M_{m,B,0}^{H,{\rm rad,saw,sph}}
  \le
  C_\star
  \sum_{|2r-m|\le2}\sum_{a=0}^2
  Q^{B-a}\mathfrak R_{r,B-a}^{G,{\rm rad,saw,sph}}.
\]
Consequently the finite inward profile and inward tail on \(H\) are bounded
by shifted original finite and tail profiles
\[
  \mathfrak F_{Q,\rho}^{G\to H,{\rm rad}},
  \qquad
  \mathfrak L_{Q,\rho}^{G\to H,{\rm rad}},
\]
up to fixed constants \(9C_\star\) and \(3C_\star\).  This gives a direct
criterion for the subdivision route in terms of original-graph radial-defect
estimates over half-radius windows.

Round 223 adds the final packaged implication.  In the subdivision criterion,
the profile hypotheses on the bipartite graph \(H=\operatorname{Sub}(G)\) can
be replaced by the shifted original radial-profile hypotheses from Round 222.
Thus, assuming the non-profile hypotheses of the one-parameter bipartite
criterion on \(H\), exponent control of
\[
  \mathfrak F_{Q,\rho}^{G\to H,{\rm rad}},
  \qquad
  \mathfrak L_{Q,\rho}^{G\to H,{\rm rad}},
  \qquad Q=q^2,
\]
implies \(p_c(G)<p_{2\to2}(G)\).  A fresh web check again located only
special-case confirmations of Benjamini--Schramm, including the
nonunimodular and hyperbolic quasi-transitive cases, and the \(L^2\) condition
continues to appear as a conjectural sufficient route for the general
nonamenable transitive case.

Round 224 makes the shifted original criterion more usable.  It first fixes
the negative-defect convention
\[
  \mathfrak R_{n,d}^{G,{\rm rad,saw,sph}}=0\qquad(d<0),
\]
so terms with \(B-a<0\) in the subdivision comparison are unambiguous.  It
then bins the finite shifted profile by
\[
  i\delta L_H\le d<(i+1)\delta L_H,
  \qquad
  0\le i<
  \left\lfloor\frac{\rho}{2\delta}\right\rfloor+1.
\]
Since \(Q<1\), finite-profile control follows from finitely many exponent
inequalities with shift \(i\delta\log_{D_H}Q\), plus the shifted tail profile.

Round 225 applies the same binning idea to the shifted tail, leaving only a
true far-tail term.  Given \(\lambda>\rho/2\), split
\[
  \mathfrak L_{Q,\rho}^{G\to H,{\rm rad}}
\]
into defects \(d\le\lambda L_H\) and \(d>\lambda L_H\).  The first range is
covered by finitely many bins
\[
  i\delta L_H\le d<(i+1)\delta L_H,
\]
with exponent shifts \(i\delta\log_{D_H}Q\); the \(O(L_H)\) number of integer
defects in each bin is negligible on the logarithmic scale.  The second range
is the far-tail profile
\[
  \mathfrak Y_{Q,\lambda}^{G\to H,{\rm rad}}.
\]
Thus the remaining shifted-tail work is a finite family of binned defect
estimates plus one far-tail estimate.

Round 226 localizes the far tail.  For a path \(\gamma\), let
\[
  M_x(\gamma)=\max_t d(x,v_t)
\]
and let \(D_x(\gamma;A)\) be the contribution to \(2I_x+H_x\) from
non-outward steps whose starting radius lies in a radial interval \(A\).  Fix
\(\sigma,\beta>0\).  A far-tail path with defect \(d>\lambda L_H\) either
overshoots its endpoint radius by more than \(\sigma L_H\), or all its radial
levels lie in \(O_{\sigma,\beta,\alpha_\omega,s}(1)\) slabs of width
\(\beta L_H\).  In the latter case, one slab carries at least
\[
  \frac{\lambda}{J_{\sigma,\beta}}L_H
\]
units of radial defect.  Hence
\[
  \mathfrak Y_{Q,\lambda}^{G\to H,{\rm rad}}
  \le
  \mathfrak O_{Q,\lambda,\sigma}^{G\to H,{\rm rad}}
  +
  \sum_{j<J_{\sigma,\beta}}
  \mathfrak V_{Q,\lambda,\sigma,\beta,j}^{G\to H,{\rm rad}}.
\]
The remaining far-tail work is therefore an overshoot estimate plus finitely
many heavy-slab estimates.

Round 227 shows that the overshoot estimate can be pushed to a deeper far
tail.  If a path starts at \(x\), ends in \(S_r(x)\), and reaches maximum
radius \(M_x(\gamma)\), then the suffix from the maximum radius back to the
endpoint contains at least \(M_x(\gamma)-r\) inward steps.  Hence
\[
  2I_x(\gamma)+H_x(\gamma)\ge2(M_x(\gamma)-r).
\]
Consequently
\[
  \mathfrak O_{Q,\lambda,\sigma}^{G\to H,{\rm rad}}
  \le
  \mathfrak Y_{Q,\max\{\lambda,2\sigma\}}^{G\to H,{\rm rad}}.
\]
Choosing \(\sigma>\lambda/2\) absorbs overshoot into a strictly deeper
far-tail cutoff.  The substantive local obstruction is therefore the
heavy-slab profile, plus a strategy for terminating or iterating the deeper
far-tail ladder.

Round 228 packages that iteration.  Given
\[
  \lambda_0<\lambda_1<\cdots<\lambda_N,
  \qquad \lambda_0>\rho/2,
\]
set \(\sigma_i=\lambda_{i+1}/2\).  Combining the Round 226 split and the
Round 227 overshoot amplification gives
\[
  \mathfrak Y_{Q,\lambda_0}^{G\to H,{\rm rad}}
  \le
  \mathfrak Y_{Q,\lambda_N}^{G\to H,{\rm rad}}
  +
  \sum_{i<N}\sum_{j<J_{\sigma_i,\beta_i}}
  \mathfrak V_{Q,\lambda_i,\sigma_i,\beta_i,j}^{G\to H,{\rm rad}}.
\]
Thus the far-tail problem can be driven to a terminal deeper cutoff, leaving
only finitely many heavy-slab estimates along the way.

Round 147 records the immediate consequence for the endpoint-anchor dichotomy.
Its parameter range has
\[
  \theta<1/31<1/19,
  \qquad
  B<\frac{1-21\theta}{2}<\frac{1-6\theta}{2}.
\]
Thus Round 146 applies directly and forces
\[
  2^j>B\log_\Delta\bar\chi_p
\]
throughout the endpoint-anchor range.  The logarithmic endpoint-anchor mass
alternative is therefore not needed as a live branch there; it remains useful
mainly as a diagnostic for how the mass would localize if a weaker scale
amplification were all that was available.

Round 021 improves the \(p_c\)-upper side for the same remaining case by using
a finite-type interval branching lower process.  Type \(m\le M\) records that a
reached fiber contains a contiguous reachable interval of length \(m\), capped
at \(M\).  From such an interval, all open horizontal seed heights into each
child fiber are retained before expanding through the child line.  This gives a
finite mean matrix \(A^{(M)}(p)\) with entries
\[
  A^{(M)}_{m\ell}(p)=2P^{(M)}_{m\ell}(p)
\]
for \(T_3\square\mathbb Z\).  If \(\rho(A^{(M)}(p))>1\), then
\(p\ge p_c(T_3\square\mathbb Z)\), with a strict bound when the inequality is
strict at \(p\).

For \(M=6\) and \(p=61/200\), exact enumeration gives the rational certificate
\[
  v=(6271,11456,15785,19374,22333,24781),\qquad
  \min_m\frac{(A^{(6)}(p)v)_m}{v_m}>1.00714.
\]
Thus
\[
  p_c(T_3\square\mathbb Z)<61/200.
\]
This is a real improvement over the two-step bound, but it still leaves a wide
gap on the SAW side: closing the line-factor case this way would require
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<200/61\approx3.27869,
\]
while the best current finite-length certificate is \(3.647512\).  The exact
calculation is reproducible with `scripts/interval_branching_bound.py`.
Monte Carlo for the full oriented reachable-height process places its threshold
near \(p\approx0.295\), so preserving more finite oriented fiber state is
unlikely by itself to reach the \(0.273\) range required by the current SAW
bound.

Round 023 uses Yamamoto's fixed-direction characterization of
\(p_c(T_d\square\mathbb Z)\) to make a non-oriented improvement for the
remaining \(T_3\square\mathbb Z\) case.  Inside the geodesic strip, attach one
off-geodesic side fiber at each column and restrict to the seven heights
\(\{-3,\ldots,3\}\).  Integrating out the nineteen edges of one decorated column
gives a \(127\times127\) transfer matrix \(M(p)\) on non-empty height subsets.
At \(p=303/1000\), exact integer arithmetic verifies a positive integer vector
\(v\) such that
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.00218.
\]
Thus the fixed-direction exponent satisfies \(\alpha(303/1000)>1/2\), and
Yamamoto's criterion gives
\[
  p_c(T_3\square\mathbb Z)<303/1000.
\]
This improves the target for the SAW side to
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<1000/303\approx3.30033.
\]
The exact certificate is reproducible with
`scripts/decorated_strip_bound.py --height-count 7 --p-num 303 --p-den 1000`.

Round 024 replaces the \(2^{3h-2}\) edge enumeration for the depth-one
decorated strip by an exact transfer along the height direction.  This makes
the nine-height window \(\{-4,\ldots,4\}\) practical.  The one-column gadget has
twenty-five edges and the transfer matrix has size \(2^9-1=511\).  At
\[
  p=149/500,
\]
integer arithmetic verifies
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.00344
\]
for a positive integer vector \(v\).  Hence
\[
  p_c(T_3\square\mathbb Z)<149/500.
\]
The current SAW target improves to
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<500/149\approx3.35570.
\]

Round 025 sharpens the same nine-height certificate close to its observed
crossing point.  With the same \(511\times511\) transfer matrix, the rational
parameter
\[
  p=743/2500
\]
still has an exact Perron-Frobenius certificate:
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.00018.
\]
Therefore
\[
  p_c(T_3\square\mathbb Z)<743/2500,
\]
and the current SAW target becomes
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<2500/743\approx3.36474.
\]

Round 026 pushes the same certificate to the edge of the nine-height method.
The rational value
\[
  p=7429/25000=0.29716
\]
has an exact certificate
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.00004,
\]
while \(14857/50000=0.29714\) falls below \(1/2\) in floating point and is not
certified by the same Perron vector.  Thus the current rigorous bound is
\[
  p_c(T_3\square\mathbb Z)<7429/25000,
\]
with SAW target
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<25000/7429\approx3.36519.
\]

Round 027 makes the depth-one decorated-strip computation sparse in the output
mask and in matrix-vector application, which makes the ten-height strip
\(\{-4,\ldots,5\}\) practical.  The transfer matrix has size
\(2^{10}-1=1023\).  At
\[
  p=591/2000,
\]
exact integer arithmetic verifies
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.00016.
\]
Thus
\[
  p_c(T_3\square\mathbb Z)<591/2000,
\]
and the current SAW target becomes
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<2000/591\approx3.38409.
\]

Round 028 uses the same ten-height sparse transfer and moves the rational
just above the observed crossing.  At
\[
  p=5909/20000,
\]
the exact integer certificate with scale \(10^8\) gives
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.000006.
\]
Thus
\[
  p_c(T_3\square\mathbb Z)<5909/20000,
\]
and the current SAW target becomes
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<20000/5909\approx3.38467.
\]
The same round also adds a row-frontier transfer for side-depth \(2\)
decorated columns.  It agrees with dense enumeration on small windows, but the
tested \(h=5\), side-depth \(2\) strip has spectral lower bound only
\(0.474980517265\) at \(p=3/10\), so it is not yet competitive with the
height-ten depth-one certificate.

Round 029 audits the remaining numerical gap for \(T_3\square\mathbb Z\).  The
nonbacktracking threshold is
\[
  1/\beta(5,2\sqrt2+2)=0.265505028230,
\]
and the best current finite-length SAW threshold is
\[
  1/\|C_{15}\|_{2\to2}^{1/15}=0.274159516989.
\]
The current decorated-strip \(p_c\)-upper certificate \(0.29545\) is still
above these by \(0.029944971770\) and \(0.021290483011\), respectively.
Thus incremental sharpening of the same height-ten fixed-ray strip cannot
close the remaining case; the next useful step has to be a structural
SAW/operator bound, a materially stronger finite-type percolation comparison,
or a direct \(p_{2\to2}\) estimate that avoids the global SAW union bound.

Round 030 first adds a floating-point decorated-strip scanner using the same
row-frontier state as the exact script.  It matches the exact side-depth \(2\),
\(h=3\), \(p=0.3\) value \(0.426310751826\).  The larger \(h=6\),
side-depth \(2\), \(p=0.3\) scan gives only \(0.488883555861\), so this window
is still not competitive.

The same round adds a fast floating-point scanner for the interval-branching
lower process.  It computes the same transition law as the exact cap-\(M\)
script by scanning vertical open components rather than enumerating all seed
and edge masks.  The scan matches the exact values at \(M=6,7\), and gives
threshold estimates
\[
\begin{array}{c|ccccc}
M&6&7&8&10&12\\
\hline
p_M&0.303335949245&0.302987507205&0.302876735094&
0.302831341492&0.302827045924.
\end{array}
\]
Thus the one-interval finite-type lower process appears to saturate near
\(0.302827\), far above \(0.274159516989\), the threshold needed to combine
with the current \(m=15\) SAW certificate.  Future percolation-side attempts
must retain more geometry than a single contiguous interval in a reached
fiber, or switch to a direct \(p_{2\to2}\) bound.

Round 031 tests exactly that richer finite-fiber-state direction.  A
finite-subset lower process retains a normalized non-empty subset of
\(\{0,\ldots,W\}\), rather than just the longest interval.  The retained child
type is chosen as a reached subset of span at most \(W\), so the process is
still dominated by the true oriented fiber exploration.  Floating thresholds
for the cardinality selector are
\[
\begin{array}{c|cccccc}
W&2&3&4&5&6&7\\
\hline
p_W&0.316714332031&0.304788514903&0.299989501051&
0.297859216380&0.296860517956&0.296377903218.
\end{array}
\]
For \(W=8\), fixed-\(p\) probes bracket the threshold in
\((0.2961,0.2962)\).  This substantially improves the one-interval family but
still does not beat the decorated-strip certificate \(0.29545\).  A weighted
selector that keeps the reached subset maximizing a positive test-vector
weight was also tested at \(W=7\); it gives ratios \(0.995691051183\) at
\(p=0.29545\) and \(1.000104820600\) at \(p=0.2964\), so it does not
materially improve the threshold at this size.

Round 032 switches from one-generation fiber processes to a depth-two
tree-block process.  From one retained vertical subset, expose a finite forward
binary tree of depth two and keep bounded-span reached subsets in the four
boundary fibers.  A Monte Carlo scan with type width \(W=5\), margin \(2\),
and cardinality selector gives
\[
\begin{array}{c|c}
p&\widehat\rho_{\rm lower}\\
\hline
0.28000&1.07116952698\\
0.274159516989&1.00965759948\text{ to }1.01436567177\\
0.27200&0.984663250668.
\end{array}
\]
This is not a proof, but it is the first percolation-side diagnostic to reach
the current finite-length SAW threshold
\[
  1/\|C_{15}\|_{2\to2}^{1/15}=0.274159516989.
\]
Two deterministic row-frontier prototypes were added, one keeping the best
subset of the union of reached boundary components and one keeping only the
best single reached component.  Both are still too slow on depth-two windows.
The next concrete target is therefore an exact rational or interval-arithmetic
transfer for this depth-two block process at the \(m=15\) SAW threshold.

Round 033 audits the regeneration in the depth-two block idea and corrects the
interpretation of the Round 032 Monte Carlo.  The sampled block exposed
vertical edges both in the incoming root fiber and in the outgoing boundary
fibers.  Iterating that block would reuse boundary-fiber vertical randomness,
so it is not a Galton-Watson lower process as stated.  Two valid factorized
mean computations were added.  If the state is already vertically expanded at
block entry and the leaves are vertically expanded before retention, the
type-width \(5\), margin \(2\) threshold is
\[
  0.308089193427.
\]
If the state is instead a raw seed set and the block expands the root and
middle fibers but leaves boundary vertical edges unexposed for the next block,
the regenerative threshold is
\[
  0.304900973287.
\]
At \(p=0.274159516989\), this valid regenerative ratio is only
\[
  0.758932096832,
\]
and a \(W=6\), margin \(2\) probe at \(p=0.28\) gives \(0.815985271421\).
Thus the valid depth-two block variants currently tested do not improve the
percolation side; the Monte Carlo result remains only a heuristic warning that
boundary-state bookkeeping is the key issue.

Round 034 tests whether the valid block conventions or larger one-step
finite-subset retention improve with width.  For type width \(7\), margin \(2\),
the valid depth-two factorized and regenerative ratios at \(p=0.296\) are only
\[
  0.955948146115,\qquad 0.954221772699,
\]
while at \(p=0.302\) they are
\[
  1.008236280010,\qquad 1.006719233170.
\]
So these valid block thresholds remain near \(0.301\).  The one-step
finite-subset process is closer: for \(W=9\),
\[
\begin{array}{c|cccc}
p&0.29545&0.29580&0.29600&0.29605\\
\hline
\rho_{\rm lower}&0.997311302109&0.998952678348&
0.999890906372&1.000125497220,
\end{array}
\]
and for \(W=10\) at \(p=0.29545\) the ratio is \(0.997581067940\).  Thus this
retention rule still does not beat the decorated-strip certificate
\(5909/20000=0.29545\), and its width improvement is slow.

## Route B: spectral contradiction

If finite-set escape fails, there are \(p_n\uparrow p_c\) and finite sets
\(K_n\) with large normalized internal mass. The associated normalized
indicators \(f_n=|K_n|^{-1/2}\mathbf 1_{K_n}\) satisfy
\[
    \langle f_n,Q_{p_n}f_n\rangle \ge \epsilon.
\]

One wants to push this to an almost-invariance statement under the simple
random walk operator \(P\), using percolation differential inequalities,
BK/Reimer inequalities, and comparison of \(T_p\) with graph-geometric
Green-type kernels. If successful, nonamenability (\(\|P\|_{2\to2}<1\)) gives a
contradiction.

Round 043 records a guardrail for this route.  On
\(\Gamma=F_2\times\mathbb Z\), for every \(\delta>0\) there is a finitely
supported symmetric generating probability measure \(\mu\) and a finite
\(\mathbb Z\)-segment \(K\) such that
\[
  |K|^{-1}\sum_{x,y\in K}\mu(x^{-1}y)\ge1-\delta .
\]
Thus nonamenability plus symmetry/adaptation of a kernel is not enough.  A
spectral contradiction has to use percolation-specific features of \(Q_p\),
such as BK, differential inequalities, the two-point convolution inequalities,
or a tilted/backscattering structure in the spirit of Hutchcroft--Pan.

## Route C: counterexample search as proof guard

Because the global theorem is open, every proposed proof should be stress
tested against:

- products \(T\times H\);
- lamplighter and wreath-product examples;
- graphs with one end and no hyperbolicity;
- nonunimodular examples where the theorem is already known;
- amenable quasi-transitive graphs, where \(p_c=p_u\) and the target must fail.

## Immediate next tasks

1. Use the last-exit decomposition to rule out the interior alternative
   \(S_p(K)\gtrsim \bar\chi_p|K|\).  A concrete route is to verify the
   killed-SAW growth condition \(A_n(K)\le C\theta^n\) with \(\theta<1/p_c\),
   equivalently \(\kappa_{\rm kill}<1/p_c\).
2. Bound the boundary-transfer alternative by estimating the energy
   \(\langle\mu_{p,K},Q_p\mu_{p,K}\rangle\), not merely by bounding
   \(\|\mu_{p,K}\|_2\).  The target is
   \(\sup_K\mathcal E_p(K)\to0\).
3. Re-read the proof of Hutchcroft's Proposition 2.7 and isolate exactly where
   nonamenability enters in known geometric cases.
4. Abstract the Hutchcroft--Pan relative/tilted mechanism beyond exact product
   and lamplighter models, or identify a unimodular replacement for its
   backscattering step.
5. Keep the paper draft honest: conditional reductions are not promoted to a
   proof of the open problem.

## Round 229 heavy-slab token split

The far-tail ladder now reduces the localized slab obstruction further.  For a
heavy slab \(A\),
\[
  D_x(\gamma;A)=2I_x(\gamma;A)+H_x(\gamma;A),
\]
so any path with \(D_x(\gamma;A)>\theta L_H\) is either inward-heavy
\(I_x(\gamma;A)>\theta L_H/4\) or horizontal-heavy
\(H_x(\gamma;A)>\theta L_H/2\).  This yields the profile bound
\[
  \mathfrak V^{\rm rad}
  \le
  \mathfrak V^{\rm rad,in}
  +
  \mathfrak V^{\rm rad,hor}.
\]
The inward-heavy term has a fixed-\(K\) refinement:
either inward tokens appear on more than \(\theta L_H/(4K)\) levels of the
slab, or one level carries more than \(K\) inward tokens.  Each inward token at
level \(u\) pairs with a last preceding \(u-1\to u\) crossing and gives an
exterior return segment whose interior stays outside \(B_{u-1}(x)\).

Next target: convert one of the three sharpened obstructions
(horizontal-heavy, spread-inward, or level-congested exterior returns) into an
actual exponential saving.  The likely route is to compare these localized
return segments with boundary/annulus energy rather than ambient degree
growth.

## Round 230 tokenized ladder

The far-tail ladder and token split are now combined.  For cutoffs
\(\lambda_i\), slab widths \(\beta_i\), and congestion thresholds \(K_i\),
\[
  \mathfrak Y_{\lambda_0}
  \le
  \mathfrak Y_{\lambda_N}
  +
  \sum_{i,j}\mathfrak V_{i,j}^{\rm hor}
  +
  \sum_{i,j}\mathfrak V_{i,j,K_i}^{\rm in,spr}
  +
  \sum_{i,j}\mathfrak V_{i,j,K_i}^{\rm in,con}.
\]
This is the cleanest current endpoint of the subdivision/radial-profile
route.  The problem is no longer phrased as one monolithic long-excess SAW
tail; it is a finite list of localized slab estimates plus a terminal
far-tail estimate.

The annulus/gate machinery nearby is percolation-kernel based, while these
slab profiles are deterministic SAW-count profiles.  A direct bridge must
therefore supply a counting-to-operator or counting-to-energy comparison; it
cannot be imported for free from the existing gate-obstruction lemmas.

## Round 231 exact-level exterior-return localization

The level-congested inward profile has been localized to exact levels.  Define
\(\mathcal X_{u,K}\) as the event that a rooted SAW contains more than \(K\)
exterior return subpaths through level \(u\), each leaving \(S_{u-1}(x)\) to
level \(u\), staying outside \(B_{u-1}(x)\), and then returning to
\(S_{u-1}(x)\).  Let
\[
  \mathfrak X_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,ret}}
\]
be the worst exact-level profile over \(u\) in the slab.  Then
\[
  \mathfrak V_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,in,con}}
  \le
  W_{\beta,p}\,
  \mathfrak X_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,ret}}.
\]
The factor \(W_{\beta,p}=O(L_H)\) is exponent-negligible.  Thus the
congested term in the tokenized ladder is no longer a slab estimate; it is a
worst-level exterior-return estimate.  This is a more natural place to try a
future counting-to-annular-energy bridge.

## Round 232 exterior-return ladder

The exact-level return localization has now been folded back into the ladder.
For \(X_{i,j}^{\rm ret}
=\mathfrak X_{Q,\lambda_i,\sigma_i,\beta_i,j,K_i}^{G\to H,{\rm rad,ret}}\),
\[
  \mathfrak Y_{\lambda_0}
  \le
  \mathfrak Y_{\lambda_N}
  +
  \sum_{i,j}\mathfrak V_{i,j}^{\rm hor}
  +
  \sum_{i,j}\mathfrak V_{i,j,K_i}^{\rm in,spr}
  +
  \sum_{i,j} W_{\beta_i,p}X_{i,j}^{\rm ret}.
\]
The \(W_{\beta_i,p}\) factors have \(o(L_H)\) logarithmic size.  The primitive
localized obligations are therefore now:
terminal far tail, horizontal-heavy slabs, spread-inward slabs, and exact
level exterior returns.  This is the current best formal reduction endpoint.

## Round 233 spread-return conversion

The spread-inward profile has also been translated into exterior-return
language.  Allowing \(\mathcal X_{u,0}\) to mean at least one exterior return
through level \(u\), define
\[
  \mathcal X^{\rm spr}_{j,K,p}
  =
  \left\{
    \#\{u\in A_{j,p}: \mathcal X_{u,0}\}
    >
    \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
  \right\}.
\]
The inward-token return lemma gives
\[
  \mathfrak V_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,in,spr}}
  \le
  \mathfrak X_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,ret,spr}}.
\]
Thus the current ladder endpoint is
\[
  \mathfrak Y_{\lambda_0}
  \le
  \mathfrak Y_{\lambda_N}
  +
  \sum_{i,j}\mathfrak V_{i,j}^{\rm hor}
  +
  \sum_{i,j}S_{i,j}^{\rm ret}
  +
  \sum_{i,j}W_{\beta_i,p}X_{i,j}^{\rm ret}.
\]
The remaining nonterminal targets are horizontal-heavy slabs, spread
exterior-return levels, and exact-level repeated exterior returns.  This
organizes the next attack around return-counting and same-level motion.

## Round 234 same-sphere horizontal localization

The horizontal-heavy profile has been split by exact radial level.  Define
\[
  \mathcal Z_{u,K}=\{H_x(\gamma;\{u\})>K\}
\]
and the spread property
\[
  \mathcal Z^{\rm spr}_{j,K,p}
  =
  \left\{
    \#\{u\in A_{j,p}:H_x(\gamma;\{u\})>0\}
    >
    \frac{\theta_{\lambda,\sigma,\beta}}{2K}L_H
  \right\}.
\]
Then
\[
  \mathfrak V_{Q,\lambda,\sigma,\beta,j}^{G\to H,{\rm rad,hor}}
  \le
  \mathfrak Z_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,hor,spr}}
  +
  W_{\beta,p}
  \mathfrak Z_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,hor,lev}}.
\]
The fully localized ladder now reduces the initial far tail to:
terminal far tail, same-sphere spread, exact-level same-sphere congestion,
spread exterior returns, and exact-level repeated exterior returns.  This is
the sharpest current deterministic decomposition of the long-defect
obstruction.

## Round 235 localized subdivision criterion

The fully localized ladder is now packaged back into the main subdivision
route.  The tail profile
\(\mathfrak L_{Q,\rho}^{G\to H,{\rm rad}}\) is controlled by:
near-tail bins \(\mathfrak E_{a,\delta}^{G\to H,{\rm rad}}\), a terminal
far-tail profile \(\mathfrak Y_{Q,\lambda_N}^{G\to H,{\rm rad}}\), and the
four localized profile families from Round 234.

Combining this with the finite-defect bins
\(\mathfrak D_{a,\delta_{\rm fin}}^{G\to H,{\rm rad}}\) gives the current
most explicit conditional route to
\[
  p_c(G)<p_{2\to2}(G).
\]
The remaining mathematical burden is now sharply identified: prove the
required exponent bounds for the finite bins, near-tail bins, terminal far
tail, same-sphere spread/congestion, and exterior-return spread/congestion.

## Round 236 tangential run split

Exact-level same-sphere congestion has been split into long tangential runs
and many tangential runs.  For an exact level \(u\), let \(T_x^u(\gamma)\) be
the maximum length of a contiguous segment of \(\gamma\) lying in \(S_u(x)\),
and \(R_x^u(\gamma)\) the number of such positive-length segments.  If
\[
  H_x(\gamma;\{u\})>K,
\]
then for every \(L\ge1\),
\[
  T_x^u(\gamma)>L
  \quad\text{or}\quad
  R_x^u(\gamma)>\lfloor K/L\rfloor.
\]
The same-sphere congestion profile is therefore reduced to a long-run profile
and a many-run profile.  This gives a more geometric target: either the graph
has long SAW motion inside one exact sphere, or the path repeatedly enters
tangential episodes at the same radius.

## Round 237 tangential localized criterion

The tangential ladder is now connected back to the subdivision route.  The
tail profile is controlled by near-tail bins, a terminal far tail, and the
five tangentially localized families:
\[
  Z^{\rm spr},\qquad
  T^{\rm long},\qquad
  T^{\rm many},\qquad
  S^{\rm ret},\qquad
  X^{\rm ret}.
\]

Together with the finite-defect bins \(\mathfrak D\), this gives a sharper
conditional route to \(p_c(G)<p_{2\to2}(G)\).  The live estimates are now
finite/near-tail bins, terminal far tail, same-sphere spread, long tangential
runs, many tangential runs, spread returns, and repeated returns.

## Round 238 adjacent-crossing tangential split

The many-run target has been split into four two-sided adjacent-crossing
types.  A level-\(u\) tangential run is assigned type
\((\eta,\zeta)\in\{-1,+1\}^2\) when the vertex immediately before the run is
in \(S_{u+\eta}(x)\) and the vertex immediately after the run is in
\(S_{u+\zeta}(x)\).  At most two tangential runs can touch an endpoint of the
whole path, so for \(R\ge2\),
\[
  \mathcal T^{\rm many}_{u,R}
  \subseteq
  \bigcup_{\eta,\zeta\in\{-1,+1\}}
  \mathcal C^{\eta,\zeta}_{u,\lfloor(R-2)/4\rfloor}.
\]
Consequently the live many-run estimate is replaced by four more structured
crossing estimates.  The current conditional endpoint is:
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  Z^{\rm spr},\quad
  T^{\rm long},\quad
  C^{-,-},C^{-,+},C^{+,-},C^{+,+},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

The next natural targets are to estimate \(C^{-,+}\) and \(C^{+,-}\) through
adjacent-level crossing counts, and to separate \(C^{-,-}\) and \(C^{+,+}\)
as repeated same-side tangential excursions.

## Round 239 return absorption of adjacent crossings

The adjacent-crossing target has been reduced further.  If a level-\(u\)
tangential crossing run exits to \(S_{u-1}(x)\), then it ends with an inward
level-\(u\) token, and hence gives an exterior return through level \(u\).
This covers \(C^{-,-}\) and \(C^{+,-}\).  If there are \(q\) runs of type
\((-1,+1)\), then each gap between consecutive runs must contain an inward
level-\(u\) token, so \(q\) runs give at least \(q-1\) same-level returns.
Thus, for \(R\ge1\) and \(K=R-1\),
\[
  C^{-,-}_{R},\ C^{+,-}_{R},\ C^{-,+}_{R}
  \preceq X^{\rm ret}_{K}.
\]
The only remaining crossing type is \(C^{+,+}\), whose entry edge is an
inward level-\(u+1\) token.  It is therefore controlled by an upper-shifted
return profile:
\[
  C^{+,+}_{R}\preceq X^{\rm ret,up}_{K}.
\]

The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  Z^{\rm spr},\quad
  T^{\rm long},\quad
  S^{\rm ret},\quad
  X^{\times},\quad
  X^{\rm ret,up},\quad
  X^{\rm ret}.
\]
This is a genuine simplification: the many-run obstruction no longer needs a
new tangential crossing estimate, except through the already central
exterior-return mechanism and its one-level upper shift.

## Round 240 return-only boundary shift

The upper-shifted return family is not a genuinely new profile.  Since the
slabs are consecutive half-open intervals
\[
  A_{j,p}=[jW_{\beta,p},(j+1)W_{\beta,p}),
\]
an integer \(u\in A_{j,p}\) has \(u+1\in A_{j,p}\cup A_{j+1,p}\).  Therefore
\[
  X^{\rm ret,up}_{j,K}
  \le
  X^{\rm ret}_{j,K}+X^{\rm ret}_{j+1,K}.
\]
Substituting this into the Round 239 ladder turns
\[
  3X_{i,j}^{\times}+U_{i,j}^{\times}
\]
into
\[
  4B_{i,j}^{\times}+B_{i,j+1}^{\times},
\]
where \(B^\times\) is an ordinary exact-level exterior-return profile with
the crossing-generated threshold \(K_i^\times\).  The only new bookkeeping is
that \(j\) runs through one extra endpoint slab \(J_{\sigma_i,\beta_i}\).

The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  Z^{\rm spr},\quad
  T^{\rm long},\quad
  S^{\rm ret},\quad
  B^{\times},\quad
  X^{\rm ret}.
\]
The many-run and adjacent-crossing mechanisms have therefore been fully
absorbed into the exterior-return framework.

## Round 241 threshold-dominated return absorption

The crossing-generated return profiles from Round 240 are ordinary
exact-level return profiles with a different threshold:
\[
  B_{i,j}^{\times}
  =
  X^{\rm ret}_{i,j,K_i^\times}.
\]
If the tail parameters are chosen so that \(K_i^\times\ge K_i\), then
\[
  \mathcal X_{u,K_i^\times}\subseteq\mathcal X_{u,K_i},
\]
and hence
\[
  B_{i,j}^{\times}\le \widehat X_{i,j}^{\rm ret}.
\]
The return-only ladder becomes a threshold-dominated return ladder with
ordinary return terms only:
\[
  \mathfrak Y_{\lambda_0}
  \le
  \mathfrak Y_{\lambda_N}
  + Z^{\rm spr}
  + W T^{\rm long}
  + S^{\rm ret}
  + W(5\widehat X^{\rm ret}_{j}+\widehat X^{\rm ret}_{j+1}).
\]
Thus the current conditional endpoint is
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  Z^{\rm spr},\quad
  T^{\rm long},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

This is the cleanest form of the localized reduction so far: all many-run
and crossing-generated obstructions are now part of the same exterior-return
profile family.

## Round 242 same-sphere spread split

Same-sphere spread is split into outward-through tangential spread and
return-generating spread.  If many levels have \(H_x(\gamma;\{u\})>0\), then
except for at most two endpoint levels each contributes a two-sided tangential
run.  Levels with type \((-1,+1)\) are recorded by \(U^{\rm out}\).  The
other three types yield inward tokens at level \(u\) or \(u+1\), hence
exterior returns.  The level map has multiplicity at most two and lands in
\(A_{j,p}\cup A_{j+1,p}\), giving
\[
  Z^{\rm spr}_{j,K}
  \preceq
  U^{\rm out}_{j,K}
  +X^{\rm ret,spr}_{j,8K}+X^{\rm ret,spr}_{j+1,8K}.
\]
Current endpoint:
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  U^{\rm out},\quad
  T^{\rm long},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 243 record outward-through split

The outward-through profile now has its own return split.  A
\((-1,+1)\)-run at level \(u\) is record outward-through if the run starts at
the first visit to level \(u\).  If an outward-through level is not record,
then there was an earlier visit to level \(u\); since the selected run is
entered from level \(u-1\), the path must cross inward from \(u\) to \(u-1\)
between the earlier visit and the run.  The inward-token lemma gives
\(\mathcal X_{u,0}\).  Therefore
\[
  U^{\rm out}_{j,K}
  \le
  U^{\rm rec}_{j,2K}
  +X^{\rm ret,spr}_{j,2K}
  \le
  U^{\rm rec}_{j,2K}
  +X^{\rm ret,spr}_{j,8K}.
\]
After substitution, the live conditional endpoint is
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  U^{\rm rec},\quad
  T^{\rm long},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 244 subterminal record split

Record outward-through levels can be split relative to the endpoint radius
\[
  e_x(\gamma)=d(x,v_\ell).
\]
If a record level \(u\) satisfies \(u\ge e_x(\gamma)\), then its selected
\((-1,+1)\)-run exits to level \(u+1\), and the path must later return to
level \(u\) to finish at radius at most \(u\).  The first such return is an
inward level-\(u+1\) token and yields \(\mathcal X_{u+1,0}\).  Since
\(u+1\in A_{j,p}\cup A_{j+1,p}\), the deterministic split is
\[
  U^{\rm rec}_{j,K}
  \le
  U^{\rm sub}_{j,2K}
  +X^{\rm ret,spr}_{j,4K}
  +X^{\rm ret,spr}_{j+1,4K}.
\]
Applied to the Round 243 ladder, the live conditional endpoint becomes
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  U^{\rm sub},\quad
  T^{\rm long},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 245 persistent subterminal split

Subterminal record levels are split according to whether they persist until
the first hit of the endpoint sphere.  Let
\[
  \tau_x^{\rm end}(\gamma)=\min\{t:d(x,v_t)=e_x(\gamma)\}.
\]
If the path returns to level \(u\) after the record \((-1,+1)\)-run exits to
level \(u+1\) and before \(\tau_x^{\rm end}\), the first such return is an
inward level-\(u+1\) token.  Hence
\[
  U^{\rm sub}_{j,K}
  \le
  U^{\rm per}_{j,2K}
  +X^{\rm ret,spr}_{j,4K}
  +X^{\rm ret,spr}_{j+1,4K}.
\]
The finite ladder absorbs the resulting \(16M_i\)-threshold spread-return
terms into the same spread-return family.  The live conditional endpoint is
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  U^{\rm per},\quad
  T^{\rm long},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 246 deep persistent tightening

Persistent subterminal record levels near the endpoint sphere occupy only a
short terminal band.  With
\[
  B=\frac{\theta_{\lambda,\sigma,\beta}}{8K}L_H,
\]
there are at most \(B\) integer levels satisfying
\[
  0<e_x(\gamma)-u\le B.
\]
Hence more than \(2B\) persistent levels force more than \(B\) levels with
\[
  e_x(\gamma)-u>B,
\]
which gives
\[
  U^{\rm per}_{j,K}\le U^{\rm deep}_{j,2K}.
\]
The live conditional endpoint is therefore
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  U^{\rm deep},\quad
  T^{\rm long},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 247 endpoint-prefix horizontal residual

Deep persistent record levels are now recorded only through their prefix
geometry.  If \(u\) is deep persistent, its record \((-1,+1)\)-run \([a,b]\)
lies before the first hit of the endpoint sphere:
\[
  b<\tau_x^{\rm end}(\gamma),
  \qquad
  e_x(\gamma)-u\gg L_H.
\]
Thus
\[
  U^{\rm deep}_{j,K}
  \le
  P^{\rm pre}_{j,K},
\]
where \(P^{\rm pre}\) is endpoint-prefix deep horizontal spread.  The live
conditional endpoint is
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre},\quad
  T^{\rm long},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 248 short endpoint-prefix residual

The endpoint-prefix residual now splits into a long-run part already present
in the ladder and a short prefix-spread part.  For \(K,L\ge1\),
\[
  P^{\rm pre}_{j,K}
  \le
  W_{\beta,p}T^{\rm long}_{j,L}
  +
  P^{\rm pre,sh}_{j,K,L}.
\]
Indeed, if the endpoint-prefix property holds but its short version fails,
then one counted level has a prefix tangential run of length \(>L\), and the
union bound over the slab costs at most \(W_{\beta,p}\).

With \(K=16M_i\) and \(L=L_i\), the finite ladder becomes the same as the
Round 247 ladder except that \(P^{\rm pre}\) is replaced by
\(P^{\rm pre,sh}\) and the long-run contribution is multiplied by \(2\).
Since the multiplier is fixed and
\[
  \log_{D_H}W_{\beta_i,p}=o(L_H),
\]
the live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,sh},\quad
  T^{\rm long},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 249 short outward-prefix residual

The short endpoint-prefix residual now splits into a short outward-through
part and a return-generating part.  A short prefix run that is not of type
\((-1,+1)\) either exits inward from level \(u\) or enters inward from level
\(u+1\).  Except for the possible initial level \(u=0\), the existing
token-to-return lemma therefore gives a spread exterior return in the current
or next slab.  Quantitatively,
\[
  P^{\rm pre,sh}_{j,K,L}
  \le
  P^{\rm pre,out,sh}_{j,2K,L}
  +
  X^{\rm spr}_{j,16K}
  +
  X^{\rm spr}_{j+1,16K}.
\]

With \(K=16M_i\), the finite ladder replaces \(P^{\rm pre,sh}\) by
\[
  P^{\rm pre,out,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,32M_i,L_i}^{
    G\to H,{\rm rad,tan,pre,out,short}},
\]
and enlarges the spread-return threshold to \(256M_i\).  The live conditional
endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,out,sh},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 250 short prefix-record residual

The short outward-prefix residual now has the same record/non-record split as
the older outward-through profile, but retaining the prefix and short-run
constraints.  If a short prefix \((-1,+1)\)-run at level \(u\) is not the
first visit to \(u\), then before entering that run the path must return from
level \(u\) to level \(u-1\).  This is an inward level-\(u\) token, and the
token-to-return lemma gives an exterior return through level \(u\).  Thus
\[
  P^{\rm pre,out,sh}_{j,K,L}
  \le
  P^{\rm pre,rec,sh}_{j,2K,L}
  +
  X^{\rm spr}_{j,2K}.
\]

With \(K=32M_i\), the finite ladder replaces \(P^{\rm pre,out,sh}\) by
\[
  P^{\rm pre,rec,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,64M_i,L_i}^{
    G\to H,{\rm rad,tan,pre,out,rec,short}},
\]
and absorbs the added return term into \(X^{\rm spr,++}\).  The live
conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,rec,sh},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 251 short persistent-prefix residual

The short prefix-record residual is now split by persistence.  If a short
record prefix \((-1,+1)\)-run \([a,b]\) at level \(u\) does not stay above
level \(u\) until \(\tau_x^{\rm end}\), then the first return to level \(u\)
after the run is an inward level-\(u+1\) token.  Therefore
\[
  P^{\rm pre,rec,sh}_{j,K,L}
  \le
  P^{\rm pre,per,sh}_{j,2K,L}
  +
  X^{\rm spr}_{j,4K}
  +
  X^{\rm spr}_{j+1,4K}.
\]

With \(K=64M_i\), the finite ladder replaces \(P^{\rm pre,rec,sh}\) by
\[
  P^{\rm pre,per,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,128M_i,L_i}^{
    G\to H,{\rm rad,tan,pre,out,per,short}},
\]
and absorbs the added return terms into \(X^{\rm spr,++}\).  The live
conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,per,sh},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 252 ordered persistent-prefix ladder residual

The short persistent-prefix residual is now repackaged as an ordered
endpoint-prefix ladder.  If levels
\[
  u_1<\cdots<u_N
\]
are counted by \(P^{\rm pre,per,sh}_{j,K,L}\), then their record runs occur in
the same chronological order.  Indeed the run at \(u_q\) begins at the first
visit to level \(u_q\), and any first visit to \(u_{q+1}>u_q\) must occur
after the first visit to \(u_q\) and outside the level-\(u_q\) run.  Thus
\[
  P^{\rm pre,per,sh}_{j,K,L}
  \le
  P^{\rm pre,lad,sh}_{j,K,L}.
\]

With \(K=128M_i\), the finite ladder replaces the residual by
\[
  P^{\rm pre,lad,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,128M_i,L_i}^{
    G\to H,{\rm rad,tan,pre,out,per,lad,short}}.
\]
No coefficients change in this round.  The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,lad,sh},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 253 bounded-gap prefix-pair residual

The ordered prefix-ladder residual now has a bounded-gap successor-pair
subresidual.  If an ordered ladder has
\[
  u_1<\cdots<u_N\subset A_{j,p},
\]
then
\[
  \sum_{q=1}^{N-1}(u_{q+1}-u_q)\le W_{\beta,p}.
\]
For
\[
  B_{\lambda,\sigma,\beta,K}
  =
  \left\lceil
    \frac{16K\beta}{\theta_{\lambda,\sigma,\beta}}
  \right\rceil+1,
\]
the number of successor gaps larger than \(B_{\lambda,\sigma,\beta,K}\) is
less than \(\theta_{\lambda,\sigma,\beta}L_H/(16K)\) for \(p\) close to
\(\pc(H)\).  Therefore linearly many successor pairs have bounded level gap:
\[
  P^{\rm pre,lad,sh}_{j,K,L}
  \le
  P^{\rm pre,pair,sh}_{j,2K,L,B_{\lambda,\sigma,\beta,K}}.
\]

With \(K=128M_i\), the finite ladder replaces the residual by
\[
  P^{\rm pre,pair,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,256M_i,L_i,B_i}^{
    G\to H,{\rm rad,tan,pre,out,per,pair,short}},
\]
where
\[
  B_i=
  \left\lceil
    \frac{2048M_i\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1.
\]
No return coefficients change.  The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,pair,sh},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 254 fixed-gap prefix-pair residual

The bounded-gap prefix-pair residual is now split by the actual successor gap.
If \(P^{\rm pre,pair,sh}_{j,K,L,B}\) holds, each counted lower level \(u\)
has at least one partner \(u+h\) with \(1\le h\le B\).  Summing over the
finite set of possible gaps gives
\[
  P^{\rm pre,pair,sh}_{j,K,L,B}
  \le
  \sum_{h=1}^B P^{\rm pre,gap,sh}_{j,KB,L,h}.
\]
The factor \(B\) is independent of \(p\) for fixed ladder parameters, so it
does not affect the exponent criterion.

With \(K=256M_i\), the finite ladder replaces the residual by the finite
fixed-gap family
\[
  P^{\rm pre,gap,sh}_{i,j,h}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,256M_iB_i,L_i,h}^{
    G\to H,{\rm rad,tan,pre,out,per,gap,short}},
  \qquad 1\le h\le B_i.
\]
The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  \{P^{\rm pre,gap,sh}_{h}:1\le h\le B_i\},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 255 confined fixed-gap bridge residual

The fixed-gap prefix-pair residual has been repackaged with the deterministic
radial geometry between the lower and upper runs retained.  If a level \(u\)
is counted by a fixed-gap pair with lower witness \([a,b]\) at level \(u\)
and upper witness \([a',b']\) at level \(u+h\), then lower persistence gives
\(d(x,v_t)>u\) for \(b<t<a'\).  Since the upper run is record at level
\(u+h\), and a graph-distance path cannot cross above \(u+h\) before first
visiting \(u+h\), one also has \(d(x,v_t)<u+h\) for \(b<t<a'\).  Hence
\[
  P^{\rm pre,gap,sh}_{j,K,L,h}
  \le
  P^{\rm pre,br,sh}_{j,K,L,h},
\]
where the right-hand profile counts fixed-gap witnesses whose connector is
confined to the annulus \(u<d(x,\cdot)<u+h\).

For the adjacent gap \(h=1\), this annulus contains no integer radial level.
Thus a confined fixed-gap bridge has \(a'=b+1\): the upper record run begins
immediately after the lower run exits upward.

The finite ladder now leaves the fixed-gap residual in the stronger confined
form
\[
  P^{\rm pre,br,sh}_{i,j,h}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,256M_iB_i,L_i,h}^{
    G\to H,{\rm rad,tan,pre,out,per,bridge,short}},
  \qquad 1\le h\le B_i.
\]
The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  \{P^{\rm pre,br,sh}_{h}:1\le h\le B_i\},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 256 adjacent stacked residual

The adjacent fixed-gap case \(h=1\) has been promoted from a remark to a
separate residual.  A confined fixed-gap bridge at levels \(u,u+1\) has no
integer radial level strictly between the two endpoints, so its upper witness
\([a',b']\) must satisfy \(a'=b+1\).  This gives the deterministic reduction
\[
  P^{\rm pre,br,sh}_{j,K,L,1}
  \le
  P^{\rm pre,adj,sh}_{j,K,L},
\]
where \(P^{\rm pre,adj,sh}\) counts adjacent stacked record runs.

The finite ladder now separates the adjacent stack from the remaining
positive-width confined bridges:
\[
  \mathfrak Y_{\lambda_0}
  \;\lesssim\;
  \mathfrak Y_{\lambda_N}
  +\sum_{i,j}P^{\rm pre,adj,sh}_{i,j}
  +\sum_{i,j}\sum_{h=2}^{B_i}P^{\rm pre,br,sh}_{i,j,h}
  +\text{previous return and long-run terms}.
\]
The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,adj,sh},\quad
  \{P^{\rm pre,br,sh}_{h}:2\le h\le B_i\},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 257 two-level outward staircase residual

The adjacent stacked residual has been repackaged as a two-level outward
staircase.  If an adjacent stack has lower run \([a,b]\) at level \(u\) and
upper run \([a',b']\) at level \(u+1\), then \(a'=b+1\).  The combined
interval is therefore a single outward staircase segment
\[
  [a,b]\,,\quad b\to b+1,\quad [b+1,b']
\]
and, if both individual runs have length at most \(L\), then
\[
  b'-a=(b-a)+1+(b'-a')\le 2L+1.
\]
This gives
\[
  P^{\rm pre,adj,sh}_{j,K,L}
  \le
  P^{\rm pre,stair,sh}_{j,K,2L+1}.
\]

The finite ladder now replaces the adjacent-stack residual by
\[
  P^{\rm pre,stair,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,256M_iB_i,2L_i+1}^{
    G\to H,{\rm rad,tan,pre,out,per,stair,short}}.
\]
The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,stair,sh},\quad
  \{P^{\rm pre,br,sh}_{h}:2\le h\le B_i\},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 258 locally short staircase residual

The two-level outward staircase residual has been split according to whether
one of its component tangential runs is already long.  A staircase counted
with total cutoff \(2L+1\) but not locally short has either lower run length
\(>L\) or upper run length \(>L\).  Since both levels \(u,u+1\) lie in the
same slab \(A_{j,p}\), this gives
\[
  P^{\rm pre,stair,sh}_{j,K,2L+1}
  \le
  W_{\beta,p}\,T^{\rm long}_{j,L}
  +
  P^{\rm pre,stair,loc,sh}_{j,K,L}.
\]

After substitution into the finite ladder, the long-run coefficient increases
from \(2\) to \(3\), but this does not affect the exponent criterion.  The
live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,stair,loc,sh},\quad
  \{P^{\rm pre,br,sh}_{h}:2\le h\le B_i\},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 259 fixed-gap staircase-pair residual

The locally short staircase residual has been split by successor gaps among
the counted staircase lower levels.  If a slab contains linearly many locally
short staircase levels, the same bounded-gap pigeonhole used for ordered
ladders gives linearly many successor pairs with gap at most
\[
  B_{\lambda,\sigma,\beta,K}
  =
  \left\lceil\frac{16K\beta}{\theta_{\lambda,\sigma,\beta}}\right\rceil+1.
\]
Pigeonholing over the finite set of possible gaps then leaves a fixed-gap
staircase-pair family.

For the finite ladder, with \(B_i\) as before, put
\[
  C_i=
  \left\lceil
    \frac{4096M_iB_i\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1.
\]
The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  \{P^{\rm pre,stair,loc,gap,sh}_{h}:1\le h\le C_i\},\quad
  \{P^{\rm pre,br,sh}_{h}:2\le h\le B_i\},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 260 staircase-chain/bridge residual

The fixed-gap locally short staircase-pair residual has been split according
to the fixed gap.  If \(h=1\), the upper staircase's lower run is the same
record level-\(u+1\) run as the lower staircase's upper run, so the pair is a
three-level locally short outward staircase chain.  If \(h=2\), the upper
staircase's lower run starts immediately after the lower staircase's upper
run exits outward, giving a four-level locally short outward staircase chain.

For \(h\ge3\), the connector from the upper run of the lower staircase to the
lower run of the upper staircase is confined:
\[
  u+1<d(x,v_t)<u+h.
\]
This leaves a genuine separated staircase-bridge residual only for
\(3\le h\le C_i\).

The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,stair,loc,chain,sh}_{q=3,4},\quad
  \{P^{\rm pre,stair,loc,brdg,sh}_{h}:3\le h\le C_i\},\quad
  \{P^{\rm pre,br,sh}_{h}:2\le h\le B_i\},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 261 staircase-chain-pair residual

The successor-gap thinning has been lifted from two-level staircases to
locally short outward staircase chains of arbitrary fixed length \(\ell\).
Many chain starts in one slab have linearly many bounded successor gaps, and
then a finite fixed-gap chain-pair family.  A fixed-gap pair of
\(\ell\)-chains with \(1\le h\le\ell\) overlaps or abuts and glues into a
single chain of length \(\ell+h\).  A fixed-gap pair with \(h\ge\ell+1\)
leaves a confined chain bridge:
\[
  u+\ell-1<d(x,v_t)<u+h.
\]

In the finite ladder this is applied to the \(q=3,4\) chain terms from
Round 260.  With
\[
  D_i=
  \left\lceil
    \frac{8192M_iB_iC_i\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+5,
  \qquad
  K_i^\sharp=1024M_iB_iC_iD_i,
\]
the live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,stair,loc,longchain,sh}_{q,h}\ (q=3,4,\ 1\le h\le q),\quad
  P^{\rm pre,stair,loc,chainbr,sh}_{q,h}\ (q=3,4,\ q<h\le D_i),\quad
  \{P^{\rm pre,stair,loc,brdg,sh}_{h}:3\le h\le C_i\},\quad
  \{P^{\rm pre,br,sh}_{h}:2\le h\le B_i\},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 262 second-stage staircase-chain amplification

Round 262 applies the Round 261 arbitrary-chain split to the finite ladder's
current longer-chain residuals.  The lengths are
\[
  \ell_{q,h}=q+h,\qquad q\in\{3,4\},\quad 1\le h\le q,
\]
so \(\ell_{q,h}\in\{4,\ldots,8\}\).  With
\[
  E_i=
  \left\lceil
    \frac{16K_i^\sharp\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+9,
  \qquad
  K_i^\flat=2K_i^\sharp E_i,
\]
each such chain profile is split into longer chains of lengths
\(\ell_{q,h}+a\) for \(1\le a\le\ell_{q,h}\), and confined chain bridges for
\(\ell_{q,h}<a\le E_i\).

The live conditional endpoint is now
\[
  \mathfrak D,\quad
  \mathfrak E,\quad
  \mathfrak Y_{\lambda_N},\quad
  P^{\rm pre,stair,loc,nextchain,sh}_{q,h,a},\quad
  P^{\rm pre,stair,loc,nextchainbr,sh}_{q,h,a},\quad
  P^{\rm pre,stair,loc,chainbr,sh}_{q,h},\quad
  \{P^{\rm pre,stair,loc,brdg,sh}_{h}:3\le h\le C_i\},\quad
  \{P^{\rm pre,br,sh}_{h}:2\le h\le B_i\},\quad
  T^{\rm long},\quad
  X^{\rm spr,++},\quad
  S^{\rm ret},\quad
  X^{\rm ret}.
\]

## Round 263 packaged chain-amplification step

The three local moves used in Rounds 261--262 have been packaged as a single
one-step staircase-chain amplification corollary.  For any fixed chain length
\(\ell\ge2\), depth parameter \(K\), and cutoff
\[
  \widetilde B\ge
  B_{\lambda,\sigma,\beta,K}
  =
  \left\lceil
    \frac{16K\beta}{\theta_{\lambda,\sigma,\beta}}
  \right\rceil+1,
  \qquad
  \widetilde K=2K\widetilde B,
\]
one has
\[
  P^{\rm chain}_{j,K,L,\ell}
  \le
  \sum_{h=1}^{\ell}P^{\rm chain}_{j,\widetilde K,L,\ell+h}
  +
  \sum_{h=\ell+1}^{\widetilde B}
  P^{\rm chainbr}_{j,\widetilde K,L,\ell,h}.
\]
This is just the bounded-successor-gap, fixed-gap, and overlap/bridge split
combined.  The finite ladder endpoint is unchanged from Round 262, but the
second-stage proof now cites this packaged step directly.

## Round 264 finite-depth chain amplification

Round 264 adds a finite-depth version of the packaged chain step.  Starting
with \(K_0=K\), choose cutoffs
\[
  B_r\ge B_{\lambda,\sigma,\beta,K_{r-1}},
  \qquad
  K_r=2K_{r-1}B_r
  \qquad(1\le r\le n).
\]
The length-history sets \(\mathcal A_r(\ell)\) are defined by
\[
  \mathcal A_0(\ell)=\{(\ell)\},\qquad
  a_{r-1}+1\le a_r\le 2a_{r-1}.
\]
For every fixed \(n\), the initial chain profile is bounded by terminal
chain profiles indexed by \(\mathcal A_n(\ell)\), plus the accumulated
confined staircase-chain bridges created at each intermediate depth:
\[
  P^{\rm chain}_{j,K_0,L,\ell}
  \le
  \sum_{\mathbf a\in\mathcal A_n(\ell)}
    P^{\rm chain}_{j,K_n,L,a_n}
  +
  \sum_{r=1}^n
  \sum_{\mathbf a\in\mathcal A_{r-1}(\ell)}
  \sum_{h=a_{r-1}+1}^{B_r}
    P^{\rm chainbr}_{j,K_r,L,a_{r-1},h}.
\]
This is still a finite conditional reduction rather than a terminal estimate,
but it removes the need for more one-off chain-amplification corollaries.

## Round 265 finite-stage chain ladder

Round 265 lifts the finite-depth chain amplification into the finite far-tail
ladder.  Starting from the staircase-chain/bridge ladder, each bin has only
the two raw chain residuals \(q=3,4\).  For fixed finite depth \(n\), set
\[
  K_{i,0}^{\rm ch}=512M_iB_iC_i,\qquad
  B_{i,r}^{\rm ch}\ge
    B_{\lambda_i,\sigma_i,\beta_i,K_{i,r-1}^{\rm ch}},\qquad
  K_{i,r}^{\rm ch}=2K_{i,r-1}^{\rm ch}B_{i,r}^{\rm ch}.
\]
The new finite-stage ladder bounds \(\mathfrak Y_{\lambda_0}\) by the
terminal far tail, terminal chains indexed by \(\mathcal A_n(3)\) and
\(\mathcal A_n(4)\), all intermediate confined chain bridges created during
the \(n\) amplification steps, and the older bridge, long-run, spread-return,
and exact-return families.  For \(n=0\) this recovers the raw chain/bridge
ladder, while \(n=1\) and \(n=2\) recover the shape of the first and second
chain-amplified ladders with explicit choices of the cutoffs.

## Round 266 finite-stage radial criterion

Round 266 adds the tail and subdivision criteria corresponding to the
finite-stage ladder.  For every fixed \(n\), the old \(q=3,4\) chain-profile
hypotheses in the staircase-chain/bridge radial criterion can be replaced by
the terminal finite-stage chains
\[
  P^{\rm pre,stair,loc,nchain,sh}_{i,j,q,\mathbf a}
  \qquad(\mathbf a\in\mathcal A_n(q))
\]
and the accumulated finite-stage chain bridges
\[
  P^{\rm pre,stair,loc,nchainbr,sh}_{i,j,q,r,\mathbf a,h}
  \qquad(1\le r\le n,\ 
    \mathbf a\in\mathcal A_{r-1}(q),\
    a_{r-1}<h\le B_{i,r}^{\rm ch}).
\]
Together with the existing terminal far-tail, bridge, long-run,
spread-return, exact-return, and finite-defect bin hypotheses, this again
implies \(p_c(G)<p_{2\to2}(G)\).  The logical endpoint remains conditional,
but the paper now has a single arbitrary finite-stage version of the chain
amplification pipeline.

## Round 267 chain support and multiplicity-free amplification

Round 267 removes artificial history multiplicities from the finite chain
amplification.  The distinct chain lengths reachable after \(r\) genuine
chain-continuation steps form the interval
\[
  I_r(\ell)=\{\ell+r,\ell+r+1,\ldots,2^r\ell\}.
\]
Thus, for fixed \(n\),
\[
  P^{\rm chain}_{j,K_0,L,\ell}
  \le
  \sum_{a\in I_n(\ell)}P^{\rm chain}_{j,K_n,L,a}
  +
  \sum_{r=1}^n
  \sum_{a\in I_{r-1}(\ell)}
  \sum_{h=a+1}^{B_r}
    P^{\rm chainbr}_{j,K_r,L,a,h},
\]
with each distinct residual profile counted once.

The same round records the support cutoff
\[
  P^{\rm chain}_{j,K,L,\ell}=0
  \qquad\text{when}\qquad \ell>W_{\beta,p},
\]
because the slab \(A_{j,p}\) contains at most \(W_{\beta,p}\) integer levels.
This identifies the next real obstruction: terminal chains can be exhausted
only at depth comparable to \(W_{\beta,p}\asymp L_H\) using the current
one-step amplification, so a proof must either control the growing-depth
bridge accumulation or find an amplification whose minimum length grows
faster than linearly.

## Round 268 counting range of chain amplification

Round 268 records the precise counting range for the bounded-successor-gap
step.  The proof starts with
\[
  N_\star>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
\]
chain starts.  After discarding large successor gaps, it forces the desired
bounded successor-pair lower bound only when
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{16K}L_H>1.
\]
If \(K\ge\theta_{\lambda,\sigma,\beta}L_H/4\), the lower bound on
\(N_\star\) is compatible with a single chain start, so no successor pair can
be forced from this count alone.  This blocks the naive plan of taking
\(n\asymp W_{\beta,p}\) in the finite chain amplification: the recursion
\[
  K_r=2K_{r-1}B_r,\qquad B_r\gtrsim K_{r-1}
\]
pushes \(K_r\) outside the counting range before the terminal chain length
has been forced beyond the slab width.  The live next target is therefore a
lower-loss successor extraction or a separate bridge estimate that survives
large \(K_r\).

## Round 269 subslab ceiling for valid chain iteration

Round 269 quantifies the preceding obstruction.  Any chain-amplification
iteration that remains inside the successor-counting range must satisfy
\[
  K_{r-1}<\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H
  \qquad(1\le r\le n).
\]
Since \(B_r\ge2\), the recursive depth parameters obey
\[
  K_r=2K_{r-1}B_r\ge4K_{r-1}.
\]
Thus
\[
  4^{n-1}K_0<\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
  \qquad
  2^n\ell\le
  \ell\sqrt{\frac{\theta_{\lambda,\sigma,\beta}}{4K_0}L_H}.
\]
Every terminal length reachable before the counting proof fails is therefore
\(O(\sqrt{L_H})\), while the slab width is \(W_{\beta,p}\asymp L_H\).  Hence
the current finite chain iteration cannot reach the support cutoff
\(\ell>W_{\beta,p}\) while still justified by the bounded-successor counting
argument.  The next viable directions are now narrowed to: reduce the
\(K\)-loss in successor extraction, restart the counted-start lower bound
after large-\(K\) renormalization, or estimate accumulated chain bridges
directly.

## Round 270 ideal doubling-loss test

Round 270 tests the most optimistic version of the lower-loss successor
direction.  Suppose the fixed-gap pigeonhole loss were removed completely, so
that the only depth-parameter loss were the unavoidable halving of counted
successor starts:
\[
  K_r^{\rm id}=2^rK_0 .
\]
If such an idealized iteration remains inside the successor-counting range and
reaches the slab support cutoff, then for some \(n=n(p)\)
\[
  2^{n-1}K_0<\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
  \qquad
  2^n\ell>W_{\beta,p}.
\]
Combining these two inequalities gives
\[
  \frac{K_0W_{\beta,p}}{L_H}
  <
  \frac{\theta_{\lambda,\sigma,\beta}}8\ell,
\]
and hence, after \(p\uparrow p_c(H)\),
\[
  K_0\beta\le\frac{\theta_{\lambda,\sigma,\beta}}8\ell .
\]

Thus merely replacing the actual step \(K\mapsto2KB\) by an ideal
\(K\mapsto2K\) is not automatically enough.  For the raw finite-ladder chain
terms \(q\in\{3,4\}\), the necessary constant inequality would be
\[
  512M_iB_iC_i\,\beta_i
  \le
  \frac{\theta_{\lambda_i,\sigma_i,\beta_i}}8q,
\]
which is not produced by the present parameter reductions.  The lower-loss
route therefore has to improve the initial depth-to-length ratio, restart the
count with a fresh ratio, or bypass terminal-chain exhaustion by estimating
bridge packets directly.

## Round 271 chain bridges project to ordinary bridges

Round 271 removes one layer of residual complexity.  A confined
staircase-chain bridge of lower-chain length \(\ell\) and fixed gap
\(h\ge\ell+1\) automatically contains an ordinary confined fixed-gap bridge.
Indeed, if the lower chain starts at \(u\), take the last lower-chain run at
level
\[
  U=u+\ell-1
\]
and the first upper-chain run at level \(u+h\).  Their ordinary bridge gap is
\[
  g=(u+h)-U=h-\ell+1.
\]
All record, persistence, local-shortness, and endpoint-clearance assumptions
are inherited from the two chain witnesses, and the chain-bridge confinement
is exactly
\[
  U<d(x,v_t)<U+g
\]
between the two runs.  Since \(u\mapsto U\) is injective and the lower chain
keeps \(U\) inside the same slab,
\[
  P^{\rm stair,loc,chain,bridge}_{j,K,L,\ell,h}
  \le
  P^{\rm bridge}_{j,K,L,h-\ell+1}.
\]

Combining this projection with the multiplicity-free finite chain
amplification gives the cleaner reduction
\[
\begin{aligned}
  P^{\rm chain}_{j,K,L,\ell}
  \le&
  \sum_{a\in I_n(\ell)}P^{\rm chain}_{j,K_n,L,a}
\\
  &+
  \sum_{r=1}^n
  \sum_{g=2}^{B_r-\ell-r+2}
  P^{\rm bridge}_{j,K_r,L,g}.
\end{aligned}
\]
Thus accumulated staircase-chain bridge profiles are no longer an independent
residual family.  The remaining bridge problem is ordinary but still
large-parameter: a growing-depth chain program requires control of ordinary
confined fixed-gap bridges with stage-dependent \(K_r\) and gaps up to
\(B_r-\ell-r+2\).

## Round 272 ordinary bridge slab-start cutoff

Round 272 adds the deterministic support cutoff for the ordinary bridge
profiles left by Round 271.  A fixed-gap bridge with gap \(h\) can only be
counted at lower levels \(u\) for which both \(u\) and \(u+h\) lie in the
same slab \(A_{j,p}\).  Since the slab contains at most \(W_{\beta,p}\)
integer levels, the number of possible starts is at most
\[
  \max\{W_{\beta,p}-h,0\}.
\]
The bridge property requires more than
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
\]
counted starts, so
\[
  P^{\rm bridge}_{j,K,L,h}=0
  \qquad\text{if}\qquad
  W_{\beta,p}-h\le
  \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H.
\]
In particular, all gaps \(h\ge W_{\beta,p}\) are empty.

Combining this support cutoff with the Round 271 ordinary-bridge reduction
truncates the finite chain-amplification residual to
\[
\begin{aligned}
  P^{\rm chain}_{j,K,L,\ell}
  \le&
  \sum_{a\in I_n(\ell)}P^{\rm chain}_{j,K_n,L,a}
\\
  &+
  \sum_{r=1}^n
  \sum_{\substack{2\le g\le B_r-\ell-r+2\\
        g<W_{\beta,p}-\theta_{\lambda,\sigma,\beta}L_H/(4K_r)}}
  P^{\rm bridge}_{j,K_r,L,g}.
\end{aligned}
\]
Thus the cutoffs \(B_r\), which may be much larger than the slab width, do
not create bridge gaps beyond \(O(L_H)\).  The remaining problem is now a
uniform ordinary-bridge estimate over a p-dependent but slab-scale range of
gaps and stage-dependent \(K_r\).

## Round 273 ordinary bridges split into inward-free bridges and returns

Round 273 separates the ordinary bridge residual into the part with radial
backtracking and the part without radial backtracking.  Define an inward-free
confined fixed-gap bridge by requiring, between the end of the lower record
run and the start of the upper record run,
\[
  d(x,v_{t+1})\ge d(x,v_t)\qquad(b\le t<a').
\]
Then, for every fixed gap \(h\),
\[
  P^{\rm bridge}_{j,K,L,h}
  \le
  P^{\rm bridge,free}_{j,2K,L,h}
  +
  X^{\rm ret,spr}_{j,\,2K\max\{h-1,1\}}.
\]

The proof is a counting split.  If more than half of the counted bridge starts
admit inward-free witnesses, the first term holds.  Otherwise, each remaining
start has an inward token at some intermediate level \(w\in(u,u+h)\).  The
standard inward-token lemma gives an exterior return through \(w\).  For a
fixed return level \(w\), at most \(\max\{h-1,1\}\) lower starts \(u\) can
have \(u<w<u+h\), so enough distinct return levels remain to trigger the
spread-return profile with parameter \(2K\max\{h-1,1\}\).

Pushing this through the Round 272 bridge-truncated chain amplification gives
\[
\begin{aligned}
  P^{\rm chain}_{j,K,L,\ell}
  \le&
  \sum_{a\in I_n(\ell)}P^{\rm chain}_{j,K_n,L,a}
\\
  &+
  \sum_{r=1}^n\sum_g
  P^{\rm bridge,free}_{j,2K_r,L,g}
  +
  \sum_{r=1}^n\sum_g
  X^{\rm ret,spr}_{j,2K_r(g-1)},
\end{aligned}
\]
where
\[
  2\le g\le B_r-\ell-r+2,\qquad
  g<W_{\beta,p}-\frac{\theta_{\lambda,\sigma,\beta}}{4K_r}L_H .
\]
Thus ordinary bridges with radial backtracking are no longer a new residual;
the only genuinely new bridge object is the inward-free confined bridge.

## Round 274 inward-free bridges become chains or long runs

Round 274 removes the inward-free bridge object as an independent residual.
If an inward-free confined bridge has gap \(h\), the radial distance is
nondecreasing from the lower record run to the upper record run.  Therefore
the path visits the intermediate levels
\[
  u+1,\ldots,u+h-1
\]
in order, with consecutive \((-1,+1)\)-crossing tangential runs.  These runs
are record runs, persistence follows from monotonicity until the upper run
and from upper-run persistence afterwards, and endpoint clearance follows
from the upper endpoint clearance.  Hence either the intermediate runs are
all locally short, giving a locally short chain of length \(h+1\), or some
intermediate level has a long tangential run:
\[
  P^{\rm bridge,free}_{j,K,L,h}
  \le
  P^{\rm chain}_{j,K,L,h+1}
  +
  W_{\beta,p}T^{\rm long}_{j,L}.
\]

Substituting this into the Round 273 finite chain amplification gives a
bridge-free finite reduction:
\[
\begin{aligned}
  P^{\rm chain}_{j,K,L,\ell}
  \le&
  \sum_{a\in I_n(\ell)}P^{\rm chain}_{j,K_n,L,a}
\\
  &+
  \sum_{r=1}^n\sum_g P^{\rm chain}_{j,2K_r,L,g+1}
  +
  \sum_{r=1}^n\sum_g X^{\rm ret,spr}_{j,2K_r(g-1)}
  +
  nW_{\beta,p}^2T^{\rm long}_{j,L},
\end{aligned}
\]
where the \(g\)-range is still
\[
  2\le g\le B_r-\ell-r+2,\qquad
  g<W_{\beta,p}-\frac{\theta_{\lambda,\sigma,\beta}}{4K_r}L_H.
\]
Thus the direct bridge route has been converted to a chain-and-return route.
The remaining obstruction is not a bridge estimate; it is now uniform control
of the p-dependent chain profiles \(P^{\rm chain}_{j,2K_r,L,g+1}\), with
lengths up to the slab scale, plus the existing spread-return estimates.

## Round 275 start-count truncation for long chains

Round 275 adds the chain analogue of the fixed-gap bridge start-count cutoff.
A locally short staircase chain of length \(\ell\) contained in one heavy slab
must start at a level \(u\) such that
\[
  u,u+1,\ldots,u+\ell-1
\]
all lie in the slab.  Therefore there are at most
\(\max\{W_{\beta,p}-\ell+1,0\}\) possible starts.  Since the profile asks for
strictly more than
\(\theta_{\lambda,\sigma,\beta}L_H/(4K)\) counted starts, the chain profile
vanishes whenever
\[
  W_{\beta,p}-\ell+1\le
  \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H.
\]

Applying this to the terminal sum in the Round 274 bridge-free finite
reduction removes all terminal lengths in the top
\(\theta_{\lambda,\sigma,\beta}L_H/(4K_n)\) part of the slab:
\[
  a<
  W_{\beta,p}+1-\frac{\theta_{\lambda,\sigma,\beta}}{4K_n}L_H.
\]
The bridge-derived chain residuals remain in the already truncated gap range
\[
  2\le g\le B_r-\ell-r+2,\qquad
  g<W_{\beta,p}-\frac{\theta_{\lambda,\sigma,\beta}}{4K_r}L_H.
\]
This improves the bookkeeping of the bridge-free reduction but does not yet
close the iteration, because one still needs uniform control of a
p-dependent family of chain profiles over a slab-scale range of lengths.

## Round 276 residual-width successor gaps

Round 276 sharpens the successor-gap count for chain profiles.  A chain of
length \(\ell\) can start only at levels whose next \(\ell-1\) successors
remain in the same slab, so the available start width is
\[
  R_{\ell,p}=\max\{W_{\beta,p}-\ell+1,0\}
\]
rather than \(W_{\beta,p}\).  Repeating the successor-gap count with this
width gives the residual cutoff
\[
  B^{\rm res}_{K,\ell,p}
  =
  \left\lceil
    \frac{16K R_{\ell,p}}{\theta_{\lambda,\sigma,\beta}L_H}
  \right\rceil+1.
\]
Provided the usual counting range
\(\theta_{\lambda,\sigma,\beta}L_H/(16K)>1\) holds,
\[
  P^{\rm chain}_{j,K,L,\ell}
  \le
  P^{\rm chain,pair}_{j,2K,L,\ell,B^{\rm res}_{K,\ell,p}} .
\]

In the near-top regime \(R_{\ell,p}\le C L_H/K\), this cutoff is bounded by
the p-independent constant
\[
  B_C=
  \left\lceil
    \frac{16C}{\theta_{\lambda,\sigma,\beta}}
  \right\rceil+1.
\]
Thus chain amplification becomes cheaper once the length is already within
\(O(L_H/K)\) of exhausting the slab.  The obstruction is now more precise:
the current argument still lacks a way to drive a fixed initial chain length
into that near-top residual regime without first accumulating the old
rapidly growing \(K\)-loss.

## Round 277 residual-width one-step amplification

Round 277 propagates the residual-width successor cutoff through the
fixed-gap and split steps.  With
\[
  B^{\rm res}_{K,\ell,p}
  =
  \left\lceil
    \frac{16K R_{\ell,p}}{\theta_{\lambda,\sigma,\beta}L_H}
  \right\rceil+1,
\]
the residual successor extraction gives a bounded-gap chain-pair profile with
parameter \(2K\) and cutoff \(B^{\rm res}_{K,\ell,p}\).  The fixed-gap
pigeonhole changes the depth parameter to
\[
  K^{\rm res}_{K,\ell,p}=2K B^{\rm res}_{K,\ell,p},
\]
and the fixed-gap split gives a one-step bound by longer chain profiles
\(P^{\rm chain}_{j,K^{\rm res}_{K,\ell,p},L,\ell+h}\) for
\(1\le h\le\ell\), plus confined chain-bridge profiles for
\(\ell+1\le h\le B^{\rm res}_{K,\ell,p}\).

In the near-top regime \(R_{\ell,p}\le C L_H/K\), this becomes a genuinely
bounded-cost one-step amplification: the cutoff is \(B_C\), independent of
\(p\), and the new depth parameter is \(K_C=2KB_C\).  This is a sharper local
tool than the old slab-width step, but it still leaves the same strategic
gap: an argument beginning from fixed small chain lengths must first reach
the near-top residual-width regime without exhausting the counting range.

## Round 278 bridge-free residual descent

Round 278 isolates the portion of the residual-width one-step amplification
where no confined chain-bridge profiles are produced.  If
\[
  B^{\rm res}_{K,\ell,p}\le \ell,
\]
then the bridge sum in the residual-width one-step bound is absent:
\[
  P^{\rm chain}_{j,K,L,\ell}
  \le
  \sum_{h=1}^{B^{\rm res}_{K,\ell,p}}
  P^{\rm chain}_{j,K^{\rm res}_{K,\ell,p},L,\ell+h}.
\]
Each surviving chain term has strictly smaller residual start width:
\[
  R_{\ell+h,p}=\max\{R_{\ell,p}-h,0\}\le\max\{R_{\ell,p}-1,0\}.
\]

The simple sufficient condition
\[
  R_{\ell,p}\le
  \frac{\theta_{\lambda,\sigma,\beta}(\ell-1)}{16K}L_H
\]
ensures \(B^{\rm res}_{K,\ell,p}\le\ell\).  In the near-top form
\(R_{\ell,p}\le C L_H/K\), it is enough that
\[
  C\le \frac{\theta_{\lambda,\sigma,\beta}(\ell-1)}{16}.
\]
Thus the manuscript now has a bridge-free residual descent mechanism once a
chain is sufficiently close to the top of the slab.  The strategic gap is
unchanged: one still needs a mechanism that reaches this bridge-free descent
regime from the fixed small chain lengths produced earlier in the reduction.

## Round 279 finite bridge-free residual descent iteration

Round 279 turns the bridge-free residual descent into an explicit finite
iteration.  Starting with \((K,\ell)\), define a descent tree by assigning to
each node \(\mathbf h\) current parameters \(K(\mathbf h)\) and
\(\ell(\mathbf h)\), residual cutoff
\[
  B(\mathbf h)=B^{\rm res}_{K(\mathbf h),\ell(\mathbf h),p},
\]
and children \(\mathbf h\frown h\), \(1\le h\le B(\mathbf h)\), with
\[
  \ell(\mathbf h\frown h)=\ell(\mathbf h)+h,\qquad
  K(\mathbf h\frown h)=2K(\mathbf h)B(\mathbf h).
\]
If every node up to depth \(m-1\) remains in the counting range and in the
bridge-free range,
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{16K(\mathbf h)}L_H>1,
  \qquad
  B(\mathbf h)\le\ell(\mathbf h),
\]
then
\[
  P^{\rm chain}_{j,K,L,\ell}
  \le
  \sum_{\mathbf h\in\mathcal H_m}
  P^{\rm chain}_{j,K(\mathbf h),L,\ell(\mathbf h)}.
\]
At every terminal node,
\[
  R_{\ell(\mathbf h),p}\le \max\{R_{\ell,p}-m,0\}.
\]
Consequently, persistence of these hypotheses through
\(m\ge R_{\ell,p}\) steps would force the initial chain profile to vanish.

This is useful because it converts the near-top part of the program into a
precise conditional exhaustion criterion.  It also makes the remaining gap
sharper: one must either prove persistence of the bridge-free/counting
hypotheses until residual exhaustion, or find a different way to enter this
descent tree with sufficiently small residual width and controlled \(K\).

## Round 280 logarithmic obstruction to bridge-free residual exhaustion

Round 280 records the cost of the conditional bridge-free descent tree.  If
the hypotheses of the finite bridge-free residual descent iteration persist
until the initial residual width \(R_{\ell,p}\) is exhausted, then the
all-ones branch remains alive down to depth \(R_{\ell,p}-1\).  Along this
branch, residual width is still positive before that depth, so every residual
cutoff is at least \(2\), and hence
\[
  K(\mathbf 1_{r+1})\ge4K(\mathbf 1_r).
\]
The counting-range hypothesis at depth \(R_{\ell,p}-1\) therefore forces
\[
  4^{R_{\ell,p}-1}K
  <
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H.
\]
Equivalently,
\[
  R_{\ell,p}
  <
  1+
  \log_4\!\left(
    \frac{\theta_{\lambda,\sigma,\beta}L_H}{16K}
  \right).
\]

Thus the current bridge-free descent recursion only certifies exhaustion
from logarithmic residual width.  The near-top program is now split into a
clear dichotomy: either find a route that enters the bridge-free descent tree
with \(R_{\ell,p}=O(\log L_H)\) and controlled \(K\), or replace the
\(K\mapsto 2KB\) growth in the descent step.

## Round 281 first obstruction on the unit residual branch

Round 281 packages the contrapositive of the logarithmic obstruction as a
first-obstruction alternative.  Put \(R=R_{\ell,p}\), and follow the
all-ones branch by setting
\[
  \ell_r=\ell+r,\qquad K_0=K,\qquad
  B_r=B^{\rm res}_{K_r,\ell_r,p},\qquad
  K_{r+1}=2K_rB_r .
\]
If the entry residual width is outside the logarithmic regime,
\[
  4^{R-1}K
  \ge
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
\]
then the branch has a first index \(r_*<R\) at which either
\[
  K_{r_*}\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H
\]
or
\[
  B_{r_*}>\ell_{r_*}.
\]
Before this first index, both the counting-range condition and the
bridge-free condition hold along the unit branch, so the bridge-free descent
is genuinely valid there.

If the first obstruction is not counting saturation, then
\(B_{r_*}>\ell_{r_*}\) while the counting range still holds, so the
residual-width one-step amplification produces a non-empty confined
chain-bridge sum at \((K_{r_*},\ell_{r_*})\).  This is a more actionable form
of the near-top obstruction: wide residual entries cannot be exhausted by
the present bridge-free recursion, but they must either create a bridge
packet or reach a node where the counted-start lower bound itself has become
too weak.

## Round 282 first bridge-active obstruction becomes ordinary bridges

Round 282 refines the bridge-active side of the first-obstruction
alternative.  If the first obstruction index \(r_*\) still satisfies the
counting range
\[
  K_{r_*}<
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
\]
then it must satisfy \(B_{r_*}>\ell_{r_*}\).  Applying the residual-width
one-step amplification and then projecting confined staircase-chain bridges
to ordinary bridges gives
\[
\begin{aligned}
  P^{\rm chain}_{j,K_{r_*},L,\ell_{r_*}}
  \le&
  \sum_{h=1}^{\ell_{r_*}}
  P^{\rm chain}_{j,K_{r_*+1},L,\ell_{r_*}+h}
\\
  &+
  \sum_{g=2}^{B_{r_*}-\ell_{r_*}+1}
  P^{\rm bridge}_{j,K_{r_*+1},L,g}.
\end{aligned}
\]
Here the bridge gap is \(g=h-\ell_{r_*}+1\).  Thus the bridge-active first
obstruction is not a new type of profile; it lands in the ordinary
confined-bridge families already present in the finite chain reduction.

The same condition gives the scale lower bound
\[
  R_{\ell_{r_*},p}>
  \frac{\theta_{\lambda,\sigma,\beta}(\ell_{r_*}-1)}
       {16K_{r_*}}L_H.
\]
So the first bridge packet appears precisely while the residual start width
is still too large for bridge-free descent.  The remaining branch to attack
is now sharper: either control the ordinary bridge packet at this first
obstruction node, or handle the alternative in which \(K_{r_*}\) has already
saturated the counted-start range.

## Round 283 counting saturation has a last large bridge-free step

Round 283 refines the remaining first-obstruction branch.  Let
\[
  T_{\lambda,\sigma,\beta,p}
  =
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H.
\]
If the first obstruction index is counting-saturating,
\[
  K_{r_*}\ge T_{\lambda,\sigma,\beta,p},
\]
then either \(r_*=0\), so the initial chain profile is already outside the
successor-counting range, or there is a predecessor \(r_0=r_*-1\) at which
both descent hypotheses still hold:
\[
  K_{r_0}<T_{\lambda,\sigma,\beta,p},
  \qquad
  B_{r_0}\le\ell_{r_0}.
\]
In the non-initial case, the predecessor step is bridge-free:
\[
  P^{\rm chain}_{j,K_{r_0},L,\ell_{r_0}}
  \le
  \sum_{h=1}^{B_{r_0}}
  P^{\rm chain}_{j,K_{r_*},L,\ell_{r_0}+h}.
\]
Since \(K_{r_*}=2K_{r_0}B_{r_0}\), counting saturation forces
\[
  B_{r_0}
  \ge
  \frac{\theta_{\lambda,\sigma,\beta}}{32K_{r_0}}L_H.
\]
Thus the counted-start branch is also now localized: before the proof loses
the successor-counting range, it passes through a bridge-free step with a
large successor window and therefore contains at least one child whose
residual width drops by \(L_H/K_{r_0}\)-scale.

Together with Round 282, the first-obstruction dichotomy is now fully
resolved into standard local alternatives: either an ordinary confined
bridge packet appears, or the final valid bridge-free step before counting
saturation has a large successor window.  The remaining work is to exploit
one of these alternatives uniformly in the near-critical limit.

## Round 284 wide residual first-obstruction normal form

Round 284 packages Rounds 281--283 into a single normal form.  For a wide
residual entry,
\[
  R=R_{\ell,p}\ge1,\qquad
  4^{R-1}K\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
\]
the unit residual branch satisfies one of three alternatives.

First, the entry may already be outside the counting range:
\[
  K\ge \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H.
\]
Second, there may be a bridge-active index \(r<R\), where
\[
  K_r<\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,\qquad B_r>\ell_r,
\]
and the corresponding chain profile is bounded by longer chain profiles plus
ordinary confined bridge profiles.  Third, there may be a last valid
large-window bridge-free step \(r<R-1\), where
\[
  K_r<\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,\qquad
  B_r\le\ell_r,\qquad
  K_{r+1}\ge\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
\]
and
\[
  B_r\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{32K_r}L_H.
\]

This is now the standard local target for the near-top program.  Wide
residual entries no longer leave an amorphous failure mode: they reduce to
initial counting loss, an ordinary bridge packet, or a final bridge-free
large-window step before counting loss.

## Round 285 source refresh and next local target

Round 285 refreshed the external status and found no announced general
solution of the Benjamini--Schramm non-uniqueness conjecture in the full
nonamenable quasi-transitive setting, nor of the stronger project target
\(p_c(G)<p_{2\to2}(G)\).  The current source picture is still special-case
and adjacent progress, so the internal proof search remains aligned with an
open target.

The Round 284 normal form now gives the next local objective.  For a wide
residual entry not already lost to initial counting saturation, it is enough
to exploit one of two standard alternatives:

\[
\text{ordinary confined bridge packet}
\qquad\text{or}\qquad
\text{last bridge-free large-window step.}
\]

The bridge-packet branch should be compared against the existing ordinary
confined-bridge reductions.  The large-window branch should be tested for a
multi-child residual drop: since
\[
  B_r\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{32K_r}L_H,
\]
the last valid bridge-free step includes a child whose residual width drops
by \(L_H/K_r\)-scale before counting is lost.  The remaining question is
whether this drop can be made useful without paying the full \(K\mapsto2KB\)
loss again.

## Round 286 bridge-packet branch truncates to returns

Round 286 pushes the ordinary bridge-packet branch of the normal form through
the existing ordinary-bridge machinery.  If the normal form lands at an
ordinary bridge packet indexed by \(r\), define
\[
  \mathcal G_r
  =
  \left\{
    2\le g\le B_r-\ell_r+1:
    g<
    W_{\beta,p}
    -
    \frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H
  \right\}.
\]
The large-fixed-gap lemma deletes all ordinary bridge gaps outside
\(\mathcal G_r\).  For the remaining gaps, the confined bridge
inward-free-or-return split gives
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le&
  \sum_{h=1}^{\ell_r}
  P^{\rm chain}_{j,K_{r+1},L,\ell_r+h}
\\
  &+
  \sum_{g\in\mathcal G_r}
  P^{\rm bridge,free}_{j,2K_{r+1},L,g}
  +
  \sum_{g\in\mathcal G_r}
  X^{\rm ret,spr}_{j,2K_{r+1}(g-1)}.
\end{aligned}
\]

Thus the bridge side of the normal form no longer needs a separate
chain-bridge analysis: after projection it reduces to the same inward-free
bridge and spread-return profiles already appearing in the finite
chain-amplification ladder.  The remaining independent branch is the
large-window bridge-free step before counting saturation.

## Round 287 large-window branch has subexponential child cost

Round 287 packages the remaining large-window branch of the normal form as a
subexponential union.  If the last valid large-window step occurs at index
\(r\), then
\[
  B_r\le \ell_r<W_{\beta,p}.
\]
Thus the bridge-free child sum has at most \(W_{\beta,p}\) terms, and
\[
  \frac{\log_{D_H}W_{\beta,p}}{L_H}\to0.
\]
Consequently, a uniform logarithmic exponent bound on the child profiles
\[
  P^{\rm chain}_{j,K_{r+1},L,\ell_r+h},
  \qquad 1\le h\le B_r,
\]
passes to the parent
\[
  P^{\rm chain}_{j,K_r,L,\ell_r}
\]
without exponent loss.

The largest child in the same subexponential family still satisfies
\[
  R_{\ell_r+B_r,p}
  \le
  \max\left\{
    R_{\ell_r,p}
    -
    \frac{\theta_{\lambda,\sigma,\beta}}{32K_r}L_H,
    0
  \right\}.
\]
So the large-window branch is reduced to proving uniform child bounds across
a subexponential family while preserving at least one substantial residual
drop.

## Round 288 large-window children reduce to finite-start profiles

Round 288 sharpens the child target in the large-window branch.  Once the
normal form reaches the last valid large-window step, the child parameter has
already saturated the counting range:
\[
  K_{r+1}\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H .
\]
Thus the ordinary chain-start threshold in each child satisfies
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H\le4 .
\]
Defining
\[
  q_{r,p}
  =
  \left\lfloor
    \frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H
  \right\rfloor+1
\]
gives \(1\le q_{r,p}\le5\).  Every child ordinary chain profile is therefore
contained in the corresponding few-start chain profile, and the whole parent
branch satisfies
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le
  \sum_{h=1}^{B_r}\sum_{q=1}^{5}
  P^{\rm chain,qstart}_{j,K_{r+1},L,\ell_r+h,q}.
\end{aligned}
\]
Since \(B_r<W_{\beta,p}\), this adds only \(5W_{\beta,p}\) summands and hence
no logarithmic exponent cost.

The wide-residual normal form is now reduced to three sharper local targets:
initial counting loss, bridge packets truncated to inward-free bridge and
spread-return profiles, or a subexponential family of bounded finite-start
chain profiles.  The next useful step is to exploit the \(q\le5\) structure,
rather than trying to restart the successor-counting amplification after
\(K\) has crossed the counting threshold.

## Round 289 finite-start chains localize to exact starts

Round 289 removes the remaining slab-level start choice from the large-window
finite-start branch.  The new exact-start chain profile fixes a start level
\(u\) and then takes the same type of supremum over
\(u\in A_{j,p}\cap\mathbb N\) used by the exact-level return profiles.

For every \(q\ge1\),
\[
  P^{\rm chain,qstart}_{j,K,L,\ell,q}
  \le
  W_{\beta,p}\,
  P^{\rm chain,exact}_{j,K,L,\ell}.
\]
Indeed, the few-start property implies that at least one admissible start
exists, and there are at most \(W_{\beta,p}\) possible start levels in the
slab.

Combining this with Round 288 gives the large-window exact-start reduction
\[
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le
  5W_{\beta,p}
  \sum_{h=1}^{B_r}
  P^{\rm chain,exact}_{j,K_{r+1},L,\ell_r+h}.
\]
Since \(B_r<W_{\beta,p}\), the fully expanded union cost is
\[
  \log_{D_H}(5W_{\beta,p}^2)=o(L_H).
\]
Thus the large-window branch no longer contains an uncontrolled slab-level
choice of chain starts.  It reduces to uniform exponent bounds for
exact-start chain profiles over a subexponential family of child lengths,
with the same largest-child residual drop as before.

## Round 290 residual exact-start localization cost

Round 290 sharpens the exact-start localization loss.  The few-start to
exact-start localization does not need the full slab width \(W_{\beta,p}\).
For a chain of length \(\ell\), the start must fit entirely inside the slab,
so the number of possible starts is only
\[
  R_{\ell,p}=\max\{W_{\beta,p}-\ell+1,0\}.
\]
Thus, for every \(q\ge1\),
\[
  P^{\rm chain,qstart}_{j,K,L,\ell,q}
  \le
  R_{\ell,p}\,
  P^{\rm chain,exact}_{j,K,L,\ell}.
\]

Propagating this through the large-window branch gives
\[
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le
  \sum_{h=1}^{B_r}
  5R_{\ell_r+h,p}\,
  P^{\rm chain,exact}_{j,K_{r+1},L,\ell_r+h},
\]
where
\[
  R_{\ell_r+h,p}=\max\{R_{\ell_r,p}-h,0\}.
\]
The total residual start cost satisfies
\[
  5\sum_{h=1}^{B_r}R_{\ell_r+h,p}\le5W_{\beta,p}^2,
\]
and hence remains subexponential.  The important gain is qualitative: the
cost now follows the residual widths of the child lengths, so the largest
child's \(L_H/K_r\)-scale residual drop is visible in the exact-start
bookkeeping rather than hidden behind a uniform \(W_{\beta,p}\) factor.

## Round 291 low-residual tail in the exact-start branch

Round 291 splits the residual-weighted exact-start branch into a prefix and a
tail.  Put
\[
  t_r=\left\lceil\frac{B_r}{2}\right\rceil .
\]
The Round 290 bound becomes
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le&
  5\sum_{h=1}^{t_r-1}
  R_{\ell_r+h,p}\,
  P^{\rm chain,exact}_{j,K_{r+1},L,\ell_r+h}
\\
  &+
  5\max\{R_{\ell_r,p}-t_r,0\}
  \sum_{h=t_r}^{B_r}
  P^{\rm chain,exact}_{j,K_{r+1},L,\ell_r+h}.
\end{aligned}
\]
The tail packet has a uniform residual-width drop.  Since the large-window
branch gives
\[
  B_r\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{32K_r}L_H,
\]
we have \(t_r\ge\theta_{\lambda,\sigma,\beta}L_H/(64K_r)\), and every child
in the tail has residual width at most
\[
  \max\left\{
    R_{\ell_r,p}
    -
    \frac{\theta_{\lambda,\sigma,\beta}}{64K_r}L_H,
    0
  \right\}.
\]

This separates the remaining large-window exact-start target into an
explicit prefix packet and a lower-residual tail packet.  The expanded
number of weighted exact-start profiles remains bounded by \(5W_{\beta,p}^2\),
so the split does not add exponent cost.

## Round 292 dyadic residual layers for exact-start children

Round 292 refines the half-tail split into a dyadic layer decomposition.  Let
\[
  M_r=\max\{1,\lceil\log_2 B_r\rceil\},\qquad
  s_{r,0}=B_r+1,\qquad
  s_{r,m}=\left\lceil\frac{B_r}{2^m}\right\rceil .
\]
Then \(s_{r,M_r}=1\), and the intervals
\[
  I_{r,m}=\{s_{r,m},\ldots,s_{r,m-1}-1\}
\]
partition \(\{1,\ldots,B_r\}\).  The exact-start branch satisfies
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le
  5\sum_{m=1}^{M_r}
  \max\{R_{\ell_r,p}-s_{r,m},0\}
  \sum_{h\in I_{r,m}}
  P^{\rm chain,exact}_{j,K_{r+1},L,\ell_r+h}.
\end{aligned}
\]

Since \(s_{r,m}\ge B_r/2^m\) and
\[
  B_r\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{32K_r}L_H,
\]
every child in layer \(m\) has residual width at most
\[
  \max\left\{
    R_{\ell_r,p}
    -
    \frac{\theta_{\lambda,\sigma,\beta}}{2^{m+5}K_r}L_H,
    0
  \right\}.
\]
The total expanded cost is still bounded by \(5W_{\beta,p}^2\).  Thus the
remaining exact-start target is now stratified by explicit residual-drop
scales, which is a better form for any future induction or layer-wise
profile estimate.

## Round 293 exact-start chains collapse to record spread except short children

Round 293 adds a direct deterministic escape from the exact-start branch.
An exact-start chain of length \(\ell\) supplies crossing runs at
\(\ell\) distinct consecutive slab levels.  Therefore, whenever
\[
  \ell>
  \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H ,
\]
the exact-start profile is bounded by the existing prefix-record
outward-spread profile:
\[
  P^{\rm chain,exact}_{j,K,L,\ell}
  \le
  P^{\rm pre,out,rec}_{j,K,L}.
\]

In the large-window branch, the child parameter satisfies
\[
  K_{r+1}\ge \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H .
\]
Thus every exact-start child with total length at least \(5\) is already a
prefix-record outward-spread event.  If
\[
  \mathcal S_r=\{h\in\{1,\ldots,B_r\}:\ell_r+h\le4\},
\]
then
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le&
  5\sum_{h\in\mathcal S_r}
  R_{\ell_r+h,p}\,
  P^{\rm chain,exact}_{j,K_{r+1},L,\ell_r+h}
\\
  &+
  5\left(\sum_{h=1}^{B_r}R_{\ell_r+h,p}\right)
  P^{\rm pre,out,rec}_{j,K_{r+1},L}.
\end{aligned}
\]
Here \(\mathcal S_r\subseteq\{1,\ldots,4-\ell_r\}\), so
\(|\mathcal S_r|\le2\), and the set is empty when \(\ell_r\ge4\).  The
record-spread coefficient is at most \(5W_{\beta,p}^2\), and the short
exact-start coefficient is at most \(10W_{\beta,p}\), both subexponential on
the \(L_H\) scale.

This means the exact-start branch no longer contains an uncontrolled family
of child lengths: all length-at-least-five children return to the earlier
prefix-record reduction tree, and only total lengths \(3\) and \(4\) remain
as genuinely new finite exact-start exceptions.

## Round 294 threshold-tight short exact-start exceptions

Round 294 replaces the coarse short-exception set from Round 293 by the
actual counting-threshold exception set
\[
  \mathcal E_r
  =
  \left\{
    h\in\{1,\ldots,B_r\}:
    \ell_r+h\le
    \frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H
  \right\}.
\]
For every \(h\notin\mathcal E_r\), the exact-start child length is already
larger than the prefix-record threshold at parameter \(K_{r+1}\), so the
child is absorbed by \(P^{\rm pre,out,rec}_{j,K_{r+1},L}\).  Thus
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le&
  5\sum_{h\in\mathcal E_r}
  R_{\ell_r+h,p}\,
  P^{\rm chain,exact}_{j,K_{r+1},L,\ell_r+h}
\\
  &+
  5\left(\sum_{h=1}^{B_r}R_{\ell_r+h,p}\right)
  P^{\rm pre,out,rec}_{j,K_{r+1},L}.
\end{aligned}
\]

Since the large-window branch has
\[
  K_{r+1}\ge\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
\]
the new exception set satisfies \(\mathcal E_r\subseteq\mathcal S_r\) and
hence \(|\mathcal E_r|\le2\).  More sharply,
\[
  \mathcal E_r=\varnothing
  \qquad\text{if}\qquad
  K_{r+1}>
  \frac{\theta_{\lambda,\sigma,\beta}}{12}L_H .
\]
If a length-four exception occurs, then the upper and lower inequalities
force exact saturation
\[
  K_{r+1}=\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H .
\]
Thus all remaining exact-start exceptions are confined to the narrow
saturated window
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H
  \le K_{r+1}
  \le
  \frac{\theta_{\lambda,\sigma,\beta}}{12}L_H .
\]

The exceptional coefficient is still at most \(10W_{\beta,p}\), and the
record-spread coefficient is at most \(5W_{\beta,p}^2\).  The large-window
branch is therefore reduced to the earlier record-spread branch except for
at most two threshold-tight exact-start children.

## Round 295 surplus-start form of the threshold exceptions

Round 295 observes that the Round 294 exact-start exception form has already
spent more information than necessary.  Before localizing to exact starts,
the large-window child has a \(q_{r,p}\)-start condition with
\[
  A_r=\frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H,
  \qquad
  q_{r,p}=\lfloor A_r\rfloor+1 .
\]
If a few-start child has length \(\ell>A_r\), then one of its admissible
starts already gives more than \(A_r\) consecutive record levels, and hence
the child is absorbed by the prefix-record outward-spread profile.

Thus, with
\[
  \mathcal E_r=\{h\in\{1,\ldots,B_r\}:\ell_r+h\le A_r\},
\]
the large-window branch has the stronger form
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le&
  \sum_{h\in\mathcal E_r}
  P^{\rm chain,qstart}_{j,K_{r+1},L,\ell_r+h,q_{r,p}}
\\
  &+
  B_r P^{\rm pre,out,rec}_{j,K_{r+1},L}.
\end{aligned}
\]
For every exceptional \(h\),
\[
  q_{r,p}>\ell_r+h,\qquad q_{r,p}\in\{4,5\}.
\]
Consequently the only remaining exceptional few-start types are
\[
  (\ell_r+h,q_{r,p})\in\{(3,4),(3,5),(4,5)\}.
\]

This improves the bookkeeping in two ways.  First, the exceptional profiles
retain surplus-start multiplicity rather than collapsing to one exact start.
Second, the record-spread coefficient is \(B_r<W_{\beta,p}\), rather than
the residual-localization coefficient \(O(W_{\beta,p}^2)\).  The remaining
large-window novelty is therefore a finite surplus-start obstruction, not an
unstructured exact-start family.

## Round 296 large-window few-start branch collapses to record spread

Round 296 removes the finite surplus-start obstruction from Round 295.  The
key point is simpler than the chain-length threshold: a \(q\)-start chain
profile already has \(q\) distinct admissible start levels, and the first run
at each such start is a prefix-record outward crossing level.  Hence, if
\[
  q>
  \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H ,
\]
then
\[
  P^{\rm chain,qstart}_{j,K,L,\ell,q}
  \le
  P^{\rm pre,out,rec}_{j,K,L}.
\]

In the large-window branch
\[
  q_{r,p}
  =
  \left\lfloor
    \frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H
  \right\rfloor+1
\]
is, by construction, strictly larger than the prefix-record threshold at
parameter \(K_{r+1}\).  Substituting the few-start child bound before any
exact-start localization gives
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  &\le
  \sum_{h=1}^{B_r}
  P^{\rm chain,qstart}_{j,K_{r+1},L,\ell_r+h,q_{r,p}}
\\
  &\le
  B_r P^{\rm pre,out,rec}_{j,K_{r+1},L}.
\end{aligned}
\]
Since \(B_r<W_{\beta,p}\), this coefficient is subexponential on the
\(L_H\) scale.

Thus the large-window branch no longer produces any new chain-type residual.
It returns to the existing prefix-record reduction tree, with only a single
\(W_{\beta,p}\)-scale multiplicative loss.

## Round 297 wide residual normal form with chain branches absorbed

Round 297 applies the same start-level observation to ordinary locally short
staircase-chain profiles.  A chain profile already has more than
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
\]
admissible starts, and the first run at each admissible start is a
prefix-record outward crossing run.  Therefore
\[
  P^{\rm chain}_{j,K,L,\ell}
  \le
  P^{\rm pre,out,rec}_{j,K,L}.
\]

This absorbs the chain-child sums left in the bridge side of the
wide-residual normal form.  Combining Round 286 with the new chain-to-record
bound gives the reduced bridge packet
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le&
  \ell_r P^{\rm pre,out,rec}_{j,K_{r+1},L}
\\
  &+
  \sum_{g\in\mathcal G_r}
  P^{\rm bridge,free}_{j,2K_{r+1},L,g}
  +
  \sum_{g\in\mathcal G_r}
  X^{\rm ret,spr}_{j,2K_{r+1}(g-1)}.
\end{aligned}
\]
Combining Round 296 with the large-window side gives
\[
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le
  B_r P^{\rm pre,out,rec}_{j,K_{r+1},L}.
\]

The coefficients and index sets are subexponential:
\[
  \ell_r\le W_{\beta,p},\qquad
  B_r<W_{\beta,p},\qquad
  |\mathcal G_r|\le W_{\beta,p}.
\]
Thus, outside initial counting saturation, the wide-residual first-obstruction
normal form now reduces to the already existing prefix-record outward-spread,
inward-free bridge, and spread-return profile families.

## Round 298 chain-absorbed downstream criteria

Round 298 propagates the Round 297 chain-to-record observation into the
finite far-tail and radial criteria.  The old staircase-chain/bridge finite
ladder contained two raw chain terms
\[
  P^{\rm pre,stair,loc,chain,sh}_{i,j,3}
  +
  P^{\rm pre,stair,loc,chain,sh}_{i,j,4}
\]
at depth \(K=512M_iB_iC_i\).  Since every locally short staircase-chain
profile is already a prefix-record outward-spread profile at the same depth,
these two terms are now replaced by
\[
  2P^{\rm pre,rec,ch}_{i,j},
  \qquad
  P^{\rm pre,rec,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,512M_iB_iC_i,L_i}.
\]

The resulting finite ladder reduces the initial far tail to the terminal far
tail, the chain-depth prefix-record profile, confined locally short
staircase-bridge profiles, ordinary confined bridge profiles, long-run
profiles, spread-return profiles, and ordinary exact-level return profiles.
The matching radial-tail and subdivision criteria have also been added, so
the downstream statement no longer needs a separate exponent hypothesis on
raw locally short staircase-chain profiles with \(q=3,4\).  The remaining
new family is prefix-record at a larger finite depth parameter; this is an
older profile type and can be attacked by the existing prefix-record
splitting mechanisms in subsequent rounds.

## Round 299 chain-depth prefix-record becomes persistent-or-returning

Round 299 applies the existing short prefix-record split to the new
chain-depth profile from Round 298.  With
\[
  K^{\rm ch}_i=512M_iB_iC_i,
\]
the profile
\[
  P^{\rm pre,rec,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,K^{\rm ch}_i,L_i}
\]
satisfies
\[
  P^{\rm pre,rec,ch}_{i,j}
  \le
  P^{\rm pre,per,ch}_{i,j}
  +
  R^{\rm spr,ch}_{i,j}
  +
  R^{\rm spr,ch}_{i,j+1},
\]
where
\[
  P^{\rm pre,per,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,2K^{\rm ch}_i,L_i},
  \qquad
  R^{\rm spr,ch}_{i,j}
  =
  X^{\rm ret,spr}_{j,4K^{\rm ch}_i}.
\]

Substituting this into the Round 298 chain-absorbed finite ladder replaces
the coefficient-\(2\) chain-depth prefix-record term by a
coefficient-\(2\) chain-depth persistent-prefix term and two coefficient-\(2\)
chain-depth spread-return terms.  The matching radial-tail and subdivision
criteria are now stated explicitly.  Thus the downstream hypotheses no longer
need the chain-depth prefix-record family itself; the remaining new
non-bridge obstruction is persistent prefix structure at depth
\(1024M_iB_iC_i\), plus spread-return profiles at threshold
\(2048M_iB_iC_i\).

## Round 300 chain-depth persistent prefixes have bounded successor gaps

Round 300 pushes the Round 299 persistent-prefix family through the existing
ordered-ladder and bounded-successor-gap reductions.  Let
\[
  K_i^{\rm per,ch}=1024M_iB_iC_i .
\]
The general persistent-prefix ordering lemma gives
\[
  P^{\rm pre,per,ch}_{i,j}
  \le
  P^{\rm pre,lad,ch}_{i,j}
\]
at the same depth \(K_i^{\rm per,ch}\).  Then the bounded-successor-gap
lemma gives
\[
  P^{\rm pre,lad,ch}_{i,j}
  \le
  P^{\rm pre,pair,ch}_{i,j},
\]
where the bounded-gap chain-depth pair profile has depth
\[
  2K_i^{\rm per,ch}=2048M_iB_iC_i
\]
and gap cutoff
\[
  B_i^{\rm ch}
  =
  \left\lceil
    \frac{16384M_iB_iC_i\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substituting this into the persistent chain-absorbed finite ladder removes
the direct \(P^{\rm pre,per,ch}\) hypothesis.  The downstream radial-tail and
subdivision criteria now require bounded-gap chain-depth persistent
prefix-pair control, chain-depth spread-return control, the existing bridge
families, long-run profiles, and exact-level return profiles.  The remaining
chain-depth prefix obstruction has therefore been converted from persistent
single-level structure to bounded-gap two-level prefix-pair structure.

## Round 301 bounded-gap chain-depth prefix pairs split by fixed gap

Round 301 applies the existing bounded-gap-to-fixed-gap split to the
chain-depth prefix-pair profile from Round 300.  With
\[
  K_i^{\rm pair,ch}=2048M_iB_iC_i,
\]
and cutoff \(B_i^{\rm ch}\), the general fixed-gap split gives
\[
  P^{\rm pre,pair,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm ch}}
  P^{\rm pre,gap,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,gap,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,K_i^{\rm gap,ch},L_i,h},
  \qquad
  K_i^{\rm gap,ch}=2048M_iB_iC_iB_i^{\rm ch}.
\]

Substituting this into the bounded-gap persistent chain-absorbed ladder
replaces the coefficient-\(2\) bounded-gap pair term by a coefficient-\(2\)
finite sum over fixed gaps.  Since \(B_i^{\rm ch}\) is fixed once the finite
ladder parameters are fixed, the sum is exponent-negligible.  The matching
radial-tail and subdivision criteria have been added, so the remaining
chain-depth prefix obstruction is now a finite family of fixed-gap
persistent prefix-pair profiles, plus the chain-depth spread-return profile
and the already existing bridge/long-run/return families.

## Round 302 fixed-gap chain-depth prefix pairs are confined bridges

Round 302 applies the existing fixed-gap prefix-pair to confined-bridge
projection at the chain-depth parameters.  For each
\[
  1\le h\le B_i^{\rm ch},
\]
the deterministic confinement argument gives
\[
  P^{\rm pre,gap,ch}_{i,j,h}
  \le
  P^{\rm pre,br,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,K_i^{\rm gap,ch},L_i,h}.
\]
No parameter is lost in this step: the confined bridge profile has the same
\(K_i^{\rm gap,ch}\), \(L_i\), and fixed gap \(h\) as the fixed-gap pair
profile.

Substituting into the Round 301 fixed-gap chain-depth ladder replaces the
finite family of fixed-gap prefix-pair hypotheses by a finite family of
chain-depth confined fixed-gap bridge hypotheses.  The downstream radial-tail
and subdivision criteria are now stated in this confined-bridge form.  The
remaining chain-depth obstruction is therefore a bridge family, which can be
fed into the existing inward-free-or-return split.

## Round 303 chain-depth confined bridges split into inward-free bridges and returns

Round 303 applies the existing confined-bridge inward-free-or-return split to
the chain-depth confined bridge profiles from Round 302.  For
\[
  1\le h\le B_i^{\rm ch},
\]
the generic split gives
\[
  P^{\rm pre,br,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,ch}_{i,j,h}
  +
  R^{\rm spr,br,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,free,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K_i^{\rm gap,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,2K_i^{\rm gap,ch}\max\{h-1,1\}}.
\]
The first term keeps only inward-free bridge witnesses; the second absorbs
all bridge witnesses with radial backtracking into spread exterior-return
profiles.  The adjacent-gap case \(h=1\) is handled by the same formula
through the factor \(\max\{h-1,1\}\).

Substitution into the Round 302 ladder replaces
\[
  2\sum_{i,j}\sum_h P^{\rm pre,br,ch}_{i,j,h}
\]
by the two finite sums
\[
  2\sum_{i,j}\sum_h P^{\rm pre,br,free,ch}_{i,j,h}
  +
  2\sum_{i,j}\sum_h R^{\rm spr,br,ch}_{i,j,h}.
\]
The downstream radial-tail and subdivision criteria are now stated in this
inward-free bridge form.  The remaining genuinely bridge-like chain-depth
obstruction is therefore the inward-free confined bridge family; all
backtracking bridge mass has been moved into return profiles.

## Round 304 inward-free chain-depth bridges are record-spread or long-run

Round 304 applies the existing inward-free bridge to chain/long-run reduction
and then immediately absorbs the resulting locally short staircase-chain
profiles into prefix-record outward-spread profiles.  For
\[
  1\le h\le B_i^{\rm ch},
\]
Round 303 left
\[
  P^{\rm pre,br,free,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K_i^{\rm gap,ch},L_i,h}.
\]
The generic inward-free bridge reduction gives
\[
  P^{\rm pre,br,free,ch}_{i,j,h}
  \le
  P^{\rm pre,out,per,stair,loc,chain}_{j,2K_i^{\rm gap,ch},L_i,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the chain-to-record observation gives
\[
  P^{\rm pre,out,per,stair,loc,chain}_{j,2K_i^{\rm gap,ch},L_i,h+1}
  \le
  P^{\rm pre,rec,br,ch}_{i,j},
\]
where
\[
  P^{\rm pre,rec,br,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,ch},L_i}.
\]

Substituting into the Round 303 ladder replaces the inward-free bridge sum by
\[
  2B_i^{\rm ch}P^{\rm pre,rec,br,ch}_{i,j}
  +
  2B_i^{\rm ch}W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Together with the existing long-run term, the total long-run coefficient at
stage \(i\) becomes \(2B_i^{\rm ch}+3\).  The downstream radial-tail and
subdivision criteria are now stated in this record-absorbed form.  The
remaining new chain-depth obstruction is therefore a prefix-record
outward-spread profile at depth \(2K_i^{\rm gap,ch}\), plus the bridge-return
spread profiles from Round 303.

## Round 305 bridge-depth prefix-record becomes persistent-or-returning

Round 305 applies the short prefix-record persistent-or-return split to the
bridge-record profile introduced in Round 304.  There
\[
  P^{\rm pre,rec,br,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,ch},L_i}.
\]
With \(K=2K_i^{\rm gap,ch}\), the general split gives
\[
  P^{\rm pre,rec,br,ch}_{i,j}
  \le
  P^{\rm pre,per,br,ch}_{i,j}
  +
  R^{\rm spr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,ch}_{i,j+1},
\]
where
\[
  P^{\rm pre,per,br,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,8K_i^{\rm gap,ch}}.
\]

Substituting into the Round 304 ladder replaces
\[
  2B_i^{\rm ch}P^{\rm pre,rec,br,ch}_{i,j}
\]
by
\[
  2B_i^{\rm ch}P^{\rm pre,per,br,ch}_{i,j}
  +
  2B_i^{\rm ch}
  \bigl(
    R^{\rm spr,recbr,ch}_{i,j}
    +R^{\rm spr,recbr,ch}_{i,j+1}
  \bigr).
\]
The downstream radial-tail and subdivision criteria are now stated with this
persistent bridge-record profile and the new bridge-record spread-return
profiles.  The remaining prefix-type obstruction is persistent structure at
depth \(4K_i^{\rm gap,ch}\), which should next be pushed through the
ordered-ladder and successor-gap reductions.

## Round 306 bridge-record persistent prefixes have bounded successor gaps

Round 306 applies the ordered-ladder and bounded-successor-gap reductions to
the bridge-record persistent profile from Round 305.  Put
\[
  \Theta_i=\theta_{\lambda_i,\sigma_i,\beta_i},
  \qquad
  B_i^{\rm br,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,ch}\beta_i}{\Theta_i}
  \right\rceil+1 .
\]
Since
\[
  P^{\rm pre,per,br,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,ch},L_i},
\]
the generic ordered-ladder lemma followed by bounded successor gaps gives
\[
  P^{\rm pre,per,br,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,8K_i^{\rm gap,ch},L_i,B_i^{\rm br,ch}}.
\]
The cutoff is fixed by the finite ladder parameters and therefore does not
add a \(p\)-dependent exponent cost.

Substitution into the Round 305 ladder replaces
\[
  2B_i^{\rm ch}P^{\rm pre,per,br,ch}_{i,j}
\]
by
\[
  2B_i^{\rm ch}P^{\rm pre,pair,br,ch}_{i,j}.
\]
The downstream radial-tail and subdivision criteria are now stated with this
bounded-gap bridge-record prefix-pair family.  The next internal move should
split this bounded-gap family by the actual gap, exactly as in Round 301 but
at the bridge-record depth.

## Round 307 bridge-record prefix pairs split by actual gap

Round 307 applies the generic bounded-gap-to-fixed-gap pigeonhole reduction
to the bridge-record prefix-pair profile from Round 306.  The Round 306
profile is
\[
  P^{\rm pre,pair,br,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,8K_i^{\rm gap,ch},L_i,B_i^{\rm br,ch}} .
\]
Define the enlarged fixed-gap parameter
\[
  K_i^{\rm gap,br,ch}
  =
  8K_i^{\rm gap,ch}B_i^{\rm br,ch}.
\]
Applying the bounded-gap split with
\[
  K=8K_i^{\rm gap,ch},\qquad B=B_i^{\rm br,ch}
\]
gives
\[
  P^{\rm pre,pair,br,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,gap,br,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,gap,br,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,K_i^{\rm gap,br,ch},L_i,h}.
\]

Substitution into the Round 306 finite ladder replaces
\[
  2B_i^{\rm ch}P^{\rm pre,pair,br,ch}_{i,j}
\]
by
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,gap,br,ch}_{i,j,h}.
\]
The radial-tail and subdivision criteria have been restated with this finite
fixed-gap bridge-record family.  The next internal move is to project each
fixed-gap bridge-record pair to a confined bridge profile at the same
enlarged depth, using the existing fixed-gap-pairs-have-confined-bridges
reduction.

## Round 308 fixed-gap bridge-record pairs have confined bridges

Round 308 projects the fixed-gap bridge-record prefix-pair profiles from
Round 307 to confined fixed-gap bridge profiles at the same enlarged depth.
For
\[
  K_i^{\rm gap,br,ch}
  =
  8K_i^{\rm gap,ch}B_i^{\rm br,ch},
\]
define
\[
  P^{\rm pre,br,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,K_i^{\rm gap,br,ch},L_i,h}.
\]
The generic fixed-gap-pairs-have-confined-bridges reduction gives, for
\(1\le h\le B_i^{\rm br,ch}\),
\[
  P^{\rm pre,gap,br,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 307 finite ladder replaces
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,gap,br,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,br,recbr,ch}_{i,j,h}.
\]
The radial-tail and subdivision criteria now use this bridge-record confined
bridge family.  The remaining bridge-record obstruction is therefore no
longer a prefix-pair obstruction; it is the confined bridge family together
with the bridge-record spread-return and bridge-return spread-return terms.

## Round 309 bridge-record confined bridges split into inward-free bridges and returns

Round 309 applies the confined-bridge inward-free-or-returning dichotomy to
the bridge-record confined bridge family from Round 308.  With
\[
  K_i^{\rm gap,br,ch}
  =
  8K_i^{\rm gap,ch}B_i^{\rm br,ch},
\]
define
\[
  P^{\rm pre,br,free,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K_i^{\rm gap,br,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,2K_i^{\rm gap,br,ch}\max\{h-1,1\}} .
\]
Then, for \(1\le h\le B_i^{\rm br,ch}\),
\[
  P^{\rm pre,br,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 308 finite ladder replaces
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,br,recbr,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  \Bigl(
    P^{\rm pre,br,free,recbr,ch}_{i,j,h}
    +
    R^{\rm spr,br,recbr,ch}_{i,j,h}
  \Bigr).
\]
The radial-tail and subdivision criteria have been restated with these two
finite bridge-record families.  The remaining bridge-record prefix-type
obstruction is the inward-free bridge family, alongside the new
bridge-record bridge-return spread terms and the earlier bridge-record
spread-return terms.

## Round 310 bridge-record inward-free bridges are record-spread or long-run

Round 310 applies the inward-free bridge to locally-short-chain/long-run
reduction to the bridge-record inward-free family from Round 309.  The
inward-free profile is
\[
  P^{\rm pre,br,free,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K_i^{\rm gap,br,ch},L_i,h}.
\]
The generic reduction gives
\[
  P^{\rm pre,br,free,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,out,per,stair,loc,chain}_{j,2K_i^{\rm gap,br,ch},L_i,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the locally-short-chain to prefix-record reduction bounds
the chain profile by
\[
  P^{\rm pre,rec,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,br,ch},L_i}.
\]

Substitution into the Round 309 ladder replaces
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,br,free,recbr,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  P^{\rm pre,rec,br,recbr,ch}_{i,j}
  +
  2B_i^{\rm ch}B_i^{\rm br,ch}
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Thus the total long-run coefficient becomes
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}+2B_i^{\rm ch}+3.
\]
The radial-tail and subdivision criteria now use the bridge-record
prefix-record family, while retaining the bridge-record bridge-return spread
terms from Round 309 and the earlier bridge-record spread-return terms.

## Round 311 bridge-record prefix-record profiles are persistent or returning

Round 311 applies the short prefix-record persistent-or-return split to the
bridge-record prefix-record profile left by Round 310:
\[
  P^{\rm pre,rec,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,br,ch},L_i}.
\]
The generic split gives
\[
  P^{\rm pre,out,rec}_{j,K,L}
  \le
  P^{\rm pre,out,per}_{j,2K,L}
  +
  X^{\rm rad,ret,spr}_{j,4K}
  +
  X^{\rm rad,ret,spr}_{j+1,4K}.
\]
Thus, with \(K=2K_i^{\rm gap,br,ch}\),
\[
  P^{\rm pre,rec,br,recbr,ch}_{i,j}
  \le
  P^{\rm pre,per,br,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,ch}_{i,j+1},
\]
where
\[
  P^{\rm pre,per,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,br,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,8K_i^{\rm gap,br,ch}}.
\]

Substitution into the Round 310 ladder replaces the coefficient
\(2B_i^{\rm ch}B_i^{\rm br,ch}\) prefix-record contribution by the
corresponding persistent-prefix contribution and two adjacent return-spread
contributions with the same fixed coefficient.  The bridge-record
bridge-return terms, the earlier bridge-record spread-return terms, and the
long-run coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}+2B_i^{\rm ch}+3
\]
are unchanged.  The radial-tail and subdivision criteria now use the
bridge-record persistent prefix family, together with the new
\(R^{\rm spr,recbr,recbr,ch}\) family and the earlier bridge-record return
families.

## Round 312 bridge-record persistent prefixes have bounded successor gaps

Round 312 applies the ordered-ladder and bounded-successor-gap reductions to
the bridge-record persistent prefix profile from Round 311:
\[
  P^{\rm pre,per,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,br,ch},L_i}.
\]
The generic ordered-ladder lemma followed by the bounded-successor-gap lemma,
with \(K=4K_i^{\rm gap,br,ch}\), gives
\[
  P^{\rm pre,per,br,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,8K_i^{\rm gap,br,ch},L_i,
    B_i^{\rm br,recbr,ch}}
\]
and
\[
  B_i^{\rm br,recbr,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,br,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substitution into the Round 311 finite ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  P^{\rm pre,per,br,recbr,ch}_{i,j}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  P^{\rm pre,pair,br,recbr,ch}_{i,j}.
\]
All return-spread and bridge-return terms from Round 311 are retained, and
the long-run coefficient remains
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}+2B_i^{\rm ch}+3.
\]
The radial-tail and subdivision criteria now use the bounded-gap
bridge-record-record prefix-pair family.  The next internal move should split
this bounded-gap family by the actual successor gap, parallel to the previous
chain-depth and bridge-record prefix-pair rounds.

## Round 313 bridge-record-record bounded-gap pairs split by fixed gap

Round 313 applies the bounded-gap-to-fixed-gap split to the bounded-gap
bridge-record-record prefix-pair profile from Round 312:
\[
  P^{\rm pre,pair,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,8K_i^{\rm gap,br,ch},L_i,
    B_i^{\rm br,recbr,ch}}.
\]
With
\[
  K=8K_i^{\rm gap,br,ch},\qquad B=B_i^{\rm br,recbr,ch},
\]
the generic fixed-gap split gives
\[
  P^{\rm pre,pair,br,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,ch}}
  P^{\rm pre,gap,br,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,gap,br,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,K_i^{\rm gap,br,recbr,ch},L_i,h},
  \qquad
  K_i^{\rm gap,br,recbr,ch}
  =
  8K_i^{\rm gap,br,ch}B_i^{\rm br,recbr,ch}.
\]

Substitution into the Round 312 finite ladder replaces the coefficient
\(2B_i^{\rm ch}B_i^{\rm br,ch}\) bounded-gap pair contribution by the finite
sum over fixed gaps with the same coefficient.  The new
\(R^{\rm spr,recbr,recbr,ch}\) return-spread family, the bridge-record
bridge-return terms, and the older bridge-record spread-return terms are
unchanged, as is the long-run coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}+2B_i^{\rm ch}+3.
\]
The radial-tail and subdivision criteria now use this finite fixed-gap
bridge-record-record prefix-pair family.

## Round 314 fixed-gap bridge-record-record pairs have confined bridges

Round 314 projects the fixed-gap bridge-record-record prefix-pair profiles
from Round 313 to confined fixed-gap bridge profiles at the same enlarged
depth.  The Round 313 family is
\[
  P^{\rm pre,gap,br,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,K_i^{\rm gap,br,recbr,ch},L_i,h}.
\]
Define
\[
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,K_i^{\rm gap,br,recbr,ch},L_i,h}.
\]
The generic fixed-gap-pairs-have-confined-bridges reduction gives
\[
  P^{\rm pre,gap,br,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 313 finite ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  \sum_{h=1}^{B_i^{\rm br,recbr,ch}}
  P^{\rm pre,gap,br,recbr,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  \sum_{h=1}^{B_i^{\rm br,recbr,ch}}
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}.
\]
The radial-tail and subdivision criteria now use this bridge-record-record
confined bridge family, while retaining all return-spread and bridge-return
families from Round 313.

## Round 315 bridge-record-record confined bridges split into inward-free bridges and returns

Round 315 applies the confined-bridge inward-free-or-returning dichotomy to
the bridge-record-record confined bridge family from Round 314:
\[
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,K_i^{\rm gap,br,recbr,ch},L_i,h}.
\]
With \(K=K_i^{\rm gap,br,recbr,ch}\), the generic split gives
\[
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,free,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K_i^{\rm gap,br,recbr,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,
    2K_i^{\rm gap,br,recbr,ch}\max\{h-1,1\}}.
\]

Substitution into the Round 314 finite ladder replaces the
coefficient-\(2B_i^{\rm ch}B_i^{\rm br,ch}\) confined bridge sum by the sum
of the inward-free family and the new bridge-return spread family.  All
older return-spread and bridge-return terms are retained, and the long-run
coefficient is unchanged.

## Round 316 bridge-record-record inward-free bridges absorb into prefix records

Round 316 applies the inward-free-bridge chain-or-long-run reduction to the
bridge-record-record inward-free bridge family from Round 315:
\[
  P^{\rm pre,br,free,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,ch},L_i,h}.
\]
With \(K=2K_i^{\rm gap,br,recbr,ch}\), the generic reduction gives a locally
short staircase-chain profile of length \(h+1\), plus the long-run term:
\[
  P^{\rm pre,br,free,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,out,per,stair,loc,chain}_{j,
    2K_i^{\rm gap,br,recbr,ch},L_i,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the locally short chain-to-prefix-record reduction bounds
the chain profile by
\[
  P^{\rm pre,rec,br,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,br,recbr,ch},L_i}.
\]

Substitution into the Round 315 finite ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  \sum_{h=1}^{B_i^{\rm br,recbr,ch}}
  P^{\rm pre,br,free,recbr,recbr,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  P^{\rm pre,rec,br,recbr,recbr,ch}_{i,j},
\]
and adds the same coefficient to the long-run term.  Hence the new long-run
coefficient is
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}
  +2B_i^{\rm ch}
  +3.
\]
The radial-tail and subdivision criteria now use the bridge-record-record
prefix-record family while retaining the bridge-record-record bridge-return
spread family and all earlier return-spread terms.  The next internal move is
to split \(P^{\rm pre,rec,br,recbr,recbr,ch}_{i,j}\) into a persistent prefix
profile plus adjacent return-spread terms, paralleling Round 311.

## Round 317 bridge-record-record prefix records split into persistent prefixes and returns

Round 317 applies the short prefix-record persistent-or-returning split to the
bridge-record-record prefix-record family from Round 316:
\[
  P^{\rm pre,rec,br,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,br,recbr,ch},L_i}.
\]
With \(K=2K_i^{\rm gap,br,recbr,ch}\), the generic split gives
\[
  P^{\rm pre,rec,br,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,per,br,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,ch}_{i,j+1},
\]
where
\[
  P^{\rm pre,per,br,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,br,recbr,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,8K_i^{\rm gap,br,recbr,ch}}.
\]

Substitution into the Round 316 finite ladder replaces the
coefficient-\(2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}\)
prefix-record term by the same coefficient times the persistent-prefix
profile and the two adjacent new return-spread profiles.  The long-run
coefficient remains
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}
  +2B_i^{\rm ch}
  +3.
\]
The radial-tail and subdivision criteria now use the persistent
bridge-record-record prefix family while retaining the new return-spread
family and all earlier return-spread terms.  The next internal move is to
convert \(P^{\rm pre,per,br,recbr,recbr,ch}_{i,j}\) to a bounded-gap prefix-pair
profile, paralleling Round 312.

## Round 318 bridge-record-record persistent prefixes have bounded successor gaps

Round 318 applies the ordered-ladder and bounded-successor-gap reductions to
the persistent bridge-record-record prefix family from Round 317:
\[
  P^{\rm pre,per,br,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,br,recbr,ch},L_i}.
\]
With \(K=4K_i^{\rm gap,br,recbr,ch}\), the two generic reductions give
\[
  P^{\rm pre,per,br,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,ch}}
\]
and
\[
  B_i^{\rm br,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,br,recbr,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substitution into the Round 317 finite ladder replaces the
coefficient-\(2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}\)
persistent-prefix term by the same coefficient times the bounded-gap
prefix-pair profile.  The new adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,ch}\), the bridge-record-record bridge-return
family, all earlier return-spread families, and the long-run coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}
  +2B_i^{\rm ch}
  +3
\]
are unchanged.

The radial-tail and subdivision criteria now use the bounded-gap
bridge-record-record-record prefix-pair family.  The next internal move is to
split \(P^{\rm pre,pair,br,recbr,recbr,ch}_{i,j}\) by the actual successor
gap, likely introducing
\[
  P^{\rm pre,gap,br,recbr,recbr,ch}_{i,j,h}
  \qquad\text{and}\qquad
  K_i^{\rm gap,br,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,ch}B_i^{\rm br,recbr,recbr,ch}.
\]

## Round 319 bridge-record-record-record bounded-gap pairs split by fixed gap

Round 319 applies the bounded-gap-to-fixed-gap split to the bounded-gap
bridge-record-record-record prefix-pair profile from Round 318:
\[
  P^{\rm pre,pair,br,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,ch}}.
\]
With \(K=8K_i^{\rm gap,br,recbr,ch}\) and
\(B=B_i^{\rm br,recbr,recbr,ch}\), the fixed-gap split gives
\[
  P^{\rm pre,pair,br,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,gap,br,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,ch},L_i,h}
\]
and
\[
  K_i^{\rm gap,br,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,ch}B_i^{\rm br,recbr,recbr,ch}.
\]

Substitution into the Round 318 finite ladder replaces the
coefficient-\(2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}\)
bounded-gap pair term by the same coefficient times the finite fixed-gap sum.
The new adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,ch}\), the bridge-record-record bridge-return
family, all earlier return-spread families, and the long-run coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}
  +2B_i^{\rm ch}
  +3
\]
are unchanged.

The radial-tail and subdivision criteria now use the fixed-gap
bridge-record-record-record prefix-pair family.  The next internal move is to
project
\[
  P^{\rm pre,gap,br,recbr,recbr,ch}_{i,j,h}
\]
to confined fixed-gap bridge profiles at the same enlarged depth, paralleling
Round 314.

## Round 320 fixed-gap bridge-record-record-record pairs have confined bridges

Round 320 projects the fixed-gap bridge-record-record-record prefix-pair
profiles from Round 319 to confined fixed-gap bridge profiles at the same
enlarged depth.  The Round 319 family is
\[
  P^{\rm pre,gap,br,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,ch},L_i,h}.
\]
The generic fixed-gap-pairs-have-confined-bridges reduction gives
\[
  P^{\rm pre,gap,br,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,ch},L_i,h}.
\]

Substitution into the Round 319 finite ladder replaces the
coefficient-\(2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}\)
fixed-gap pair sum by the same coefficient times the confined bridge sum.
The return-spread and bridge-return families from Round 319 are retained, and
the long-run coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}
  +2B_i^{\rm ch}
  +3
\]
is unchanged.

The radial-tail and subdivision criteria now use the bridge-record-record-record
confined bridge family.  The next internal move is to split
\[
  P^{\rm pre,br,recbr,recbr,recbr,ch}_{i,j,h}
\]
into an inward-free bridge family and a bridge-return spread family,
paralleling Round 315.

## Round 321 bridge-record-record-record confined bridges split into inward-free bridges and returns

Round 321 applies the confined-bridge inward-free-or-returning dichotomy to
the bridge-record-record-record confined bridge family from Round 320:
\[
  P^{\rm pre,br,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,ch},L_i,h}.
\]
The split gives
\[
  P^{\rm pre,br,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,recbr,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,
    2K_i^{\rm gap,br,recbr,recbr,ch}\max\{h-1,1\}}.
\]

Substitution into the Round 320 finite ladder replaces the confined bridge
sum by the same coefficient times the inward-free bridge sum plus the new
bridge-return spread sum.  The existing adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,ch}\), the bridge-record-record bridge-return
family, all earlier return-spread families, and the long-run coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}
  +2B_i^{\rm ch}
  +3
\]
are unchanged.

The radial-tail and subdivision criteria now use the
bridge-record-record-record inward-free bridge family together with the new
bridge-return spread family.  The next internal move is to absorb
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,ch}_{i,j,h}
\]
into a deeper prefix-record family plus long-run terms, paralleling
Round 316.

## Round 322 bridge-record-record-record inward-free bridges are prefix records or long runs

Round 322 applies the inward-free bridge chain-or-long-run reduction to the
bridge-record-record-record inward-free family from Round 321:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,ch},L_i,h}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,ch},
\]
the reduction gives a locally short staircase chain plus a long-run term.
Since the resulting chain length is \(h+1\ge2\), the locally short
staircase-chain-to-prefix-record reduction gives
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j},
\]
where
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,
    2K_i^{\rm gap,br,recbr,recbr,ch},L_i}.
\]

Substitution into the Round 321 finite ladder replaces the inward-free bridge
sum by the same coefficient times the new prefix-record profile and adds
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}
\]
to the long-run coefficient.  The new long-run coefficient is
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}
  +2B_i^{\rm ch}
  +3.
\]
All bridge-return and return-spread families from Round 321 are retained.

The radial-tail and subdivision criteria now use the
bridge-record-record-record prefix-record family.  The next internal move is
to split
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
\]
into a persistent prefix profile plus adjacent return-spread terms,
paralleling Round 317.

## Round 323 bridge-record-record-record prefix records split into persistent prefixes and returns

Round 323 applies the short prefix-record persistent-or-returning split to the
deeper bridge-record-record-record prefix-record family from Round 322:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,
    2K_i^{\rm gap,br,recbr,recbr,ch},L_i}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,ch},
\]
the split gives
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,per,br,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,ch}_{i,j+1},
\]
where
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,
    8K_i^{\rm gap,br,recbr,recbr,ch}}.
\]

Substitution into the Round 322 finite ladder replaces the prefix-record
profile by the persistent prefix profile and two adjacent return-spread
profiles with the same fixed coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}.
\]
The long-run coefficient is unchanged, and all bridge-return and
return-spread families from Round 322 are retained.

The radial-tail and subdivision criteria now use the
bridge-record-record-record persistent prefix family together with the new
adjacent return-spread family.  The next internal move is to convert
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,ch}_{i,j}
\]
to a bounded-gap prefix-pair profile, paralleling Round 318.

## Round 324 persistent bridge-record-record-record prefixes have bounded-gap pairs

Round 324 converts the persistent bridge-record-record-record prefix profile
from Round 323,
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,ch},L_i},
\]
to a bounded-gap prefix-pair profile.  Applying the persistent-prefix
ordered-ladder reduction and then the bounded-successor-gap reduction with
\[
  K=4K_i^{\rm gap,br,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,ch}}
\]
and
\[
  B_i^{\rm br,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,br,recbr,recbr,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1.
\]

Substitution into the Round 323 finite ladder replaces the persistent-prefix
profile by the bounded-gap prefix-pair profile with the same fixed coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}.
\]
The adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,ch}\), all retained bridge-return and
return-spread families, and the long-run coefficient are unchanged.

The radial-tail and subdivision criteria now use the bounded-gap
bridge-record-record-record-record-record prefix-pair family.  The next
internal move is to split
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,ch}_{i,j}
\]
by the actual successor gap, paralleling Round 319.

## Round 325 bounded-gap bridge-record-record-record-record pairs split by successor gap

Round 325 splits the bounded-gap bridge-record-record-record-record
prefix-pair profile from Round 324 by the actual successor gap:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,ch}} .
\]
The bounded-gap-to-fixed-gap split with
\[
  K=8K_i^{\rm gap,br,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h}
\]
and
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 324 finite ladder replaces the bounded-gap
prefix-pair profile by the finite actual-gap sum with the same fixed
coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}.
\]
All return-spread and bridge-return families from Round 324 are retained, and
the long-run coefficient is unchanged.

The radial-tail and subdivision criteria now use the fixed-gap
bridge-record-record-record-record prefix-pair family.  The next internal move
is to project
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h}
\]
to confined fixed-gap bridge profiles, paralleling Round 320.

## Round 326 fixed-gap bridge-record-record-record-record pairs have confined bridges

Round 326 projects the fixed-gap bridge-record-record-record-record
prefix-pair family from Round 325 to a confined fixed-gap bridge family:
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h}.
\]
The fixed-gap pair-to-confined-bridge reduction with
\[
  (\lambda,\sigma,\beta,K,L)
  =
  (\lambda_i,\sigma_i,\beta_i,
    K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i)
\]
gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h}.
\]

Substitution into the Round 325 finite ladder replaces the fixed-gap
prefix-pair family by the confined bridge family with the same inherited
coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,ch}
  =
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}.
\]
All return-spread and bridge-return families from Round 325 are retained, and
the long-run coefficient is unchanged.

The radial-tail and subdivision criteria now use the confined fixed-gap
bridge-record-record-record-record bridge family.  The next internal move is
to split
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
into an inward-free bridge profile and a bridge-return spread profile,
paralleling Round 321.

## Round 327 bridge-record-record-record-record confined bridges split into inward-free bridges and returns

Round 327 applies the confined-bridge inward-free-or-returning dichotomy to
the bridge-record-record-record-record confined bridge family from Round 326:
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h}.
\]
The split gives
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
with
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,ch}\max\{h-1,1\}}.
\]

Substitution into the Round 326 finite ladder replaces the confined bridge sum
by the same inherited coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,ch}
\]
times the inward-free bridge sum plus the new bridge-return spread sum.  The
existing adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,ch}\), all earlier bridge-return and
return-spread families, and the long-run coefficient are unchanged.

The radial-tail and subdivision criteria now use the
bridge-record-record-record-record inward-free bridge family together with the
new bridge-return spread family.  The next internal move is to absorb
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
into a deeper prefix-record family plus long-run terms, paralleling Round 322.

## Round 328 bridge-record-record-record-record inward-free bridges are prefix records or long runs

Round 328 applies the inward-free bridge chain-or-long-run reduction to the
bridge-record-record-record-record inward-free family from Round 327:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,ch},
\]
the reduction gives a locally short staircase chain plus a long-run term.
Since the resulting chain length is \(h+1\ge2\), the locally short
staircase-chain-to-prefix-record reduction gives
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j},
\]
where
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i}.
\]

Substitution into the Round 327 finite ladder replaces the inward-free bridge
sum by the new prefix-record profile with coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,ch}.
\]
The same coefficient is added to the long-run coefficient:
\[
  A_i^{\rm long,br,recbr,recbr,recbr,ch}
  =
  A_i^{\rm long,br,recbr,recbr,ch}
  +D_i^{\rm rec,br,recbr,recbr,recbr,ch}.
\]
All bridge-return and return-spread families from Round 327 are retained.

The radial-tail and subdivision criteria now use the
bridge-record-record-record-record prefix-record family.  The next internal
move is to split
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
into a persistent prefix profile plus adjacent return-spread terms,
paralleling Round 323.

## Round 329 bridge-record-record-record-record prefix records split into persistent prefixes

Round 329 applies the short prefix-record persistent-or-returning split to the
bridge-record-record-record-record prefix-record family from Round 328:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,ch},
\]
the split gives
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1},
\]
where
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,ch}}.
\]

Substitution into the Round 328 finite ladder replaces the prefix-record term
under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,ch}
\]
by the corresponding persistent prefix term and the two adjacent return-spread
terms.  The long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,ch}
\]
is unchanged.  All bridge-return and older return-spread families from Round
328 are retained.

The radial-tail and subdivision criteria now use the
bridge-record-record-record-record persistent prefix family and the new
adjacent return-spread family.  The next internal move is to convert
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
to a bounded-gap prefix-pair profile, paralleling Round 324.

## Round 330 persistent bridge-record-record-record-record prefixes have bounded-gap pairs

Round 330 converts the persistent bridge-record-record-record-record prefix
profile from Round 329,
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i},
\]
to a bounded-gap prefix-pair profile.  Applying the persistent-prefix
ordered-ladder reduction and then the bounded-successor-gap reduction with
\[
  K=4K_i^{\rm gap,br,recbr,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,recbr,ch}}
\]
and
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,br,recbr,recbr,recbr,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1.
\]

Substitution into the Round 329 finite ladder replaces the persistent-prefix
profile by the bounded-gap prefix-pair profile with the same fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,ch}.
\]
The adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,ch}\), all retained bridge-return
and return-spread families, and the long-run coefficient are unchanged.

The radial-tail and subdivision criteria now use the bounded-gap
bridge-record-record-record-record-record prefix-pair family.  The next
internal move is to split
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
by the actual successor gap, paralleling Round 325.

## Round 331 bounded-gap bridge-record-record-record-record-record pairs split by successor gap

Round 331 splits the bounded-gap bridge-record-record-record-record-record
prefix-pair profile from Round 330 by the actual successor gap:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,recbr,ch}} .
\]
The bounded-gap-to-fixed-gap split with
\[
  K=8K_i^{\rm gap,br,recbr,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i,h}
\]
and
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 330 finite ladder replaces the bounded-gap
prefix-pair profile by the finite actual-gap sum with the same fixed
coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,ch}.
\]
All return-spread and bridge-return families from Round 330 are retained, and
the long-run coefficient is unchanged.

The radial-tail and subdivision criteria now use the fixed-gap
bridge-record-record-record-record-record prefix-pair family.  The next
internal move is to project
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
to confined fixed-gap bridge profiles at the same enlarged depth, paralleling
Round 326.

## Round 332 fixed-gap bridge-record-record-record-record-record pairs have confined bridges

Round 332 projects the fixed-gap bridge-record-record-record-record-record
prefix-pair family from Round 331 to a confined fixed-gap bridge family:
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
The fixed-gap pair-to-confined-bridge reduction with
\[
  (\lambda,\sigma,\beta,K,L)
  =
  (\lambda_i,\sigma_i,\beta_i,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i)
\]
gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]

Substitution into the Round 331 finite ladder replaces the fixed-gap
prefix-pair family by the confined bridge family with the same inherited
coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,ch}.
\]
All return-spread and bridge-return families from Round 331 are retained, and
no new variable multiplicative loss is introduced.

The radial-tail and subdivision criteria now use the confined fixed-gap
bridge-record-record-record-record-record bridge family.  The next internal
move is to split
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
into an inward-free bridge profile and a bridge-return spread profile,
paralleling Round 327.

## Round 333 bridge-record-record-record-record-record confined bridges split into inward-free bridges and returns

Round 333 applies the confined-bridge inward-free-or-returning dichotomy to
the bridge-record-record-record-record-record confined bridge family from
Round 332:
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
The split gives
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
with
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch}\max\{h-1,1\}}.
\]

Substitution into the Round 332 finite ladder replaces the confined bridge
sum by the same inherited coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,ch}
\]
times the inward-free bridge sum plus the new bridge-return spread sum.  The
existing adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,ch}\), all earlier bridge-return
and return-spread families, and the long-run coefficient are unchanged.

The radial-tail and subdivision criteria now use the
bridge-record-record-record-record-record inward-free bridge family together
with the new bridge-return spread family.  The next internal move is to absorb
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
into a deeper prefix-record family plus long-run terms, paralleling Round 328.

## Round 334 bridge-record-record-record-record-record inward-free bridges are prefix records or long runs

Round 334 applies the inward-free bridge chain-or-long-run reduction to the
bridge-record-record-record-record-record inward-free bridge family from
Round 333:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
The reduction gives
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,out,per,stair,loc,chain}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the locally short staircase-chain prefix-record reduction
bounds the chain profile by
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i}.
\]

Substitution into the Round 333 finite ladder replaces the inward-free bridge
sum by the new prefix-record profile with coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,ch}.
\]
It also enlarges the long-run coefficient to
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,ch}
  =
  A_i^{\rm long,br,recbr,recbr,recbr,ch}
  +D_i^{\rm rec,br,recbr,recbr,recbr,recbr,ch}.
\]
All bridge-return and return-spread families from Round 333 are retained.

The radial-tail and subdivision criteria now use the
bridge-record-record-record-record-record prefix-record family.  The next
internal move is to split
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
into a persistent prefix profile plus adjacent return-spread terms, paralleling
Round 329.

## Round 335 bridge-record-record-record-record-record prefix records split into persistent prefixes

Round 335 applies the short prefix-record persistent-or-returning split to the
Round 334 prefix-record family:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\]
Here the persistent prefix uses the doubled prefix threshold,
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i},
\]
while the adjacent return-spread profile uses the general split threshold
\(4K=8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch}\):
\[
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch}}.
\]

Substitution into the Round 334 finite ladder replaces the prefix-record term
under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,ch}
\]
by the persistent prefix and the same/next-slab adjacent return-spread terms.
The long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,ch}
\]
is unchanged in this round, and all retained bridge-return, adjacent
return-spread, staircase/local bridge, enlarged spread-return, and exact-level
return terms remain in the ladder.

The radial-tail and subdivision criteria now use the persistent
bridge-record-record-record-record-record prefix family together with the new
adjacent return-spread family.  The next internal move is to convert
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
to a bounded-gap prefix-pair profile, paralleling the Round 330 conversion.

## Round 336 persistent bridge-record-record-record-record-record prefixes have bounded-gap pairs

Round 336 converts the persistent prefix family from Round 335 to a bounded-gap
prefix-pair profile.  The starting profile is
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i}.
\]
Applying the persistent-prefix ordered-ladder reduction and then the
bounded-successor-gap reduction with
\[
  K=4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
The bounded-gap pair profile is
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,ch}},
\]
where
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substitution into the Round 335 finite ladder replaces the persistent prefix
term under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,ch}
\]
by the bounded-gap prefix-pair term.  The adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), the bridge-return
families, the older return-spread families, and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,ch}
\]
are unchanged.

The radial-tail and subdivision criteria now use the bounded-gap
bridge-record-record-record-record-record-record prefix-pair family.  The next
internal move is to split
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
by the actual successor gap, paralleling Round 331.

## Round 337 bounded-gap bridge-record-record-record-record-record-record pairs split by successor gap

Round 337 splits the bounded-gap
bridge-record-record-record-record-record-record prefix-pair profile from
Round 336 by the actual successor gap:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,ch}}.
\]
The bounded-gap-to-fixed-gap split with
\[
  K=8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
Here
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i,h},
\]
with
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 336 finite ladder replaces the bounded-gap pair
term under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,ch}
\]
by the finite fixed-gap sum.  The adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), the bridge-return
families, the older return-spread families, and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,ch}
\]
are unchanged.

The radial-tail and subdivision criteria now use the fixed-gap
bridge-record-record-record-record-record-record prefix-pair family.  The next
internal move is to project
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
to confined fixed-gap bridge profiles at the same enlarged depth, paralleling
Round 332.

## Round 338 fixed-gap bridge-record-record-record-record-record-record pairs have confined bridges

Round 338 projects the fixed-gap
bridge-record-record-record-record-record-record prefix-pair family from
Round 337 to a confined fixed-gap bridge family:
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
The fixed-gap pair-to-confined-bridge reduction with
\[
  (\lambda,\sigma,\beta,K,L)
  =
  (\lambda_i,\sigma_i,\beta_i,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i)
\]
gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]

Substitution into the Round 337 finite ladder replaces the fixed-gap
prefix-pair sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,ch}
\]
by the confined bridge sum.  The adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), the bridge-return
families, the older return-spread families, and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,ch}
\]
are unchanged.

The radial-tail and subdivision criteria now use the confined fixed-gap
bridge-record-record-record-record-record-record bridge family.  The next
internal move is to split
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
into an inward-free bridge family plus a bridge-return spread family,
paralleling Round 333.

## Round 339 bridge-record-record-record-record-record-record confined bridges split into inward-free bridges and returns

Round 339 applies the confined-bridge inward-free-or-returning dichotomy to
the Round 338 confined bridge family:
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
With
\[
  K=K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},
\]
the generic bridge split gives
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K,L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,2K\max\{h-1,1\}}.
\]

Substitution into the Round 338 finite ladder replaces the confined bridge
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the inward-free bridge sum plus the new
bridge-return spread sum.  The adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), all earlier
bridge-return and return-spread families, and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,ch}
\]
are retained.

The radial-tail and subdivision criteria now use the
bridge-record-record-record-record-record-record inward-free bridge family
together with the new bridge-return spread family.  The next internal move is
to absorb
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
into a deeper prefix-record profile plus a long-run contribution, paralleling
Round 334.

## Round 340 bridge-record-record-record-record-record-record inward-free bridges absorb into prefix records

Round 340 applies the inward-free bridge chain-or-long-run reduction to the
bridge-record-record-record-record-record-record inward-free family from
Round 339:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},
\]
the generic inward-free bridge reduction gives
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,out,per,stair,loc,chain}_{j,K,L_i,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the locally short staircase-chain reduction bounds the
chain term by the prefix-record profile
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,K,L_i}.
\]

Substitution into the Round 339 finite ladder replaces the inward-free bridge
sum by the prefix-record sum under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The long-run coefficient becomes
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,ch}
  =
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,ch}
  +D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,ch}.
\]
All bridge-return and return-spread families from Round 339 are retained.

The radial-tail and subdivision criteria now use the
bridge-record-record-record-record-record-record prefix-record family.  The
next internal move is to split
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
into a persistent prefix family and adjacent return-spread terms, paralleling
Round 335.

## Round 341 bridge-record-record-record-record-record-record prefix records split into persistent prefixes

Round 341 applies the short prefix-record persistent-or-returning split to the
deeper prefix-record family left by Round 340:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},
\]
the generic split gives
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1},
\]
where
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch}}.
\]

Substitution into the Round 340 finite ladder replaces the prefix-record sum
under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the persistent prefix sum and the two adjacent
return-spread sums.  The long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,ch}
\]
is unchanged in this split, and all bridge-return and older return-spread
families from Round 340 are retained.

The radial-tail and subdivision criteria now use the
bridge-record-record-record-record-record-record persistent prefix family and
the new adjacent return-spread family.  The next internal move is to convert
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
to a bounded-gap prefix-pair profile, paralleling Round 336.

## Round 342 persistent bridge-record-record-record-record-record-record prefixes have bounded-gap pairs

Round 342 applies the persistent-prefix ordered-ladder reduction and the
bounded-successor-gap reduction to the persistent prefix family left by
Round 341:
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i}.
\]
With
\[
  K=4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},
\]
the ordered-ladder and bounded-successor-gap reductions give
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
\]
and
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substitution into the Round 341 finite ladder replaces the persistent-prefix
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the bounded-gap prefix-pair sum.  The adjacent
return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), the
bridge-return families, the older return-spread families, and the long-run
coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,ch}
\]
are unchanged.

The radial-tail and subdivision criteria now use the fixed bounded-gap
bridge-record-record-record-record-record-record-record prefix-pair family.
The next internal move is to split
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
by the actual successor gap, paralleling Round 337.

## Round 343 bounded-gap bridge-record-record-record-record-record-record-record pairs split by actual gap

Round 343 applies the bounded-gap-to-fixed-gap split to the bounded-gap
prefix-pair family left by Round 342:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,ch}}.
\]
With
\[
  K=8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}
\]
and
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 342 finite ladder replaces the bounded-gap
prefix-pair sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the finite fixed-gap \(h\)-sum.  The adjacent
return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), the
bridge-return families, the older return-spread families, and the long-run
coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,ch}
\]
are unchanged.

The radial-tail and subdivision criteria now use the fixed-gap
bridge-record-record-record-record-record-record-record prefix-pair family.
The next internal move is to project
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
to confined fixed-gap bridge profiles, paralleling Round 338.

## Round 344 fixed-gap bridge-record-record-record-record-record-record-record pairs have confined bridges

Round 344 projects the fixed-gap prefix-pair family from Round 343 to a
confined fixed-gap bridge family:
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
The fixed-gap pair-to-confined-bridge reduction with
\[
  (\lambda,\sigma,\beta,K,L)
  =
  (\lambda_i,\sigma_i,\beta_i,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i)
\]
gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]

Substitution into the Round 343 finite ladder replaces the fixed-gap
prefix-pair \(h\)-sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the confined bridge \(h\)-sum.  The adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), the
bridge-return families, the older return-spread families, and the long-run
coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,ch}
\]
are unchanged.

The radial-tail and subdivision criteria now use the confined fixed-gap
bridge-record-record-record-record-record-record-record bridge family.  The
next internal move is to split
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
into an inward-free bridge family plus a bridge-return spread family,
paralleling Round 339.

## Round 345 bridge-record-record-record-record-record-record-record confined bridges split into inward-free bridges and returns

Round 345 applies the confined-bridge inward-free-or-returning dichotomy to
the Round 344 confined bridge family:
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
With
\[
  K=K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the generic bridge split gives
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K,L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,2K\max\{h-1,1\}}.
\]

Substitution into the Round 344 finite ladder replaces the confined bridge
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the seventh inward-free bridge sum plus the new
seventh bridge-return spread sum.  The adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), all earlier
bridge-return and return-spread families, and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,ch}
\]
are retained.

The radial-tail and subdivision criteria now use the
bridge-record-record-record-record-record-record-record inward-free bridge
family together with the new bridge-return spread family.  The next internal
move is to absorb
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
into a deeper prefix-record profile plus a long-run contribution, paralleling
Round 340.

## Round 346 bridge-record-record-record-record-record-record-record inward-free bridges absorb into prefix records

Round 346 applies the inward-free bridge chain-or-long-run reduction to the
seventh inward-free bridge family from Round 345:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the generic inward-free bridge reduction gives
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,out,per,stair,loc,chain}_{j,K,L_i,h+1}
  +
  W_{\beta_i,p}T_{i,j}^{\rm long}.
\]
Since \(h+1\ge2\), the locally short staircase-chain-to-prefix-record
reduction bounds the chain term by
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,K,L_i}.
\]
Thus the seventh inward-free bridge hypothesis is replaced by this
prefix-record hypothesis plus a long-run contribution.

Substitution into the Round 345 finite ladder replaces the inward-free bridge
sum by the prefix-record sum with coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
It also updates the long-run coefficient to
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,ch}
  +D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
All bridge-return and return-spread families from Round 345 are retained.

The radial-tail and subdivision criteria now use the
bridge-record-record-record-record-record-record-record prefix-record family.
The next internal move is to split this prefix-record family into a persistent
prefix profile plus adjacent return-spread terms, paralleling Round 341.

## Round 347 bridge-record-record-record-record-record-record-record prefix records split into persistent prefixes

Round 347 applies the short prefix-record persistent-or-returning split to the
deeper prefix-record family left by Round 346:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le{}&
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]
Here the persistent-prefix threshold is \(2K\) and the return threshold is
\(4K\), i.e.
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}}.
\]

Substitution into the Round 346 finite ladder replaces the prefix-record sum
under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the persistent-prefix sum plus the two adjacent
return-spread sums.  The long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
is unchanged, and all bridge-return and return-spread families from Round 346
are retained.

The radial-tail and subdivision criteria now use the eighth persistent prefix
family together with the new eighth adjacent return-spread family.  The next
internal move is to convert this persistent-prefix family into a bounded-gap
prefix-pair family, paralleling Round 342.

## Round 348 persistent bridge-record-record-record-record-record-record-record prefixes have bounded-gap pairs

Round 348 applies the persistent-prefix ordered-ladder reduction and the
bounded-successor-gap reduction to the eighth persistent prefix family from
Round 347:
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i}.
\]
With
\[
  K=4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the two reductions give
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
\]
and
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substitution into the Round 347 finite ladder replaces the persistent-prefix
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the bounded-gap prefix-pair sum.  The adjacent
return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), all older
return-spread and bridge-return families, and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
are unchanged.

The radial-tail and subdivision criteria now use the eighth bounded-gap
prefix-pair family.  The next internal move is to split this bounded-gap
family by the actual successor gap, paralleling Round 343.

## Round 349 bounded-gap bridge-record-record-record-record-record-record-record-record pairs split by actual gap

Round 349 applies the bounded-gap-to-fixed-gap split to the eighth bounded-gap
prefix-pair family from Round 348:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}.
\]
With
\[
  K=8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
Here
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}
\]
and
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 348 finite ladder replaces the bounded-gap pair
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the fixed-gap \(h\)-sum.  The adjacent
return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), all older
return-spread and bridge-return families, and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
are unchanged.

The radial-tail and subdivision criteria now use the eighth fixed-gap
prefix-pair family.  The next internal move is to project the fixed-gap
prefix-pair family to confined fixed-gap bridge profiles, paralleling
Round 344.

## Round 350 fixed-gap bridge-record-record-record-record-record-record-record-record pairs project to confined bridges

Round 350 applies the fixed-gap pair-to-confined-bridge reduction to the
eighth fixed-gap prefix-pair family from Round 349:
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
With
\[
  (\lambda,\sigma,\beta,K,L)
  =
  (\lambda_i,\sigma_i,\beta_i,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i),
\]
the projection gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
Here
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]

Substitution into the Round 349 finite ladder replaces the fixed-gap
prefix-pair sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the confined bridge sum.  The adjacent
return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), all older
return-spread and bridge-return families, and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
are unchanged.

The radial-tail and subdivision criteria now use the eighth confined bridge
family.  The next internal move is to split the confined bridge family into an
inward-free bridge family plus a bridge-return spread family, paralleling
Round 345.

## Round 351 confined bridge-record-record-record-record-record-record-record-record bridges split into inward-free bridges and bridge returns

Round 351 applies the confined-bridge inward-free-or-returning dichotomy to
the eighth confined bridge family from Round 350:
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
The dichotomy gives
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
Here
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
    \max\{h-1,1\}}.
\]

Substitution into the Round 350 finite ladder replaces the confined bridge
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the inward-free bridge sum plus the new
bridge-return spread sum.  The adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), all older
return-spread and bridge-return families, and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
are unchanged.

The radial-tail and subdivision criteria now use the eighth inward-free bridge
family together with the new eighth bridge-return spread family.  The next
internal move is to absorb the inward-free bridge family into a deeper
prefix-record profile plus a long-run contribution, paralleling Round 346.

## Round 352 inward-free bridge-record-record-record-record-record-record-record-record bridges absorb into prefix records

Round 352 applies the inward-free-bridge chain-or-long-run reduction to the
eighth inward-free bridge family from Round 351:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h}.
\]
It gives
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,out,per,stair,loc,chain}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the staircase-chain-to-prefix-record reduction bounds the
chain term by
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]

Substitution into the Round 351 finite ladder replaces the inward-free bridge
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the new prefix-record sum under
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The long-run coefficient is updated to
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  +D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The eighth bridge-return family
\(R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), the
adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}\), and all
older return-spread and bridge-return families are retained.

The radial-tail and subdivision criteria now use the eighth prefix-record
family.  The next internal move is to split the prefix-record family into a
persistent prefix family plus adjacent return-spread terms, paralleling
Round 347.

## Round 353 bridge-record-record-record-record-record-record-record-record prefix records split into persistent prefixes

Round 353 applies the short prefix-record persistent-or-returning split to the
deeper prefix-record family left by Round 352:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le{}&
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]
Here the persistent-prefix threshold is \(2K\) and the return threshold is
\(4K\), i.e.
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}.
\]

Substitution into the Round 352 finite ladder replaces the prefix-record sum
under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the same coefficient times the persistent-prefix sum plus the two adjacent
return-spread sums.  The long-run coefficient
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
is unchanged, and all bridge-return and return-spread families from Round 352
are retained.

The radial-tail and subdivision criteria now use the ninth persistent prefix
family together with the new ninth adjacent return-spread family.  The next
internal move is to convert this persistent-prefix family into a bounded-gap
prefix-pair family, paralleling Round 348.

## Round 354 ninth persistent prefixes convert to bounded-gap prefix pairs

Round 354 applies the ordered-ladder and bounded-successor-gap reductions to
the ninth persistent prefix family left by Round 353:
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i}.
\]
With
\[
  \Theta_i=\theta_{\lambda_i,\sigma_i,\beta_i}
\]
the new bounded successor-gap cutoff is
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\Theta_i}
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  \right\rceil+1.
\]
The reduction gives
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j},
\]
where the pair profile uses cutoff
\[
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
and the new \(B_i\)-bound above.

Substitution into the Round 353 finite ladder replaces the persistent-prefix
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the bounded-gap prefix-pair sum under the same coefficient.  The ninth
adjacent return-spread family, the eighth bridge-return family, all earlier
return-spread and bridge-return families, long-run profiles, and exact-level
return profiles are retained.

The radial-tail and subdivision criteria now use the ninth bounded-gap
prefix-pair family.  The next internal move is to split the bounded-gap pair
profile by the actual successor gap, paralleling Round 349.

## Round 355 ninth bounded-gap prefix pairs split by actual successor gap

Round 355 applies the bounded-gap-to-fixed-gap split to the ninth bounded-gap
prefix-pair family left by Round 354:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With
\[
  K=8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the fixed-gap scale is
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The reduction gives
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 354 finite ladder replaces the bounded-gap
prefix-pair sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the finite \(h\)-sum of fixed-gap pair profiles under the same coefficient.
The ninth adjacent return-spread family, the eighth bridge-return family, all
earlier return-spread and bridge-return families, long-run profiles, and
exact-level return profiles are retained.

The radial-tail and subdivision criteria now use the ninth fixed-gap
prefix-pair family.  The next internal move is to project the fixed-gap pair
profile to confined bridge profiles, paralleling Round 350.

## Round 356 ninth fixed-gap prefix pairs project to confined bridges

Round 356 applies the fixed-gap pair-to-confined-bridge projection to the ninth
fixed-gap prefix-pair family left by Round 355:
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
With
\[
  (\lambda,\sigma,\beta,K,L)
  =
  (\lambda_i,\sigma_i,\beta_i,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i),
\]
the projection gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 355 finite ladder replaces the fixed-gap pair
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the confined bridge sum under the same coefficient.  The ninth adjacent
return-spread family, the eighth bridge-return family, all earlier
return-spread and bridge-return families, long-run profiles, and exact-level
return profiles are retained.

The radial-tail and subdivision criteria now use the ninth confined bridge
family.  The next internal move is to split this confined bridge family into
an inward-free bridge family plus a bridge-return spread family, paralleling
Round 351.

## Round 357 ninth confined bridges split into inward-free bridges

Round 357 applies the confined-bridge inward-free-or-returning dichotomy to
the ninth confined bridge family left by Round 356:
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
With
\[
  (\lambda,\sigma,\beta,K,L)
  =
  (\lambda_i,\sigma_i,\beta_i,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i),
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le{}&
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}\\
  &+
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\end{aligned}
\]

Substitution into the Round 356 finite ladder replaces the confined bridge
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the inward-free bridge sum plus the new bridge-return spread sum under the
same coefficient.  The ninth adjacent return-spread family, the eighth
bridge-return family, all earlier return-spread and bridge-return families,
long-run profiles, and exact-level return profiles are retained.

The radial-tail and subdivision criteria now use the ninth inward-free bridge
family and the ninth bridge-return spread family.  The next internal move is
to absorb the inward-free bridge family into a deeper prefix-record profile
plus a long-run contribution, paralleling Round 352.

## Round 358 ninth inward-free bridges absorb into prefix records

Round 358 applies the inward-free-bridge chain-or-long-run reduction to the
ninth inward-free bridge family left by Round 357:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
The reduction gives a locally short staircase-chain profile at level \(h+1\)
plus \(W_{\beta_i,p}T^{\rm long}_{i,j}\).  Since \(h+1\ge2\), the
staircase-chain-to-prefix-record reduction bounds the chain term by
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]

Substitution into the Round 357 finite ladder replaces the inward-free bridge
sum with this prefix-record sum under the new coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The long-run coefficient is updated to
\[
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  A_i^{\rm long,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  +D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The ninth bridge-return family, the adjacent return-spread family, and all
older return-spread and bridge-return families are retained.

The radial-tail and subdivision criteria now use the ninth prefix-record
family.  The next internal move is to split the prefix-record family into a
persistent prefix family plus adjacent return-spread terms, paralleling
Round 353.

## Round 359 ninth prefix records split into persistent prefixes

Round 359 applies the short prefix-record persistent-or-returning split to the
ninth prefix-record family left by Round 358:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le{}&
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The persistent prefix threshold is
\[
  4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
and the return-spread threshold is
\[
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 358 finite ladder replaces the ninth prefix-record
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the corresponding persistent prefix sum plus same- and next-bin
return-spread sums.  The long-run coefficient from Round 358 is unchanged.

The radial-tail and subdivision criteria now use the tenth persistent prefix
family and the tenth adjacent return-spread family, while retaining the ninth
bridge-return family and all older return-spread and bridge-return families.
The next internal move is to convert the persistent prefix family into a
bounded-gap prefix-pair family, paralleling Round 354.

## Round 360 tenth persistent prefixes become bounded-gap pairs

Round 360 applies the ordered-ladder and bounded-successor reductions to the
tenth persistent prefix family left by Round 359:
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
At
\[
  K=4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the successor-gap cutoff becomes
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  \right\rceil+1,
\]
and the pair profile uses radial cutoff
\[
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
Thus
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]

Substitution into the Round 359 finite ladder replaces the persistent prefix
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the corresponding bounded-gap pair sum.  The adjacent tenth return-spread
family, ninth bridge-return family, older return-spread and bridge-return
families, and long-run terms are retained.

The radial-tail and subdivision criteria now use the tenth bounded-gap
prefix-pair family.  The next internal move is to split that pair family by
the actual successor gap, paralleling Round 355.

## Round 361 tenth bounded-gap pairs split by successor gap

Round 361 applies the bounded-gap-to-fixed-gap split to the tenth
bounded-gap prefix-pair family left by Round 360:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With
\[
  K=8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
The new product cutoff is
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 360 finite ladder replaces the bounded-gap pair
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by a finite sum over fixed successor gaps.  The adjacent tenth return-spread
family, ninth bridge-return family, older return-spread and bridge-return
families, and long-run terms are retained.

The radial-tail and subdivision criteria now use the tenth fixed-gap
prefix-pair family.  The next internal move is to project that fixed-gap pair
family to confined fixed-gap bridge profiles, paralleling Round 356.

## Round 362 tenth fixed-gap pairs project to confined bridges

Round 362 applies the fixed-gap pair-to-confined-bridge reduction to the
tenth fixed-gap prefix-pair family left by Round 361:
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At the fixed product cutoff
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the reduction gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 361 finite ladder replaces the fixed-gap pair sum
under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the corresponding confined bridge sum.  The adjacent tenth return-spread
family, ninth bridge-return family, older return-spread and bridge-return
families, and long-run terms are retained.

The radial-tail and subdivision criteria now use the tenth confined bridge
family.  The next internal move is to split that confined bridge family into
an inward-free bridge family plus a bridge-return spread family, paralleling
Round 357.

## Round 363 tenth confined bridges split inward-free/returning

Round 363 applies the confined-bridge inward-free/returning split to the
tenth confined bridge family left by Round 362:
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At the fixed bridge cutoff
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 362 finite ladder replaces the confined bridge
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the corresponding inward-free bridge sum plus the new bridge-return spread
sum.  The adjacent tenth return-spread family, ninth bridge-return family,
older return-spread and bridge-return families, and long-run terms are
retained.

The radial-tail and subdivision criteria now use the tenth inward-free bridge
family and the new tenth bridge-return spread family.  The next internal move
is to absorb the tenth inward-free bridge family into a deeper prefix-record
profile plus a long-run contribution, paralleling Round 358.

## Round 364 tenth inward-free bridges absorb into prefix records

Round 364 applies the inward-free-bridge chain/long-run alternative to the
tenth inward-free bridge family left by Round 363:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At cutoff
\[
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the short-chain branch is absorbed by the prefix-record profile
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j},
\]
while the other branch contributes \(W_{\beta_i,p}T_{i,j}^{\rm long}\).
After summing over the finite \(h\)-range, the new fixed prefix-record
coefficient is
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
and the long-run coefficient is incremented by this same fixed quantity.

The tenth bridge-return spread family, adjacent tenth return-spread family,
ninth bridge-return family, older return-spread and bridge-return families,
and exact-level return terms are retained.  The radial-tail and subdivision
criteria now use the tenth prefix-record profile.  The next internal move is
to split this prefix-record family into a persistent-prefix family plus
adjacent return-spread profiles, paralleling Round 359.

## Round 365 tenth prefix records split to persistent prefixes

Round 365 applies the short prefix-record spread/persistent-return split to
the tenth prefix-record family left by Round 364:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives a persistent-prefix profile at cutoff \(2K\) and two adjacent
return-spread profiles at cutoff \(4K\):
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]

Substitution into the Round 364 finite ladder replaces the tenth
prefix-record sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the eleventh persistent-prefix sum plus two adjacent eleventh return-spread
sums.  The tenth bridge-return spread family, adjacent tenth return-spread
family, ninth bridge-return family, older return-spread and bridge-return
families, and long-run terms are retained.

The radial-tail and subdivision criteria now use the eleventh persistent
prefix family and the new eleventh return-spread family.  The next internal
move is to convert this persistent-prefix family into a bounded-gap
prefix-pair family, paralleling Round 360.

## Round 366 eleventh persistent prefixes become bounded-gap pairs

Round 366 applies the ordered-ladder and bounded-successor reductions to the
eleventh persistent-prefix family left by Round 365:
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With persistent cutoff
\[
  4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the bounded successor cutoff is
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  \right\rceil+1,
\]
and
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]

Substitution into the Round 365 finite ladder replaces the eleventh
persistent-prefix sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the bounded-gap prefix-pair sum.  The eleventh adjacent return-spread
family, tenth bridge-return spread family, adjacent tenth return-spread
family, older return-spread and bridge-return families, and long-run terms
are retained.

The radial-tail and subdivision criteria now use the eleventh bounded-gap
prefix-pair family.  The next internal move is to split this bounded-gap
family by the actual successor gap, paralleling Round 361.

## Round 367 eleventh bounded-gap pairs split by fixed gap

Round 367 applies the bounded-gap-to-fixed-gap split to the eleventh
bounded-gap prefix-pair family left by Round 366:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With
\[
  K=8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the fixed-gap cutoff is
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
and
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 366 finite ladder replaces the bounded-gap pair
term under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the finite fixed-gap sum under the same coefficient.  The eleventh
adjacent return-spread family, tenth bridge-return spread family, adjacent
tenth return-spread family, older return-spread and bridge-return families,
and long-run terms are retained.

The radial-tail and subdivision criteria now use the eleventh fixed-gap
prefix-pair family.  The next internal move is to project this fixed-gap
family to confined fixed-gap bridge profiles, paralleling Round 362.

## Round 368 eleventh fixed-gap pairs project to confined bridges

Round 368 applies the fixed-gap pair-to-confined-bridge reduction to the
eleventh fixed-gap prefix-pair family left by Round 367:
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At the fixed product cutoff
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the reduction gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 367 finite ladder replaces the fixed-gap pair sum
under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the corresponding confined bridge sum.  The eleventh adjacent
return-spread family, tenth bridge-return spread family, adjacent tenth
return-spread family, older return-spread and bridge-return families, and
long-run terms are retained.

The radial-tail and subdivision criteria now use the eleventh confined bridge
family.  The next internal move is to split that confined bridge family into
an inward-free bridge family plus a bridge-return spread family, paralleling
Round 363.

## Round 369 eleventh confined bridges split inward-free/returning

Round 369 applies the confined-bridge inward-free/returning split to the
eleventh confined bridge family left by Round 368:
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At the fixed bridge cutoff
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 368 finite ladder replaces the confined bridge
sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the corresponding inward-free bridge sum plus the new bridge-return spread
sum.  The eleventh adjacent return-spread family, tenth bridge-return spread
family, adjacent tenth return-spread family, older return-spread and
bridge-return families, and long-run terms are retained.

The radial-tail and subdivision criteria now use the eleventh inward-free
bridge family and the new eleventh bridge-return spread family.  The next
internal move is to absorb the eleventh inward-free bridge family into a
deeper prefix-record profile plus a long-run contribution, paralleling
Round 364.

## Round 370 eleventh inward-free bridges absorb into prefix records

Round 370 applies the inward-free-bridge chain/long-run alternative to the
eleventh inward-free bridge family left by Round 369:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At cutoff
\[
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the short-chain branch is absorbed by the prefix-record profile
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j},
\]
while the other branch contributes \(W_{\beta_i,p}T_{i,j}^{\rm long}\).
After summing over the finite \(h\)-range, the new fixed prefix-record
coefficient is
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
and the long-run coefficient is incremented by this same fixed quantity.

The eleventh bridge-return spread family, adjacent eleventh return-spread
family, tenth bridge-return spread family, adjacent tenth return-spread
family, older return-spread and bridge-return families, and long-run terms
are retained.  The radial-tail and subdivision criteria now use the eleventh
prefix-record profile.  The next internal move is to split this prefix-record
family into a persistent-prefix family plus adjacent return-spread profiles,
paralleling Round 365.

## Round 371 eleventh prefix records split to persistent prefixes

Round 371 applies the short prefix-record spread/persistent-return split to
the eleventh prefix-record family left by Round 370:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives a persistent-prefix profile at cutoff \(2K\) and two
adjacent return-spread profiles at cutoff \(4K\):
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]

Substitution into the Round 370 finite ladder replaces the eleventh
prefix-record sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the twelfth persistent-prefix sum plus two adjacent twelfth return-spread
sums.  The eleventh bridge-return spread family, adjacent eleventh
return-spread family, tenth bridge-return spread family, adjacent tenth
return-spread family, older return-spread and bridge-return families, and
long-run terms are retained.

The radial-tail and subdivision criteria now use the twelfth persistent
prefix family and the new twelfth return-spread family.  The next internal
move is to convert this persistent-prefix family into a bounded-gap
prefix-pair family, paralleling Round 366.

## Round 372 twelfth persistent prefixes convert to bounded-gap pairs

Round 372 applies the ordered-ladder and bounded-successor reductions to the
twelfth persistent-prefix family left by Round 371:
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
At persistent cutoff
\[
  4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the reductions give the bounded-gap prefix-pair profile
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
with successor-gap cutoff
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  \right\rceil+1.
\]

Substitution into the Round 371 finite ladder replaces the twelfth
persistent-prefix term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the twelfth bounded-gap prefix-pair term.  The twelfth adjacent
return-spread family, eleventh bridge-return spread family, adjacent eleventh
return-spread family, all older spread families, long-run profiles, and
exact-level return terms are retained.

The radial-tail and subdivision criteria now use the twelfth bounded-gap
prefix-pair hypothesis.  The next internal move is to split this bounded-gap
family by the actual successor gap, paralleling Round 367.

## Round 373 twelfth bounded-gap pairs split by fixed successor gap

Round 373 applies the bounded-gap-to-fixed-gap split to the twelfth
bounded-gap prefix-pair family left by Round 372:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With
\[
  K=8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the fixed-gap scale is
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  KB.
\]
Thus
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 372 finite ladder replaces the twelfth
bounded-gap prefix-pair term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by a finite sum over fixed gap \(h\).  The twelfth adjacent return-spread
family, eleventh bridge-return spread family, adjacent eleventh return-spread
family, all older spread families, long-run profiles, and exact-level return
terms are retained.

The radial-tail and subdivision criteria now use the twelfth fixed-gap
prefix-pair hypothesis.  The next internal move is to replace this family by
confined fixed-gap bridge profiles, paralleling Round 368.

## Round 374 twelfth fixed-gap pairs project to confined bridges

Round 374 applies the fixed-gap pair-to-confined-bridge reduction to the
twelfth fixed-gap prefix-pair family left by Round 373:
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At the same fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the reduction gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 373 finite ladder replaces the twelfth fixed-gap
prefix-pair term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the twelfth confined bridge term.  The twelfth adjacent return-spread
family, eleventh bridge-return spread family, adjacent eleventh return-spread
family, all older spread families, long-run profiles, and exact-level return
terms are retained.

The radial-tail and subdivision criteria now use the twelfth confined bridge
hypothesis.  The next internal move is to split this confined bridge family
into inward-free bridge and bridge-return alternatives, paralleling Round 369.

## Round 375 twelfth confined bridges split to inward-free bridges

Round 375 applies the confined-bridge inward-free/returning split to the
twelfth confined bridge family left by Round 374:
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le&\;
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\\
  &+
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\end{aligned}
\]

Substitution into the Round 374 finite ladder replaces the twelfth confined
bridge term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the twelfth inward-free bridge term plus the twelfth bridge-return spread
term.  The twelfth adjacent return-spread family, eleventh bridge-return
spread family, adjacent eleventh return-spread family, all older spread
families, long-run profiles, and exact-level return terms are retained.

The radial-tail and subdivision criteria now use the twelfth inward-free
bridge and bridge-return hypotheses.  The next internal move is to absorb the
twelfth inward-free bridge family into a deeper prefix-record profile plus a
long-run contribution, paralleling Round 370.

## Round 376 twelfth inward-free bridges absorb into prefix records

Round 376 applies the inward-free-bridge chain/long-run alternative to the
twelfth inward-free bridge family left by Round 375:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At cutoff
\[
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the short-chain branch is absorbed by the prefix-record profile
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j},
\]
while the other branch contributes \(W_{\beta_i,p}T_{i,j}^{\rm long}\).
After summing over the finite \(h\)-range, the new fixed prefix-record
coefficient is
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
and the long-run coefficient is incremented by this same fixed quantity.

The twelfth bridge-return spread family, adjacent twelfth return-spread
family, eleventh bridge-return spread family, adjacent eleventh return-spread
family, older return-spread and bridge-return families, and long-run terms
are retained.  The radial-tail and subdivision criteria now use the twelfth
prefix-record profile.  The next internal move is to split this prefix-record
family into a persistent-prefix family plus adjacent return-spread profiles,
paralleling Round 371.

## Round 377 twelfth prefix records split to persistent prefixes

Round 377 applies the short prefix-record spread/persistent-return split to
the twelfth prefix-record family left by Round 376:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
At base scale
\[
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]

Substitution into the Round 376 finite ladder replaces the twelfth
prefix-record term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the thirteenth persistent-prefix term and two adjacent thirteenth
return-spread terms.  No long-run coefficient changes in this split.

The radial-tail and subdivision criteria now use the thirteenth persistent
prefix and adjacent return-spread hypotheses.  The next internal move is to
convert the thirteenth persistent-prefix family into a bounded-gap prefix-pair
family, paralleling Round 372.

## Round 378 thirteenth persistent prefixes become bounded-gap pairs

Round 378 applies the ordered-ladder and bounded-successor reductions to the
thirteenth persistent-prefix family left by Round 377:
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
At persistent cutoff
\[
  4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the reductions give
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
The new bounded-successor cutoff is
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  \right\rceil+1.
\]

Substitution into the Round 377 finite ladder replaces the thirteenth
persistent-prefix term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the thirteenth bounded-gap prefix-pair term.  The adjacent thirteenth
return-spread family and all retained older spread families remain in the
ladder.  The next internal move is to split this bounded-gap family by the
actual successor gap, paralleling Round 373.

## Round 379 thirteenth bounded-gap pairs split by actual gap

Round 379 applies the bounded-gap-to-fixed-gap split to the thirteenth
bounded-gap prefix-pair family left by Round 378:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
as in Round 378, define
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
Then
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 378 finite ladder replaces the thirteenth
bounded-gap prefix-pair term by the finite fixed-gap sum under the same fixed
coefficient.  The adjacent thirteenth return-spread family and all older
retained spread families remain.  The next internal move is to project these
fixed-gap pair profiles to confined fixed-gap bridge profiles, paralleling
Round 374.

## Round 380 thirteenth fixed-gap pairs project to confined bridges

Round 380 applies the fixed-gap pair-to-confined-bridge reduction to the
thirteenth fixed-gap profiles left by Round 379:
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At the fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the reduction gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 379 finite ladder replaces the fixed-gap
prefix-pair term by the confined bridge term under the same fixed coefficient.
The adjacent thirteenth return-spread family and all older retained spread
families remain.  The next internal move is to split the thirteenth confined
bridge family into an inward-free bridge family plus a bridge-return spread
family, paralleling Round 375.

## Round 381 thirteenth confined bridges split to inward-free bridges

Round 381 applies the confined-bridge inward-free/returning split to the
thirteenth confined bridge family left by Round 380:
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le&\;
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\\
  &+
  R^{\rm spr,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\end{aligned}
\]

Substitution into the Round 380 finite ladder replaces the thirteenth
confined bridge term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the thirteenth inward-free bridge term plus the thirteenth bridge-return
spread term.  The adjacent thirteenth return-spread family and all older
retained spread families remain.  The next internal move is to absorb the
thirteenth inward-free bridge family into a deeper prefix-record profile plus
a long-run contribution, paralleling Round 376.

## Round 382 thirteenth inward-free bridges absorb into prefix records

Round 382 applies the inward-free bridge dichotomy and locally-short-chain
absorption to the thirteenth inward-free bridge family left by Round 381:
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
At cutoff
\[
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
and for
\[
  1\le h\le
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the reduction gives
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  W_{\beta_i,p}T_{i,j}^{\rm long}.
\]

Substitution into the Round 381 finite ladder replaces the thirteenth
inward-free bridge sum by a thirteenth prefix-record sum with fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The long-run coefficient is increased by the same fixed amount.  The
thirteenth bridge-return spread family, adjacent thirteenth return-spread
family, and all older retained spread families remain.  The next internal
move is to split the thirteenth prefix-record family into persistent-prefix
and adjacent return-spread profiles, paralleling Round 377.

## Round 383 thirteenth prefix records split to persistent prefixes

Round 383 applies the short-prefix-record persistent/return split to the
thirteenth prefix-record family left by Round 382:
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With
\[
  K=
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The persistent-prefix and adjacent return-spread cutoffs are respectively
\[
  4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  \quad\text{and}\quad
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 382 finite ladder replaces the thirteenth
prefix-record term by the persistent-prefix term and the two adjacent
fourteenth return-spread terms under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The long-run coefficient is unchanged.  The next internal move is to convert
the persistent-prefix family to a bounded-gap prefix-pair family, paralleling
the previous bounded-gap reduction.

## Round 384 persistent prefixes convert to bounded-gap pairs

Round 384 applies the persistent-prefix ordered-ladder reduction and the
bounded-successor-gap reduction to the thirteenth persistent-prefix family
left by Round 383:
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
The bounded-gap budget is
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  \right\rceil+1.
\]
The resulting bound is
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j},
\]
where the pair profile uses cutoff
\[
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
and the displayed height budget.

Substitution into the Round 383 finite ladder replaces the persistent-prefix
term by the fourteenth bounded-gap prefix-pair term under the unchanged
coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The adjacent fourteenth return-spread family and all older retained spread
families remain.  The next internal move is to split the bounded-gap
prefix-pair family into fixed-gap profiles, paralleling the previous
fixed-gap reduction.

## Round 385 bounded-gap pairs decompose to fixed-gap profiles

Round 385 applies the bounded-gap-to-fixed-gap reduction to the fourteenth
bounded-gap prefix-pair family left by Round 384:
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
With height budget
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
define
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
Then
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 384 finite ladder replaces the bounded-gap
prefix-pair term by the fixed-gap finite sum under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The adjacent fourteenth return-spread family and all older retained spread
families remain.  The next internal move is to project the fixed-gap profiles
to confined bridge profiles, paralleling the previous projection.

## Round 386 fixed-gap profiles project to confined bridges

Round 386 applies the fixed-gap-to-confined-bridge projection to the
fourteenth fixed-gap prefix-pair family left by Round 385:
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
The projection uses the same fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
and the same height range
\[
  1\le h\le
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
Substitution into the Round 385 finite ladder replaces the fixed-gap sum by
the confined-bridge sum under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The adjacent fourteenth return-spread family and all older retained spread
families remain.  The next internal move is to split the confined bridge
profiles into inward-free bridge profiles and the next bridge-return spread
family.

## Round 387 confined bridges split into inward-free bridges

Round 387 applies the confined-bridge dichotomy to the fourteenth confined
bridge profiles left by Round 386:
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
The new inward-free and bridge-return profiles use the doubled threshold
\[
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
and therefore carry fourteen \({\rm recbr}\) markers.  The height range is
unchanged:
\[
  1\le h\le
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
Substitution into the Round 386 finite ladder replaces the confined bridge
sum by the inward-free bridge sum plus the new bridge-return spread sum under
the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The adjacent fourteenth return-spread family and all older retained spread
families remain.  The next internal move is to absorb the inward-free bridge
profiles into a prefix-record family, retaining the new bridge-return spread
family.

## Round 388 inward-free bridges absorb into prefix records

Round 388 applies the inward-free bridge chain/long-run split to the
fourteenth inward-free bridge profiles left by Round 387 and then uses the
locally short staircase-chain-to-prefix-record reduction:
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  +
  W_{\beta_i,p}T_{i,j}^{\rm long}.
\]
The prefix-record profile uses threshold
\[
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
and carries fourteen \({\rm recbr}\) markers.  The finite height sum is
absorbed into a new fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
and the long-run coefficient is increased by this new coefficient.

The fourteenth bridge-return spread family introduced in Round 387 is
retained, as are the adjacent fourteenth return-spread family and all older
retained spread families.  The next internal move is to split the
fourteenth prefix-record profiles into persistent-prefix profiles and the
next adjacent return-spread family.

## Round 389 prefix records split to persistent prefixes

Round 389 applies the short prefix-record persistent/returning split to the
fourteenth prefix-record profiles left by Round 388:
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}.
\]
The split uses
\[
  K=
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
so the persistent-prefix threshold is \(4K_i^{\rm gap,\ldots,ch}\), while
the return-spread threshold is \(8K_i^{\rm gap,\ldots,ch}\).  The persistent
profile carries fourteen \({\rm recbr}\) markers, and the new adjacent
return-spread family carries fifteen.

Substitution into the Round 388 finite ladder keeps the coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
unchanged and retains the fourteenth bridge-return spread family, adjacent
fourteenth return-spread family, and all older retained spread families.  The
next internal move is to convert the persistent-prefix profiles into
bounded-gap prefix-pair profiles.

## Round 390 fifteenth persistent prefixes become bounded-gap pairs

Round 390 applies the persistent-prefix ordered-ladder reduction and the
bounded-successor-gap reduction to the fifteenth persistent-prefix family left
by Round 389:
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
The profile has fourteen \({\rm recbr}\) markers, and the scale inherited from
Round 389 is
\[
  4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The bounded-gap budget is
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1,
\]
with fourteen \({\rm recbr}\) markers in \(B_i\) and thirteen in the gap
cutoff.  The resulting bound is
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j},
\]
where the pair profile uses cutoff
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and the displayed height budget.

Substitution into the Round 389 finite ladder replaces the persistent-prefix
term by the fifteenth bounded-gap prefix-pair term under the unchanged
coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The adjacent fifteenth return-spread family and all older retained spread
families remain.  The next internal move is to split this bounded-gap
prefix-pair family into fixed-gap profiles, paralleling the previous fixed-gap
reduction.

## Round 391 fifteenth bounded-gap pairs split by fixed gap

Round 391 applies the bounded-gap-to-fixed-gap reduction to the fifteenth
bounded-gap prefix-pair family left by Round 390:
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
With height budget
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
define the new fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
Here the new \(K_i\)- and \(B_i\)-superscripts have fourteen \({\rm recbr}\)
markers, and the inherited gap scale has thirteen.  Then
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 390 finite ladder replaces the bounded-gap
prefix-pair term by the finite fixed-gap sum under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The adjacent fifteenth return-spread family and all older retained spread
families remain.  The next internal move is to project the fixed-gap profiles
to confined bridge profiles, paralleling the previous projection.

## Round 392 fifteenth fixed-gap profiles project to confined bridges

Round 392 applies the fixed-gap-to-confined-bridge projection to the fifteenth
fixed-gap prefix-pair family left by Round 391:
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
The fixed-gap scale and height budget are unchanged:
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
  \qquad
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
For each \(i,j,h\),
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 391 finite ladder replaces the fixed-gap
prefix-pair term by the confined bridge term under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The adjacent fifteenth return-spread family and all older retained spread
families remain.  The next internal move is to split the confined bridge
profiles into inward-free bridge profiles and bridge-return spread profiles,
paralleling the previous confined-bridge split.

## Round 393 fifteenth confined bridges split to inward-free bridges

Round 393 applies the confined-bridge inward-free/returning dichotomy to the
fifteenth confined bridge family left by Round 392:
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
For \(1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch}\), the split gives
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
The inward-free bridge and bridge-return spread profiles use cutoff
\[
  2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
with fifteen \({\rm recbr}\) markers in the profile superscripts and fourteen
in the inherited cutoff.

Substitution into the Round 392 finite ladder replaces the confined bridge
sum by the fifteenth inward-free bridge sum plus the fifteenth bridge-return
spread sum under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The adjacent fifteenth return-spread family, fourteenth bridge-return and
adjacent return-spread families, thirteenth retained spread families, older
return-spread and bridge-return families, and long-run profiles remain.  The
radial-tail and subdivision criteria now use the fifteenth inward-free bridge
and fifteenth bridge-return spread hypotheses.  The next internal move is to
absorb the fifteenth inward-free bridge profiles into a deeper prefix-record
family while retaining the new bridge-return spread family.

## Round 394 fifteenth inward-free bridges absorb into prefix records

Round 394 applies the inward-free bridge chain/long-run alternative to the
fifteenth inward-free bridge family left by Round 393:
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
the reduction gives a locally short chain profile at height \(h+1\) plus the
long-run term \(W_{\beta_i,p}T_{i,j}^{\rm long}\).  Since \(h+1\ge2\), the
locally-short-chain-to-prefix-record lemma bounds the chain term by
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]

Substitution into the Round 393 finite ladder replaces the fifteenth
inward-free bridge sum by a fifteenth prefix-record sum with coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  =
  D_{i,\mathrm{old}}^{\rm rec,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
where the new coefficient carries fourteen \({\rm recbr}\) markers, the old
coefficient carries thirteen, and the height budget carries fourteen.  The
same new coefficient is added to the long-run coefficient.  The fifteenth
bridge-return spread family, adjacent fifteenth return-spread family,
fourteenth bridge-return and adjacent return-spread families, older retained
spread families, and exact-level return profiles remain.  The radial-tail and
subdivision criteria now use the fifteenth prefix-record hypothesis in place
of the fifteenth inward-free bridge hypothesis.  The next internal move is to
convert this prefix-record family to a persistent-prefix family while retaining
the spread families.

## Round 395 fifteenth prefix records split to persistent prefixes

Round 395 applies the short prefix-record persistent/returning split to the
fifteenth prefix-record family left by Round 394:
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}.
\end{aligned}
\]
Here the persistent-prefix profile carries fifteen \({\rm recbr}\) markers
and the new adjacent return-spread family carries sixteen.  Substitution into
the Round 394 finite ladder replaces the fifteenth prefix-record term by the
sixteenth persistent-prefix term and the two adjacent sixteenth return-spread
terms under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The fifteenth bridge-return spread family, adjacent fifteenth return-spread
family, older retained spread families, exact-level return terms, and the
long-run coefficient remain.  The radial-tail and subdivision criteria now
use the sixteenth persistent-prefix and adjacent return-spread hypotheses.
The next internal move is to convert the sixteenth persistent-prefix family
into a bounded-gap prefix-pair family.

## Round 396 sixteenth persistent prefixes become bounded-gap pairs

Round 396 applies the ordered-ladder and bounded-successor reductions to the
sixteenth persistent-prefix family left by Round 395:
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
Define
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1,
\]
where the \(B_i\)-superscript carries fifteen \({\rm recbr}\) markers and
the gap cutoff carries fourteen.  Applying the ordered-ladder conversion with
\[
  K=4K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and then the bounded-successor reduction gives
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j},
\]
where the pair profile uses cutoff
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and the new \(B_i\)-budget.

Substitution into the Round 395 finite ladder replaces the sixteenth
persistent-prefix term by the sixteenth bounded-gap prefix-pair term under
the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The adjacent sixteenth return-spread family, fifteenth bridge-return spread
family, adjacent fifteenth return-spread family, older retained spread
families, exact-level return terms, and the long-run coefficient remain.  The
radial-tail and subdivision criteria now use the sixteenth bounded-gap
prefix-pair hypothesis while retaining the sixteenth adjacent return-spread
hypotheses.  The next internal move is to split the sixteenth bounded-gap
prefix-pair family into fixed-gap profiles.

## Round 397 sixteenth bounded-gap pairs split into fixed gaps

Round 397 applies the bounded-gap-to-fixed-gap reduction to the sixteenth
bounded-gap prefix-pair family left by Round 396:
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
Define
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
where the new \(K_i\)- and \(B_i\)-superscripts carry fifteen
\({\rm recbr}\) markers and the inherited gap cutoff carries fourteen.  Then
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 396 finite ladder replaces the sixteenth
bounded-gap prefix-pair term by the finite fixed-gap sum under the unchanged
coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The adjacent sixteenth return-spread family, fifteenth bridge-return spread
family, adjacent fifteenth return-spread family, older retained spread
families, exact-level return terms, and the long-run coefficient remain.  The
radial-tail and subdivision criteria now use the sixteenth fixed-gap profile
hypotheses while retaining the sixteenth adjacent return-spread hypotheses.
The next internal move is to project the sixteenth fixed-gap profiles to
confined fixed-gap bridge profiles.

## Round 398 sixteenth fixed gaps project to confined bridges

Round 398 applies the fixed-gap-to-confined-bridge projection to the
sixteenth fixed-gap prefix-pair family left by Round 397:
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
With the fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and the finite height range
\[
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
the confined-bridge projection gives
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 397 finite ladder replaces the sixteenth
fixed-gap prefix-pair term by the finite confined bridge sum under the
unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The height range, fixed-gap scale, adjacent sixteenth return-spread family,
fifteenth bridge-return spread family, adjacent fifteenth return-spread
family, older retained spread families, exact-level return terms, and the
long-run coefficient remain.  The radial-tail and subdivision criteria now
use the sixteenth confined bridge profile hypotheses while retaining the
sixteenth adjacent return-spread hypotheses.  The next internal move is to
split the sixteenth confined bridge profiles into inward-free bridge profiles
plus the next bridge-return spread family.

## Round 399 sixteenth confined bridges split

Round 399 applies the confined-bridge inward-free/returning dichotomy to the
sixteenth confined bridge family left by Round 398:
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
With the confined bridge scale
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and the finite height range
\[
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
the dichotomy gives
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
The new profiles use doubled cutoff
\[
  2K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and carry sixteen \({\rm recbr}\) markers, while the inherited scale and
height budget carry fifteen.

Substitution into the Round 398 finite ladder replaces the sixteenth confined
bridge term by two finite sums over the same \(h\)-range: the sixteenth
inward-free bridge profiles and the sixteenth bridge-return spread profiles.
The coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
\]
is unchanged.  The adjacent sixteenth return-spread family, fifteenth
bridge-return spread family, adjacent fifteenth return-spread family, older
retained spread families, exact-level return terms, and the long-run
coefficient remain.  The radial-tail and subdivision criteria now use the
sixteenth inward-free bridge and sixteenth bridge-return spread hypotheses.
The next internal move is to absorb the sixteenth inward-free bridge profiles
into prefix-record profiles while retaining the new bridge-return spread
family.

## Round 400 sixteenth inward-free bridges absorb into prefix records

Round 400 applies the inward-free bridge chain/long-run alternative to the
sixteenth inward-free bridge family left by Round 399:
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
the reduction gives a locally short chain profile at height \(h+1\) plus the
long-run term \(W_{\beta_i,p}T_{i,j}^{\rm long}\).  Since \(h+1\ge2\), the
locally-short-chain-to-prefix-record lemma bounds the chain term by
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]

Substitution into the Round 399 finite ladder replaces the sixteenth
inward-free bridge sum by a sixteenth prefix-record sum with coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  =
  D_{i,\mathrm{old}}^{\rm rec,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
where the new coefficient carries fifteen \({\rm recbr}\) markers, the old
coefficient carries fourteen, and the height budget carries fifteen.  The
same new coefficient is added to the long-run coefficient.  The sixteenth
bridge-return spread family, adjacent sixteenth return-spread family,
fifteenth retained spread families, exact-level return terms, and older
retained families remain.  The radial-tail and subdivision criteria now use
the sixteenth prefix-record hypothesis in place of the sixteenth inward-free
bridge hypothesis.  The next internal move is to convert this prefix-record
family to a persistent-prefix family while retaining the spread families.

## Round 401 sixteenth prefix records split to persistent prefixes

Round 401 applies the short prefix-record persistent/returning split to the
sixteenth prefix-record family left by Round 400:
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The persistent-prefix cutoff is
\[
  4K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
and the new adjacent return-spread cutoff is
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}.
\]
The persistent-prefix profile carries sixteen \({\rm recbr}\) markers, while
the new adjacent return-spread family carries seventeen.

Substitution into the Round 400 finite ladder replaces the prefix-record term
under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
\]
by the persistent-prefix term and the two adjacent seventeenth return-spread
terms.  The sixteenth bridge-return spread family, adjacent sixteenth
return-spread family, fifteenth retained spread families, exact-level return
terms, older retained families, and long-run coefficient remain.  The
radial-tail and subdivision criteria now use the persistent-prefix and
seventeenth adjacent return-spread hypotheses.  The next internal move is to
convert this persistent-prefix family into a bounded-gap prefix-pair family.

## Round 402 seventeenth persistent prefixes become bounded-gap pairs

Round 402 applies the persistent-prefix ordered-ladder reduction and the
bounded-successor-gap reduction to the persistent-prefix family left by
Round 401:
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
In preparing this reduction, the Round 401 \(P^{\rm per16}\) displayed
profile was corrected to preserve the bridge-record marker depth of the
Round 400 \(P^{\rm rec16}\) profile.
With
\[
  K=4K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
the bounded-successor reduction produces the fixed budget
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1
\]
and gives
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
The bounded-gap pair profile uses cutoff
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and the new \(B_i\)-budget.

Substitution into the Round 401 finite ladder replaces only the
persistent-prefix term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
\]
by the bounded-gap prefix-pair term.  The adjacent seventeenth return-spread
family, sixteenth bridge-return spread family, adjacent sixteenth
return-spread family, fifteenth retained spread families, exact-level return
terms, older retained families, and long-run coefficient remain.  The
radial-tail and subdivision criteria now use the bounded-gap prefix-pair
hypothesis while retaining the seventeenth adjacent return-spread hypotheses.
The next internal move is to split this bounded-gap family into fixed-gap
profiles.

## Round 403 seventeenth bounded-gap pairs split into fixed gaps

Round 403 applies the bounded-gap-to-fixed-gap reduction to the bounded-gap
prefix-pair family left by Round 402:
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
The bounded-gap profile has cutoff
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and finite budget
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
Define the new fixed-gap scale by
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
Then
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 402 finite ladder replaces the bounded-gap
prefix-pair term under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
\]
by the finite fixed-gap sum.  The adjacent seventeenth return-spread family,
sixteenth bridge-return spread family, adjacent sixteenth return-spread
family, fifteenth retained spread families, exact-level return terms, older
retained families, and long-run coefficient remain.  The radial-tail and
subdivision criteria now use the fixed-gap profiles while retaining the
seventeenth adjacent return-spread hypotheses.  The next internal move is to
project the fixed-gap profiles to confined bridge profiles.

## Round 404 seventeenth fixed-gap profiles project to confined bridges

Round 404 applies the fixed-gap-to-confined-bridge reduction to the finite
family left by Round 403:
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h},
  \qquad
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
The confined bridge family is defined at the same fixed scale:
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  =
  \mathfrak P^{G\to H,{\rm rad,tan,pre,out,per,bridge,short}}_
  {Q,\lambda_i,\sigma_i,\beta_i,j,
   K_i^{\rm gap,br,recbr,\ldots,recbr,ch},L_i,h}.
\]
For each finite \(i,j,h\),
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 403 finite ladder replaces the finite fixed-gap
sum under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
\]
by the finite confined bridge sum.  The adjacent seventeenth return-spread
family, sixteenth bridge-return spread family, adjacent sixteenth
return-spread family, fifteenth retained spread families, exact-level return
terms, older retained families, and long-run coefficient remain.  The
radial-tail and subdivision criteria now use the confined bridge profiles
while retaining the seventeenth adjacent return-spread hypotheses.  The next
internal move is to split these confined bridge profiles into inward-free
bridge profiles and bridge-return spread profiles.

## Round 405 seventeenth confined bridges split by inward freedom

Round 405 applies the confined-bridge dichotomy to the finite family left by
Round 404:
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
At the same finite \(h\)-range, define the inward-free bridge profiles
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
\]
and the new bridge-return spread profiles
\[
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
Then
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 404 finite ladder replaces the confined bridge
sum under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
\]
by the inward-free bridge sum plus the new seventeenth bridge-return spread
sum.  The adjacent seventeenth return-spread family, sixteenth bridge-return
spread family, adjacent sixteenth return-spread family, fifteenth retained
spread families, exact-level return terms, older retained families, and
long-run coefficient remain.  The radial-tail and subdivision criteria now
use the inward-free bridge and new bridge-return profiles while retaining the
seventeenth adjacent return-spread hypotheses.  The next internal move is to
absorb the seventeenth inward-free bridge profiles into record profiles.

## Round 406 seventeenth inward-free bridges absorb into records

Round 406 applies the inward-free bridge reduction to the finite family left
by Round 405:
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
For each finite \(h\), the inward-free profile is bounded by a locally short
staircase-chain profile of length \(h+1\) plus a long-run term:
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,stair,loc,chain}_{i,j,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the staircase-chain term is absorbed by the prefix-record
profile
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]

The finite \(h\)-range is absorbed into the new coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
  =
  D_i^{\rm rec,br,recbr,\ldots,ch}
  B_i^{\rm br,recbr,\ldots,ch},
\]
and the same new coefficient is added to the long-run coefficient.  The
finite-ladder, radial-tail, and subdivision criteria now use the seventeenth
record-absorbed formulation.  The seventeenth bridge-return spread family,
adjacent seventeenth return-spread family, sixteenth retained spread
families, exact-level return terms, older retained families, and long-run
coefficient remain under their updated notation.  The next internal move is
to split the new prefix-record profiles into persistent prefixes plus
adjacent return-spread profiles.

## Round 407 seventeenth prefix records split to persistent prefixes

Round 407 applies the short prefix-record persistent/returning split to the
seventeenth prefix-record family left by Round 406:
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The persistent-prefix cutoff is \(4K_i^{\rm gap,br,\ldots,ch}\), and the
new adjacent return-spread cutoff is \(8K_i^{\rm gap,br,\ldots,ch}\).

Substitution into the Round 406 finite ladder replaces the prefix-record
term under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
\]
by the persistent-prefix term and two adjacent eighteenth return-spread
terms.  No long-run coefficient changes in this split.  The radial-tail and
subdivision criteria now use the eighteenth persistent formulation.  The next
internal move is to convert this persistent-prefix family into a bounded-gap
prefix-pair family.

## Round 408 eighteenth persistent prefixes become bounded-gap pairs

Round 408 applies the ordered persistent-prefix ladder reduction and the
bounded-successor-gap reduction to the eighteenth persistent-prefix family
left by Round 407:
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
The ordered-ladder cutoff is
\[
  4K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
and bounded successors give the doubled cutoff
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
with fixed range
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1.
\]
Substitution into the Round 407 finite ladder replaces only the
persistent-prefix term
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
  \sum_j P_{i,j}^{\rm per17}
\]
by the bounded-gap prefix-pair term
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
  \sum_j P_{i,j}^{\rm pair18}.
\]
The adjacent eighteenth return-spread family and all retained bridge-return,
return-spread, long-run, enlarged spread-return, and exact-level return terms
remain.  No long-run coefficient changes.  The next internal move is to split
the bounded-gap prefix-pair family into a finite sum over fixed successor
gaps.

## Round 409 eighteenth bounded-gap pairs split into fixed gaps

Round 409 applies the bounded-gap-to-fixed-gap reduction to the eighteenth
bounded-gap prefix-pair family left by Round 408:
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
For the finite range
\[
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
the fixed-gap scale is
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
Thus
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
Substitution into the Round 408 finite ladder replaces only the bounded-gap
term
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
  \sum_j P_{i,j}^{\rm pair18}
\]
by the finite fixed-gap sum under the same coefficient.  The adjacent
eighteenth return-spread family and all retained bridge-return, return-spread,
long-run, enlarged spread-return, and exact-level return terms remain.  The
next internal move is to project the fixed-gap profiles to confined bridge
profiles.

## Round 410 eighteenth fixed-gap profiles project to confined bridges

Round 410 applies the fixed-gap-to-confined-bridge reduction to the
eighteenth fixed-gap prefix-pair profiles left by Round 409:
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
For the same finite range
\[
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
and the same fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
define
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  =
  \mathfrak P^{G\to H,{\rm rad,tan,pre,out,per,bridge,short}}_
  {Q,\lambda_i,\sigma_i,\beta_i,j,
   K_i^{\rm gap,br,recbr,\ldots,recbr,ch},L_i,h}.
\]
Then, for every finite \(i,j,h\),
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
Substitution into the Round 409 finite ladder replaces only the fixed-gap
sum under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}.
\]
The \(h\)-range, fixed-gap scale, adjacent eighteenth return-spread family,
seventeenth bridge-return and adjacent return-spread families, all retained
older spread families, long-run profiles, enlarged spread-return profiles,
and exact-level return terms remain.  The radial-tail and subdivision
criteria now use the eighteenth confined bridge formulation.  The next
internal move is to split these confined bridge profiles into inward-free
bridge profiles plus bridge-return spread profiles.

## Round 411 eighteenth confined bridges split inward-free or returning

Round 411 applies the confined-bridge inward-free-or-returning reduction to
the eighteenth confined bridge profiles left by Round 410:
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
At the same finite range
\[
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
and using the same fixed-gap scale with a doubled radius in the child
profiles, define
\[
\begin{gathered}
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h},\\
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\end{gathered}
\]
Then, for every finite \(i,j,h\),
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
Substitution into the Round 410 finite ladder replaces only the confined
bridge sum under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}.
\]
The \(h\)-range, fixed-gap scale, adjacent eighteenth return-spread family,
seventeenth bridge-return and adjacent return-spread families, all retained
older spread families, long-run profiles, enlarged spread-return profiles,
and exact-level return terms remain.  The radial-tail and subdivision
criteria now use the eighteenth inward-free bridge formulation together with
the new eighteenth bridge-return spread profiles.  The next internal move is
to absorb the inward-free bridge profiles into prefix-record profiles and
update the long-run coefficient.

## Round 412 eighteenth inward-free bridges absorb into records

Round 412 applies the inward-free bridge chain/long-run reduction to the
eighteenth inward-free bridge profiles left by Round 411:
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
At the same finite \(h\)-range, define the prefix-record profile
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
\]
at scale \(2K_i^{\rm gap,br,recbr,\ldots,recbr,ch}\).  For every finite
\(i,j,h\),
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  +
  W_{\beta_i,p}T_{i,j}^{\rm long}.
\]
The locally short staircase-chain term is absorbed by the prefix-record
profile with length \(h+1\).

Substitution into the Round 411 finite ladder replaces the inward-free bridge
sum by a prefix-record sum with new coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,\ldots,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
and updates the long-run coefficient by
\[
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
  =
  A_i^{\rm long,br,recbr,\ldots,ch}
  +
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The eighteenth bridge-return spread profiles, adjacent eighteenth
return-spread family, all retained older bridge-return and return-spread
families, enlarged spread-return profiles, exact-level return terms, and
finite \(h\)-range remain.  The radial-tail and subdivision criteria now use
the eighteenth prefix-record formulation.  The next internal move is to split
these prefix-record profiles into persistent-prefix profiles plus adjacent
return-spread profiles.

## Round 413 eighteenth records split into nineteenth persistent prefixes

Round 413 applies the short prefix-record spread/persistent-return split to
the eighteenth prefix-record profiles left by Round 412:
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
With
\[
  K=2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
the split gives, for every finite \(i,j\),
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}.
\]
The persistent-prefix scale is \(4K_i^{\rm gap,br,recbr,\ldots,ch}\), and
the new adjacent return-spread scale is
\(8K_i^{\rm gap,br,recbr,\ldots,ch}\).

Substitution into the Round 412 finite ladder leaves the coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
\]
and the long-run coefficient unchanged.  The only replaced term is the
eighteenth prefix-record sum; it becomes the persistent-prefix sum plus the
two adjacent nineteenth return-spread sums.

The eighteenth bridge-return spread profiles, adjacent eighteenth
return-spread family, all retained older bridge-return and return-spread
families, enlarged spread-return profiles, exact-level return terms, and
finite cutoffs remain.  The radial-tail and subdivision criteria now use the
nineteenth persistent-prefix formulation.  The next internal move is to
convert these persistent-prefix profiles into bounded-gap prefix-pair
profiles for the next cycle.

## Round 414 nineteenth persistent prefixes convert to bounded-gap prefix pairs

Round 414 applies the persistent-prefix ordered-ladder reduction followed by
the bounded-successor-gap reduction to the nineteenth persistent-prefix
profiles left by Round 413:
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
With persistent-prefix scale
\[
  4K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
the bounded-successor reduction doubles the scale and introduces the fixed
cutoff
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\Theta_i}
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1 .
\]
Thus, for every finite \(i,j\),
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]

Substitution into the Round 413 finite ladder replaces the nineteenth
persistent-prefix sum by the nineteenth bounded-gap prefix-pair sum under the
same coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}.
\]
No long-run coefficient changes.  The adjacent nineteenth return-spread
family, eighteenth bridge-return and adjacent return-spread families, all
retained older spread families, enlarged spread-return profiles, exact-level
return terms, and finite cutoffs remain.  The radial-tail and subdivision
criteria now use the nineteenth bounded-gap prefix-pair formulation.  The next
internal move is to split this bounded-gap family into finite fixed-gap
prefix-pair profiles.

## Round 415 nineteenth bounded-gap pairs split by fixed gap

Round 415 applies the bounded-gap pair fixed-gap reduction to the nineteenth
bounded-gap prefix-pair family left by Round 414:
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
With
\[
  K=
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \qquad\text{and}\qquad
  B=B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
the fixed-gap scale is
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}=KB.
\]
Thus, for every finite \(i,j\),
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 414 finite ladder replaces the nineteenth
bounded-gap prefix-pair sum by this finite fixed-gap sum under the same
coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}.
\]
No long-run coefficient changes.  The adjacent nineteenth return-spread
family, eighteenth bridge-return and adjacent return-spread families, all
retained older spread families, enlarged spread-return profiles, exact-level
return terms, and finite cutoffs remain.  The radial-tail and subdivision
criteria now use the nineteenth fixed-gap prefix-pair formulation.  The next
internal move is to project these fixed-gap profiles to confined bridge
profiles.

## Round 416 nineteenth fixed-gap pairs project to confined bridges

Round 416 applies the fixed-gap pair-to-confined-bridge reduction to the
nineteenth fixed-gap prefix-pair profiles left by Round 415:
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
For every finite \(i,j,h\) in the retained range,
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 415 finite ladder replaces the nineteenth
fixed-gap prefix-pair sum by the nineteenth confined bridge sum under the same
coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}.
\]
No long-run coefficient changes, and the finite \(h\)-range is unchanged.
The adjacent nineteenth return-spread family, eighteenth bridge-return and
adjacent return-spread families, all retained older spread families, enlarged
spread-return profiles, exact-level return terms, and finite cutoffs remain.
The radial-tail and subdivision criteria now use the nineteenth confined
bridge formulation.  The next internal move is to split these confined bridge
profiles into inward-free bridge profiles plus bridge-return spread profiles.

## Round 417 nineteenth confined bridges split inward-free or returning

Round 417 applies the confined-bridge inward-free-or-returning reduction to
the nineteenth confined bridge profiles left by Round 416:
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
At the same finite range
\[
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
and using the same fixed-gap scale with a doubled radius in the child
profiles, define
\[
\begin{gathered}
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h},\\
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\end{gathered}
\]
Then, for every finite \(i,j,h\),
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 416 finite ladder replaces only the confined
bridge sum under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}.
\]
The \(h\)-range, fixed-gap scale, adjacent nineteenth return-spread family,
eighteenth bridge-return and adjacent return-spread families, all retained
older spread families, long-run profiles, enlarged spread-return profiles,
and exact-level return terms remain.  The radial-tail and subdivision
criteria now use the nineteenth inward-free bridge formulation together with
the new nineteenth bridge-return spread profiles.  The next internal move is
to absorb the inward-free bridge profiles into prefix-record profiles and
update the long-run coefficient.

## Round 418 nineteenth inward-free bridges absorb into records

Round 418 absorbs the nineteenth inward-free bridge profiles left by Round
417 into prefix-record profiles and a long-run term.  At the same finite
\(h\)-range, the inward-free bridge chain/long-run alternative gives
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j},
\]
where the prefix-record profile is evaluated at the doubled fixed-gap scale.

Substitution into the Round 417 finite ladder replaces the finite
inward-free bridge sum by a prefix-record contribution with coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,\ldots,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
and updates the long-run coefficient by adding this same new fixed
coefficient.  The nineteenth bridge-return spread profiles, adjacent
nineteenth return-spread family, eighteenth retained spread families, older
retained families, enlarged spread-return profiles, exact-level return terms,
and all finite cutoffs remain.  The next internal move is to split the
prefix-record profiles into persistent-prefix profiles plus adjacent
return-spread profiles.

## Round 419 nineteenth records split into persistent prefixes

Round 419 applies the short prefix-record persistent/returning split to the
nineteenth prefix-record profiles left by Round 418.  With
\[
  K=2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
the split gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The persistent-prefix profile uses scale
\[
  4K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
and the adjacent return-spread profile is placed at radius
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}.
\]
The coefficient and long-run coefficient are unchanged in this split.  The
next internal move is to convert the persistent-prefix profiles into
bounded-gap prefix-pair profiles.

## Round 420 nineteenth persistent prefixes convert to bounded-gap pairs

Round 420 applies the ordered persistent-prefix ladder and
bounded-successor-gap reductions to the nineteenth persistent-prefix family
left by Round 419:
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
The bounded-gap profile uses scale
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and the finite budget
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\Theta_i}
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1 .
\]
Substitution replaces only the persistent-prefix contribution by the
bounded-gap prefix-pair contribution under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
No return-spread, bridge-return, or long-run term is created by this local
step.  The next internal move is to split the bounded-gap prefix-pair family
into finite fixed-gap profiles.

## Round 421 nineteenth bounded-gap pairs split by fixed gap

Round 421 applies the bounded-gap-to-fixed-gap reduction to the nineteenth
bounded-gap prefix-pair family left by Round 420:
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
Let \(K_i^{\rm src}\) denote the inherited Round 420 source scale
\[
  K_i^{\rm src}=K_i^{\rm gap,br,recbr,\ldots,recbr,ch}.
\]
With
\[
  K=
  8K_i^{\rm src},
  \qquad
  B=B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
define the fixed successor-gap scale by
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch;{\rm fix}}=KB.
\]
The fixed-gap profiles then relabel this new scale as
\(K_i^{\rm gap,br,recbr,\ldots,recbr,ch}\), as in the previous ladder
cycles.
Then, for every finite \(i,j\),
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 420 finite ladder replaces only the bounded-gap
prefix-pair contribution by this finite fixed-gap sum.  The coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
\]
and the long-run coefficient
\[
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
\]
are unchanged.  The adjacent nineteenth return-spread family, nineteenth
bridge-return spread family, eighteenth retained spread families, older
retained families, enlarged spread-return profiles, exact-level return terms,
and all finite cutoffs remain.  The radial-tail and subdivision criteria now
use the nineteenth fixed-gap prefix-pair formulation.  The next internal move
is to project these fixed-gap profiles to confined bridge profiles.

## Round 422 nineteenth fixed-gap pairs project to confined bridges

Round 422 applies the fixed-gap-to-confined-bridge reduction to the
nineteenth fixed-gap prefix-pair profiles left by Round 421.  For the same
finite range
\[
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
define
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  =
  \mathfrak P^{G\to H,{\rm rad,tan,pre,out,per,bridge,short}}_
  {Q,\lambda_i,\sigma_i,\beta_i,j,
   K_i^{\rm gap,br,recbr,\ldots,recbr,ch},L_i,h}.
\]
Then, for every finite \(i,j,h\),
\[
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 421 finite ladder replaces only the fixed-gap
sum by the corresponding finite confined-bridge sum under the same
coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The finite \(h\)-range, fixed-gap scale, and long-run coefficient are
unchanged.  The adjacent nineteenth return-spread family, nineteenth
bridge-return spread family, eighteenth retained spread families, older
retained families, enlarged spread-return profiles, exact-level return terms,
and all finite cutoffs remain.  The radial-tail and subdivision criteria now
use the nineteenth confined bridge formulation.  The next internal move is to
split these confined bridge profiles into inward-free bridge profiles plus
bridge-return spread profiles.

## Round 423 nineteenth confined bridges split inward-free or returning

Round 423 applies the confined-bridge inward-free-or-returning dichotomy to
the nineteenth confined bridge profiles left by Round 422.  At the same
finite range
\[
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
and at doubled fixed-gap scale
\[
  2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
define
\[
\begin{gathered}
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h},\\
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\end{gathered}
\]
The bridge-return spread radius is
\[
  2K_i^{\rm gap,br,recbr,\ldots,recbr,ch}\max\{h-1,1\}.
\]
Then, for every finite \(i,j,h\),
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 422 finite ladder replaces the confined bridge
sum by an inward-free bridge sum plus the new bridge-return spread sum under
the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
The finite \(h\)-range and long-run coefficient are unchanged.  The adjacent
nineteenth return-spread family, the earlier nineteenth bridge-return spread
family, eighteenth retained spread families, older retained families,
enlarged spread-return profiles, exact-level return terms, and all finite
cutoffs remain.  The radial-tail and subdivision criteria now use the
nineteenth inward-free bridge and new bridge-return spread formulation.  The
next internal move is to absorb the inward-free bridge profiles into
prefix-record profiles and update the long-run coefficient.

## Round 424 nineteenth inward-free bridges absorb into records

Round 424 applies the inward-free bridge chain/long-run reduction to the
inward-free bridge profiles left by Round 423.  At doubled fixed-gap scale,
define
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  =
  \mathfrak P^{G\to H,{\rm rad,tan,pre,out,rec,short}}_
  {Q,\lambda_i,\sigma_i,\beta_i,j,
   2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},L_i}.
\]
For every finite \(i,j,h\),
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]

Substitution into the Round 423 finite ladder replaces the inward-free bridge
sum by a prefix-record sum with coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
and updates the long-run coefficient by
\[
  A_i^{\rm long,br,recbr,\ldots,recbr,recbr,ch}
  =
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
  +
  D_i^{\rm rec,br,recbr,\ldots,recbr,recbr,ch}.
\]
The bridge-return spread family from Round 423, earlier nineteenth
bridge-return and adjacent return-spread families, eighteenth retained spread
families, older retained families, enlarged spread-return profiles,
exact-level return terms, and all finite cutoffs remain.  The radial-tail and
subdivision criteria now use the prefix-record formulation with one
additional bridge-record marker.  The next internal move is to split these
prefix-record profiles into persistent-prefix profiles plus adjacent
return-spread profiles.

## Round 425 coefficient-scale audit for the bridge-record cycle

Round 425 pauses the formal reduction ladder and extracts the quantitative
descent invariant of one bridge-record cycle.  Let \(K_m,D_m,A_m,B_m\) denote
the current source scale, prefix-record coefficient, long-run coefficient,
and bounded-successor budget at bridge-record depth \(m\).  The bounded-gap
and fixed-gap steps use
\[
  B_m=\left\lceil \frac{64\beta_i}{\Theta_i}K_m\right\rceil+1,
  \qquad
  K_{m+1}=8K_mB_m,
\]
while inward-free absorption updates
\[
  D_{m+1}=D_mB_m,
  \qquad
  A_{m+1}=A_m+D_{m+1}.
\]
Hence
\[
  \frac{D_{m+1}}{K_{m+1}}=\frac{D_m}{8K_m},
\]
and after \(r\) complete cycles,
\[
  \frac{D_{m+r}}{K_{m+r}}=8^{-r}\frac{D_m}{K_m}.
\]
The long-run coefficient satisfies
\[
  \frac{A_{m+1}}{K_{m+1}}
  =
  \frac{A_m}{8K_mB_m}
  +
  \frac{D_m}{8K_m}.
\]

Thus the current ladder contains a real normalized scale gain: the finite
budget \(B_m\) is paid in both coefficient and scale, and the fixed-gap
conversion contributes an extra factor \(8\) in scale.  The program still
does not prove the target theorem until the retained bridge-return,
adjacent-return, and long-run profiles are bounded strongly enough to use
this gain.  The next proof target is a scale-decay lemma showing that the
retained spread families at scale \(K_m\), after summing over \(j\) and the
finite \(h\)-range, decay at least like \(O(K_m^{-1})\), together with a
compatible long-run estimate.

## Round 426 monotonicity obstruction to naive scale decay

Round 426 corrects the naive scale-decay target from Round 425.  The
spread-return event is monotone increasing in its parameter \(K\):
\[
  \mathcal X^{\rm spr}_{j,K,p}
  =
  \left\{
    \#\{u\in A_{j,p}\cap\mathbb N:u\ge1,\mathcal X_{u,0}\}
    >
    \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
  \right\}.
\]
If \(K_1\le K_2\), then the threshold for \(K_1\) is larger, so
\[
  \mathcal X^{\rm spr}_{j,K_1,p}
  \subseteq
  \mathcal X^{\rm spr}_{j,K_2,p}
\]
and hence the corresponding property-restricted profile is nondecreasing in
\(K\).  Therefore a bound of the form
\[
  \mathfrak X^{\rm rad,ret,spr}_{j,K}=O(K^{-1})
\]
cannot be justified from the definitions and is not the right target.

The correct parameter is the return-density threshold
\[
  \delta=\theta_{\lambda,\sigma,\beta}/(4K).
\]
A usable spread-return estimate should be a fixed-density exponent bound
\[
  \mathfrak X^{\rm rad,ret,spr}_{j,K}(s,p)
  \le
  D_H^{-(\psi(\delta)+o(1))L_H},
\]
with \(\psi(\delta)>0\) for each fixed \(\delta>0\), together with control of
how \(\psi(\delta)\) degenerates as \(\delta\downarrow0\).  This matters
because bridge-return terms produced at source scale \(K_m\) have parameter
\[
  2K_m\max\{h-1,1\},\qquad 1\le h\le B_m,
\]
which can be comparable to the next fixed-gap scale and therefore to a much
smaller density threshold.

Thus the bridge-record coefficient identity remains useful bookkeeping, but
it is not yet a proof mechanism in the existing logarithmic-exponent
framework, where finite coefficients independent of \(p\) do not affect the
exponent.  The next proof target is a fixed-density spread-return exponent
lemma and a compatible long-run exponent lemma, with explicit dependence on
the density parameter.

## Round 427 entropy cost in fixed-density spread-return estimates

Round 427 identifies the entropy term that any fixed-density spread-return
estimate must beat.  Since
\[
  W_{\beta,p}=\max\{1,\lfloor\beta L_H\rfloor\},
\]
the slab \(A_{j,p}\) contains \(\beta L_H+O(1)\) possible return levels.  For
\[
  \delta=\theta_{\lambda,\sigma,\beta}/(4K),
\]
the spread-return event asks for more than \(\delta L_H\) return levels.
Selecting these levels naively costs
\[
  \log \binom{\beta L_H}{\delta L_H}
  =
  \beta H(\delta/\beta)L_H+o(L_H),
\]
or
\[
  \frac{\beta H(\delta/\beta)}{\log D_H}L_H+o(L_H)
\]
in base \(D_H\).  For small \(\delta\), this entropy is
\[
  \delta\log(\beta/\delta)+O(\delta),
\]
which dominates a merely linear \(c\delta\) saving as
\(\delta\downarrow0\).

Therefore a usable spread-return exponent lemma must either produce a
return-level cost \(a(\delta)\) satisfying
\[
  a(\delta)>\beta H(\delta/\beta)/\log D_H
\]
on the finite density range used by the ladder, or exploit structural
dependencies between exterior returns that reduce the raw binomial entropy.
This gives a sharper next target than Round 426: prove such a density-rate
estimate, or show that the bridge-record descent must stop before it enters
the small-density regime where the entropy barrier dominates.

## Round 428 laminarity of exterior-return intervals

Round 428 records the first structural dependence for the spread-return
profiles.  Exterior-return intervals are laminar.  If \(I=[s,t]\) is an
exterior return through level \(u\) and \(J=[s',t']\) is an exterior return
through level \(v\), then their intervals cannot cross.  For instance, if
\(u\le v\) and \(s<s'<t<t'\), then \(t\in(s',t')\), so the level-\(v\)
interior condition gives \(d(x,v_t)\ge v\), while the level-\(u\) endpoint
condition gives \(d(x,v_t)=u-1\le v-1\), a contradiction.  The other crossing
order is ruled out similarly.

Containment also respects radial order: a higher-level return can be nested
inside a lower-level return, but a lower-level return cannot be strictly
nested inside a higher-level return.  Hence any chosen family of one
exterior-return witness per return level forms a laminar forest ordered by
level.

This does not yet beat the Round 427 entropy barrier, but it replaces the
raw model of independently chosen return levels by a structured laminar
excursion forest.  The next target is to quantify this forest entropy and to
show that many spread-return levels force either a long nested chain of
returns or many disjoint excursions that can be charged separately.

## Round 429 chain-antichain dichotomy for spread returns

Round 429 applies the elementary height-width dichotomy to the laminar return
forest.  If a path has more than
\[
  N=\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
\]
return levels in \(A_{j,p}\), choose one exterior-return interval for each
level.  For any integer \(a\ge2\), either the laminar forest has a nested
chain of length at least \(a\), or some depth class contains at least
\[
  \left\lceil \frac{N}{a-1}\right\rceil
\]
pairwise disjoint return intervals.  Hence
\[
  \mathcal X^{\rm spr}_{j,K,p}
  \subseteq
  \mathcal X^{\rm chain}_{j,K,a,p}
  \cup
  \mathcal X^{\rm disj}_{j,K,a,p}.
\]

The nested-chain alternative should be estimated by nested-annulus or
repeated-backtracking methods.  The disjoint-excursion alternative is the
natural place to try BK/Reimer-style or transfer-factorization estimates,
since the witness intervals are time-disjoint.  This converts the
spread-return exponent problem into two more structured density-rate
problems.

## Round 430 chain-disjoint profile reduction

Round 430 packages the Round 429 dichotomy as a radial-profile inequality.
For \(a\ge2\), define \(\mathcal X^{\rm chain}_{j,K,a,p}\) to be the
existence of nested exterior-return intervals through
\[
  u_1<\cdots<u_a,\qquad u_i\in A_{j,p}\cap\mathbb N,
\]
and define \(\mathcal X^{\rm disj}_{j,K,a,p}\) to be the existence of at
least
\[
  \left\lceil
    \frac{\theta_{\lambda,\sigma,\beta}L_H}{4K(a-1)}
  \right\rceil
\]
pairwise time-disjoint exterior-return intervals through levels in
\(A_{j,p}\).  Let the corresponding property-restricted profiles be denoted
\[
  \mathfrak X^{\rm chain}_{Q,\lambda,\sigma,\beta,j,K,a},
  \qquad
  \mathfrak X^{\rm disj}_{Q,\lambda,\sigma,\beta,j,K,a}.
\]
Then
\[
  \mathfrak X^{G\to H,{\rm rad,ret,spr}}_{Q,\lambda,\sigma,\beta,j,K}
  \le
  \mathfrak X^{\rm chain}_{Q,\lambda,\sigma,\beta,j,K,a}
  +
  \mathfrak X^{\rm disj}_{Q,\lambda,\sigma,\beta,j,K,a}.
\]
This deterministic reduction introduces no \(p\)-dependent coefficient.

## Round 431 defect lower bound and why it is insufficient

Round 431 records that every exterior return contributes a distinct inward
step at its upper level.  Hence if a path has exterior returns through
\(N\) distinct levels, then
\[
  I_x(\gamma)\ge N,\qquad 2I_x(\gamma)+H_x(\gamma)\ge2N.
\]
For the spread-return event this gives
\[
  2I_x(\gamma)+H_x(\gamma)
  >
  \frac{\theta_{\lambda,\sigma,\beta}}{2K}L_H.
\]
But the surrounding far-tail profile already restricts to
\[
  d>\lambda L_H,
\]
and since \(\theta_{\lambda,\sigma,\beta}=\lambda/J_{\sigma,\beta}\), the
spread-return lower bound is at most \(\lambda L_H\) for \(K\ge1\).  Thus the
direct inward-step count does not improve the defect threshold.  The
chain-disjoint reduction must be exploited structurally, by reducing witness
entropy or factorizing time-disjoint excursions, not merely by adding defect.

## Round 432 density loss in the chain-antichain split

Round 432 audits the quantitative limitation of the chain-disjoint reduction.
If
\[
  N=\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H,
\]
then the parameter \(a\ge2\) gives either a nested chain of length \(a\), or
at least \(N/(a-1)\) disjoint exterior-return intervals.  No single choice of
\(a\) makes both lower bounds linear in \(L_H\): fixed \(a\) gives a linear
disjoint branch but only a fixed chain branch; \(a\asymp L_H\) gives a linear
chain branch but only \(O(1)\) disjoint intervals; and the balanced choice
gives only \(O(\sqrt{L_H})\) witnesses.

Thus laminarity plus height-width alone cannot provide an order-\(L_H\)
exponent saving.  The next deterministic target is a density-preserving
refinement, preferably involving chain span.  A nested chain
\[
  u_1<\cdots<u_a
\]
with large span \(u_a-u_1\) forces the outer return to contain a large radial
excursion before returning below its entry level.  A useful future split
would be: linear nested span, linear disjoint returns, or a residual
small-span laminar forest that must have additional structure.

## Round 433 span-root split and residual tree cost

Round 433 makes the span split precise and records its limitation.  For
\(\eta>0\), either some exterior-return interval through level \(u\) contains
a descendant return interval through level \(v\) with
\[
  v-u\ge \eta L_H,
\]
or every root tree in the laminar return forest contains at most
\(\lceil\eta L_H\rceil\) selected return levels.  In the latter case the
number of root intervals is at least
\[
  \left\lceil\frac{N}{\lceil\eta L_H\rceil}\right\rceil,
  \qquad
  N=\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H,
\]
and these root intervals are pairwise time-disjoint.

For fixed \(\eta\), however, this gives only \(O(1)\) disjoint root
excursions.  Thus span alone does not recover a linear-density branch.  The
remaining target is a tree-cost lemma: a laminar return tree with \(m\)
selected return levels in a short radial band should pay a cost growing with
\(m\) or with a weighted sum of parent-child level increments.  This is the
next concrete obstruction in the spread-return program.

## Round 434 corridor model blocks a purely radial tree-cost lemma

Round 434 shows that the tree-cost lemma cannot be purely radial.  In an
annular corridor with two radial rails and one top connector, a self-avoiding
path can go outward from radius \(u-1\) to \(u+m\), cross once, and return
inward on the other rail to radius \(u-1\).  For every
\[
  w\in\{u,\ldots,u+m\},
\]
the subpath between the two visits to radius \(w-1\) is an exterior return
through level \(w\), and all these returns form one nested laminar chain.
The radial cost is only
\[
  I=m+1,\qquad H=1,\qquad 2I+H=2m+3.
\]
Thus laminarity alone gives no hidden superlinear cost.  Any successful
estimate must control the availability of annular corridors or use
percolation-specific factorization, not just radial-word combinatorics.

## Round 435 annular-return kernel target

Round 435 reformulates spread returns through annular kernels.  For
\(a,b\in S_{u-1}(x)\), let \(\mathcal A_u^x(a,b)\) be the event that \(a\)
and \(b\) are connected by an open path whose first and last edges enter
\(S_u(x)\) and whose internal vertices stay outside \(B_{u-1}(x)\).  Define
\[
  R_{p,u}^x(a,b)=\mathbf P_p(\mathcal A_u^x(a,b)).
\]
Time-disjoint exterior-return intervals yield disjoint occurrences of such
annular events after recording their boundary endpoints, so BK/Reimer should
bound them by sums of products of the kernels \(R_{p,u}^x\).

A plausible sufficient estimate is an averaged annular-return contraction,
schematically
\[
  \sup_{x,u}
  \frac{1}{|S_{u-1}(x)|}
  \sum_{a,b\in S_{u-1}(x)}R_{p,u}^x(a,b)
  \le \rho_{\rm ann}<1,
\]
or a weaker density-rate version beating the entropy term from Round 427.
The crude bound \(R_{p,u}^x(a,b)\le\tau_p(a,b)\) is not enough; the useful
object is the killed two-point kernel in the exterior of \(B_{u-1}(x)\).
This reconnects the spread-return obstruction to finite-set escape and
boundary susceptibility estimates.

## Round 436 annular kernels are exterior boundary energies

Round 436 makes the previous connection explicit.  Let
\[
  E_u^+(x)=\{(a,a'):d(x,a)=u-1,\ d(x,a')=u,\ a\sim a'\}
\]
and \(X_u=V\setminus B_{u-1}(x)\).  If \(T_p^{X_u}\) is the killed two-point
operator in \(X_u\), then
\[
  R_{p,u}^x(a,b)
  \le
  p^2
  \sum_{\substack{a':(a,a')\in E_u^+(x)}}
  \sum_{\substack{b':(b,b')\in E_u^+(x)}}
  \tau_p^{X_u}(a',b').
\]
Consequently
\[
  \sum_{a,b\in S_{u-1}(x)}R_{p,u}^x(a,b)
  \le
  p^2\langle \nu_u,T_p^{X_u}\nu_u\rangle,
\]
where \(\nu_u(y)=\#\{a\in S_{u-1}(x):a\sim y\}\) for \(y\in S_u(x)\).

Thus averaged annular-return contraction is a ball-boundary version of the
boundary-energy estimate from the last-exit decomposition.  The spread-return
route has returned to the central analytic obstruction: prove that boundary
mass transported through a killed exterior kernel contracts uniformly in
nonamenable quasi-transitive graphs.

## Round 437 killed-\(L^2\) annular contraction criterion

Round 437 extracts a calibration criterion.  If \(G\) has maximum degree
\(\Delta\), then the boundary multiplicity vector satisfies
\[
  \|\nu_u\|_2^2\le \Delta^2 |S_{u-1}(x)|.
\]
Hence, if
\[
  \|T_p^{X_u}\|_{2\to2}\le C_{\rm kill}
\]
uniformly in \(x,u\), then
\[
  \frac{1}{|S_{u-1}(x)|}
  \sum_{a,b\in S_{u-1}(x)}R_{p,u}^x(a,b)
  \le p^2\Delta^2 C_{\rm kill}.
\]
One-step annular contraction follows if \(p^2\Delta^2C_{\rm kill}<1\).

This criterion is probably too crude and risks circularity, since a strong
killed \(L^2\) bound near \(p_c\) resembles the desired operator conclusion.
The more realistic target is a direct boundary-vector estimate for
\(\langle\nu_u,T_p^{X_u}\nu_u\rangle\), exploiting the special geometry of
balls and exterior domains rather than the full killed operator norm.

## Round 438 profile-compatible annular kernels

Round 438 corrects the annular-kernel target for the radial-profile route.
The spread-return profiles are deterministic \(Q\)-weighted SAW counts, not
percolation connection probabilities.  For an exterior-return subpath
\(\eta\) that starts and ends on \(S_{u-1}(x)\), the outward and inward counts
inside \(\eta\) are equal.  Hence its defect contribution is exactly its
length:
\[
  2I(\eta)+H(\eta)=|\eta|.
\]
Thus the global profile weight factors through the \(Q\)-weighted annular
SAW transfer kernel
\[
  A_{Q,u}^x(a,b)
  =
  \sum_{\eta:a\to b\ {\rm exterior\ return\ through}\ u} Q^{|\eta|}.
\]
The percolation existence kernel \(R_{p,u}^x(a,b)\) is only a probabilistic
analogy: it loses multiplicity and does not upper bound the weighted SAW
count.  Since the criterion uses \(Q=q^2>\pc(G)\), the untruncated generating
function may be infinite or too large.  The correct object is a truncated
annular SAW transfer \(A_{Q,u,\le L}^x\), with \(L\) bounded by the available
defect budget.

## Round 439 endpoint weights block scalar annular averages

Round 439 records that even the corrected \(Q\)-weighted annular transfer
cannot be used only through its scalar average.  After deleting a marked
return interval, the surrounding skeleton generates endpoint weights
\(\alpha,\beta\) on \(S_{u-1}(x)\), and reinserting the interval contributes
\[
  \langle\alpha,A_{Q,u}^x\beta\rangle.
\]
The normalized scalar average
\[
  |S_{u-1}(x)|^{-1}\sum_{a,b}A_{Q,u}^x(a,b)
\]
controls only diffuse endpoint weights.  A skeleton may concentrate prefixes
and suffixes on a small subset of the sphere.  Therefore the live target must
be a Schur/operator transfer estimate, or an endpoint-spread dichotomy: either
the endpoint weights are diffuse enough for an averaged annular estimate, or
their concentration creates a separate congestion/support profile.

## Round 440 truncated annular SAW boundary energy

Round 440 defines the deterministic boundary energy matching the corrected
transfer kernel.  Let
\[
  C_{Q,\le L}^{X_u}(y,z)
  =
  \sum_{\substack{\eta:y\to z,\ \eta\subset X_u\ {\rm SAW}\\|\eta|\le L}}
  Q^{|\eta|},
  \qquad X_u=V\setminus B_{u-1}(x).
\]
Then, with \(\nu_u(y)=\#\{a\in S_{u-1}(x):a\sim y\}\),
\[
  \sum_{a,b\in S_{u-1}(x)}A_{Q,u,\le L}^x(a,b)
  \le
  Q^2\langle\nu_u,C_{Q,\le L-2}^{X_u}\nu_u\rangle.
\]
More generally, for endpoint weights \(f,g\) on \(S_{u-1}(x)\), if
\[
  \widehat f(y)=\sum_{a\sim y,\ a\in S_{u-1}(x)}f(a),
  \qquad
  \widehat g(y)=\sum_{b\sim y,\ b\in S_{u-1}(x)}g(b),
\]
then
\[
  \langle f,A_{Q,u,\le L}^xg\rangle
  \le
  Q^2\langle\widehat f,C_{Q,\le L-2}^{X_u}\widehat g\rangle.
\]
This is now the precise analytic object: a truncated exterior SAW
boundary-vector estimate for the endpoint weights produced by radial-profile
skeletons.  A full \(L^2\) bound would suffice but is likely too strong; the
more plausible route is to combine scalar boundary energy with an
endpoint-spread/congestion split.

## Round 441 endpoint weights reduce to annular cut norms

Round 441 sharpens the endpoint-weight obstruction.  For the truncated
annular transfer matrix \(A=A_{Q,u,\le L}^x\), weighted insertion costs are
\[
  \langle f,Ag\rangle.
\]
Dyadic level-set decomposition of \(f\) and \(g\) reduces this to unweighted
annular cuts
\[
  A(U,V)=\sum_{a\in U}\sum_{b\in V}A(a,b),
  \qquad U,V\subseteq S_{u-1}(x).
\]
Indeed, if \(U_i=\{2^i\le f<2^{i+1}\}\) and
\(V_j=\{2^j\le g<2^{j+1}\}\), then
\[
  \langle f,Ag\rangle
  \le
  4\sum_{i,j}2^{i+j}A(U_i,V_j).
\]
Thus any large weighted annular insertion either comes from endpoint
congestion in the skeleton weights or from a large annular cut between
boundary subsets.  The correct replacement for a scalar average is therefore
a restricted cut-norm estimate for \(A_{Q,u,\le L}^x(U,V)\).

## Round 442 subset boundary energy for annular cuts

Round 442 rewrites those annular cuts as subset boundary energies.  For
\(U,V\subseteq S_{u-1}(x)\), define
\[
  \nu_U(y)=\#\{a\in U:a\sim y\},
  \qquad
  \nu_V(y)=\#\{b\in V:b\sim y\}.
\]
Then
\[
  A_{Q,u,\le L}^x(U,V)
  \le
  Q^2\langle\nu_U,C_{Q,\le L-2}^{X_u}\nu_V\rangle.
\]
The live analytic target is therefore a rate bound
\[
  Q^2\langle\nu_U,C_{Q,\le L}^{X_u}\nu_V\rangle
  \le
  \Phi_Q(L,|U|,|V|,|S_{u-1}(x)|)
\]
for boundary subsets generated by endpoint level sets.  Schur or \(L^2\)
operator bounds would imply this, but the subset-energy formulation is weaker
and provides a sharper inverse problem: failure of spread-return decay should
produce large exterior SAW energy between boundary subsets in many annuli.

## Round 443 raw Schur bounds are too expensive

Round 443 calibrates the corrected annular transfer against the trivial
bounded-degree estimate.  For a fixed \(a\in S_{u-1}(x)\),
\[
  \sum_b A_{Q,u,\le L}^x(a,b)
  \le
  C_\Delta\sum_{\ell=2}^L (Q(\Delta-1))^\ell .
\]
In the subdivision criterion \(Q=q^2>\pc(G)\), while the universal bound
\(\pc(G)\ge(\Delta-1)^{-1}\) gives no reason for \(Q(\Delta-1)<1\).  Thus
the naive Schur row sum can grow exponentially in the truncation length.

Any successful annular-transfer estimate must therefore use structure beyond
ambient degree growth: exact-sphere averaging, the annular cut/subset
formulation, laminar nesting, or graph-specific operator geometry.  This is
the same obstruction seen earlier for unrestricted radial tails, now localized
to return intervals.

## Round 444 root return intervals cover contiguous level blocks

Round 444 improves the deterministic spread-return split.  If
\(I=[s,t]\) is an exterior return through level \(u\) and
\[
  M(I)=\max_{s\le r\le t}d(x,v_r),
\]
then \(I\) generates exterior returns through every level
\[
  w\in\{u,\ldots,M(I)\}.
\]
The reason is that after reaching radius at least \(w\), the interval must
make an inward \(w\to w-1\) step before returning to level \(u-1\); the
inward-token lemma then gives an exterior return through \(w\).

Thus each root interval in the laminar forest has a radial coverage block
\[
  C(I)=[u,M(I)]\cap\mathbb N.
\]
The selected spread-return levels are contained in the union of the root
coverage blocks.  If \(h(I)=|C(I)|\), then the root interval has length and
defect at least \(2h(I)\).  This recasts the entropy problem: few root
intervals mean interval-cover entropy, not arbitrary subset entropy; many
root intervals mean many pairwise time-disjoint annular returns.

## Round 445 coverage-entropy split

Round 445 gives the quantitative form.  Let the slab contain
\(B=\beta L_H+O(1)\) levels and let the spread event require
\(N=\delta L_H+O(1)\) return levels.  If the number \(m\) of root return
intervals is at least \(\kappa L_H\), there are linearly many time-disjoint
root returns, with density \(\kappa\).

If \(m<\kappa L_H\), the selected levels are covered by fewer than
\(\kappa L_H\) intervals in a slab of length \(B\).  Their coverage entropy is
\[
  \exp[\beta H(2\kappa/\beta)L_H+o(L_H)]
\]
for \(2\kappa<\beta\), while the root-span defect contributes at least
\[
  Q^{2N}=\exp[-2\delta|\log Q|L_H+o(L_H)].
\]
Thus the few-root branch can plausibly be paid for whenever
\[
  \beta H(2\kappa/\beta)<2\delta|\log Q|.
\]
For fixed \(\delta>0\), choosing \(\kappa\) small makes this possible.  The
spread-return entropy obstruction is therefore pushed into the many-root
branch, where the corrected annular transfer/cut machinery is the relevant
tool.

## Round 446 coverage-root profile reduction

Round 446 turns the coverage split into a profile inequality.  For an
exterior-return interval \(I\) through level \(u(I)\), define
\[
  C_{j,p}(I)=[u(I),M(I)]\cap A_{j,p}\cap\mathbb N.
\]
Let \(\delta=\theta_{\lambda,\sigma,\beta}/(4K)\).  For \(\kappa>0\), define
\(\mathcal X^{\rm rootdisj}_{j,\kappa,p}\) to be the property that the path
contains at least \(\lceil\kappa L_H\rceil\) pairwise time-disjoint
exterior-return intervals through slab levels.  Define
\(\mathcal X^{\rm cov}_{j,K,\kappa,p}\) to be the property that fewer than
\(\lceil\kappa L_H\rceil\) pairwise time-disjoint exterior-return intervals
have slab coverage blocks whose union has size \(>\delta L_H\).

Then
\[
  \mathcal X^{\rm spr}_{j,K,p}
  \subseteq
  \mathcal X^{\rm rootdisj}_{j,\kappa,p}
  \cup
  \mathcal X^{\rm cov}_{j,K,\kappa,p},
\]
and hence
\[
  \mathfrak X^{\rm rad,ret,spr}_{Q,\lambda,\sigma,\beta,j,K}
  \le
  \mathfrak X^{\rm rootdisj}_{Q,\lambda,\sigma,\beta,j,\kappa}
  +
  \mathfrak X^{\rm cov}_{Q,\lambda,\sigma,\beta,j,K,\kappa}.
\]
This is the current clean deterministic endpoint: a few-root coverage branch
with low interval entropy, and a many-root branch with linearly many
time-disjoint annular returns.

## Round 447 jump-skeleton correction to coverage cost

Round 447 corrects the cost bookkeeping needed for the few-root branch.  When
a root return interval \(I=[s,t]\) is deleted, the remaining object has a gap
from \(v_s\) to \(v_t\), both on the same sphere.  The natural skeleton
therefore has a formal same-sphere jump, charged as one horizontal step.

If \(m\) root intervals are deleted, producing a jump skeleton
\(\gamma^\circ\), then
\[
  d(\gamma^\circ)
  =
  d(\gamma)-\sum_{r=1}^m |I_r|+m.
\]
Since \(|I_r|\ge2h_r\), where \(h_r\) is the radial coverage length,
\[
  d(\gamma)-d(\gamma^\circ)
  \ge
  2\sum_{r=1}^m h_r-m.
\]
In the few-root branch, \(\sum h_r\ge\delta L_H\) and
\(m<\kappa L_H\), so the net gain over the jump skeleton is
\[
  (2\delta-\kappa)L_H+O(1).
\]
Thus the honest entropy-cost condition for a deletion/skeleton proof is
\[
  \beta H(2\kappa/\beta)<(2\delta-\kappa)|\log Q|,
\]
still achievable by taking \(\kappa\) small.  The remaining technical lemma is
to control the resulting same-sphere jump-skeleton profiles without losing a
linear exponent.

## Round 448 jump endpoints cannot be counted as clique edges

Round 448 records a caveat for the jump-skeleton strategy.  If same-sphere
jumps are counted as arbitrary edges in a complete graph on each sphere, the
endpoint entropy per jump can be
\[
  \log |S_u(x)|=O(L_H)
\]
at the relevant radii.  With \(m\le\kappa L_H\) jumps this can cost
\(O(\kappa L_H^2)\), far beyond the \(O(L_H)\) exponent budget.

Therefore jump skeletons cannot be controlled by crude augmented-graph
counting.  The endpoint choices must remain coupled to the annular transfer
kernels.  The few-root coverage split pays only the radial level entropy; the
vertex endpoint entropy still requires the cut/subset boundary-energy
machinery.

## Round 449 current branch obligations after coverage split

Round 449 summarizes the live obligations.  The many-root branch has
\(\kappa L_H\) time-disjoint root return intervals and needs a product
estimate for the corrected annular transfer kernels
\(A_{Q,u,\le L}^x\), with endpoint weights controlled by Schur, \(L^2\), or
subset-cut estimates.

The few-root branch has low radial interval-cover entropy and net defect gain
\((2\delta-\kappa)L_H\) over same-sphere jump skeletons, but Round 448 shows
that vertex endpoints remain dangerous.  It also needs annular transfer/cut
control, now for fewer longer intervals.

Thus the current unified target is an annular cut-energy estimate strong
enough for both linearly many root intervals at density \(\kappa\) and
sublinear/few root intervals with total radial coverage at least
\(\delta L_H\).  Failure of this target should produce boundary subsets
\(U,V\) with anomalously large truncated exterior \(Q\)-weighted SAW energy.

## Round 450 annular cut energy implies restricted SAW operator mass

Round 450 links the annular cut obstruction to SAW operator norms.  Let
\[
  C_\ell^{X_u}(y,z)
  =
  \#\{\eta:y\to z,\ \eta\subset X_u\ {\rm SAW},\ |\eta|=\ell\}.
\]
Since \(C_{Q,\le L}^{X_u}=\sum_{\ell\le L}Q^\ell C_\ell^{X_u}\), a large cut
energy
\[
  E=Q^2\langle\nu_U,C_{Q,\le L}^{X_u}\nu_V\rangle
\]
implies that for some \(\ell\le L\),
\[
  \|C_\ell^{X_u}\|_{2\to2}
  \gtrsim
  \frac{E}{(L+1)Q^{\ell+2}\Delta^2\sqrt{|U||V|}}.
\]
Thus failure of annular cut control produces coherent restricted exterior SAW
operator mass, not merely many paths.

## Round 451 killed SAW operator gap would close annular cuts

Round 451 records the corresponding sufficient condition.  If for some
\(a<1/Q\),
\[
  \|C_\ell^{X_u}\|_{2\to2}\le e^{o(\ell)}a^\ell
\]
uniformly over ball exteriors \(X_u\), then
\[
  A_{Q,u,\le L}^x(U,V)
  \le
  C_Q\sqrt{|U||V|}
\]
for all boundary subsets \(U,V\).  This would give the desired \(L^2\)-type
annular cut estimate.

The condition is close to the global SAW operator-gap route
\(\gamma_{\rm SAW,2}(G)<1/Q\).  The exterior-domain version may be weaker, but
it is still a serious analytic input.  Avoiding it requires exploiting the
special boundary-vector structure of \(\nu_U,\nu_V\), not just bounding the
full killed operator norm.

## Round 452 annular boundary SAW exponent

Round 452 names the boundary-vector exponent
\[
  \Gamma_{\rm ann}(G)
  =
  \limsup_{\ell\to\infty}
  \sup_{x,u,U,V}
  \left(
    \frac{\langle\nu_U,C_\ell^{X_u}\nu_V\rangle}
         {\sqrt{|U||V|}}
  \right)^{1/\ell}.
\]
This is bounded above by the global SAW \(L^2\) growth exponent, but it only
tests killed exterior paths between boundary vectors coming from one sphere.
If
\[
  Q\Gamma_{\rm ann}(G)<1,
\]
then the annular cut estimate
\[
  A_{Q,u,\le L}^x(U,V)\le C_Q\sqrt{|U||V|}
\]
holds uniformly.  On a regular tree, \(\Gamma_{\rm ann}=0\), since ball
exteriors split into disjoint forward cones and nontrivial exterior returns
do not exist.

## Round 453 cut estimates control weighted insertions via endpoint \(L^2\)

Round 453 converts cut control into weighted insertion control.  If
\[
  A_{Q,u,\le L}^x(U,V)\le C\sqrt{|U||V|}
\]
for all boundary subsets, then dyadic decomposition of endpoint weights
\(f,g\) gives
\[
  \langle f,A_{Q,u,\le L}^xg\rangle
  \le
  4C\sqrt{N_fN_g}\,\|f\|_2\|g\|_2,
\]
where \(N_f,N_g\) are the numbers of nonempty dyadic levels.  For skeleton
weights of length \(O(L_H)\), these dyadic counts are \(O(L_H)\), hence
subexponential in the logarithmic scale.  Thus annular cut control reduces
the insertion problem to endpoint \(L^2\) control.

## Round 454 endpoint \(L^2\) is a two-replica congestion profile

Round 454 identifies that remaining \(L^2\) term.  If \(f(a)\) is the
weighted count of skeleton prefixes ending at \(a\in S_{u-1}(x)\), then
\[
  \|f\|_2^2=\sum_a f(a)^2
\]
counts ordered pairs of skeleton prefixes with the same boundary endpoint.
Large endpoint \(L^2\) is therefore a two-replica boundary congestion
profile.  The spread-return branch now separates into a boundary-vector SAW
gap problem for annular transfer and a two-replica endpoint-congestion
problem for skeleton concentration.

## Round 455 endpoint congestion is not automatically finite-set two-replica

Round 455 compares this endpoint \(L^2\) term with the earlier finite-set
two-replica profile.  The earlier object is percolative:
\[
  \mathcal R_p(K)
  =
  \frac{1}{\bar\chi_p|K|}
  \sum_z\left(\sum_{x\in K}\tau_p(x,z)\right)^2.
\]
The new endpoint term has the same algebraic form, but its weights are
deterministic \(Q\)-weighted skeleton counts with \(Q>\pc(G)\), not
near-critical two-point masses.  Thus it is not automatically controlled by
\(\mathcal R_p\).  One must either compare these skeleton counts to
percolation mass, or add a deterministic endpoint two-replica profile.

## Round 456 endpoint \(L^2\) extracts support-congestion sets

Round 456 gives the inverse form.  If \(f\) is a skeleton endpoint weight on a
sphere and \(U_i=\{2^i\le f<2^{i+1}\}\), then some dyadic level set
\(U\) satisfies
\[
  \frac{\left(\sum_{a\in U}f(a)\right)^2}{|U|}
  \ge
  \frac{\|f\|_2^2}{4N_f},
\]
where \(N_f\) is the number of nonempty dyadic levels.  For skeletons of
length \(O(L_H)\), \(N_f=O(L_H)\), so this loses only \(e^{o(L_H)}\).  Hence
endpoint \(L^2\) failure extracts a boundary support-congestion set carrying
large skeleton mass per square-root support.

## Round 457 current reduced obstruction map

Round 457 summarizes the state.  The spread-return profile is reduced to a
few-root coverage branch and a many-root branch.  Both require annular
insertion estimates.  These split into:

1. annular transfer control, for example
   \(\Gamma_{\rm ann}(G)<1/Q\);
2. endpoint \(L^2\) or support-congestion control for deterministic skeleton
   weights;
3. a possible bridge from those deterministic support profiles to the
   percolative finite-set/two-replica machinery.

The remaining obstructions are now localized boundary-vector and
support-congestion statements, not arbitrary return-level entropy.

## Round 458 the annular gap threshold is \(1/p_c\)

Round 458 calibrates the parameter.  In the subdivision route
\[
  Q=q^2,\qquad q>\pc(\operatorname{Sub}(G)),
\]
and \(\pc(\operatorname{Sub}(G))^2=\pc(G)\).  Hence \(Q\) can be chosen
arbitrarily close to \(\pc(G)\) from above.  The useful annular condition is
therefore
\[
  \Gamma_{\rm ann}(G)<1/\pc(G).
\]
This is the boundary-return analogue of the global SAW operator-gap condition
\(\gamma_{\rm SAW,2}(G)<1/\pc(G)\), but it only tests killed exterior
boundary-to-boundary returns.  The raw degree bound cannot prove it, since
\(\Gamma_{\rm ann}\le\Delta-1\) and \(\pc(G)\ge(\Delta-1)^{-1}\) give no
strict gap.

## Round 459 annular gap plus endpoint support is a conditional endpoint theorem

Round 459 packages the current route.  For a fixed spread-return density
\(\delta>0\), choose \(\kappa>0\) with
\[
  \beta H(2\kappa/\beta)<(2\delta-\kappa)|\log Q|.
\]
The coverage-root split pays the few-root radial entropy and leaves the
many-root branch with \(\kappa L_H\) time-disjoint root returns.  If
\[
  \Gamma_{\rm ann}(G)<1/Q,
\]
then annular insertions in both branches are controlled by endpoint \(L^2\)
norms up to \(e^{o(L_H)}\).  If the endpoint support-congestion profiles from
Round 456 also have subcritical logarithmic exponent, the spread-return
profile has the desired fixed-density exponent bound.

Thus the route has a conditional endpoint: annular boundary gap plus
deterministic endpoint support control would close the spread-return branch.

## Round 460 product staircase lower bound for \(\Gamma_{\rm ann}\)

Round 460 stress-tests \(\Gamma_{\rm ann}\) on products
\(T_d\square H\).  Root at \((o,h_0)\), choose a tree vertex \(t\) at depth
\(u-1\), and start from \(a=(t,h_0)\).  After the first outward tree step,
take a geodesic path \(h_0,\ldots,h_k\) in \(H\), alternating one step in
\(H\) with one inward tree step.  The resulting staircase stays outside
\(B_{u-1}(x)\) until it ends at a boundary vertex in \(S_{u-1}(x)\).  Hence
\[
  \Gamma_{\rm ann}(T_d\square H)\ge \sqrt{g_{\rm geo}(H)},
\]
where \(g_{\rm geo}(H)\) is the exponential growth rate of geodesic
self-avoiding paths in \(H\).  The square root appears because \(k\) factor
steps produce a return of length \(2k+O(1)\).

## Round 461 annular product stress is weaker than global SAW stress

Round 461 compares this with the old global product lower bound
\[
  \gamma_{\rm SAW,2}(T_d\square H)\ge\sqrt{d-1}+\mu(H).
\]
The first annular staircase lower bound has no tree-branching term.  Exterior
returns are boundary-to-boundary events, so inward tree movement must be paid
for by factor motion or previous outward motion.  Thus this first diagnostic
does not refute the annular gap
\[
  \Gamma_{\rm ann}(G)<1/\pc(G)
\]
by the standard product obstruction to the global SAW operator route.

## Round 462 product out-and-back lower bound for \(\Gamma_{\rm ann}\)

Round 462 corrects the product calibration.  If \(H\) has an edge, then
\(T_d\square H\) has exterior returns that move outward \(r\) steps in the
tree, shift once in \(H\), and return inward in the shifted fibre.  There are
\((d-1)^r\) choices and the killed exterior length is \(2r+O(1)\).  Therefore
\[
  \Gamma_{\rm ann}(T_d\square H)\ge\sqrt{d-1}.
\]
Together with Round 460,
\[
  \Gamma_{\rm ann}(T_d\square H)
  \ge
  \max\{\sqrt{d-1},\sqrt{g_{\rm geo}(H)}\}.
\]
This is still weaker than the global product lower bound
\(\sqrt{d-1}+\mu(H)\).

## Round 463 product annular gap remains plausible after correction

Round 463 notes that the corrected lower bound still does not contradict the
desired annular gap in tree-product cases.  Since
\[
  \pc(T_d\square H)\le 1/(d-1),
\]
we have \(1/\pc(T_d\square H)\ge d-1>\sqrt{d-1}\).  Thus the tree
out-and-back lower bound stays below the target threshold.  The next
calibration is an upper bound for \(\Gamma_{\rm ann}\) on
\(T_d\square\mathbb Z^r\), ideally via a transfer matrix for the tree and
factor distance pair.

## Round 464 two-layer product is the first annular upper-bound test

Round 464 identifies \(T_d\square K_2\) as the simplest non-tree calibration.
Here
\[
  d((o,0),(v,\epsilon))=d_T(o,v)+\epsilon.
\]
The lower bound from Round 462 gives
\[
  \Gamma_{\rm ann}(T_d\square K_2)\ge\sqrt{d-1}.
\]
Since there is no factor-geodesic growth, any larger value must come from
repeated layer switching while moving in the tree.  The first target is either
\[
  \Gamma_{\rm ann}(T_d\square K_2)=\sqrt{d-1}
\]
or at least the strict bound
\[
  \Gamma_{\rm ann}(T_d\square K_2)<d-1,
\]
which would match \(1/\pc(T_d\square K_2)\ge d-1\).

## Round 465 half-plane transfer overcounts the two-layer product

Round 465 tests the crude radial-excess transfer for \(T_d\square K_2\).
Tracking only
\[
  e=d_T(o,v)+\epsilon-u\ge0
\]
gives upward weight about \(d\) and downward weight about \(2\), hence a
half-plane excursion spectral radius of order \(2\sqrt{2d}\), far too large.
The overcount forgets self-avoidance in each layer.  A useful transfer must
remember stack/spine information: whether an inward tree move retraces a
segment already used in the same layer, and whether a layer switch lands on a
previously used tree vertex.

## Round 466 branch-switch recursion in \(T_d\square K_2\)

Round 466 isolates the principal recursive family.  In a descendant cone of
the rooted tree, let \(S(z)\) count self-avoiding paths from \((v,0)\) to
\((v,1)\) in \(T_d\square K_2\), avoiding the parent of \(v\).  Either the
path switches directly across the rung at \(v\), or it chooses one of
\(q=d-1\) children, switches layers in that child cone, and returns in the
other layer.  Hence
\[
  S(z)=z+qz^2S(z)=\frac{z}{1-qz^2}.
\]
The resulting exponent is \(\sqrt{d-1}\), matching the out-and-back lower
bound.  This does not yet prove the full upper bound for \(\Gamma_{\rm ann}\),
but it identifies the principal return type and suggests a finite/pushdown
recursive system may close the two-layer product calibration.

## Round 467 exterior components in \(T_d\square K_2\) are two-port cones

Round 467 gives the missing component structure.  For root \(x=(o,0)\), the
exterior \(X_u=V\setminus B_{u-1}(x)\) decomposes into components \(C_t\)
indexed by tree vertices \(t\) at depth \(u-1\).  Each \(C_t\) consists of
the layer-\(1\) descendant cone of \(t\) together with the layer-\(0\)
descendant cones of the children of \(t\).  It has only two boundary ports:
\[
  A_t=(t,0),\qquad B_t=(\operatorname{par}(t),1).
\]
Every exterior return through level \(u\) is carried by one such two-port
component.

## Round 468 exact two-port transfer in \(T_d\square K_2\)

Round 468 computes the transfer between the two ports.  With \(q=d-1\) and
\[
  S(z)=\frac{z}{1-qz^2},
\]
the boundary-to-boundary transfer generating function is
\[
  F(z)=z^2+qz^3S(z)
      =z^2+\frac{qz^4}{1-qz^2}.
\]
Thus the transfer coefficients grow exactly like \(q^{n/2}\).  Same-port
transfers are degenerate for self-avoiding annular returns.

## Round 469 exact annular exponent for \(T_d\square K_2\)

Round 469 combines the component decomposition and transfer formula:
\[
  \Gamma_{\rm ann}(T_d\square K_2)=\sqrt{d-1}.
\]
The component incidence contributes only bounded-degree constants.  Since
\[
  \pc(T_d\square K_2)\le 1/(d-1),
\]
this gives the strict annular gap
\[
  \Gamma_{\rm ann}(T_d\square K_2)<1/\pc(T_d\square K_2)
  \qquad(d\ge3).
\]
This is the first exact non-tree calibration of the annular boundary exponent.

## Round 470 finite-fiber tree products reduce to bounded-width transfers

Round 470 abstracts the \(K_2\) calculation to \(T_d\square F\) with \(F\)
finite.  If \(R=\max_f d_F(f_0,f)\), then outside
\(B_{u-1}((o,f_0))\) the components are decorated descendant cones indexed by
tree vertices at depth \(u-R\).  Each component has only \(O_{F,d}(1)\)
boundary ports: descendant-side ports at relative level
\(d_T(a,w)+d_F(f_0,f)=R-1\), and parent-side ports
\((\operatorname{par}(a),f)\) with \(d_F(f_0,f)=R\).
Thus \(\Gamma_{\rm ann}(T_d\square F)\) should be computable from a
finite-state boundary-to-boundary SAW transfer on one rooted decorated cone.
For \(F=K_2\), the transfer is the one-recursion system of Rounds 466--469.
For general finite \(F\), the proof target is a finite matrix or pushdown
transfer with exponent \(\rho_F(d-1)\), to be compared with
\(1/\pc(T_d\square F)\).  The stronger inequality
\(\rho_F(d-1)<d-1\) is a useful low-width sufficient condition, but it is not
the natural target for arbitrary high-entropy finite fibers.

## Round 471 explicit finite-state transfer for \(T_d\square F\)

Round 471 makes the finite-fiber transfer concrete.  View
\(T_d\square F\) as a rooted tree of finite bags, each bag a copy of \(F\).
A transfer state at a bag records the used subset of the bag, degrees
\(0,1,2\), connectivity pairings of open path ends through processed child
cones, and the distinguished boundary terminals when relevant.  The local
transition chooses fiber edges in the bag and child-cone transfers, then
forbids degree \(>2\), premature cycles, and disconnected terminal outputs.

Since the child number is \(q=d-1\) and the bag is finite, the state vector
\(\mathbf G(z)\) satisfies a finite recursive system
\[
  \mathbf G(z)=\Phi_F(z,\mathbf G(z);q)
\]
with nonnegative coefficients.  The relevant annular transfer functions are
selected coordinates or finite linear combinations.  Thus the finite-fiber
case is reduced to proving that the corresponding singularity exponent
\(\rho_F(q)\) obeys
\[
  \rho_F(q)<1/\pc(T_d\square F).
\]
For \(F=K_2\), this system collapses to \(S(z)=z+qz^2S(z)\).

## Round 472 finite-fiber correction: ports and threshold comparison

Round 472 records two corrections to the finite-fiber roadmap.  First,
components in \(T_d\square F\) have both descendant-side ports and
parent-side ports \((\operatorname{par}(a),f)\) with
\(d_F(f_0,f)=R\).  The parent-side port is exactly the \(B_t\) port in the
\(K_2\) calibration, so it cannot be omitted from the transfer.

Second, the natural inequality for finite fibers is
\[
  \rho_F(d-1)<1/\pc(T_d\square F),
\]
not uniformly \(\rho_F(d-1)<d-1\).  The latter remains a strong sufficient
condition and holds for \(K_2\), but high-entropy finite fibers should be
compared with the actual finite-width percolation threshold.

## Round 473 finite-type formula for \(\pc(T_d\square F)\)

Round 473 gives the matching finite percolation object.  For percolation on
\(T_d\square F\), a forward cluster entering a bag has type
\(A\subseteq V(F)\), the nonempty set of fiber coordinates connected inside
the current bag.  From type \(A\), a child bag receives open entries
\(D\subseteq A\) through the tree edges and then closes \(D\) under open
edges of \(F\), yielding a nonempty type \(B\).  This defines a finite kernel
\[
  K_p(A,B)=\mathbb P_p(\operatorname{cl}_F(D)=B),
\]
and the multitype branching mean matrix is
\[
  M_p(A,B)=(d-1)K_p(A,B).
\]
Hence
\[
  \pc(T_d\square F)=\inf\{p:r(M_p)>1\}.
\]
The finite-fiber annular problem is therefore a comparison between the SAW
transfer exponent \(\rho_F(d-1)\) and \(1/p_*\), where \(r(M_{p_*})=1\).

## Round 474 clique-fiber stress test for the strong \(<q\) target

Round 474 tests \(F=K_m\).  The component over a boundary tree vertex \(t\)
has one descendant-side port \((t,0)\) and \(m-1\) parent-side ports
\((\operatorname{par}(t),f)\), \(f\ne0\).  Choose disjoint fiber sets
\(O,I\subseteq\{1,\ldots,m-1\}\), with \(|O|=\alpha\), \(|I|=\beta\).  An
exterior return can go outward along a tree ray while traversing self-avoiding
fiber paths through \(O\) in each bag, switch once at the deepest bag, and
return inward through disjoint fiber paths in \(I\).  This gives
\[
  \Gamma_{\rm ann}(T_d\square K_m)
  \ge
  \max_{\substack{\alpha,\beta\ge2\\ \alpha+\beta\le m-1}}
  \bigl((d-1)(\alpha-2)!(\beta-2)!\bigr)^{1/(\alpha+\beta)}.
\]
For \(\alpha,\beta\asymp m/2\), this lower bound is of order \(m\).  Thus the
strong condition \(\rho_F(d-1)<d-1\) is not a plausible uniform finite-fiber target.
The actual comparison must use \(1/\pc(T_d\square F)\), which also reflects
the finite-fiber branching capacity.

## Round 475 clique-fiber percolation scale is also linear

Round 475 pairs the \(K_m\) annular lower bound with the matching percolation
scale.  Set \(p=C/m\).  Inside each clique bag, open edges form
\(G(m,C/m)\), which has a giant component of density \(\theta(C)>0\) for
\(C>1\), with \(\theta=1-e^{-C\theta}\).  A giant-sized parent type and a
child giant overlap in about \(\theta^2m\) fiber coordinates; the chance that
some matching parent-child tree edge is open is approximately
\[
  1-\exp(-C\theta(C)^2).
\]
For \(C=C(d)\) large enough, the coarse giant-type branching process is
supercritical, giving
\[
  \pc(T_d\square K_m)\le \frac{C(d)+o(1)}{m}.
\]
Thus \(1/\pc(T_d\square K_m)\) also grows linearly in \(m\).  The
clique-fiber calibration is therefore a constant-comparison problem between
the finite-state SAW transfer and the finite-type percolation matrix, not a
comparison with the embedded tree branching \(d-1\).

## Round 476 one-ended product warning: \(T_d\square \mathbb Z\)

Round 476 marks the next product test.  Finite fibers work because exterior
components have boundedly many ports, and finite root anomalies cannot be
used linearly many times by a self-avoiding path.  For
\(T_d\square\mathbb Z\), however,
\[
  d((o,0),(v,z))=d_T(o,v)+|z|,
\]
and outside \(B_{u-1}((o,0))\) all tree branches communicate through the high
\(\mathbb Z\)-levels \(|z|\ge u\).  A self-avoiding annular path can switch
between tree branches at many distinct heights, so the finite-bag recursion
\(\mathbf G=\Phi_F(z,\mathbf G;q)\) no longer applies.

The next one-ended calibration is therefore a half-plane transfer in
\[
  h=d_T(o,v),\qquad k=|z|,\qquad h+k\ge u,
\]
with self-avoidance memory that prevents reuse of tree vertices at the same
\(\mathbb Z\)-height.  The lower bound \(\Gamma_{\rm ann}\ge\sqrt{d-1}\)
survives, but it is probably not sharp.

## Round 477 product-shuffle fork for \(T_d\square\mathbb Z\)

Round 477 isolates the next calibration fork.  The global product SAW
operator has the shuffle lower bound
\[
  \gamma_{\rm SAW,2}(T_d\square\mathbb Z)\ge \sqrt{d-1}+1.
\]
Finite-fiber annular calculations do not realize this additive entropy:
branching is paid in out-and-back pairs inside bounded-port cones.  For
\(T_d\square\mathbb Z\), unbounded portal heights may allow tree
out-and-back entropy, monotone \(\mathbb Z\)-motion, and binomial shuffle
entropy to coexist.

The fork is now explicit: either construct an annular product-shuffle family
giving
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\ge \sqrt{d-1}+1,
\]
or prove that the exterior/sphere constraint couples line motion to tree
return depth strongly enough to lose the additive shuffle term.  This must be
settled before \(T_d\square\mathbb Z\) can calibrate the universal annular
gap.

## Round 478 portal-staircase lower bound in \(T_d\square\mathbb Z\)

Round 478 constructs a concrete one-ended lower bound.  Start from an outward
neighbor \((v,0)\) with tree depth \(u\).  Move to \((o,u)\) using \(u\)
inward tree steps and \(u\) upward \(\mathbb Z\)-steps; staying outside the
ball is the Catalan prefix condition, giving \(C_u\asymp4^u u^{-3/2}\)
interleavings.  Then move from \((o,u)\) to \((w,0)\) in a different
principal branch using \(u\) outward tree steps and \(u\) downward
\(\mathbb Z\)-steps, giving another \(C_u\) choices.  There are
\(\asymp q^u\) possible terminal branches, and after normalization by
\(\sqrt{|V|}\) the length-\(4u\) contribution is
\[
  \asymp 16^u q^{u/2}/\operatorname{poly}(u).
\]
Hence
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\ge 2(d-1)^{1/8}.
\]
Together with the tree out-and-back family, this gives
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  \max\{\sqrt{d-1},2(d-1)^{1/8}\}.
\]
This does not settle the \(\sqrt{d-1}+1\) shuffle fork, but it proves that
unbounded portal heights create genuine annular entropy beyond finite-fiber
cone returns.

## Round 479 symmetric portal-staircase lower bound

Round 479 strengthens Round 478 by using large boundary sets on both sides
of the annular cut norm.  Choose two disjoint principal tree branches.  Let
\(U\) and \(V\) be the boundary vertices \((p,0)\) at tree depth \(u-1\) in
the two branches.  Then \(|U|\asymp |V|\asymp q^u\).  For each start child
\((v,0)\) and terminal child \((w,0)\), the Catalan path through \((o,u)\)
has length \(4u\) and contributes \(C_u^2\), with
\(C_u\asymp4^u u^{-3/2}\).  Since the branches are disjoint, the paths are
self-avoiding.  The normalized cut contribution is
\[
  \frac{C_u^2 q^2 |U||V|}{\sqrt{|U||V|}}
  \asymp
  16^u q^u/\operatorname{poly}(u).
\]
Thus
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\ge 2(d-1)^{1/4},
\]
and the current lower calibration is
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  \max\{\sqrt{d-1},2(d-1)^{1/4}\}.
\]
This still does not attain \(\sqrt{d-1}+1\) for large \(d\), but it shows
that both endpoint sides of the annular cut norm can contribute tree entropy
through a high-\(\mathbb Z\) portal.

## Round 480 optimizing one-portal staircases

Round 480 optimizes the one-portal family.  Let endpoint tree depth be
\(r=\lambda u\), endpoint line height \(u-r\), and portal height \(M=\mu u\)
with \(\mu\ge1\).  One leg has \(r\) tree steps and \(M-u+r\) line steps, so
its exponential count is
\[
  \binom{M-u+2r}{r}
  =
  \exp\{u nH(\lambda/n)+o(u)\},
  \qquad n=\mu-1+2\lambda.
\]
After two legs, endpoint-set normalization, and total length \(2un\), the
rate is
\[
  \exp\{H(t)+(t/2)\log q\},\qquad t=\lambda/n\le1/2.
\]
This is increasing on \([0,1/2]\), so the maximum is at \(t=1/2\), i.e.
\(\mu=1\), with value
\[
  2q^{1/4}.
\]
Thus a raised single portal cannot reach the global product-shuffle scale
\(\sqrt q+1\); any such lower bound would need repeated or distributed
portals.

## Round 481 high-root bubble transfer and the missing exit cost

Round 481 isolates a repeated-portal transfer.  After reaching \((o,u)\), repeat
bubbles from \((o,H)\) to \((o,H+s)\): move outward to tree depth \(r\) at
height \(H\), take one upward line step, then return inward while
interleaving the remaining \(s-1\) upward steps.  The first upward step keeps
the inward traversal off the outward vertices, and increasing root heights
make different bubbles self-avoiding; avoiding the previous first branch
costs only a bounded factor.

One bubble has at least
\[
  c q^r\binom{r+s-1}{r}
\]
choices and length \(2r+s\).  With \(s=ar\), optimizing
\[
  \frac{\log q+(1+a)H(1/(1+a))}{2+a}
\]
gives \((1+a)/a^2=q\), and the optimal rate is
\[
  \lambda_q=\frac{1+\sqrt{1+4q}}{2}.
\]
This is only a high-root transfer rate.  It does not by itself imply
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\ge\lambda_q,
\]
because after many bubbles the path is far above the fixed annular boundary
and the final descent costs a comparable number of line steps.

## Round 482 corrected repeated-bubble variational target

Round 482 includes the missing exit cost.  Start at \((o,u)\), run a bubble
phase with total branch depth \(R\) and upward gain \(S\), then exit to a
terminal boundary set at tree depth \(T\).  The bubble phase contributes
\[
  q^R\binom{R+S}{R}
\]
and length \(2R+S\).  The exit phase contributes
\[
  \binom{S+2T}{T}
\]
and endpoint normalization \(q^{T/2}\), with length \(S+2T\).  Thus the
corrected repeated-bubble family gives
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  \exp\!\left[
    \sup_{R,S,T\ge0}
    \frac{
      R\log q
      +(R+S)H(R/(R+S))
      +(T/2)\log q
      +(S+2T)H(T/(S+2T))
    }{2(R+S+T)}
  \right].
\]
This variational expression, not \(\lambda_q\) alone, is the next object to
optimize.  The proven current calibration remains at least
\(\max\{\sqrt q,2q^{1/4}\}\) until this corrected expression is evaluated.

## Round 483 corrected bubble subfamily gives \(\sqrt{q+1}\)

Round 483 extracts a paid-exit subfamily from Round 482.  Start at
\((o,u)\), move out to tree depth \(R\) at height \(u\), and return to
\((o,u+S)\) by interleaving upward line steps with the inward tree return.
This contributes
\[
  q^R\binom{R+S}{R}
\]
and length \(2R+S\).  Then exit through a fresh terminal column of depth
\(T=o(R)\), even fixed \(T=1\) in a different first branch, paying length
\(S+o(R)\) to descend back to radius \(u\).  The terminal normalization is
subexponential.

With \(S=aR\), the paid-exit rate is
\[
  \exp\left\{
    \frac{\log q+(1+a)H(1/(1+a))}{2(1+a)}
  \right\},
\]
maximized at \(a=1/q\), with value
\[
  \sqrt{q+1}.
\]
Thus
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  \max\{2(d-1)^{1/4},\sqrt d\}.
\]
This is a valid annular lower bound with the descent cost included, still
below the global product-shuffle scale \(\sqrt{d-1}+1\).

## Round 484 generating function for the corrected bubble variational problem

Round 484 optimizes the corrected repeated-bubble family.  With \(t\) marking
half-length \(R+S+T\), the generating function is
\[
  F_q(t)=
  \sum_{R,S,T\ge0}
  q^R\binom{R+S}{R}q^{T/2}\binom{S+2T}{T}t^{R+S+T}.
\]
The \(T=0\) terms encode the same exponential radius as a fixed fresh
terminal column \(T=1\), so they do not create a fake annular shortcut.
Using
\[
  \sum_R\binom{R+S}{R}(qt)^R=(1-qt)^{-S-1}
\]
and
\[
  \sum_T\binom{S+2T}{T}x^T
  =
  \frac{A(x)^S}{\sqrt{1-4x}},
  \qquad
  A(x)=\frac{1-\sqrt{1-4x}}{2x},
\]
one obtains
\[
  F_q(t)=
  \frac{1}{(1-qt)\sqrt{1-4\sqrt q\,t}}
  \frac{1}{1-tA(\sqrt q\,t)/(1-qt)}.
\]
Thus this family has optimized rate
\[
  \Lambda_q=t_q^{-1/2},
\]
where \(t_q\) is the smallest positive singularity, including the possible
interior solution
\[
  \frac{tA(\sqrt q\,t)}{1-qt}=1.
\]
Consequently
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\ge \Lambda_{d-1}.
\]
This refines the explicit \(\max\{2q^{1/4},\sqrt{q+1}\}\) lower bound but
still stays below the unresolved \(\sqrt q+1\) shuffle scale in the current
construction family.

## Round 485 explicit phase formula for \(\Lambda_q\)

Round 485 solves the singularity comparison.  Put \(s=\sqrt q\) and
\(y=\Lambda_q^2=t_q^{-1}\).  The interior singularity equation is
\[
  \frac{1-\sqrt{1-4s/y}}{2s}=1-\frac{s^2}{y}.
\]
After squaring, the valid root is
\[
  y_-(s)=
  \frac{
    2s^3-s^2-1
    -
    \sqrt{(2s^3-s^2-1)^2-4(s-1)s^5}
  }{2(s-1)}.
\]
The interior singularity occurs before the branch singularity
\(t=1/(4s)\) exactly when
\[
  s\ge2+\sqrt2,\qquad q\ge6+4\sqrt2.
\]
Thus
\[
  \Lambda_q=
  \begin{cases}
    2q^{1/4}, & q<6+4\sqrt2,\\
    \sqrt{y_-(\sqrt q)}, & q\ge6+4\sqrt2.
  \end{cases}
\]
For integer \(q=d-1\), the transition starts at \(q=12\).  Asymptotically
\(\Lambda_q=\sqrt q+O(q^{-1/2})\), still below \(\sqrt q+1\).

## Round 486 column-cluster percolation comparison for \(T_d\square\mathbb Z\)

Round 486 compares the lower calibration with an elementary \(\pc\) upper
bound.  Explore forward tree columns.  When a column is reached, reveal its
open vertical cluster of size \(N=1+L+R\), with \(L,R\) geometric and
\(\mathbb P(L=k)=(1-p)p^k\).  A given child column is hit with probability
\(1-(1-p)^N\), so the forward exploration has Galton-Watson mean
\[
  m_q(p)
  =
  q\left(
    1-\frac{(1-p)^3}{(1-p+p^2)^2}
  \right).
\]
If \(m_q(p)>1\), then \(p\ge\pc(T_d\square\mathbb Z)\).  For \(q=2\),
\[
  p_{\rm col}=0.3276217564\ldots,\qquad
  1/p_{\rm col}=3.0523003446\ldots,
\]
which is above \(\Lambda_2=2\cdot2^{1/4}\).  For integer \(q\ge3\), the
embedded tree gives \(1/\pc\ge q\), and Round 485 gives \(\Lambda_q<q\).
Thus the currently identified annular lower-bound mechanisms do not obstruct
\(\Gamma_{\rm ann}<1/\pc\) on \(T_d\square\mathbb Z\); the hard direction is
upper control of the annular transfer.

## Round 487 sharp upper target for \(T_d\square\mathbb Z\)

Round 487 identifies the sharp upper target
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\le\sqrt{d-1}+1.
\]
This would imply the annular gap: for \(q=d-1\ge3\),
\(\sqrt q+1<q\le1/\pc\), while for \(q=2\) the column-cluster bound from
Round 486 gives \(1/\pc\ge3.0523003446\ldots>\sqrt2+1\).

A sufficient estimate is the tree-line split.  Let \(C_{n,a}^{X_u}\) count
annular exterior SAWs of length \(n\) with exactly \(a\) tree steps.  It is
enough to prove
\[
  \frac{\langle \nu_U,C_{n,a}^{X_u}\nu_V\rangle}{\sqrt{|U||V|}}
  \le
  e^{o(n)}\binom{n}{a}(d-1)^{a/2}
\]
uniformly over roots, levels, and boundary sets.  Summing over \(a\) gives
the \((\sqrt{d-1}+1)^n\) bound.  The remaining obstacle is to recover
Haagerup-type square-root tree branching despite tree backtracks occurring at
different \(\mathbb Z\)-heights.

## Round 488 stack-charge lemma for the tree-line split

Round 488 isolates the combinatorial lemma behind the Round 487 estimate.
For an annular SAW with \(a\) tree steps and endpoint tree displacement \(D\),
the projected tree walk has
\[
  P=(a+D)/2
\]
forward stack pushes and \(R=(a-D)/2\) pops.  Raw branching costs \(q^P\),
but endpoint \(L^2\) averaging supplies the Haagerup gain \(q^{D/2}\), leaving
\(q^{a/2}\).  The remaining danger is Catalan push-pop entropy.

The needed lemma is that, for annular exterior SAWs in
\(T_d\square\mathbb Z\), this push-pop schedule is encodable up to
\(e^{o(n)}\) choices by the tree/line interleaving and the line-height trace.
Self-avoidance should force every nontrivial pop to be separated from its
matching push by line-height motion; crossing back at the same height would
revisit a vertex.  Proving this stack-charge lemma would give
\[
  \langle\nu_U,C_{n,a}^{X_u}\nu_V\rangle/\sqrt{|U||V|}
  \le e^{o(n)}\binom na q^{a/2},
\]
and hence \(\Gamma_{\rm ann}(T_d\square\mathbb Z)\le\sqrt q+1\).

## Round 489 vertical-run entropy in the stack-charge lemma

Round 489 corrects an incompleteness in Round 488.  The line-height trace is
not subexponential for free: after moving to a fresh tree vertex, a path may
change vertical direction without revisiting a vertex.  If \(b\) line steps
are split into \(r\) maximal monotone vertical runs, then \(r\le a+1\), and
the crude number of run choices is
\[
  \sum_{r\le a+1}2^r\binom{b-1}{r-1},
\]
which can be exponential in \(n\).  Thus the missing lemma must jointly
control tree stack schedules and vertical run decompositions.

The refined target is: after endpoint \(L^2\) averaging, the combined choices
of tree stack schedule, vertical runs, and line-height trace for annular
exterior SAWs with \(a\) tree steps and \(b\) line steps are bounded by
\[
  e^{o(n)}\binom na q^{a/2}.
\]
The exterior excursion condition \(d_T(o,v)+|z|-u\ge0\) and the fixed annular
endpoint radius must be used to absorb the vertical-run entropy.

## Round 490 fresh-column vertical-run obstruction to the \(\sqrt q+1\) target

Round 490 shows that \(\sqrt q+1\) is too strong for \(q=2,3\).  Consider
paths that only move outward in the tree, and after each tree step take a
monotone vertical run in the fresh tree column.  These paths are
self-avoiding, and their excess \(e=d_T(o,v)+z-u\) is a one-dimensional
excursion.  After endpoint \(L^2\) normalization, an outward tree step has
weight \(\sqrt q\).  The fresh-column block inventory is
\[
  B_q(z,w)=
  \sqrt q\,z\,w
  \left(1+\frac{zw}{1-zw}+\frac{z/w}{1-z/w}\right).
\]
The excursion critical equations \(B_q=1\), \(\partial_wB_q=0\) give lower
rate
\[
  \Xi_q=\sqrt{1+4\sqrt q}.
\]
Since \(\Xi_q>\sqrt q+1\) exactly for \(q<4\), the corrected upper target is
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \le
  \max\{\sqrt q+1,\sqrt{1+4\sqrt q}\}.
\]
This still suffices for the annular gap: for \(q\ge4\) it is below \(q\), for
\(q=3\) it is below \(3\), and for \(q=2\) it is below the column-cluster
inverse threshold from Round 486.

## Round 491 corrected master upper target for \(T_d\square\mathbb Z\)

Round 491 sets the corrected target
\[
  M_q=\max\{\sqrt q+1,\sqrt{1+4\sqrt q}\},
  \qquad
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\le M_q.
\]
This target matches the two known mechanisms: stack/product-shuffle behavior
at scale \(\sqrt q+1\), and fresh-column vertical-run excursions at scale
\(\sqrt{1+4\sqrt q}\).  It still implies the annular gap for all integer
\(q=d-1\ge2\), using the embedded-tree bound for \(q\ge3\) and the
column-cluster bound for \(q=2\).

The corresponding operator target is
\[
  \langle\nu_U,C_n^{X_u}\nu_V\rangle/\sqrt{|U||V|}
  \le e^{o(n)}M_q^n.
\]
The missing proof must show that alternating between stack-return behavior
and fresh-column vertical-run behavior does not create a third larger
exponential scale; transitions must be charged to the same annular excess
budget and endpoint \(L^2\) tree averaging.

## Round 492 support-tree and edge-height representation

Round 492 separates tree branching from height-order entropy.  For an
annular SAW \(\gamma\), let \(S(\gamma)\) be the tree subtree visited by the
tree projection, and for each tree edge \(e\) let \(H_e\) be the set of
heights at which \(\gamma\) crosses \(e\).  Self-avoidance implies each
\(H_e\) has no repeated height.

If \(a\) is the number of tree steps, \(D\) the tree endpoint displacement,
and \(K=|E(S(\gamma))|\), then
\[
  K\le(a+D)/2.
\]
Thus branch choices cost \(q^K\), and endpoint \(L^2\) averaging contributes
the Haagerup gain \(q^{D/2}\), leaving
\[
  q^{K-D/2}\le q^{a/2}.
\]
The desired tree factor is therefore a support-tree edge-count fact.  The
remaining problem is to count abstract support-tree traversals, crossing
heights \(H_e\), and vertical moves under self-avoidance and the annular
excess constraint.  Round 490 is the \(K=a\) fresh-edge case; stack-return
families have \(K<a\) and force repeated crossings at distinct heights.

## Round 493 fixed-height run decomposition is too crude

Round 493 tests the naive run decomposition.  Alternate fixed-height tree
runs and vertical runs.  A nonempty tree run has Haagerup inventory
\[
  \frac{\sqrt q\,z}{1-\sqrt q\,z},
\]
and a crude vertical run has inventory \(2z/(1-z)\).  Free alternation gives
the singularity
\[
  \frac{\sqrt q\,z}{1-\sqrt q\,z}\frac{2z}{1-z}=1,
\]
with rate
\[
  R_{\rm run}(q)=
  \frac{\sqrt q+1+\sqrt{q+6\sqrt q+1}}{2}.
\]
This is too large; for \(q=3\), \(R_{\rm run}=3.262\ldots>3\).  The loss is
that signs and depth changes of tree runs are treated as free.  The annular
excess \(d_T(o,v)+|z|-u\) must be tracked through signed tree-run and
vertical-run increments.  The next upper model therefore needs a signed
tree-run inventory, not just run lengths.

## Round 494 signed run inventory still overcounts without support memory

Round 494 tests signed run tracking.  The Haagerup-weighted signed tree-run
inventory is
\[
  T_s(z,w)=\frac{1}{(1-szw)(1-sz/w)}-1,\qquad s=\sqrt q,
\]
and the vertical-run inventory is
\[
  V(z,w)=\frac{zw}{1-zw}+\frac{z/w}{1-z/w}.
\]
The free signed excursion kernel \(T_s+V\) has symmetric critical point
\(w=1\) and gives rates such as \(6.4859\ldots\) for \(q=2\) and
\(7.4914\ldots\) for \(q=3\), far above the target.  The overcount comes from
forgetting support-tree memory: later tree runs are allowed to reuse tree
edges and columns as if fresh.  Therefore the upper proof must retain
edge-height support memory, distinguishing fresh-edge moves from repeated
edge crossings.

## Round 495 rooted cone height-kernel architecture

Round 495 proposes a recursive transfer that keeps support memory.  For an
oriented tree edge from parent \(p\) to child \(r\), let \(E_z(h,h')\) be the
generating function of self-avoiding excursions in the descendant cone of
\(r\) that enter through \((p,h)\to(r,h)\), stay in the cone, and exit through
\((r,h')\to(p,h')\), without using the parent edge in between.  Repeated use
of the same tree edge is then recorded by distinct crossing heights.

Inside the root column of the cone, the path uses disjoint vertical intervals
and launches excursions into the \(q\) child cones, each contributing another
copy of \(E_z\).  This suggests an interval-renewal inequality
\[
  E_z\preceq \mathcal F_q(z,E_z)
\]
on kernels over \(\mathbb Z\).  Proving this transform is finite in an
annular cut norm for \(z<M_q^{-1}\), with
\[
  M_q=\max\{\sqrt q+1,\sqrt{1+4\sqrt q}\},
\]
would give the corrected master upper bound.  The architecture directly
targets the support-memory loss in Rounds 493--494.

## Round 496 multi-port cone kernels are necessary

Round 496 corrects Round 495.  A global self-avoiding path can use the same
child cone more than once at different root-column heights.  After deleting
the root column, one child cone may contain several disjoint subpaths whose
endpoints lie in an ordered finite height set \(A\subset\mathbb Z\).  Thus a
two-height kernel \(E_z(h,h')\) is only the \(|A|=2\) special case.

The correct recursive object is a multi-port cone kernel
\[
  E_z(\mathcal P;A),
\]
where \(\mathcal P\) records the connectivity pattern of the path segments
inside the cone.  Root-column self-avoidance supplies an ordered list of
visited heights; gaps are filled by vertical intervals or by child-cone
multi-port configurations.  The needed norm is therefore a polymer norm over
finite height sets, not merely an \(\ell^2(\mathbb Z)\) operator norm.  A
plausible target is
\[
  \sum_{\mathcal P}E_z(\mathcal P;A)\le C(z)^{|A|}\Phi_z(A),
\]
with span/gap penalties strong enough to close a renewal or cluster-expansion
bound at \(z<M_q^{-1}\).

## Round 497 root-column trace words

Round 497 refines the multi-port object.  For a cone path, record the ordered
root-column visits
\[
  h_0,h_1,\ldots,h_m,
\]
all distinct by self-avoidance.  Each consecutive pair is either a vertical
interval in the root column or a child-cone piece labeled by a child
\(c\in\{1,\ldots,q\}\).  Thus the recursive boundary object is a trace word
\[
  \mathcal W=(h_0,\ell_0,h_1,\ldots,\ell_{m-1},h_m),
\]
not an unordered height set with arbitrary pairings.  For each child label,
the corresponding subword is passed recursively to that child cone in global
path order.  The transform must sum trace words with distinct heights,
disjoint vertical intervals, recursive child feasibility, and the annular
excess constraint.  A suitable bound on
\[
  \sum_{\mathcal W:h_0=h,\ h_m=h'} Z_z(\mathcal W)
\]
is the concrete form of the interval-renewal estimate needed for
\(z<M_q^{-1}\).

## Round 498 compressed trace words and root-interval validity

Round 498 corrects the trace-word language: the heights \(h_i\) should be
compressed portal heights, not every root-column vertex.  Vertical labels are
maximal vertical runs.  For a portal set
\[
  P(\mathcal W)=\{h_0,\ldots,h_m\},
\]
root-column self-avoidance is equivalent to the following interval rule:
the portal heights are distinct, no two maximal vertical labels are
consecutive, and the \(V\)-labeled pairs form a matching of adjacent pairs in
the increasing order of \(P(\mathcal W)\).

Consequently vertical-run entropy is a hard-core matching on ordered height
gaps, with contribution
\[
  \prod_{\{x_j,x_{j+1}\}\in M_V} z^{x_{j+1}-x_j},
  \qquad x_0<\cdots<x_m.
\]
This replaces the free signed-run overcount from Rounds 493--494 by a local
gap gas.  The annular exterior condition adds the constraint
\[
  r+|t|\ge u
\]
throughout every selected vertical gap in a cone rooted at tree depth \(r\)
outside a ball of radius \(u\).  The remaining entropy to control is therefore
the time order of the portals and the interleaving of child-label subwords,
not arbitrary vertical run decomposition.

## Round 499 ordered child packets and shuffle norms

Round 499 refines what a child label receives from a root trace word.  For
each child \(c\), the induced object is not one continuous trace inside the
child cone, but an ordered packet
\[
  \Pi_c(\mathcal W)=\bigl((h_i,h_{i+1}):\ell_i=c\bigr)
\]
of boundary-to-boundary pieces.  The child cone must realize these pieces by
mutually avoiding path segments, ordered by global path time.  Thus the
recursive partition function is
\[
  E_z(\Pi),\qquad
  \Pi=((a_1,b_1),\ldots,(a_k,b_k)),
\]
with \(k=1\) giving the two-height kernel and \(k>1\) giving the multi-port
kernel.

The root transform has schematic form
\[
  Z_z(\mathcal W)
  \le
  {\bf 1}_{\rm valid}(\mathcal W)\,
  \mathcal V_z(\mathcal W)
  \prod_{c=1}^q E_z(\Pi_c(\mathcal W)),
\]
where \(\mathcal V_z\) is the hard-core vertical-gap weight.  The time-order
shuffle of packets with sizes \(k_1,\ldots,k_q\) and \(v\) vertical runs
creates the multinomial factor
\[
  \binom{k_1+\cdots+k_q+v}{k_1,\ldots,k_q,v}.
\]
Therefore the natural recursive norm should be exponential-generating in the
number of packet atoms:
\[
  \mathcal N_z(E;\xi,\Phi)
  =
  \sum_{k\ge0}\frac{\xi^k}{k!}
  \sup_{\Pi:|\Pi|=k}\frac{E_z(\Pi)}{\Phi(\Pi)}.
\]
The factorials exactly absorb shuffle factors.  The next concrete target is
to choose a gap/excess weight \(\Phi\) for which the trace transform is
contractive or invariant at every \(z<M_q^{-1}\).

## Round 500 excess-weight calibration for the packet norm

Round 500 calibrates the excess part of the packet norm against the known
fresh-column obstruction.  Put \(s=\sqrt q\).  The one-particle fresh-column
block inventory is
\[
  B_q(z,w)
  =
  szw\left(
    1+\frac{zw}{1-zw}+\frac{z/w}{1-z/w}
  \right),
\]
where \(w\) marks annular excess.  The critical equations for \(B_q\) give
the \(\sqrt{1+4s}\) rate from Round 490.  Hence, for every
\[
  z<M_q^{-1},\qquad M_q=\max\{s+1,\sqrt{1+4s}\},
\]
one should choose \(w=w(z)\) with \(B_q(z,w)<1\).

For a cone rooted at tree depth \(r\) outside a ball of radius \(u\), define
\[
  e_r(h)=r+|h|-u,\qquad
  E_r(\Pi)=\sum_{(a,b)\in\Pi}(e_r(a)+e_r(b)).
\]
The candidate weighted packet norm is
\[
  \|E\|_{z,\xi,w,\Phi}
  =
  \sum_{k\ge0}\frac{\xi^k}{k!}
  \sup_{\Pi:|\Pi|=k}
  \frac{E_z(\Pi)}{w^{E_r(\Pi)}\Phi(\Pi)}.
\]
The factorial controls time shuffles, the \(w\)-weight controls annular
excess, and the still-missing gap factor \(\Phi\) must control ordered portal
heights and hard-core vertical matchings.  Passing a \(k\)-packet to a child
cone increases the excess of its \(2k\) boundary ports by one, producing only
a deterministic per-atom factor that can be absorbed into \(\xi\).

## Round 501 two-component gap weight

Round 501 proposes the missing gap factor.  For a packet
\[
  \Pi=((a_1,b_1),\ldots,(a_k,b_k)),
\]
set
\[
  L(\Pi)=\sum_{j=1}^k |a_j-b_j|,
  \qquad
  A(\Pi)=\{a_1,b_1,\ldots,a_k,b_k\}=\{x_0<\cdots<x_m\}.
\]
The child-jump summation needs pair-span decay \(\alpha^{L(\Pi)}\), with
\(z<\alpha<1\), since each boundary pair forces at least \(|a_j-b_j|\) line
steps.  The vertical-run summation needs the adjacent-gap gas
\[
  G_\eta(A)=\prod_{i=0}^{m-1}(1+\eta^{x_{i+1}-x_i}),
  \qquad z<\eta<1,
\]
because the hard-core matching partition of vertical intervals is bounded by
\[
  \prod_i(1+z^{x_{i+1}-x_i})\le G_\eta(A).
\]
Thus the current candidate norm is
\[
  \|E\|_{z,\xi,w,\alpha,\eta}
  =
  \sum_{k\ge0}\frac{\xi^k}{k!}
  \sup_{\Pi:|\Pi|=k}
  \frac{E_z(\Pi)}
       {w^{E_r(\Pi)}\alpha^{L(\Pi)}G_\eta(A(\Pi))}.
\]
The remaining task is to prove a finite-parameter closure of the root trace
transform in this norm for every \(z<M_q^{-1}\).

## Round 502 explicit fresh-block excess multiplier

Round 502 optimizes the fresh-column excess multiplier.  With \(s=\sqrt q\),
write \(a=zw\) and \(r=z^2\).  Then
\[
  B_q(z,w)
  =
  s\left(
    \frac{a}{1-a}
    +
    \frac{ar}{a-r}
  \right),
  \qquad r<a<1.
\]
The minimizer is
\[
  a_*(z)=\frac{2z^2}{1+z^2},
  \qquad
  w_*(z)=\frac{2z}{1+z^2},
\]
and
\[
  \min_w B_q(z,w)
  =
  \frac{4\sqrt q\,z^2}{1-z^2}.
\]
Hence \(B_q(z,w)<1\) is possible exactly when
\[
  z<\frac{1}{\sqrt{1+4\sqrt q}}.
\]
This proves that every \(z<M_q^{-1}\) has an explicit calibrated choice
\(w=w_*(z)\).  Note that \(w_*(z)<1\), so excess is penalized in the packet
norm; the child-depth shift gives a favorable per-atom factor \(w_*^{2}\).

## Round 503 packet-level root transform

Round 503 states the recursion at the correct packet level.  For
\[
  \Pi=((a_1,b_1),\ldots,(a_k,b_k)),
\]
\(E_z(\Pi)\) sums \(k\) mutually avoiding cone pieces ordered by global path
time.  At the cone root column, this means choosing an ordered family
\[
  \mathfrak W=(\mathcal W^{(1)},\ldots,\mathcal W^{(k)})
\]
of compressed trace words, where \(\mathcal W^{(j)}\) starts at \(a_j\) and
ends at \(b_j\).  These trace words are separated outside the cone, but share
the same root column avoidance constraints.

The valid family condition is global: all portal heights over all
\(\mathcal W^{(j)}\)'s are distinct, all vertical labels form a hard-core
matching of adjacent gaps in the sorted union of portal heights, and for each
child \(c\), the child packet \(\Pi_c(\mathfrak W)\) is obtained by collecting
all \(c\)-labeled pairs in global order.  The transform is
\[
  (\mathcal T E)_z(\Pi)
  =
  \sum_{\mathfrak W:\partial\mathfrak W=\Pi}
  {\bf 1}_{\rm valid}(\mathfrak W)\,
  \mathcal V_z(\mathfrak W)
  \prod_{c=1}^q E_z(\Pi_c(\mathfrak W)).
\]
Thus the closure problem is a polymer estimate for ordered trace families
sharing one root column; the single-trace case is only \(k=1\).

## Round 504 scalar row-sum closure is too crude

Round 504 tests a tempting collapse of the Round 501 norm, but the diagnostic
as first stated omitted the two parent-child crossing-edge costs per child
atom.  The uncorrected inventory was
\[
  C_{\rm row}(q,z)
  =
  q\,w_*(z)^2\,\frac{2z}{1-z}.
\]
This is superseded by Round 505.  The corrected convention includes a factor
\(z^2\) for entering and exiting the child cone.

## Round 505 corrected scalar child-atom inventory

Round 505 restores the crossing-edge cost.  With
\[
  w_*(z)=\frac{2z}{1+z^2},
\]
one child atom has corrected scalar inventory
\[
  A_q(z)
  =
  qz^2w_*(z)^2\frac{2z}{1-z}
  =
  \frac{8qz^5}{(1-z)(1+z^2)^2}.
\]
At the target radius \(z=M_q^{-1}\), this is \(<1\) with a large margin for
every integer \(q\ge2\).  For \(q=s^2\ge4\), \(M_q=s+1\) and
\[
  A_q(M_q^{-1})
  =
  \frac{8s}{((s+1)^2+1)^2}
  \le0.16.
\]
For \(q=2,3\), the values are \(0.172718\ldots\) and \(0.165820\ldots\).
Thus child-label and height-jump row sums are not the obstruction once the
two crossing edges are charged.  The next closure attempt should combine the
small atom inventory \(A_q(z)<1\) with the adjacent-gap hard-core gas and the
packet norm.

## Round 506 two-state scalar trace skeleton is subcritical

Round 506 keeps only one structural rule from compressed trace words: two
maximal vertical runs cannot be consecutive.  With
\[
  A_q(z)=qz^2w_*(z)^2\frac{2z}{1-z},
  \qquad
  U(z)=\frac{2z}{1-z},
\]
the row-summed atom sequence is dominated by the two-state matrix
\[
  R_q(z)=
  \begin{pmatrix}
    A_q(z)&U(z)\\
    A_q(z)&0
  \end{pmatrix}.
\]
Its positive eigenvalue is
\[
  \rho_q(z)=
  \frac{A_q(z)+\sqrt{A_q(z)^2+4A_q(z)U(z)}}{2},
\]
and \(\rho_q(z)<1\) iff \(A_q(z)(1+U(z))<1\).  At
\(z=M_q^{-1}\), this holds uniformly.  For \(q=s^2\ge4\),
\[
  A_q(M_q^{-1})(1+U(M_q^{-1}))
  =
  \frac{8(s+2)}{(s^2+2s+2)^2}
  \le0.32,
\]
while for \(q=2,3\) the spectral radii are \(0.561834\ldots\) and
\(0.518255\ldots\).  Thus the corrected scalar one-trace skeleton is already
subcritical; the next task is lifting this estimate to packet families.

## Round 507 span-resolved trace skeleton

Round 507 refines Round 506 by keeping endpoint span.  Let
\[
  c_q(z)=qz^2w_*(z)^2.
\]
For a monotone height subdivision, a child atom of length \(\ell\) has weight
\(c_q(z)z^\ell\), while a vertical atom has weight \(z^\ell\), with no two
vertical atoms consecutive.  With \(P(x)=x/(1-x)\), the color/length transfer
matrix is
\[
  R_c(x)=
  \begin{pmatrix}
    cP(x)&P(x)\\
    cP(x)&0
  \end{pmatrix}.
\]
The critical equation is \(cP(1+P)=1\), giving span growth
\[
  \lambda(c)=
  \frac{2+c+\sqrt{c^2+4c}}{2},
  \qquad
  (\lambda(c)-1)^2=c\lambda(c).
\]
Thus monotone portal subdivisions of total height span \(n\) are controlled
by \((z\lambda(c_q(z)))^n\).  At \(z=M_q^{-1}\), this base is below one for
all integer \(q\ge2\); the values for \(q=2,3,4\) are
\[
  0.559622\ldots,\quad 0.522249\ldots,\quad 0.495974\ldots.
\]
For \(q\ge4\), \(z\le1/3\) and \(c_q(z)\le0.16\), so the \(q=4\) value is an
upper bound.  Therefore the packet norm should choose a span parameter
\[
  z\lambda(c_q(z))<\alpha<1,
\]
not \(\alpha\downarrow z\).  This slack absorbs monotone portal subdivisions
uniformly in the endpoint height difference.

## Round 508 monotone packet supersolution

Round 508 inserts the packet constant into the span-resolved monotone model.
Assume temporarily that
\[
  E_z(\Pi)\le C^{|\Pi|}w_*^{E_r(\Pi)}\alpha^{L(\Pi)}.
\]
After dividing by the output span weight, put \(t=z/\alpha\) and
\(P(t)=t/(1-t)\).  A monotone one-trace transform is bounded by
\[
  H_{q,z,\alpha}(C)
  =
  \frac{
    P(t)\bigl(1+Cc_q(z)+Cc_q(z)P(t)\bigr)
  }{
    1-Cc_q(z)P(t)(1+P(t))
  }.
\]
Thus \(H_{q,z,\alpha}(C)\le C\) is a scalar supersolution condition, and then
a \(k\)-packet is bounded by \(C^k\) in the monotone model.

At \(z=M_q^{-1}\), the explicit choice
\[
  \alpha=0.9,\qquad C=2
\]
works uniformly for all integer \(q\ge2\).  The values of \(H(2)\) for
\(q=2,3,4\) are \(1.755378\ldots\), \(1.444189\ldots\), and
\(1.265548\ldots\); for \(q\ge4\), \(z\le1/3\) and \(c_q(z)\le0.16\), so the
\(q=4\) value bounds the rest.  This gives a concrete packet-level
supersolution for monotone trace families.

## Round 509 two-sided tilt fails in low branching

Round 509 tests the natural extension to nonmonotone height traces.  Tilting
toward the endpoint gives positive- and negative-increment inventories
\[
  P_+(\alpha)=\frac{z/\alpha}{1-z/\alpha},
  \qquad
  P_-(\alpha)=\frac{z\alpha}{1-z\alpha},
  \qquad P=P_++P_-.
\]
The same scalar majorant as Round 508 has a supersolution \(C\) only if
\[
  (1-b)^2-4bP\ge0,
  \qquad b=c_q(z)P(1+P).
\]
The best tilt is \(\alpha=1\), where \(P=2z/(1-z)\).  At
\(z=M_q^{-1}\), the discriminant is negative for \(q=2,3,4,5,6\) and becomes
positive at \(q=7\).  Thus a plain two-sided tilted row-sum majorant cannot
handle the low-branching nonmonotone traces.  The remaining proof must use
the discarded structure: distinct portal heights, adjacent-gap hard-core
constraints, killed annular excess, and mutual packet avoidance.

## Round 510 finite low-branching residual target

Round 510 turns the Round 509 obstruction into a finite residual inequality.
Use \(C=2\) and choose the weaker span decay \(\alpha=0.99\).  At
\(z=M_q^{-1}\), the monotone contribution leaves the margins
\[
\begin{array}{c|ccccc}
q&2&3&4&5&6\\
\hline
2-H_{q,z,0.99}(2)
&0.690084&0.885074&1.003447&1.181635&1.298499
\end{array}
\]
up to the displayed precision.  Since the two-sided tilted scalar
supersolution has positive discriminant for \(q\ge7\), the remaining scalar
trace problem is finite: bound the valid nonmonotone trace-family
contribution for \(q=2,\ldots,6\) by these margins.

A nonmonotone trace has total variation \(V\) and endpoint span \(S\) with
\(V-S\ge2\).  The next target is a reversal-cluster expansion that attaches
these excess-variation clusters to the monotone bridge, using the full
constraints from portal distinctness, adjacent-gap vertical matchings,
annular excess, and mutual packet avoidance.

## Round 511 neutral reversal-bubble inventory closes the scalar margins

Round 511 tests a concrete reversal-bubble majorant for the finite residual
cases.  A neutral reversal bubble leaves the monotone frontier, moves
backward in height, and returns to the frontier.  Its endpoint span is zero,
so its two legs are paid with
\[
  P_0(z)=\frac{z}{1-z}.
\]
Since two vertical atoms cannot be consecutive, at least one leg must be a
child atom.  With \(c_q(z)=qz^2w_*^2\) and packet constant \(C=2\), the bubble
inventory is
\[
  D_q(z)=P_0(z)^2\bigl((1+Cc_q(z))^2-1\bigr).
\]
Allowing a sequence of such bubbles gives \(D_q/(1-D_q)\).

At \(z=M_q^{-1}\), \(\alpha=0.99\), this correction fits inside the Round 510
margin for every \(q=2,\ldots,6\):
\[
  H_{q,z,0.99}(2)\frac{D_q(z)}{1-D_q(z)}
  <
  2-H_{q,z,0.99}(2).
\]
The worst case is \(q=2\), where the left side is
\(0.433037\ldots\) and the margin is \(0.690084\ldots\).  Thus the remaining
technical lemma is combinatorial: inject valid nonmonotone trace families
into monotone traces decorated by neutral reversal bubbles without increasing
weight.

## Round 512 leg collapse and record-envelope decomposition

Round 512 explains why the primitive bubble inventory from Round 511 is not
immediately invalidated by subdivided monotone legs.  In the residual regime
\(q=2,\ldots,6\), \(z=M_q^{-1}\), and \(C=2\),
\[
  Cc_q(z)=2qz^2w_*^2\le0.32<1.
\]
Thus any monotone leg of total height length \(L\) can be collapsed without
decreasing the majorant weight: a pure vertical leg is already one vertical
atom, while a leg with \(m\ge1\) child atoms has color factor
\((Cc_q)^m\le Cc_q\) and may be replaced by one child atom of length \(L\).
For a reversal bubble, the two collapsed legs cannot both be vertical,
because that would contradict maximal vertical-run compression.  This
justifies the Round 511 factor
\[
  D_q(z)=\left(\frac{z}{1-z}\right)^2
  \bigl((1+Cc_q(z))^2-1\bigr)
\]
as a collapsed-leg majorant.

The proposed combinatorial proof is a record-envelope decomposition.  For an
endpoint to the right, follow running record maxima.  Record increments form
the monotone skeleton; excursions below the current record that return to or
cross the record become neutral reversal bubbles.  If a child jump crosses
over the record to a new record, insert a virtual cut at the record level,
splitting the jump into a return plus a forward atom without increasing
weight.  The remaining formal task is to carry this decomposition through
packet families and verify compatibility with adjacent-gap vertical
matchings.

## Round 513 single-trace record-envelope lemma

Round 513 states the scalar combinatorial lemma.  In the residual cases set
\[
  a=Cc_q(z)=2qz^2w_*^2<1.
\]
Atoms have weight \(z^{|\delta|}\) if vertical and
\(az^{|\delta|}\) if child, with no consecutive vertical atoms.  Every trace
from \(0\) to \(S>0\) should be encodable by a monotone increasing trace from
\(0\) to \(S\) and an ordered list of neutral primitive bubbles, with no
smaller majorant weight.  A primitive bubble has inventory
\[
  D_q(z)=\left(\frac{z}{1-z}\right)^2\bigl((1+a)^2-1\bigr).
\]

The proof uses running record maxima.  Excursions below a record level are
cut out as neutral bubbles; if the return atom crosses the record to a new
record, split that child atom at the virtual record level.  This split does
not increase weight because a vertical atom cannot cross an already visited
record in a valid compressed trace, and \(a<1\) controls the color factor.
Internal reversals are handled recursively after reflection, producing a
depth-first ordered list of primitive bubbles.  This would prove the scalar
one-trace low-branching residual; the remaining extension is to packet
families sharing the root column.

## Round 514 packet lift from the scalar record-envelope lemma

Round 514 records that the single-trace lemma would close the scalar packet
transform.  Let
\[
  B_q(z)=\frac{H_{q,z,0.99}(2)}{1-D_q(z)}.
\]
For \(q=2,\ldots,6\) at \(z=M_q^{-1}\), the values are
\[
  1.742953,\quad1.411562,\quad1.223666,\quad0.951638,\quad0.788235,
\]
all below \(C=2\).  Applying the single-trace encoding independently to each
of the \(k\) traces in a packet gives a bound \(B_q(z)^k\le C^k\).

The scalar majorant already includes child-label choices, crossing edges, and
the recursive child packet factor.  Indeed, child packets collected across
all traces contribute
\[
  \prod_{c=1}^q C^{|\Pi_c|}
  =
  C^{\sum_c|\Pi_c|}.
\]
Shared root-column avoidance only removes valid families, so it does not
increase the scalar bound.  Thus, modulo the single-trace record-envelope
lemma, the scalar packet transform closes with \(C=2\), \(\alpha=0.99\), and
\(w=w_*(z)\).  The remaining non-scalar issue is to reinsert the ordered gap
gas \(G_\eta(A)\) and verify that virtual cuts do not create a deficit in the
gap weight.

## Round 515 span-scale audit: the scalar closure needs a two-scale norm

Round 515 audits a hidden assumption in Rounds 507--514.  In a same-scale
packet norm
\[
  E_z(\Pi)\le C^{|\Pi|}w^{E_r(\Pi)}\alpha^{L(\Pi)},
\]
a child atom of height span \(\ell\) contributes
\[
  Cqz^2w^2\alpha^\ell,
\]
not \(Cqz^2w^2z^\ell\).  After division by the parent output
\(\alpha^S\), monotone child subdivisions of total span \(S\) leave the
composition factor
\[
  Cqz^2w^2(1+Cqz^2w^2)^{S-1}.
\]
Thus the same-scale norm alone cannot justify the scalar closure.

The scalar calculations should be interpreted as a two-scale estimate.  If
recursive child packets are controlled with a stronger span parameter
\(\theta\) and the parent is measured with \(\alpha>\theta\), then a child
atom carries effective span ratio \((\theta/\alpha)^\ell\), while a root
vertical atom carries \((z/\alpha)^\ell\).  The corrected target is therefore
a Banach-scale bound
\[
  \mathcal T:\mathcal B_\theta\to\mathcal B_\alpha,
  \qquad 0<\theta<\alpha<1.
\]
Rounds 507--514 provide calibrated scalar evidence for such a two-scale
bound, roughly with \(\theta/\alpha\approx z/\alpha\), but not yet a
same-scale fixed point.  The next rigorous task is to prove the
record-envelope and packet estimates with separate child and vertical span
ratios, then find a bootstrap or analytic-norm argument that yields
finiteness for every \(z<M_q^{-1}\).

## Round 516 corrected two-scale scalar residual inequalities

Round 516 rewrites the residual calculation in the correct two-scale
notation.  Fix
\[
  \alpha=0.99,\qquad \theta=z,\qquad C=2,
\]
and set \(a_q(z)=Cqz^2w_*^2\).  A recursive child atom has span inventory
\[
  P_c=\frac{\theta/\alpha}{1-\theta/\alpha},
\]
while a root vertical atom has
\[
  P_v=\frac{z/\alpha}{1-z/\alpha}.
\]
The monotone transform is
\[
  H_q^{\theta,\alpha}(z)
  =
  \frac{a_qP_c+P_v+a_qP_cP_v}
       {1-a_qP_c(1+P_v)}.
\]
For a neutral bubble,
\[
  D_q^\theta(z)
  =
  \left(a_q\frac{\theta}{1-\theta}+\frac{z}{1-z}\right)^2
  -
  \left(\frac{z}{1-z}\right)^2.
\]
At \(z=M_q^{-1}\), \(q=2,\ldots,6\), the values of
\[
  H_q^{z,0.99}(z)/(1-D_q^z(z))
\]
are \(1.742953,1.411562,1.223666,0.951638,0.788235\), all below \(C=2\).
Thus the scalar residual calculation is valid as a two-scale estimate
\(\mathcal B_z\to\mathcal B_{0.99}\).  The remaining analytic problem is to
obtain or bootstrap control at the stronger scale \(\theta=z\).

## Round 517 scalar span-only bootstrap obstruction

Round 517 shows that a span-only bootstrap cannot supply that stronger-scale
control in the low-branching cases.  The monotone recursive scalar generating
function satisfies
\[
  F=V+b_q(1+V)F+b_q(1+V)F^2,
  \qquad
  V(x)=\frac{zx}{1-zx},
  \quad b_q=qz^2w_*^2.
\]
At \(z=M_q^{-1}\), its effective span bases are
\[
\begin{array}{c|ccccc}
q&2&3&4&5&6\\
\hline
\beta_q&0.974664&0.948207&0.925926&0.829994&0.753661.
\end{array}
\]
Thus monotone recursive control is only available for
\(\theta>\beta_q\).  Starting a two-scale step at
\(\theta=\beta_q+0.005\) and \(\alpha=0.999\), with the exact monotone input
norm \(F(1/\theta)\), already gives a negative transform denominator for
\(q=2,3,4,5\), and for \(q=6\) the neutral bubble inventory is
\(0.946516\ldots\).  Hence span scale alone cannot close the bootstrap.

The next norm must be excess-sensitive or gap-sensitive: reversal bubbles
must be charged against annular excess, adjacent-gap hard-core constraints,
shared packet avoidance, or stronger child-packet data before the span scale
approaches one.

## Round 518 excess reservoir replaces the geometric bubble sum

Round 518 identifies the missing geometric charge.  At root depth \(r\),
height \(h\) has annular excess
\[
  e_r(h)=r+h-u
\]
in the one-sided regime.  At a record height \(R\), a downward reversal of
depth \(d\) is legal only if \(d\le e_r(R)\), and portal heights are
distinct.  Thus reversal bubbles below a fixed record draw from the finite
reserve
\[
  \{R-e_r(R),\ldots,R-1\}.
\]
The unconstrained geometric factor \(1/(1-D)\) should be replaced by a
finite-reservoir factor
\[
  (1+D)^{e_r(R)}.
\]

This is compatible with the calibrated excess multiplier.  For
\(q=2,\ldots,6\) at \(z=M_q^{-1}\),
\[
  w_*(z)(1+D_q(z))<1,
\]
with worst value \(0.841367\ldots\) at \(q=2\).  Therefore the existing
excess weight has room to pay for reversal bubbles assigned to distinct
lower excess levels.  The next rigorous lemma is an injection from
record-envelope bubbles below a record height to distinct levels in that
record's annular reserve.
