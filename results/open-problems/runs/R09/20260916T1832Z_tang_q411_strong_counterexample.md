Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — MOVEMENT: the fixed Tang-periodic-tree curvature metric moves from exact 4 to **UNBOUNDED ABOVE** in the same stem family `T_k`; new methods used this run: **B3 PROVE SOMETHING STRONGER, B16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, B24 FIND THE EXTREMAL OBJECT**. The scheduler still exposes no model selector or reasoning selector, so GPT-6/maximum remains prompt-only and is not claimed.

Problem/source: Pengfei Tang, *A note on some critical thresholds of Bernoulli percolation*, arXiv:2012.01135v2 / Electron. J. Probab. 28 (2023), Question 4.11. The source asks whether the Bernoulli **bond**-percolation probability `theta(p)` is concave on `(p_c,1)` for a transitive graph or a periodic rooted tree.

Mathematical status after this run: the literal universal Question 4.11 has a negative answer through the periodic-tree class; the transitive-graph-only variant remains OPEN. The previous finite-stem counterexample is strengthened here in two ways: (i) its curvature is unbounded over the already fixed stem family, and (ii) there is an exact counterexample inside Tang's **strongly connected finite directed-cover subclass**, so the phenomenon is not an artefact of a reducible finite stem. Fleet closure is still NOT CLOSED because the required two independent OTHER-track audits, including P26, have not yet appeared.

## 1. Continuity, source, ownership, and exclusions

I continued from the newest R09 report, not from scratch:

`runs/R09/20260916T173216Z_tang_q411_stem_counterexample.md`.

That report proved that the `k=3` stem-into-binary-tree example is periodic under Tang Definition 4.1, selected the physical fixed-point branch by decreasing finite-generation survival / greatest fixed point, and established

`theta_3(p)=2p^2-p`, `theta_3''(p)=4` on `(1/2,1)`.

The former R09 critical-SITE-percolation-on-Z3 route remains immutably retired from this slot, not solved; its historical reports/artifacts are untouched.

Before new mathematics this run I reread the controlling campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical claim `operations/claims/TANG-2020-Q4.11.md`, and the newest own report. I also checked the newest R10 report because R09 has a directed-audit duty when an R10 package is actually ready. The latest R10 I0070 report is explicitly an author-side proof candidate rather than a closure-ready self-contained paper package, and a targeted `paper_I0070` repository search returned no package, so I did not spend this research run pretending that an audit trigger had fired.

The canonical Tang claim is still owned by R09 and still carries the coordinator-side label `PENDING_ADMISSION`; attacking workers are not authorized to rewrite that shared file. Research-side admission checks are now complete to the extent accessible: the original source statement was reread, current-status/later-author/citing-paper searches were refreshed, `POSTED.md` has no Tang-Q4.11 exclusion, and repository searches for `2012.01135`, `TANG-Q411`, the exact problem phrase, `2p^2-p`, and finite-stem percolation found no competing research owner or posted/settled copy. This is a bounded search, not a worldwide novelty certificate.

The large intake JSONL collections cannot be literally materialized line-by-line into model context before connector truncation. I performed target/author/formula searches across the repository and record that access limitation rather than claim a fictitious complete 780-row visible reread.

The intake exclusion `I0055 / Lyons-Peres Question 5.16` remains respected: Tang's Theorem 1.6 answers Kahn's modified bond-percolation first-moment question and is not a reserve target for R09.

### Dated current-literature search, 2026-09-16

Fresh queries included:

- exact title + `Question 4.11` + `periodic tree` + `concavity`;
- `percolation probability concave periodic tree Tang`;
- `directed cover percolation concavity theta`;
- DOI `10.1214/23-EJP926` + `concavity`;
- `Pengfei Tang` + later percolation papers/citing papers;
- exact formulas / mechanisms such as `2p^2-p percolation tree` and finite stems.

The current arXiv record remains v2 (last revised 1 March 2023) and the 2023 EJP paper still contains Question 4.11. No later primary resolution surfaced. Tang's visible later work includes the 2024 USF-union paper, unrelated to this concavity question. Zhongyang Li's 2025 site-cutset paper cites Tang for threshold/cutset material, not for concavity. Negative search is not a novelty certificate; in particular the finite-stem multiplication mechanism is elementary enough to be potential folklore.

## 2. Source hypotheses that matter

Tang Definition 4.1 uses the standard broad periodic-tree definition: every forward subtree is rooted-isomorphic to one whose root lies within uniformly bounded distance of the original root. Equivalently, periodic trees are directed covers of finite directed multigraphs. Strong connectivity is an extra hypothesis in Tang's derivative results, not in Question 4.11.

For a finite directed-cover type matrix `A=(a_ij)`, the survival vector satisfies

`theta_i(p) = 1 - product_j (1-p theta_j(p))^(a_ij)`.

For a strongly connected finite type graph, the percolation threshold is the inverse Perron root of `A` (equivalently the associated irreducible multitype Galton-Watson mean matrix is `pA`), the physical survival vector is positive for `p>p_c`, and Tang's Lemma 4.14 gives uniqueness of the positive fixed point. Tang's Lemma 4.13 gives analyticity on the supercritical interval. Those source facts are used below to distinguish the physical branch from algebraic fixed points.

## 3. B3 — stronger theorem: finite stems generically destroy concavity

The previous counterexample family was

`T_k = k bond-edges in series above an infinite rooted binary tree`.

Its exact physical survival function is

`theta_k(p)=p^(k-2)(2p-1)`, for `p>1/2`,

and `p_c(T_k)=1/2`. Differentiating gives

`theta_k''(p)=(k-2)p^(k-4)[2(k-1)p-(k-3)]`.

The last report used `k=3`, for which the curvature is exactly `4`. The stronger structural statement is that this is not an isolated witness.

### Theorem R09-TANG-STEM-UNBOUNDED

For every integer `k>=4`, set

`p_k = 1 - 1/k^2`.

Then `p_k in (1/2,1)` and

`theta_k''(p_k) >= (15/16) k(k-2)`.

Consequently the curvature in the fixed candidate family `{T_k:k>=3}` is unbounded above:

`sup_{k>=3, p in (1/2,1)} theta_k''(p) = +infinity`.

#### Proof

At `p_k`,

`theta_k''(p_k)=(k-2)(1-1/k^2)^(k-4)[k+1-2(k-1)/k^2]`.

The bracket is strictly larger than `k`, because

`1-2(k-1)/k^2 = ((k-1)^2+1)/k^2 > 0`.

Bernoulli's inequality gives

`(1-1/k^2)^(k-4) >= 1-(k-4)/k^2`.

For every `k>=4`,

`(k-4)/k^2 <= 1/16`,

because this is equivalent to `(k-8)^2>=0`. Hence

`theta_k''(p_k) >= (15/16) k(k-2)`.

The right-hand side tends to infinity. QED.

This turns the frozen metric from the previous value `4` into **UNBOUNDED ABOVE**: for every finite `M` there is a completely source-admissible periodic tree `T_k` and an explicit admissible parameter `p_k` with `theta_k''(p_k)>M`.

This is more informative than simply choosing a larger finite `k`: finite rooted decorations are not a minor edge case for a universal concavity claim, because multiplication by powers of `p` can create arbitrarily strong positive curvature.

## 4. B16 — search the strongly-connected finite-type subclass

A reasonable objection to the first witness is that its finite stem makes its type graph reducible, whereas Tang obtains several clean derivative theorems for strongly connected directed covers. I therefore changed the counterexample search space rather than adding another stem lemma.

Exploratory small-type computations led to the three-type matrix

`A = [[0,1,1], [1,1,0], [2,1,2]]`.

The exploratory scan itself is not a theorem and I do not record its negative search portions as exact finite claims. The candidate it produced is certified exactly below.

The directed graph of `A` is strongly connected. Its characteristic polynomial is

`(lambda-3)(lambda-1)(lambda+1)`,

so its Perron root is `3` and

`p_c=1/3`.

Take the directed cover rooted at type `1` (zero-indexed middle row). This is a periodic tree in the source's class and also belongs to the strongly-connected subclass.

Write its survival vector as `(x_0,y,x_2)`. The fixed-point equations are

`x_0 = 1-(1-py)(1-px_2)`,

`y   = 1-(1-px_0)(1-py)`,

`x_2 = 1-(1-px_0)^2(1-py)(1-px_2)^2`.

The exact admissible parameter will be

`p_0=17/50 > 1/3`.

## 5. Exact elimination and physical-branch certification

From the second and first equations, for a positive solution with `py != 1`,

`x_0 = y(1-p)/(p(1-py))`,

and

`x_2 = y(p^3 y-p^2-p+1)/(p^2(1-py)^2)`.

Substitution into the third equation leaves a nonzero rational factor times the quartic

`P(p,y) =`

`p^6 y^4 -5p^5 y^3 -p^4 y^3 +10p^4 y^2`

`+p^3 y^3 +2p^3 y^2 -9p^3 y`

`-2p^2 y^3 +p^2 y^2 -3p^2 y +3p^2`

`+p y^3 +2p -y^3 +2y^2 -y -1`.

The exact symbolic checker verifies the identity

`E_2 / P = -y(p-1)/(p^2(py-1)^5)`

after the first two equations are solved, so no root in the interval below is introduced by the elimination denominators.

At `p=17/50`, exact Sturm arithmetic gives exactly one root

`y_* in [16112/10^6, 16113/10^6]`.

The same exact interval calculation reconstructs

`0 < x_0 < 1`, `0 < y_* < 1`, `0 < x_2 < 1`.

Hence this is a strictly positive fixed point. Since `A` is strongly connected and `p_0>p_c`, Tang's uniqueness lemma for positive fixed points identifies it with the actual physical percolation vector. Thus this step cannot accidentally select the ever-present zero/extinction algebraic branch.

## 6. Exact positive curvature in the strongly-connected subclass

Along the physical analytic branch `P(p,y(p))=0`,

`y' = -P_p/P_y`,

and

`y'' = -(P_pp + 2 P_py y' + P_yy (y')^2)/P_y`.

Write the resulting rational function as

`y'' = N(p,y)/D(p,y)`.

The denominator simplifies to `P_y^3`. On the exact root-isolating interval at `p=17/50`, the checker uses Sturm root counts to prove simultaneously:

1. `P_y<0` throughout the interval, so `D=P_y^3<0`;
2. `N-(4929/1000)D < 0` throughout the interval.

Because both the comparison numerator and denominator are negative,

`y''(17/50) - 4929/1000 > 0`.

Therefore

`theta_1''(17/50) > 4929/1000 > 0`.

### Theorem R09-TANG-Q411-STRONGLY-CONNECTED

Let `T` be the directed cover rooted at type 1 of the finite strongly connected directed multigraph with adjacency/count matrix

`A = [[0,1,1],[1,1,0],[2,1,2]]`.

Then `T` is a periodic rooted tree, `p_c(T)=1/3`, and at `p=17/50`

`theta_T''(p) > 4929/1000`.

In particular `theta_T` is not concave on `(p_c,1)`.

This is a source-level counterexample inside the strongly-connected finite-type periodic-tree subclass. It removes the possible concern that the negative answer depended only on a reducible finite stem.

## 7. B24 — extremal structure of the stem family

For completeness, the stem-family curvature is increasing in `p` for `k>=4`. Differentiating once more gives

`d/dp theta_k''(p) = (k-2)(k-3)p^(k-5)[2(k-1)p-(k-4)]`,

which is positive for `p>1/2`. Thus

`sup_{p in (1/2,1)} theta_k''(p) = (k-2)(k+1)`

(the limit as `p` tends to `1` from below). Letting `k` grow makes the source-compatible positive curvature quadratic in stem length. The explicit `p_k=1-1/k^2` argument in Section 3 avoids relying on an unattained endpoint and supplies interior admissible parameters.

The conceptual lesson is stronger than the first counterexample: the broad periodic-tree class is not stable under curvature sign because finite rooted extensions multiply the tail survival law by a polynomial factor in `p`, and even irreducibility does not restore concavity, as Section 6 shows.

## 8. Exact-arithmetic self-check

Substantive checker:

`artifacts/R09/20260916T1832Z_tang_q411_strongly_connected_checker.py`

creation/readback commit `9fbf38ab3dec54a7a4757c8d6d5b5d41b2dce341`.

Archived output:

`artifacts/R09/20260916T1832Z_tang_q411_strongly_connected_checker.out`

creation/readback commit `60ea1cf1622b83ef4f5541462a1f23fa6b409f85`.

Local executed-output SHA-256:

`b13dc782c9cc4fed22a67c45d0cf78c99c21afaa741ba1de10046bf67b6554d8`.

The output ends in `PASS`. The checker uses Python `Fraction` for the stem family and SymPy over exact rationals `QQ` with exact Sturm root counts for the strongly-connected candidate. No Monte Carlo or floating comparison enters any PASS assertion.

It verifies:

- previous `theta_3''(3/4)=4` and `theta_4''(3/4)=7`;
- the exact finite instances of the analytic unbounded-family inequality as a self-check;
- strong connectivity of the 3-type matrix;
- exact characteristic polynomial / Perron root `3`;
- the elimination identities;
- a unique quartic root in the rational interval;
- positive reconstructed fixed-point coordinates;
- nonvanishing/sign of `P_y` on the interval;
- the exact rational comparison `theta_1''(17/50)>4929/1000`.

The written inequalities in Sections 3 and 7 prove the all-`k` claims; the loop over `k<=100` is only a self-check.

## 9. Prior art and novelty qualification

The source/current-literature search still finds Tang's question open in the visible literature. The exact finite-stem mechanism and the 3-type matrix above did not appear in the bounded searches, but absence from search is not a novelty proof. The identity `theta_new=p^k theta_tail` after grafting a finite series stem is elementary and should be described as an elementary mechanism unless specialist prior-art review says otherwise.

The strongly-connected 3-type witness is less tautological and is the most important novelty-risk object for independent audit. It should not be advertised externally until the source hypotheses, elimination, physical branch and prior art are independently checked by P26 and a second distinct track.

## 10. Scheduler/model interface status requested by owner

The limitation remains, with one important historical/current distinction.

The exposed automation schema has fields for title, prompt, schedule, enablement and timing mode, but no model selector and no reasoning-effort selector. This runtime identifies the model as GPT-5.6 Sol and has no authenticated reasoning-effort telemetry, so reasoning is `UNVERIFIED`. Prompt text saying `Model: GPT-6. Reasoning: maximum` is only a request.

To make GPT-6/maximum enforceable, the authorized scheduler/product API would need model and reasoning-effort fields plus runtime telemetry, or the task would need to be managed through an authorized interface that exposes those controls. A repository edit cannot add that capability.

The repository policy records historical modification probes for P26/P01/P03 that returned `You cannot modify this task`. The newer root `RESULTS.md` also records that P26's full update later succeeded from a different authorized context, while another context saw explicit edit denials for the R-series native IDs. These facts are compatible: edit permission depends on the exposed account/workspace/native-task context. The permitted workaround for a task that still refuses modification is to use the authorized account/workspace/interface that owns it or platform support to repair ownership. Do not bypass the restriction and do not create a duplicate scheduled job.

This run made no scheduler change.

## 11. R10 directed-audit status

The newest R10 report is now on Agresti--Veraar Problem 6 / I0070. It labels its main statement an author-side full-source proof candidate and does not present a self-contained closure paper package; a targeted repository search found no `paper_I0070` package. Under the instruction to audit R10 **when a package is ready**, no new R10 audit is claimed this run. The previous R09 audits of older finite R10 packages remain historical and are not reused as audits of this new I0070 claim.

## 12. Status and closure obligations

Mathematical answer to Tang Q4.11 as literally universal over transitive graphs or periodic trees: **NO**, by a periodic tree. The stronger 3-type witness shows NO even within the strongly-connected periodic directed-cover subclass.

The transitive-graph-only subquestion remains OPEN and is not needed to falsify the literal universal question.

Fleet status remains **NOT CLOSED**. Missing closure obligations are:

1. P26 full end-to-end audit of the source-matching periodic-tree counterexample;
2. one independent full audit by a second OTHER track;
3. a publication-level prior-art review broad enough to distinguish an elementary/folklore finite-stem observation from a genuinely new source answer.

No audit IDs are invented.

## 13. Structured ledger delta

```yaml
ledger_delta:
  source: "Pengfei Tang, A note on some critical thresholds of Bernoulli percolation, arXiv:2012.01135v2 / EJP 28 (2023), Question 4.11"
  target: "Decide concavity of bond-percolation theta(p) on (p_c,1); periodic-tree universal assertion first"
  metric: "greatest rigorously certified lower bound for theta'' at an admissible parameter in the fixed stem family T_k"
  before: "4 exactly at (T_3,p=3/4)"
  after: "UNBOUNDED_ABOVE: for k>=4, theta_k''(1-1/k^2) >= (15/16) k(k-2)"
  status: "SOURCE UNIVERSAL NEGATIVE VIA PERIODIC TREE; strongly-connected periodic subclass also counterexample; transitive-only variant OPEN; fleet NOT_CLOSED"
  unchanged_count: 0
  exact_evidence:
    - "artifacts/R09/20260916T1832Z_tang_q411_strongly_connected_checker.py @ 9fbf38ab3dec54a7a4757c8d6d5b5d41b2dce341"
    - "artifacts/R09/20260916T1832Z_tang_q411_strongly_connected_checker.out @ 60ea1cf1622b83ef4f5541462a1f23fa6b409f85; PASS; SHA256 b13dc782c9cc4fed22a67c45d0cf78c99c21afaa741ba1de10046bf67b6554d8"
    - "strongly-connected witness A=[[0,1,1],[1,1,0],[2,1,2]], root type 1, p=17/50, theta''>4929/1000"
  audit_ids: []
  audit_status: "0/2 required OTHER-track audits found for this Tang claim"
  ownership: "operations/claims/TANG-2020-Q4.11.md; owner R09; shared label remains PENDING_ADMISSION"
```

## 14. Next research move

The periodic-tree half no longer needs more counterexample hunting. The next high-value activity is independent auditing and prior-art clearance. If both audits pass, produce the source-matching `paper_tang_q411_periodic_tree_counterexample/` package and retire the source-level universal question from R09 research.

If research continues before audits arrive, it should not inflate the already unbounded curvature metric. The only mathematically useful direction is the separate **transitive-graph-only** variant: ask whether vertex transitivity forbids the curvature mechanism that is now seen both in reducible and strongly-connected periodic trees. That would be a new scope and must receive its own source/metric treatment rather than being smuggled into the closed periodic-tree argument.

No email, Drive, public posting, purchase, permission change, workflow execution, scheduler mutation, shared-root edit, claim-file edit or peer-file edit was performed.
