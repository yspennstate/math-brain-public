# B02 FOREST research report — universal STAR-2 unitizers cannot be size-controlled

**Run:** `20260922T095045Z-b02-forest-r11`  
**Outcome:** `CANDIDATE_REFUTED`  
**Refuted mechanism:** `UNIVERSAL_JOINT_STAR2_UNITIZER_AS_MINIMALITY_STEP`  
**Parent target:** FOREST remains `OPEN`; no target-level proof or disproof is claimed.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh controls and exact inherited scope


The latest complete campaign-lead version actually read is fleet01/B01 candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, canonical report revision `79044b575c4b689248892f37b9930e983dddabca` and source-bound handoff blob `4cee205cb7d254caf785692838111988a0b8a155`. I use only its source-safe edge-minimal triangle-conditioning localization: contracting a triangle edge `g=uv` creates weight 2 exactly on the star edges corresponding to common neighbors of `u,v`. I do **not** use its rank-degree complete-log-concavity claim; the preceding B02 run supplied the explicit K3 obstruction showing that rank-degree homogenization is not the cited CLC theorem.

Named OTHER-account result consumed and applied: fleet02/B03 run `20260922T094532Z-b03-forest-auto11`, report blob `d5915bec9e6d551a078f7f1902d1492cc7989ac7`, checker-output blob `bb7d53e3eb7091e5f48fe6b232e321d61a1c7a0d`. Its exact theorem is that every finite simple unit two-terminal network of response `C/D=2` has at least 7 edges and at least 5 vertices; the minima are attained simultaneously by the direct terminal edge plus three internally-disjoint length-2 terminal paths, with `(D,C)=(27,54)`. The peer also proved that independent replacement of each doubled star edge therefore cannot preserve edge-minimality.

The present run strengthens that no-go result from **independent local gadgets** to **every boundary-exact joint unitizer**, including gadgets that try to share internal structure across the whole doubled star.

## 2. Exact boundary formulation

Let the source-generated weighted star have terminals

`c,w_1,...,w_d`

and weighted edges `c w_i`, each of activity 2. Denote it by `S_d^(2)`.

For a finite simple unit network `N` with the same terminals (and arbitrary additional internal vertices), let

`W_N(pi)`

be the number of forests of `N` whose connectivity relation on the terminal set is exactly the partition `pi`.

Call `N` a **boundary-exact universal unitizer** for `S_d^(2)` if there is a scalar `lambda>0` such that for every terminal partition `pi`,

`W_N(pi) = lambda W_S(pi)`.

This is the standard condition needed for substituting `N` for the weighted star inside an arbitrary outside graph without changing relative forest weights: gluing to the outside depends only on the terminal connectivity partition, and the common scalar cancels from every normalized probability and multiplies all marked forest counts equally.

The weighted star has only the partitions

`pi_T = { {c} union T } union { {w_i}: w_i notin T }`,  `T subseteq {w_1,...,w_d}`,

and

`W_S(pi_T)=2^|T|`.

Every partition in which two leaves lie in one block while `c` is outside that block has weight zero.

## 3. New theorem: every boundary-exact joint unitizer splits into response-2 branches

### Theorem

If a finite simple unit network `N` is a boundary-exact universal unitizer for `S_d^(2)`, then

`|E(N)| >= 7d`

and

`|V(N)| >= 1+4d`.

More precisely, after deleting terminal-free 1-sum factors that contribute only a common scalar, `N` is a 1-sum at `c` of `d` two-terminal subnetworks `N_i`, one for each leaf `w_i`, and every `N_i` has exact response

`C_i/D_i = 2`.

Consequently the fleet02/B03 seven-edge two-terminal lower bound applies independently to every branch. Shared internal structure cannot reduce the edge count of an exact universal star emulator.

### Proof, including multiplicities and acyclicity

Remove the center vertex `c` from the underlying graph of `N`. I first claim that every connected component of `N-c` contains at most one leaf terminal.

Suppose instead that one component contains distinct leaves `w_i,w_j`. Because it is connected, it contains a simple path `P` from `w_i` to `w_j` avoiding `c`. Choose exactly the edges of `P` and no other edges of `N`. This edge set is a forest: a simple path contains no cycle. Its induced terminal partition has a block containing `w_i,w_j` but not `c`. Therefore `W_N(pi)>=1` for a partition whose weighted-star value is zero, contradicting boundary exactness. Hence each component of `N-c` contains at most one leaf.

For each component `C` of `N-c`, let `N_C` be the subgraph induced by `C union {c}`, including all edges from `c` into `C`. Distinct `N_C` share only the articulation vertex `c` and have disjoint edge sets.

There is now a literal multiplicity-one forest decomposition:

`F subseteq E(N)` is a forest

if and only if every restriction `F_C = F intersect E(N_C)` is a forest.

The forward direction is hereditary. Conversely, if every `F_C` is acyclic, a cycle in their union would have to use edges from two different components of `N-c`; such a simple cycle would have to leave and re-enter `c`, hence visit `c` twice, impossible. Thus restriction gives a bijection

`Forests(N) <-> product_C Forests(N_C)`.

This proves both acyclicity and multiplicity one rather than assuming a local swap is injective.

Components containing no leaf terminal contribute a positive scalar

`Q = product_C |Forests(N_C)|`

to every boundary state. For the unique component containing `w_i`, write `N_i=N_C`, and let

- `D_i` be the number of forests of `N_i` in which `c,w_i` are disconnected;
- `C_i` be the number in which they are connected.

The empty forest gives `D_i>0`. By the product bijection, for every `T subseteq {1,...,d}`,

`W_N(pi_T) = Q product_{i in T} C_i product_{i notin T} D_i`.      (1)

Boundary exactness and the target signature give

`W_N(pi_T)=lambda 2^|T|`.                                      (2)

Taking `T=empty` in (1)-(2),

`lambda = Q product_i D_i`.

Taking `T={i}` and dividing by the empty-state identity gives exactly

`C_i/D_i = 2`                                                    (3)

for every branch `i`.

Now apply the named fleet02/B03 theorem to each finite simple unit two-terminal `N_i`: response 2 forces at least 7 edges and 5 vertices. Edge sets of the branches are disjoint, so

`|E(N)| >= sum_i |E(N_i)| >= 7d`.

The non-center vertices of distinct branches are disjoint, so

`|V(N)| >= 1 + sum_i (|V(N_i)|-1) >= 1+4d`.

Terminal-free components can only increase these counts. This proves the theorem. QED.

## 4. Exact consequence for the lead's edge-minimal STAR-2 route

Let the edge-minimal simple parent counterexample candidate have `m` edges, and let a conditioned triangle edge `g=uv` have exactly `d>=1` common neighbors. Contracting `g` and collapsing each resulting parallel pair to one representative weight-2 edge gives a simple weighted quotient `J` with

`|E(J)| = m-1-d`.

The `d` weighted representatives are part of those `m-1-d` edges. If one deletes them and substitutes any boundary-exact universal unitizer `N`, the resulting unit-simple graph has

`|E(S)| = (m-1-d)-d+|E(N)|`

and therefore, by the theorem,

`|E(S)| >= m-1-2d+7d = m-1+5d > m`.                            (4)

So **no exact universal terminal-network substitution, even a fully joint gadget sharing arbitrary internal structure across the star, can turn the source-generated STAR-2 quotient into a smaller unit-simple graph for edge-minimal induction.**

This strictly strengthens fleet02/B03's no-go statement. The peer ruled out independent local response-2 replacements. Equation (1) shows that boundary exactness itself forces every supposed joint emulator to decompose into response-2 branches, so independent replacement is already globally optimal within the entire universal-substitution class.

Thus the following candidate mechanism is refuted:

`CANDIDATE_REFUTED: UNIVERSAL_JOINT_STAR2_UNITIZER_AS_MINIMALITY_STEP`.

The no-go theorem does **not** rule out a parent-specific transformation that uses the outside graph or moves mass between different boundary fibers; such a map is not a universal terminal substitution and need not reproduce every boundary partition separately.

## 5. First essential missing implication after the no-go theorem

The source-safe conditional end-to-end route is now sharper:

1. Choose an edge-minimal simple counterexample and violating marked pair `(e,f)`.
2. Triangle-free conditioners remain source-safe because both deletion and contraction are smaller simple graphs.
3. A triangle conditioner creates the exact `{1,2}`-weighted star described by the lead.
4. Universal unitization cannot restore simple-graph minimality by Theorem 3 above.
5. Therefore the first unpaid implication must be a **parent-specific cross-fiber comparison**, not another terminal gadget.

For one doubled edge `h`, fleet02/B03 gives the exact quadratic identity

`q(t)=Delta(e,f;t)=D0+M t+D1 t^2`,

`q(2)=2q(1)-q(0)+2D1`.                                         (5)

The missing step is to prove (5) is nonnegative from the actual split-triangle parent fibers, or to find a genuine source-valid counterexample. For several doubled star edges, the analogous proof must couple the fibers jointly; repeated independent unitization is now rigorously excluded.

A useful equivalent unweighted formulation is retained. If `g=uv` is the conditioned parent edge and `H=G-g`, then deleting compulsory `g` is a bijection between forests of `G` containing `g` and forests `A` of `H` satisfying `u` and `v` disconnected. Its inverse is `A -> A+g`, whose acyclicity follows because `g` joins two different components. Hence the contraction gap is exactly the pairwise gap in the uniform law on forests of the smaller simple `H`, **conditioned on `u` and `v` being disconnected**. If `D,D_e,D_f,D_ef` denote those conditional counts, the missing inequality is

`D_e D_f - D D_ef >= 0`.                                       (6)

Equation (6) is the clean target for a genuine forest-pair switching. It must exploit the fact that `H+uv` is the edge-minimal parent; proving (6) for arbitrary `(H,u,v)` is essentially a weighted/minor-strengthening and should not be mislabeled as a small lemma.

## 6. Exact finite stress test of the conditioned formulation

I executed a new exact integer exhaustive check of (6), independent of the partner's gadget checker. By relabelling it suffices to fix terminals `u=0,v=1`. For each `n=3,4,5,6`, the checker enumerates every simple graph `H` on `[n]` with `01` absent, every pair of distinct present marked edges, and every forest of `H`; it retains exactly the forests with `0,1` disconnected and computes

`gap = D_e D_f - D D_ef`.

A subset-zeta transform makes the census exact over all graph supermasks. Results:

| n | graphs H | marked-pair instances | negative | zero | positive | maximum gap |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 4 | 1 | 0 | 0 | 1 | 1 |
| 4 | 32 | 80 | 0 | 24 | 56 | 16 |
| 5 | 512 | 4,608 | 0 | 1,200 | 3,408 | 529 |
| 6 | 16,384 | 372,736 | 0 | 67,248 | 305,488 | 31,684 |

Total: **377,425** marked-pair instances and **zero negative gaps**. The attached stdout ends `STATUS=PASS`.

This is `AUXILIARY_ONLY` evidence, not closure: a finite census does not prove (6) in general. It does show that the direct conditioned-disconnection formulation survives exhaustive testing through six vertices, including source-generated STAR-2 contractions, and it gives a regression target for the next cross-fiber switching.

## 7. Status and next action

**Run outcome: `CANDIDATE_REFUTED`.** Parent FOREST remains open.

The substantive advance is a structural impossibility theorem: exact universal joint STAR-2 emulation cannot share its way around the partner's seven-edge lower bound. Any successful proof through triangle conditioning must therefore use the **specific parent graph** and transfer mass across boundary-connectivity fibers, or prove the conditioned-disconnection gap (6) directly. The most useful next B02 attack is a multiplicity-controlled map on pairs

`D_00 x D_11 -> D_10 x D_01`

that is allowed to change the union/intersection fiber and uses the split edge `uv`/triangle-star geometry as a certificate. A union/intersection-preserving local exchange is not assumed injective.

No installation/benchmark work, scheduler mutation, email, Drive, public posting, paid/remote compute, credential access, permission change, or production mutation was performed. Model self-report is `GPT-5.6 Sol`; configured reasoning effort is `UNKNOWN_NOT_EXPOSED` in the latest fleet01 inventory. Notification flags exposed in that inventory are already false for B02. Provider thinking counters are not exposed.
