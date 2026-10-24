Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — NO MOVEMENT in the frozen Tang curvature metric: **UNBOUNDED ABOVE -> UNBOUNDED ABOVE**; supported unchanged count is **1** because the immediately preceding Tang run moved the metric. New-method moves actually tried this run: **B6 DEFORM TO A POINT YOU CAN SOLVE, B14 FIND THE GROUP ACTING, B22 READ THE FAILURES, NOT THE SUCCESSES**. The scheduler interface exposed to this worker still has no model selector and no reasoning-effort selector, so GPT-6/maximum remains prompt text rather than a verified runtime setting.

Problem/source: Pengfei Tang, *A note on some critical thresholds of Bernoulli percolation*, arXiv:2012.01135v2 / Electron. J. Probab. 28 (2023), **Question 4.11 in the PDF**: for a transitive graph or a periodic rooted tree, is the Bernoulli bond-percolation probability `theta(p)` concave on `(p_c,1)`?

Mathematical status after this run:

- the literal universal Question 4.11 already has a negative answer through the periodic-tree class from the preceding R09 runs;
- this run proves a structural finite-stem theorem explaining why the broad periodic-tree formulation is unstable under the source's own periodicity definition;
- the transitive-graph-only variant remains OPEN; this run attacks one natural transitive Cayley family exactly and finds **strict concavity**, not a counterexample;
- the frozen periodic-tree curvature metric was already unbounded above, so it cannot move further;
- one genuinely independent OTHER-track audit is now recovered: `R08-AUDIT-R09-TANG-Q411-PERIODIC-01 = PASS`; a P26 audit of this Tang claim is still absent, so the owner closure protocol is **not complete**.

No paper folder is created yet because closure requires both independent audits.

# 1. Continuity, source locator, ownership, and current status

I continued from the newest own immutable report rather than restarting:

`runs/R09/20260916T1832Z_tang_q411_strong_counterexample.md`.

That report proved two facts:

1. for the fixed stem-into-binary family `T_k`, the curvature is unbounded above on admissible interior parameters;
2. the three-type strongly connected directed-cover matrix
   `[[0,1,1],[1,1,0],[2,1,2]]`
   has a physical branch with `theta''(17/50)>4929/1000`, so the negative periodic-tree answer is not merely a reducible-stem pathology.

Before new mathematics I reread or queried the controlling repository state: campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical claim `operations/claims/TANG-2020-Q4.11.md`, the newest own report, the newest neighboring R08 material, the current P26 audit stream, and the latest R10 reports/package search. The large intake JSONL collections cannot be literally rendered row-by-row through the connector before truncation; I used target/author/formula/ownership searches and record that access limitation instead of claiming a fictitious complete visible read of all intake rows.

The shared Tang claim file remains owner `R09` with coordinator-side label `PENDING_ADMISSION`. The research-side current-literature and ownership checks have already been completed in the two preceding Tang runs; I did not mutate this shared claim file. Root `POSTED.md` contains no Tang-Q4.11 exclusion and repository search still finds no competing owner for this exact source scope.

## Exact locator correction

The current arXiv **PDF** v2 is authoritative for the locator used by the owner prompt. On PDF page 15 it states:

`Question 4.11. For a transitive graph or a periodic tree with root o, is the percolation probability theta(p) concave on (p_c,1)?`

The arXiv HTML renderer currently shifts several environment numbers and displays this item as Question 4.12. The PDF itself is unambiguous and matches the owner instruction: **Question 4.11**.

Tang Definition 4.1 says that `T` is `N`-periodic when for every vertex `x` there is an adjacency-preserving bijection from the forward subtree `T^x` to another forward subtree whose root has depth at most `N`. The definition does not require the finite type graph to be strongly connected. Strong connectivity enters Tang's later derivative theorem, not Question 4.11.

## Dated literature search, 2026-09-16

Fresh bounded searches included:

- exact title + `Question 4.11` + `concavity`;
- `percolation probability concave periodic tree counterexample Tang`;
- `directed cover percolation concavity theta`;
- Tang's later percolation publications and current citing material;
- exact stem mechanism phrases and the previously found formulas.

The current arXiv record remains `2012.01135v2` (1 March 2023), and no later primary source resolving the concavity question surfaced in this bounded search. Tang's later visible USF paper is on a different topic. Zhongyang Li's later site-cutset work cites Tang for the threshold/cutset theorem, not for Question 4.11. This is a bounded prior-art check, **not** proof of novelty or worldwide absence. The finite-stem mechanism below is elementary enough that it must be treated as potentially folklore until specialist review.

# 2. Recovered independent audit

The neighboring R08 report

`runs/R08/20260916T1828Z_i0082_strictstable_firstvariation_c84d2e.md`

contains the independent audit

**`R08-AUDIT-R09-TANG-Q411-PERIODIC-01 = PASS`.**

R08 did not trust the R09 checker: it independently rederived Tang periodicity for the stem tree, the binary-tail physical survival branch, and

`theta_3(p)=2p^2-p`, `theta_3''(p)=4>0` on `(1/2,1)`.

Thus one of the two owner-required OTHER-track audits is now durably present. Targeted repository search of the current P26 audit stream finds no P26 Tang-Q4.11 audit yet. Fleet closure remains pending that audit; repeated self-checks are not substituted for it.

# 3. B6 — structural finite-stem instability theorem

The first counterexample can be understood without solving any special binary recursion.

Let `T` be a rooted infinite tree with root `o`, and for integer `k>=1` let `S_k(T)` be obtained by attaching a new `k`-edge path above `o`; the new endpoint is the new root. Write `theta_T(p)` for the bond-percolation survival probability from `o` and `Theta_k(p)` for survival from the new root.

## Theorem R09-TANG-FINITE-STEM-INSTABILITY

Assume:

1. `T` is `N`-periodic in Tang Definition 4.1;
2. `p0 in (p_c(T),1)`;
3. `theta_T` is twice differentiable at `p0`.

Then:

- `S_k(T)` is `(N+k)`-periodic;
- `p_c(S_k(T))=p_c(T)`;
- for every `p`,
  `Theta_k(p)=p^k theta_T(p)`;
- for all sufficiently large `k`,
  `Theta_k''(p0)>0`.

### Proof

For a stem vertex at depth at most `k`, the identity on its forward subtree is an admissible periodicity witness. For a vertex `x` lying in the original `T`, use the `N`-periodicity map already supplied in `T`. Its target root had old depth at most `N`, hence has new depth at most `N+k`. Therefore `S_k(T)` is `(N+k)`-periodic.

The new root percolates to infinity exactly when all `k` stem edges are open and the old root percolates in `T`. Independence gives the exact identity

`Theta_k(p)=p^k theta_T(p)`.

It follows immediately that the critical probability is unchanged.

Twice differentiating gives

`Theta_k''(p0)=p0^(k-2) [ k(k-1) theta_T(p0) + 2 k p0 theta_T'(p0) + p0^2 theta_T''(p0) ]`.

Because `p0>p_c`, `theta_T(p0)>0`. The percolation probability is nondecreasing in `p`, so at a differentiability point `theta_T'(p0)>=0`. The final term is a fixed finite number. Hence the positive quadratic term

`k(k-1) theta_T(p0)`

dominates as `k -> infinity`, proving `Theta_k''(p0)>0` for all sufficiently large `k`.

QED.

### Consequence

Tang's broad periodic-tree class is closed under finite root stems, and **any** periodic tree having one smooth supercritical point generates a periodic counterexample after a long enough finite stem. Tang's own strongly connected finite-type trees are analytic on `(p_c,1)`, so this mechanism applies immediately to them before any special elimination is done.

This explains the earlier binary witness structurally: the obstruction is not the binary formula itself but closure of the source class under finite series extensions at the distinguished root.

This theorem does not move the frozen metric because the preceding run already proved the metric is unbounded above in the fixed `T_k` family. It does substantially simplify the mechanism a paper would present.

# 4. B14 — attack the transitive half through a Cayley block graph

The periodic half is already dead, so I used group symmetry to test whether the same curvature reversal might survive after imposing vertex transitivity.

Take

`Gamma = C_3 * C_3 = <a,b | a^3=b^3=e>`

with symmetric generating set

`S={a,a^{-1},b,b^{-1}}`.

Its Cayley graph is connected, simple, 4-regular and vertex-transitive. It is a tree of triangles: every vertex lies in one `a`-triangle and one `b`-triangle, and the incidence graph of these blocks is a tree.

Explore percolation through one fresh triangle entered at one vertex. Let `X` be the number of the other two triangle vertices connected to the entry vertex using edges of that triangle. Exact enumeration gives

`P(X=0)=(1-p)^2`,

`P(X=1)=2p(1-p)^2`,

`P(X=2)=p^2(3-2p)`.

Because different descendant triangle blocks have disjoint edge sets and the block-incidence graph is a tree, a branch is an ordinary Galton-Watson process with offspring pgf

`phi(t)=(1-p)^2 + 2p(1-p)^2 t + p^2(3-2p)t^2`.

Let `q` be its extinction probability. The fixed-point polynomial factors exactly as

`phi(t)-t=(t-1)[p^2(3-2p)t-(1-p)^2]`.

The offspring mean exceeds one exactly when

`h(p):=p^2(3-2p)-(1-p)^2 = -2p^3+2p^2+2p-1 > 0`.

Moreover

`h'(p)=2(1-p)(3p+1)>0` on `(0,1)`, and exact arithmetic gives

`h(2/5)<0<h(41/100)`.

Thus there is a unique

`p_c in (2/5,41/100)`.

For `p>p_c`, the physical extinction root is the smaller root

`q=(1-p)^2/[p^2(3-2p)] < 1`.

The root belongs to two independent initial triangle blocks, so

`theta_G(p)=1-q^2`.

Differentiation gives

`theta_G''(p) = -12(1-p)^2 R(p) / [p^6(3-2p)^4]`,

where

`R(p)=2p^4-12p^3+30p^2-34p+15`.

The sign is exact because `R` has the positive Bernstein representation

`R(p)=15(1-p)^4 + 26p(1-p)^3 + 18p^2(1-p)^2 + 6p^3(1-p) + p^4`.

Hence

**`theta_G''(p)<0` for every `p in (p_c,1)`.**

So this natural transitive Cayley candidate is strictly concave and is **not** a counterexample. This is a useful failed attack: the finite-stem mechanism relies on a distinguished finite series decoration, while genuine vertex transitivity destroys exactly that asymmetry in this block-tree model.

I do **not** infer the universal transitive-graph half from this one graph. Its status remains OPEN.

# 5. B22 — read the source's failure modes rather than adding another candidate

The source itself is informative about what Tang expected. Example 4.10 computes several periodic directed-cover examples and explicitly checks concavity before posing Question 4.11. The subsequent strong-connectivity lemmas prove analyticity and uniqueness of the positive fixed-point branch, but no argument there is invariant under adding a finite unary stem above the distinguished root.

That is the exact structural gap exploited by Section 3: Question 4.11 uses the broad rooted periodic definition, whereas the pleasant multitype derivative theory is local to the irreducible core and does not control arbitrary finite root decoration.

The current literature search did not reveal a published discussion of this finite-decoration obstruction. I therefore record it as **potential folklore / uncited elementary mechanism**, not as a novelty-certified theorem.

For the transitive half, the Cayley calculation in Section 4 shows why simply replacing the rooted stem by a symmetric tree-of-blocks does not reproduce the effect: in the first natural example the physical extinction equation collapses to a quadratic whose exact curvature is negative throughout the supercritical interval.

# 6. Exact self-check

New substantive artifact:

`artifacts/R09/20260916T192944Z_tang_stem_operator_checker.py`

creation/readback commit

`eae951b2c7ff722f5a11303bf2237214c0b7defe`.

Archived PASS output:

`artifacts/R09/20260916T192944Z_tang_stem_operator_checker.out`

creation/readback commit

`78fb7495976b735bbdd066bd02fae2c3a2612682`.

Local executed-output SHA-256:

`8f9700cdc910e8b8cc01ad4ca32d6b5372b4bb4aa4700634feeeb69c62d522fb`.

The checker uses exact symbolic/rational arithmetic to verify:

- the triangle-block offspring probabilities and pgf factorization;
- the exact critical equation and rational bracket `2/5 < p_c < 41/100`;
- the physical extinction formula above threshold;
- the exact formula for `theta_G''`;
- the positive Bernstein identity for `R`;
- the general stem second-derivative identity;
- the retained concrete witness `theta_3''=4`.

The checker is a self-check. The theorem-sized arguments are written on this page.

A spreadsheet-runtime warmup warning printed to stderr when the checker process started; the checker itself exited successfully and the archived stdout ends in `PASS`. No spreadsheet functionality is used in the proof.

# 7. Audit and package state

Current source-matching periodic-tree audit count:

1. `R08-AUDIT-R09-TANG-Q411-PERIODIC-01 = PASS` — independent rederivation;
2. P26 Tang audit — **not found yet** in the current P26 audit stream.

Therefore the periodic-tree result is mathematically refuted in R09 and independently confirmed once, but the owner-defined fleet closure gate is not yet satisfied. No `paper_Tang_Q4_11` folder is created prematurely.

The latest R10 reports now concern I0070. A targeted repository search still finds no `paper_I0070` package, so the directed R09->R10 package audit trigger is not treated as ready this run.

# 8. Model/scheduler escalation status

No new control became available this run. The exposed task-modification schema supports prompt/title/schedule/enabled/timing fields but **not** a model selector or reasoning-effort selector. Therefore this worker cannot make GPT-6/maximum a verified runtime setting from the available interface.

What would be required to change that honestly: either the product must expose model/reasoning fields in the authorized task interface, or the task must be edited from an owning workspace/UI that exposes those settings, with runtime metadata confirming the result. Prompt text alone is not verification.

The repository policy records earlier `You cannot modify this task` responses for P26/P01/P03 from some contexts and later successful P26 editing from a different authorized context. The legitimate workaround is to use the account/workspace/interface that actually owns the native task or platform support to repair ownership. Creating a duplicate task or bypassing the permission boundary is not authorized. No scheduler modification is attempted here.

# 9. What changed / next research route

The fixed metric cannot improve beyond `UNBOUNDED ABOVE`, so this is correctly labeled a **no-movement metric run**, not disguised as progress. The real advances are structural and diagnostic:

- a general finite-stem instability theorem explains the source-level periodic counterexample without special algebra;
- the first natural transitive Cayley/block-tree attempt is solved exactly and remains concave;
- one required independent audit has now been recovered.

The highest-value next actions are:

1. obtain the missing independent P26 end-to-end audit for the source-matching periodic-tree theorem; and
2. if research rather than closure work is still appropriate, attack the transitive-only variant through a **different** symmetry-preserving construction, not another rooted finite decoration. A natural next candidate class is a free product / graph-of-finite-blocks with unequal block reliability laws or a vertex-transitive replacement product where the effective passage map is not the quadratic triangle law.

Do not spend future runs increasing the already-infinite curvature metric.

# 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R09
  source: "Pengfei Tang, A note on some critical thresholds of Bernoulli percolation, arXiv:2012.01135v2 / EJP 28 (2023), PDF Question 4.11"
  target: "decide concavity of bond-percolation theta(p) on (p_c,1), with periodic-tree class first"
  metric: "greatest rigorous lower bound for theta''(p) at a certified admissible parameter in the fixed candidate tree family"
  before: "UNBOUNDED ABOVE"
  after: "UNBOUNDED ABOVE"
  moved: false
  unchanged_count: 1
  status: "PARTIAL/FLEET-NOT-CLOSED: periodic-tree universal assertion REFUTED; transitive-graph-only variant OPEN; 1/2 required audits recovered"
  new_claims:
    - "R09-TANG-FINITE-STEM-INSTABILITY: any periodic tree with one C^2 supercritical point becomes locally convex after a sufficiently long finite root stem"
    - "Cay(C3*C3,{a,a^-1,b,b^-1}) has strictly concave bond-percolation theta on its entire supercritical interval"
  exact_evidence:
    checker_source: "artifacts/R09/20260916T192944Z_tang_stem_operator_checker.py @ eae951b2c7ff722f5a11303bf2237214c0b7defe"
    checker_output: "artifacts/R09/20260916T192944Z_tang_stem_operator_checker.out @ 78fb7495976b735bbdd066bd02fae2c3a2612682"
    output_sha256: "8f9700cdc910e8b8cc01ad4ca32d6b5372b4bb4aa4700634feeeb69c62d522fb"
  audit_ids:
    - "R08-AUDIT-R09-TANG-Q411-PERIODIC-01=PASS"
  missing_audit: "P26 end-to-end Tang Q4.11 periodic-tree audit"
  ownership: "operations/claims/TANG-2020-Q4.11.md; owner R09; shared coordinator label remains PENDING_ADMISSION"
  next_methods: [1, 15, 23]
```

No Gmail, Drive, email, public publication, purchase, permission change, workflow execution, shared-root ledger edit, peer-file edit, or scheduler change was performed.
