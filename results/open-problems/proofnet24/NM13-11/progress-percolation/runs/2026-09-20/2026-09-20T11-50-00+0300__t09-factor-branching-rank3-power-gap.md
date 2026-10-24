Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — free-product factor branching lowers the nonfree power rank from 10 to 3

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorems below; universal T09 remains OPEN.** The arguments below are complete as written and the finite core has an exhaustive exact-arithmetic self-check, but there has been no independent review. External priority of these exact fixed generating-set families remains **UNVERIFIED** after the bounded current search recorded below.

## 1. Frozen source problem and source-level before/after

The source problem is unchanged:

> For iid bond percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

The universal statement remains **OPEN**.

### Before this run

The immediately preceding NM13-11 theorem treated nonfree power-thickened free cores. With a symmetric 3-element ambient generating set `B`, two distinct exponent layers, and free rank `r>=10`, it proved a strict gap. The explicit endpoint had

`r=10`, degree `43`, `p_c<=1/19`, `p_u>20/363`, and `p_u-p_c>17/6897`.

Its `p_c` proof deliberately used only **one** exponent layer, so it discarded the percolative gain from the second, algebraically dependent layer. That was the main quantitative waste.

### After this run

I replace the one-layer witness by a free-product **factor-cluster branching process** that is still exact despite the power relations.

1. **Arbitrary two distinct exponent layers now work already at free rank `r=4`.** For any distinct positive integers `e<f`, the degree-19 Cayley graph constructed below satisfies

`boxed(p_c < 81/1000 < 41/500 < p_u)`

and hence

`boxed(p_u-p_c > 1/1000)`.

For every `r>=5`, the same arbitrary-pair construction also has `p_c<p_u`; there a simple alternating-factor tree already suffices on the critical side.

2. **The doubled pair works at free rank `r=3`.** For exponent layers `{m,2m}` with any `m>=1`, the resulting degree-15 Cayley graph satisfies

`boxed(p_c < 47/500 < 941/10000 < p_u)`

and therefore

`boxed(p_u-p_c > 1/10000)`.

Thus the concrete `SL_n(Z)`, `n>=5`, application drops from degree 43 / free rank 10 to degree 19 for an arbitrary exponent pair, and to degree 15 for a doubled pair.

**Original-problem delta:** universal T09 is still OPEN. The proved restricted scope expands from two-layer power thickenings requiring `r>=10` to every two-layer pair at `r>=4`, plus the doubled pair already at `r=3`, with explicit positive gaps and direct transfer to `p_c,p_u`.

**Mechanism delta:** instead of throwing away all but one power layer for `p_c`, I use the free-product normal form to turn finite percolation clusters inside cyclic factor-cosets into a genuine multitype Galton--Watson process. This is what crosses the `r=4` and `r=3` boundaries.

## 2. Compact continuity handoff and recovered Benjamini--Schramm attempts

The controlling policy is `operations/PROGRESS20_2026-09-20.md`; LIVE20 assigns NM11 to T09 at `proofnet24/NM13-11/progress-percolation/`. `POSTED.md` was checked for exclusions; no posted claim is being reopened here.

The June Benjamini--Schramm archive remains preserved under

`probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/`.

The relevant historical attempts include the finite-set escape plus BK/last-exit decomposition, killed-SAW and susceptibility-weighted boundary energy, global `ell^2` SAW growth, scalar nonbacktracking/product stress tests, quotient/fibre-shell comparisons, and fixed-endpoint bridge criteria. The recovered PROB10-09 handoff identifies rounds 011, 018, 040, 042, 053, 054, and 055 as the main nonbacktracking / fibre-branching / fixed-endpoint attempts. Several of these produced only auxiliary inequalities because the required percolation transfer remained incomplete; they are not relabelled as source progress.

The September continuation then produced actual subgroup/nonbacktracking transfers on explicit `SL_3(Z)`, low-rank free-core, triangle-fibre, S-arithmetic, and Rattaggi families. The immediate predecessor was the nonfree power-thickening theorem just summarized. This run continues that exact target and changes the `p_c` mechanism rather than adding more generators.

No unchanged-run recovery is triggered: the theorem scope moves substantially in this invocation.

## 3. Algebraic setup: power pairs inside a free subgroup

Let `Gamma` be a finitely generated group with a symmetric generating set `B` of cardinality three, and suppose `Gamma` contains an embedded free subgroup `F_2`. As in the preceding report, inside `F_2=<u,v>` the kernel of

`phi:F_2 -> Z`, `phi(u)=1`, `phi(v)=0`

has Schreier free basis

`C_infty={u^j v u^{-j}: j in Z}`.

Because `B` is finite, and because distinct free-basis elements have distinct nonzero powers up to the obvious same-generator equality, for any fixed finite exponent set we may choose as many basis elements `c_1,...,c_r` as needed so that every new power label is nontrivial, pairwise distinct, and disjoint from `B`.

Fix two distinct positive exponents `e<f` and put `d=gcd(e,f)`, `a=e/d`, `b=f/d`. Then

`H=<c_1^d,...,c_r^d> ~= F_r = Z_1 * ... * Z_r`,

where `Z_i=<c_i^d> ~= Z`. In the `i`th cyclic factor, the labels `c_i^{+-e},c_i^{+-f}` are exactly the steps `+-a,+-b` after identifying `Z_i` with `Z`.

The full generating set is

`S = B union {c_i^{+-e},c_i^{+-f}:1<=i<=r}`,

so the ambient graph is simple and has degree

`D=3+4r`.

For the doubled pair `{m,2m}`, after replacing `c_i` by `c_i^m` the factor step set is exactly `{+-1,+-2}`.

## 4. The factor-cluster branching lemma

This is the new critical-side mechanism.

Consider iid bond percolation at parameter `p` on the subgraph of `Cay(Gamma,S)` generated by the power-pair edges. The free-product normal form lets us explore factor-cosets without collisions.

A particle of type `i` is a reduced-word prefix whose last used factor is `Z_i`. For every `j != i`, expose a prescribed finite set of edges in the translated factor-coset `x Z_j` around the seed `x`. Every non-seed vertex connected to `x` by the exposed edges becomes a child of type `j`.

Two facts make this an honest multitype Galton--Watson process.

1. Distinct translated factor-cosets encountered by reduced prefixes have disjoint edge sets, except for their seed vertices. Indeed, if two relevant `Z_j`-cosets coincided, free-product normal form would force the corresponding prefixes to differ by a `Z_j` syllable, which is exactly the forbidden immediate same-factor continuation.
2. Offspring vectors attached to different particles are therefore independent and identically distributed by translation invariance. Dependencies among siblings inside one finite factor window are harmless.

If `mu(p)` denotes the expected number of non-seed vertices produced by one chosen `Z_j` factor window, the mean matrix has zero diagonal and every off-diagonal entry equal to `mu(p)`. Its Perron eigenvalue is

`(r-1) mu(p)`.

Therefore

`(r-1) mu(p)>1  ==>  p_c(Cay(Gamma,S)) < p`

whenever `mu` is obtained from a finite window and the inequality is strict: the offspring mean is then a polynomial in `p`, so it remains supercritical at some `p'<p`.

This is a direct infinite-cluster transfer, not merely a finite-event estimate.

## 5. Rank 4 with an arbitrary exponent pair

Take `r=4`. In one cyclic factor with step set `{+-a,+-b}`, expose only the following six possible nonzero children:

`+-a`, `+-b`, and `+-(a+b)`.

The first four are connected to the seed when their single corresponding edge is open. The vertex `a+b` is connected whenever the two-edge path

`0 -> a -> a+b`

is open, and similarly on the negative side. The six target vertices are distinct because `a,b` are distinct positive integers. Hence

`mu(p) >= 4p+2p^2`.

At

`p_4=81/1000`,

exact arithmetic gives

`mu(p_4) >= 168561/500000`,

and therefore

`3 mu(p_4)-1 >= 5683/500000 >0`.

The factor-branching lemma yields

`p_c < 81/1000`.                                      (5.1)

### Operator / uniqueness side

Write `q=2r-1=7`. For each exponent layer separately, the corresponding adjacency operator is a direct sum over free-subgroup cosets of the 8-regular tree adjacency, so its `ell^2` norm is exactly

`2 sqrt(7)`.

There are two layers, while the three ambient generators contribute norm at most 3. Thus

`||A|| <= 3+4 sqrt(7)`.

The graph has `D=19`, so `Q=D-1=18`. Let

`beta_D(A0)`

be the largest characteristic-root modulus for

`z^2-lambda z+Q=0`, `|lambda|<=A0`.

Equivalently, above `sqrt(Q)`, `beta` is controlled by the increasing function

`h(z)=z+Q/z`.

Use

`sqrt(7) < 127/48`, because `(127/48)^2-7=1/2304`,

and take

`z_4=500/41`.

Then `z_4^2>18` and

`z_4+18/z_4 - (3+4*(127/48)) = 5399/61500 >0`.

Hence

`beta_D(||A||) < 500/41`.

The standard nonbacktracking transfer, reproduced in Section 7 below, gives

`p_u >= p_{2->2} > 41/500`.                            (5.2)

Combining (5.1) and (5.2),

`boxed(p_u-p_c > 41/500-81/1000 = 1/1000)`.

This proves the arbitrary-pair theorem already at rank four.

## 6. Rank 3 for the doubled pair: exact finite-window cluster computation

Now take `r=3` and exponent layers `{m,2m}`. In every cyclic factor, after scaling by `m`, the local graph is

`L = Cay(Z,{+-1,+-2})`.

A one- or two-step hand estimate is too weak at rank three, so I used an exact finite window rather than assuming the full one-dimensional susceptibility.

Let `L_5` be the induced graph on vertices

`{-5,-4,...,4,5}`

with all edges of length 1 or 2. It has 19 edges. For `0<=k<=19`, define `A_k` to be the sum, over every `k`-edge subset of `L_5`, of the number of nonzero vertices in the open component of 0.

The exhaustive `2^19` enumeration gives

`A = [0,4,84,838,5258,23130,75278,186662,358566,538580,635614,590636,432292,248424,111100,37992,9626,1708,190,10]`.

Therefore the expected number of non-seed children produced by this finite window is exactly

`mu_5(p)=sum_{k=0}^{19} A_k p^k (1-p)^(19-k)`.

At

`p_3=47/500`,

the executed exact checker obtains

`mu_5(p_3)
 =119351131833746153494153941230463512463778953339751
  /238418579101562500000000000000000000000000000000000`

`=0.500594929654808...`,

so

`2 mu_5(p_3)-1
 =141842282964903494153941230463512463778953339751
  /119209289550781250000000000000000000000000000000000
 >0`.

For three free factors the mean matrix has Perron eigenvalue `2 mu_5`, hence the finite-window process is supercritical. Strict continuity gives

`p_c < 47/500`.                                      (6.1)

This calculation is deliberately finite: no simulation and no unproved formula for the full susceptibility of `Cay(Z,{+-1,+-2})` is used.

### Operator / uniqueness side

Here `q=2r-1=5`, degree `D=15`, and `Q=14`. As before,

`||A|| <= 3+4 sqrt(5)`.

Use

`sqrt(5) < 223607/100000`,

with square margin

`(223607/100000)^2-5 = 90449/10^10 >0`.

Take

`z_3=10000/941`.

Then `z_3^2>14` and the exact root-test margin is

`z_3+14/z_3 - (3+4*(223607/100000))
 =331/2940625 >0`.

Thus the nonbacktracking growth exponent is `<10000/941`, and

`p_u >= p_{2->2} > 941/10000`.                       (6.2)

From (6.1)--(6.2),

`boxed(p_u-p_c > 941/10000-47/500 = 1/10000)`.

This is the first rank-three / degree-15 dependent-power theorem on this track.

## 7. Complete nonbacktracking-to-percolation transfer

For completeness, let `G` be an infinite `D`-regular graph, `A` its adjacency operator, and `N_n(x,y)` the number of nonbacktracking walks of length `n` from `x` to `y`. The walk operators satisfy

`N_0=I`, `N_1=A`, `N_2=A^2-DI`,

and for `n>=3`,

`N_n=A N_{n-1}-(D-1)N_{n-2}`.

If `||A||<=A0`, the spectral theorem reduces the exponential growth of `||N_n||` to the roots of

`z^2-lambda z+(D-1)=0`, `|lambda|<=A0`.

Let `beta` be the maximum root modulus. Every open connection contains a shortest open path, which is nonbacktracking, so entrywise

`T_p(x,y) <= sum_{n>=0} p^n N_n(x,y)`.

Hence `T_p` is bounded on `ell^2` whenever `p beta<1`, giving

`p_{2->2} >= 1/beta`.

Finally, for `p>p_u`, uniqueness of the infinite cluster and FKG imply

`T_p(x,y) >= theta(p)^2`

for every pair `x,y`; a kernel bounded below by a positive constant cannot define a bounded operator on `ell^2` of an infinite graph. Therefore

`p_{2->2} <= p_u`.

This proves the transfer used in Sections 5 and 6.

## 8. Arbitrary exponent pairs for every rank r>=5

There is also a clean all-rank continuation which shows that the rank-four endpoint is not isolated.

For any two distinct exponent layers and any `r>=5`, form the rooted subgraph consisting only of reduced words that switch cyclic factor at every edge. From a nonroot word there are exactly

`4(r-1)`

allowed forward choices (`+-e` or `+-f` in any factor different from the current last factor), and free-product normal form makes this subgraph a tree. Therefore

`p_c <= 1/[4(r-1)]`.

Put `q=2r-1>=9`. Then the reciprocal of this tree threshold is

`z=4(r-1)=2(q-1)`.

As above,

`Q=2q+4`, `||A||<=3+4sqrt(q)`.

The exact root-test margin at this `z` is

`F(q)=2q-4+3/(q-1)-4sqrt(q)`.

At `q=9`,

`F(9)=19/8>0`,

and for every `q>=9`,

`F'(q)=2-3/(q-1)^2-2/sqrt(q)
      >=2-3/64-2/3
      =247/192>0`.

Thus `F(q)>0` for all `q>=9`, so `beta<2(q-1)` and

`1/beta > 1/[2(q-1)] = 1/[4(r-1)] >= p_c`.

Consequently every arbitrary two-exponent construction with `r>=5` also satisfies `p_c<p_u`.

Together with Section 5:

`boxed(any two distinct exponent layers work for every r>=4)`.

The doubled-pair finite-window argument of Section 6 lowers the endpoint one step further to `r=3`.

## 9. Concrete higher-rank application

For every `n>=5`, `SL_n(Z)` is generated by an involution and an element of order 3, hence has a symmetric generating set

`B={s,t,t^{-1}}`

of cardinality three. This completed `(2,3)`-generation fact is recorded in the current literature; a 2025 survey/record on generating pairs states that `SL(n,Z)` is `(2,3)`-generated precisely for `n>=5`.

`SL_n(Z)` also contains an embedded `F_2`. Using the infinite Schreier basis above, choose the needed free elements avoiding `B` and its finitely many forbidden power collisions.

Therefore, for every `n>=5`:

- every pair of distinct positive exponents yields explicit **degree-19** Cayley graphs with `p_u-p_c>1/1000` using `r=4`;
- every doubled pair `{m,2m}` yields explicit **degree-15** Cayley graphs with `p_u-p_c>1/10000` using `r=3`.

These are new fixed generating sets relative to the previous track scope; they contain systematic algebraic power relations and short cycles. I do **not** claim a new group-level existence theorem, since Pak--Smirnova-Nagnibeda already proved that every finitely generated nonamenable group has some Cayley graph with a nonuniqueness phase.

The concrete higher-rank lattices are not Gromov-hyperbolic and are not acylindrically hyperbolic, so Hutchcroft's hyperbolic theorem and Choi--Seo's all-Cayley acylindrically-hyperbolic theorem do not subsume these fixed graphs. The 2026 Mukherjee--Recke property-(T) result proves that Bernoulli percolation at `p_u` does not have a unique infinite cluster on property-(T) Cayley graphs, but it does not by itself imply the strict quantitative separation `p_c<p_u` proved here.

## 10. Current source scopes checked 20 September 2026

This is a bounded present-status check, not a worldwide novelty certificate.

- **Hutchcroft, arXiv:1804.10191, current v3, 26 March 2019.** The arXiv history says v3 changed metadata only, with no text change. Theorem 1.3 proves `p_c<p_u` for connected, locally finite, nonamenable, **Gromov-hyperbolic quasi-transitive** graphs. URL: `https://arxiv.org/abs/1804.10191`.
- **Hutchcroft--Pan, arXiv:2409.12283, current v1, 18 September 2024.** It studies the state **at `p_u`**, proving nonuniqueness there for groups with an amenable `wq`-normal subgroup of exponential growth and proving a co-heredity theorem for a stronger endpoint property via subgroup relativization. It does not state a general fixed-Cayley quantitative `p_c<p_u` theorem. URL: `https://arxiv.org/abs/2409.12283`.
- **Terlov--Timar, arXiv:2502.02560, current v2, 14 September 2025.** It characterizes weighted/level amenability and proves a relaxed Pak--Smirnova-Nagnibeda-style form of a weighted `p_h<p_u` conjecture. It is not the ordinary unimodular fixed-Cayley `p_c<p_u` statement. URL: `https://arxiv.org/abs/2502.02560`.
- **Choi--Seo, arXiv:2508.08932.** They prove a nonuniqueness phase on every Cayley graph of every acylindrically hyperbolic group. Higher-rank `SL_n(Z)` is outside that class.
- **Mukherjee--Recke, PTRF 2026, `Haagerup property and group-invariant percolation`.** Their Theorem 4.4 gives nonuniqueness at `p_u` for property-(T) and relative-property-(T) settings. This endpoint theorem does not supply the strict positive gap above.

A bounded search for combinations of Cayley percolation with generator powers / power-thickening and `SL_n(Z)` did not locate the rank-three or rank-four factor-branching theorem here. This is negative search evidence only; external novelty remains UNVERIFIED.

## 11. Exact computation and archived output

Actual checker source:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T11-50-00+0300__t09-power-pair-factor-branch-check.py`

created at commit

`9373da24611a0572befddb7374cff7bfecf45246`.

The checker was executed locally in this invocation. Its actual stdout was archived as

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T11-50-00+0300__t09-power-pair-factor-branch-check.out`

at commit

`988e7f981c46a59a5818e56d25163bd6136e76fa`.

It verifies exactly:

- all `2^19` configurations of the rank-three `{+-1,+-2}` finite window and the integer coefficient vector `A_k`;
- `mu_5(47/500)>1/2` with the exact rational margin displayed above;
- the degree-15 root-test margin `331/2940625` and gap `>1/10000`;
- the rank-four arbitrary-pair branching margin `5683/500000`;
- the degree-19 root-test margin `5399/61500` and gap `>1/1000`;
- the `r>=5` endpoint margin `F(9)=19/8` and derivative lower bound `247/192`.

The output ends `ALL_EXACT_CHECKS_PASS`.

## 12. Residual obstruction and next attack

This is a genuine weakening, but the generating sets are still engineered from a free subgroup. Unknown is not zero: the argument does **not** yet prove a gap for the standard elementary-matrix Cayley graph of a higher-rank lattice, nor for an arbitrary fixed Cayley graph of such a group.

The factor-branching mechanism suggests a more natural next step. Replace the cyclic factors by a **nonfree subgroup block already present in a natural presentation**, compute a finite-window cluster reproduction number for that block, and combine it with its actual regular-representation adjacency norm. This would remove the auxiliary Schreier-basis construction rather than merely improve another constant.

A second route is relation-aware colored nonbacktracking control for the natural generator types. The scalar triangle inequality remains the main loss on the `p_u` side. Either route is materially different from further increasing the power rank.

## 13. ledger_delta

```yaml
ledger_delta:
  worker: NM13-11
  parent: T09
  status: PARTIAL
  candidate_status: CANDIDATE_FULL_RESTRICTED_PENDING_REVIEW
  universal_target_before: OPEN
  universal_target_after: OPEN
  source_scope_before: "two-layer nonfree power-thickening certified for r>=10; concrete SL_n(Z), n>=5, degree 43"
  source_scope_after: "arbitrary two distinct exponent layers certified for every r>=4; doubled pair {m,2m} additionally certified at r=3"
  concrete_group_family: "SL_n(Z), n>=5"
  arbitrary_pair_endpoint:
    free_rank: 4
    degree: 19
    pc_bound: "< 81/1000"
    pu_bound: "> 41/500"
    certified_gap: "> 1/1000"
  doubled_pair_endpoint:
    free_rank: 3
    degree: 15
    pc_bound: "< 47/500"
    pu_bound: "> 941/10000"
    certified_gap: "> 1/10000"
  general_arbitrary_pair_range: "r>=4"
  mechanism_advance: "free-product factor-coset Galton-Watson exploration uses dependent power layers on the pc side; exact radius-5 finite window crosses r=3 for the doubled pair"
  prior_attempts_preserved: "finite-set escape; BK/last-exit; killed-SAW; susceptibility boundary energy; global ell2-SAW; scalar NB/product; quotient/fibre-shell; fixed-endpoint bridge; earlier subgroup/free-core/triangle/S-arithmetic/Rattaggi/power-thickening transfers"
  unchanged_substantive_runs: 0
  failed_recoveries: 0
  checker_commit: 9373da24611a0572befddb7374cff7bfecf45246
  output_commit: 988e7f981c46a59a5818e56d25163bd6136e76fa
  independent_review: NOT_YET_DONE
  next_attack: "natural nonfree subgroup block with finite-window reproduction plus operator norm, or relation-aware colored nonbacktracking on a natural higher-rank generating set"
```
