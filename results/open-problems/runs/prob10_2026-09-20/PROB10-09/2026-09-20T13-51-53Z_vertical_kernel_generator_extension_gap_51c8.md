Runtime model: **GPT-5.6 Sol**. Requested GPT-6 maximum is not an authenticated/selectable runtime control in this scheduler. Reasoning effort: **UNVERIFIED**.

# PROB10-09 — vertical-kernel generator extension of the quotient/nonbacktracking criterion

Status: **PARTIAL / restricted theorem proved in this run; universal Benjamini–Schramm Cayley conjecture remains OPEN.** All new mathematics below has an executed exact/self-check and a second internal proof route for the frozen graph, but **no independent validator has yet source-closed it**.

## 0. Frozen parent target

The target remains exactly:

> For every locally finite Cayley graph `G` of every finitely generated nonamenable group, iid **bond** percolation satisfies `p_c(G)<p_u(G)`.

No planar nontransitive site-percolation variant is substituted. Hutchcroft's nonamenable Gromov-hyperbolic quasi-transitive theorem is prior art, not a new result here.

## 1. R20 owner-refocus handoff first: actual predecessor state, artifacts and ownership

The owner-refocus handoff read first is

`runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`.

It records the actual R20 predecessor state that must be preserved rather than silently overwritten:

1. **I0100 / Paley one-localization** — `OPEN/PARTIAL`, current `p_max=1213`, canonical reservation `operations/claims/I0100.md`; preserve all `artifacts/R20/i0100_*` evidence.
2. **KNSV-2026-LOOPY-U** — `OPEN/PARTIAL`, source endpoint `N_sep>11`; preserve `knsv_next_routes_check.*`, `knsv_two_terminal_n12_check.*`, `knsv_seven_vertex_dual_check.*`, `knsv_loopy_rooted_gadget_check.*`, `knsv_one_cross_edge_quotient_exact.*`, and `knsv_transfer_signature_iso_n12_check.*`.
3. **BMO-2025-PUSHING-DELTA** — last actual mathematical R20 target before the owner refocus, `OPEN/PARTIAL`, current `n_all=9`; preserve `bmo_n9_witness_exact.cpp`, `bmo_n9_exact_check.out`, and the six-run handoff `runs/R20/2026-09-19T06-47-48Z_bmo_sixrun_handoff_deficit_sum_d4a8c2.md` plus its associated artifacts.
4. The old terminal waiting predecessor is `runs/R20/2026-09-19T22-59-30Z_terminal_wait_eight_claim_delta_hard_releases_no_free_5a7c31.md`. The owner refocus supersedes that waiting state for this native slot only; it does not alter the predecessor claims or their ownership.

The canonical Benjamini–Schramm source alias remains `D0061 = lyons_nonamenable_2000::conjecture_3.8_(benjamini-schramm_1996)`. The current claim search found no conflicting `operations/claims/D0061` closure. Current `POSTED.md` is an exclusion/posting registry and does not close this unrestricted percolation target.

The neighboring percolation worker NM13-11/T09 was also checked. Its newest report at handoff time is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T15-50-00+0300__t09-one-free-pair-k4-gap.md`,

which owns the Rattaggi/free-layer/factor-branching/product-fibre lane. This run therefore stays in the **quotient/extension/two-point-operator lane** and does not relabel NM13's result.

## 2. Recovered June attempt history

The June archive was not treated as just a status file. I recovered the research directory containing

`probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`

and the large `research/proof_strategy.md`, together with the relevant proof-attempt notes. In particular, this run re-read:

- `notes/round_011.md`: scalar nonbacktracking polynomial/operator bound;
- `notes/round_018.md`: vertical fibre-cluster Galton–Watson attempt and its fixed-depth obstruction;
- `notes/round_040.md`: fixed-direction exponent argument on tree products;
- `notes/round_042.md`: correction by the Hutchcroft–Pan tree-times-amenable/lamplighter prior art and suggested quotient/backscattering routes;
- `notes/round_053.md`: fixed-endpoint nonbacktracking excess criterion;
- `notes/round_054.md`: nonbacktracking fixed-endpoint detour generating function;
- `notes/round_055.md`: bridge-probability criterion
  `p_c(D-1) lambda_c^{NB,br} rho_{sph,2}<1`.

The immediate PROB10-09 predecessor also preserves the earlier normalized finite-set escape, BK/last-exit, killed-SAW/susceptibility boundary-energy, global `ell^2` SAW, product stress, and quotient/fibre-shell failures. None of those is renamed as new work here.

## 3. Idea-before-code record and the three routes

Before running the checker I wrote

`artifacts/prob10_2026-09-20/PROB10-09/20260920T1454Z_vertical_kernel_augmentation_idea_51c8.md`

(commit `b41f5d0cd8452beb8dde62b00ff4f1c7d99a73f7`). It compared genuinely different routes before computation:

1. **Full-graph nonbacktracking + a free marked quotient subset** — succeeds and gives the strongest frozen quantitative gap.
2. **Horizontal nonbacktracking excursions separated from vertical kernel steps** — also succeeds, independently at the mechanism level, but gives a weaker quantitative gap.
3. **Horizontal-component Cheeger transfer + full-graph nonbacktracking** — gives a valid general criterion but fails quantitatively on the frozen `m=6` example; the exact obstruction is recorded below.
4. A still cruder **all-walk adjacency resolvent** was used as a negation control and fails exactly on the frozen example.

Thus code was used only after the mathematical route and its failure tests were written down.

## 4. New structural theorem: vertical kernel generators may be essential

Let

`pi: Gamma -> Q`

be a surjective homomorphism. Let `S_Q` be a finite symmetric generating set of `Q`, with

`D0=|S_Q|`,

and choose an inverse-compatible set `S_H` containing one lift of every element of `S_Q`. **Do not assume `S_H` generates `Gamma`.** Let

`V subset ker(pi)`

be a finite symmetric set, disjoint from `S_H`, with `m=|V|`, and assume only that

`S=S_H union V`

generates `Gamma`. Assume the resulting Cayley graph is simple with degree `D=D0+m`. Put

`Y=Cay(Q,S_Q)`, `X=Cay(Gamma,S)`,

and let

`r_Q=||A_Y||_{2->2}`.

For `D>=3` define

`beta_D(a)=sqrt(D-1)` for `a<=2sqrt(D-1)`,

and

`beta_D(a)=(a+sqrt(a^2-4(D-1)))/2`

otherwise.

### Theorem 4.1 — vertical-generator extension criterion

If `S_Q` contains a symmetric marked subset arising from `k` positive generators that freely generate `F_k` in `Q`, and

`beta_{D0+m}(r_Q+m) < 2k-1`,                                         (4.1)

then

`p_c(X) <= 1/(2k-1) < 1/beta_{D0+m}(r_Q+m) <= p_{2->2}(X) <= p_u(X)`. (4.2)

In particular `p_c(X)<p_u(X)`.

This removes the immediate predecessor's requirement that the horizontal lifts themselves generate the whole extension. The kernel is **arbitrary**: no centrality, abelianity or amenability is assumed.

### Proof

Write the full adjacency operator as

`A_X=A_H+A_V`,

where `A_H` contains the lifted quotient generators and `A_V` contains the vertical kernel generators.

Let `H=<S_H>`. Right multiplication by `S_H` preserves every left coset of `H`, so `A_H` is an orthogonal direct sum of copies of the horizontal Cayley adjacency on `H`. The restriction `pi:H->Q` is still onto because `S_H` contains a lift of every quotient generator.

For one copy, decompose `ell^2(H)` over the fibres of `pi`. If `f` is regarded as an `ell^2(ker(pi|_H))`-valued function on `Q`, then each horizontal edge is a unitary cocycle map between fibres. Pointwise,

`||(A_H f)(q)|| <= sum_{s in S_Q} ||f(qs)||`.

Writing `F(q)=||f(q)||` and applying the scalar adjacency on `Y`,

`||A_H f||_2 <= ||A_Y F||_2 <= r_Q ||F||_2 = r_Q ||f||_2`.

Hence

`||A_H|| <= r_Q`.                                                       (4.3)

Every vertical generator acts by a unitary right translation, so the triangle inequality gives

`||A_V|| <= m`.                                                         (4.4)

Therefore

`||A_X|| <= r_Q+m`.                                                      (4.5)

For a `D`-regular graph the standard nonbacktracking operators satisfy

`N_0=I`, `N_1=A`, `N_2=A^2-DI`,
`N_n=A N_{n-1}-(D-1)N_{n-2}` for `n>=3`.

Spectral calculus and (4.5) bound their exponential `ell^2` growth by `beta_D(r_Q+m)`. Every open connection has a shortest open path and every shortest path is nonbacktracking. Consequently

`T_p(x,y) <= sum_{n>=0} p^n N_n(x,y)`

entrywise, so the operator series is bounded whenever

`p beta_D(r_Q+m)<1`.

Thus

`p_{2->2}(X) >= 1/beta_D(r_Q+m)`.                                       (4.6)

Now choose the marked `k` positive quotient generators. Their lifts satisfy no nontrivial reduced relation: any relation upstairs would project to a nontrivial relation among the free quotient generators. Hence their lifts freely generate an `F_k` subgroup, and the corresponding marked edges form a `2k`-regular tree subgraph of `X`. Monotonicity of bond percolation under adding edges gives

`p_c(X) <= p_c(T_{2k})=1/(2k-1)`.                                      (4.7)

Combining (4.1), (4.6), and (4.7) proves the strict middle inequality. Finally `p_{2->2}<=p_u`: for `p>p_u`, uniqueness and FKG give a uniform positive lower bound `T_p(x,y)>=theta(p)^2`, which is incompatible with boundedness on `ell^2` of an infinite graph. This proves (4.2). `square`

## 5. Companion criterion with no free marked subset

The horizontal subgroup can also be used only on the `p_c` side. The connected Cayley graph

`C=Cay(H,S_H)`

is a label-preserving Cayley cover of `Y`, even though `H` can be proper in `Gamma`. The predecessor's fibre-count coarea proof therefore gives

`phi_E(C)>=phi_E(Y)`.

Since `C` is an infinite subgraph of `X`,

`p_c(X)<=p_c(C)<=1/(1+phi_E(Y))`.

Combining this with (4.6) gives a second theorem:

> If
> `beta_{D0+m}(r_Q+m)<1+phi_E(Y)`,
> then
> `p_c(X)<p_{2->2}(X)<=p_u(X)`.

Unlike Theorem 4.1 this criterion has no free-subset hypothesis. Its usefulness is controlled by the quantitative cost `+m` on the adjacency side.

## 6. Surface-quotient family: complete scope of the proved criterion

Let

`Q=Gamma_g=<a_1,b_1,...,a_g,b_g | prod_{i=1}^g [a_i,b_i]=1>`, `g>=2`,

with the standard symmetric generating set. Then `D0=4g`.

By the classical Dehn–Magnus Freiheitssatz, every proper subset of the `2g` positive standard generators freely generates the subgroup it spans. Therefore we may take

`k=2g-1`.                                                               (6.1)

Żuk's 1997 surface-walk estimate gives, for this standard marking,

`||M_g|| <= 1/sqrt(g)`

for the normalized random-walk operator. Equivalently,

`r_Q=||A_Q|| <= 4sqrt(g)`.                                               (6.2)

Theorem 4.1 now proves a strict percolation gap for **every** group extension of `Gamma_g`, every inverse-compatible standard horizontal lift, and every symmetric vertical kernel set `V` generating the missing kernel directions whenever

`beta_{4g+m}(4sqrt(g)+m)<4g-3`.                                         (6.3)

This condition has a closed form. Put

`B=4g-3`, `q=4g+m-1`, `a=4sqrt(g)+m`.

In the relevant range `B>sqrt(q)`, so `beta<B` is equivalent to

`a < B+q/B`.

After multiplying by `B` and collecting the `m` terms,

`4(g-1)m < 16g^2-20g+8-(16g-12)sqrt(g)`.

Hence the exact scope is

`m < M_g := [4g^2-5g+2-(4g-3)sqrt(g)]/(g-1)`.                           (6.4)

For orientation,

`M_2=0.9289...`, `M_3=3.7057...`, `M_4=20/3`, `M_5=9.7467...`.

Thus this method permits vertical-kernel cardinality at most `0,3,6,9` respectively for `g=2,3,4,5` (with the obvious parity/involution restrictions imposed by the chosen symmetric kernel set). The checker scanned 8,476 `(g,m)` cases through `g=100` against (6.3) and (6.4) and found no mismatch; the proof above, not the scan, establishes the equivalence.

This is a **restricted family theorem**, hence PARTIAL with respect to the universal conjecture.

## 7. Frozen graph outside the hyperbolic/acylindrical-hyperbolic all-Cayley classes

Take `g=4` and let

`Gamma = Z^3 semidirect_alpha Gamma_4`,

where

`alpha(a_1)=M = [[1,1,0],[0,1,1],[0,0,1]]`

and every other positive standard surface generator acts trivially. This is a well-defined homomorphism: every surface commutator maps to the identity because the corresponding `b_i` actions are trivial. The matrix `M` is unipotent of infinite order, so the `Z^3` kernel is genuinely noncentral.

Use the split lifts of all sixteen standard symmetric surface directions together with

`V={+-e_1,+-e_2,+-e_3}`,

so `m=6`. The horizontal lifts alone generate only `{0} x Gamma_4`; therefore the immediately preceding horizontal-generation theorem does **not** apply. The full set does generate `Gamma`.

This group is not Gromov hyperbolic because it contains `Z^3`. It is also not acylindrically hyperbolic: `Z^3` is an infinite normal subgroup, while Osin's s-normal-subgroup theorem says every infinite normal subgroup of an acylindrically hyperbolic group is itself acylindrically hyperbolic; `Z^3` is amenable and is not. Thus Hutchcroft's hyperbolic theorem and Choi–Seo's every-Cayley theorem for acylindrically hyperbolic groups do not subsume this graph.

The subgroup-relativization theorem of Hutchcroft–Pan (`arXiv:2409.12283`) assumes an amenable `wq`-normal subgroup of **exponential growth** for its main new class. The normal kernel here has polynomial growth. In fact every amenable subgroup of this particular semidirect product has polynomial growth: its projection to the surface group is virtually cyclic, and the corresponding action on a subgroup of `Z^3` is by a power of the same unipotent matrix `M`; hence it lies in a virtually unipotent polycyclic group. So that exponential-growth hypothesis is not available here.

Juschenko–Nagnibeda-type results guaranteeing the existence of *some* good generating set for broad extension classes are prior art; the present statement concerns this explicit fixed generating set and a uniform quantitative criterion.

## 8. Certified frozen gap

For the frozen graph,

`D=16+6=22`,

and from (4.5) and Żuk,

`||A_X|| <= 8+6=14`.

The nonbacktracking exponent bound is therefore

`beta_22(14)=(14+sqrt(196-84))/2 = 7+2sqrt(7)`.                          (8.1)

By Freiheitssatz, seven of the eight positive surface generators freely generate `F_7`, so

`p_c(X) <= 1/13`.                                                       (8.2)

From (8.1),

`p_{2->2}(X) >= 1/(7+2sqrt(7)) = (7-2sqrt(7))/21`.                     (8.3)

Therefore

`p_u(X)-p_c(X) >= (70-26sqrt(7))/273 = 0.00443394107077...`             (8.4)

and in particular

`boxed(p_u(X)-p_c(X) > 1/250 = 0.004).`                                 (8.5)

The checker proves the final comparison without floating point: (8.4) is greater than `1/250` iff

`17227 > 6500 sqrt(7)`,

and squaring gives exact positive margin

`17227^2-7*6500^2 = 1,019,529`.

A completely rational nonbacktracking certificate is also recorded. Take

`p_*=81/1000` and `z=1/p_*=1000/81`.

Then

`z^2-21 = 862219/6561 >0`,

and

`z+21/z-14 = 3781/81000 >0`.

So the NB growth is strictly below `z`, hence `p_{2->2}>81/1000`. Together with (8.2),

`p_u-p_c > 81/1000-1/13 = 53/13000 > 1/250`,

with exact slack `1/13000` beyond `1/250`.

### Source metric

- **Before:** this explicit vertical-generator graph had no PROB10-09 strict-gap certificate, because the horizontal lifts do not generate the full semidirect product.
- **After:** `p_u-p_c>1/250`, with the stronger analytic lower bound (8.4).

### Parent-source metric

- **Before:** universal Cayley bond conjecture `OPEN/PARTIAL`.
- **After:** universal Cayley bond conjecture `OPEN/PARTIAL`.

There is therefore **no universal source closure** in this run.

### Auxiliary/mechanism delta

- Before structural scope: arbitrary extension only when the horizontal lifted set generated the whole extension (or the whole graph was itself the connected horizontal cover).
- After structural scope: arbitrary extension with horizontal generation **not required**; finitely many essential kernel generators are allowed under (4.1), or under the Cheeger variant.
- Surface specialization: exact vertical-budget criterion (6.4); at genus four it certifies every such extension with `m<=6`.

This structural delta is kept separate from the parent source metric.

## 9. Distinct alternate route: two-type horizontal/vertical resolvent

The frozen graph admits a second internal proof that does not use the full degree-22 nonbacktracking characteristic root.

Let `N_n^H` denote horizontal nonbacktracking operators for the degree-16 horizontal Cayley cover. Their generating function is

`R_H(p)=sum_{n>=0} p^n N_n^H
       =(1-p^2)(I-pA_H+15p^2 I)^(-1)`.

Using `||A_H||<=8`,

`||R_H(p)|| <= (1-p^2)/(1-8p+15p^2)`                                   (9.1)

when the denominator is positive.

Every simple path in the full graph decomposes into maximal horizontal nonbacktracking segments separated by individual vertical steps. Overcounting all such concatenations gives the positive-kernel domination

`T_p <= R_H(p) sum_{j>=0} [p A_V R_H(p)]^j`.                            (9.2)

Hence boundedness follows whenever

`p m ||R_H(p)||<1`.                                                      (9.3)

At

`p=39/500`,

the checker obtains exactly

`1-8p+15p^2 = 23363/50000 >0`,

and the equivalent cubic slack

`1-14p+15p^2+6p^3 = 131707/62500000 >0`.

Equivalently,

`1 - 6p(1-p^2)/(1-8p+15p^2) = 131707/29203750 >0`.

By continuity, `p_{2->2}>39/500`. Combined with `p_c<=1/13`, this independently gives

`p_u-p_c > 7/6500 > 1/1000`.

This is weaker than (8.5), but it is a genuinely different internal mechanism check. It is **not** counted as independent external/source validation.

## 10. Negation tests and exact obstructions

### 10.1 Vertical budget cannot be made arbitrary

At genus four with `m=6`,

`beta_22(14)=7+2sqrt(7)<13`

because `sqrt(7)<3`.

At the very next integer budget `m=7`,

`beta_23(15)=(15+sqrt(137))/2>13`

because `137>121`. Thus the present scalar theorem genuinely stops between six and seven vertical directions; it must not be advertised as arbitrary vertical augmentation. (For torsion-free kernels a symmetric set may jump by pairs, but the abstract theorem allows involutions, so `m=7` is a legitimate boundary test.)

### 10.2 Cheeger-only route fails on the frozen example

For the genus-four surface quotient, the predecessor's Mohar/Dodziuk estimate from `r_Q<=8` gives

`phi_E(Y)>=16(16-8)/15=128/15`,

so the available comparison is only

`1+phi_E(Y)>=143/15`.

But

`7+2sqrt(7)>143/15`

(the checker reduces this to the exact positive square margin
`7-(19/15)^2=1214/225`). Therefore the no-free-subset Cheeger criterion does not close this `m=6` graph. The free marked quotient subset is quantitatively load-bearing here.

### 10.3 Crude all-walk adjacency resolvent also fails

Using only `||A_X||<=14` yields `p_{2->2}>=1/14`, while the tree witness gives only `p_c<=1/13`. Since

`1/14<1/13`

with exact gap `1/182`, ordinary walk growth cannot prove the desired separation. Nonbacktracking structure is essential to this certificate.

These failure checks are the requested attempt to falsify the new statement and delimit its exact mechanism scope.

## 11. Executed tests

The checker is

`artifacts/prob10_2026-09-20/PROB10-09/20260920T1456Z_vertical_kernel_augmentation_exact_check_51c8.py`

and its captured output is

`artifacts/prob10_2026-09-20/PROB10-09/20260920T1456Z_vertical_kernel_augmentation_exact_check_51c8.out`.

It finished with

`ALL_EXACT_CORE_CHECKS_PASS`.

Load-bearing exact outputs include:

- scalar NB characteristic slack `3781/81000` at `p=81/1000`;
- rational frozen gap `53/13000`, exceeding `1/250` by `1/13000`;
- radical-square margin `1019529` for the stronger analytic bound;
- `m=6` pass / `m=7` fail margins `2` and `16` after exact squaring;
- two-type resolvent strict slack `131707/29203750`;
- Cheeger-route obstruction square margin `1214/225`;
- 8,476-case auxiliary scan of (6.3) versus (6.4), with zero mismatches.

## 12. Literature/prior-art closure for this run

Consumed/current sources include:

1. Tom Hutchcroft, *Percolation on Hyperbolic Graphs*, arXiv:1804.10191 / GAFA 2019: bond `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs, and the `p_{2->2}` framework.
2. Tom Hutchcroft and Minghao Pan, *Percolation at the uniqueness threshold via subgroup relativization*, arXiv:2409.12283 (2024): new `p_u` nonuniqueness classes via amenable `wq`-normal subgroups of exponential growth, among other results.
3. Grigory Terlov and Ádám Timár, *Weighted-amenability and percolation*, arXiv:2502.02560 (2025): weighted/nonunimodular analogues; it does not replace the present unimodular Cayley bond target.
4. Inhyeok Choi and Donggyun Seo, *Percolation in acylindrically hyperbolic groups*, arXiv:2508.08932 (2025): every Cayley graph of an acylindrically hyperbolic group has a nonuniqueness phase.
5. Andrzej Żuk, *A remark on the norms of a random walk on surface groups*, Colloq. Math. 72 (1997), 195–206: normalized standard surface-walk norm at most `1/sqrt(g)`. The bibliographic record is also linked from Żuk's 1997 Annales de l'Institut Fourier paper.
6. Classical Dehn–Magnus Freiheitssatz for one-relator groups: a proper subset of the generators in the standard surface one-relator presentation freely generates.
7. Denis Osin, *Acylindrically hyperbolic groups*, arXiv:1304.1246 / Trans. AMS 2016: acylindrical-hyperbolicity machinery, including the s-normal/infinite-normal subgroup obstruction used above.
8. Shirshendu Chatterjee, Yang Chen, Grigory Terlov, *beta-Skewed Maximal Spanning Forests*, arXiv:2609.11845, submitted 10 September 2026: fresh background continuing to treat the broader nonuniqueness questions as active rather than universally closed.

The 2026 planar **site** paper was noticed in search and deliberately not substituted for the frozen Cayley **bond** target.

No claim of external novelty is made beyond the repo-relative structural extension until a dedicated priority search and an independent proof audit occur.

## 13. Unresolved full gap

The universal obstruction is unchanged in substance. The new theorem is powerful only when a quotient simultaneously supplies:

1. a controlled horizontal adjacency norm `r_Q`,
2. enough cheap critical-side growth (a free marked subset, or sufficient expansion), and
3. a bounded vertical-generator penalty `m`.

For a general fixed Cayley graph of a nonamenable group there need be no useful quotient of this form, no visible free marked subset, and no small vertical budget. The exact genus-four `m=7` failure already demonstrates that simply charging arbitrary extra directions by the triangle inequality cannot scale to the universal conjecture.

Thus the next mathematically meaningful continuation inside this conjecture is not to repeat the same scalar estimate, but to reduce the vertical penalty from `m` by exploiting the **actual operator norm or nonbacktracking transition structure of the kernel-generated vertical block**, or to prove a quotient/subgroup comparison that preserves enough two-point decay without paying one unit per added direction.

## 14. Validation and delivery status

- Universal target: **OPEN/PARTIAL**.
- New restricted theorem: **proved in this report subject to independent validation**.
- Exact arithmetic/self-check: **PASS**.
- Internal alternate mechanism check: **PASS**, but not an independent audit.
- Independent source/proof validation: **NOT YET PRESENT**.
- No canonical claim was closed or overwritten.
- No schedule/enabled-state, email, Drive, public-posting, or neighboring-worker state was changed.
