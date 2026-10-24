Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — operator-sparse generator perturbations; Rattaggi k=4,...,8 fixed-graph gaps

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorem below; universal T09 remains OPEN.** The restricted proof is complete as written and has an exact-rational self-check, but has not had independent review. External priority of the exact fixed generating sets is **UNVERIFIED** after the bounded search recorded below.

## 1. Original problem: before/after source-level scope

Frozen parent problem: for iid bond percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove

`p_c(G) < p_u(G)`.

The universal statement remains **OPEN**.

### Before this run

The latest NM13-11 report proved a perturbative stability theorem for Rattaggi's `(12,8)`-group `Sigma`: starting from the standard Cayley graph

`Cay(Sigma,S0) ~= T_12 square T_8`,

one could add **up to three arbitrary new inverse generator pairs** and retain a certified positive gap. The weakest endpoint there was `k=3`, with

`p_c < 3/50 = 0.06`, `p_u > 0.0609`, hence `p_u-p_c>0.0009`.

No theorem in the track covered four or more added pairs on this same non-hyperbolic, non-acylindrically-hyperbolic ambient group.

### After this run

I prove an operator-sparse perturbation criterion and apply it to explicit new generating sets on the **same Rattaggi group**. Let

`S0={a_1^{+-1},...,a_6^{+-1},b_1^{+-1},...,b_4^{+-1}}`

be Rattaggi's standard `(12,8)` generating set. For `j>=1` put

`c_j = a_1^j a_2 a_1^{-j}`.

For each `4<=k<=8`, define

`G_k = Cay(Sigma, S0 union {c_1^{+-1},...,c_k^{+-1}})`.

Then:

| k | degree | certified `p_u` lower bound | common `p_c` upper bound | certified gap |
|---:|---:|---:|---:|---:|
| 4 | 28 | `p_u>323/5000=0.0646` | `p_c<7/125=0.056` | `p_u-p_c>43/5000=0.0086` |
| 5 | 30 | `p_u>31/500=0.062` | `p_c<7/125` | `p_u-p_c>3/500=0.006` |
| 6 | 32 | `p_u>299/5000=0.0598` | `p_c<7/125` | `p_u-p_c>19/5000=0.0038` |
| 7 | 34 | `p_u>29/500=0.058` | `p_c<7/125` | `p_u-p_c>1/500=0.002` |
| 8 | 36 | `p_u>113/2000=0.0565` | `p_c<7/125` | `p_u-p_c>1/2000=0.0005` |

Thus the demonstrated fixed-graph scope expands from three arbitrary added pairs to **eight explicit genuinely new added pairs**, and the added-pair hypothesis is weakened at the abstract level from cardinality alone to an operator-norm criterion that also allows many nonfree choices.

**Original-problem delta:** five additional fixed Cayley graphs `G_4,...,G_8` on the uncovered Rattaggi ambient group now have explicit strictly positive `p_u-p_c` gaps; in particular `G_8` was previously UNMEASURED and now has `p_u-p_c>1/2000`.

**Mechanism delta:** (i) the product-subgraph `p_c` certificate is strengthened from `p_c<0.06` to `p_c<0.056` by a depth-three fibre Galton--Watson construction; (ii) the perturbation is measured by the actual `l^2` norm of the added-generator adjacency operator rather than the crude bound `2k`; (iii) the explicit horizontal conjugates form a free `F_k`, giving the exact optimal-tree norm `2 sqrt(2k-1)` for that perturbation block.

## 2. Compact continuity handoff

Controlling policy is `operations/PROGRESS20_2026-09-20.md`; current LIVE20 assigns NM11 to T09 at `proofnet24/NM13-11/progress-percolation/`.

The preserved June Benjamini--Schramm archive (`probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md` and `proof_strategy.md`) records these earlier routes:

- normalized finite-set escape plus BK/last-exit boundary decomposition;
- killed-SAW interior growth and susceptibility-weighted boundary energy;
- global `l^2` SAW growth;
- scalar nonbacktracking polynomial bounds and product stress tests;
- quotient/fibre-shell and fixed-endpoint bridge criteria.

Several remained CONDITIONAL because their auxiliary inequalities lacked a complete transfer to `p_c<p_u`; product-only calculations were later recognized as already-covered qualitative families and are not re-counted here.

The recent NM13-11 sequence then established a load-bearing `p_{2->2}` transfer on explicit `SL_3(Z)` and higher-rank examples, weakened the free-core/complement hypotheses through degree 14, 11 and 9 constructions, introduced a `C_3*Z` fibre comparison, and in the immediate predecessor switched to Rattaggi's virtually simple `(12,8)` lattice with up to three arbitrary generator pairs. This run continues that fixed ambient group but changes the quantitative obstruction: the fourth arbitrary pair defeats the crude `2k` perturbation norm, so the new attack measures the perturbation by its actual subgroup operator norm and simultaneously strengthens the `p_c` side.

No historical or peer file is overwritten.

## 3. General operator-sparse perturbation theorem

Let `Gamma` be any `(12,8)`-group with standard inverse-closed generating set `S0`, so

`Cay(Gamma,S0) ~= T_12 square T_8`.

Let `C={c_1^{+-1},...,c_k^{+-1}}` be pairwise distinct new generators, disjoint from `S0`, and put

`G_C=Cay(Gamma,S0 union C)`.

Let

`K_C = sum_i (R_{c_i}+R_{c_i^{-1}})`

on `l^2(Gamma)` and write `kappa=||K_C||_{2->2}`. Then `G_C` is `D=20+2k` regular and

`||A_{G_C}|| <= 2 sqrt(11)+2 sqrt(7)+kappa`.        (3.1)

The theorem proved below is:

> **Operator-sparse perturbation criterion.** Every such graph satisfies
> `p_c(G_C)<7/125`. If `Q=19+2k` and there exists `z>sqrt(Q)` such that
> 
> `z + Q/z > 2 sqrt(11)+2 sqrt(7)+kappa`,             (3.2)
> 
> then `p_u(G_C)>1/z`, hence
> 
> `p_u(G_C)-p_c(G_C) > 1/z - 7/125`
> 
> whenever the right-hand side is positive.

In particular, taking `z=125/7` gives a clean qualitative sufficient condition

`kappa < 125/7 + 7(19+2k)/125 - 2 sqrt(11)-2 sqrt(7)`,       (3.3)

which directly implies `p_c<p_u`.

This is strictly weaker than requiring the new generators themselves to be free: freeness is only one convenient way to certify a small `kappa`.

## 4. The improved `p_c` transfer: depth-three fibre Galton--Watson

The standard product is a spanning subgraph of every `G_C`, so it is enough to prove

`p_c(T_12 square T_8) < 7/125`.

Root the `T_12` factor. A non-root base vertex has 11 forward child fibres after its unique parent direction is discarded. When exploration reaches a fibre `{x} x T_8` at one seed `(x,y)`, expose only the open cluster of `y` inside the radius-three ball of that `T_8` fibre; call its size `Z_3`.

For each of the 11 forward base children `x'`, inspect the horizontal edges from all `Z_3` exposed fibre-cluster vertices into `{x'} x T_8`. Conditional on `Z_3`, the probability that at least one is open is

`1-(1-p)^{Z_3}`.

Declare at most one offspring in each child fibre, using a fixed deterministic first open edge. Distinct child fibres use disjoint horizontal edge sets, every rooted `T_12` base vertex has a unique parent, and the internal radius-three edges in a newly entered fibre have not previously been exposed. Therefore the resulting particles form an honest Galton--Watson process with offspring mean

`m_3(p)=11 E[1-(1-p)^{Z_3}]`.

Write `s=1-p`. The exact truncated fibre pgf is obtained recursively:

`h_0=s`,

`h_1=s(s+p h_0)^7`,

`h_2=s(s+p h_1)^7`,

`C_3=s(s+p h_2)^8 = E[s^{Z_3}]`.

Hence

`m_3(p)=11(1-C_3)`.

At `p=7/125`, the exact-rational checker created and executed in this run proves the stronger inequality

`m_3(7/125) > 1 + 1/5000`.

Numerically,

`m_3(7/125)=1.000207277722705...`.

Thus the embedded Galton--Watson process is supercritical at `7/125`. Since `m_3(p)` is a polynomial/continuous function of `p` and the inequality is strict, it remains supercritical for some `p<7/125`. Therefore

`p_c(T_12 square T_8) < 7/125`,

and by spanning-subgraph monotonicity

`boxed(p_c(G_C)<7/125)`

for every perturbation considered here.

This is a genuine percolation transfer, not a finite auxiliary statistic.

## 5. The `p_u` transfer from the adjacency operator

For completeness, here is the operator-to-percolation step used in the recent track and needed to make (3.2) source-level.

Let `G` be a simple `D`-regular graph, `A` its adjacency operator, `Q=D-1`, and suppose `||A||<=a`. Let `N_n(x,y)` be the number of length-`n` nonbacktracking walks. Then

`N_0=I`, `N_1=A`, `N_2=A^2-DI`,

and for `n>=3`,

`N_n=A N_{n-1}-Q N_{n-2}`.

Spectral calculus for this quadratic recurrence gives

`limsup ||N_n||^{1/n} <= beta_D(a)`,

where

`beta_D(a)=sqrt(Q)` for `a<=2sqrt(Q)`, and otherwise

`beta_D(a)=(a+sqrt(a^2-4Q))/2`.

Every open connection contains a self-avoiding path, and every self-avoiding path is nonbacktracking. The union bound therefore gives the positive-kernel inequality

`T_p(x,y)=P_p(x<->y) <= sum_{n>=0} p^n N_n(x,y)`.

If `p beta_D(a)<1`, the right side converges in `l^2` operator norm, so `||T_p||_{2->2}<infinity`. Hence

`p_{2->2}(G) >= beta_D(a)^{-1}`.

On an infinite Cayley graph, for every `p>p_u`, uniqueness of the infinite cluster and FKG give

`T_p(x,y) >= P_p(x<->infinity, y<->infinity) >= theta(p)^2>0`.

A kernel bounded below by a positive constant on an infinite vertex set cannot be bounded on `l^2`, so

`p_{2->2}(G) <= p_u(G)`.

Consequently

`p_u(G) >= beta_D(a)^{-1}`.                         (5.1)

If `z>sqrt(Q)` and `z+Q/z>a`, then the larger root of `lambda^2-a lambda+Q=0` is strictly below `z`, so (5.1) yields `p_u>1/z`. This proves (3.2) with the adjacency estimate (3.1).

## 6. Rattaggi's group and the free horizontal perturbations

Rattaggi's 2007 construction gives a group

`Sigma=<a_1,...,a_6,b_1,...,b_4 | R_Sigma>`

whose standard Cayley graph is `T_12 square T_8`; its canonical index-four subgroup `Sigma_0` is finitely presented, torsion-free and simple.

Because the `a`-edges are exactly one tree direction in the standard product Cayley graph, the subgroup

`H_A=<a_1,...,a_6>`

has Cayley graph `T_12` with respect to these six inverse pairs. Hence

`H_A ~= F_6`.

Inside `<a_1,a_2> ~= F_2`, consider the homomorphism

`phi:F(a_1,a_2)->Z`, `phi(a_1)=1`, `phi(a_2)=0`.

The standard Schreier transversal `{a_1^j:j in Z}` shows that

`ker(phi)`

has free basis

`{a_1^j a_2 a_1^{-j}: j in Z}`.

Therefore for every finite `k`, the elements

`c_j=a_1^j a_2 a_1^{-j}`, `1<=j<=k`,

freely generate `F_k`. Their reduced `F_6` word lengths are `2j+1>=3`, so they are genuinely new, pairwise distinct, not inverses of one another, and disjoint from `S0`.

On `l^2(Sigma)`, right translation by this free subgroup preserves left cosets of `<c_1,...,c_k>`, and each coset block is the regular representation of `F_k`. Thus the added-generator adjacency operator has the exact norm

`kappa = 2 sqrt(2k-1)`.                              (6.1)

Combining (3.1), (6.1), the depth-three `p_c` bound, and the exact root tests in the checker gives the table in Section 1 for every `4<=k<=8`.

The weakest new endpoint is `k=8`:

`p_c(G_8)<7/125=0.056`,

`p_u(G_8)>113/2000=0.0565`,

so

`boxed(p_u(G_8)-p_c(G_8)>1/2000=0.0005)`.

This is a fixed-graph theorem on a concrete generating set; no simulation, asymptotic random-generator argument, or unproved percolation transfer is used.

## 7. Why this is not being counted from an already-covered family

The base *unperturbed* graph `T_12 square T_8` is a product and is not claimed as new. The graphs `G_k` add long horizontal word generators and are not the standard product generating set; the proof above establishes their gap directly.

Rattaggi proves that `Sigma_0` is an infinite finitely generated simple normal subgroup of finite index in `Sigma`. If `Sigma` were acylindrically hyperbolic, the standard infinite-normal-subgroup theorem would force `Sigma_0` to be acylindrically hyperbolic. Non-elementary acylindrically hyperbolic groups are SQ-universal, impossible for an infinite simple group. Thus `Sigma` is not acylindrically hyperbolic. Since every non-elementary hyperbolic group is acylindrically hyperbolic and `Sigma` is nonamenable/non-virtually-cyclic, `Sigma` is not Gromov hyperbolic either.

Therefore the all-Cayley theorems for hyperbolic groups and for acylindrically hyperbolic groups do not supply these fixed-graph gaps.

A bounded current search did not locate a theorem specifically covering these long-horizontal-generator perturbations of Rattaggi's lattice. This is bounded negative evidence only; **external novelty/priority remains UNVERIFIED**.

## 8. Requested current literature scopes, checked 20 September 2026

### arXiv:1804.10191 — Hutchcroft, *Percolation on hyperbolic graphs*

Current arXiv version is **v3, 26 March 2019**. It proves `p_c<p_u` for every connected locally finite **nonamenable Gromov-hyperbolic quasi-transitive graph**, and proves the triangle condition at `p_c`. It is a genuine solution on the hyperbolic class, not the general nonamenable Cayley problem.

### arXiv:2409.12283 — Hutchcroft--Pan, *Percolation at the uniqueness threshold via subgroup relativization*

Current arXiv entry is **v1, submitted 18 September 2024**. Its headline results concern the state **at `p_u`**: nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth, and co-heredity of a strong endpoint nonuniqueness property. The paper develops subgroup relativization, relative uniqueness monotonicity, connectivity decay, sharpness and a relative Burton--Keane theorem. Its stated theorem is not a quantitative fixed-Cayley `p_c<p_u` estimate for the Rattaggi graphs here.

### arXiv:2502.02560 — Terlov--Timar, *Weighted-amenability and percolation*

Current arXiv version is **v2, revised 14 September 2025**. It studies weighted amenability/nonunimodular transitive graphs, characterizes weighted amenability through finite unions of levels, and proves a relaxed Pak--Smirnova-Nagnibeda-style version of Hutchcroft's conjectural `p_h<p_u` statement. This is not the ordinary unimodular fixed-Cayley `p_c<p_u` theorem used here.

### Later enlargement checked

Choi--Seo, arXiv:2508.08932 (2025), prove `p_c<p_u` for **every Cayley graph of every acylindrically hyperbolic group**. As explained above, Rattaggi's `Sigma` is outside that group class.

## 9. Exact computation saved in this run

Load-bearing checker:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T08-50-00+0300__t09-rattaggi-free-horizontal-k8-check.py`

created at commit

`be1c51851c431c51da474b91a784f43349affcea`.

Executed output is archived as

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T08-50-00+0300__t09-rattaggi-free-horizontal-k8-check-output.txt`

at commit

`7a417d22fe5bc943e7b8451e5bbc7390eea9d92a`.

The exact assertions verify:

- `m_3(7/125)>1+1/5000`;
- rational square-root upper bounds used in every adjacency estimate;
- for `k=4,...,8`, the chosen `z=1/p_u_floor` satisfies `z^2>Q` and `z+Q/z>a_up`;
- every displayed `p_u` floor exceeds `7/125`.

The archived output terminates `ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit.

## 10. Residual obstruction and next attack

The universal T09 statement is still open. The new theorem remains a fixed-generating-set criterion that needs a sufficiently small perturbation operator norm.

The explicit free-horizontal construction reaches `k=8`. At `k=9`, the free perturbation already has norm `2 sqrt(17)`, and the present scalar adjacency/nonbacktracking method is numerically too tight to certify a gap using the current one-fibre comparison. I do **not** claim impossibility: that is a route boundary, not a source theorem.

The next materially useful attack is therefore one of:

1. a colored/nonbacktracking operator recurrence that keeps the standard-product and perturbation edge types separate instead of collapsing them into `||A_0||+kappa`; or
2. a multi-seed/two-coordinate percolation subprocess improving the `p_c` comparison below the one-fibre threshold.

Either route must produce an actual `p_c`/`p_u` transfer before being counted as source-level progress.

## ledger_delta

```yaml
ledger_delta:
  track: NM13-11
  parent: T09
  status: PARTIAL
  candidate_status: CANDIDATE_FULL_RESTRICTED_THEOREM
  source_problem: "pc(G)<pu(G) for every Cayley graph of every finitely generated nonamenable group"
  original_problem_before:
    universal_status: OPEN
    latest_fixed_scope: "Rattaggi (12,8)-group standard graph plus k<=3 arbitrary new inverse pairs"
    common_pc_bound: "<3/50"
    weakest_gap: ">9/10000 at k=3"
  original_problem_after:
    universal_status: OPEN
    new_fixed_scope: "same Rattaggi group with explicit horizontal-free perturbations k=4,...,8"
    common_pc_bound: "<7/125"
    k8_pu_bound: ">113/2000"
    k8_gap: ">1/2000"
  mechanism_progress:
    - "depth-3 T8-fibre Galton-Watson transfer: pc(T12 x T8)<7/125"
    - "operator-sparse perturbation criterion in terms of kappa=||K_C||"
    - "Schreier free horizontal conjugates give kappa=2*sqrt(2k-1)"
  prior_routes_preserved:
    - finite_set_escape_BK_last_exit
    - killed_SAW_boundary_energy
    - global_l2_SAW
    - scalar_nonbacktracking_and_product_stress_tests
    - quotient_fibre_shell_and_bridge
    - SL3_free_core_triangle_fibre_S_arithmetic
    - Rattaggi_k_le_3_arbitrary_perturbations
  unchanged_substantive_runs: 0
  failed_recoveries: 0
  essential_checker_commit: be1c51851c431c51da474b91a784f43349affcea
  essential_output_commit: 7a417d22fe5bc943e7b8451e5bbc7390eea9d92a
  independent_review: NOT_DONE
  external_priority: UNVERIFIED
  next_attack: "colored nonbacktracking split by standard-product vs perturbation edge type, or multi-seed two-coordinate pc subprocess"
```
