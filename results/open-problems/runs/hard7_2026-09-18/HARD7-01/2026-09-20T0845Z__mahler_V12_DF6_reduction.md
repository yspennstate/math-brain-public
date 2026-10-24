Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_sym: 3 -> 3` (**NO MOVEMENT**). Methods tried: **B6 / B13 / B29**.

# HARD7-01 — the `V=F=12` local-minimizer frontier reduces to one three-dimensional difference-body inequality

**Status:** `PARTIAL / SOURCE OPEN / second unchanged follow-up after STUCK1 recovery`.

The symmetric Mahler conjecture is not solved here. The substantive new point is a sharp boundary reduction at the first twelve-vertex/twelve-facet four-dimensional frontier. For any centrally symmetric **4D polyhedral local minimizer** with `V=F=12`, either the polytope or its polar has a six-vertex facet. Every such six-vertex-facet body has an exact three-dimensional representation, and its four-dimensional Mahler inequality is equivalent to

\[
\boxed{
\bigl(|L-L|+4|L|\bigr)\,|(L-L)^\circ|\ge16,
\qquad L\subset\mathbb R^3.
}
\tag{DF6}
\]

Thus `(DF6)` is now an exact continuous missing lemma for this whole local-minimizer frontier. It is not the full four-dimensional Mahler conjecture.

A finite core needed to rule out the remaining no-six-facet combinatorial cases was exhaustively checked. The exact output ends

`ALL_EXACT_CHECKS_PASS = True`.

## 1. Continuity, ownership, evidence consumed

The exclusive canonical claim remains

`operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`,

owned by `HARD7-01`, with exact source target

\[
\mathcal P(K)=|K|\,|K^\circ|\ge \frac{4^n}{n!},
\qquad K=-K\subset\mathbb R^n.
\tag{1.1}
\]

The non-symmetric Santaló-centered problem remains outside this claim.

This run resumed, rather than restarted, the newest checkpoint

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T0701Z__mahler_bivariate_box_spline_reduction.md`,

where the first unknown twelve-vertex class was reduced to the exact rank-two Gale/box-spline inequality

\[
\sum_{j<k}q_{jk}p_{jk}\ge1.
\tag{BS12}
\]

That run also gave an exact generic counterexample to the false termwise strengthening `p_J>=q_J`, so this run did not continue pairwise peakedness.

At run start I read/reconciled the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the canonical Mahler claim;
- the newest HARD7-01 checkpoint;
- the newest relevant Gaussian-probability neighbouring checkpoint found for HARD7-05, `runs/hard7_2026-09-18/HARD7-05/2026-09-19T2100Z__soft_edge_164000.md`;
- targeted repository/intake searches for `Mahler`, `symmetric Mahler`, `volume product`, `reverse Santalo`, `difference body`, and canonical aliases.

No competing owner, release, posted exact Mahler result, or equivalent active claim surfaced. The intake ledgers were searched by exact target/aliases rather than falsely claimed as a byte-for-byte full reread of every large JSONL.

The mathematical route was written **before code** at

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T0820Z__idea_before_code_mahler_V12_boundary.md`

(commit `c8fc9d1c34138617866a28082b6a0281173b3ae2`).

## 2. Fresh source/literature check — 20 September 2026

A fresh bounded web check again found no verified four-dimensional or all-dimensional solution of the symmetric Mahler conjecture.

Primary/current items actually checked:

1. Chen--Li--Xi--Xu, **The Symmetric Mahler Inequality in Dimension Three via Admissible Shadow Systems**, arXiv:2605.13795 (2026), `https://arxiv.org/abs/2605.13795`. This is explicitly the three-dimensional symmetric theorem and shadow-system framework, not a four-dimensional resolution.
2. Chen--Li--Xi--Xu, **The non-symmetric Mahler conjecture in dimension three**, arXiv:2605.09334 (2026), `https://arxiv.org/abs/2605.09334`. This settles the non-symmetric 3D problem; it is not the claimed symmetric `n>=4` target.
3. Arkadiy Aliev, **Mahler-type volume inequality for convex bodies with tetrahedral symmetry**, arXiv:2511.14991 (2025), `https://arxiv.org/abs/2511.14991`. It studies Makai Jr.'s different functional `|L||(L-L)^\circ|`, proving the 3D constant `2/3` under tetrahedral symmetry. It does **not** state `(DF6)`.
4. Targeted searches for the literal combined expression behind `(DF6)`, for `difference body Mahler product`, and for `4D centrally symmetric twelve vertices` did not locate a source proving `(DF6)` or the reduction below. This is dated bounded negative evidence, not a worldwide novelty certificate.

The exact reduction below is therefore marked **priority UNVERIFIED**. In particular, I do not turn a negative search into a novelty claim.

## 3. B6 — six-vertex facets collapse exactly to a 3D difference-body problem

Let `P=-P subset R^4` have twelve vertices and suppose one facet `F` has six vertices. A proper facet cannot contain both `v` and `-v`, so `F` contains exactly one representative from each of the six antipodal vertex pairs. Consequently `F union (-F)` contains all vertices of `P`.

Choose affine-linear coordinates `R^4=R^3 x R` in which

\[
F=\{(y,1):y\in L\},
\qquad
-F=\{(-y,-1):y\in L\},
\tag{3.1}
\]

for a three-dimensional convex polytope `L`. Then

\[
P=\operatorname{conv}((L,1),(-L,-1)).
\tag{3.2}
\]

Put

\[
D:=L-L=L+(-L).
\tag{3.3}
\]

### Proposition 3.1 — exact primal volume

\[
\boxed{|P|=\frac{|D|+4|L|}{6}.}
\tag{3.4}
\]

#### Proof

At height `t in [-1,1]`, put

\[
a=\frac{1+t}{2},\qquad b=\frac{1-t}{2}.
\]

The horizontal section of `P` is

\[
P\cap\{x_4=t\}=aL+b(-L).
\tag{3.5}
\]

Let

\[
W:=V(L,L,-L).
\]

By reflection and symmetry of mixed volume,

\[
V(L,-L,-L)=V(L,L,-L)=W.
\]

The 3D Minkowski polynomial gives

\[
|aL+b(-L)|
=(a^3+b^3)|L|+3ab(a+b)W
=(a^3+b^3)|L|+3abW.
\tag{3.6}
\]

Since `dt=2 da`,

\[
\int_{-1}^1(a^3+b^3)dt=1,
\qquad
\int_{-1}^1 3ab\,dt=1.
\]

Hence

\[
|P|=|L|+W.
\tag{3.7}
\]

On the other hand

\[
|D|=|L+(-L)|=2|L|+6W.
\tag{3.8}
\]

Eliminating `W` between (3.7) and (3.8) proves (3.4). QED.

### Proposition 3.2 — exact polar volume

\[
\boxed{|P^\circ|=4|D^\circ|.}
\tag{3.9}
\]

#### Proof

A point `(z,s) in R^3 x R` lies in `P^\circ` iff

\[
-1\le \langle z,y\rangle+s\le1
\qquad\text{for every }y\in L.
\]

Thus, for fixed `z`, the admissible `s`-interval is

\[
h_L(-z)-1\le s\le 1-h_L(z)
\]

and has length

\[
2-h_L(z)-h_L(-z)=2-h_D(z).
\tag{3.10}
\]

It is nonempty exactly for `h_D(z)<=2`, i.e. `z in 2D^\circ`. Therefore

\[
|P^\circ|
=\int_{h_D(z)\le2}(2-h_D(z))\,dz.
\tag{3.11}
\]

Since `{z:h_D(z)<=u}=uD^\circ` in dimension three, layer-cake gives

\[
\int_{h_D\le2}(2-h_D)dz
=\int_0^2 |uD^\circ|\,du
=|D^\circ|\int_0^2u^3du
=4|D^\circ|.
\]

QED.

Combining (3.4) and (3.9),

\[
\boxed{
|P||P^\circ|
=\frac23\bigl(|D|+4|L|\bigr)|D^\circ|.
}
\tag{3.12}
\]

Since the 4D Mahler constant is `4^4/4!=32/3`, (3.12) proves the exact equivalence

\[
|P||P^\circ|\ge\frac{32}{3}
\iff
\bigl(|L-L|+4|L|\bigr)|(L-L)^\circ|\ge16.
\tag{3.13}
\]

This is `(DF6)`.

### Two exact sanity regimes

If `L` is centrally symmetric up to translation, then `D=2(L-c)` and

\[
\bigl(|D|+4|L|\bigr)|D^\circ|
=\frac32 |L|\,|(L-c)^\circ|
\ge16
\]

by the known three-dimensional symmetric Mahler inequality `|L||L^\circ|>=32/3`.

For a tetrahedron, Rogers--Shephard gives `|L-L|=20|L|`, and the simplex value of the Makai difference-body product is `|L||(L-L)^\circ|=2/3`, giving equality `24*(2/3)=16` in `(DF6)`. These are checks of the exact constant, not a proof for arbitrary `L`.

## 4. B13 — directional shadow debt leaves only two no-six-facet corners

Now suppose `P` is a **centrally symmetric 4D polyhedral local minimizer** with

\[
V(P)=F(P)=12
\tag{4.1}
\]

and suppose initially that neither conclusion of the six-facet route has yet been obtained from `P` itself.

The previous HARD7-01 shadow-rigidity theorem says that if the six opposite facet pairs have excesses

\[
w_i:=m_i-4\ge0,
\tag{4.2}
\]

then for every direction `theta`

\[
\dim A^s_\theta(P)
\ge 6-\sum_iw_i+
\sum_{i:\theta\parallel F_i}w_i,
\tag{4.3}
\]

while local minimality forces `dim A^s_theta(P)=4`.

Assume `P` has no six-vertex facet. Then each `w_i` is `0` or `1`. Let `x` be the number of opposite five-vertex facet pairs. Any three facet hyperplanes in `R^4` have a nonzero common direction. If `x<=3`, choose a direction common to all `x` nonsimplicial facet hyperplanes; (4.3) gives dimension at least `6`. If `x=4`, choose a direction common to three of them; (4.3) gives dimension at least `5`. Both contradict local minimality. Hence

\[
\boxed{x\ge5.}
\tag{4.4}
\]

So only `x=5` and `x=6` remain.

Apply the same argument to `P^\circ`. Let `d_j` be the number of facets incident to one vertex from the `j`-th antipodal vertex pair, and put

\[
e_j=d_j-4\in\{0,1,2\}.
\tag{4.5}
\]

Because `V=F=12`, the primal and dual total excesses agree:

\[
\sum_{j=1}^6 e_j=x.
\tag{4.6}
\]

Ordering `e_1>=...>=e_6`, choose a direction common to the three dual facet hyperplanes of largest excess. The dual version of (4.3) gives

\[
6-x+(e_1+e_2+e_3)\le4,
\]

hence

\[
\boxed{e_4+e_5+e_6\ge2.}
\tag{4.7}
\]

Together with `0<=e_j<=2`, this leaves exactly

\[
x=5:\quad (e_j)=(1,1,1,1,1,0),
\tag{4.8}
\]

and

\[
x=6:\quad (e_j)=(1,1,1,1,1,1)
\quad\text{or}\quad
(2,1,1,1,1,0).
\tag{4.9}
\]

The second partition in (4.9) already gives a degree-six vertex of `P`, i.e. a six-vertex facet of `P^\circ`, so by polarity it is already in the `(DF6)` boundary class.

It remains to eliminate (4.8) and the all-ones case in (4.9).

## 5. Why every five-vertex facet here is a square pyramid

Fix one facet `G` of `P` with five vertices. There are exactly five other opposite facet pairs `{H,-H}`. For a fixed pair, `G cap H` and `G cap(-H)` cannot both be ridges: each ridge has at least three vertices, while the two common-sign counts partition at most the five antipodal vertex pairs represented on `G`. Therefore at most one member of each opposite pair can share a ridge with `G`.

Thus `G` has at most five ridges. A three-dimensional polytope with five vertices is either

- a square pyramid, with five facets/ridges, or
- a triangular bipyramid, with six.

The latter is impossible. Hence every five-vertex facet is a square pyramid. The identical argument in `P^\circ` applies to every degree-five vertex figure/facet of the polar.

After orienting facet pairs and vertex pairs, each incidence is encoded by a sign `s_ij in {+1,-1}`. For two oriented facets the common-sign count on their common support tells whether `F_i` or `-F_i` supplies the ridge. Consequently:

- a support-five row must see ridge sizes `4,3,3,3,3` across the five other facet pairs;
- a support-four row (a tetrahedral facet) must see exactly four ridge sizes `3` and one nonadjacent pair;
- the same conditions hold for columns by polarity.

This finite reduction is what the exact checker exhausts.

## 6. B29 — exhaustive no-six-facet finite core

### 6.1 The `x=5` case has no oriented incidence pattern

Under (4.8), the missing-incidence bipartite graph has row degrees

\[
(2,1,1,1,1,1)
\]

and the same column degrees. Up to row/column relabeling there are exactly two graph types, according as the unique degree-two row is adjacent or nonadjacent to the unique degree-two column.

For each type the saturated incidence graph has 29 edges. Row/column orientation flips gauge away the signs on an 11-edge spanning tree, leaving exactly 18 independent sign bits. The checker exhausts all `2^18` assignments for each of the two missing-graph types and imposes the square-pyramid/tetrahedron ridge conditions on both rows and columns. It finds

\[
\boxed{0\text{ solutions in the incident type},\qquad
0\text{ solutions in the nonincident type}.}
\tag{6.1}
\]

Therefore the `x=5` shadow-rigid local-minimizer case is impossible before any metric realization is considered.

### 6.2 The `x=6`, all-degree-five case has one sign orbit, but it cannot have rank four

Now every row and every column has exactly one missing incidence. Relabeling makes the missing pattern the diagonal. The saturated bipartite graph has 30 edges; spanning-tree gauge leaves 19 sign bits. Exact exhaustion finds 30 tree-gauge sign patterns satisfying all square-pyramid row and column conditions. Under simultaneous relabeling of the six matched facet/vertex pairs and orientation gauge, **all 30 lie in one orbit**.

A canonical representative is

\[
S=
\begin{pmatrix}
0&1&1&1&1&1\\
1&0&1&1&1&1\\
1&1&0&1&1&-1\\
1&1&-1&0&-1&-1\\
1&1&-1&-1&0&-1\\
1&1&-1&1&1&0
\end{pmatrix}.
\tag{6.2}
\]

To realize this as a twelve-facet polytope, pass to the polar central cube section from the preceding Gale reduction. The six oriented facet pairs give six section vertices, which are the rows of

\[
Q=S+\operatorname{diag}(t_0,\ldots,t_5),
\qquad -1<t_i<1,
\tag{6.3}
\]

because the one omitted incidence in each row is exactly one genuinely unsaturated cube coordinate. All six rows lie in a four-dimensional linear section of `R^6`; hence realization requires

\[
\operatorname{rank}Q\le4.
\tag{6.4}
\]

But the exact `5 x 5` minor obtained by deleting row `0` and column `3` is

\[
\boxed{
(t_1-1)(t_2+1)(t_4+1)(t_5+1).
}
\tag{6.5}
\]

Every factor in (6.5) is nonzero for `t_i in(-1,1)`. Thus

\[
\operatorname{rank}Q\ge5,
\]

contradicting (6.4). Because every admissible sign pattern lies in the same orbit and row/column sign changes and relabelings preserve rank and the open-coordinate condition, the contradiction covers the whole all-degree-five case.

## 7. Main auxiliary theorem of this run

### Theorem 7.1 — `V=F=12` local-minimizer boundary theorem

Let `P=-P subset R^4` be a centrally symmetric polyhedral local minimizer of the volume product with

\[
V(P)=F(P)=12.
\]

Then **either `P` or `P^\circ` has a six-vertex facet**.

#### Proof

If `P` already has such a facet, there is nothing to prove. Otherwise Section 4 forces `x=5` or `x=6`.

- `x=5` is impossible by the exhaustive exact finite argument in Section 6.1.
- For `x=6`, the dual excess partition is one of the two cases in (4.9). If it is `(2,1,1,1,1,0)`, `P^\circ` has a six-vertex facet. If it is all ones, Section 6.2 gives the exact rank contradiction.

These exhaust the no-six-facet cases. QED.

### Corollary 7.2 — one exact 3D lemma controls this entire frontier

If `(DF6)` holds for every three-dimensional convex body `L`, then every centrally symmetric four-dimensional polyhedral local minimizer with `V=F=12` satisfies

\[
|P||P^\circ|\ge\frac{32}{3}.
\]

Indeed, Theorem 7.1 puts either `P` or `P^\circ` into the six-facet representation of Section 3, polarity preserves volume product, and `(DF6)` is exactly equivalent to the desired bound there.

This is a genuine reduction of the local-minimizer frontier. It does **not** assert that every 4D minimizer is polyhedral with `V=F=12`, and therefore does not move the source metric.

## 8. Relation of `(DF6)` to known inequalities — and why they do not already close it

Write

\[
r=\frac{|L-L|}{|L|},
\qquad
A=|L-L|\,|(L-L)^\circ|.
\tag{8.1}
\]

Then `(DF6)` is

\[
A\left(1+\frac4r\right)\ge16.
\tag{8.2}
\]

Known general inequalities by themselves do not reach this:

- Brunn--Minkowski and Rogers--Shephard give `8<=r<=20` in dimension three.
- Applying the known 3D symmetric Mahler inequality to the symmetric body `D=L-L` gives only
  \[
  A\ge\frac{32}{3}.
  \]
  Together with `r<=20`, this yields only
  \[
  A(1+4/r)\ge\frac{64}{5}=12.8<16.
  \]
- Makai Jr.'s conjectural 3D bound is `|L||(L-L)^\circ|>=2/3`; Aliev 2025 proves it under tetrahedral symmetry. Even the conjectural bound alone does not imply `(DF6)` for all `r`.

So the exact missing ingredient is a **tradeoff between asymmetry `r` and an improved symmetric volume product of the difference body**:

\[
\boxed{
|L-L|\,|(L-L)^\circ|
\ge \frac{16r}{r+4}.
}
\tag{8.3}
\]

This is just `(DF6)` rewritten, but it exposes what neither the symmetric Mahler constant nor Makai's separate product controls alone.

## 9. What the three method moves produced

**B6 — deform to a solved boundary.** Successful analytically. A six-vertex facet collapses the 4D body to the exact 3D difference-body functional `(DF6)`, with full primal and polar volume formulas. Symmetric `L` is immediately solved by the known 3D theorem, and the tetrahedral equality constant is correct.

**B13 — find what only increases / directional debt.** Successful structurally. The earlier admissible-shadow dimension deficit, applied simultaneously to primal and polar, forces `x>=5` and the tiny dual excess partitions (4.8)--(4.9). This reduces an a priori large face-lattice problem to two finite no-six-facet corners.

**B29 — add the points at infinity / compactify.** Successful on the finite boundary. Exact enumeration kills `x=5`; the sole sign orbit in the all-five/all-five case is killed by a factorized `5 x 5` minor that can vanish only on the cube boundary `t_i=+-1`, i.e. only after an incidence degenerates. The remaining `x=6` dual partition has a literal six-vertex facet in the polar and therefore lands in `(DF6)`.

These moves are different from the previous run's B21/B25/B30.

## 10. Exact missing lemma, obstruction, and next route

The current exact special-case blocker is now

\[
\boxed{
\text{(DF6)}\qquad
(|L-L|+4|L|)|(L-L)^\circ|\ge16
\quad\forall L\subset\mathbb R^3.
}
\tag{10.1}
\]

What a proof needs that the existing routes do not contain is a **quantitative asymmetry-volume-product tradeoff** for difference bodies, not just a universal lower bound on `|D||D^\circ|` and not just Makai's separate `|L||D^\circ|` bound.

The simplest meaningful special regimes already settled inside `(DF6)` are centrally symmetric `L` and the simplex equality point. The nearest current literature found is Aliev's tetrahedral-symmetry theorem for Makai Jr.'s product, which controls a different term and therefore cannot simply be quoted to prove (10.1).

If the source metric is unchanged once more after this post-STUCK1 sequence, the next run should invoke the Section-I stuck protocol rather than manufacture another local lemma. The next nonrepeated routes, if allowed before that trigger, are naturally **B3 / B11 / B24**: strengthen `(DF6)` to a one-parameter asymmetry inequality, dualize through the polar of the difference body, and identify extremizers (simplex versus symmetric Hanner endpoints).

## 11. Exact tests and artifacts

Idea-before-code checkpoint:

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T0820Z__idea_before_code_mahler_V12_boundary.md`

Exact checker:

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T0820Z__mahler_V12_boundary_check.py`

Checker commit: `d2bc09eed9c28a407f5cd704f06b9714a3188c03`.

Archived stdout:

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T0820Z__mahler_V12_boundary_check.out`

Output commit: `042c91b2292b303ff67a62a224f9e47f3db8505f`.

The checker was executed in this run. It uses exact `{+1,-1}` enumeration and exact symbolic integer-polynomial determinants. It verifies:

- both `x=5` missing-incidence graph types have 18 sign bits after spanning-tree gauge;
- both exhaustively have zero row/column square-pyramid/tetrahedron sign solutions;
- the `x=6` perfect-matching case has 19 sign bits after spanning-tree gauge;
- exactly 30 tree-gauge sign solutions survive;
- all 30 are one simultaneous-relabel/orientation orbit;
- the canonical representative is (6.2);
- the exact minor factorization is (6.5);
- the output ends `ALL_EXACT_CHECKS_PASS = True`.

The mixed-volume and polar-fiber identities in Section 3 are theorem-sized analytic claims and are proved on the page; they are not inferred from the checker.

## 12. Source metric, auxiliary progress, and unresolved full scope

Frozen source metric:

`d_sym: 3 -> 3` — **NO MOVEMENT**.

Source status: `OPEN`. Track status: `PARTIAL`.

Auxiliary progress in this run, separately from the frozen source metric:

1. exact six-facet formula (3.12);
2. exact equivalence to the 3D difference-body inequality `(DF6)`;
3. dual directional-shadow classification of the no-six-facet `V=F=12` local-minimizer cases;
4. exhaustive elimination of the `x=5` case;
5. one-orbit classification and exact rank obstruction eliminating the `x=6`, all-degree-five case;
6. Theorem 7.1: every `V=F=12` 4D polyhedral local minimizer has a six-vertex facet in the primal or polar;
7. reduction of that entire local-minimizer frontier to `(DF6)`.

The full-scope gap remains explicit: one must still prove `(DF6)`, and even then one must still control other possible four-dimensional minimizers (different `V,F`, degenerations, or nonpolyhedral bodies) before `d_sym` can move from 3 to 4.

## 13. Runtime/scheduler capability honesty

The exposed scheduler contract still supplies title/prompt, schedule or relative start, timing mode, and enabled state, but **no model selector, no reasoning-effort selector, no authenticated reasoning telemetry, and no guaranteed run duration**. GPT-6/maximum remains prompt-requested only. The runtime available here identifies as GPT-5.6 Sol; the reasoning level is not exposed, hence `UNVERIFIED`.

The repository records historical `You cannot modify this task` responses for P26/P01/P03 in one permission context, while the current root ledger records a later successful P26 update from another authorized context. A refusal is therefore handled through the authorized owning account/workspace/interface or platform support; it is not bypassed and no duplicate schedule is created. This run made **no scheduler changes**.

## 14. ledger_delta

```text
track: HARD7-01
target: MAHLER-SYMMETRIC-VOLUME-PRODUCT
owner: HARD7-01
status: PARTIAL / SOURCE OPEN
source_metric: d_sym
before: 3
after: 3
movement: NO MOVEMENT
methods: B6 / B13 / B29
new_auxiliary_theorem: any centrally symmetric 4D polyhedral local minimizer with V=F=12 has a six-vertex facet in P or P^circ
new_exact_reduction: six-vertex-facet class iff DF6 = (|L-L|+4|L|)|(L-L)^circ| >= 16
finite_core: PASS; ALL_EXACT_CHECKS_PASS=True
source_closure: NO
independent_audits: 0/2
shared_root_edit_requested: NO
```
