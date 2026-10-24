Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — nonfree power-thickening of a free core

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorem proved below; universal T09 remains OPEN.** The theorem is complete as written and has an exact-arithmetic self-check, but it has not had independent review. External priority of this exact power-thickening family is **UNVERIFIED** after the bounded literature check recorded below.

## 1. Frozen source problem and source-level before/after

The parent problem is unchanged:

> For iid bond percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

The universal statement remains **OPEN**.

### Before this run

The NM13-11 lane had proved genuine fixed-graph gaps using free cores and nonbacktracking operator control. In particular, one earlier theorem covered groups with a symmetric 3-element generating set `B` and an embedded free subgroup by adding a *free marked set* `c_1^{+-1},...,c_r^{+-1}`; for `r=4` this gave degree-11 examples in `SL_n(Z)`, `n>=5`. Later runs developed triangle-fibre, S-arithmetic, and Rattaggi product/free-augmentation families, culminating in a complete explicit free Schreier-augmentation tail on the Rattaggi group.

The explicit structural weakness left open was that the added marked generators themselves were free (or contained a free layer that was the whole added set). The first promised weakening was to permit genuine algebraic relations among the new generators while preserving an actual `p_c`-to-`p_u` transfer.

### After this run

Let `Gamma` have a symmetric generating set `B` with `|B|=3` and contain a subgroup `F_2`. Let `E` be any finite set of distinct positive integers with `M=|E|>=2`. Then one can choose free elements `c_1,...,c_r` inside the embedded `F_2`, avoiding all collisions with `B`, and form

`S(B,E,r) = B union { c_i^{+- e} : 1<=i<=r, e in E }`.

This marked set is **not free** as soon as `M>=2`: for two distinct exponents `e,f in E`, powers of each fixed `c_i` satisfy a nontrivial relation

`(c_i^e)^(f/d) = (c_i^f)^(e/d)`, where `d=gcd(e,f)`.

Nevertheless, writing

`q=2r-1`, `D=3+M(q+1)`, `Q=D-1=Mq+M+2`,

I prove

`p_c(Cay(Gamma,S)) <= 1/q`

and

`p_u(Cay(Gamma,S)) >= p_{2->2}(Cay(Gamma,S)) >= 1/beta_D(3+2M sqrt(q))`,

where

`beta_D(a)=sqrt(Q)` if `a<=2sqrt(Q)`, and otherwise

`beta_D(a)=(a+sqrt(a^2-4Q))/2`.

Hence every parameter pair satisfying

`beta_D(3+2M sqrt(q)) < q`

has a strict source-level gap. Two proved ranges are:

1. `M=2` and **every `r>=10`** (`q>=19`);
2. every `M>=2` whenever **`q >= (2M+1)^2`**.

The concrete endpoint `M=2,r=10` has degree `D=43` and the exact rational certificate

`p_c <= 1/19 < 20/363 < p_u`,

so

`boxed(p_u-p_c > 17/6897 = 0.002464839785413948...)`.

This is a new source-level class for the track: the full generating set has systematic power relations and many short cycles; it is not a tree/free-marked-set perturbation.

For every `n>=5`, `SL_n(Z)` has a `(2,3)` generating pair, hence a symmetric 3-element generating set, and contains `F_2`. Therefore every `SL_n(Z)`, `n>=5`, admits the above degree-43 nonfree power-thickened Cayley graphs with the displayed quantitative gap. The group-level existence of *some* favorable generating set is old (Pak--Smirnova-Nagnibeda); the advance here is the explicit related marked family and the quantitative transfer for it, not a new existence theorem for the group.

**Original-problem delta:** before, this branch of the argument required the entire added marked set to be free; after, it proves `p_c<p_u` for explicit nonfree power-thickened marked sets with arbitrarily many prescribed exponent layers (subject to the displayed rank condition).

**Mechanism delta:** the `p_c` witness and the operator charge are now separated. One exponent layer supplies a free-tree percolation subgraph, while every additional power layer may introduce relations but costs only one free-tree adjacency norm in `ell^2`.

## 2. Compact continuity handoff

The controlling policy is `operations/PROGRESS20_2026-09-20.md`; LIVE20 assigns NM11 to T09 at `proofnet24/NM13-11/progress-percolation/`.

Preserved June Benjamini--Schramm attempts include finite-set escape plus BK/last-exit decompositions, killed-SAW and susceptibility-weighted boundary energy, global `ell^2` SAW growth, scalar nonbacktracking/product stress tests, quotient/fibre-shell arguments, and fixed-endpoint bridge criteria. Several remained CONDITIONAL because their auxiliary inequalities never transferred all the way to a strict `p_c<p_u` statement. Those are not relabelled as progress here.

The current NM13-11 sequence then obtained actual transfers on explicit `SL_3(Z)`, free-core, triangle-fibre, S-arithmetic and Rattaggi fixed generating sets. The immediate predecessor closed the explicit Rattaggi free Schreier-augmentation family for all finite ranks. This run therefore did **not** increase that free rank again. It changes the marked-set algebra by adding dependent power layers and proves that the gap survives.

No unchanged-run recovery is triggered: the source-level theorem scope moved in this invocation.

## 3. Choosing the free core while avoiding the ambient generators

Fix an embedded free subgroup `F=<u,v> ~= F_2` of `Gamma`. Consider

`phi:F->Z`, `phi(u)=1`, `phi(v)=0`.

Schreier rewriting gives the free basis

`C_infty={ u^j v u^{-j} : j in Z }`

for `ker(phi)`.

Let `E` and `B` be finite. For distinct basis elements `c_j,c_k` and positive integers `e,f`, an equality

`c_j^e=c_k^f != 1`

would force `c_j` and `c_k` to lie in the same cyclic centralizer in the free group. Distinct members of the displayed Schreier basis do not, so `j=k`; then uniqueness of powers in the infinite cyclic group `<c_j>` gives `e=f`. Thus all power labels `c_j^e` are distinct across `(j,e)`.

Only finitely many `j` can have some `c_j^{+-e}` in the finite set `B`. Delete those indices and choose any remaining `r`. This gives a simple symmetric generating set `S(B,E,r)` because `B` already generates `Gamma` and the new labels are nontrivial, pairwise distinct, and disjoint from `B`.

For each fixed positive exponent `e`, the substitution endomorphism of `F_r=<c_1,...,c_r>` given by

`c_i |-> c_i^e`

is injective: substituting the blocks `c_i^{+-e}` into a nonempty reduced word cannot cancel the entire word, since adjacent inverse letters were absent before substitution. Hence

`H_e=<c_1^e,...,c_r^e> ~= F_r`.

This elementary fact drives both sides of the percolation comparison.

## 4. Critical side: one power layer already gives a tree

Fix any `e in E`. The subgraph using only the edges labelled by

`{c_1^{+-e},...,c_r^{+-e}}`

is a disjoint union of left cosets of `H_e`, each canonically the `2r`-regular tree `T_{2r}`. Therefore

`p_c(G) <= p_c(T_{2r}) = 1/(2r-1) = 1/q`.      (4.1)

This is a direct infinite-cluster comparison, not a finite event or an auxiliary bound.

Notice that no assumption says the *union* over exponents is free. Indeed it is not when `M>=2`; (4.1) needs only one layer.

## 5. Operator side: each dependent layer costs only `2 sqrt(q)`

Let

`K_e = sum_{i=1}^r (R_{c_i^e}+R_{c_i^{-e}})`

on `ell^2(Gamma)`. Right multiplication by `H_e` preserves its left cosets, so `K_e` is a direct sum of adjacency operators of `T_{2r}`. Kesten's tree norm gives exactly

`||K_e|| = 2 sqrt(2r-1) = 2 sqrt(q)`.           (5.1)

The adjacency contribution of `B` is a sum of three unitary right translations, so

`||A_B|| <= 3`.                                  (5.2)

Hence for the full adjacency operator `A`,

`||A|| <= 3 + sum_{e in E} ||K_e||
       <= 3 + 2M sqrt(q) =: a`.                  (5.3)

This is the key weakening: relations between different exponent layers are harmless for the norm upper bound. Freeness is used separately inside each layer, not for their union.

The graph degree is

`D=3+2Mr=3+M(q+1)`,

so

`Q=D-1=Mq+M+2`.                                  (5.4)

## 6. Complete nonbacktracking transfer

For an infinite `D`-regular graph let `N_n(x,y)` be the number of nonbacktracking walks of length `n` from `x` to `y`, and let `N_n` denote the corresponding operator. We have

`N_0=I`, `N_1=A`, `N_2=A^2-DI`,

and for `n>=3`,

`N_n=A N_{n-1}-Q N_{n-2}`.                       (6.1)

By the spectral theorem, if `||A||<=a`, then the exponential growth rate of `||N_n||` is at most

`beta_D(a)=sqrt(Q)` for `a<=2sqrt(Q)`, and otherwise

`beta_D(a)=(a+sqrt(a^2-4Q))/2`.                  (6.2)

Indeed, for each spectral parameter `lambda in [-a,a]`, the recurrence has characteristic equation

`z^2-lambda z+Q=0`;

the largest modulus is maximized at `|lambda|=a`. At the double-root boundary a polynomial factor in `n` can occur, which does not change the convergence radius.

Every open connection contains a shortest open path, and that path is nonbacktracking. Therefore the two-point kernel satisfies entrywise

`T_p(x,y) <= sum_{n>=0} p^n N_n(x,y)`.           (6.3)

Consequently `T_p` is a bounded `ell^2` operator whenever

`p beta_D(a)<1`,

so

`p_{2->2}(G) >= beta_D(a)^(-1)`.                 (6.4)

Finally, if `p>p_u`, uniqueness of the infinite cluster and FKG give

`T_p(x,y) >= P_p(x<->infinity, y<->infinity) >= theta(p)^2`

for every `x,y`. A kernel bounded below by a positive constant is not bounded on `ell^2` of an infinite graph. Hence

`p_{2->2}(G) <= p_u(G)`.                         (6.5)

Combining (4.1), (5.3), (6.4), and (6.5), it is enough to prove

`beta_D(3+2M sqrt(q)) < q`.                      (6.6)

## 7. A general nonfree exponent-set theorem

For `z>sqrt(Q)`, the function

`h(z)=z+Q/z`

is strictly increasing, and `beta_D(a)` is the unique `z>=sqrt(Q)` satisfying `h(z)=a` in the nontrivial branch. Thus (6.6) follows if

`q>sqrt(Q)` and `q+Q/q>a`.                       (7.1)

Assume `M>=2` and

`q >= (2M+1)^2`.                                 (7.2)

First, at `q_0=(2M+1)^2`,

`q_0^2-(M q_0+M+2)
 =16M^4+28M^3+20M^2+6M-1 >0`,

and the left side is increasing in `q` for `q>=q_0`; hence `q^2>Q`.

Second, using (5.3),

`q+Q/q-a
 >= q+M+(M+2)/q -3 -2M sqrt(q)
 >  q+M-3-2M sqrt(q)`.

Put `y=sqrt(q)`. By (7.2), `y>=2M+1`, and

`y^2-2My+M-3`

is increasing for `y>=2M+1`. At the endpoint it equals

`(2M+1)^2-2M(2M+1)+M-3 = 3M-2 >0`.

Thus (7.1) holds and therefore

`boxed(p_c(G) <= 1/q < beta_D(3+2M sqrt(q))^(-1) <= p_u(G))`.   (7.3)

This gives an explicit positive gap

`boxed(Delta(M,r) = beta_D(3+2M sqrt(2r-1))^(-1) - (2r-1)^(-1) >0)`

throughout the range (7.2).

The exponents themselves do not matter: only their number `M` appears. Thus the theorem permits any finite prescribed exponent pattern, not just consecutive powers.

## 8. Sharpening the first genuinely nonfree case: two power layers

Take `M=2`. Then

`D=2q+5`, `Q=2q+4`, `a=3+4sqrt(q)`.

For `q>=19`,

`q+Q/q-a
 = q-1+4/q-4sqrt(q)`.

At `q=19`, use the exact rational upper bound

`sqrt(19) < 109/25`, since `(109/25)^2-19=6/625`.

Then

`q-1+4/q-4sqrt(q)
 > 18+4/19-436/25
 = 366/475 >0`.                                  (8.1)

The derivative of the right-hand function is

`1-4/q^2-2/sqrt(q)`.

For `q>=19`, `sqrt(q)>4`, so

`1-4/q^2-2/sqrt(q)
 > 1/2-4/19^2
 =353/722>0`.                                    (8.2)

Also `q^2>2q+4`. Thus (7.1) holds for every odd `q>=19`, proving the full `M=2, r>=10` statement.

### Exact endpoint `r=10`

Here

`q=19`, `D=43`, `Q=42`.

Use again `sqrt(19)<109/25`, so

`a=3+4sqrt(19)<511/25`.

Take

`z=363/20`.

Then `z^2>42`, and the exact root-test margin is

`z+42/z-511/25 = 291/12100 >0`.

Hence `beta_D(a)<363/20`, and therefore

`p_u >= p_{2->2} > 20/363`.

Together with `p_c<=1/19`,

`boxed(p_u-p_c > 20/363-1/19 = 17/6897)`.

The checker archived in this run verifies every rational identity above and ends `ALL_EXACT_CHECKS_PASS`.

## 9. Concrete uncovered higher-rank application

The completed `(2,3)`-generation classification states that `SL_n(Z)` is `(2,3)`-generated exactly for `n>=5`. Thus for every `n>=5` there is an involution `s` and an order-three element `t` generating the group; the symmetric set

`B={s,t,t^{-1}}`

has cardinality three.

The group also contains a standard embedded `F_2` (for example inside a suitable rank-two unipotent block after passing to the standard Sanov-type pair), so Section 3 supplies the required arbitrarily large Schreier free family while avoiding the finite set `B`.

Therefore for every `n>=5` and every choice of two distinct positive exponents `e<f`, there are degree-43 Cayley graphs

`Cay(SL_n(Z), {s,t,t^{-1}} union {c_i^{+-e},c_i^{+-f}:1<=i<=10})`

with

`boxed(p_u-p_c > 17/6897)`.

These graphs contain explicit power-relation cycles in every `i`-coordinate and are not free-core Cayley trees with a small complement.

This application lies outside the three owner-specified covered scopes. `SL_n(Z)`, `n>=5`, is a higher-rank lattice: it contains `Z^2`, so it is not Gromov-hyperbolic, and higher-rank lattice rigidity says its hyperbolic actions are elementary when there is no rank-one factor, so it is not acylindrically hyperbolic. Thus Hutchcroft's hyperbolic theorem and the later Choi--Seo all-Cayley acylindrically-hyperbolic theorem do not already settle these graphs.

## 10. Current literature scope refresh — 20 September 2026

This was a bounded current check, not a worldwide priority certificate.

- **arXiv:1804.10191 (Hutchcroft), current v3, 26 March 2019.** Theorem 1.3 proves `p_c<p_u` for connected, locally finite, nonamenable, Gromov-hyperbolic, quasi-transitive graphs. The arXiv history says v3 changed metadata only, not the text. This does not cover higher-rank `SL_n(Z)` Cayley graphs.
- **arXiv:2409.12283 (Hutchcroft--Pan), current v1, 18 September 2024.** It studies the state *at `p_u`*: in particular nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth, plus a co-heredity theorem for a strong endpoint nonuniqueness property. It does not state the quantitative fixed-Cayley `p_c<p_u` theorem above.
- **arXiv:2502.02560 (Terlov--Timar), current v2, 14 September 2025.** It characterizes weighted/level amenability and proves a relaxed Pak--Smirnova-Nagnibeda-style version of a weighted `p_h<p_u` conjecture. It is not the ordinary unimodular fixed-Cayley `p_c<p_u` result used here.
- **arXiv:2508.08932 (Choi--Seo).** It proves a nonuniqueness phase on every Cayley graph of every acylindrically hyperbolic group. Higher-rank `SL_n(Z)` is outside that group class by hyperbolic-action rigidity.
- Pak--Smirnova-Nagnibeda (2000) proves that every finitely generated nonamenable group has *some* finite generating set with a nonempty nonuniqueness phase. This remains important prior art and is why I do not claim a new group-level existence theorem.

A bounded search for combinations of `generator powers`, `Cayley graph`, `p_c`, `p_u`, free-subgroup augmentation, and the Pak--Smirnova-Nagnibeda criterion did not locate the precise power-thickening theorem above. That is negative search evidence only; external novelty remains UNVERIFIED.

## 11. Exact computation and sanity checks

Actual checker source:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T10-50-00+0300__t09-power-thickening-check.py`

created at commit

`fa7b15570116def79df24f5438a7ba5951b2f76a`.

Actually executed output was archived as

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T10-50-00+0300__t09-power-thickening-check.out`

at commit

`2621fcf1d9a49ab6ebacae2bfe8e208fc0514547`.

The output verifies:

- `q=19, D=43, Q=42`;
- `(109/25)^2-19=6/625>0`;
- adjacency upper bound `511/25`;
- root-test margin `291/12100>0` at `z=363/20`;
- `p_c<=1/19` and `p_u>20/363`;
- gap `17/6897>0`;
- the monotonic `M=2,r>=10` margin and derivative bounds;
- the symbolic sufficient-threshold identities for `M=2,...,100` as a self-check of the general algebra.

The general theorem itself is proved algebraically in Sections 6--8; the finite loop over `M<=100` is only a consistency check and is not the proof of the all-`M` assertion.

## 12. Failure / residual obstruction and next attack

The extra hypothesis is weaker but still engineered: the graph is built from a small ambient generating set plus many powers of a deliberately chosen Schreier free family. Unknown is not zero: this does **not** show that an arbitrary natural generating set of `SL_n(Z)` contains enough low-norm, low-`p_c` structure.

A tempting stronger claim, that an arbitrary set of dependent added generators can be charged by `O(sqrt{|C|})`, is false without additional structure; the triangle bound can be linear and no universal cancellation was proved. I therefore did not promote a colored-operator statement without hypotheses.

The next materially useful route is to replace the power layers by a **nonfree subgroup/block already present in a natural presentation** and compute both its `p_c` witness and its regular-representation norm. A second promising route is a matrix/colored nonbacktracking estimate that uses relations in a fixed generating set instead of first extracting an auxiliary Schreier basis. Either route would weaken the construction hypothesis rather than merely increase `r` or `M`.

## 13. ledger_delta

```yaml
ledger_delta:
  worker: NM13-11
  parent: T09
  status: PARTIAL
  candidate_status: CANDIDATE_FULL_RESTRICTED_PENDING_REVIEW
  universal_target_before: OPEN
  universal_target_after: OPEN
  source_scope_before: free-marked-set subgroup/nonbacktracking families, including free-core SL_n(Z) and full explicit Rattaggi free-augmentation tail
  source_scope_after: nonfree power-thickened free-core generating sets; arbitrary finite exponent patterns under an explicit rank condition
  concrete_group_family: SL_n(Z), n>=5
  concrete_graph_degree: 43
  concrete_parameters:
    exponent_layers: 2
    free_rank: 10
    q: 19
  pc_bound_after: "<= 1/19"
  pu_bound_after: "> 20/363"
  certified_gap_after: "> 17/6897 = 0.002464839785413948..."
  general_range_1: "M=2, r>=10"
  general_range_2: "M>=2 and 2r-1 >= (2M+1)^2"
  mechanism_advance: separate one-layer free-tree pc witness from layerwise ell2 norm charging; union of power layers may have relations
  prior_attempts_preserved: finite-set escape; BK/last-exit; killed-SAW; boundary energy; global ell2-SAW; scalar NB/product; quotient/fibre-shell; bridge; earlier SL/free-core/triangle/S-arithmetic/Rattaggi transfers
  unchanged_substantive_runs: 0
  failed_recoveries: 0
  checker_commit: fa7b15570116def79df24f5438a7ba5951b2f76a
  output_commit: 2621fcf1d9a49ab6ebacae2bfe8e208fc0514547
  independent_review: NOT_YET_DONE
  next_attack: natural nonfree subgroup block or relation-aware colored nonbacktracking transfer
```
