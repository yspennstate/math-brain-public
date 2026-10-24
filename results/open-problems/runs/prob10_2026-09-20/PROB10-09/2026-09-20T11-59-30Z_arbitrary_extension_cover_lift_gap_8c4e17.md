Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is not authenticated by an exposed scheduler/model selector.**

# PROB10-09 — arbitrary-extension cover-lift criterion and a genuinely noncentral infinite-kernel gap

Status: **PARTIAL for the Benjamini–Schramm source problem.** This run proves a complete restricted structural criterion that removes the central/abelian-kernel hypothesis from the preceding R20 operator argument, and gives an explicit noncentral semidirect-product Cayley graph with a certified positive `p_u-p_c` lower bound. The proof has an executed exact-arithmetic/algebraic self-check, but **no independent other-track validation**. No source closure or worldwide novelty claim is made.

## 0. Frozen source, R20 handoff, consumed history, aliases, and ownership boundary

The frozen target remains exactly the owner-specified original Cayley-graph problem:

> For iid **BOND** percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

No nontransitive planar SITE-percolation problem is substituted. Known nonamenable Gromov-hyperbolic quasi-transitive cases are prior art, not a new result.

The required pre-refocus R20 handoff was re-read rather than duplicated:

`runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`

blob `6e1b9e54cbc01461d32b523854c3bd82e50bfd04`.

It preserves the actual pre-PROB10 R20 state and artifacts: I0100/Paley remains OPEN/PARTIAL with exact `p_max=1213`; KNSV-2026-LOOPY-U remains OPEN/PARTIAL with its restricted exact diagnostics; BMO-2025-PUSHING-DELTA was the final mathematical R20 target before terminal wait, remains OPEN/PARTIAL with exact `n_all=9`, and retains `artifacts/R20/bmo_n9_witness_exact.cpp` and `artifacts/R20/bmo_n9_exact_check.out`. Those historical canonical claims are not edited here.

Consumed current PROB10 evidence before the new proof:

- `operations/PROB10_2026-09-20.md` on current `master`;
- current `POSTED.md`, whose exclusion registry does not close the unrestricted Benjamini–Schramm target;
- source alias `D0061 = lyons_nonamenable_2000::conjecture_3.8_(benjamini-schramm_1996)`, still a HARD/open source rather than a closed canonical theorem;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`, blob `ee8bde8735e84ff75d3a625fed61e9bafbefd64f`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md`, blob `d94127841f3b335a32b7936b86d8dee7a6b8d093`;
- immediate R20 predecessor `runs/prob10_2026-09-20/PROB10-09/2026-09-20T10-59-30Z_higher_rank_abelian_central_kernel_gap_7d4b2e.md`;
- newest neighboring T09 report located before writing this report, `proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T13-50-00+0300__t09-pure-triangle-supplement-gap.md`.

The June archive's normalized finite-set escape, BK finite-volume/last-exit boundary dichotomy, killed-SAW criteria, susceptibility/boundary-energy route, global `ell^2` SAW growth, scalar nonbacktracking/product stress tests, quotient/fibre-shell comparisons, and fixed-endpoint bridge attempts remain consumed history. None is relabeled as new.

**Collision boundary.** NM13-11 currently owns the distinct free-core / torsion-block / higher-rank-lattice subgroup lane, including `SL_n(Z)`, S-arithmetic, triangle-fibre, power-thickening, factor-branching, and the new pure-triangle supplement theorem. R20 stays on the **quotient-cover / extension operator** lane. No NM13 theorem, metric, or claim is overwritten or absorbed.

No schedule, cadence, enabled state, email, Drive, public posting, POSTED registry, canonical claim file, or neighboring ownership state is changed.

## 1. Current source/prior-art screen

The source distinctions were refreshed on 20 September 2026.

1. Hutchcroft, `https://arxiv.org/abs/1804.10191`, proves `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs. It is a proper special case of the frozen target.
2. Hutchcroft, `https://arxiv.org/abs/1904.05804`, develops the `L^2` threshold `p_{2->2}` and records that the `L^2` boundedness condition implies the older nonuniqueness conjecture.
3. Hutchcroft–Pan, `https://arxiv.org/abs/2409.12283`, prove subgroup-relativized results at `p_u`, including nonuniqueness at `p_u` when there is an amenable `wq`-normal subgroup of exponential growth. The normal kernel in the concrete example below is `Z^2`, of polynomial growth, so that displayed corollary is not the mechanism used here.
4. Terlov–Timár, `https://arxiv.org/abs/2502.02560`, treat weighted amenability and heavy-cluster thresholds rather than resolving the frozen universal fixed-Cayley statement.
5. Choi–Seo, `https://arxiv.org/abs/2508.08932`, prove a nonuniqueness phase on every Cayley graph of every acylindrically hyperbolic group. The concrete group below has an infinite amenable normal subgroup `Z^2`, whereas an acylindrically hyperbolic group has finite amenable radical; see Osin's survey discussion of the finite/amenable radical. Hence that all-Cayley theorem does not cover the concrete example below.
6. Pak–Smirnova-Nagnibeda (2000) and Juschenko–Nagnibeda, `https://arxiv.org/abs/1206.2183`, show existence of *some* generating set with a nonuniqueness phase for broad classes, including every finitely generated nonamenable group in the former result and groups with an infinite normal subgroup and nonamenable quotient in the latter. Therefore no group-level existence novelty is claimed here. The new repository-level statement is about the specified horizontal-lift generating set and gives an explicit threshold certificate.
7. Żuk, *A remark on the norm of a random walk on surface groups* (Colloq. Math. 72 (1997), 195–206), proves for the standard genus-`g` surface Cayley graph that the simple-random-walk operator norm is at most `1/sqrt(g)`. Thus the standard adjacency norm is at most `4 sqrt(g)`.
8. A fresh paper submitted 10 September 2026, `https://arxiv.org/abs/2609.11845`, still discusses the classical Benjamini–Schramm nonamenability/nonuniqueness conjecture as open in its general quasi-transitive form. This is fresh status evidence, not a proof that no other result exists.

A bounded search did not locate the exact arbitrary-extension horizontal-cover criterion combined with the fixed semidirect surface example below. This is **negative search evidence only**, not a priority certificate.

## 2. Metrics — source, structural scope, and auxiliary mechanism kept separate

### Parent source metric

Before: **OPEN/PARTIAL**.

After: **OPEN/PARTIAL**.

The universal all-nonamenable-group/all-Cayley theorem is not proved.

### Structural-scope metric

Before: the strongest R20 horizontal-lift theorem required a **finitely generated abelian central kernel** and used a Pontryagin-dual magnetic decomposition.

After: the kernel may be **arbitrary**. More precisely, for any surjective group homomorphism

`pi: Gamma -> Q`

and any inverse-compatible horizontal lift of a finite symmetric quotient generating set that generates all of `Gamma`, the lifted adjacency norm is bounded by the quotient adjacency norm. Combined with a visible free quotient subset and the nonbacktracking transfer, this gives a strict percolation-gap criterion independent of centrality, abelianness, amenability, or the extension cocycle.

This is the complete scope of the proved structural criterion in this run; the full-generation hypothesis is essential and is explicitly tested below.

### Frozen new graph quantitative metric

Freeze the genus-two surface quotient `Q=Gamma_2`, the infinite-order action

`M = [[0,-1],[1,3]] in SL_2(Z)`,

and the semidirect product

`Gamma = Z^2 semidirect_alpha Gamma_2`,

where `alpha(a_1)=M` and `alpha(b_1)=alpha(a_2)=alpha(b_2)=I`. Use the eight inverse-closed horizontal directions specified in Section 5 and **no separately adjoined kernel generator**.

Before: **UNMEASURED** in the genuinely noncentral infinite-kernel R20 lane.

After:

`p_c <= 1/5`,

`p_{2->2} >= 1/(1+2 sqrt(2)) = (2 sqrt(2)-1)/7`,

and therefore

`p_u-p_c >= (10 sqrt(2)-12)/35 > 61/1000`.

Thus the certified source-family metric is

`boxed(p_u-p_c > 0.061)`

for this frozen graph.

### Auxiliary mechanism delta

Scalar Fourier characters are unnecessary. The correct invariant is the quotient **Hilbert-fibre cover structure**: every lifted generator acts between adjacent quotient fibres by a unitary map, and fibrewise triangle inequality directly dominates the extension adjacency by the scalar quotient adjacency. This is the matrix-/crossed-product mechanism the earlier central-extension report identified as missing.

## 3. Idea-before-code, negation test, and three distinct methods

The new mathematical route was persisted before any new checker at

`artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T11-52-00Z_noncentral_cover_lift_idea.md`

creation commit `7904ca6bd2032f5daaf8ae786deef2dc2ee7af3b`.

That note used a first noncentral matrix example. During the mathematical pass, the explicit matrix was strengthened to the hyperbolic/infinite-order matrix used below, eliminating the possibility that the example is merely virtually central. The structural idea itself is unchanged and predates both exact checkers.

Three genuinely different routes were compared.

1. **Vector-valued cover domination — SUCCESS.** Replace scalar central Fourier fibres by `ell^2(N)`-valued quotient fibres and unitary edge transports. This proves the arbitrary-extension adjacency domination in one line after the correct fibre identification.
2. **Fourier-orbit / crossed-product decomposition — VIABLE BUT INFERIOR.** For `Z^m semidirect Q`, Fourier transforming the kernel produces an operator on `Q x T^m` in which quotient generators move characters by the dual action. A Schur estimate is possible, but the direct Hilbert-fibre norm argument is strictly cleaner and works for nonabelian kernels as well.
3. **Subgroup-only gap transfer — REJECTED.** Proving a gap in a proper horizontal subgroup and then adding generators to recover the full group does not preserve the needed inequality from the elementary monotonicities alone: `p_c` decreases under added edges, while no matching monotonicity for `p_u` keeps the strict comparison. This is the exact obstruction already recorded in the central-kernel lane.

**Negation test.** Full horizontal generation is not automatic. A second exact semidirect example in the checker has an orbit lattice of determinant `2`, so its horizontal relator values span only an index-two sublattice of the kernel. In that case the same operator domination holds on each component, but the horizontal label graph is not a connected Cayley graph of the full extension. This is an exact admissibility boundary, not a cosmetic hypothesis.

## 4. General arbitrary-extension cover-lift criterion

Let

`1 -> N -> Gamma --pi--> Q -> 1`                         (4.1)

be an arbitrary group extension. No assumption is imposed on `N`.

Let `S_Q` be a finite inverse-closed generating set of `Q`, with

`D=|S_Q|`, `rho_Q=||A_{Q,S_Q}||_{2->2}`.

Choose an inverse-compatible set `S~` of lifts, one for each element of `S_Q`, and assume

`<S~>=Gamma`.                                             (4.2)

Write `X=Cay(Gamma,S~)` and `Y=Cay(Q,S_Q)`. Assume also that `S_Q` contains `k>=2` generator pairs represented by elements `t_1,...,t_k` that freely generate `F_k` in `Q`.

Put `q=D-1` and

`beta_D(rho) = sqrt(q)` if `rho<=2 sqrt(q)`,

and

`beta_D(rho) = (rho+sqrt(rho^2-4q))/2` if `rho>2 sqrt(q)`.

**Theorem 4.1 (arbitrary-extension horizontal-cover gap criterion).** If

`beta_D(rho_Q) < 2k-1`,                                    (4.3)

then

`boxed(p_c(X) <= 1/(2k-1) < 1/beta_D(rho_Q) <= p_{2->2}(X) <= p_u(X)).`   (4.4)

In particular `p_c(X)<p_u(X)`.

### 4.1 Proof of adjacency domination with no centrality

Choose any section `sigma:Q->Gamma`. Each fibre `pi^{-1}(q)` is in bijection with `N`, and hence

`ell^2(Gamma) ~= ell^2(Q; ell^2(N))`.                       (4.5)

Fix `s in S_Q` and its lift `s~`. Right multiplication by `s~` maps the fibre over `q` bijectively onto the fibre over `qs`. Relative to the chosen section this map is represented by a unitary operator

`U(q,s):ell^2(N)->ell^2(N)`.                               (4.6)

Consequently the adjacency operator of `X` has the block form

`(A_X f)(q)=sum_{s in S_Q} U(q,s) f(qs)`.                  (4.7)

Define the scalar nonnegative function

`F(q)=||f(q)||_{ell^2(N)}`.

The triangle inequality in the Hilbert fibre gives pointwise

`||(A_X f)(q)|| <= sum_s ||f(qs)|| = (A_Y F)(q)`.          (4.8)

Squaring and summing over `q` yields

`||A_X f||_2 <= ||A_Y F||_2 <= rho_Q ||F||_2 = rho_Q ||f||_2`.

Therefore

`boxed(||A_X||_{2->2} <= rho_Q).`                          (4.9)

This proof uses neither commutativity nor amenability of `N`; it is a pure labelled-cover domination statement.

### 4.2 Critical side: the free subset lifts faithfully

Let `t~_1,...,t~_k` be the selected lifts. If a nonempty freely reduced word in `t~_i^{+-1}` were the identity in `Gamma`, projecting by `pi` would give the corresponding nonempty freely reduced word equal to the identity in `Q`, contradicting freeness of `t_1,...,t_k`.

Hence the lifts freely generate `F_k`. The edges of `X` belonging to these `k` pairs contain the standard `2k`-regular tree through each coset. Bond percolation on that tree has threshold `1/(2k-1)`, so

`boxed(p_c(X)<=1/(2k-1)).`                                (4.10)

### 4.3 Nonbacktracking transfer

For a `D`-regular simple Cayley graph, let `N_n` denote the length-`n` nonbacktracking-walk operator. Then

`N_0=I`, `N_1=A_X`, `N_2=A_X^2-DI`,

and for `n>=3`,

`N_n=A_X N_{n-1}-(D-1)N_{n-2}`.                           (4.11)

For a spectral value `lambda` of `A_X`, the characteristic equation is

`u^2-lambda u+q=0`, `q=D-1`.

Using (4.9) and the spectral theorem gives

`limsup_n ||N_n||^(1/n) <= beta_D(rho_Q)`.                (4.12)

Every open connection has a shortest open path, and every shortest path is nonbacktracking. Thus, entrywise,

`T_p(x,y)=P_p(x<->y) <= sum_{n>=0} p^n N_n(x,y)`.         (4.13)

If `p beta_D(rho_Q)<1`, the right-hand operator series converges in `ell^2` operator norm, so `T_p` is `ell^2` bounded. Hence

`p_{2->2}(X) >= 1/beta_D(rho_Q)`.                         (4.14)

Finally `p_{2->2}<=p_u` on an infinite transitive graph: for `p>p_u`, uniqueness of the infinite cluster and FKG give a positive uniform lower bound `T_p(x,y)>=theta(p)^2`; such a kernel cannot be bounded on `ell^2`. Combining (4.10), (4.14), and (4.3) proves Theorem 4.1. ∎

## 5. A genuinely noncentral, infinite-order semidirect surface family

Let

`Q=Gamma_2=<a_1,b_1,a_2,b_2 | [a_1,b_1][a_2,b_2]=1>`     (5.1)

with the standard eight-element inverse-closed generating set.

Let

`M=[[0,-1],[1,3]] in SL_2(Z)`.                            (5.2)

Its determinant is `1` and trace is `3>2`, so `M` is hyperbolic and has infinite order.

Define a homomorphism

`alpha:Q->SL_2(Z)`

by

`alpha(a_1)=M`,
`alpha(b_1)=alpha(a_2)=alpha(b_2)=I`.                     (5.3)

This respects the surface relation because `[M,I][I,I]=I`.

Set

`Gamma=Z^2 semidirect_alpha Q`,                           (5.4)

with multiplication

`(x,g)(y,h)=(x+alpha(g)y,gh)`.

Put

`v=(-2,1)`, `e_1=(1,0)`, `e_2=(0,1)`.                    (5.5)

A direct calculation gives

`(M-I)v=e_1`, `M e_1=e_2`.                               (5.6)

Choose the four positive horizontal lifts

`A_1=(0,a_1)`,
`B_1=(v,b_1)`,
`A_2=(0,a_2)`,
`B_2=(0,b_2)`,                                            (5.7)

and let `S` consist of these and their inverses. Then `|S|=8`.

### 5.1 Exact generation of the whole semidirect product

Because `b_1` acts trivially on `Z^2`, the lifted commutator satisfies

`[A_1,B_1]=((M-I)v,1)=(e_1,1)`.                           (5.8)

Also `[A_2,B_2]=(0,1)`. Hence the lifted surface relator already places `(e_1,1)` in `H=<S>`.

Conjugating by `A_1` gives

`A_1(e_1,1)A_1^{-1}=(M e_1,1)=(e_2,1)`.                 (5.9)

Thus the full kernel `Z^2=<e_1,e_2>` lies in `H`. Since `v=-2e_1+e_2`, multiplying `B_1` by an appropriate kernel element yields the pure quotient lift `(0,b_1)`. The other three positive lifts are already pure. Therefore `H` contains `Z^2` and pure lifts of all four standard quotient generators, so

`boxed(<S>=Gamma).`                                       (5.10)

The kernel is genuinely noncentral because conjugation by `A_1` sends `e_1` to `e_2 != e_1`. Moreover the action has infinite image because `M` has infinite order. In particular this is not merely a finite-action/virtually-central cosmetic perturbation of the previous central examples.

The group is nonamenable because it surjects onto the nonamenable surface group `Q`. It contains the normal subgroup `Z^2`, so it is not word-hyperbolic; and its infinite amenable normal subgroup rules out acylindrical hyperbolicity by the finite-amenable-radical theorem.

### 5.2 Quantitative strict gap

By Magnus' Freiheitssatz, deleting one standard generator from the genus-two one-relator presentation leaves a free subgroup of rank three. Thus the standard quotient generating set contains `k=3` free generator pairs.

Żuk's theorem gives

`rho_Q <= 4 sqrt(2)`.                                    (5.11)

Here `D=8`, so `q=7`. Since `(4 sqrt(2))^2=32>28`,

`beta_8(4 sqrt(2))`
`=(4 sqrt(2)+sqrt(32-28))/2`
`=1+2 sqrt(2)`.                                          (5.12)

And

`1+2 sqrt(2)<5=2k-1`.                                    (5.13)

Theorem 4.1 therefore gives

`p_c(Cay(Gamma,S)) <= 1/5`,                              (5.14)

and

`p_u(Cay(Gamma,S)) >= p_{2->2} >= 1/(1+2 sqrt(2))`
`=(2 sqrt(2)-1)/7`.                                      (5.15)

Subtracting,

`p_u-p_c >= (10 sqrt(2)-12)/35`.                         (5.16)

Finally

`(10 sqrt(2)-12)/35 > 61/1000`,                          (5.17)

because this is equivalent to `10000 sqrt(2)>14135`, and squaring the positive sides gives exact margin

`200000000-14135^2 = 201775>0`.

Thus

`boxed(p_u-p_c>61/1000).`                                (5.18)

This is a **restricted fixed-Cayley theorem**, hence PARTIAL for the parent conjecture.

## 6. Exact negation test: why generation is a real hypothesis

The cover norm inequality (4.9) itself survives if the horizontal labels generate a proper subgroup, but then the resulting graph is disconnected as a graph on the full group and is not the requested connected Cayley graph.

The exact checker includes a concrete failure mode. Let

`M_bad=[[0,-1],[1,0]]`, `v_bad=(1,0)`.

Then

`w_bad=(M_bad-I)v_bad=(-1,1)`,

and

`M_bad w_bad=(-1,-1)`.

These two vectors have determinant `2`, so they span an index-two sublattice of `Z^2`, not the whole kernel. This falsifies the tempting statement that any nontrivial relator displacement plus its action orbit automatically generates the full fibre.

Hence the criterion's hypothesis `<S~>=Gamma` cannot simply be deleted.

## 7. Executed tests and artifacts

The idea-before-code artifact is

`artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T11-52-00Z_noncentral_cover_lift_idea.md`

at creation commit `7904ca6bd2032f5daaf8ae786deef2dc2ee7af3b`.

A preliminary noncentral finite-action checker was retained as honest run history:

- `artifacts/prob10_2026-09-20/PROB10-09/noncentral_cover_lift_exact.py`,
- `artifacts/prob10_2026-09-20/PROB10-09/noncentral_cover_lift_exact.out`.

The stronger final frozen example uses the infinite-order hyperbolic action and is checked by

- `artifacts/prob10_2026-09-20/PROB10-09/noncentral_hyperbolic_action_exact.py`,
- `artifacts/prob10_2026-09-20/PROB10-09/noncentral_hyperbolic_action_exact.out`.

Its actual saved output is:

```
PROB10-09 NONCENTRAL HYPERBOLIC-ACTION EXACT CHECK
det_M=1
trace_M=3
w=(M-I)v=(1, 0)
Mw=(0, 1)
kernel_orbit_basis_det=1
noncentral_test_Me1_ne_e1=True
infinite_order_reason=trace_M_gt_2_for_SL2Z
gap_gt_61_over_1000_square_margin=201775
pu_gt_261_over_1000_square_margin=1153
negation_index_det=2
ALL_EXACT_CHECKS_PASS
```

This finite checker certifies only the algebra/radical core. The Hilbert-fibre domination, free-subgroup step, and nonbacktracking transfer are analytical proofs in Sections 4–5; the checker is not substituted for them.

## 8. What remains unresolved

The universal source gap is still large. The present theorem requires a quotient generating set with two quantitative properties simultaneously:

1. a visible free subset large enough to give `p_c<=1/(2k-1)`; and
2. a sufficiently small quotient adjacency norm so that `beta_D(rho_Q)<2k-1`.

An arbitrary Cayley generating set of an arbitrary nonamenable group need not visibly expose such a free subset, and nonamenable groups without nonabelian free subgroups exist. The cover domination therefore does **not** reduce the universal Benjamini–Schramm conjecture to a trivial quotient choice. It is a rigorous extension theorem for a broad mechanism, not a universal proof.

The next genuinely different in-conjecture route would have to replace the visible-free-tree `p_c` witness by a quotient invariant available in groups without free subgroups (for example an exact factor-cluster/subgroup branching witness or a certified isoperimetric exploration) while retaining the cover/operator domination on the `p_u` side. Merely restating `p_c<p_{2->2}` as the remaining lemma would not be progress.

## 9. Validation and verdict

- Complete written proof for the new structural criterion: **YES, self-check**.
- Complete written proof for the frozen semidirect example: **YES, self-check**.
- Exact finite-core checker executed/saved: **YES, `ALL_EXACT_CHECKS_PASS`**.
- Current prior-art screen: **YES, bounded only**.
- Independent other-track audit: **NO**.
- Source closure: **NO**.
- Parent Benjamini–Schramm status: **OPEN/PARTIAL**.
- Schedule/email/Drive/public-posting/canonical-claim changes: **NONE**.

The source-level before/after metric is therefore unchanged (`OPEN/PARTIAL -> OPEN/PARTIAL`), while the structural theorem advances from central abelian fibres to arbitrary extension kernels, and the frozen noncentral infinite-order semidirect graph advances from UNMEASURED to the certified quantitative gap `p_u-p_c>61/1000`.
