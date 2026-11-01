Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — pure-triangle amplification and finite-supplement gap

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorems below; universal T09 remains OPEN.** The theorem arguments below are complete as written and the load-bearing endpoint arithmetic was executed exactly in this run. There has been no independent review. External priority of the exact fixed generating-set families remains **UNVERIFIED** after the bounded source check below.

## 1. Frozen source problem and source-level before/after

The source problem is unchanged:

> For iid bond percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

The universal statement remains **OPEN**.

### Before this run

The immediately preceding NM13-11 report proved a degree-7 gap for every `SL_n(Z)`, `n>=5`, using the block

`C_3 * C_3 * Z`

inside a finite-index kernel of a ping-pong subgroup `C_3*Z`, together with one involution. It also proved an arbitrary-finite-supplement theorem by retaining the kernel generator `u=g^N`; that theorem required `N>=b+6` for a supplement of cardinality `b`, and at the coarse endpoint had degree `3b+14`.

The residual obstruction was to replace the imported infinite-order block edge by a more intrinsic relation-rich block and to weaken the finite-supplement requirements without losing the demonstrated `p_c`-to-`p_u` transfer.

### After this run

The infinite-order kernel generator can be discarded entirely. If

`L=<t,g> ~= C_3 * Z`,

then the conjugates

`t_j=g^j t g^{-j}`, `0<=j<N`,

generate the pure torsion subgroup

`H_N=<t_0,...,t_{N-1}> ~= *_{j=0}^{N-1} C_3`.

Using exact factor-cluster branching on `H_N`, a new weighted-Schur estimate for its standard adjacency, and the nonbacktracking `L^2` transfer gives the theorem below.

**Theorem A (pure-triangle finite supplement).** Let `Gamma` contain `L=<t,g> ~= C_3*Z`. Let `B` be a finite symmetric set of cardinality `b>=1` such that `Gamma=<B,t>`. Fix `N>=2`, put

`t_j=g^j t g^{-j}`, `0<=j<N`,

`T_N={t_j,t_j^{-1}:0<=j<N}`,

and assume `B` is disjoint from `T_N`. Let

`G_N=Cay(Gamma,B union T_N)`.

Write

`D=b+2N`, `Q=D-1=b+2N-1`,

`a_{N,b}=b+1+2 sqrt(2(N-1))`,

and

`beta_Q(a)=sqrt(Q)` if `a<=2sqrt(Q)`, while

`beta_Q(a)=(a+sqrt(a^2-4Q))/2` otherwise.

Then

`p_c(G_N) < r_N`,

where `r_N` is the unique solution in `(0,1)` of

`2(N-1)(p+p^2-p^3)=1`,

and

`p_u(G_N) >= p_{2->2}(G_N) >= 1/beta_Q(a_{N,b}).`

In particular, every

`N >= max{4,b+2}`

is certified to satisfy

`boxed(p_c(G_N)<p_u(G_N)).`

For `N>=b+3`, and also for the endpoint `N=b+2` when `b>=4`, the proof has the common pivot

`boxed(p_c(G_N)<1/(2N-2)<p_u(G_N))`.

The two exceptional endpoints needed to complete the range are quantitative:

- `b=2,N=4`: `p_c<3/20<153/1000<p_u`, hence `p_u-p_c>3/1000`;
- `b=3,N=5`: `p_c<23/200<3/25<p_u`, hence `p_u-p_c>1/200`.

For the concrete one-involution case there is a sharper certificate.

**Theorem B (all-torsion degree-9 higher-rank family).** Suppose `Gamma=<s,t>`, where `s^2=t^3=1`, and there exists `g` with `<t,g> ~= C_3*Z`. Put `t_j=g^j t g^{-j}` for `j=0,1,2,3`. Then

`S={s} union {t_j,t_j^{-1}:0<=j<=3}`

is a simple symmetric generating set of cardinality nine and

`boxed(p_c(Cay(Gamma,S))<3/20<23/125<p_u(Cay(Gamma,S)))`.

Consequently

`boxed(p_u-p_c>17/500=0.034).`

Every label in `S` has finite order two or three. Thus this is structurally different from the preceding degree-7 theorem, whose marked set included the infinite-order kernel edge `g^2`.

For every `n>=5`, the completed `(2,3)`-generation theorem for `SL_n(Z)` supplies `s,t`, and the ping-pong theorem used in the preceding report supplies `g` with `<t,g>~=C_3*Z`. Therefore every `SL_n(Z)`, `n>=5`, has an explicit **degree-9 all-torsion Cayley graph** with gap `>17/500`.

**Original-problem delta:** universal T09 remains OPEN. The source-level fixed-graph scope expands from torsion-plus-infinite-order kernel blocks to pure finite-order marked sets, and the arbitrary supplement theorem improves from `N>=b+6` with an extra `u^{+-1}` pair to `N>=max(4,b+2)` with no `u` pair.

**Mechanism delta:** the new mechanism uses the subgroup `*_{j=0}^{N-1}C_3` itself for both sides: exact triangle-factor branching lowers `p_c`, while a syllable-weight Schur estimate bounds its regular-representation norm. This is transferred through the nonbacktracking kernel all the way to `p_u`; it is not an auxiliary operator inequality without a percolation conclusion.

## 2. Compact continuity handoff and preserved Benjamini--Schramm history

The controlling policy is `operations/PROGRESS20_2026-09-20.md`; LIVE20 assigns NM11 to T09 at `proofnet24/NM13-11/progress-percolation/`. The current `POSTED.md` exclusion registry does not mark the universal T09 target as closed or posted, and no excluded claim is reopened here.

Preserved June routes from `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md` and `open_status.md` include:

- normalized-kernel finite-set escape and the BK/last-exit finite-volume versus boundary-energy dichotomy;
- killed-SAW interior growth and susceptibility-weighted boundary norms;
- the combined killed-growth/boundary-energy criterion, calibrated on regular trees but circular in general when it imports the desired `L^2` boundedness;
- global `ell^2` SAW growth, with amenable guardrails and product stress tests;
- nonbacktracking polynomial/operator bounds;
- quotient/fibre-shell and fixed-endpoint bridge attempts.

Those routes that did not complete a transfer to `p_c<p_u` remain mechanism history, not source-level advances. The September continuation then produced complete restricted transfers for free cores, triangle fibres, S-arithmetic examples, product-lattice perturbations, free augmentation tails, dependent power layers, factor branching, and the preceding `C_3*C_3*Z` kernel construction. This run changes the subgroup block again rather than polishing the same constants.

No unchanged-run recovery rule is triggered.

## 3. Pure triangle subgroup inside `C_3*Z`

Let

`L=<t,g | t^3=1> ~= C_3*Z`.

For `N>=2`, define

`t_j=g^j t g^{-j}`, `0<=j<N`.

The finite-index-kernel calculation from the preceding report gives

`ker(L -> Z/N) ~= (*_{j=0}^{N-1} C_3) * Z`,

with the `C_3` factors generated by the `t_j` and the infinite cyclic factor generated by `g^N`. Therefore the subgroup generated only by the torsion factors is

`boxed(H_N=<t_0,...,t_{N-1}> ~= *_{j=0}^{N-1} C_3).`       (3.1)

Equivalently, this follows directly from free-product normal form in `C_3*Z`: a nonempty reduced word in the distinct conjugate factors cannot collapse.

The standard symmetric generating set of `H_N` is

`T_N={t_j,t_j^{-1}:0<=j<N}`,

of cardinality `2N`.

## 4. Critical side: exact free-factor cluster branching

For a triangle factor `C_3`, generated by its two nonidentity elements, a specified non-seed vertex is connected to the seed either by its direct edge or by the two-edge route through the third vertex. Thus

`P(seed <-> specified vertex)=p+(1-p)p^2=p+p^2-p^3`,

and the expected number of non-seed vertices in the open factor cluster is

`mu_C(p)=2(p+p^2-p^3)`.                                  (4.1)

Explore percolation on `H_N=*_{j=0}^{N-1}C_3` by free-product factor cosets. A particle whose reduced prefix ends in factor `i` exposes the seed cluster in every factor coset `j!=i`; each non-seed vertex reached there becomes a child of type `j`. Distinct child cosets reached from distinct reduced prefixes have disjoint edge sets apart from seed vertices, so offspring vectors of different particles are independent. This is an honest `N`-type Galton--Watson subprocess.

Its mean matrix has zero diagonal and every off-diagonal entry equal to `mu_C(p)`. Hence its Perron eigenvalue is

`rho(M_p)=(N-1)mu_C(p)`.                                 (4.2)

Let

`p_0=1/(2N-2)=1/(2(N-1))`.

Writing `m=N-1`, exact algebra gives

`m mu_C(1/(2m))-1=(2m-1)/(4m^2)>0`.                     (4.3)

Therefore the subprocess is strictly supercritical at `p_0`, and by continuity it is supercritical for some `p<p_0`. Thus

`boxed(p_c(Cay(H_N,T_N))<1/(2N-2)).`                     (4.4)

Since every left coset of `H_N` gives a copy of this Cayley graph inside `G_N`,

`boxed(p_c(G_N)<1/(2N-2)).`                              (4.5)

More sharply, the exact factor criterion gives

`p_c(G_N)<r_N`,                                          (4.6)

where `r_N` is the unique root of `2(N-1)(p+p^2-p^3)=1`.

This factor-branching identity is consistent with the classical free-product percolation framework; no novelty is claimed for that general identity. The new use here is the pure-torsion finite-index conjugate block inside the fixed ambient Cayley graph together with the uniqueness-side operator transfer.

## 5. A syllable-weight Schur bound for `* C_3`

Let `A_N` be the adjacency operator of `Cay(H_N,T_N)`. Give a reduced free-product word `w` the positive weight

`omega(w)=r^(number of nontrivial factor syllables)`.

Suppose `w` ends in factor `i`. Of the two generators of factor `i`, one changes the final nontrivial element inside that same `C_3` and has weight ratio `1`, while the other cancels the final syllable and has ratio `r^{-1}`. Each of the `2(N-1)` generators from the other factors appends a new syllable and has ratio `r`. Hence

`(A_N omega)(w)/omega(w) <= 1+r^{-1}+2(N-1)r`.           (5.1)

At the identity the ratio is `2Nr`. The weighted Schur test for the symmetric nonnegative kernel therefore gives

`||A_N|| <= max{1+r^{-1}+2(N-1)r, 2Nr}`.                (5.2)

Set

`r=1/sqrt(2(N-1))`, `x=sqrt(2(N-1))`.

Then the first term equals `1+2x`. The identity term is

`2N/x=x+2/x <= 1+2x`,

because `x>=sqrt(2)>1` and `2/x<=1+x`. Therefore

`boxed(||A_N|| <= 1+2sqrt(2(N-1))).`                    (5.3)

If `B` is a symmetric supplement of cardinality `b`, its adjacency contribution is a sum of `b` unitary right translations, hence has norm at most `b`. Consequently

`boxed(||A_{G_N}|| <= a_{N,b}:=b+1+2sqrt(2(N-1))).`      (5.4)

## 6. Nonbacktracking transfer to `p_u`

The graph `G_N` is `D=b+2N` regular; put `Q=D-1=b+2N-1`.

If `N_m(x,y)` counts length-`m` nonbacktracking walks, the corresponding operators satisfy

`N_0=I`, `N_1=A`, `N_2=A^2-DI`,

and for `m>=3`,

`N_m=A N_{m-1}-Q N_{m-2}`.

The spectral theorem therefore bounds their exponential `ell^2` growth by

`beta_Q(a)=sqrt(Q)` if `a<=2sqrt(Q)`, and

`beta_Q(a)=(a+sqrt(a^2-4Q))/2`

otherwise, for any upper bound `a>=||A||`.

Every open connection contains a shortest open path, which is nonbacktracking, so entrywise

`T_p(x,y) <= sum_{m>=0} p^m N_m(x,y)`.

Hence the connectivity kernel is `ell^2` bounded whenever `p beta_Q(a)<1`, and

`p_{2->2}(G_N) >= 1/beta_Q(a_{N,b}).`                    (6.1)

Finally `p_{2->2}<=p_u`: for `p>p_u`, uniqueness of the infinite cluster and FKG imply `T_p(x,y)>=theta(p)^2>0` for every pair, so a row of `T_p` is not in `ell^2` on an infinite graph. Thus

`boxed(p_u(G_N) >= 1/beta_Q(a_{N,b})).`                  (6.2)

A convenient root test is: if `z>sqrt(Q)` and

`z+Q/z>a_{N,b}`,                                         (6.3)

then `beta_Q(a_{N,b})<z` and therefore `p_u>1/z`.

## 7. Proof of the range `N>=max(4,b+2)`

### 7.1 The easy range `N>=b+3`

Take

`z=2N-2`.

By (4.5), `p_c<1/z`. Since `Q=z+b+1`,

`z+Q/z-a_{N,b}`

`=z-b+(b+1)/z-2sqrt(z)`.                                (7.1)

If `N>=b+3`, then `b<=N-3`, so

`z-b=2N-2-b >= N+1`.

Also

`(N+1)^2-4(2N-2)=(N-3)^2>0`

for `N>=4`, hence

`N+1>2sqrt(2N-2)=2sqrt(z)`.

Therefore (7.1) is strictly positive. Moreover `z^2>Q` in this range. The root test gives

`p_u>1/z=1/(2N-2)>p_c`.                                  (7.2)

In fact, with `beta=beta_Q(a_{N,b})`,

`p_u-p_c > 1/beta - 1/(2N-2) >0`.                       (7.3)

### 7.2 The endpoint `N=b+2` for `b>=4`

Now

`z=2N-2=2b+2`, `Q=3b+3`,

and

`z+Q/z-a_{N,b}`

`=b+5/2-2sqrt(2b+2)`.                                   (7.4)

Both sides are positive, and

`(b+5/2)^2-4(2b+2)=(4b^2-12b-7)/4>0`

for every `b>=4` (already positive at `b=4`, and increasing thereafter). Thus (7.4) is positive. Also `z^2>Q`. Therefore again

`p_c<1/(2N-2)<p_u`.                                      (7.5)

### 7.3 Exceptional endpoint `b=2,N=4`

The critical-side block has four triangle factors. At `p=3/20`,

`3 mu_C(p)-1=59/4000>0`,

so

`p_c<3/20`.                                              (7.6)

Here `D=10`, `Q=9`, and

`a_{4,2}=3+2sqrt(6)<79/10`,

using `sqrt(6)<49/20`. Take `z=1000/153`. Then `z^2>9` and exact arithmetic gives

`z+9/z-79/10=1981/153000>0`.

Hence

`p_u>153/1000`,

so

`boxed(p_u-p_c>3/1000).`                                 (7.7)

### 7.4 Exceptional endpoint `b=3,N=5`

At `p=23/200`,

`4 mu_C(p)-1=13633/1000000>0`,

so

`p_c<23/200`.                                            (7.8)

Here `D=13`, `Q=12`, and

`a_{5,3}=4+2sqrt(8)=4+4sqrt(2)<338/35`,

using `sqrt(2)<99/70`. Take `z=25/3`. Then `z^2>12` and

`z+12/z-338/35=61/525>0`.

Thus

`p_u>3/25`,

and

`boxed(p_u-p_c>1/200).`                                  (7.9)

Combining Sections 7.1--7.4 proves Theorem A for every

`N>=max{4,b+2}`.

## 8. Sharpened one-involution endpoint and `SL_n(Z)`

Take `b=1,N=4`. The critical calculation at `p=3/20` is still

`3mu_C(3/20)-1=59/4000>0`,

so

`p_c<3/20`.                                              (8.1)

Here `D=9`, `Q=8`, and

`a_{4,1}=2+2sqrt(6)<69/10`.

Take `z=125/23`. Then `z^2>8` and

`z+8/z-69/10=39/5750>0`.                                (8.2)

Therefore

`p_u>23/125`,

and

`boxed(p_u-p_c>23/125-3/20=17/500).`                    (8.3)

Now let `Gamma=SL_n(Z)`, `n>=5`. Vsemirnov's completed `(2,3)`-generation result gives an involution `s` and an order-three element `t` with `Gamma=<s,t>`. The simultaneous ping-pong result of Janssens--Temmerman--Thilmany used in the preceding report supplies an infinite-order `g` with

`<t,g> ~= C_3*Z`.

Define `t_j=g^j t g^{-j}`, `j=0,1,2,3`. Free-product normal form makes the eight labels `t_j^{+-1}` distinct. They all have order three, while `s` has order two, so `s` is disjoint from them. Since `t_0=t`, the set

`S_n={s,t_j,t_j^{-1}:0<=j<=3}`

generates `SL_n(Z)` and has cardinality nine. Therefore (8.3) applies.

This application is not subsumed by the all-Cayley hyperbolic or acylindrically-hyperbolic theorems: `SL_n(Z)`, `n>=5`, is a higher-rank lattice, and higher-rank lattice hyperbolic-action rigidity excludes a non-elementary acylindrical action of the kind required for acylindrical hyperbolicity. The 2026 property-(T) endpoint theorem gives nonuniqueness at `p_u` but does not itself furnish the quantitative fixed-graph separation proved here.

The exact worldwide priority of this all-torsion degree-9 family is **UNVERIFIED**. Pak--Smirnova-Nagnibeda already prove group-level existence of some favorable generating set for every finitely generated nonamenable group, so no new group-level existence claim is made.

## 9. Current exact source scopes

A fresh source check in this run gives:

1. **Hutchcroft, arXiv:1804.10191.** Current arXiv version is **v3, last revised 26 March 2019**. The paper proves `p_c<p_u` for connected, locally finite, nonamenable, **Gromov-hyperbolic quasi-transitive graphs**. Its v3 note says the metadata changed for bureaucratic reasons and the text did not change. This is a hyperbolic special case, not arbitrary nonamenable Cayley graphs.

2. **Hutchcroft--Pan, arXiv:2409.12283.** Current arXiv version is still **v1, submitted 18 September 2024**. It studies percolation **at `p_u`**, proving nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth and a co-heredity result for a strong endpoint property. It does not state a general quantitative fixed-graph `p_c<p_u` theorem of the present kind.

3. **Terlov--Timar, arXiv:2502.02560.** Current arXiv version is **v2, last revised 14 September 2025**. It develops weighted/level amenability and proves a relaxed Pak--Smirnova-Nagnibeda-style form of a conjecture involving the heavy-cluster threshold `p_h<p_u` in the weighted/nonunimodular setting. It is not the ordinary unimodular fixed-Cayley `p_c<p_u` statement.

The later Choi--Seo theorem, arXiv:2508.08932, proves `p_c<p_u` for every Cayley graph of every **acylindrically hyperbolic** group. The higher-rank `SL_n(Z)` application above is outside that group class.

Sources checked in this run:

- https://arxiv.org/abs/1804.10191
- https://arxiv.org/abs/2409.12283
- https://arxiv.org/abs/2502.02560
- https://arxiv.org/abs/2508.08932
- M. A. Vsemirnov, *On (2,3)-generation of matrix groups over the ring of integers, II*, St. Petersburg Math. J. 32 (2021).
- Bader--Caprace--Furman--Sisto, *Hyperbolic actions of higher rank lattices come from rank-one factors*, ETDS 45 (2025), 961--988.
- Janssens--Temmerman--Thilmany, simultaneous ping-pong theorem, as cited and checked in the preceding NM13-11 report.

## 10. Exact checker and actual output

Checker source:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T13-50-00+0300__t09-pure-triangle-supplement-gap-check.py`

creation commit:

`f4c7d2abec0b40678b66e1766e3122b80e7119ca`.

The checker was actually executed in this invocation. Its archived output is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T13-50-00+0300__t09-pure-triangle-supplement-gap-check.out`

creation commit:

`3d97f2f3b5825552f86ba731d2990244955d6760`.

The output ends

`ALL_EXACT_CHECKS_PASS`.

The general theorem is proved algebraically above; the finite loops in the checker are sanity checks rather than substitutes for the symbolic proof.

## 11. Honest residual obstruction and next attack

The first pure-triangle boundary is now very sharp. For `b=1,N=3`, the graph would have degree seven with the all-torsion marked set

`{s,t_0^{+-1},t_1^{+-1},t_2^{+-1}}`.

The exact triangle-block critical threshold solves

`4(p+p^2-p^3)=1`,

namely

`p=0.214003365841898...`.

The present scalar operator bound is

`||A||<=6`, `Q=6`,

which yields only

`p_u >= 1/(3+sqrt(3)) = 0.211324865405187...`.

Thus this method misses the degree-7 pure-torsion case by about `0.00267850`. This is a **method failure**, not evidence that `p_c=p_u`; the case remains unknown here.

The next materially different attack should exploit the interaction of the involution with the three triangle factors instead of charging it by the scalar norm `1`: either a colored nonbacktracking recurrence separating the involution and triangle edge types, or a branching construction that uses selected `s`-edges on the critical side. Constant polishing of the scalar triangle inequality is unlikely to cross this endpoint.

## 12. ledger_delta

```yaml
ledger_delta:
  owner_slot: NM11
  parent: T09
  universal_status: OPEN
  restricted_status: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  before_source_scope:
    - degree-7 SL_n(Z), n>=5, block C3*C3*Z plus involution, gap > 1/100
    - arbitrary supplement b with kernel generator u included, sufficient N>=b+6
  after_source_scope:
    - pure-torsion block H_N = *_{j=0}^{N-1} C3
    - arbitrary supplement theorem for every N>=max(4,b+2), no u-generator pair
    - degree-9 all-torsion Cayley graphs of every SL_n(Z), n>=5
    - concrete gap p_u-p_c > 17/500 for the degree-9 family
  mechanism_progress:
    - exact N-type triangle-factor Galton-Watson transfer to p_c
    - weighted syllable Schur bound ||A_HN|| <= 1+2sqrt(2(N-1))
    - nonbacktracking L2 transfer to p_u
  failed_boundary:
    scope: b=1,N=3 pure-triangle degree-7 case
    status: UNKNOWN
    obstruction: scalar norm route gives 0.2113248654 below exact block critical threshold 0.2140033658
    next_method: colored nonbacktracking or s-edge-enhanced branching
  checker_commit: f4c7d2abec0b40678b66e1766e3122b80e7119ca
  output_commit: 3d97f2f3b5825552f86ba731d2990244955d6760
```
