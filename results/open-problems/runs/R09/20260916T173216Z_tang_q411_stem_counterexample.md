Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — MOVEMENT: fixed metric UNMEASURED -> exact 4 at the certified pair (T_3,p=3/4); methods tried this run: B2 ATTACK THE NEGATION, B5 ADD A PARAMETER AND DIFFERENTIATE, B19 MAKE IT AN ALGORITHM. The scheduler exposes no model selector or reasoning selector, so GPT-6/maximum is prompt-only and is not claimed.

Problem/source: Pengfei Tang, *A note on some critical thresholds of Bernoulli percolation*, arXiv:2012.01135v2 / Electron. J. Probab. 28 (2023), Question 4.11. Source question: for a transitive graph or a periodic tree rooted at o, is the Bernoulli BOND-percolation probability theta(p) concave on (p_c,1)?

Run status: PARTIAL at fleet/source-family granularity. The periodic-tree universal assertion is REFUTED by a fully written counterexample family below; the transitive-graph class is untouched and remains OPEN here. The periodic-tree refutation is not fleet-closed until the required P26 audit and a second OTHER-track audit are obtained. Consecutive unchanged count remains UNKNOWN from prior scheduling history; the metric moved on this first R09 Tang run.

## 1. Repository continuity, admission, and old-slot handoff

Before research I read the current campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/claims/TANG-2020-Q4.11.md`. I also recovered the newest pre-transfer R09 report `runs/R09/20260916T162904Z_7a42c1e9.md` and inspected the newest nearby R08/R10 reports available on master. Targeted searches were run across the intake/campaign repository material. The very large intake JSONL files cannot be literally materialized row-by-row through the connector before output truncation; I record that as an access/output limitation rather than claim a fictitious complete 780-row visible read.

The canonical Tang claim is owned by R09 and still says `PENDING_ADMISSION`; I do not mutate that shared claim file. This report completes the pending research-side checks: the original Question 4.11 is current in arXiv v2 and the 2023 journal paper; bounded current-literature searches found no later primary resolution; repository searches for `2012.01135`, `TangQ4.11`, `periodic-tree concavity`, and the exact Question 4.11 phrase found no competing research owner or posted/settled copy of this scope. The only canonical ownership record found is the R09 claim. Thus there is no ownership/exclusion conflict for the present work. The coordinator/P26 may reconcile the claim label later.

### Immutable handoff of the former R09 route

The former R09 critical-SITE-percolation-on-Z^3 one-arm route is RETIRED FROM THIS SLOT, not mathematically solved. Its newest preserved report is `runs/R09/20260916T162904Z_7a42c1e9.md`, with the exact radius-4 one-arm upper bound and the L^{-3/2} moving-window passage compiler. All old reports/artifacts remain untouched. Nothing in this Tang run changes their mathematical status.

## 2. Source locator and hypotheses

Primary source checked 2026-09-16: arXiv:2012.01135v2, last revised 1 Mar 2023, published as EJP 28 (2023), DOI 10.1214/23-EJP926.

Tang studies Bernoulli **bond** percolation. On PDF page 10, Definition 4.1 says that an infinite locally finite rooted tree T is N-periodic if for every vertex x there exists an adjacency-preserving bijection

    f : T^x -> T^{f(x)}

with |f(x)| <= N; T is periodic if it is N-periodic for some finite N. There is no strong-connectivity assumption in this definition.

On PDF page 15, after Example 4.10, Question 4.11 asks exactly whether theta(p) is concave on (p_c,1) for a transitive graph **or a periodic tree with root o**. The strong-connectivity condition belongs to Theorem 4.7 and its directed-cover derivative theorem, not to Question 4.11. Indeed Tang explicitly discusses periodic directed covers that are not strongly connected immediately before the question. I therefore do not import strong connectivity into the source statement.

Tang's finite-type recursion is

    theta_i(p) = 1 - product_j [1-p theta_j(p)]^{a_ij}.

The source itself warns implicitly about algebraic branches: zero is always a fixed point, while the physical percolation vector is the infinite-survival branch.

## 3. Current-literature / historical-ownership search

Dated searches on 2026-09-16 included:

1. exact title + `Question 4.11` + `concave` + `periodic tree`;
2. exact phrase `percolation probability concave periodic tree`;
3. `Pengfei Tang` + `concavity` + `percolation`;
4. exact candidate formula searches `2p^2-p percolation tree` and `finite stem percolation probability tree concave`;
5. the journal DOI `10.1214/23-EJP926` plus `concavity`;
6. Tang's later-author publication surface and papers citing the threshold note.

No later primary paper resolving Question 4.11 was found in this bounded search. A 2025 citing paper by Zhongyang Li concerns critical SITE cutsets, not concavity. Tang's later visible papers concern USF/MST/nonunimodular topics, not this question. This negative search is not a proof of worldwide novelty. The counterexample mechanism below is elementary — finite rooted-edge extension multiplies a tail survival probability by a power of p — and should be treated as potentially folklore until broader specialist prior-art review and the two required audits are complete.

The intake exclusion `I0055 / Lyons-Peres Question 5.16` is respected: Tang's Theorem 1.6 already gives the positive answer to the modified first-moment question for bond percolation, so it is not used as a reserve target.

## 4. Method B2 — attack the negation: a three-edge stem into a binary tree

The negation search succeeds.

For an integer k>=0 define T_k as follows. Start with a path

    v_0=o -- v_1 -- ... -- v_k.

From v_k onward attach the infinite rooted binary tree: v_k has two children and every later vertex has exactly two children. The case k=0 is the ordinary rooted binary tree. The candidate that freezes the R09 metric is T_3.

### Lemma 4.1 — T_k is k-periodic in Tang's exact sense

For every k>=0, T_k is a periodic tree under Tang Definition 4.1.

Proof. T_k is infinite and locally finite. If x=v_i is one of the stem vertices with 0<=i<=k, use the identity map T^x -> T^x; its image root is x and |x|=i<=k. If x is a strict descendant of v_k, then T^x and T^{v_k} are both rooted infinite binary trees. Delete the finite word identifying the route from v_k to x and map descendants of x bijectively, child-by-child, to descendants of v_k. This is an adjacency-preserving bijection T^x -> T^{v_k}, sends x to v_k, and |v_k|=k. Thus every x has the required forward-subtree bijection to a root within the first k levels. QED.

This verifies the source periodicity hypothesis directly; no appeal to transitivity or strong connectivity is made.

## 5. Method B5 — add p and differentiate the exact physical formula

Let beta(p) be the probability that the root of the infinite binary tail belongs to an infinite open cluster. The usual first-generation decomposition gives

    beta = 1 - (1-p beta)^2.

Equivalently

    beta [p^2 beta - (2p-1)] = 0.

For p<=1/2 the only fixed point in [0,1] that is the infinite-survival probability is beta=0. For p>1/2 the positive root is

    beta(p) = (2p-1)/p^2.

I verify the physical branch, rather than merely choosing this algebraic root, in Section 6 below.

The root o of T_k reaches infinity iff all k stem edges are open and v_k survives through the binary tail. These use disjoint edges, hence

    theta_k(p) = p^k beta(p).

Therefore

    theta_k(p)=0,                    p<=1/2,
    theta_k(p)=p^{k-2}(2p-1),       p>1/2.

In particular p_c(T_k)=1/2 for every finite k.

For k>=3,

    theta_k''(p)
      = (k-2) p^{k-4} [ 2(k-1)p - (k-3) ].

If p>1/2 then

    2(k-1)p-(k-3) > (k-1)-(k-3)=2,

so theta_k''(p)>0 on the *entire* supercritical interval. Thus every T_k with k>=3 has a strictly convex percolation function on (1/2,1), directly contradicting concavity.

The smallest member of this stem family with positive curvature is k=3. For it,

    theta_3(p)=p(2p-1)=2p^2-p,
    theta_3''(p)=4

for every p in (1/2,1).

At the frozen exact parameter p=3/4,

    theta_3(3/4)=3/8,
    theta_3''(3/4)=4.

Hence the fixed R09 metric moves from UNMEASURED to the exact value 4. Since equality theta''=4 is proved, 4 is not merely a numerical estimate but the greatest possible rigorous lower bound at this frozen candidate/parameter.

### Theorem R09-TANG-Q411-PERIODIC

Tang Question 4.11 has a negative answer in the periodic-tree class as stated in Definition 4.1. The 3-periodic tree T_3 above has p_c=1/2 and

    theta(p)=2p^2-p,  p in (1/2,1),

so theta''(p)=4>0 throughout the supercritical interval and theta is strictly convex, not concave.

This theorem does not address the transitive-graph class.

## 6. Method B19 — certified branch-selection algorithm; zero is rejected

A fixed-point identity alone is not enough: B_p(0)=0 always, so blindly solving the polynomial system can select the extinction branch. Here is the branch rule and its exact specialization.

For any finite-type directed-cover recursion

    B_p(alpha)_i = 1-product_j(1-p alpha_j)^{a_ij},

define alpha^(0)=1 and alpha^(n+1)=B_p(alpha^(n)). The ith coordinate alpha_i^(n) is exactly the probability that type i reaches generation n. These events decrease with n, hence alpha^(n) decreases coordinatewise to the physical infinite-survival vector theta(p). Continuity of B_p gives B_p(theta)=theta.

Moreover, if gamma in [0,1]^d is any fixed point, monotonicity gives

    gamma = B_p^n(gamma) <= B_p^n(1)=alpha^(n)

for every n. Therefore gamma<=theta after n->infinity. Thus **the physical percolation vector is the greatest fixed point** of B_p. This argument does not require strong connectivity.

For T_3 the type matrix is

    A = [[0,1,0,0],
         [0,0,1,0],
         [0,0,0,1],
         [0,0,0,2]].

The fixed-point equations are triangular:

    theta_0=p theta_1,
    theta_1=p theta_2,
    theta_2=p theta_3,
    theta_3=1-(1-p theta_3)^2.

For p>1/2 the terminal equation has only theta_3=0 and theta_3=(2p-1)/p^2 in [0,1]. If theta_3=0, triangularity forces the whole vector to zero. If theta_3 is the positive root, the upstream coordinates are uniquely forced. Since the positive fixed point is coordinatewise larger than zero, it is the greatest fixed point and hence the physical percolation vector.

At p=3/4 the exact physical vector is

    (theta_0,theta_1,theta_2,theta_3)
      = (3/8, 1/2, 2/3, 8/9).

Equivalently, the binary-tail extinction equation is

    q=(1/4+3q/4)^2,

or

    (q-1)(9q-1)=0.

The physical extinction probability is the smaller root q=1/9, while q=1 is the spurious extinction fixed point above p_c. This completely separates the physical branch from the algebraic zero branch.

## 7. Exact-arithmetic self-check

Artifact source:
`artifacts/R09/20260916T173216Z_tang_q411_stem_checker.py`
creation commit `9e21612abe0677b6577f8ef47c897e27fe402b81`.

Archived output:
`artifacts/R09/20260916T173216Z_tang_q411_stem_checker.out`
creation commit `9ff9a8ee12a6bb2a5c30ce6ffac64c7d0c000b84`.
Local output SHA-256 recorded there:
`372b380827bdd44f9d7f2cb97529c1bf6190cf319c15ac47e43868b8735bcb7e`.

The checker uses Python `Fraction` only. It verifies exactly at p=3/4:
- the four-type recurrence;
- the positive vector `(3/8,1/2,2/3,8/9)`;
- the zero algebraic fixed point separately;
- the two binary extinction roots 1/9 and 1;
- supercritical mean 2p=3/2;
- the forced upstream stem recursion;
- p_c=1/2 for the candidate decomposition;
- theta_root(p)=2p^2-p and theta_root''=4;
- the N=3 periodicity witness data.

The analytic proof above, not the checker, establishes the infinite-tree periodicity and the all-p formula.

## 8. Why this does not silently change the source scope

1. Model: Tang is using Bernoulli **bond** percolation; so is T_3.
2. Graph: T_3 is an infinite locally finite tree.
3. Periodicity: proved directly from Tang Definition 4.1 with N=3.
4. Root: the source asks for a periodic tree with root o; the stem root is exactly o.
5. Strong connectivity: not part of Question 4.11 and not imposed here. The source itself separates the strongly-connected hypothesis of Theorem 4.7 from general periodic trees.
6. Physical branch: selected by the greatest-fixed-point / finite-depth survival algorithm, not by algebraic wishful thinking.
7. Parameter: p=3/4 belongs to (p_c,1) because p_c=1/2.

## 9. Model/scheduler interface status requested by owner

The situation is still as recorded in the controlling repository policy. This runtime identifies the model as GPT-5.6 Sol; reasoning effort has no authenticated runtime telemetry here, so it is UNVERIFIED. The scheduler interface exposed to the fleet permits task title/prompt/schedule/enablement/timing mode, but exposes no model selector and no reasoning-effort selector. Therefore putting `Model: GPT-6. Reasoning: maximum` in prompt text is only a request, not a verified scheduler setting.

To make GPT-6/maximum a real enforceable task setting, the authorized scheduler/product interface would need to expose model and reasoning-effort fields (and runtime telemetry confirming them), or the task would need to be managed in an authorized interface that provides those controls. Prompt text alone cannot do this.

The controlling policy records historical native modification probes for P26/P01/P03 that returned `You cannot modify this task`. It also records that a P26 full update later succeeded in a different exposed authorized context. The safe workaround for a task that still refuses modification is to use the account/workspace/interface that actually owns that native task, or platform support to correct ownership/permissions. Do not bypass the restriction and do not create a duplicate scheduler job. This run made no scheduler change.

## 10. Status, closure obligations, and next work

Mathematical status:
- periodic-tree half of Tang Question 4.11: **REFUTED by T_3**, subject to independent audit;
- transitive-graph half: **OPEN / untouched**;
- fleet closure: **NOT CLOSED** because the required two independent OTHER-track audits are absent.

Required closure checks still missing:
1. P26 end-to-end audit of the exact source definition, periodicity proof, physical branch, and curvature;
2. a second independent audit from a different track;
3. broader specialist prior-art review beyond the bounded searches above, with explicit treatment of the elementary finite-stem mechanism as potentially folklore.

No `paper_<name>/` folder is created before those closure requirements are met.

Highest-value next route if this periodic refutation survives audits: test whether the source's transitive-graph half may still be true, where the finite-stem mechanism is forbidden by transitivity. A genuinely new attack there should not merely repeat the reducible directed-cover construction.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R09
  source: "Pengfei Tang, A note on some critical thresholds of Bernoulli percolation, arXiv:2012.01135v2 / EJP 28 (2023), Question 4.11"
  target: "Concavity of bond-percolation theta(p) on (p_c,1), periodic-tree class first"
  metric: "greatest rigorous lower bound for theta'' at the frozen certified candidate T_3 and p=3/4"
  before: "UNMEASURED"
  after: "4 exactly"
  movement: true
  status: "PARTIAL: periodic-tree universal assertion REFUTED; transitive-graph class OPEN; audit closure pending"
  unchanged_count: "UNKNOWN (metric moved this run; prior Tang-run history did not exist)"
  exact_evidence:
    checker_source: "artifacts/R09/20260916T173216Z_tang_q411_stem_checker.py @ 9e21612abe0677b6577f8ef47c897e27fe402b81"
    checker_output: "artifacts/R09/20260916T173216Z_tang_q411_stem_checker.out @ 9ff9a8ee12a6bb2a5c30ce6ffac64c7d0c000b84"
    output_sha256: "372b380827bdd44f9d7f2cb97529c1bf6190cf319c15ac47e43868b8735bcb7e"
  audit_ids: []
  prior_art: "bounded dated search found no later resolution; finite-stem mechanism flagged as elementary/potential folklore, novelty not certified"
  old_R09_handoff: "critical Z3 SITE route retired from this slot; last report runs/R09/20260916T162904Z_7a42c1e9.md preserved"
```

No Gmail, Drive, public posting, purchases, permission changes, workflow execution, shared-ledger edits, peer-file edits, or scheduler changes were made.
