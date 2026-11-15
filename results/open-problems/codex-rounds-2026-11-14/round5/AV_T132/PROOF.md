# Interior localization of sewing paths

The passage under examination is the interior clause of Lemma 'tree:lem:chart_reconstruction', used in Lemma 'tree:lem:nonzero_local_cost' of OpenAI, *Metric-measure limits of subcritical FK and spanning-tree planar maps* (September 24, 2026). The sources are [background.tex](sources/background.tex) and [certificates.tex](sources/certificates.tex). The argument below concerns actual sewn-graph paths and the internal graph of one complete interval. The construction of field-readable chart laws is a separate assertion.

## 1. Deterministic localization

Let $J$ be a compact real interval, $E$ a metric space, and $\eta:J\to E$ continuous. Fix $I=[a,b]\subset J$ and an open $O\subset E$ such that

\[
                       \eta^{-1}(O)\subset(a,b).                 \tag{1}
\]

Let $K\subset O$ be nonempty and compact. Suppose finite sewing paths $P_n$ have contour meshes $h_n\to0$. Let $T_n\subset J$ record every contour representative used, including both representatives of every zero-cost change. Suppose their projections use maps $\eta_n$ converging uniformly to $\eta$ on the mesh in $J$, and

\[
                 \sup_{t\in T_n}d_E(\eta_n(t),K)\to0.             \tag{2}
\]

Use the exact axial-walk rules of background.tex, with unscaled indices:

* A horizontal step joins its consecutive first-coordinate classes.
* A zero-cost change from $i$ to $j$ uses $L_i=L_j=\min_{[i,j]}L$.
* A vertical up-step ending at $u$ matches a down-step ending at $v>u$ when $R_{u-1}=R_v<\min_{u\le r<v}R_r$. The primal endpoint representatives are $u-1,v-1$.

An interval graph keeps horizontal steps and identifications witnessed within its interval, and vertical matches only when both complete steps belong to it. If mesh intervals $I_n$ have endpoints tending to $a,b$, then the same links of $P_n$ eventually form an internal path in $I_n$, in the same order and with unchanged cost.

### Proof

The set $A=\eta^{-1}(K)$ is compact and contained in $(a,b)$. If it is empty, the compact sets $\eta(J)$ and $K$ have positive distance, contradicting (2) and uniform convergence for any nonempty paths at large $n$. Otherwise choose $\delta>0$ with

\[
                         A\subset(a+3\delta,b-3\delta).
\]

The compact set $F=J\setminus(a+2\delta,b-2\delta)$ has image disjoint from $K$. If $F$ is nonempty, the distance $\rho$ between its image and $K$ is positive. For $t\in T_n\cap F$ we would have

\[
 \rho\le d_E(\eta(t),K)
 \le d_E(\eta(t),\eta_n(t))+d_E(\eta_n(t),K)\to0.
\]

Thus, also trivially if $F$ is empty,

\[
                         T_n\subset(a+2\delta,b-2\delta)         \tag{3}
\]

for every sufficiently large $n$. An independent compactness proof is to select offending $t_n\in F$, extract a convergent subsequence, and use (2) and continuity to put its limit in $A\cap F$, a contradiction.

Take $h_n<\delta/2$ and endpoint errors of $I_n$ less than $\delta/2$. Every horizontal step used is then internal. A first-coordinate change has its entire witnessing interval between its two recorded times, hence internal; its minimum test is unchanged. For a vertical match, (3) holds for its primal representatives $u-1,v-1$. Advancing each by one mesh step includes the two terminal times $u,v$, still strictly inside $I_n$. The entire witnessing interval is internal, so the same positive-cost edge is enabled. No second-coordinate edge is replaced by a zero-cost identification.

These are all link types. The first-coordinate relation inside $I_n$ equals the restriction of the full relation, since both test the same interval between the two times. Hence consecutive links still concatenate. The assertion holds simultaneously for every link, with no bound on their number and no accumulated error per crossing. This proves the claim.

## 2. The preimage condition from swept area

The argument at background.tex lines 199–206 has an elementary measure-theoretic formulation. Let $\eta:\mathbb R\to E$ be continuous and let $\mu$ be an area measure with the exact swept-area identity

\[
                    \mu(\eta([s,t]))=t-s \qquad(s<t).            \tag{4}
\]

Images of time intervals with disjoint interiors have zero $\mu$-overlap. Indeed split their spanning interval into the two intervals and the intervening interval. The image of the spanning interval is the union of these images. Equation (4) says that the measure of the union equals the sum of their measures. The sum of their indicator functions minus the indicator of their union is nonnegative and has integral zero; every pairwise overlap therefore has measure zero. Adjacent intervals need just the two-piece version.

Put $Q=\eta([a,b])$. If an outside time $t<a$ or $t>b$ mapped into $Q^\circ$, continuity would put the image of a positive-length interval around $t$, disjoint from $[a,b]$, inside $Q^\circ$. Its positive area contradicts zero overlap. If $\eta(a)\in Q^\circ$, continuity gives such an interval immediately before $a$; for $b$, use an interval immediately after it. Thus

\[
                         \eta^{-1}(Q^\circ)\subset(a,b).         \tag{5}
\]

This argument requires neither a Brownian fiber classification nor disk topology. It does use the exact swept-area property (4). Properness of the bilateral curve, asserted in background.tex, bounds all representatives above a planar compact set in a fixed contour window. The continuum encoding, its area parametrization and its properness are inputs here, not independently constructed LQG objects.

## 3. Consequence for retained certificates

Certificates retain the complete raw time ranges and their spatial projections separately; see certificates.tex lines 30–53. Proposition 'tree:prop:certificate_limit'(1) asserts actual path approximants for finite-cost certificates. Suppose such a certificate has spatial range $K\Subset Q^\circ$ and the asserted joint raw/spatial convergence holds in a fixed contour window. Its approximants satisfy (2). Equations (5) and the localization lemma make every sufficiently late approximating path internal to $[a,b]$, with unchanged cost. The same conclusion holds with any finite number of ordered marks.

This is an interior-only lifting statement for actual sewn-graph approximants. It does not establish that arbitrary formal chart paths have actual approximants; the general realization and conditional-kernel assertions of 'tree:lem:chart_reconstruction' are distinct. Nor does range restriction recover an earlier instruction graph with disabled windows: that graph has extra restrictions absent from the internal graph of one complete interval.

## 4. The nonzero-local-cost contradiction, conditional on remaining inputs

The following lists the additional inputs needed to apply the result to 'tree:lem:nonzero_local_cost'.

1. The cell $Q=\eta([0,1])$ has connected open interior, with times $a_j\downarrow0$, $b_j\uparrow1$ whose images are interior points.
2. Local certificates have the actual approximants above. The local joining assertion of Proposition 'tree:prop:certificate_limit'(2) holds: endpoints converging to a common spatial point can be joined with vanishing cost in any prescribed small open neighborhood.
3. The unit internal endpoint costs have a jointly retained almost sure limit $X$. The internal time modulus provides random errors $e_j\to0$ almost surely bounding the limsup of the sum of the normalized tip-interval costs on $[0,a_{j,n}]$ and $[b_{j,n},1]$, where $a_{j,n}\to a_j$ and $b_{j,n}\to b_j$ are grid choices.
4. All compactly local limiting certificate costs vanish simultaneously for the pairs and open sets used. Moment conclusions additionally assume uniform integrability of the kth powers.

Fix $j$ large enough that $a_j<b_j$. A connected open subset of a surface is path connected: the points reachable by paths form an open subset with open complement, by local path connectedness. Join $\eta(a_j)$ to $\eta(b_j)$ by a continuous path in $Q^\circ$. Its range is compact. Cover it by finitely many neighborhoods with compact closure in $Q^\circ$ and subdivide it so consecutive subdivision points share a neighborhood.

For any $\varepsilon>0$, input 4 supplies finitely many local certificates between these points with total cost at most $\varepsilon$, each confined to its neighborhood. Approximate them by actual paths. Input 2 joins the finitely many mismatched representatives, including the outer endpoints to $a_{j,n},b_{j,n}$, with total extra cost tending to zero. Choose joining neighborhoods with compact closure in $Q^\circ$. All these middle paths have projected ranges approaching one compact subset of $Q^\circ$. Section 1 makes them internal to $[0,1]$.

Prepend and append the two internal tip paths. The internal triangle inequality and input 3 give

\[
                              0\le X\le e_j+\varepsilon.        \tag{6}
\]

Here $j$ and $\varepsilon$ are fixed before taking the resolution limit. Intersect the events for countably many $j$ and positive rational $\varepsilon$, send $\varepsilon\downarrow0$, and then $j\to\infty$. This gives $X=0$ almost surely. Uniform integrability forces the approximating kth moments to tend to zero. A positive retained kth moment is consequently impossible under these hypotheses.

Input 3 is explicitly a joint-limit modulus assertion; a bound in probability at one resolution is not substituted for it. The disk-cell assertion, local joining and construction of jointly convergent certificates remain inputs. So does the implication from ambient upper comparison constants tending to zero to input 4. The argument proves the interior lifting and this deterministic contradiction, conditional on those inputs; it does not independently prove the full nonzero-local-cost lemma in the planar-map construction.

## 5. Attempts to break the argument

The interior margin is necessary. For $\eta(t)=t$ on $[-1,2]$, $I=[0,1]$, and the boundary compact $K=\{0\}$, representatives $-1/n$ project towards $K$ but never lie in $I$. The preimage condition is necessary too: with $\eta(t)=t^2$ on $[-1,1]$, $I=[0,1]$, and $K=\{1/4\}\Subset\eta(I)^\circ$, the outside representative $-1/2$ persists. This curve does not satisfy the swept-area hypothesis in Section 2.

The one-mesh-step buffer in the vertical-edge argument cannot be omitted. Take successive increments $(0,1),(1,0),(0,-1)$. The vertical match has terminal indices $u=1,v=3$ and primal representatives $0,2$. Both representatives lie in $[0,2]$, but the down-step ending at $3$ does not. That vertical edge is absent from the internal graph of $[0,2]$. The fixed margin in (3), together with $h_n\to0$, excludes the case. The statement concerns this edge occurrence even though another route between its endpoints is available.

The script [audit.py](audit.py) compares two independent discrete implementations, minimum tests and stack matching, on every axial walk through length seven and every subinterval. It tests restriction of first-coordinate equivalence, complete-step restriction of vertical matches, the boundary case above, the earlier moment-bound exponents, and exact main-theorem quotations. Finite enumeration checks the sewing rules; the compactness argument handles unbounded path lengths and continuum limits.

The next unverified passage is bootstrap.tex lines 120–129: whether ambient comparisons with constants tending to zero provide zero-cost certificates for every compact local route in a joint limit, uniformly enough for changing laws and quantum-scale zooms. This requires the coupled reference metric and upper-certificate realization/closure inputs. The present argument does not establish them, the field-local kernels, full GHP convergence, or a positive-q distance exponent.
