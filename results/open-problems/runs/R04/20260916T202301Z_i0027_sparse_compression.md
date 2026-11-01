Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the exposed runtime/scheduler has no model-family or reasoning-effort selector or authenticated telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the frozen coefficient-width metric; Section-B methods actually tried: #1 CHANGE THE CATEGORY, #19 MAKE IT AN ALGORITHM, #29 ADD THE POINTS AT INFINITY.**

Problem/source: David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 6.13, tau_0/Kemeny half only, intake I0027.

# R04 immutable run report — I0027 / sparse surgery and bridge compactification

Run ID: `20260916T202301Z_i0027_sparse_compression`  
Repository: `yspennstate/math-open-problems`, branch `master`.  
Overall source status after this run: **PARTIAL / OPEN**. The full-class coefficient interval does not move in this invocation, but the previous bottleneck-chain theorem is upgraded to an asymptotically lossless reduction to bridge-chain graphs, and the entire leading contribution of the bridge skeleton is proved to be at most the conjectured `1/54`. The remaining obstruction is now isolated inside the effective-resistance geometry of the bridge blocks themselves.

## 1. Continuity, ownership, source/status, exclusions

Before new mathematics I reread/recovered the required control state: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, `QUEUE.md`; `operations/NEW_METHODS_2026-09-16.md`; `operations/claims/I0027.md`; the newest complete own report `runs/R04/20260916T191214Z_i0027_bottleneck_chain.md`; the newest neighboring R03 report `runs/R03/20260916T1909Z_18_second_incidence.md`; and the newest R05 package `runs/R05/20260916T192250Z_i0030_edge_mnhd_n13.md`. Repository search was also repeated for the I0027 aliases and the retired C31/AF4.49(ii) history. Large intake JSONL surfaces remain connector-truncated, so I do not claim a semantic row-by-row reread of all approximately 780 intake rows.

The shared claim file remains an exclusive provisional reservation to R04 but still says `PENDING_ADMISSION, not READY`. I did not edit or promote that shared registry. Current source/status checks below continue to support working under the existing reservation; no conflicting owner was found.

The old R04 critical random-band-matrix route remains preserved in its immutable handoff/history and is not reopened. Historical C31 Kemeny filenames concern the different Aldous–Fill 4.49(ii) source and do not own this target.

### Exact source locator and tau_2 separation

The primary source was rechecked on 2026-09-16 at
`https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch6.S3.html`.
In §6.3.2, equation (6.19) records

\[
\max\tau_0,\ \max\tau_2\le (2/27+o(1))n^3,
\]

and Open Problem 6.13 immediately asks to prove

\[
\max\tau_0\sim n^3/54,
\qquad
\max\tau_2\sim n^3/54.
\]

R04 continues to work only on `tau_0`.

The `tau_2` half remains **KNOWN**: Aksoy--Chung--Tait--Tobin, *The maximum relaxation time of a random walk* (arXiv:1804.05500 / Advances in Applied Mathematics), prove that the minimum nonzero normalized-Laplacian eigenvalue is asymptotic to `54/n^3`; equivalently the maximum relaxation time is `n^3/54`, asymptotically attained by the double kite.

Fresh bounded literature queries on 2026-09-16 included exact `Open Problem 6.13`, `Kemeny maximum n^3/54`, multiplicative degree--Kirchhoff extremal bounds, 1-separation/barbell formulas, later Kemeny papers through 2026, and the recent derivative/edge-centrality literature. I found no current source settling the all-connected-graph `tau_0` asymptotic. This is bounded negative search evidence, not a worldwide novelty certificate.

Relevant prior art used or checked this run:
- Faught--Kempton--Knudson, *A 1-Separation Formula for the Graph Kemeny Constant and Braess Edges*, arXiv:2108.01061 / J. Math. Chem. (2021/22): exact 1-separation formulas, maximal tree result, barbell optimization;
- Aksoy--Chung--Tait--Tobin: sharp `tau_2`/spectral-gap half;
- the 2026 directional-derivative paper on Kemeny's constant: sensitivity/edge-centrality, not the all-graph sharp asymptotic.

## 2. Frozen metric — no movement

Let

\[
M_n:=\max_{|V(G)|=n}\tau_0(G).
\]

Retain the barbell/double-kite lower coefficient

\[
L=1/54,
\]

and R04-I0027-C2's full-class upper coefficient

\[
U=\sqrt2/54.
\]

Therefore the fixed metric remains

\[
\boxed{
W=U-L=(\sqrt2-1)/54
=0.007670621525427686\ldots .
}
\]

Before this run: `(sqrt(2)-1)/54`.  
After this run: **same**.  
Unchanged-run count: `2`.

The preceding coefficient theorem retains the independent audit
`R03-AUDIT-R04-I0027-C2-05 = PASS`; P26 is still pending. No source closure is claimed.

## 3. Method #1 — CHANGE THE CATEGORY: sparse graph surgery as an electrical perturbation

The previous C3 theorem says every cubic-scale contender contains a linearly long nested family of bounded cuts in a uniform spanning tree. To turn that structural statement into an extremal reduction, one must know that deleting only `O(n)` edges from a dense cubic-scale contender cannot change the leading `n^3` Kemeny coefficient by an order-one amount.

That is true with an explicit deterministic bound.

### R04-I0027-C4 — sparse-deletion stability

**STATUS: PROVED.**

Let `G` be a connected simple graph on `n` vertices and let `H` be a connected spanning subgraph. Put

\[
m_G=|E(G)|,\qquad m_H=|E(H)|,\qquad q=m_G-m_H.
\]

Then

\[
\boxed{
K(G)
\le
\frac{m_H}{m_G}K(H)
+
(n-1)\frac{2qm_H+q^2}{m_G}.
}
\tag{C4.1}
\]

In particular,

\[
\boxed{
K(G)\le K(H)+2q(n-1)+\frac{q^2(n-1)}{m_G}.
}
\tag{C4.2}
\]

Hence if `m_G >= a n^2` for some fixed `a>0` and `q=O(n)`, then

\[
K(G)\le K(H)+O_a(n^2)=K(H)+o(n^3).
\tag{C4.3}
\]

#### Proof

Write `d^G=d^H+r`, where `r_v` is the number of deleted edges incident to `v`. Then

\[
\sum_v r_v=2q.
\]

Rayleigh monotonicity gives

\[
R_G(u,v)\le R_H(u,v).
\]

Using the multiplicative degree--Kirchhoff representation

\[
K(G)=\frac1{2m_G}
\sum_{u<v}d^G_ud^G_vR_G(u,v),
\]

we obtain

\[
2m_GK(G)
\le
\sum_{u<v}(d^H_u+r_u)(d^H_v+r_v)R_H(u,v).
\]

The `d^H d^H` part is `2m_HK(H)`. Since a connected `n`-vertex unweighted graph has `R_H(u,v)<=dist_H(u,v)<=n-1`, the two cross terms contribute at most

\[
(n-1)
\sum_{u\ne v}r_ud^H_v
\le
(n-1)(2q)(2m_H)
=4qm_H(n-1),
\]

and the `rr` term contributes at most

\[
(n-1)\sum_{u<v}r_ur_v
\le
2q^2(n-1).
\]

Divide by `2m_G` to obtain C4.1. C4.2 follows from `m_H<=m_G`. QED.

The exact checker exhaustively verifies C4.1 for 976 connected one-edge deletions among Graph Atlas graphs through six vertices and for 1,630 connected multi-edge spanning-subgraph pairs in the enumerated `n<=5` range.

## 4. Method #19 — MAKE IT AN ALGORITHM: compress every cubic contender to a bridge chain

The retained C3 bottleneck theorem is now converted into a deterministic surgery algorithm.

### R04-I0027-C5 — asymptotically lossless bridge-chain reduction

**STATUS: PROVED FROM RETAINED C3; external audit pending.**

Call a graph a **bridge chain** if its vertex set can be partitioned into nonempty connected induced blocks

\[
C_0,C_1,\ldots,C_L
\]

such that there is exactly one edge between `C_{j-1}` and `C_j` for each `j`, each of those edges is a bridge, and there are no other edges between distinct blocks.

Let `M_n^{chain}` denote the maximum Kemeny constant over `n`-vertex bridge-chain graphs. Then

\[
\boxed{
\limsup_{n\to\infty}\frac{M_n}{n^3}
=
\limsup_{n\to\infty}\frac{M_n^{chain}}{n^3}.
}
\tag{C5.1}
\]

So the full Aldous--Fill leading-coefficient problem can be reduced, without asymptotic loss, to bridge chains with completely arbitrary connected blocks.

#### Proof

The `>=` direction is trivial because bridge chains are graphs.

For the reverse direction, use the known barbell lower bound to restrict attention to a subsequence with

\[
K(G_n)\ge \kappa n^3
\]

for a fixed `kappa>0`. Retained C3 provides a spanning tree `T_n` and nested child-subtree cuts

\[
A_1\supsetneq A_2\supsetneq\cdots\supsetneq A_L,
\qquad L=\Theta_\kappa(n),
\]

with

\[
|\partial_GA_j|\le B_\kappa
\]

for a constant `B_kappa` independent of `n`.

Root `T_n` outside `A_1`. Define the layers

\[
C_0=V\setminus A_1,
\qquad
C_j=A_j\setminus A_{j+1}\ (1\le j<L),
\qquad
C_L=A_L.
\]

Because each `A_j` is a child subtree on one root-to-leaf chain, every `C_j` is connected in `T_n`. If `e_j` is the tree edge defining `A_j`, then `e_j` is the unique tree edge between `C_{j-1}` and `C_j`.

Every graph edge whose endpoints lie in distinct layers crosses at least one selected cut. Therefore the number of cross-layer edges satisfies

\[
|E_{cross}|
\le
\sum_{j=1}^L|\partial_GA_j|
\le B_\kappa L
=O_\kappa(n).
\]

Construct `H_n` by retaining every same-layer edge and all tree edges, and deleting every other cross-layer edge. Then `H_n` contains `T_n`, so it is connected; its only inter-layer edges are the `e_j`; hence it is a bridge chain. The deletion count is

\[
q_n=O_\kappa(n).
\]

The elementary bound `K(G)<=m_G(n-1)` implies from `K(G_n)>=kappa n^3` that

\[
m_G\ge \frac{\kappa n^3}{n-1}=\Theta_\kappa(n^2).
\]

C4 therefore yields

\[
K(G_n)\le K(H_n)+O_\kappa(n^2).
\]

Divide by `n^3` and take the limsup. QED.

This is stronger than merely saying an extremizer has a bottleneck: at leading `n^3` scale, **all non-chain cross-links can be surgically removed**.

The exact checker separately validates the layer/cut combinatorics on 200 random finite tree-plus-chord instances with fixed seed `202609162012`: after deleting non-tree cross-layer edges, the graph remains connected and the quotient is exactly the selected bridge path.

## 5. Method #29 — ADD THE POINTS AT INFINITY: compactify the bridge skeleton

C5 says any asymptotic counterexample to `1/54` can be searched for among bridge chains. The next question is whether the bridges themselves can already create a coefficient larger than `1/54`.

They cannot.

For a connected graph `H`, let `B(H)` be its set of bridges. For a bridge `e`, let `A_e,A_e^c` be the two sides after deleting it and write `vol(A)=sum_{v in A}d(v)`. Define the exact **bridge part** of the Kemeny resistance sum by

\[
K_{br}(H)
:=
\frac1{2m}
\sum_{e\in B(H)}
\operatorname{vol}(A_e)\operatorname{vol}(A_e^c).
\tag{5.1}
\]

This is exactly the contribution to `K(H)` coming from the unit resistance of bridge edges; all remaining Kemeny mass comes from effective resistance inside the bridge blocks.

### R04-I0027-C6 — sharp bridge-energy bound

**STATUS: PROVED.**

For every sequence of connected simple `n`-vertex graphs with

\[
m_n=\Theta(n^2),
\]

we have

\[
\boxed{
\limsup_{n\to\infty}
\frac{K_{br}(H_n)}{n^3}
\le \frac1{54}.
}
\tag{C6.1}
\]

The constant is sharp: the balanced double-kite/barbell bridge skeleton attains `1/54+o(1)`.

#### Step 1: exact bridge-block identity

Delete every bridge from `H`. Let the resulting connected components be `C_i`, with

\[
n_i=|C_i|,\qquad m_i=|E(C_i)|.
\]

Contract each `C_i`. The quotient `Q` is a tree. Put

\[
w_i=m_i+1,
\qquad
W=\sum_iw_i=m+1,
\qquad
p_i=w_i/W.
\]

For a quotient edge whose side is the connected node set `S`, the original side contains `|S|-1` internal quotient bridges, hence

\[
\operatorname{vol}(A_e)
=2\sum_{i\in S}m_i+2(|S|-1)+1
=2W p(S)-1.
\]

If `X,Y` are independent quotient vertices with law `p`, the tree cut formula gives

\[
\mathbb E_p d_Q(X,Y)
=2\sum_{e\in E(Q)}p(S_e)(1-p(S_e)).
\]

Substitution into (5.1) yields the exact identity

\[
\boxed{
K_{br}(H)
=
\frac{(m+1)^2}{m}\,\mathbb E_p d_Q(X,Y)
-
\frac{(2m+1)|E(Q)|}{2m}.
}
\tag{C6.2}
\]

The checker verifies this identity exactly on several nontrivial bridge-block quotient paths.

#### Step 2: retain only macroscopic bridge blocks

Pass to a subsequence with

\[
m/n^2\to\alpha>0.
\]

Fix `delta>0` and call a bridge block **large** when `n_i>=delta n`. There are at most `1/delta` such blocks.

For all small blocks,

\[
\sum_{small}m_i
\le
\frac12\sum_{small}n_i^2
\le
\frac{\delta n}{2}\sum_i n_i
\le
\frac\delta2 n^2.
\]

The extra `+1` in each `w_i` sums to at most `n`, so the total `p`-mass outside the large blocks is `O_alpha(delta)+o(1)`.

Let the large-block normalized vertex fractions be

\[
x_i=n_i/n,
\qquad s=\sum_i x_i,
\]

and normalize their `p`-masses to a probability vector `tilde p` with total large mass `P=1-O_alpha(delta)-o(1)`.

The minimal subtree of `Q` joining the large blocks has at most

\[
n-1-\sum_{large}(n_i-1)
=(1-s)n+O_\delta(1)
\]

edges. Thus, after dividing graph distances by `n`, its total available metric length is at most `1-s+o(1)`.

Pairs involving a small block contribute only `O_alpha(delta)n` to `E_p d_Q`. For large-large pairs,

\[
\frac1n\mathbb E_{\tilde p}d_Q(X,Y)
\le
(1-s)
\left(1-\sum_i\tilde p_i^2\right)+o(1),
\tag{5.2}
\]

because every pair distance is at most the total joining-subtree length.

#### Step 3: vertex capacity plus a Renyi interpolation inequality

For a large simple block,

\[
m_i+1\le \frac12n_i^2+o(n^2).
\]

Since `W/n^2 -> alpha`, this gives

\[
x_i
\ge
\sqrt{2\alpha P\,\tilde p_i}+o(1).
\]

Put

\[
S=\sum_i\sqrt{\tilde p_i},
\qquad
Q_2=\sum_i\tilde p_i^2.
\]

Summing the capacity inequality gives

\[
\alpha P\le \frac{s^2}{2S^2}+o(1).
\tag{5.3}
\]

Hölder interpolation at exponents `1/2,1,2` gives

\[
1=\sum_i\tilde p_i
\le
\left(\sum_i\sqrt{\tilde p_i}\right)^{2/3}
\left(\sum_i\tilde p_i^2\right)^{1/3},
\]

so

\[
Q_2S^2\ge1.
\]

Consequently

\[
\frac{1-Q_2}{S^2}
\le
\frac{1-S^{-2}}{S^2}
\le\frac14,
\tag{5.4}
\]

where the last one-variable maximum occurs at `S^2=2`.

Combining (C6.2), (5.2), (5.3), and (5.4), and using `P<=1`, gives

\[
\limsup\frac{K_{br}(H_n)}{n^3}
\le
\frac{s^2(1-s)}8+O_\alpha(\delta).
\]

Finally

\[
\max_{0\le s\le1}\frac{s^2(1-s)}8
=\frac1{54}
\]

at `s=2/3`. Let `delta downarrow 0` to prove C6.1. QED.

The exact checker tests the equivalent finite Renyi inequality

\[
4(Q_2^{raw\,2}-Q_4^{raw})
\le
Q_2^{raw}S_1^2
\]

on 19,530 integer vectors; equality occurs only for two equal positive atoms in the tested domain. It also verifies symbolically that the vertex-budget function is maximized at `s=2/3` with value `1/54`.

### Meaning of C6

C6 is a sharp separation of mechanisms. In a bridge-chain reduction, **the bridge skeleton itself cannot beat Aldous--Fill's constant**. Therefore any hypothetical sequence with

\[
K(G_n)\ge (1/54+\varepsilon)n^3
\]

must obtain a positive `Theta(n^3)` excess from effective resistance **inside** the bridge blocks (equivalently, from large two-terminal moments of blocks encountered by stationary mass crossing the chain).

This is now the exact remaining mathematical obstruction. A proof that internal-block resistance can be recursively charged to the same vertex budget without double-counting would close the source constant.

## 6. Why the source is not closed yet

C5 reduces the full leading-coefficient problem to bridge chains, and C6 proves the bridge term has the sharp conjectured coefficient. However, a bridge chain can have nontrivial effective resistance inside a block between its left and right attachment vertices. Those internal two-terminal terms also enter cross-block resistances.

A terminal block may have small *intrinsic* Kemeny constant yet still possess a distinguished high-resistance pair, so simply inducting on `K(block)` is not presently justified. The source-closing strengthening must control a **two-terminal weighted resistance functional**, not only the unrooted Kemeny constant.

The next route should therefore strengthen the induction state from one scalar `K(G)` to a rooted/two-terminal package containing

\[
K(G),\quad
\mu(G,a)=\sum_v d_vR(v,a),\quad
\mu(G,b),\quad
R(a,b),
\]

because Faught--Kempton--Knudson's 1-separation formula closes exactly on Kemeny constants, rooted moments, and separator resistances. This is a more precise obligation than the previous generic instruction to “analyze the bridge chain.”

## 7. Independent R05 audit — newest n=13 package

Newest R05 package read:
`runs/R05/20260916T192250Z_i0030_edge_mnhd_n13.md`.
Its finite metric moved `12 -> 13`, using four order-13 connected symmetric graphs with valencies

\[
2,4,6,12.
\]

I independently audited the **order-13 completeness** by a prime-degree group-theoretic route, rather than by repeating R05's marked-isomorphism census routine.

External group-theory input: the Burnside--Schur theorem says a primitive permutation group with a regular cyclic subgroup is either 2-transitive or contained in the one-dimensional affine group; Turner's theorem says every vertex-transitive graph of prime order is circulant. For an arc-transitive graph on 13 vertices:
- in the 2-transitive case, adjacency is a nontrivial invariant relation, hence the connected graph is `K_13` (degree 12);
- otherwise, after identifying vertices with `F_13`, the arc stabilizer is a multiplicative subgroup `H<=F_13^*`, and the connection set is one `H`-orbit. Undirected arc-transitivity forces `-1 in H`.

Since `F_13^*` is cyclic of order 12, its subgroups containing `-1` have exactly the orders

\[
2,4,6,12.
\]

Up to multiplication there is one resulting Cayley graph for each order. The R05 adjacency lists are exactly those four cyclic connection-set classes (the degree-4 list uses differences `{+/-1,+/-5}`, and the degree-6 list the order-6 subgroup), together with `C_13` and `K_13`.

The exact R04 checker independently enumerates the subgroup orders, builds the four Cayley classes, verifies connectivity/degree and pairwise non-isomorphism.

Audit ID:
`R04-AUDIT-R05-I0030-N13-PRIME-20260916T202301Z`

Verdict:
**PASS_COMPLETE_ORDER13_CLASSIFICATION_GIVEN_BURNSIDE_SCHUR / NOVELTY_UNVERIFIED.**

This audits the finite order-13 completeness layer; it does not replace the already-existing independent audit of R05's analytic monotonicity theorem.

## 8. Exact artifacts

Executed before archival:

- `artifacts/R04/20260916T202301Z_i0027_sparse_compression_exact.py`
  - creation commit `287000e1a917df67d50aabded80f56717116f960`;
- `artifacts/R04/20260916T202301Z_i0027_sparse_compression_exact.out`
  - creation commit `47cff2f1198cfff4c45a071909aac1cf38f4eb54`.

Archived output ends `RESULT PASS` and records:
- 976 exact one-edge C4 Graph-Atlas checks;
- 1,630 exact multi-edge connected spanning-subgraph C4 checks;
- 200 C5 layer-compression combinatorial checks with seed `202609162012`;
- 19,530 exact C6 Renyi-vector checks;
- symbolic `1/54` optimization;
- exact bridge-block identity checks;
- independent R05 prime-13 subgroup audit.

The unrelated spreadsheet-runtime warmup warning emitted by the local Python environment occurred only after the checker itself had completed with `RESULT PASS`; it does not affect the archived checker output.

## 9. Scheduler/model interface status

The operational limitation is unchanged. The exposed task interface supports prompt/title, schedule/timing and enabled state, but no model-family or reasoning-effort field and no authenticated runtime telemetry. Therefore “GPT-6, maximum” remains a prompt request rather than a verified runtime setting. Honest repair requires the product/API or an authorized owner-facing interface to expose those controls/telemetry.

A task returning “You cannot modify this task” is an ownership/authorization boundary. The permissible workaround is modification from the owning/admin context or platform support; creating a duplicate task or bypassing permissions is not legitimate. The current repository records that P26 succeeded in one authorized P/C context even though other contexts rejected edits, so the permission result is context-specific. No scheduler changes were made in this run.

## 10. Cumulative status and next attack

### Retained full-class metric

\[
\boxed{
1/54
\le
\liminf M_n/n^3
\le
\limsup M_n/n^3
\le
\sqrt2/54.
}
\]

### New claims

- **C4 PROVED:** deleting `O(n)` edges from a dense `Theta(n^2)` graph changes the relevant Kemeny upper comparison by only `O(n^2)`.
- **C5 PROVED from C3:** the all-graph leading coefficient equals the leading coefficient over bridge-chain graphs.
- **C6 PROVED:** the bridge contribution of any dense graph sequence is at most `n^3/54+o(n^3)`, sharply.

### Remaining obligation

The only possible `Theta(n^3)` excess above `1/54` after C5--C6 is internal two-terminal resistance inside the bridge blocks. The next run should formulate and attack a **two-terminal 1-separation induction** using the exact state `(K, mu_a, mu_b, R_ab)` from Faught--Kempton--Knudson, rather than adding another unrooted lemma.

If the frozen coefficient width fails to move once more, the metric will have been unchanged for three consecutive runs and the owner's Section-I stuck protocol must trigger on the following invocation.

```yaml
ledger_delta:
  worker: R04
  source: "Aldous-Fill Open Problem 6.13 / intake I0027, tau_0 half only"
  target: "max over connected simple n-vertex graphs tau_0(G) ~ n^3/54"
  metric: "width U-L of rigorous leading n^3 coefficient interval"
  before:
    L: "1/54"
    U: "sqrt(2)/54"
    width: "(sqrt(2)-1)/54"
  after:
    L: "1/54"
    U: "sqrt(2)/54"
    width: "(sqrt(2)-1)/54"
  movement: "NO MOVEMENT"
  unchanged_count: 2
  status: PARTIAL
  tried_moves: [1, 19, 29]
  new_claims:
    - "R04-I0027-C4: sparse-deletion stability"
    - "R04-I0027-C5: asymptotically lossless reduction to bridge chains"
    - "R04-I0027-C6: sharp 1/54 upper bound for the bridge contribution"
  exact_evidence:
    - "artifacts/R04/20260916T202301Z_i0027_sparse_compression_exact.py @ 287000e1a917df67d50aabded80f56717116f960"
    - "artifacts/R04/20260916T202301Z_i0027_sparse_compression_exact.out @ 47cff2f1198cfff4c45a071909aac1cf38f4eb54"
  audit_ids:
    - "SELF-CHECK:R04-I0027-C4/C5/C6-20260916T202301Z-PASS"
    - "R03-AUDIT-R04-I0027-C2-05=PASS (preceding coefficient theorem)"
    - "P26:PENDING"
  outgoing_audit:
    - "R04-AUDIT-R05-I0030-N13-PRIME-20260916T202301Z:PASS_COMPLETE_ORDER13_CLASSIFICATION_GIVEN_BURNSIDE_SCHUR/NOVELTY_UNVERIFIED"
```

**No claim of source closure is made.**
