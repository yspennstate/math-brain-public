Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — a degree-7 higher-rank-lattice gap from a finite-index triangle kernel

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorems below; universal T09 remains OPEN.** The theorem arguments below are complete as written and the load-bearing arithmetic has an executed exact-rational checker, but there has been no independent review. External priority of the exact fixed generating-set family remains **UNVERIFIED** after the bounded source search recorded below.

## 1. Frozen source problem and source-level before/after

The source problem is unchanged:

> For iid bond percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

The universal statement remains **OPEN**.

### Before this run

The immediately preceding NM13-11 report proved positive gaps for nonfree power-thickened free cores. Its strongest low-degree concrete higher-rank-lattice endpoint was a degree-15 Cayley graph of every `SL_n(Z)`, `n>=5`, with a doubled power layer and

`p_c < 47/500 < 941/10000 < p_u`,

so `p_u-p_c>1/10000`.

That construction still came from an auxiliary Schreier free basis. The explicit residual obstruction was to replace the free-cyclic-factor engineering by a genuinely nonfree block and retain both a critical-side percolation transfer and a uniqueness-side operator estimate.

### After this run

A finite-index kernel inside one ping-pong subgroup `C_3 * Z` gives a torsion block

`K_2 ~= C_3 * C_3 * Z`.

A weighted Schur estimate for its standard adjacency, combined with exact factor-cluster branching, yields the following degree-7 theorem.

**Theorem A (one-involution extension of a `C_3*C_3*Z` block).** Suppose a group `Gamma` contains

`K=<t_0>*<t_1>*<u> ~= C_3 * C_3 * Z`,

where `t_0,t_1` have order three and `u` has infinite order, and suppose `Gamma=<s,K>` for an involution `s`. Then the simple Cayley graph with generating set

`S={s,t_0,t_0^{-1},t_1,t_1^{-1},u,u^{-1}}`

is 7-regular and satisfies

`boxed(p_c(G)<21/100<11/50<p_u(G))`,

hence

`boxed(p_u(G)-p_c(G)>1/100)`.

A concrete application is obtained for every `SL_n(Z)`, `n>=5`: choose a `(2,3)`-generating pair `(s,t)`, choose a ping-pong partner `g` with `<t,g> ~= C_3 * Z`, and set

`t_0=t`, `t_1=g t g^{-1}`, `u=g^2`.

Then

`S_n={s,t,t^{-1},gtg^{-1},gt^{-1}g^{-1},g^2,g^{-2}}`

has seven distinct nonidentity labels, generates `SL_n(Z)`, and its Cayley graph has the displayed gap `>1/100`.

This lowers the concrete higher-rank-lattice degree from 15 to 7 and improves the certified gap by two orders of magnitude.

The structural hypothesis can then be weakened away from a single involution supplement.

**Theorem B (arbitrary finite symmetric supplement).** Suppose `Gamma` contains `L=<t,g> ~= C_3*Z`, and let `B` be a finite symmetric set of cardinality `b>=1`, disjoint from the block generators below, such that `Gamma=<B,t>`. For any integer `N>=b+6`, define

`t_j=g^j t g^{-j}` for `0<=j<N`, `u=g^N`,

and

`S=B union {t_j,t_j^{-1}:0<=j<N} union {u,u^{-1}}`.

Then

`boxed(p_c(Cay(Gamma,S)) < 1/(2N-3) < 1/(2N-4) < p_u(Cay(Gamma,S)))`

and therefore

`boxed(p_u-p_c > 1/((2N-4)(2N-3))).`

At the coarse endpoint `N=b+6`, this gives degree `3b+14`,

`p_c<1/(2b+9)`, `p_u>1/(2b+8)`.

Thus the demonstrated mechanism is not tied to a complement of one involution.

**Original-problem delta:** universal T09 is still OPEN. The source-level restricted scope expands from degree-15 power-thickened free-core graphs to degree-7 higher-rank-lattice Cayley graphs built from a torsion free-product kernel, together with an arbitrary-finite-supplement theorem.

**Mechanism delta:** the new ingredients are (i) finite-index Reidemeister--Schreier amplification `C_3*Z -> (* C_3)*Z`, (ii) a positive-weight Schur estimate for the torsion-block adjacency, and (iii) factor-cluster branching using the exact triangle susceptibility and line susceptibility. These are connected all the way to `p_c` and `p_u`.

## 2. Compact handoff and preserved Benjamini--Schramm history

The controlling policy is `operations/PROGRESS20_2026-09-20.md`; LIVE20 assigns NM11 to T09 at `proofnet24/NM13-11/progress-percolation/`. No POSTED exclusion is reopened.

Preserved earlier Benjamini--Schramm routes include finite-set escape plus BK/last-exit, killed-SAW and susceptibility-weighted boundary energy, global `ell^2` SAW growth, scalar nonbacktracking/product stress tests, quotient/fibre-shell comparisons, and fixed-endpoint bridge criteria. Several of those produced useful inequalities but never completed a `p_c`-to-`p_u` transfer and remain mechanism history rather than source progress.

The September continuation then obtained complete restricted transfers for explicit `SL_3(Z)`, free-core, `T_6 x C_3`, S-arithmetic, Rattaggi product-lattice, free-augmentation, nonfree power-thickening, and factor-branching families. The immediately preceding run lowered the dependent-power endpoint to rank three. This invocation follows its stated next attack and changes the subgroup block itself rather than polishing the same power constants.

No unchanged-run recovery rule is triggered.

## 3. Finite-index kernel: one `C_3*Z` pair produces arbitrarily many triangle factors

Let

`L=<t,g | t^3=1> ~= C_3 * Z`,

with `g` generating the infinite cyclic free factor. Fix `N>=2` and define

`phi_N:L -> Z/N`, `phi_N(g)=1`, `phi_N(t)=0`.

Let `K_N=ker(phi_N)`. Choose Schreier transversal

`1,g,...,g^{N-1}`.

Reidemeister--Schreier rewriting gives the kernel generators

`t_j=g^j t g^{-j}` for `0<=j<N`,

and one generator

`u=g^N`.

The sole relator family is `t_j^3=1`; no relator involves `u`. Hence

`boxed(K_N ~= (*_{j=0}^{N-1} C_3) * Z).`                 (3.1)

The standard symmetric block generating set is

`T_N={t_j,t_j^{-1}:0<=j<N} union {u,u^{-1}}`,

of cardinality `2N+2`.

For `N=2`, this is exactly `C_3*C_3*Z` with degree six before the ambient involution is adjoined.

## 4. A weighted Schur bound for the block adjacency

Let `A_N` be the adjacency operator of `Cay(K_N,T_N)`. Every nontrivial element of `K_N` has a unique reduced free-product normal form alternating between nontrivial syllables from the `C_3` factors and from `<u> ~= Z`.

Fix positive `r,sigma`. Give a reduced word `w` the weight

`omega(w)=r^(number of C_3 syllables) * sigma^(sum of absolute Z exponents)`.

When the last syllable of `w` is in a `C_3` factor, the two generators in that same factor contribute weight ratios `1` and `r^{-1}` (one changes the nontrivial element inside the factor; the other cancels the factor syllable), the other `N-1` triangle factors contribute `2(N-1)r`, and the two `u`-edges contribute `2 sigma`. Thus

`(A_N omega)(w)/omega(w) <= 1+r^{-1}+2(N-1)r+2 sigma`.   (4.1)

When the last syllable is in the `Z` factor, all triangle generators append a syllable and contribute `2Nr`, while multiplication by `u^{+-1}` contributes `sigma+sigma^{-1}`. Hence

`(A_N omega)(w)/omega(w) <= 2Nr+sigma+sigma^{-1}`.        (4.2)

At the identity the ratio is `2Nr+2sigma`. Therefore the weighted Schur test for a symmetric nonnegative kernel gives

`||A_N|| <= max{1+r^{-1}+2(N-1)r+2sigma,
                 2Nr+sigma+sigma^{-1},
                 2Nr+2sigma}.`                          (4.3)

For completeness, the Schur implication follows directly from `2ab <= a^2 q + b^2/q`: applying this on each undirected edge with `q=omega(y)/omega(x)` bounds `<f,A_N f>` by the supremum in (4.3) times `||f||_2^2`.

Two specializations will be used.

### Sharp `N=2` specialization

Take

`r=1/2`, `sigma=sqrt(2)-1`.

Since `sigma^{-1}=sqrt(2)+1`, both (4.1) and (4.2) equal `2+2sqrt(2)`, while the identity ratio is smaller. Thus

`boxed(||A_2|| <= 2+2sqrt(2)).`                          (4.4)

### Uniform all-N specialization

Take `r=sigma=1/2`. Then (4.1) is `N+3`, (4.2) is `N+3`, and the identity ratio is `N+1`. Hence

`boxed(||A_N|| <= N+3).`                                 (4.5)

No free-probability formula is being assumed here; (4.4)--(4.5) are elementary operator bounds proved above.

## 5. Critical side of Theorem A: exact factor-cluster branching

Work first inside

`K_2=C_3^{(0)} * C_3^{(1)} * Z`.

Explore iid bond percolation by factor cosets. A particle whose reduced prefix ends in one factor exposes the open cluster of its seed in each of the other factor cosets. Every non-seed vertex in such a cluster becomes a child of that factor type. Distinct factor cosets reached by reduced prefixes have disjoint edge sets except at their seed vertices, by free-product normal form; therefore offspring vectors of distinct particles are independent. Dependencies among siblings within one factor cluster are harmless. This is an honest multitype Galton--Watson subprocess of percolation.

For a triangle factor `C_3` with its two nonidentity generators, the probability that a specified non-seed vertex is connected to the seed equals

`p+(1-p)p^2 = p+p^2-p^3`.

Hence its expected number of non-seed cluster vertices is

`mu_C(p)=2(p+p^2-p^3)`.                                  (5.1)

For the standard Cayley line of `Z`, the expected number of non-seed vertices in the open seed cluster is

`mu_Z(p)=2 sum_{k>=1} p^k = 2p/(1-p)`.                   (5.2)

Aggregate the two identical triangle types into one `C` type. The mean offspring matrix for types `(C,Z)` is

`M(p)=[[mu_C,mu_Z],[2mu_C,0]]`.

Its Perron eigenvalue exceeds one exactly when

`mu_C(p)(1+2mu_Z(p))>1`.                                 (5.3)

At `p=21/100`, exact arithmetic gives

`mu_C=244839/500000`, `mu_Z=42/79`,

and

`mu_C(1+2mu_Z)-1 = 408757/39500000 >0`.                  (5.4)

Thus the branching process is supercritical at `21/100`. Since the left side of (5.3) is continuous for `p<1`, it remains supercritical at some `p'<21/100`; consequently

`boxed(p_c(Cay(K_2,T_2))<21/100).`                       (5.5)

The same subgraph sits inside the ambient graph of Theorem A, so

`boxed(p_c(G)<21/100).`                                  (5.6)

This critical-side mechanism is not claimed as a new general theory of free products: Kozakova, arXiv:math/0611668, already determines `p_c` of free products through factor cluster expectations. The source-level advance here is the specific finite-index torsion block plus the operator/nonbacktracking transfer in an uncovered ambient fixed Cayley graph.

## 6. Uniqueness side of Theorem A: operator bound plus nonbacktracking transfer

The involution contributes one unitary translation of norm one. From (4.4),

`||A_G|| <= (2+2sqrt(2))+1 = 3+2sqrt(2)`.                (6.1)

The graph is `D=7` regular, so `Q=D-1=6` in the nonbacktracking recurrence. Use the exact rational bound

`sqrt(2)<99/70`, because `(99/70)^2-2=1/4900`.

Thus

`||A_G|| < 204/35`.                                      (6.2)

Take

`z=50/11`.

Then `z^2>6`, and the exact root-test margin is

`z+6/z-204/35 = 71/1925 >0`.                             (6.3)

It follows that the exponential `ell^2` growth rate `beta` of the nonbacktracking walk operators is strictly smaller than `50/11`.

For completeness, if `N_n(x,y)` counts nonbacktracking walks of length `n`, the operators satisfy

`N_0=I`, `N_1=A`, `N_2=A^2-DI`,

and for `n>=3`,

`N_n=A N_{n-1}-(D-1)N_{n-2}`.

The spectral theorem reduces exponential growth to the roots of

`r^2-lambda r+Q=0`, `|lambda|<=||A||`.

For `z>sqrt(Q)`, the inequality `z+Q/z>||A||` gives `beta<z`.

Every open connection contains a shortest open path, which is nonbacktracking, so entrywise

`T_p(x,y) <= sum_{n>=0} p^n N_n(x,y)`.

Therefore the connectivity kernel is bounded on `ell^2` whenever `p beta<1`, and

`p_{2->2} >= 1/beta > 11/50`.                            (6.4)

Finally `p_{2->2}<=p_u`: if `p>p_u`, uniqueness of the infinite cluster and FKG imply

`T_p(x,y)>=theta(p)^2>0`

for every `x,y`; such a kernel cannot map a delta mass into `ell^2` on an infinite graph. Hence

`boxed(p_u(G)>11/50).`                                   (6.5)

Combining (5.6) and (6.5),

`boxed(p_c(G)<21/100<11/50<p_u(G))`,

and

`boxed(p_u(G)-p_c(G)>1/100).`                            (6.6)

This completes Theorem A.

## 7. Concrete uncovered family: degree-7 Cayley graphs of `SL_n(Z)`, `n>=5`

A completed `(2,3)`-generation result for integer matrix groups states that `SL_n(Z)` is generated by an involution `s` and an element `t` of order three iff `n>=5`; see M. A. Vsemirnov, *On (2,3)-generation of matrix groups over the ring of integers, II*, St. Petersburg Math. J. 32 (2021), and the earlier generation literature.

Fix `n>=5` and such a pair `(s,t)`. The cyclic subgroup `<t>` has trivial intersection with the center of `SL_n(R)` because the center visible in `SL_n(Z)` has no nontrivial element of order three in this range. Theorem 3.23 of Janssens--Temmerman--Thilmany, arXiv:2510.23957, applies to Zariski-dense subgroups of inner real forms of `SL_n`/`GL_n` and gives an infinite-order `g in SL_n(Z)` for which the canonical map

`<t> * <g> -> <t,g>`

is an isomorphism. Thus `<t,g> ~= C_3*Z`.

Apply Section 3 with `N=2`. Set

`t_0=t`, `t_1=gtg^{-1}`, `u=g^2`.

Then `<t_0,t_1,u> ~= C_3*C_3*Z`. Since `s,t` already generate `SL_n(Z)`, the seven-element symmetric set

`S_n={s,t,t^{-1},gtg^{-1},gt^{-1}g^{-1},g^2,g^{-2}}`

generates the ambient group. Free-product normal form shows the six block labels are pairwise distinct and nontrivial; the involution cannot equal a block label because `C_3*C_3*Z` has no element of order two. Therefore the Cayley graph is simple and 7-regular.

Theorem A yields, uniformly for every `n>=5`,

`boxed(p_c(Cay(SL_n(Z),S_n))<0.21<0.22<p_u(Cay(SL_n(Z),S_n)))`,

with

`boxed(p_u-p_c>0.01).`                                   (7.1)

These higher-rank lattices contain `Z^2`, so their Cayley graphs are not Gromov-hyperbolic. Haettel's hyperbolic-rigidity theorem (arXiv:1607.02004) states that every action of a higher-rank lattice on a Gromov-hyperbolic space is elementary, excluding acylindrical hyperbolicity as well. Thus Hutchcroft's hyperbolic theorem and the Choi--Seo all-Cayley theorem for acylindrically hyperbolic groups do not subsume this family.

Pak--Smirnova-Nagnibeda already prove that every finitely generated nonamenable group has *some* generating set with a nonuniqueness phase, so no new group-level existence claim is made. The candidate advance is the explicit degree-7 fixed generating-set family and the quantified transfer.

## 8. Weakening Theorem A to an arbitrary finite symmetric supplement

Now prove Theorem B. Keep `L=<t,g> ~= C_3*Z`, choose `N>=2`, and use the kernel `K_N` from Section 3. Let `B` be symmetric, `|B|=b`, disjoint from `T_N`, and assume `Gamma=<B,t>`. Since `t=t_0` belongs to `T_N`, the set

`S=B union T_N`

generates `Gamma`. Its degree is

`D=2N+2+b`, `Q=D-1=2N+b+1`.                             (8.1)

### Critical side

Ignore the `Z` factor and all `B`-edges. The `N` triangle factors generate the free product `*_{j=0}^{N-1} C_3`. Factor-cluster branching has `N` types, zero diagonal, and every off-diagonal mean equal to `mu_C(p)` from (5.1). Its Perron eigenvalue is

`(N-1)mu_C(p)`.

Set

`p_0=1/(2N-3)`.

For `0<p<1`,

`mu_C(p)=2(p+p^2-p^3)>2p`.

Therefore

`(N-1)mu_C(p_0) > 2(N-1)/(2N-3) >1`.                   (8.2)

Continuity again gives supercriticality at some `p<p_0`, hence

`boxed(p_c(G)<1/(2N-3)).`                               (8.3)

### Operator / uniqueness side

By (4.5), `||A_{K_N}||<=N+3`. The supplement is a sum of `b` unitary translations, so

`||A_G||<=N+b+3`.                                       (8.4)

Assume now

`N>=b+6`.

Take

`z=2N-4`.

First, `b<=N-6`, so

`Q=2N+b+1<=3N-5`,

and for `N>=6`, `(2N-4)^2>3N-5`; hence `z>sqrt(Q)`.

Second,

`z+Q/z-(N+b+3)
 = N-b-7 + (2N+b+1)/(2N-4)`.                            (8.5)

If `N-b=6`, the right side is

`-1+(3N-5)/(2N-4)=(N-1)/(2N-4)>0`.

If `N-b>=7`, the first term in (8.5) is nonnegative and the fraction is positive. Thus in all cases `N>=b+6`,

`z+Q/z>||A_G||`.

The nonbacktracking transfer of Section 6 gives

`boxed(p_u(G)>1/(2N-4)).`                               (8.6)

Combining (8.3) and (8.6),

`boxed(p_u-p_c > 1/(2N-4)-1/(2N-3)
                =1/((2N-4)(2N-3))>0).`                 (8.7)

At `N=b+6`, the degree is `3b+14` and

`p_c<1/(2b+9)`, `p_u>1/(2b+8)`.

For example, `b=1,N=7` gives degree 17 and the coarse universal-supplement certificate

`p_c<1/11<1/10<p_u`, `p_u-p_c>1/110`.

This completes Theorem B and removes the one-involution-complement hypothesis at the mechanism level.

## 9. Current source scopes checked 20 September 2026

This is a bounded present-status check, not a worldwide novelty certificate.

- **Hutchcroft, arXiv:1804.10191, current v3, 26 March 2019.** The abstract states `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs; v3 changed metadata only. This does not cover higher-rank `SL_n(Z)` Cayley graphs. URL: https://arxiv.org/abs/1804.10191
- **Hutchcroft--Pan, arXiv:2409.12283, current v1, 18 September 2024.** This is an endpoint-`p_u` subgroup-relativization theorem, including nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth, plus a co-heredity result. It does not give the fixed-graph quantitative gap here. URL: https://arxiv.org/abs/2409.12283
- **Terlov--Timar, arXiv:2502.02560, current v2, 14 September 2025.** This treats weighted/level amenability and a relaxed weighted `p_h<p_u` conjecture, not the ordinary unimodular fixed-Cayley target. URL: https://arxiv.org/abs/2502.02560
- **Choi--Seo, arXiv:2508.08932.** Their all-Cayley result is for acylindrically hyperbolic groups. Higher-rank lattices are excluded by hyperbolic-action rigidity.
- **Janssens--Temmerman--Thilmany, arXiv:2510.23957, Theorem 3.23.** This supplies the required infinite-order ping-pong partner for the finite order-three subgroup in the `SL_n(Z)` application. URL: https://arxiv.org/abs/2510.23957
- **Kozakova, arXiv:math/0611668.** Free-product critical probabilities in terms of factor cluster expectations are already known. Accordingly, the factor-branching identity itself is not advertised as novel. URL: https://arxiv.org/abs/math/0611668
- **Haettel, arXiv:1607.02004.** Every hyperbolic-space action of a higher-rank lattice is elementary, excluding the acylindrically-hyperbolic all-Cayley scope for the concrete application. URL: https://arxiv.org/abs/1607.02004

A bounded search did not locate this finite-index `C_3*C_3*Z` degree-7 percolation comparison or the finite-supplement theorem. That is only negative search evidence. External priority remains **UNVERIFIED**.

## 10. Exact checker and actual archived output

Checker source:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T12-50-00+0300__t09-triangle-kernel-degree7-check.py`

created at commit

`3c61318d39244f9dace06c2b4310675264e40a8c`.

Actual stdout from the executed exact-rational calculation was archived as

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T12-50-00+0300__t09-triangle-kernel-degree7-check.out`

at commit

`baeb2519628f974fcc15173b1fd59ddd3ab93af2`.

The output is:

```text
SPECIAL_N2
mu_C(21/100)= 244839/500000
mu_Z(21/100)= 42/79
branch_margin= 408757/39500000 0.010348278481012657
sqrt2_upper= 99/70 square_margin= 1/4900
A_total_upper= 204/35
z= 50/11 z2_minus_Q= 1774/121
root_margin= 71/1925 0.036883116883116886
certified_gap= 1/100 0.01

GENERAL_N_GE_B_PLUS_6
verified exact inequalities for 0<=b<=100 and b+6<=N<b+40

B1_N7_COROLLARY
degree= 17
pc< 1/11
pu> 1/10
gap> 1/110 0.00909090909090909
ALL_EXACT_CHECKS_PASS
```

The finite range loop is only a regression check; Theorem B itself is proved symbolically in Section 8 for all `b>=1,N>=b+6`.

## 11. Residual obstruction and next attack

The new subgroup block is genuinely nonfree and the degree-7 ambient graphs are substantially less engineered than the preceding power-thickened free-basis families, but the construction still imports a ping-pong partner `g`. Unknown is not zero: this run does **not** prove `p_c<p_u` for the standard elementary-matrix generating set of `SL_n(Z)`, nor for an arbitrary fixed Cayley graph of a higher-rank lattice.

The next useful weakening is therefore not another finite-index amplification. Two materially different routes remain:

1. apply the weighted-Schur/factor-cluster template to a torsion or parabolic block already present in a natural higher-rank presentation, with no added ping-pong generator; or
2. execute a colored nonbacktracking recurrence for natural elementary-matrix generator types, avoiding the scalar triangle-inequality loss on the `p_u` side.

If either route stalls for the mandated number of substantive runs, switch target as prescribed while preserving this theorem and ownership.

## 12. ledger_delta

```yaml
ledger_delta:
  worker: NM13-11
  parent: T09
  status: PARTIAL
  candidate_status: CANDIDATE_FULL_RESTRICTED_PENDING_REVIEW
  universal_target_before: OPEN
  universal_target_after: OPEN
  source_scope_before: "degree-15 doubled-power Cayley graphs of SL_n(Z), n>=5, with gap >1e-4; arbitrary power pair degree 19"
  source_scope_after: "degree-7 Cayley graphs of SL_n(Z), n>=5, from a C3*C3*Z finite-index kernel, gap >1/100; plus arbitrary finite symmetric supplement theorem"
  concrete_group_family: "SL_n(Z), n>=5"
  degree7_endpoint:
    degree: 7
    pc_bound: "<21/100"
    pu_bound: ">11/50"
    certified_gap: ">1/100"
  general_supplement_theorem:
    supplement_size: b
    kernel_parameter: "N>=b+6"
    degree: "2N+2+b"
    pc_bound: "<1/(2N-3)"
    pu_bound: ">1/(2N-4)"
    certified_gap: ">1/((2N-4)(2N-3))"
  mechanism_advance: "Reidemeister-Schreier finite-index amplification C3*Z -> (*_N C3)*Z; weighted Schur operator bound; exact triangle/line factor-cluster branching; complete nonbacktracking transfer"
  prior_attempts_preserved: "finite-set escape; BK/last-exit; killed-SAW; susceptibility boundary energy; global ell2-SAW; scalar NB/product; quotient/fibre-shell; fixed-endpoint bridge; prior subgroup/free-core/triangle/S-arithmetic/Rattaggi/power-thickening/factor-branching transfers"
  known_overlap_not_claimed_new: "Kozakova free-product pc factor-susceptibility theory; Pak-Smirnova-Nagnibeda group-level existence of some favorable generating set"
  unchanged_substantive_runs: 0
  failed_recoveries: 0
  checker_commit: 3c61318d39244f9dace06c2b4310675264e40a8c
  output_commit: baeb2519628f974fcc15173b1fd59ddd3ab93af2
  independent_review: NOT_YET_DONE
  external_priority: UNVERIFIED
  next_attack: "natural higher-rank torsion/parabolic block without ping-pong engineering, or colored nonbacktracking on a natural elementary-matrix generating set"
```
