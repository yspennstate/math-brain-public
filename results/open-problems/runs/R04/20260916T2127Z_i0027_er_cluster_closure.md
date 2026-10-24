Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime/scheduler exposes no model-family selector, no reasoning-effort selector and no authenticated telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: rigorous R04 coefficient width `(sqrt(2)-1)/54 -> 0` by a new all-graph proof; Section-B methods actually used: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #4 PROVE SOMETHING WEAKER COMPLETELY, #6 DEFORM TO A POINT YOU CAN SOLVE.**

Problem/source: David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 6.13, `tau_0` / Kemeny half only, intake I0027.

# R04 immutable run report — I0027 / effective-resistance clustering closure proof

Run ID: `20260916T2127Z_i0027_er_cluster_closure`  
Repository: `yspennstate/math-open-problems`, branch `master`.

**Mathematical status after this run:** R04 has a complete proof of
\[
\max_{|V(G)|=n}K(G)\sim \frac{n^3}{54}
\]
for connected simple unweighted graphs, using a published effective-resistance graph decomposition theorem plus retained R04 claims C4 and C6, both reproved/expanded below where needed. The frozen coefficient-width metric therefore moves to `0` at the level of the R04 proof.

**Fleet closure status:** **NOT CLOSED YET.** The owner’s closure rule requires two independent OTHER-track audits, one from P26 and one from a different track. Those audits do not yet exist for the source-closing theorem/C6 package. Therefore no paper folder is created and no public-posting claim is made. Current governance label: **PROVED BY R04 / AUDIT-GATED; source closure pending two independent audits.**

## 1. Continuity, source, admission, ownership, and exclusions

Before new mathematics I reread/recovered the required control state:
- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0027.md`;
- newest own report `runs/R04/20260916T202301Z_i0027_sparse_compression.md`;
- newest neighboring R03 report `runs/R03/20260916T2309Z_19_rank_obstruction.md`;
- newest R05 report `runs/R05/20260916T201837Z_i0030_edge_mnhd_n14.md`;
- newest same-area retired/unavailable C31 report `proofnet24/C31-closure-kemeny/runs/2026-09-16/2026-09-16T19-52-55Z__report.md`;
- targeted repository/intake searches for `I0027`, `Open Problem 6.13`, and `tau_0`.

The large intake JSONL surfaces remain connector-truncated; I used exact-ID/alias search rather than falsely claiming to have visually reread every one of roughly 780 rows.

`operations/claims/I0027.md` still says `Owner: R04` and `PENDING_ADMISSION, not READY`. The source/current-status/ownership checks that file was waiting on were repeated in this run:
1. outside source verified;
2. target statement verified exactly;
3. current bounded literature search through 2026-09-16 found no source-level `tau_0` solution;
4. repository ownership search found no conflicting owner; C31 explicitly records I0027 as unavailable because it is reserved to R04;
5. `POSTED.md` does not mark this source scope posted/settled.

R04 does **not** edit or self-promote the shared claim file; that is shared-ledger/coordinator work. Research proceeds under the already-exclusive R04 reservation after completing the pending substantive checks.

The historical C31/PROB20-13 filenames concern Aldous–Fill 4.49(ii), not this problem. That research remains retired. The old R04 random-band-matrix route remains preserved in immutable history and is not reopened.

## 2. Exact source locator and `tau_2` separation

Primary source rechecked 2026-09-16:
`https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch6.S3.html`.

In §6.3.2, equation (6.19), Aldous–Fill record
\[
\max\tau_0,\ \max\tau_2\le (2/27+o(1))n^3.
\]
Immediately afterward, Open Problem 6.13 asks to prove
\[
\max\tau_0\sim \frac{n^3}{54},
\qquad
\max\tau_2\sim \frac{n^3}{54}.
\]

R04 works only on `tau_0`, i.e. Kemeny’s constant.

The `tau_2` half remains **KNOWN**. Aksoy–Chung–Tait–Tobin, *The maximum relaxation time of a random walk*, arXiv:1804.05500 / Advances in Applied Mathematics, prove that the minimum normalized-Laplacian gap over connected simple `n`-vertex graphs is `(1+o(1))54/n^3`, asymptotically attained by the double kite. Equivalently the maximum relaxation time is `(1+o(1))n^3/54`.

## 3. Current literature / prior-art search

Dated bounded queries this run included:
- `"Aldous Fill" "Open Problem 6.13" Kemeny`;
- `"n^3/54" Kemeny graph`;
- `"Kemeny" "1/54" graph maximum`;
- `"Kemeny constant" "effective resistance" decomposition maximum graph`;
- `"Graph Clustering using Effective Resistance" Kemeny`;
- `"effective resistance diameter" Kemeny maximum graph`;
- `"Kemeny" "resistance diameter" partition`;
- 2026-specific queries for Kemeny extremal graphs and double kites.

Recovered/current adjacent literature includes:
- Faught–Kempton–Knudson, arXiv:2108.01061, exact 1-separation formulas and optimal barbell within the barbell family;
- Alev–Anari–Lau–Oveis Gharan, *Graph Clustering using Effective Resistance*, ITCS 2018, DOI `10.4230/LIPIcs.ITCS.2018.41`;
- Kooij–Dubbeldam, *Further Exploration of an Upper Bound for Kemeny’s Constant*, Entropy 2025;
- Li–Sun–Yang, arXiv:2608.08797, diameter-two Kemeny bounds;
- Abiad–Carmona–Encinas–Ghorbani–Jiménez–Samperio, arXiv:2609.17481 (submitted 2026-09-15), matrix compression/interlacing lower bounds and deletion estimates;
- Breen–deBlieck–Vander Meulen, arXiv:2608.04150, Braess cliques.

No bounded search returned a proof of the full connected-graph `tau_0` asymptotic, nor a source explicitly combining the Alev effective-resistance decomposition with the sharp `1/54` bridge-energy variational bound below. This is **bounded negative search evidence only**; novelty remains **UNVERIFIED** until a broader literature review/audits.

## 4. Frozen metric — moves to zero in the R04 proof

Let
\[
M_n:=\max_{|V(G)|=n} K(G).
\]

Before this run, retained R04 results gave
\[
\frac1{54}
\le
\liminf_{n\to\infty}\frac{M_n}{n^3}
\le
\limsup_{n\to\infty}\frac{M_n}{n^3}
\le
\frac{\sqrt2}{54},
\]
so
\[
W_{\rm before}
=
\frac{\sqrt2-1}{54}
=
0.007670621525427686\ldots.
\]

The theorem proved in §9 gives
\[
\lim_{n\to\infty}\frac{M_n}{n^3}=\frac1{54}.
\]
Therefore
\[
\boxed{W_{\rm after}=0.}
\]

This is a genuine movement of the fixed owner metric over the full source graph class. It is **not fleet closure** until the two required independent audits are recorded.

Unchanged-run count resets to `0`.

## 5. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: effective-resistance graph clustering

The previous run had isolated the obstruction: after reducing to bridge-like geometry, the bridge skeleton itself contributes at most `1/54`; any excess would have to come from internal effective resistance inside dense blocks.

The useful theorem comes from a different literature: graph-partitioning algorithms.

### Published input: Alev–Anari–Lau–Oveis Gharan Theorem 3

For a weighted undirected graph \(G=(V,E,w)\) and sufficiently large \(\delta>1\), Alev–Anari–Lau–Oveis Gharan prove that \(V\) can be partitioned into induced subgraphs
\[
V=V_1\sqcup\cdots\sqcup V_h
\]
such that, with universal implied constants,
\[
w\!\left(E\setminus\bigcup_iE(V_i)\right)
\lesssim \frac{w(E)}{\delta}
\tag{5.1}
\]
and
\[
\operatorname{Rdiam}(G[V_i])
\lesssim
\delta^3\frac{|V|}{w(E)}
\qquad\text{for every }i.
\tag{5.2}
\]

For an unweighted graph with \(m\) edges, this becomes
\[
q_{\rm cross}\le C_1\frac m\delta,
\qquad
\operatorname{Rdiam}(G[V_i])
\le C_2\delta^3\frac n m
\tag{5.3}
\]
for universal constants \(C_1,C_2\).

Their ITCS paper states this as Theorem 3 (Main); the proof explicitly chooses the decomposition parameters at the end and works for sufficiently large \(\delta\). No Kemeny conclusion is stated in that source.

This theorem is exactly calibrated to the remaining R04 obstruction:
- only an \(o(1)\) fraction of edges must be removed if \(\delta\to\infty\);
- every remaining induced cluster has vanishing resistance diameter when \(m=\Theta(n^2)\) and \(\delta^3=o(n)\).

## 6. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY: the clustered dense-graph theorem

Before using the full source extremal problem, isolate the mechanism.

### R04-I0027-C7 — clustered dense graphs are controlled by their bridge skeleton

**STATUS: PROVED.**

Let \(G_n\) be connected simple graphs with
\[
m_n=\Theta(n^2).
\]
Suppose there is a partition
\[
V(G_n)=V_1\sqcup\cdots\sqcup V_h
\]
such that
\[
q_n:=\left|E(G_n)\setminus\bigcup_iE(G_n[V_i])\right|=o(n^2)
\tag{6.1}
\]
and
\[
\varepsilon_n
:=
\max_i\operatorname{Rdiam}(G_n[V_i])
=o(1/n^0)
=o(1).
\tag{6.2}
\]
Assume in addition
\[
n\,\varepsilon_n=o(n),
\]
equivalently simply \(\varepsilon_n=o(1)\); the Kemeny error below is \(m_n n\varepsilon_n=o(n^3)\).

Choose a spanning tree of the connected quotient graph on the clusters. For every quotient-tree edge retain one original cross-cluster edge that realizes it, retain **all** within-cluster edges, and delete every other cross-cluster edge. Call the resulting connected spanning graph \(H_n\).

Then
\[
m(G_n)-m(H_n)\le q_n=o(n^2).
\tag{6.3}
\]

Retained C4, whose proof is reproduced in §7, gives
\[
K(G_n)\le K(H_n)+o(n^3).
\tag{6.4}
\]

The quotient of \(H_n\) by the clusters is a tree, and every retained cross-cluster edge is a bridge.

For \(u,v\in V(H_n)\), let \(r(u,v)\) be the number of quotient-tree bridge edges on the cluster path between the clusters containing \(u,v\). By iterating the cut-vertex/effective-resistance series law,
\[
R_{H_n}(u,v)
=
r(u,v)+
\sum_{\text{clusters visited on the quotient path}}
R_{G_n[V_i]}(a_i,b_i)
\tag{6.5}
\]
for suitable entry/exit vertices \(a_i,b_i\) (with \(u,v\) used at the endpoints). There are at most \(n\) visited clusters, so
\[
R_{H_n}(u,v)
\le
r(u,v)+n\varepsilon_n.
\tag{6.6}
\]

Let \(\pi_H(x)=d_H(x)/(2m_H)\). The degree-weighted resistance identity is
\[
K(H_n)
=
m_H\,\mathbb E_{\pi_H\otimes\pi_H}
R_{H_n}(X,Y).
\tag{6.7}
\]
The expectation of \(r(X,Y)\) contributes exactly the quotient-bridge part of Kemeny’s resistance sum and is no larger than the contribution \(K_{\rm br}(H_n)\) of **all** bridges of \(H_n\). Therefore
\[
\boxed{
K(H_n)
\le
K_{\rm br}(H_n)+m_Hn\varepsilon_n.
}
\tag{6.8}
\]
Since \(m_H=\Theta(n^2)\) and \(\varepsilon_n=o(1)\),
\[
K(H_n)
\le
K_{\rm br}(H_n)+o(n^3).
\tag{6.9}
\]

Thus any sharp upper bound on the bridge contribution immediately transfers to the whole clustered graph.

The exact checker independently verifies the finite resistance split and (6.8) on several nontrivial cluster trees using rational Laplacian inverses.

## 7. Retained C4, strengthened to the exact range needed here

### R04-I0027-C4 — sparse-deletion stability

**STATUS: PROVED / retained.**

If \(H\subseteq G\) is a connected spanning subgraph on \(n\) vertices and
\[
m_G=|E(G)|,\quad m_H=|E(H)|,\quad q=m_G-m_H,
\]
then
\[
\boxed{
K(G)
\le
\frac{m_H}{m_G}K(H)
+
(n-1)\frac{2qm_H+q^2}{m_G}.
}
\tag{7.1}
\]
In particular,
\[
\boxed{
K(G)\le K(H)+2q(n-1)+\frac{q^2(n-1)}{m_G}.
}
\tag{7.2}
\]

#### Proof

Write
\[
d^G=d^H+r,\qquad \sum_vr_v=2q.
\]
Rayleigh monotonicity gives
\[
R_G(u,v)\le R_H(u,v).
\]
Using
\[
K(G)
=
\frac1{2m_G}
\sum_{u<v}d_u^Gd_v^GR_G(u,v)
\]
and \(R_H(u,v)\le n-1\), the \(d^Hd^H\) contribution is \(2m_HK(H)\); the two cross terms total at most \(4qm_H(n-1)\); and the \(rr\) term is at most \(2q^2(n-1)\). Divide by \(2m_G\).

Consequently, whenever
\[
m_G=\Theta(n^2),\qquad q=o(n^2),
\]
we have
\[
K(G)\le K(H)+o(n^3),
\tag{7.3}
\]
because
\[
qn=o(n^3),\qquad
\frac{q^2n}{m_G}=o(n^3).
\]

The previous report only highlighted the special case \(q=O(n)\); (7.3) is the direct full range of the same proved inequality and is the range required by Alev clustering.

## 8. Retained C6, with full proof restated because it is source-closing input

### R04-I0027-C6 — every dense graph has bridge contribution at most \(n^3/54+o(n^3)\)

**STATUS: PROVED / retained; independent audit still pending.**

For a connected graph \(H\) with \(m\) edges define
\[
K_{\rm br}(H)
=
\frac1{2m}
\sum_{e\in B(H)}
\operatorname{vol}(A_e)\operatorname{vol}(A_e^c),
\tag{8.1}
\]
where \(B(H)\) is the set of bridges and \(A_e,A_e^c\) are the two sides of \(H-e\).

For every connected simple graph sequence with
\[
m_n=\Theta(n^2),
\]
\[
\boxed{
\limsup_{n\to\infty}\frac{K_{\rm br}(H_n)}{n^3}
\le\frac1{54}.
}
\tag{8.2}
\]

#### Step 1. Exact bridge-block identity

Delete all bridges. Let the resulting bridge blocks be \(C_i\), with internal edge counts \(m_i\). Contract each \(C_i\); the quotient \(Q\) is a tree.

Put
\[
w_i=m_i+1,\qquad
W=\sum_iw_i=m+1,\qquad
p_i=\frac{w_i}{W}.
\]
For a quotient edge whose side is \(S\subseteq V(Q)\),
\[
\operatorname{vol}(A_e)
=
2\sum_{i\in S}m_i+2(|S|-1)+1
=
2Wp(S)-1.
\tag{8.3}
\]
Hence, for independent \(X,Y\sim p\) on \(Q\),
\[
\boxed{
K_{\rm br}(H)
=
\frac{(m+1)^2}{m}\,
\mathbb E_p d_Q(X,Y)
-
\frac{(2m+1)|E(Q)|}{2m}.
}
\tag{8.4}
\]
In particular,
\[
K_{\rm br}(H)
\le
\frac{(m+1)^2}{m}\,
\mathbb E_p d_Q(X,Y).
\tag{8.5}
\]

#### Step 2. Macroscopic blocks

Pass to a subsequence with
\[
\frac{m}{n^2}\to\alpha>0.
\]
Fix \(\eta>0\). Call a block large if
\[
n_i:=|C_i|\ge\eta n.
\]
Let \(L\) be the large-block index set and
\[
P=\sum_{i\in L}p_i.
\]
For small blocks,
\[
m_i\le \frac{n_i(n_i-1)}2
\le \frac{\eta n\,n_i}{2},
\]
so
\[
1-P
\le
\frac{\eta}{2\alpha}+o(1).
\tag{8.6}
\]

Write
\[
x_i=\frac{n_i}{n},\qquad
s=\sum_{i\in L}x_i,
\qquad
\widetilde p_i=\frac{p_i}{P},
\]
and define
\[
S=\sum_{i\in L}\sqrt{\widetilde p_i},
\qquad
Q_2=\sum_{i\in L}\widetilde p_i^2.
\tag{8.7}
\]

Simple-graph capacity \(m_i\le n_i^2/2\) gives
\[
\sqrt{p_i}
\le
\frac{x_i}{\sqrt{2\alpha}}+o(1)
\]
uniformly over the \(O_\eta(1)\) large blocks. Summing and squaring,
\[
P S^2
\le
\frac{s^2}{2\alpha}+o(1),
\]
hence
\[
\alpha
\le
\frac{s^2}{2PS^2}+o(1).
\tag{8.8}
\]

#### Step 3. Quotient-distance budget

Between two large quotient nodes, a tree path contains at most all small quotient nodes plus \(O_\eta(1)\) large nodes. Every small block contains at least one original vertex, so
\[
d_Q(i,j)
\le
(1-s)n+O_\eta(1)
\qquad (i,j\in L).
\tag{8.9}
\]

Pairs where at least one sample is small have total probability at most \(2(1-P)\), and every quotient distance is at most \(n-1\). Thus
\[
\frac1n\mathbb E_p d_Q(X,Y)
\le
P^2(1-s)(1-Q_2)
+
2(1-P)+o(1).
\tag{8.10}
\]

From (8.5),
\[
\limsup\frac{K_{\rm br}(H)}{n^3}
\le
\alpha\left[
P^2(1-s)(1-Q_2)+2(1-P)
\right].
\tag{8.11}
\]
Let \(n\to\infty\) and then \(\eta\downarrow0\). By (8.6), \(P\to1\), and the second term vanishes. Using (8.8),
\[
\limsup\frac{K_{\rm br}(H)}{n^3}
\le
\frac{s^2(1-s)}{2}
\frac{1-Q_2}{S^2}.
\tag{8.12}
\]

Hölder interpolation gives
\[
1
=
\left(\sum_i\widetilde p_i\right)^3
\le
\left(\sum_i\widetilde p_i^2\right)
\left(\sum_i\sqrt{\widetilde p_i}\right)^2
=
Q_2S^2.
\tag{8.13}
\]
Therefore
\[
\frac{1-Q_2}{S^2}
\le
Q_2(1-Q_2)
\le
\frac14.
\tag{8.14}
\]
Finally,
\[
\limsup\frac{K_{\rm br}(H)}{n^3}
\le
\frac{s^2(1-s)}8
\le
\frac1{54},
\tag{8.15}
\]
with the last maximum attained at \(s=2/3\).

This proves C6.

The exact checker verifies (8.14) on 3905 square-rational probability vectors and symbolically verifies the \(s=2/3\), \(1/54\) optimization.

## 9. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: source-closing theorem

### R04-I0027-C8 — Aldous–Fill Open Problem 6.13, `tau_0` half

**STATUS: PROVED BY R04; FLEET CLOSURE PENDING TWO INDEPENDENT AUDITS.**

For connected simple unweighted \(n\)-vertex graphs,
\[
\boxed{
\max_G K(G)
=
\left(\frac1{54}+o(1)\right)n^3.
}
\tag{C8}
\]

#### Proof

For each \(n\), let \(G_n\) be a graph maximizing \(K(G)\), and put
\[
m_n=|E(G_n)|.
\]

### Lower bound and forced density

Faught–Kempton–Knudson give an exact formula for the balanced barbell
\[
B(1,n/3,n/3,n/3)
\]
(for divisible \(n\)) whose leading term is
\[
K(B)
=
\frac{n^3}{54}+O(n^2).
\tag{9.1}
\]
Rounding the three parameters by \(O(1)\) gives the same leading coefficient for every \(n\). Hence
\[
K(G_n)\ge
\left(\frac1{54}-o(1)\right)n^3.
\tag{9.2}
\]

The elementary bound
\[
K(G)\le |E(G)|(n-1)
\tag{9.3}
\]
therefore forces
\[
m_n
\ge
\left(\frac1{54}-o(1)\right)n^2.
\tag{9.4}
\]
Trivially \(m_n\le n^2/2\), so
\[
m_n=\Theta(n^2).
\tag{9.5}
\]

### Effective-resistance clustering

Choose
\[
\delta_n=n^{1/10}.
\tag{9.6}
\]
For all sufficiently large \(n\), Alev–Anari–Lau–Oveis Gharan Theorem 3 gives a partition
\[
V(G_n)=V_1\sqcup\cdots\sqcup V_h
\tag{9.7}
\]
such that the number of cross-cluster edges is
\[
q_{\rm cross}
\le
C_1\frac{m_n}{\delta_n}
=
o(n^2)
\tag{9.8}
\]
and every induced cluster satisfies
\[
\operatorname{Rdiam}(G_n[V_i])
\le
C_2\delta_n^3\frac{n}{m_n}.
\tag{9.9}
\]
Using (9.5),
\[
\varepsilon_n
:=
\max_i\operatorname{Rdiam}(G_n[V_i])
=
O\!\left(\frac{\delta_n^3}{n}\right)
=
O(n^{-7/10})
=
o(1).
\tag{9.10}
\]

Finite resistance diameter implies each induced \(G_n[V_i]\) is connected.

### Quotient-tree surgery

The quotient graph on clusters is connected because \(G_n\) is connected. Choose a spanning tree of this quotient. For each quotient-tree edge retain one original cross-cluster edge realizing it; retain every intra-cluster edge; delete every other cross-cluster edge. Let the resulting connected spanning graph be \(H_n\).

Its deletion count \(q_n\) satisfies
\[
q_n\le q_{\rm cross}
=
O(m_n/\delta_n)
=
o(n^2),
\tag{9.11}
\]
so
\[
m(H_n)=m_n-o(n^2)=\Theta(n^2).
\tag{9.12}
\]

By C4,
\[
\begin{aligned}
K(G_n)
&\le
K(H_n)
+
2q_n(n-1)
+
\frac{q_n^2(n-1)}{m_n}\\
&=
K(H_n)+
O\!\left(\frac{n^3}{\delta_n}\right)
+
O\!\left(\frac{n^3}{\delta_n^2}\right)\\
&=
K(H_n)+o(n^3).
\end{aligned}
\tag{9.13}
\]

### Internal cluster resistance is lower order

The quotient of \(H_n\) is a tree, so C7 applies:
\[
K(H_n)
\le
K_{\rm br}(H_n)+
m(H_n)\,n\,\varepsilon_n.
\tag{9.14}
\]
By (9.10) and (9.12),
\[
m(H_n)n\varepsilon_n
=
O(\delta_n^3n^2)
=
O(n^{23/10})
=
o(n^3).
\tag{9.15}
\]
Thus
\[
K(H_n)
\le
K_{\rm br}(H_n)+o(n^3).
\tag{9.16}
\]

### Sharp bridge variational bound

Since \(m(H_n)=\Theta(n^2)\), C6 applies:
\[
K_{\rm br}(H_n)
\le
\left(\frac1{54}+o(1)\right)n^3.
\tag{9.17}
\]
Combining (9.13), (9.16), and (9.17),
\[
K(G_n)
\le
\left(\frac1{54}+o(1)\right)n^3.
\tag{9.18}
\]
Together with the barbell lower bound (9.2),
\[
\boxed{
K(G_n)
=
\left(\frac1{54}+o(1)\right)n^3.
}
\]
QED.

### Why the proof is not circular

- Alev et al. supply only a graph decomposition theorem in effective-resistance geometry.
- C4 is a deterministic comparison under sparse edge deletion.
- C6 is a direct bridge-tree variational inequality proved above.
- The lower bound is the published barbell computation.
- No use is made of the already-known `tau_2` upper bound to upper-bound `tau_0` (which would be invalid since `tau_2 <= tau_0`).
- No unproved assumption that an extremizer is a barbell/bridge chain is made.

## 10. Adversarial tests of the strongest claim

I explicitly tested the likely failure points.

1. **Could the Alev clusters be disconnected?** No: the theorem gives finite effective-resistance diameter of each induced \(G[V_i]\); that requires connectivity within each induced cluster.

2. **Could discarded cross-cluster edges be too numerous for C4?** No. Alev gives \(q=O(m/\delta_n)\). Since the extremizer is forced dense, \(m=\Theta(n^2)\), and \(\delta_n\to\infty\), so \(q=o(n^2)\), precisely the range of C4.

3. **Could outside branches reduce resistance inside a cluster and invalidate (6.5)?** In the quotient-tree graph \(H_n\), every off-path branch is attached through a single cut vertex. It cannot furnish an alternative route between two attachment points of the visited cluster. Iterated cut-vertex resistance additivity gives the exact series decomposition.

4. **Could there be too many cluster-resistance terms?** At most one for each visited cluster, hence at most \(n\). The Alev diameter is \(O(\delta_n^3/n)\) in the dense regime, so the total Kemeny error is \(O(\delta_n^3n^2)=o(n^3)\).

5. **Could hidden constants in Alev depend on \(n\) or \(\delta\) destructively?** Their theorem uses universal `lesssim` constants and is stated for every sufficiently large \(\delta>1\). The proof chooses \(R\asymp\delta^2 n/W\) and \(W=w(E)/\delta\) at the end. Choosing \(\delta_n=n^{1/10}\to\infty\) is within that regime for all sufficiently large \(n\).

6. **Could C6 miss bridges inside the Alev clusters?** No. C7 uses only the quotient-tree bridge contribution and bounds it above by \(K_{\rm br}(H_n)\), which includes *all* bridges, internal or inter-cluster. C6 is therefore conservative.

7. **Could a sparse maximizing graph avoid the decomposition argument?** No. The published barbell lower bound plus \(K(G)\le m(n-1)\) forces every maximizer to have \(m=\Theta(n^2)\).

No obstruction survived these tests.

## 11. Exact self-check

Executed:
`artifacts/R04/20260916T2127Z_i0027_er_cluster_closure_exact.py`

Archived output:
`artifacts/R04/20260916T2127Z_i0027_er_cluster_closure_exact.out`

The checker:
- verifies the three asymptotic error exponents for \(\delta_n=n^{1/10}\):
  `29/10`, `14/5`, `23/10`, all below `3`;
- verifies the C6 Hölder-derived probability inequality on 3905 exact square-rational distributions;
- computes exact Laplacian resistances and Kemeny constants on three nontrivial cluster-tree graphs and verifies
  \[
  K(H)\le K_{\rm br}(H)+mn\varepsilon;
  \]
- symbolically verifies the normalized C4 surgery error;
- symbolically verifies the sharp \(s^2(1-s)/8\le1/54\) optimization.

Output ends `RESULT PASS`.

The unrelated spreadsheet-runtime warmup warning printed by the Python environment after the mathematical checker completed successfully does not enter any proof step and is not included in the archived mathematical output.

## 12. Independent audit duty — newest R05 package

Newest R05 package read:
`runs/R05/20260916T201837Z_i0030_edge_mnhd_n14.md`.

I independently audited the new analytic theorem R05-I0030-C5, not merely its finite census.

R05-C5 says: for any finite connected \(d\)-regular graph, with
\[
P=A/d,\qquad H_t=e^{t(P-I)},
\]
the normalized average neighbor heat ratio
\[
\bar r_x(t)
=
\frac{1}{dH_t(x,x)}
\sum_{y\sim x}H_t(x,y)
\]
is strictly increasing from \(0\) to \(1\).

Independent verification:

Put
\[
a_x(t)=H_t(x,x).
\]
Since \(H_t\) commutes with \(P\),
\[
a_x'(t)
=
(H_t(P-I))_{xx}
=
\frac1d\sum_{y\sim x}H_t(x,y)-a_x(t),
\]
hence
\[
\bar r_x(t)=1+\frac{a_x'(t)}{a_x(t)}.
\]
With \(L=I-P\) symmetric positive semidefinite,
\[
a_x(t)
=
\int e^{-\lambda t}\,d\mu_x(\lambda).
\]
Under the exponentially tilted local spectral measure,
\[
\bar r_x'(t)
=
\frac{a_xa_x''-(a_x')^2}{a_x^2}
=
\operatorname{Var}_{\nu_{x,t}}(\lambda).
\]
Connectedness gives positive local spectral mass at \(\lambda=0\), while \(L_{xx}=1\) forces positive mass on the positive spectrum, so the variance is strictly positive for every finite \(t\). The endpoint values follow from \(H_0=I\) and convergence \(H_t(x,y)\to1/|V|\).

**Audit ID:**
`R04-AUDIT-R05-I0030-C5-20260916T2127Z = PASS_MATH / NOVELTY_UNVERIFIED`.

This is claim-scoped; I did not independently redo Conder’s complete order-14 census.

## 13. Audit/closure ledger

Existing other-track audits relevant to earlier R04 work:
- `R03-AUDIT-R04-I0027-C2-05 = PASS` for the previous diameter-profile upper bound;
- `R03-AUDIT-R04-I0027-C3-06 = PASS` for the previous UST bottleneck-chain theorem.

Those are **not enough** to governance-close C8, because the source-closing route depends essentially on C4, C6, C7 and the Alev input.

Required closure audits now:
- `P26 full C4/C6/C7/C8 package audit: PENDING`;
- `second independent OTHER-track C4/C6/C7/C8 package audit: PENDING`.

Until both exist, R04 does not create `paper_<name>/`, does not call the source CLOSED, and does not stop the recurring research task.

## 14. Model/scheduler interface and denied-task workaround

The interface limitation is unchanged and was rechecked against the current owner policy. The exposed automation mutation schema supports title, prompt, schedule/timing mode and enabled state; it has **no model-family field and no reasoning-effort field**. Therefore `GPT-6 / maximum` remains prompt text only and cannot be authenticated from this worker.

To genuinely change this, the product/API or an authorized owner-facing task UI must expose model/reasoning selectors or runtime telemetry.

For any scheduler task returning `You cannot modify this task` (the historical P26 case), the legitimate workaround is modification from the owning/admin-authorized account/workspace context or escalation to platform support. There is no legitimate parameter trick, duplicate-task workaround, or permission bypass. No scheduler change was attempted here.

## 15. Cumulative R04 I0027 ledger

- Exact source `tau_0` statement: **R04 PROVED; fleet closure audit-gated**.
- `tau_2` half: **KNOWN** (Aksoy–Chung–Tait–Tobin).
- Published barbell lower coefficient \(1/54\): **KNOWN**.
- C1 clique-tree restricted \(1/54\) variational result: **PROVED / retained**.
- C2 full-class upper coefficient \(\sqrt2/54\): **PROVED / retained; R03 audit PASS**.
- C3 cubic-scale UST bottleneck chain: **PROVED / retained; R03 audit PASS**.
- C4 sparse-deletion stability: **PROVED / retained; source-closing input**.
- C5 asymptotic bridge-chain reduction: **PROVED / retained**.
- C6 sharp bridge contribution \(1/54\): **PROVED / retained; source-closing input; audit pending**.
- C7 clustered dense-graph reduction: **PROVED NEW**.
- C8 exact source asymptotic \(M_n\sim n^3/54\): **PROVED NEW BY R04; closure pending audits**.
- Frozen coefficient-width metric: **MOVED TO 0**.
- Current unchanged count: `0`.
- Paper package: **NOT YET**, because closure audits are missing.
- Public posting: **NONE**.

## 16. ledger_delta

```yaml
ledger_delta:
  worker: R04
  source: "Aldous and Fill, Reversible Markov Chains and Random Walks on Graphs, Open Problem 6.13 / intake I0027"
  source_scope: "tau_0 / Kemeny half only"
  target: "max_{|V(G)|=n} tau_0(G) ~ n^3/54 over connected simple unweighted graphs"
  metric: "width U-L of the rigorous leading n^3 coefficient interval over the full source class"
  before:
    L: "1/54"
    U: "sqrt(2)/54"
    width: "(sqrt(2)-1)/54"
  after:
    L: "1/54"
    U: "1/54"
    width: "0"
  movement: "SOURCE-MATCHING FULL-CLASS PROOF; metric width -> 0"
  status: "PROVED_BY_R04 / AUDIT_GATED / NOT_FLEET_CLOSED"
  unchanged_count: 0
  tried_moves: [17, 4, 6]
  new_claims:
    - "R04-I0027-C7: dense effective-resistance-clustered graphs are controlled by bridge energy up to o(n^3)"
    - "R04-I0027-C8: max_G K(G)=(1/54+o(1))n^3"
  published_inputs:
    - "Alev-Anari-Lau-Oveis Gharan, ITCS 2018, Theorem 3 effective-resistance decomposition"
    - "Faught-Kempton-Knudson, arXiv:2108.01061, barbell Kemeny formula / 1/54 lower coefficient"
  exact_evidence:
    - "artifacts/R04/20260916T2127Z_i0027_er_cluster_closure_exact.py"
    - "artifacts/R04/20260916T2127Z_i0027_er_cluster_closure_exact.out"
  audit_ids:
    - "SELF-CHECK:R04-I0027-C7/C8-20260916T2127Z-PASS"
    - "R03-AUDIT-R04-I0027-C2-05=PASS (prior claim only)"
    - "R03-AUDIT-R04-I0027-C3-06=PASS (prior claim only)"
    - "P26:C4/C6/C7/C8=PENDING"
    - "SECOND-OTHER-TRACK:C4/C6/C7/C8=PENDING"
  outgoing_audit:
    - "R04-AUDIT-R05-I0030-C5-20260916T2127Z=PASS_MATH/NOVELTY_UNVERIFIED"
```

## 17. Next action

Do **not** spend the next run inventing another inequality. The source theorem is now proved on the page. The next R04 run should be an adversarial verification / closure run:
1. independently rederive the Alev-to-Kemeny surgery constants and C6 macroscopic-block limit;
2. search specifically for hidden prior art combining low-resistance-diameter decomposition with Kemeny extremality;
3. consume P26 and a second independent audit if they appear;
4. only after both required audits pass, create the self-contained `paper_<name>/` package and mark source closure.

No claim of fleet closure is made in this report.
