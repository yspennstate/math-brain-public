# FOREST / fleet02 B01 — source-safe loopless transfer pays STAR-2 and yields an all-edge Simpson gate

**Run:** `B01-20260922T090454Z-forest-r17`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Parent target:** OPEN; no full-proof claim.

## 1. Fresh controls and source scope


The target remains exactly the unit uniform law on **all** unrooted forests of every finite simple graph, including disconnected forests and all sizes. Old installation/benchmark work remains stopped.

Latest complete lead version actually consumed: fleet01/B01 run `20260922T050946Z-b01-forest-auto11`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, canonical report creation commit `79044b575c4b689248892f37b9930e983dddabca`. Its source-safe chain proves the Simpson deletion/contraction gate only for third edges contained in no triangle and identifies the triangle case as the `{1,2}`-weighted contracted-star debt `STAR-2`.

Named partner results consumed and applied:

- fleet03/B02 run `20260922T050248Z-B02-forest-r13`, report blob `6c3101a038048aecfb7a0e788cb73630945d1c62`, which records the exact three-length-two-path unit simulation of a loopless multigraph edge and the class-wide simple <-> loopless-multigraph transfer without needing the fixed-graph weighted Cocks implication;
- fleet03/B02 run `20260922T080202Z-B02-forest-r11`, report blob `6400890ad534d0e095716d83402946e60fc04e58`, which proves the exact nonnegative Rayleigh formula when the marked pair are two members of a three-edge cut.

My immediate complete predecessor is fleet02/B01 `B01-20260922T081641Z-forest-r17`, report blob `86f82b29bd0c186c46dbd6706eda65e51d10a5dc`. Its path-packing / cut-surplus work is retained, not repeated.

## 2. The theta-3 marked-edge transfer, fully written in source language

Let `M` be any finite loopless multigraph. Replace every labelled edge `h=uv` by three internally vertex-disjoint length-two paths `u-a_{h,j}-v`, `j=1,2,3`, using fresh internal vertices for every labelled edge. Call the resulting graph `S(M)`. Even when `M` has parallel edges, `S(M)` is simple because all internal vertices are distinct.

For a forest of `S(M)`, define the projected indicator `Y_h=1` iff exactly one of the three paths in gadget `h` is complete. A forest can never contain two complete paths in one gadget, since they form a 4-cycle. Conversely, after fixing each gadget to have either no complete path or exactly one complete path, an expanded cycle exists iff the projected labelled edges contain a multigraph cycle. Hence projection takes expanded forests exactly to multigraph forests.

The local lift counts are equal:

- projection `Y_h=0`: each length-two path is in one of its three incomplete states, so `L0=3^3=27`;
- projection `Y_h=1`: choose the complete path in 3 ways and choose incomplete states on the other two paths, so `L1=3*3^2=27`.

Therefore every multigraph forest has exactly `27^{|E(M)|}` lifts and the projection of the uniform forest of `S(M)` is exactly the uniform forest of `M`.

For a marked multigraph edge `h`, choose one physical half-edge `A_h` of one distinguished length-two path in its gadget. Conditional on the projection,

`P(A_h=1 | Y_h=0)=1/3`,

`P(A_h=1 | Y_h=1)=1/3+(2/3)(1/3)=5/9`.

Thus

`E[A_h | Y]=1/3+(2/9)Y_h`.

Given the full projection, different gadgets are independent because their conditional lift counts factor. Consequently for two distinct marked multigraph edges `e,f`,

`Cov_{S(M)}(A_e,A_f) = (2/9)^2 Cov_M(Y_e,Y_f) = (4/81) Cov_M(e,f)`.      (2.1)

Hence a positive-covariance pair in a loopless multigraph would give a positive-covariance pair in a finite simple graph. Since simple graphs are already a subclass of loopless multigraphs, the source conjecture is **equivalent** to its labelled loopless-multigraph version. This is a class-wide unit-law transfer; it does not assert arbitrary external-field Rayleigh for one fixed graph.

This pays the lead's `STAR-2` source debt by changing the induction universe rather than proving a weighted theorem: after moving to a minimal loopless unit counterexample, a triangle contraction is simply another smaller **unit** loopless multigraph, with parallel copies retained as labelled edges.

## 3. New theorem A — all-edge deletion/contraction Simpson gate

Assume the source conjecture is false. By (2.1), choose a loopless-multigraph counterexample `M` with the minimum number `m` of nonloop labelled edges, and choose a bad pair `e,f` with

`c = Cov(X_e,X_f) > 0`.

Fix any third edge `g`. Let `p=P(g in F)`. Since `g` is a nonloop, the empty forest and singleton `{g}` both exist, so `0<p<1`.

Conditioning on `g=0` is the uniform forest law of `M\g`, hence

`c0 = Cov(X_e,X_f | g=0) <= 0`

by edge-minimality. Conditioning on `g=1`, deleting the compulsory copy and contracting its endpoints gives the uniform forest law of `M/g` after discarding loops. If a marked edge becomes a loop because it was parallel to `g`, its conditional indicator is identically zero; otherwise the two marked labelled copies survive in a smaller loopless multigraph. Therefore in every case

`c1 = Cov(X_e,X_f | g=1) <= 0`.

The binary law of total covariance gives exactly

`c = (1-p)c0 + p c1 + Cov(X_e,X_g) Cov(X_f,X_g) / Var(X_g)`.

Hence for **every** third edge,

`boxed: Cov(X_e,X_g) Cov(X_f,X_g) / Var(X_g) >= c > 0.`          (3.1)

Writing `rho_ij` for correlations and `a=rho_ef>0`, this becomes

`boxed: rho_eg rho_fg >= a > 0.`                                 (3.2)

No triangle exception remains. This is precisely the lead's formerly triangle-free Simpson gate, now paid for every conditioner without fixed-graph weighted Cocks.

## 4. New theorem B — the positive-covariance graph is a global matching

The preceding argument applies to **any** positive-covariance pair in the same edge-minimal counterexample, because any such pair is itself a source violation.

If `Cov(i,j)>0` and `Cov(j,k)>0`, apply (3.1) to the bad pair `(i,j)` with conditioner `k`. The product `Cov(i,k)Cov(j,k)` is positive, and the second factor is positive, so `Cov(i,k)>0`. Thus positive covariance is transitive.

A positive triangle is impossible. For three distinct edges with positive correlations

`x=rho_ij`, `y=rho_ik`, `z=rho_jk`,

(3.2) applied cyclically gives

`x <= yz`, `y <= xz`, `z <= xy`.

Multiplying yields `xyz <= (xyz)^2`. But `0<x,y,z<1`: distinct edge indicators cannot have correlation 1 because the singleton forests `{i}` and `{j}` both occur with positive probability and distinguish them. Contradiction.

Therefore every positive-covariance connected component has size at most two:

`boxed: the graph on E(M) with ij an edge iff Cov(X_i,X_j)>0 is a matching.`   (4.1)

In particular, for the chosen bad pair `(e,f)`, every third edge satisfies the strict sign conclusion

`boxed: Cov(X_e,X_g)<0 and Cov(X_f,X_g)<0.`                        (4.2)

This upgrades the lead's matching theorem from triangle-free physical edges to **all** physical labelled edges.

## 5. New theorem C — exact two-edge-cut formula and connectedness of M-{e,f}

A second separator identity is useful and needs no weighted transfer. Suppose a vertex bipartition has exactly two crossing labelled edges `{e,f}`. Delete the two cut edges. Let `Z_L,Z_R` count forests on the two sides, and let `C_L,C_R` count side forests connecting the two boundary endpoints on that side. Put

`N=Z_L Z_R`, `B=C_L C_R`.

For a pair of side forests not counted by `B`, all four subsets of `{e,f}` are allowed. For a pair counted by `B`, the subset `{e,f}` is the unique forbidden cut choice. Hence

`Z=4N-B`, `Z_e=Z_f=2N-B`, `Z_ef=N-B`,

and therefore

`boxed: Z_e Z_f - Z Z_ef = N B >= 0.`                            (5.1)

So two edges forming an entire two-edge cut can never be a bad pair.

This immediately proves a source-safe structural fact for the minimal loopless counterexample:

`boxed: M-{e,f} is connected.`                                   (5.2)

Indeed, `M` itself is connected (otherwise factor away components not containing both marks, while marks in different components are independent), and no marked edge is a coloop. If `M-{e,f}` had two components, either exactly one mark reconnects them, making it a coloop, or both reconnect them and form the two-edge cut excluded by (5.1). Three components would force the two marked edges to be bridges in the component tree; more than three cannot be connected by only two added edges.

Also, `M` has no unmarked coloop: a coloop factors as an independent fair choice, so deleting it preserves the bad-pair marginal law and gives a smaller counterexample.

## 6. New theorem D — partner triad formula forces a two-path bridge skeleton

Let `G0=M-{e,f}`, which is connected by (5.2), and let `g` be a bridge of `G0`. Removing `g` defines a vertex cut. In `M` the only possible additional crossing copies are `e` and `f`.

- Neither mark can cross, because then `g` is a coloop of `M`.
- Both marks cannot cross. In that case `{e,f,g}` is exactly a three-edge cut. The fleet03/B02 triad-cut proof is purely a forest-count factorization after deleting the three labelled cut edges; it does not use simplicity of the side graphs, so it extends verbatim to loopless multigraph sides. Its Rayleigh gap is a sum of nonnegative terms and rules out `e,f` as a bad pair.

Therefore every bridge of `G0` is crossed by **exactly one** of the two marked edges.

Contract each 2-edge-connected bridge-block of `G0` to a vertex and let `T` be the resulting bridge tree. A bridge of `T` lies on the unique block-tree path `P_e` between the endpoint blocks of `e` iff `e` crosses that bridge cut, and similarly for `P_f`. The preceding paragraph says every tree edge lies on exactly one of these paths. Hence

`boxed: E(T)=E(P_e) disjoint_union E(P_f).`                       (6.1)

If both paths are nonempty they meet in exactly one tree vertex; if one is empty, the other is all of `T`. Thus the bridge skeleton of `G0` is not arbitrary: it is the union of at most two edge-disjoint simple paths, with at most one branching block.

This conclusion does **not** assume the disputed weighted two-separator reduction or a pre-existing 3-connected-minimal-counterexample theorem.

## 7. New theorem E — the lead spectral budget now holds on every third edge

Apply the lead's already source-checked rank-homogeneous complete-log-concavity inequality to the graphic matroid of `M`. Let `R` be matroid rank, `K=|F|`, `mu=E K`, `p_h=P(h in F)`, `c_h=Cov(X_h,K)`, and

`T_h = c_h^2 / ((R-mu)p_h(1-p_h)).`

The lead inequality says

`T_e + sum_{h!=e}(1-p_h) rho_eh^2 <= p_e`,

and likewise for `f`. Adding, retaining the marked-pair terms, and using the all-edge (3.2) gives

`T_e+T_f +(2-p_e-p_f)a^2 + sum_{g!=e,f}(1-p_g)(rho_eg^2+rho_fg^2) <= p_e+p_f`.

For every third `g`, AM-GM and (3.2) give `rho_eg^2+rho_fg^2 >= 2a`. Deleting an edge injects containing forests into omitting forests, so `p_h<=1/2`. In the minimal counterexample equality cannot occur because equality is exactly the coloop factor case already excluded. Hence

`boxed: T_e+T_f+a^2+(m-2)a < 1.`                                 (7.1)

In particular

`a < (sqrt((m-2)^2+4)-(m-2))/2`.

The significance is not the numerical bound alone: the lead's triangle-free set `S` has been replaced by the **entire set of m-2 third edges**, with all of them carrying the strict negative sign (4.2).

## 8. Exact regression used in this run

`theta3_cut2_check.py` performs direct exact-rational enumeration for two independent checks:

1. the theta-3 marked-edge covariance factor `4/81` on a triangle and on a genuine triple-parallel loopless multigraph;
2. formula (5.1) on the C4 two-side/two-cut example.

Captured output:

`triangle: base=(Z=7,Ze=3,Zf=3,Zef=1,gap=2,cov=-2/49); theta3=(Z=137781,Ze=59049,Zf=59049,Zef=25029,gap=38263752,cov=-8/3969); cov_ratio=4/81`

`triple_parallel: base=(Z=4,Ze=1,Zf=1,Zef=0,gap=1,cov=-1/16); theta3=(Z=78732,Ze=30618,Zf=30618,Zef=11664,gap=19131876,cov=-1/324); cov_ratio=4/81`

`two_cut_C4: Z=15,Ze=7,Zf=7,Zef=3,gap=4,expected_gap=4`

`THETA3_AND_CUT2_REGRESSION_PASS`

Script Git blob: `254d3ea40ced839b69cf537450af6481572fc9f0`; SHA-256 `174edf96b019c5295e68a45f8e16657d9fb2c3494bc9758239af09995f8618bc`.

Output Git blob: `cef3032cf1e83fcbf3bbaf0b458a9248ff56f146`; SHA-256 `6af7b79ff607c682916bfb915611bdd45deecda6bd6873e6c7e0b61e1460aee6`.

The computation is regression evidence only. Theorems (2.1), (3.1), (4.1), (5.1), and (6.1) are symbolic.

## 9. Compact conditional end-to-end chain and exact remaining implication

The alternative source-safe route is now:

1. if the simple FOREST target fails, theta-3 marked-edge scaling produces an edge-minimal loopless **unit** counterexample;
2. every deletion and contraction of a third labelled edge is a smaller loopless unit instance, so the total-covariance Simpson gate is valid for **all** third edges — this directly pays the lead's `STAR-2` gap without arbitrary weights;
3. the positive-covariance graph of the minimal counterexample is a matching; the bad pair is strictly negatively correlated with every other edge;
4. the exact two-cut formula forces `M-{e,f}` to be connected;
5. the named partner's exact triad-cut formula forces every bridge of `M-{e,f}` to be crossed by exactly one mark, so its bridge tree is the union of two edge-disjoint marked paths;
6. the lead's rank-homogeneous spectral inequality therefore receives the Simpson lower bound from every third edge, giving (7.1).

The **first essential remaining implication** is now `ALL-EDGE-MATCHING-INCONSISTENCY / BRIDGE-PATH-CLOSURE-v1`:

> prove that no loopless graphic independent-set law can have a positive marked pair `(e,f)` while simultaneously satisfying (3.1) for every third edge, the global matching sign structure (4.1)-(4.2), connected `M-{e,f}`, the bridge-path skeleton (6.1), and the rank budget (7.1); or construct an actual loopless graph realizing all of these constraints and a positive marked covariance.

This is strictly downstream of the lead's former triangle/STAR-2 debt; that debt is paid here. I do not assume the remaining inconsistency and therefore do not claim `FULL_PROOF_CANDIDATE`.

## 10. Integrity and operational record

Current-account managed inventory was inspected once: 20/20 fleet02 tasks were enabled with hourly-valid recurrence and quiet task-level notification/email flags. No gap was observed and B01 made zero scheduler mutations. No other-account authentication or mutation occurred.

No brain runtime was authenticated or used, so execution remains `WITHOUT_VERIFIED_BRAIN`. No installation, benchmark, sealed-answer access, email, Drive, public posting, paid API/model/Codex call, remote workflow, permission change, or production-state activation was performed.

Model self-report: `GPT-5.6 Sol`. Requested effort: `maximum actually supported`. Configured effort: `UNKNOWN / not exposed`. Known actual effort: `UNKNOWN / not exposed`. Provider reasoning-token usage: `null / not exposed`. Provider thinking time: `null / not exposed`. Elapsed execution is recorded separately at finish and includes connector/runtime overhead rather than pure thinking.
