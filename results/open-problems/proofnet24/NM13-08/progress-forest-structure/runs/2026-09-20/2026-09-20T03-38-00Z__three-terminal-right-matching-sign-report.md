Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-08 / T07 — a three-terminal nilpotent transfer algebra and strict p-NC for matching-augmented `K_{3,n}`

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and why this is a genuinely different attack

The preceding NM13-08 work developed two-terminal generating-polynomial machinery: exact edge-substitution factorization, PF-Rayleigh series/parallel closure, transparent substitution into unit-p-NC cores, arbitrary-internal transparent insertion, and explicit transparent non-series-parallel neutralizers. NM13-04 independently developed terminal-partition transfers for split-3, split-4 and split-5 families, most recently an activity-2 split-5 atom and recursively decorated bicliques.

The preserved P14 history is also important here. P14 completed the dense nine-vertex sector, restored Cocks's fixed-graph implication from the unit source inequality to all-positive-weight independence correlation, reduced a vertex-minimal source counterexample to a 3-connected graph by block/two-separator transfer, and isolated the still-unresolved degree-three mixed-polarization obstruction. In particular, Cocks also proves correlated matroids closed under 2-sum. Therefore I do **not** claim that another two-terminal edge replacement is a new general closure theorem; that would overstate novelty.

This run instead moves to a genuinely three-terminal decomposition. The new layer has two right-side vertices joined by an **internal matching edge**, so it is not a two-sum/edge-substitution gadget. Its five terminal-partition states collapse to a common nilpotent algebra with the ordinary `K_{3,n}` star layer. This gives an exact all-parameter sign theorem for

\[
G_{k,r}:=K_{3,\,2k+r}+M_k,
\]

where `M_k` is a matching of size `k` placed inside the `(2k+r)`-vertex side. The theorem holds for every `k>=1,r>=0`; the tail `k>=28` is beyond the current repository's complete-bipartite-width-30 minor route and beyond the split-5 minor closure.

`POSTED.md` was respected. No posted source theorem is reopened and no parent closure is claimed. Novelty/priority of the exact three-terminal matching-layer theorem is **UNVERIFIED**; bounded public searching on 20 September 2026 did not surface this exact family or transfer identity.

## 1. Parent theorem before/after, separate from mechanism gain

For a finite graph `G=(V,E)`, write its forest generating polynomial

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\]

and for distinct edges `e,f`

\[
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation for the uniform measure on **all** forests, with every component count mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph vertex order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid counterexample-order lower bound:** `>=10 -> >=10`.

No complete-order metric moves in this run.

The **demonstrated mechanism scope** does move:

* before: two-terminal PF/substitution theory and fixed split-family terminal transfers;
* after: a new **three-terminal layer algebra** with a nontrivial internal right-side edge, exact marked-layer commutation, and a complete 14-orbit sign certificate proving strict unit p-NC for every `G_{k,r}`, `k>=1,r>=0`.

This is not finite enumeration: `k` and `r` are arbitrary and the proof is symbolic in both parameters.

## 2. Exact recovered source, P14 and literature scope

Only dependencies needed for this argument were reread.

### Grimmett–Winkler and P14

Grimmett and Winkler, `math/0302185`, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444–460, study the uniform measure on **all forests**. Their published computation verifies the conjectured pairwise inequality for every graph with at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree negative-correlation theorem; a spanning-tree theorem is not the present problem.

Repository P14/HARD10 continuity supplies the complementary dense nine-vertex sector (`19..36` edges), giving all simple graphs through nine vertices. P14 also records the fixed-graph Cocks correction: if the unit Grimmett–Winkler inequality holds for a graph `G`, then the graphic matroid is independence correlated, i.e. the Rayleigh inequalities hold for all positive edge weights. This is a graph-by-graph implication, not merely a class statement. Together with the two-separator transfer it implies that a vertex-minimal source counterexample may be taken 3-connected.

The P14 degree-three star/mesh attack remains incomplete in general. Its exact mixed-polarization term is not universally nonnegative, and the proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex witness while that graph's actual source Rayleigh gap remained positive. This run does not revive that false sufficient condition.

### Cocks / Semple–Welsh

Semple–Welsh formulate the generalized weighted independence-correlation property. Their final paper notes Cocks's fixed-graph result, and Cocks, *Correlated Matroids*, CPC 17 (2008), 511–518, proves the equivalence relevant to the Grimmett–Winkler conjecture and proves that 2-sums of correlated matroids remain correlated. Thus the genuinely new point sought here must go beyond another one-edge/two-terminal sum.

### Erickson and later work

Erickson, `arXiv:1008.3660`, proves a sum-of-squares formula for the spanning-forest Rayleigh difference of every series-parallel graph, yielding the stronger all-positive-weight independent-set-Rayleigh property there.

Huang, `arXiv:2311.00965` / Statistics & Probability Letters 213 (2024), treats arboreal-gas negative correlation in restricted settings and continues to describe the general problem as open.

Bado, DOI `10.1016/j.spl.2026.110960`, proves strict pairwise negative edge correlation for every wheel under the uniform-all-forests law. Wheels are an infinite 3-connected non-series-parallel family, but are planar and structurally different from the nonplanar family proved below.

Tang–Zhang, `arXiv:2603.10738` (11 March 2026), prove p-NC for specified complete-graph spanning-subgraph ensembles, including forests with a **fixed number of components** for fixed `k` and sufficiently large `n`. That is not the arbitrary-graph uniform law on all forests used here.

The current PROB10-07 repository theorem proves unit p-NC for complete bipartite `K_{a,b}` whenever `min(a,b)<=30`. That result is used only to compare coverage below; the proof here does not depend on it.

## 3. The new graph class

Fix integers `k,r>=0`. Let

\[
L=\{0,1,2\},\qquad |R|=2k+r.
\]

Join every vertex of `L` to every vertex of `R`, and inside `R` add exactly `k` pairwise vertex-disjoint edges. There are no other edges. Call the graph `G_{k,r}`. Thus

\[
|V(G_{k,r})|=3+2k+r,
\qquad
|E(G_{k,r})|=3(2k+r)+k=7k+3r.
\]

For `k=0` this is the bare biclique `K_{3,r}`. The new regime is `k>=1`, where every matching edge together with any left vertex forms a triangle.

### Theorem `T07-K3N-RIGHT-MATCHING-PNC-09`

For every `k>=1` and `r>=0`, and every two distinct present edges `e,f` of `G_{k,r}`,

\[
\boxed{\Delta_{G_{k,r}}(e,f)>0.}
\]

Hence the uniform measure on **all forests** of `G_{k,r}` has strict pairwise negative edge correlation.

The proof is an exact two-parameter terminal-partition calculation, not interpolation from finitely many `(k,r)` values.

## 4. New decomposition lemma: the three-terminal layer algebra

Track only the connectivity partition induced on the three fixed left terminals. There are five states:

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

A layer is glued to the same three terminals, with fresh interior. A transfer entry counts acyclic edge subsets of the new layer that take the incoming terminal partition to the outgoing one. Because a new layer may only coarsen terminal connectivity, every transfer matrix is upper triangular in the order above.

### 4.1 Ordinary star layer

One ordinary right vertex has three incident edges, one to each terminal. Exhausting its `2^3` edge subsets gives

\[
S=\begin{pmatrix}
4&1&1&1&1\\
0&4&0&0&2\\
0&0&4&0&2\\
0&0&0&4&2\\
0&0&0&0&4
\end{pmatrix}.
\tag{4.1}
\]

Set

\[
N=S-4I.
\]

Direct multiplication gives

\[
\boxed{N^3=0,\qquad N^2\ne0.}
\tag{4.2}
\]

### 4.2 Matched-pair layer

A matched-pair layer consists of two fresh right vertices `p,q`, each joined to all three terminals, plus the internal edge `h=pq`. Exhausting its `2^7` edge subsets gives

\[
P=\begin{pmatrix}
23&12&12&12&22\\
0&23&0&0&24\\
0&0&23&0&24\\
0&0&0&23&24\\
0&0&0&0&23
\end{pmatrix}.
\tag{4.3}
\]

The key exact identity is

\[
\boxed{P=23I+12N+\frac53N^2.}
\tag{4.4}
\]

Therefore `S` and `P` lie in the same three-dimensional commutative algebra `span{I,N,N^2}`.

### Lemma `T07-THREE-TERMINAL-MATCHING-ALGEBRA-09`

For arbitrary nonnegative integers `k,r`, the unmarked transfer of `k` matched-pair layers and `r` ordinary layers is independent of layer order and equals

\[
P^kS^r=23^k4^r\bigl(I+u_{k,r}N+v_{k,r}N^2\bigr),
\tag{4.5}
\]

where

\[
u_{k,r}=\frac{12k}{23}+\frac r4,
\tag{4.6}
\]

and

\[
v_{k,r}
=\frac{5k}{69}+\frac{72k(k-1)}{529}
 +\frac{r(r-1)}{32}+\frac{3kr}{23}.
\tag{4.7}
\]

Moreover every transfer matrix obtained by requiring one or two specified edges in a single layer commutes with every disjoint unmarked layer transfer.

#### Proof

Equation (4.5) follows by the binomial theorem truncated at `N^2` because `N^3=0`; (4.6)–(4.7) are the resulting coefficients. The marked commutation has both an algebraic and a combinatorial proof. Algebraically, the exact five-state matrices in the checker commute. Combinatorially, adding two disjoint layers in either order enumerates exactly the same pairs of layer forests, and the final terminal partition depends only on their union. Requiring a fixed local edge in one layer does not alter this bijection. QED.

This is the new decomposition step: the internal matching edge is genuinely a three-terminal interaction, but it still lands in a rank-three nilpotent response algebra.

## 5. Exact forest generating count

Start from state `D`, represented by row vector `d=(1,0,0,0,0)`, and sum over all final states with the all-ones column `1`. Equations (4.5)–(4.7) give

\[
Z_{k,r}:=I_{G_{k,r}}(\mathbf1)
=23^k4^r\,d\bigl(I+u_{k,r}N+v_{k,r}N^2\bigr)\mathbf1.
\]

After simplification,

\[
\boxed{
Z_{k,r}
=23^k4^r\,
\frac{6912k^2+6624kr+14432k+1587r^2+6877r+8464}{8464}.
}
\tag{5.1}
\]

The exact checker independently brute-forces small instances and recovers (5.1):

* `G_{1,1}`: `|V|=6`, `|E|=10`, `Z=488`;
* `G_{2,0}`: `|V|=7`, `|E|=14`, `Z=4061`;
* `G_{2,1}`: `|V|=8`, `|E|=17`, `Z=21672`.

For a theorem-only instance beyond the complete nine-vertex census, `G_{4,0}` has `11` vertices, `28` edges and `Z=5,844,921`.

## 6. Complete sign proof: 14 edge-pair orbits

The automorphism group contains

\[
S_3\times(S_2\wr S_k)\times S_r,
\]

acting on the three left terminals, on the `k` matched right pairs (including endpoint swaps), and on the `r` ordinary right vertices. Therefore every unordered pair of distinct edges falls into one of exactly fourteen templates when the corresponding layers exist.

Call a spoke from an ordinary right vertex an `O` edge; inside a matched layer call its internal matching edge `h` and its six left-right edges `M` spokes. The fourteen templates are:

1. two `O` spokes in the same ordinary layer, different terminals;
2. two `O` spokes in different ordinary layers, same terminal;
3. two `O` spokes in different ordinary layers, different terminals;
4. `h` and a spoke in the same matched layer;
5. two spokes at the same endpoint of one matched edge, different terminals;
6. two spokes at opposite endpoints of one matched edge, same terminal;
7. two spokes at opposite endpoints of one matched edge, different terminals;
8. two `h` edges in distinct matched layers;
9. `h` in one matched layer and a spoke in another;
10. spokes in distinct matched layers, same terminal;
11. spokes in distinct matched layers, different terminals;
12. `h` and an `O` spoke;
13. matched spoke and `O` spoke, same terminal;
14. matched spoke and `O` spoke, different terminals.

For each edge or pair of edges, replace the corresponding unmarked layer matrix by the exact marked transfer matrix obtained by requiring those edges present. By Lemma 4.9 these marked matrices can be moved next to the initial state, leaving only a power `P^{k-a}S^{r-b}`. Hence every derivative entering a Rayleigh difference is an explicit polynomial in `k,r` of degree at most two after the positive base factors `23^k4^r` are removed. Every Rayleigh gap is therefore an explicit polynomial of degree at most four.

For same-layer pairs one bookkeeping factor is necessary. Two first derivatives remove the layer's base factor twice, while a second derivative removes the layer once. Thus the normalized Rayleigh formulas have the form

\[
\widehat\Delta_{OO}^{\rm same}=o_eo_f-4Z\,o_{ef},
\tag{6.1}
\]

and

\[
\widehat\Delta_{MM}^{\rm same}=m_em_f-23Z\,m_{ef}.
\tag{6.2}
\]

For distinct-layer and mixed-layer pairs there is no extra factor.

The attached checker constructs every marked matrix directly from edge subsets and verifies all fourteen signs symbolically. For each orbit let `(k_0,r_0)` be the minimum layer counts needed for that orbit. After the substitution

\[
K=k-k_0\ge0,\qquad R=r-r_0\ge0,
\]

the exact numerator has **only positive nonzero coefficients** in `K,R` (zero coefficients are simply absent). The certificate summary is:

| orbit | `(k_0,r_0)` | positive denominator | nonzero monomials | smallest nonzero coefficient |
|---|---:|---:|---:|---:|
| O same layer, different terminal | (0,1) | 71639296 | 14 | 2518569 |
| O different layers, same terminal | (0,2) | 67712 | 6 | 21689 |
| O different layers, different terminal | (0,2) | 67712 | 6 | 8993 |
| same M layer: h/spoke | (1,0) | 17909824 | 15 | 7555707 |
| same M layer: same endpoint, different terminals | (1,0) | 71639296 | 15 | 62964225 |
| same M layer: opposite endpoints, same terminal | (1,0) | 35819648 | 15 | 2518569 |
| same M layer: opposite endpoints, different terminals | (1,0) | 35819648 | 15 | 2518569 |
| different M layers: h/h | (2,0) | 279841 | 6 | 38088 |
| different M layers: h/spoke | (2,0) | 279841 | 6 | 261855 |
| different M layers: spokes, same terminal | (2,0) | 2238728 | 6 | 24476301 |
| different M layers: spokes, different terminal | (2,0) | 2238728 | 6 | 9364887 |
| mixed h/O | (1,1) | 48668 | 6 | 7935 |
| mixed spoke/O, same terminal | (1,1) | 389344 | 6 | 728433 |
| mixed spoke/O, different terminal | (1,1) | 389344 | 6 | 290421 |

Two of the longer shifted numerators illustrate why the domain shift is useful. For the first orbit, after `r=R+1`, the numerator is

\[
\begin{aligned}
&47775744K^4+91570176K^3R+199507968K^3
 +65816064K^2R^2+286262784K^2R+286286848K^2\\
&\quad+21024576KR^3+136913664KR^2+273251776KR+149508096K\\
&\quad+2518569R^4+21827598R^3+65202953R^2+71639296R,
\end{aligned}
\tag{6.3}
\]

which is nonnegative and is positive whenever either `K>0` or `R>0`. The sole zero boundary `(k,r)=(0,1)` is the three-edge star, whose edge indicators are in fact independent. In the new regime `k>=1`, (6.3) is strict.

For two spokes at the same endpoint of one matched layer, after `k=K+1` the numerator is

\[
\begin{aligned}
&1194393600K^4+2289254400K^3R+7124336640K^3
 +1645401600K^2R^2+10227985920K^2R+14992073728K^2\\
&\quad+525614400KR^3+4894561920KR^2+14327893056KR+12532949504K\\
&\quad+62964225R^4+780756390R^3+3423294953R^2
 +5995313584R+2579014656,
\end{aligned}
\tag{6.4}
\]

strictly positive for every `K,R>=0`.

The other twelve certificates are generated from the same exact five-state matrices and archived by the checker. Since the fourteen templates exhaust all distinct edge pairs, this proves Theorem `T07-K3N-RIGHT-MATCHING-PNC-09`. QED.

As independent sanity checks, direct subset enumeration gives minimum unit Rayleigh numerators

\[
448\quad(G_{1,1}),\qquad
3300\quad(G_{2,0}),\qquad
69696\quad(G_{2,1}),
\]

all strictly positive.

## 7. Why the application is genuinely outside current covered mechanisms

This needs a stronger argument than merely saying that the pictures look different.

### 7.1 Beyond split-5 and its minor closure

The vertex-cover number of `G_{k,r}` is exactly

\[
\boxed{\tau(G_{k,r})=\min(2k+r,\,k+3).}
\tag{7.1}
\]

Indeed, if a vertex cover omits any left vertex, then every right vertex must belong to the cover, giving size at least `2k+r`. If all three left vertices are included, the `k` internal matching edges still require one endpoint each, giving size at least `k+3`. Both bounds are attained.

Every `K_5\vee\overline{K_n}` has a vertex cover of size five, and vertex-cover number cannot increase under taking a minor. Hence for `k>=3`, where `tau(G_{k,r})>=6`, these graphs do not lie in the minor closure of NM13-04's split-5 family.

### 7.2 Beyond the current biclique-width-30 route

There is a useful comparison. `G_{k,r}` is a minor of

\[
K_{k+3,\,2k+r}:
\]

use three left vertices as the final `L`, use one extra left auxiliary vertex for each desired matching edge, delete each auxiliary's edges except those to its designated right pair, and contract one of those two remaining edges. Thus the current PROB10 theorem for `min(a,b)<=30` already implies this class for the range in which `min(k+3,2k+r)<=30`.

But (7.1) shows that this route cannot cover the tail `k>=28`: then

\[
\tau(G_{k,r})\ge31.
\]

Every minor of every biclique with `min(a,b)<=30` has vertex-cover number at most 30. Therefore **every `G_{k,r}` with `k>=28` is genuinely beyond the current width-30 biclique theorem even after allowing minor closure.** This supplies an unbounded new parameter direction rather than a finite decoration of known cases.

### 7.3 Beyond series-parallel graphs and wheels

Whenever `2k+r>=3`, the graph contains `K_{3,3}` as a subgraph, so it is nonplanar. Hence it is not series-parallel and is not a wheel or a minor of a wheel. The theorem is therefore structurally distinct from Erickson's series-parallel class and Bado's wheel class.

A concrete first point in the genuinely new tail is

\[
G_{28,0}:\qquad |V|=59,\quad |E|=196,\quad \tau=31,
\]

and the theorem covers `G_{k,r}` for every larger `k` and arbitrary `r` as well.

## 8. Relation to Cocks after the new unit theorem

Cocks's fixed-graph implication can now be applied **after** Theorem 3.1: each individual `G_{k,r}` is not only unit-p-NC but independence correlated at all positive real edge weights. This is a corollary of the new unit theorem plus existing literature, not an ingredient smuggled into the three-terminal proof.

This distinction matters. The layer theorem creates new unit source-valid graphs outside the previously certified minor ranges; Cocks then upgrades each newly proved graph to its weighted graphic-matroid statement.

## 9. Exact artifacts and execution

Exact checker:

`proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T03-38-00Z__right-matching-transfer-checker.py`

Archived executed output:

`proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T03-38-00Z__right-matching-transfer-checker.out`

The checker:

1. constructs the five terminal partitions from first principles;
2. enumerates all `2^3` ordinary-star and `2^7` matched-pair layer subsets;
3. verifies `N^3=0` and `P=23I+12N+(5/3)N^2`;
4. constructs every marked one-edge and two-edge transfer used by the fourteen pair orbits;
5. verifies exact commutation;
6. derives the symbolic two-parameter Rayleigh gaps;
7. shifts to each orbit's exact existence domain and verifies every nonzero coefficient is positive;
8. directly brute-forces three small physical graphs as an independent check.

The archived output terminates

`ALL_EXACT_CHECKS_PASS`.

## 10. What did not move and the next obstruction

The arbitrary-graph conjecture remains OPEN and the complete all-graph cutoff remains nine vertices. The new algebra is special: it exploits a common three-terminal interface and a right-side graph of maximum degree one. It does **not** prove arbitrary 3-sum closure, arbitrary degree-three elimination, or p-NC for all 3-connected graphs.

The next natural attack is therefore not another certificate for the same matching class. Replace a matched-pair layer by a **three-right-vertex path layer** (two internal right-side edges). If its unmarked and marked terminal transfers stay inside a tractable extension of the same nilpotent algebra and the pair-orbit gaps remain in a positive coefficient cone, the theorem would expand from right-side matchings to right-side linear forests. If the path layer breaks commutation or sign, the exact failing orbit will identify the first genuine obstruction to this three-terminal decomposition.

## ledger_delta

```yaml
status: PARTIAL_PARENT__CANDIDATE_FULL_RESTRICTED
parent: T07 uniform-all-forests p-NC
parent_before_after: OPEN -> OPEN; complete all-graph order 9 -> 9
new_lemma: T07-THREE-TERMINAL-MATCHING-ALGEBRA-09
new_theorem: T07-K3N-RIGHT-MATCHING-PNC-09
new_scope: strict p-NC for G_{k,r}=K_{3,2k+r}+M_k for every k>=1,r>=0
uncovered_tail: k>=28, since tau(G)>=31 excludes minors of current min-side<=30 biclique coverage; k>=3 also excludes split-5 minor closure
certificate: 14 exact edge-pair orbit polynomials; all admissibly shifted numerators coefficientwise nonnegative, strict for k>=1
parent_metric_movement: none
residual_obstruction: arbitrary 3-connected graphs / general 3-sum remain uncontrolled
next_attack: three-terminal path layer, aiming from matching to linear-forest structure on the large side
```

END OF REPORT
