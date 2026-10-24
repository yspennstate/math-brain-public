Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-08 / T07 — one-port-field Rayleigh closure under series/parallel macro-decomposition

Status: **PARTIAL on the parent conjecture / CANDIDATE_FULL for the restricted theorems below, pending later independent review.** The arbitrary-finite-graph uniform-forest conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and this run's new direction

The two preceding NM13-08 runs established:

1. an exact two-terminal substitution formula for the forest generating polynomial and every Rayleigh difference, with the cross-edge sign factor
   \[
   J_Q(p):=D_Q C_{Q,p}-C_QD_{Q,p};
   \]
2. a transparent-port closure: if a two-terminal gadget has unit activity `t=C/D=1` and its completion by the port edge is I-Rayleigh, it may replace an edge of an arbitrary **unit-only** p-NC core;
3. a series/parallel calculus for terminal activity and `J`, yielding infinitely many exact unit-transparent theta gadgets and arbitrary theta expansions of wheel graphs.

The companion NM13-04 has independently proved strict unit p-NC for every
\[
K_4\vee\overline{K_n},\qquad n\ge1,
\]
by a complete 15-state partition transfer. I do not reprove or relabel that unit theorem.

This run takes a materially stronger decomposition direction. Instead of forcing activity `t=1`, it introduces a **one-port-field Rayleigh property**: only the distinguished virtual port edge is allowed to vary over all `s>=0`, while all real edges stay at unit weight. I prove:

* this weaker-than-I-Rayleigh property is closed under both terminal **parallel and series composition**;
* the port-deleted split atoms
  \[
  Q_n=(K_4\vee\overline{K_n})-g
  \]
  have this one-port-field property for every `n>=1`, for a clique edge `g`;
* therefore any finite series/parallel expression tree whose leaves are arbitrary `Q_{n_i}` is p-NC at unit weights.

This yields a new all-parameter class built from non-series-parallel split atoms, complementary to NM13-04's single 4-connected split family.

`POSTED.md` was checked through the current T07 reports; the parent conjecture and the restricted results here are not treated as posted/settled. Novelty/priority of the exact closure formulation is **UNVERIFIED**.

## 1. Parent theorem before/after — kept separate from mechanism gain

For a finite simple graph `G=(V,E)`, let
\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e.
\]
For distinct edges `e,f`,
\[
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]
At unit weights, `Delta_G(e,f)>=0` is exactly
\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F)
\]
for the uniform measure on **all** acyclic spanning edge subsets. Isolated vertices and all component counts are allowed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-graph vertex order in the repository:** `9 -> 9`.  
**Counterexample-order lower bound:** `>=10 -> >=10`.

This run therefore does **not** move the complete all-graph finite-order metric.

The mechanism scope does move:

* **before:** transparent (`t=1`) substitutions and transparent theta expansions;
* **after:** one-port-field Rayleigh closure under arbitrary terminal series/parallel macro-composition, with a new unbounded non-series-parallel atom family `Q_n`.

## 2. Recovered exact literature/P14 scope

Only the dependencies needed for this proof were reread.

### Grimmett--Winkler

Grimmett--Winkler, `math/0302185`, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444--460, studies the uniform measure on all forests, separately from the uniform spanning-tree law. Their numerical verification covers every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly note that pairwise negative association is already known for uniform spanning trees; that theorem is not the uniform-forest conjecture.

### P14 repository continuation

The preserved P14/HARD10 work fills the complementary dense nine-vertex sector, giving exact unit-weight coverage of every simple graph through nine vertices. P14 also preserves:

* block/direct-sum factorization, reducing a vertex-minimal counterexample to 2-connected;
* a two-separator transfer plus the fixed-graph balanced-to-weighted implication, reducing a vertex-minimal counterexample further to 3-connected;
* exact one-edge-field quadratics as a useful local invariant.

P14's failed generic routes remain failed: the degree-three star/mesh elimination leaves a mixed three-terminal polarization term; universal nonnegativity of that mixed term is false; the reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex graph; Lorentzian/complete-log-concavity and naive stability/Garding shortcuts still lack the hypothesis needed to force entrywise Rayleigh signs.

### Erickson and later work

Erickson, `arXiv:1008.3660`, defines the stronger **I-Rayleigh** property: every Rayleigh difference is nonnegative at every positive evaluation of all edge weights. His Theorem 1.2 gives a sum-of-squares proof for series-parallel graphs. The paper also records earlier work of Cocks, Semple--Welsh and Wagner showing closure of I-Rayleigh graphs under two-sums.

The theorem below is different: real edges remain at weight `1`; only one virtual port edge varies. This is strictly less data than full I-Rayleigh, and the split atoms used below are **not** claimed I-Rayleigh under arbitrary simultaneous edge weights.

Recent bounded checks retain the same distinction:

* Huang, `arXiv:2311.00965`, treats negative correlation for arboreal gas in specific regimes and describes the general problem as open.
* Bado, *Negative edge correlation for uniform random forests on wheel graphs*, Statistics & Probability Letters 241, 110960, proves strict p-NC for all wheels under the uniform-all-forests law.
* Tang--Zhang, `arXiv:2603.10738`, proves p-NC for specified families of spanning subgraphs of `K_n`, including forests with a **fixed number of components** for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph, all-component-count law here.

Fresh bounded searches for the exact combination “uniform forest + one-edge Rayleigh field + two-terminal series/parallel composition + split graph atom” did not surface the theorem below. That miss is negative evidence only.

## 3. Two-terminal notation and the one-port-field property

Let `Q` be a two-terminal graph with terminals `x,y`, with all **real** edge weights fixed at `1`. Split its forest sum as
\[
I_Q=D_Q+C_Q,
\]
where `D_Q` counts forests in which `x,y` are disconnected and `C_Q` counts forests in which they are connected. Write
\[
t_Q=\frac{C_Q}{D_Q}\ge0.
\]

For a real edge `p` of `Q`, define
\[
J_Q(p)=D_QC_{Q,p}-C_QD_{Q,p}.
\]

Let `\widehat Q(s)` be obtained by adjoining a new terminal edge `g=xy` of weight `s>=0`. Then
\[
I_{\widehat Q(s)}=I_Q+sD_Q=C_Q+(1+s)D_Q,
\tag{3.1}
\]
and
\[
\Delta_{\widehat Q(s)}(p,g)=J_Q(p),
\tag{3.2}
\]
independent of `s`.

### Definition: PF-Rayleigh

Call `Q` **PF-Rayleigh** (one-port-field Rayleigh) if for every `s>=0`,
\[
\Delta_{\widehat Q(s)}(e,f)\ge0
\]
for every distinct pair of edges in `\widehat Q(s)`.

This property is weaker than I-Rayleigh: all real edges are frozen at `1`, and only the virtual port edge varies.

## 4. New closure theorem: PF-Rayleigh is closed under terminal parallel and series composition

### Theorem `T07-PORT-FIELD-SP-CLOSURE-06`

Let `Q_1,Q_2` be PF-Rayleigh two-terminal graphs with disjoint interiors.

1. Their terminal parallel composition `Q_1 || Q_2` is PF-Rayleigh.
2. Their terminal series composition `Q_1 o Q_2` is PF-Rayleigh.

Hence every finite series/parallel expression tree whose leaves are PF-Rayleigh two-terminal graphs is PF-Rayleigh.

### Proof: parallel composition

Write `D_i,C_i,I_i,t_i,J_i` for `Q_i`. For
\[
Q=Q_1\parallel Q_2
\]
the standard acyclic-union classification gives
\[
D_Q=D_1D_2,\qquad
C_Q=C_1D_2+D_1C_2.
\tag{4.1}
\]

After adding the outer port edge of weight `s`,
\[
\begin{aligned}
I_{\widehat Q(s)}
 &= I_Q+sD_Q\\
 &=D_2\left[I_1+(s+t_2)D_1\right]\\
 &=D_2\,I_{\widehat Q_1(s+t_2)}.
\end{aligned}
\tag{4.2}
\]

Therefore for two real edges `p,q in Q_1`,
\[
\boxed{
\Delta_{\widehat Q(s)}(p,q)
 =D_2^2\,
 \Delta_{\widehat Q_1(s+t_2)}(p,q)\ge0.
}
\tag{4.3}
\]
The symmetric statement handles pairs inside `Q_2`.

For `p in Q_1`, `q in Q_2`, direct differentiation of
\[
I_Q=D_1D_2+C_1D_2+D_1C_2
\]
gives the exact factorization
\[
\boxed{
\Delta_{\widehat Q(s)}(p,q)=J_1(p)J_2(q).
}
\tag{4.4}
\]
The outer port weight cancels. By (3.2), each `J_i` is itself a port-edge Rayleigh difference in `\widehat Q_i`, hence is nonnegative.

Finally, for `p in Q_1`,
\[
\boxed{
J_Q(p)=D_2^2J_1(p)\ge0,
}
\tag{4.5}
\]
and symmetrically on side 2. Thus all pairs, including pairs with the new outer port edge, are nonnegative for every `s>=0`. This proves parallel closure.

### Proof: series composition

Let
\[
Q=Q_1\circ Q_2
\]
by identifying the second terminal of `Q_1` with the first terminal of `Q_2`. Any union of constituent forests is acyclic, and the outer terminals connect iff both pieces connect, so
\[
C_Q=C_1C_2,\qquad
D_Q=D_1I_2+C_1D_2.
\tag{4.6}
\]

Add an outer port edge of weight `s`. Then
\[
I_{\widehat Q(s)}
=I_1I_2+s(D_1I_2+C_1D_2).
\tag{4.7}
\]

For real edges in `Q_1`, factor (4.7) as
\[
I_{\widehat Q(s)}
=(I_2+sD_2)
\left[C_1+(1+r_1)D_1\right],
\tag{4.8}
\]
where
\[
\boxed{
r_1=\frac{sC_2}{I_2+sD_2}\ge0.
}
\tag{4.9}
\]
The bracket in (4.8) is exactly `I_{\widehat Q_1(r_1)}`. Hence
\[
\boxed{
\Delta_{\widehat Q(s)}(p,q)
=(I_2+sD_2)^2
\Delta_{\widehat Q_1(r_1)}(p,q)\ge0
}
\tag{4.10}
\]
for `p,q in Q_1`; the symmetric formula handles pairs in `Q_2`.

For a cross pair `p in Q_1`, `q in Q_2`, expanding (4.7) and cancelling gives
\[
\boxed{
\Delta_{\widehat Q(s)}(p,q)
=s(1+s)J_1(p)J_2(q)\ge0.
}
\tag{4.11}
\]

For a real edge `p in Q_1`, the outer-port difference is
\[
\boxed{
J_Q(p)=C_2I_2J_1(p)\ge0,
}
\tag{4.12}
\]
and symmetrically on side 2.

Equations (4.10)--(4.12) cover every pair. Thus series composition preserves PF-Rayleigh. Induction on an arbitrary finite expression tree proves the final statement. QED.

### Why this is not Erickson's ordinary two-sum closure

Erickson's cited closure assumes the full I-Rayleigh property of the pieces: all positive real-edge weights may vary. Here each atom only needs a **single distinguished port field** with every other real edge frozen at `1`. The proof works because the series/parallel reductions send the outer field `s` to another single nonnegative scalar field (`s+t_2` in parallel, `sC_2/(I_2+sD_2)` in series). No simultaneous multi-edge weighted hypothesis is introduced.

## 5. New atom theorem: split graphs are Rayleigh along a clique-port field

Let
\[
H_n=K_4\vee\overline{K_n},\qquad n\ge1,
\]
with clique terminals `0,1,2,3`. Fix the clique edge
\[
g=01
\]
and define the port-deleted atom
\[
Q_n=H_n-g
\]
with terminals `0,1`.

### Theorem `T07-SPLIT4-ONE-PORT-FIELD-07`

For every integer `n>=1`, `Q_n` is PF-Rayleigh. Equivalently, if the distinguished edge `g=01` is restored with arbitrary weight `s>=0`, while every other edge has weight `1`, then every Rayleigh difference is nonnegative.

For `s>0` the port-completed graph is strictly pairwise Rayleigh; at `s=0` the deletion `Q_n` is pairwise p-NC.

### 5.1 Exact finite-state reduction

NM13-04's 15-state transfer is reused, not rederived from its closed unit formulas.

Process the `n` independent-side vertices one by one and retain the partition of the four clique terminals induced by the partial forest. There are `B_4=15` states. The transfer matrix is
\[
M=5I+N,\qquad N^4=0.
\tag{5.1}
\]
The five diagonal choices are the empty spoke set and four singleton spoke sets; every other legal choice strictly coarsens the terminal partition.

Hence
\[
M^n
=5^nI+n5^{n-1}N+\binom n2 5^{n-2}N^2+\binom n3 5^{n-3}N^3.
\tag{5.2}
\]

Put weight `s` only on the clique port edge `g`. The initial `K_4` vector is therefore
\[
u(s)=u^{(0)}+s\,u^{(1)}.
\tag{5.3}
\]
Every marked count (`Z`, `Z_e`, `Z_{ef}`) is linear in `s`, and after dividing out `5^n` its coefficients are polynomials in `n` of degree at most three. Consequently every non-port Rayleigh difference has the exact form
\[
\boxed{
\Delta_{H_n(s)}(e,f)
=25^n\bigl(a_{ef}(n)+b_{ef}(n)s+c_{ef}(n)s^2\bigr),
}
\tag{5.4}
\]
where `a,b,c` have degree at most six.

The stabilizer of `g` in the clique symmetry, together with symmetry of the independent-side vertices, gives exactly **18 non-port pair orbits** and **4 port-edge pair orbits**. Thus (5.4) is a finite exact symbolic problem.

The attached checker computes the transfer over exact integers, divides by `25^n`, and uses seven exact values of `n` to identify each degree-`<=6` coefficient polynomial. Because the degree bound is proved in (5.2), seven values are an exact interpolation certificate, not an asymptotic or numerical guess. It then reads the identities back on thirteen further values and brute-force checks small physical graphs.

### 5.2 Sign certificate

For 15 of the 18 non-port orbit families, the exact polynomials `a,b,c`, after shifting `n` by the natural lower endpoint (`n>=1` or `n>=2`), have coefficientwise nonnegative expansions, with `a,c>0`. Hence the quadratic in `s` is positive for every `s>=0`.

A sixteenth orbit, labelled in the checker `cs_A_non_otherg`, also has coefficientwise positive `a,b,c` for every `n>=2`. At the only exceptional parameter `n=1`,
\[
25^{-1}\Delta(s)=\frac{148}{25}-\frac{2}{25}s+\frac{64}{25}s^2,
\]
whose discriminant is
\[
-\frac{37884}{625}<0.
\tag{5.5}
\]

Two orbit families have a genuinely negative mixed coefficient for all `n`; these are where a discriminant argument is needed.

#### Exceptional orbit 1: two disjoint `A`-type clique edges

For representatives `02` and `13`,
\[
25^{-n}\Delta(s)=a_1+b_1s+c_1s^2
\]
with
\[
a_1=\frac{4(n^3+34n^2+265n+625)}{625},
\]
\[
b_1=-\frac{n(3n+7)}{125},
\qquad
c_1=\frac{n^2+13n+50}{25}.
\]
Its discriminant is
\[
\boxed{
b_1^2-4a_1c_1
=
-\frac{
16n^5+743n^4+12070n^3+92271n^2+342000n+500000
}{15625}<0.
}
\tag{5.6}
\]

#### Exceptional orbit 2: spokes from different right vertices to the two port endpoints

For representatives `(0,r_1)` and `(1,r_2)`, `r_1\ne r_2`, hence `n>=2`,
\[
25^{-n}\Delta(s)=a_2+b_2s+c_2s^2
\]
with
\[
a_2=
\frac{2(464n^4+13333n^3+144677n^2+700578n+1277298)}
{390625},
\]
\[
b_2=
-\frac{2(104n^3+2536n^2+20009n+51756)}
{78125},
\]
\[
c_2=
\frac{2(74n^2+1023n+3558)}
{15625}.
\]
The discriminant is
\[
\boxed{
b_2^2-4a_2c_2
=
-\frac{4P_6(n)}{6103515625}<0,
}
\tag{5.7}
\]
where
\[
\begin{aligned}
P_6(n)=\;&126528n^6+5317768n^5+93393508n^4\\
&+876893732n^3+4641021935n^2\\
&+13126157904n+15499821600,
\end{aligned}
\]
which is positive for every `n>=0`.

Thus all 18 non-port orbit quadratics are positive for every admissible `n` and every `s>=0`.

### 5.3 Pairs involving the port edge

If one edge is `g`, its Rayleigh difference is independent of `s` by (3.2). The four orbit representatives reduce exactly to the four positive NM13-04 unit formulas:
\[
\Delta(g,A)=
\frac{25^n}{625}
(16n^4+411n^3+3963n^2+17010n+27500),
\tag{5.8}
\]
\[
\Delta(g,D)=
\frac{2\,25^n}{625}
(2n^3+73n^2+675n+1875),
\tag{5.9}
\]
\[
\Delta(g,\text{incident spoke})=
\frac{2\,25^n}{15625}
(176n^4+4731n^3+47450n^2+210443n+348450),
\tag{5.10}
\]
\[
\Delta(g,\text{nonincident spoke})=
\frac{2\,25^n}{15625}
(16n^4+421n^3+4375n^2+21113n+39700).
\tag{5.11}
\]
Every coefficient is positive.

Equations (5.4)--(5.11) prove `T07-SPLIT4-ONE-PORT-FIELD-07`. QED.

### 5.4 Exact terminal activity of the atom

For later composition it is useful to record the unit activity of `Q_n`. From NM13-04's exact counts,
\[
Z(H_n)
=\frac{5^n}{125}(16n^3+327n^2+2182n+4750),
\]
and for a clique edge
\[
Z_g(H_n)
=\frac{5^n}{25}(8n^2+107n+350).
\]
Removing `g` gives
\[
D_{Q_n}=Z_g(H_n),\qquad
C_{Q_n}=Z(H_n)-2Z_g(H_n),
\]
so
\[
\boxed{
t_n=
\frac{16n^3+247n^2+1112n+1250}
{5(8n^2+107n+350)}>0.
}
\tag{5.12}
\]
No matching or transparency condition is needed because the PF closure handles every nonnegative effective field.

## 6. New all-parameter graph class: split-atom series/parallel macro-networks

### Theorem `T07-SPLIT4-MACRONETWORK-08`

For every finite binary series/parallel expression tree `T`, put at each leaf an arbitrary atom
\[
Q_{n_i}=(K_4\vee\overline{K_{n_i}})-g_i,\qquad n_i\ge1,
\]
always using fresh disjoint interiors and composing only by the designated terminal pairs.

Let `G(T;n_1,\dots,n_L)` be the resulting simple graph after forgetting the outer terminal labels. Then the uniform measure on **all** forests of `G` is pairwise negatively edge-correlated.

### Proof

Each leaf `Q_{n_i}` is PF-Rayleigh by Theorem `T07-SPLIT4-ONE-PORT-FIELD-07`. Theorem `T07-PORT-FIELD-SP-CLOSURE-06` propagates PF-Rayleigh inductively through every internal series or parallel node of the expression tree. At the root, evaluate the optional virtual outer port at `s=0`. The remaining real graph is exactly `G`, and every real-edge Rayleigh difference is nonnegative. QED.

### Size parameters

A leaf `Q_n` has
\[
|V(Q_n)|=n+4,\qquad |E(Q_n)|=4n+5.
\]
If the binary expression tree has `L` leaves, `S` series internal nodes and `P` parallel internal nodes (`S+P=L-1`), then
\[
\boxed{
|E(G)|=\sum_{i=1}^L(4n_i+5),
}
\tag{6.1}
\]
\[
\boxed{
|V(G)|=\sum_{i=1}^L(n_i+4)-S-2P.
}
\tag{6.2}
\]

The family is therefore unbounded simultaneously in:

* number of macro-atoms `L`;
* every split parameter `n_i`;
* decomposition-tree topology;
* placement of series versus parallel internal nodes.

### Why this is genuinely outside the preceding solved classes

1. It is not NM13-04's split family. NM13-04 proves a single 4-connected core `K_4∨overline{K_n}`. The new graphs are assembled from port-deleted split atoms through arbitrary articulation/2-terminal macro-decompositions.
2. It is not Erickson's series-parallel graph class. Already `Q_1=K_5-g` contains a `K_4` subgraph, hence is not series-parallel; every macro-network containing such a leaf inherits a non-series-parallel minor.
3. It is not a spanning-tree theorem.
4. It is not Tang--Zhang's fixed-component complete-graph ensemble.
5. It is not merely finite verification: `L`, every `n_i`, and the expression-tree shape are arbitrary.

For concrete source-uncovered sizes:
\[
Q_3\parallel Q_4
\]
has `13` vertices and `38` edges, while
\[
Q_3\circ Q_4
\]
has `14` vertices and `38` edges. Both are beyond the repository's complete all-graph order `9`, and both are covered symbolically by the theorem.

The earlier transparent-theta theorem may also be applied **after** this construction to replace arbitrary edges of `G` by any transparent theta gadget `A_\ell`, `\ell>=2`, giving a further independent parameter layer without changing the proof above.

## 7. Exact executed certificate

The exact checker saved in this run is

`proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T01-39-00Z__portfield_sp_checker.py`

and was executed before persistence. Its archived output is

`proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T01-39-00Z__portfield_sp_checker.out`.

The checker is standard-library Python and uses only exact integer/Fraction arithmetic for the mathematical certificate. It verifies:

* `15` partition states;
* `M=5I+N`, `N^3 != 0`, `N^4=0`;
* all `18` non-port field orbits;
* all `4` port-edge orbit families;
* exact degree-`<=6` interpolation and overdetermined readback;
* the three non-coefficientwise sign cases by exact discriminants;
* brute-force physical unit checks:
  * `Q_1=K_5-g`: `Z=198`, minimum Rayleigh numerator `124`;
  * `Q_1||Q_1`: `n=8`, `m=18`, `Z=28179`, minimum numerator `44100`;
  * `Q_1 o Q_1`: `n=9`, `m=18`, `Z=39204`, minimum numerator `0` (the zero is the expected independence of edges lying on opposite sides of the articulation).

Terminal line:
`ALL_EXACT_CHECKS_PASS`.

Artifact creation commits before this report:

* checker: `d186eb5d435633c120828edd95e6d64908a8fbc5`;
* output: `c8b9536616ac40ac3339ced2bef40c82e4b54b5e`;
* ledger delta: `676792e2344a992a43ba154faf02a0ed4919db76`.

## 8. Honest status and residual obstruction

**Parent theorem:** no change; arbitrary finite graphs remain OPEN and the complete all-graph order stays `9`.

**Demonstrated mechanism gain:** substantial.

Before this run the unit-only closure required exact transparent activity `t=1` when the core lacked a weighted theorem. After this run:

* no transparency equation is required;
* effective port fields may be arbitrary nonnegative values;
* the property is closed under both series and parallel terminal composition;
* every `K_4∨overline{K_n}` clique-port deletion supplies a non-series-parallel PF atom;
* arbitrary finite SP macro-networks of those atoms are certified.

The remaining obstruction is also clear. An arbitrary 3-connected graph need not decompose into two-terminal macro-atoms, and the current atom theorem varies only **one** distinguished port field at a time. It does not prove arbitrary simultaneous positive edge weights, nor does it control a generic three-terminal separator. Therefore this is genuine structural progress but not a proof of the Grimmett--Winkler conjecture.

The natural next attack is a three-terminal analogue of PF closure, or a two-independent-port field theorem for the split atoms. Either would allow decomposition trees with interacting 2-separators rather than one terminal pair per macro-node.

## 9. ledger_delta

See the separate immutable file

`2026-09-20T01-39-00Z__ledger_delta.yaml`.

Summary:
```yaml
parent: T07
parent_status: OPEN -> OPEN
complete_all_graph_vertex_order: 9 -> 9
mechanism:
  before: transparent t=1 substitution / theta expansion
  after: PF-Rayleigh series+parallel closure + split4 port-field atoms + arbitrary macro-networks
restricted_status: CANDIDATE_FULL pending later independent review
novelty_priority: UNVERIFIED
unchanged_substantive_runs: 0
failed_recovery_routes: 0
```

`END OF REPORT`
