Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-effort telemetry is exposed, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 random 3-SAT: a two-menu collision branching barrier for majority-repair trees

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT with independent fair signs on three distinct variables**  
Status: **OPEN / PARTIAL**

## 0. Source threshold before / after, kept separate from mechanism progress

The strongest explicit-decimal bracket I can independently support directly from published source statements remains

\[
\boxed{3.52\le \liminf \alpha_n^*\le \limsup \alpha_n^*\le4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability with high probability below `3.52` by a degree-based constructive algorithm. Díaz--Kirousis--Mitsche--Pérez-Giménez prove a.a.s. unsatisfiability at `4.4898`. The 27 March 2026 Cambridge paper on the random `k`-SAT Gibbs-uniqueness threshold still states that the satisfiability threshold is known precisely for `k=2` and all sufficiently large `k`, while fixed small `k>=3` remains unresolved. Carenini's August 2026 scaling-window result for every fixed `k>=3` narrows the window but does not locate its center or settle convergence of the `k=3` center sequence.

Therefore the **external source metric is unchanged**:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad W:0.9698\longrightarrow0.9698.
\]

Companion NM13-13 has meanwhile advanced the project's distinct cluster-aware upper-bound route to **CANDIDATE_FULL, pending later independent review, at `4.38890`** (`NM13-13-T04-GAUSS3-TAIL-438890-UPPER-07`). Thus the current internal candidate bracket is `[3.52,4.38890]`, width `0.86890`. I do not promote that project candidate into the externally published metric.

This run makes **no threshold-endpoint claim**. It executes a materially different method after the recent four-spectrum/adjoint sequence: return to the majority-repair construction, but analyze the *global compatibility selector* rather than another local repair recursion. The new result is an exact best-case branching parameter for a natural two-menu selector. It crosses criticality already between `3.58068` and `3.58069`, only about `0.06069` above the published lower endpoint. This sharply identifies why “give every bad clause two independent repair trees and solve the resulting compatibility problem by a subcriticality argument” cannot be the missing proof at `alpha=3.6`.

## 1. Compact handoff and routes not repeated

The majority-repair line already established the following local facts.

1. Under the literal-majority assignment, if `P,N iid Pois(mu)` with `mu=3 alpha/2`, `Z=min(P,N)` and `M=max(P,N)`, then the false-literal occurrence fraction is

\[
q=\frac{\mathbb E Z}{2\mu}
=\frac12\left[1-e^{-2\mu}\{I_0(2\mu)+I_1(2\mu)\}\right].
\tag{1.1}
\]

2. A variable reached through a false literal has the Palm law proportional to `Z`; conditional on `(P,N)`, its initial break count is

\[
B\mid(P,N)\sim\operatorname{Bin}(M,q^2).
\tag{1.2}
\]

3. Greedily choosing the lower-break candidate among the two new false literals in a newly broken clause has subcritical offspring mean

\[
r_2=\mathbb E\min(B_1,B_2),
\tag{1.3}
\]

throughout the explicit source bracket; at `alpha=3.6`, `r_2=0.50814836789645...`.

4. The static initially blocked-majority hypergraph is also subcritical through `4.4898`; hence neither one-tree genealogy nor the initial blocked core explains the constructive barrier.

5. Independent one-shot zero-break thinning was proved impossible: every fixed degree-type independent thinning leaves a positive linear density of bad clauses. Finite repair menus, by contrast, are locally abundant with double-exponentially small no-menu probability. Their unresolved step was simultaneous compatibility (Hall/Haxell/LLL-type selection).

The separate four-spectrum line derived exact cascade drifts, hidden 2/3-clause split gains and a terminal adjoint compiler. Those are preserved, but three successive substantive reports had remained on that same recovery architecture without moving the source endpoint. Under the current progress-first instruction this run therefore does **not** add another four-spectrum lemma.

## 2. The fresh-copy repair-tree class

I isolate the best possible local tree in the memoryless class before analyzing global collisions.

An initially majority-unsatisfied root clause offers three false-literal variables. Flipping one variable may break `B` clauses that it had uniquely satisfied. Every newly broken clause has two remaining false-literal variables available for repair (the parent variable is excluded). In the local tree limit, the candidate break counts are independent copies of (1.2).

A **fresh-copy memoryless tree policy** sees only the candidate break counts at the current broken clause, chooses exactly one candidate variable, and then treats the resulting broken child clauses independently with the same rule. Auxiliary randomness is allowed. Let `C` be the expected number of flipped variables required to repair one nonroot broken clause, and let `S` be the expected total number of flipped variables in the repair of an initially unsatisfied root clause.

### Proposition 2.1 — exact local optimum in the memoryless tree class

Put

\[
r_k:=\mathbb E\min(B_1,\ldots,B_k)
=\sum_{t\ge1}\Pr(B\ge t)^k.
\tag{2.1}
\]

If `r_2<1`, then among all fresh-copy memoryless policies the smallest possible expected nonroot repair cost and root repair-tree size are

\[
\boxed{C_*={1\over1-r_2}},
\qquad
\boxed{S_*=1+{r_3\over1-r_2}}.
\tag{2.2}
\]

They are attained by choosing a candidate of minimum break count at every clause.

#### Proof

Suppose a nonroot broken clause presents candidate break counts `(b_1,b_2)`. Under the fresh-copy rule, once candidate `i` is flipped, the `b_i` newly broken clauses start independent copies of the same continuation problem. If the continuation cost is `C`, the conditional expected total cost is therefore

\[
1+b_i C.
\]

Because `C>=0`, this is minimized pointwise by choosing `min(b_1,b_2)`. Randomization cannot improve a pointwise minimum. Hence every optimal policy obeys

\[
C=1+r_2 C,
\]

which gives the first formula in (2.2) when `r_2<1`.

At the root there are three candidate variables. The same argument says that the optimal first flip has break count `min(B_1,B_2,B_3)`, after which every broken child costs `C_*`. Thus

\[
S_*=1+r_3 C_*=1+\frac{r_3}{1-r_2}.
\]

This also proves minimality among all memoryless policies in the stated class. QED.

This proposition matters for the global obstruction below: the collision parameter derived there is increasing in `S`, so using `S_*` gives the **best possible two-menu collision branching factor** obtainable from this whole fresh-copy memoryless tree family.

## 3. From two repair menus to a selector implication graph

The earlier unresolved global problem was: give each bad root more than one valid repair tree and select one tree per root so that selected trees do not conflict.

To separate the unavoidable random-collision scale from formula-specific correlations, define the following surrogate exactly.

### Definition 3.1 — two-menu fresh-label surrogate

Let

\[
u(\alpha)=\alpha q(\alpha)^3
\tag{3.1}
\]

be the local-tree-limit density of initially majority-unsatisfied clauses. Take `R_n=floor(u n)` roots. Each root `r` receives two independent repair options `T_r^0,T_r^1`. Their sizes are iid copies of the locally optimal repair-tree size from Proposition 2.1; conditional on its size `s`, an option uses `s` distinct resource labels sampled uniformly from `[n]`. Options are independent across roots and between the two choices of one root.

Two options conflict if their resource sets intersect. Introduce a binary selector `x_r` choosing option `0` or `1` for root `r`. A conflict between `(r,i)` and `(s,j)` adds the 2-CNF clause forbidding `x_r=i,x_s=j`. Equivalently, it adds implications

\[
(r,i)\to(s,1-j),
\qquad
(s,j)\to(r,1-i).
\tag{3.2}
\]

This surrogate intentionally ignores additional dangerous-clause conflicts and all correlations of two trees exposed in the same original formula. Therefore it is a **best-case diagnostic**, not a transfer theorem for random 3-SAT.

### Proposition 3.2 — exact local collision branching mean

Assume the repair-tree size has finite second moment (it does here because `B` has an exponential moment and `r_2<1`). In the surrogate of Definition 3.1, the local implication exploration from a uniformly sampled option literal has mean offspring

\[
\boxed{
\mathcal C_2(\alpha)=2u(\alpha)\,S_*(\alpha)^2.
}
\tag{3.3}
\]

Moreover, for every fixed exploration depth the implication neighborhood converges to the corresponding resource-mediated branching process. In particular, if `C_2<1`, the limiting implication exploration is subcritical with an exponential total-progeny tail; if `C_2>1`, its local branching process has positive survival probability.

#### Proof

There are `2R_n` option sets. Their total expected resource incidence is

\[
2R_n S_*=2uS_* n+o(n).
\]

Fix one occurrence of a resource label inside a currently explored option. Apart from the current occurrence, the number of incidences of that same resource among all other options converges by the law of small numbers to a Poisson random variable of mean

\[
2uS_*.
\tag{3.4}
\]

If the current option has size `s`, summing over its `s` resources gives conditional mean outgoing implications

\[
2uS_*\,s+o(1).
\]

Every such implication lands at the *complement* option of the encountered root. Because the two options of a root are independent in the surrogate, that complement option has the ordinary repair-tree size law, not the resource-size-biased law. Averaging the preceding display over the ordinary current size, whose mean is `S_*`, gives (3.3).

At fixed depth, repeated root/resource discoveries have probability `o(1)` after conditioning on bounded explored size; exponential tails allow the usual truncation removing the bounded-size conditioning. Thus the neighborhood converges to the resource-mediated branching process. Its mean is (3.3). Standard Galton--Watson/compound-Poisson arguments give exponential total progeny below mean one and positive survival probability above mean one. QED.

### Important limitation

`C_2>1` is **not** a proof that the actual repair-menu selector is unsatisfiable. Even in the surrogate, branching supercriticality by itself is weaker than a complete 2-SAT unsatisfiability theorem because resource cliques create dependent clauses. In the original formula the two menus are additionally correlated, and a deliberately anti-correlated menu construction could reduce collisions. The valid conclusion is narrower and useful: any proof that replaces actual menus by asymptotically independent fresh copies and then relies on *subcritical implication components* cannot reach densities where the best-case value (3.3) already exceeds one.

## 4. Numerical location of the best-case two-menu branching transition

All ingredients in (3.3) are explicit:

\[
q=\frac12\left[1-e^{-2\mu}(I_0(2\mu)+I_1(2\mu))\right],
\quad \mu=\frac{3\alpha}{2},
\tag{4.1}
\]

\[
B\mid(P,N)\sim\operatorname{Bin}(\max(P,N),q^2)
\quad\text{under Palm weight }{\min(P,N)\over\mathbb E\min(P,N)},
\tag{4.2}
\]

\[
r_2=\sum_{t\ge1}\Pr(B\ge t)^2,
\quad
r_3=\sum_{t\ge1}\Pr(B\ge t)^3,
\quad
S_*=1+{r_3\over1-r_2},
\tag{4.3}
\]

and `u=alpha q^3`.

The executed high-precision diagnostic is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T12-25-17__two_menu_collision_branching.py`

created at commit `2727c75ccc1ec44f80c0cee077a0f675de014c5d`; its archived output is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T12-25-17__two_menu_collision_branching.out`

created at commit `58c491b0643c4a94ea646d79bd398fe4cd9f286d`.

The code uses 50 decimal digits and truncates the independent Poisson sums at `P,N<=50`. At all displayed densities the omitted ordinary Poisson mass is below `9e-30` and the omitted false-Palm mass below `2.3e-29`. These are truncation diagnostics only: the script explicitly labels itself a high-precision finite-sum calculation, **not** a directed-rounding interval certificate.

The decisive values are

\[
\begin{array}{c|c|c|c|c}
\alpha & r_2 & r_3 & S_* & \mathcal C_2\\ \hline
3.52 & 0.489551142506079 &0.285456332145715&1.559226116299251&0.929666955224413\\
3.55 & 0.496507365200655 &0.290811748020920&1.577588881983975&0.963617097375678\\
3.58 & 0.503484941211354 &0.296199161894639&1.596556250715295&0.999168019570850\\
3.60 & 0.508148367896451 &0.299808316800522&1.609550314021127&1.023807549590812
\end{array}
\tag{4.4}
\]

and the sign change is already resolved at five decimal places:

\[
\boxed{
\mathcal C_2(3.58068)=0.999993168960466853<1,
}
\tag{4.5}
\]

\[
\boxed{
\mathcal C_2(3.58069)=1.00000531003766883>1.
}
\tag{4.6}
\]

A linear interpolation inside this tiny bracket gives the diagnostic crossing

\[
\boxed{\alpha_{\rm coll}\approx3.58068562639.}
\tag{4.7}
\]

Because the arithmetic is not outward-rounded, (4.7) is **not** promoted to a rigorous decimal theorem. The symbolic formula (3.3) and the local-optimality result (2.2) are the theorem-sized advances; (4.5)--(4.7) are a decisive high-precision mechanism calculation. The margins in (4.5)--(4.6), about `6.8e-6` and `5.3e-6`, are vastly larger than the displayed truncation tails, so only floating/rounding certification remains if this auxiliary crossing itself later becomes worth formalizing.

## 5. What this rules out and what it does not

### 5.1 A real obstruction to the naive two-menu proof architecture

At `alpha=3.6`, even the locally **smallest-mean** fresh-copy memoryless repair tree has

\[
S_*=1.6095503140...,
\]

while the initial bad-root density is

\[
u=0.19759648638... .
\]

Thus

\[
\boxed{2uS_*^2=1.02380754959...>1.}
\tag{5.1}
\]

Every other memoryless one-variable-per-broken-clause tree policy has expected size at least `S_*`, hence an equal or larger fresh-copy collision branching mean. Therefore **the entire two-independent-menu + subcritical-selector strategy is already on the wrong side of its best-case local branching transition at the first target density `3.6`**.

This is more informative than the previous statement “global Hall compatibility is still open.” It says exactly which cheap globalization cannot close that Hall step.

### 5.2 Why this does not kill the majority-repair family

The selected-tree variable load at `alpha=3.6` is only

\[
 uS_*=0.3180414867...<1.
\tag{5.2}
\]

So there is no deterministic resource-capacity contradiction. The supercritical value in (5.1) is a **birthday-collision effect caused by independent menus**, not an unavoidable shortage of variables. This distinction points to the only remaining plausible form of the repair route: menu generation must itself be negatively correlated / load-aware, or it must expose three or more structured alternatives per root and solve a genuine set-packing problem. Treating menu trees as fresh independent samples throws away exactly the global structure one needs.

The actual random formula is also harder than the surrogate because two disjoint variable sets can still be incompatible through a satisfied clause whose true literals are flipped by different trees. Hence a successful proof must control both resource overlap and these clause-mediated conflicts; (3.3) only addresses the former.

## 6. Relation to the published Hajiaghayi--Sorkin constructive route

I rechecked the original Hajiaghayi--Sorkin source during this run. Their published heuristic chooses pure variables first and otherwise maximizes signed-degree discrepancy `|i-j|`, ties by maximal `i+j`, with unit propagation after each free choice. They report `3.52`, compared with `3.50`, `3.44`, and `3.42` for weaker selection rules, and explicitly propose a future four-parameter split between positive/negative appearances in 2- and 3-clauses. Their paper also notes that a fully rigorous decimal numerical implementation requires derivative/Lipschitz bounds and interval arithmetic.

That source check reinforces the role of this run: the collision calculation is **not** another claimed reproduction of their differential equations and does not alter `3.52`; it analyzes a distinct majority-start local-repair construction that had shown unusually strong local subcriticality but lacked a global compatibility theorem.

## 7. Current verdict and next attack

**Verdict:** source threshold unchanged; new mechanism theorem and a failed globalization route.

The majority-repair programme has now passed three increasingly global tests:

- local repair genealogy: subcritical;
- static blocked-majority core: subcritical;
- naive two-independent-menu compatibility selector: **best-case implication branching becomes supercritical at about `3.58069`**.

Thus the obstruction has moved from local repair existence to the *correlation architecture of menus*. This is useful negative information: continuing to add independent repair alternatives and invoking a standard subcritical 2-SAT/LLL argument at `alpha=3.6` is not credible.

The next materially distinct constructive calculation, if this family is continued, should be a **correlated three-menu/resource-allocation scheme**: expose candidate trees while forbidding already-heavy resource labels, derive the induced two-type load process, and prove a Hall/set-packing condition directly rather than via fresh-copy collision subcriticality. If that load-aware scheme cannot keep a positive Hall margin at `alpha=3.6`, this majority-repair family should be retired and the worker should return to a different T04 construction or a complementary upper-bound inequality rather than tune the same local tree again.

## 8. Literature/access note

Fresh bounded checks on 20 September 2026 used:

- Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, arXiv `math/0310193` / 2003 source PDF;
- Díaz--Kirousis--Mitsche--Pérez-Giménez, *A new upper bound for 3-SAT*, arXiv `0807.3600`, FSTTCS 2008;
- Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited*, Cambridge CPC, published online 27 March 2026;
- Carenini, *The Scaling Window of Random k-SAT*, ECCC TR26-145, August 2026.

The recent papers do not turn a large-`k`, Gibbs-uniqueness, or scaling-window statement into the missing exact iid `k=3` threshold. The search is bounded and is not asserted to prove worldwide novelty of the present auxiliary collision theorem.

## 9. ledger_delta

```yaml
ledger_delta:
  worker: NM13-06
  parent: T04
  source_model: classical iid random 3-SAT; uniform signed proper 3-clauses on distinct variables
  status: OPEN/PARTIAL
  source_metric:
    kind: explicit published threshold bracket
    before: "[3.52, 4.4898]"
    after: "[3.52, 4.4898]"
    movement: none
  companion_project_candidate:
    worker: NM13-13
    upper_endpoint: "4.38890"
    status: CANDIDATE_FULL_PENDING_LATER_INDEPENDENT_REVIEW
  route_this_run: majority_repair_two_menu_collision_branching
  route_change_reason: three recent four-spectrum/adjoint reports had no source endpoint movement; materially different global-compatibility method executed
  demonstrated_mechanism_gain:
    theorem: "fresh-copy memoryless tree optimum S*=1+r3/(1-r2); two-menu resource-conflict implication mean C2=2*alpha*q^3*S*^2"
    alpha_3_52_C2: "0.929666955224413"
    alpha_3_60_C2: "1.023807549590812"
    high_precision_crossing_bracket: "3.58068 < alpha_coll < 3.58069 (diagnostic, not outward-rounded)"
    interpretation: "best-case fresh-independent two-menu selector is already supercritical at alpha=3.6; local capacity itself is not exhausted"
  threshold_gain_claimed: false
  surrogate_unsat_claimed: false
  actual_formula_transfer_claimed: false
  failed_attack_preserved:
    - two_choice_local_genealogy alone does not globalize
    - static_blocked_core is not the barrier
    - independent_zero_break_thinning leaves linear residual
    - naive_two_independent_menus_plus_subcritical_selector fails its best-case branching test at alpha=3.6
  essential_artifacts:
    code_commit: 2727c75ccc1ec44f80c0cee077a0f675de014c5d
    output_commit: 58c491b0643c4a94ea646d79bd398fe4cd9f286d
  next_attack: correlated three-menu/load-aware set packing with direct Hall criterion; retire majority-repair if no positive margin at alpha=3.6
```
