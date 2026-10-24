Runtime model: **GPT-5.6 Sol**. Requested GPT-6 maximum is not an authenticated/selectable runtime control exposed here. Reasoning effort: **UNVERIFIED**.

# PROB10-09 — vertical-subgroup spectral budget for extension Cayley graphs

Status: **PARTIAL / new restricted structural theorem proved in this run; the universal Benjamini–Schramm Cayley-graph conjecture remains OPEN.** The finite arithmetic core was executed exactly and archived, but there is **no independent validator / source-closure audit** for the new theorem yet.

## 0. Frozen parent target

The target remains exactly the owner-specified one:

> For every locally finite Cayley graph `G` of every finitely generated nonamenable group, iid **bond** percolation satisfies `p_c(G)<p_u(G)`.

No planar nontransitive site-percolation problem is substituted. Known hyperbolic and acylindrically-hyperbolic all-Cayley results are prior art, not fleet progress.

## 1. Continuity first: R20 handoff, aliases, ownership, consumed history

Before doing new mathematics I re-read the owner directive `operations/PROB10_2026-09-20.md`, current `POSTED.md`, the R20 owner-refocus handoff

`runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`

(blob `6e1b9e54cbc01461d32b523854c3bd82e50bfd04`), and current source/neighbor records.

The handoff preserves, without changing ownership or artifacts:

1. `I0100 / Paley one-localization`: `OPEN/PARTIAL`, frozen `p_max=1213`, canonical `operations/claims/I0100.md`, with all `artifacts/R20/i0100_*` retained.
2. `KNSV-2026-LOOPY-U`: `OPEN/PARTIAL`, source endpoint `N_sep>11`, with the `knsv_*` exact diagnostic artifacts retained.
3. `BMO-2025-PUSHING-DELTA`: the last actual R20 mathematical target before owner refocus, `OPEN/PARTIAL`, frozen `n_all=9`, preserving `bmo_n9_witness_exact.cpp`, `bmo_n9_exact_check.out`, and the six-run handoff.
4. The old terminal-wait report remains historical only; the owner refocus supersedes that wait state for R20 without rewriting the predecessor claims.

The canonical Benjamini–Schramm intake alias remains

`D0061 = lyons_nonamenable_2000::conjecture_3.8_(benjamini-schramm_1996)`.

Current claim search found no canonical closure file for `D0061`. `POSTED.md` is an exclusion/posting register and does not close this unrestricted source.

### June attempt archive actually recovered

I did not use only the status summary. The following archive files were re-read/consumed:

- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`, blob `ee8bde8735e84ff75d3a625fed61e9bafbefd64f`;
- `.../research/proof_strategy.md`, blob `d94127841f3b335a32b7936b86d8dee7a6b8d093`;
- `.../notes/round_011.md`, blob `e4b38be74ddddaa15b36aa564d31cf338f3fa4e9`: scalar nonbacktracking polynomial/operator bound;
- `.../notes/round_018.md`, blob `e171f9c1a80a24ca6cb8a67ce9fd563763029221`: vertical-fibre Galton–Watson comparison and the low-branching fixed-depth obstruction;
- `.../notes/round_040.md`, blob `e2de09e883e9082440e370e4cf67bd782f1e145f`: fixed-direction exponent / tree-sphere operator mechanism;
- `.../notes/round_042.md`, blob `82caa389484574736ab38f75df5f41687449ea2d`: correction that the tree-times-amenable and lamplighter product theorem is prior art, and the suggested quotient/backscattering directions;
- `.../notes/round_053.md`, blob `bdad4bb3aa58303dd35a7dab4c1e42d9d597245b`: fixed-endpoint nonbacktracking excess criterion;
- `.../notes/round_054.md`, blob `43d7d8aee783aba9fdf019d76669855483a9aea4`: fixed-endpoint detour generating function;
- `.../notes/round_055.md`, blob `8a06a66baca79d2fbb9dc934269e8a850b094fc1`: nonbacktracking bridge-probability criterion.

The older normalized finite-set escape, BK/last-exit decomposition, killed-SAW/boundary-energy, global `ell^2` SAW, product stress, quotient/fibre-shell, and bridge attempts remain failed/conditional history rather than being renamed as new.

### Neighboring ownership

The newest neighboring T09 report checked is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T17-25-00+0300__t09-two-seed-arbitrary-four-pairs-gap.md`.

That worker owns the Rattaggi / product-of-trees / free-layer / multiseed fibre-branching lane and has a restricted degree-28 four-arbitrary-pair theorem there. This iteration remains in R20's **quotient/extension/two-point-operator** lane and does not absorb or relabel that claim.

## 2. Idea-before-code and three different routes

Before running the checker I wrote

`artifacts/prob10_2026-09-20/PROB10-09/20260920T1458Z_vertical_subgroup_spectral_budget_idea_8f31.md`

at commit `1a21781e73ecd8bd79d1a76cdab08c5c5aa9c96d`.

It compared three materially different routes:

1. **Vertical spectral-budget refinement (primary)**: replace the predecessor's crude `||A_V||<=m` by the exact norm of the vertical Cayley adjacency. This succeeds.
2. **Old vertical-cardinality route (negation control)**: deliberately choose a graph outside the previous `m<M_g` surface-extension scope and verify that its old `+m` beta test fails. This fails exactly as intended and certifies that the example is genuinely new relative to the immediate R20 theorem.
3. **Quotient-Cheeger route without a free marked subset**: combine the quotient expansion bound with the same new uniqueness-side estimate. This remains valid but is quantitatively too weak on the frozen graph; the exact obstruction is recorded below.

The neighboring multiseed product-fibre method was not pursued because it belongs to NM13-11.

During the required prior-art/negation stress I replaced the first draft's exponentially growing Nielsen action by a finite-image nontrivial action, without changing any spectral calculation. That correction is preserved in

`artifacts/prob10_2026-09-20/PROB10-09/20260920T1511Z_vertical_subgroup_priorart_stress_addendum_8f31.md`.

## 3. New theorem: vertical cardinality can be replaced by vertical spectral norm

Let

`pi: Gamma -> Q`

be a surjective homomorphism with kernel `N`. Let `S_Q` be a finite symmetric generating set of `Q`, `D0=|S_Q|`, and choose one inverse-compatible lift in `Gamma` of every element of `S_Q`; call the lifted set `S_H`.

Let `V subset N` be finite symmetric, disjoint from `S_H`, with `m=|V|`, and assume

`S=S_H union V`

generates `Gamma` and gives a simple `D=D0+m` regular Cayley graph `X=Cay(Gamma,S)`. Put

`Y=Cay(Q,S_Q)`,
`r_Q=||A_Y||_{2->2}`,
`r_V=||A_{N,V}||_{2->2}`,

where `A_{N,V}` is the (possibly disconnected, if `V` does not generate all of `N`) right-adjacency operator determined by `V` on `ell^2(N)`.

For `D>=3`, define

`beta_D(a)=sqrt(D-1)` if `a<=2sqrt(D-1)`,

and

`beta_D(a)=(a+sqrt(a^2-4(D-1)))/2`

otherwise.

### Theorem 3.1 — vertical spectral-budget extension criterion

Assume the quotient marking contains `k` positive generators whose subgroup in `Q` is freely generated by those `k` elements. If

`beta_{D0+m}(r_Q+r_V) < 2k-1`,                                      (3.1)

then

`p_c(X) <= 1/(2k-1) < 1/beta_{D0+m}(r_Q+r_V) <= p_{2->2}(X) <= p_u(X)`. (3.2)

In particular `p_c(X)<p_u(X)`.

This strictly strengthens the preceding R20 theorem whenever `r_V<m`: the vertical set may be large provided its own Cayley adjacency has sufficiently small spectral norm.

### Proof

Write

`A_X=A_H+A_V`

for the horizontal and vertical parts of the full adjacency operator.

#### Horizontal part

For each quotient vertex `q`, identify the fibre `pi^{-1}(q)` with `ell^2(N)` after choosing a representative `x_q`. Right multiplication by a horizontal lift sends one quotient fibre bijectively to the neighboring quotient fibre. Under the fibre identifications it is therefore a unitary map on the Hilbert fibre `ell^2(N)`.

If `f` is regarded as an `ell^2(N)`-valued function on `Q`, set

`F(q)=||f(q)||_{ell^2(N)}`.

Pointwise triangle inequality gives

`||(A_H f)(q)|| <= sum_{s in S_Q} F(qs)=(A_Y F)(q)`.

Hence

`||A_H f||_2 <= ||A_Y F||_2 <= r_Q ||F||_2 = r_Q ||f||_2`,

so

`||A_H|| <= r_Q`.                                                     (3.3)

#### Vertical part — the new step

Right multiplication by any `v in V subset N` preserves every quotient fibre. On the fibre `pi^{-1}(q)=x_q N`, the identification

`n -> x_q n`

conjugates the vertical action exactly to right multiplication by `v` on `N`. Therefore `A_V` is an orthogonal direct sum, indexed by `Q`, of copies of `A_{N,V}`. Consequently

`boxed(||A_V||=r_V)`.                                                  (3.4)

This is the improvement over the previous bound `||A_V||<=m`.

By (3.3)-(3.4),

`||A_X|| <= r_Q+r_V`.                                                  (3.5)

#### Nonbacktracking two-point bound

For a `D`-regular graph let `N_n` denote the length-`n` nonbacktracking walk operator. Then

`N_0=I`, `N_1=A_X`, `N_2=A_X^2-DI`,
`N_n=A_X N_{n-1}-(D-1)N_{n-2}` for `n>=3`.

Spectral calculus for this recurrence and (3.5) gives

`limsup_n ||N_n||^{1/n} <= beta_D(r_Q+r_V)`.                           (3.6)

If `T_p(x,y)=P_p(x<->y)` is the bond-percolation two-point function, every open connection contains a shortest open path, every shortest path is nonbacktracking, and a union bound therefore gives entrywise

`T_p(x,y) <= sum_{n>=0} p^n N_n(x,y)`.                                (3.7)

Thus (3.6) implies boundedness of `T_p` on `ell^2` whenever

`p beta_D(r_Q+r_V)<1`,

and hence

`p_{2->2}(X) >= 1/beta_D(r_Q+r_V)`.                                   (3.8)

#### Critical-probability upper bound

Choose the `k` freely generating positive quotient generators. Their selected lifts in `Gamma` also freely generate `F_k`: a reduced relation among the lifts would project to the same reduced nontrivial relation in `Q`. Their marked edges therefore form a `2k`-regular tree subgraph. Monotonicity under adding edges gives

`p_c(X) <= p_c(T_{2k})=1/(2k-1)`.                                    (3.9)

Under (3.1), (3.8)-(3.9) give the strict middle inequality in (3.2).

Finally `p_{2->2}<=p_u`: if `p>p_u`, uniqueness of the infinite cluster and FKG imply

`T_p(x,y) >= P(x in C_infty, y in C_infty) >= theta(p)^2>0`

uniformly in `x,y`. A kernel bounded below by a positive constant cannot define a bounded operator on `ell^2` of an infinite graph. This completes the proof. `square`

## 4. Complete criterion for surface quotients with product-free vertical kernels

Let

`Q=Gamma_g=<a_1,b_1,...,a_g,b_g | product_i [a_i,b_i]=1>`, `g>=2`,

with its standard `4g`-direction generating set. By the Dehn--Magnus Freiheitssatz, any proper subset of the `2g` positive standard generators freely generates the subgroup it spans, so we may take

`k=2g-1`.                                                             (4.1)

Żuk's surface-walk estimate in the normalization used by the preceding R20 reports gives

`r_Q=||A_Q|| <= 4 sqrt(g)`.                                            (4.2)

Now take

`N=F_s x F_s`, `s>=2`,

with the standard product marking. It has

`m=4s`,
`r_V=4 sqrt(2s-1)`,                                                    (4.3)

because each `F_s` factor has Cayley graph `T_{2s}` and adjacency norm `2sqrt(2s-1)`, while the Cartesian-product adjacency is the sum of the two commuting factor adjacencies.

Theorem 3.1 therefore proves a strict gap for every such extension/lift satisfying

`beta_{4g+4s}(4sqrt(g)+4sqrt(2s-1)) < 4g-3`.                          (4.4)

This condition has an exact algebraic scope. Put

`B=4g-3`, `q=4g+4s-1`, `h=2s-1`.

If `B^2<=q`, then `beta>=sqrt(q)>=B` and (4.4) fails. If `B^2>q`, the elementary root identity gives

`beta_D(a)<B  iff  a < B+q/B`.

With `a=4(sqrt(g)+sqrt(h))`, this is

`sqrt(g)+sqrt(h) < C_{g,s}:=(4g^2-5g+s+2)/(4g-3)`.                    (4.5)

Hence, setting

`R_{g,s}=C_{g,s}^2-g-h`,

condition (4.4) is equivalent to the entirely rational test

`B^2>q`, `R_{g,s}>0`, and `R_{g,s}^2>4gh`.                            (4.6)

Thus (4.6) is the complete scope of this proved surface/product-kernel criterion, not merely a numerical sufficient sample.

## 5. Frozen new graph and exact quantitative gap

Take

`g=5`, `s=3`.

Let `N=F_3 x F_3` with free bases `(x_1,x_2,x_3)` and `(y_1,y_2,y_3)`. Let `sigma in Aut(N)` simultaneously swap `x_1<->x_2` and `y_1<->y_2`, fixing `x_3,y_3`. Define an action of `Gamma_5` on `N` by

`alpha(a_1)=sigma`,

and all `b_1,a_2,b_2,...,a_5,b_5` acting trivially. The surface relator maps to the identity because every image commutator is trivial, so

`Gamma=(F_3 x F_3) semidirect_alpha Gamma_5`

is well-defined. Use split lifts of all 20 surface directions together with the standard 12 vertical directions of `F_3 x F_3`. The Cayley graph `X` is 32-regular and the kernel is genuinely noncentral (`a_1 x_1 a_1^{-1}=x_2`).

For this graph,

`D=32`, `D-1=31`,
`r_Q<=4sqrt5`, `r_V=4sqrt5`,

so

`||A_X|| <= 8sqrt5`.

The nonbacktracking root is exact:

`beta_32(8sqrt5)
 = (8sqrt5 + sqrt(320-124))/2
 = 7+4sqrt5
 <17`.

The free marked quotient subset has rank `k=9`, hence

`p_c(X)<=1/17`,

while

`p_u(X)>=p_{2->2}(X)>=1/(7+4sqrt5)=(4sqrt5-7)/31`.

Therefore

`p_u(X)-p_c(X)
 >= (4sqrt5-7)/31 -1/17
 = (68sqrt5-150)/527
 = 0.0038949192978855775...`.

The exact checker certifies the cleaner rational lower bound

`boxed(p_u(X)-p_c(X)>1/260)`                                         (5.1)

because

`17680 sqrt5 >39527`

and

`17680^2*5-39527^2=528271>0`.

### This graph is outside the immediate predecessor's scope

The previous vertical-cardinality theorem for genus `g=5` required

`m<M_5=(77-17sqrt5)/4=9.746711...`.

Here `m=12`, and

`12>M_5 iff 17sqrt5>29`,

with exact square margin

`17^2*5-29^2=604>0`.

Equivalently, the old `+m` adjacency bound gives

`a_old=12+4sqrt5=20.94427...`,

whereas `beta_32(a_old)<17` would require

`a_old<17+31/17=320/17=18.823529...`.

Thus the old theorem provably does **not** certify this frozen graph.

## 6. Negation test of the third route

Using only the quotient spectral-to-edge-expansion estimate gives, at best for this stress test,

`phi_E(Q)>=20-4sqrt5`

and hence the crude percolation upper bound

`p_c(X)<=1/(21-4sqrt5)=0.0829481...`.

The new uniqueness floor is only

`1/(7+4sqrt5)=0.0627184...`.

So this Cheeger-only route cannot cross on the frozen graph. The failure is exact because

`1/(21-4sqrt5)>1/(7+4sqrt5)`

is equivalent to

`14<8sqrt5`,

and `64*5-14^2=124>0`.

This obstruction prevents relabeling the weaker route as progress.

## 7. Executed exact tests

The load-bearing checker and actual output are

- `artifacts/prob10_2026-09-20/PROB10-09/vertical_subgroup_spectral_budget_exact_8f31.py`;
- `artifacts/prob10_2026-09-20/PROB10-09/vertical_subgroup_spectral_budget_exact_8f31.out`.

The run ends

`ALL_EXACT_CHECKS_PASS`.

It verifies:

- exact frozen beta identity and strict `beta<17`;
- the `>1/260` gap via integer-square margin `528271`;
- exact failure of the preceding `m<M_5` theorem via square margin `604`;
- exact failure of the old `+m` beta test;
- exact failure of the quotient-Cheeger stress route;
- the rational criterion (4.6) on every `(g,s)` in `2<=g,s<=40`, with a separate 80-digit direct-beta consistency check and zero mismatches.

The finite scan has `1521` pairs, `1231` successes for the new criterion, and `651` pairs where the new criterion succeeds while the previous cardinality criterion fails. The first such pair is exactly the frozen `(g,s)=(5,3)`. These grid counts are auxiliary mechanism evidence; the algebraic theorem (4.6), not the scan, establishes the full stated scope.

## 8. Current prior-art screen and class separation

The source screen was refreshed rather than relying only on June metadata.

- Hutchcroft, `https://arxiv.org/abs/1804.10191`, proves `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs. That is known prior art.
- Hutchcroft--Pan, `https://arxiv.org/abs/2409.12283`, prove nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth and a co-heredity principle; this is a major proper subclass, not the universal theorem.
- Terlov--Timár, `https://arxiv.org/abs/2502.02560`, concerns weighted/level amenability and a relaxed weighted `p_h<p_u` statement, not the frozen ordinary Cayley bond target.
- Choi--Seo, `https://arxiv.org/abs/2508.08932`, prove a nonuniqueness phase on **every** Cayley graph of every acylindrically hyperbolic group.
- Pak--Smirnova-Nagnibeda and Juschenko--Nagnibeda (`https://arxiv.org/abs/1206.2183`) give important **existence of a favorable generating set** results for broad nonamenable groups / extensions. They do not assert the required fixed-marking theorem for every Cayley graph.
- A current September 10, 2026 source (`arXiv:2609.11845`, beta-skewed maximal spanning forests) still records the general Benjamini--Schramm nonamenability/nonuniqueness statement as a conjectural problem.

For the frozen group above:

1. it is not Gromov hyperbolic because it contains `Z^2`;
2. it is not acylindrically hyperbolic because the infinite normal subgroup `F_3 x F_3` is not acylindrically hyperbolic, while infinite normal (indeed s-normal) subgroups of an acylindrically hyperbolic group are acylindrically hyperbolic;
3. it has no amenable subgroup of exponential growth, so the explicit Hutchcroft--Pan sufficient class does not apply. To see this, an amenable subgroup projects to a cyclic subgroup of the torsion-free hyperbolic surface quotient. Its intersection with `F_3 x F_3` has cyclic coordinate projections and hence lies in `Z^2`. Passing to index at most two kills the finite-image action; normalizers of infinite cyclic subgroups in a free group are cyclic, so the resulting subgroup is virtually abelian of rank at most three.

This is a bounded class/prior-art screen, **not a proof of worldwide novelty**. I did not find a current theorem that already gives the fixed-marking quantitative statement (5.1), but external priority is `UNVERIFIED` pending independent literature review.

## 9. Metric ledger

```yaml
ledger_delta:
  worker: PROB10-09 / R20
  source: Benjamini-Schramm nonuniqueness-phase conjecture for iid bond percolation on Cayley graphs
  parent_status_before: OPEN/PARTIAL
  parent_status_after: OPEN/PARTIAL
  source_metric_before_for_new_frozen_family: UNKNOWN / not certified by immediate predecessor (m=12 exceeds M_5)
  source_metric_after_for_new_frozen_family: p_u-p_c > 1/260
  previous_structural_scope: beta_{4g+m}(4sqrt(g)+m)<4g-3 (vertical cost by cardinality)
  new_structural_scope: beta_{D0+m}(r_Q+r_V)<2k-1, with exact r_V=||A_{N,V}||; surface F_s x F_s specialization given exactly by (4.6)
  auxiliary_delta: 651 exact finite-grid (g,s) pairs in 2..40 newly certified relative to the prior cardinality criterion; zero direct-beta consistency mismatches
  validation: SELF_CHECK_ONLY
  independent_source_closure: false
```

The scalar `>1/260` should not be compared as an improvement over earlier gaps on different frozen graphs; the substantive source-level advance is the **strictly larger structural criterion** and a concrete graph that the predecessor theorem cannot reach.

## 10. Unresolved full gap

The universal source remains open. The theorem still requires a useful quotient/extension decomposition together with a quotient free marked subset (or some independently strong `p_c` upper bound) and a sufficiently favorable combined spectral budget. An arbitrary Cayley graph of an arbitrary nonamenable group need not present such a quotient or vertical decomposition in its given generating set. Nothing here converts (3.1) into a universal consequence of nonamenability, and the June bridge/endpoint obstruction is not resolved in that generality.

Therefore this run is **PARTIAL**. Complete source closure would additionally require a universal argument plus independent validation and the required other-track audits; a self-check cannot supply that.

No canonical claim, `POSTED.md`, schedule, enabled state, email, Drive, or public-posting state was changed in this run.
