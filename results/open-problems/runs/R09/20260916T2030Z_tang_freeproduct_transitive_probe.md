Model: **GPT-5.6 Sol. Reasoning: UNVERIFIED — NO MOVEMENT in the frozen Tang periodic-tree curvature metric: UNBOUNDED ABOVE -> UNBOUNDED ABOVE; supported unchanged count 2. Section-B moves actually tried: B1 CHANGE THE CATEGORY, B15 BREAK THE SYMMETRY ON PURPOSE, B23 DO WHAT THE PROPOSER DID NOT EXPECT.** The exposed scheduler interface still has no model selector or reasoning-effort selector, so GPT-6/maximum remains prompt text rather than a verified runtime setting.

Problem/source: Pengfei Tang, *A note on some critical thresholds of Bernoulli percolation*, arXiv:2012.01135v2 / Electron. J. Probab. 28 (2023), **Question 4.11 in the PDF**: for a transitive graph or a periodic rooted tree, is the Bernoulli bond-percolation probability `theta(p)` concave on `(p_c,1)`?

Mathematical status after this run:

- the periodic-tree universal assertion is already mathematically **REFUTED** by R09's source-admissible stem family, and the fixed curvature metric is already unbounded above;
- this run does not relabel the saturated metric as movement;
- the separate transitive-graph-only variant remains **OPEN**;
- this run proves a new exact transitive subclass theorem: the simple degree-three Cayley graph `Cay(C2*C3,{a,b,b^{-1}})` has `theta''(p)<0` on its entire supercritical interval;
- the free-product branching compiler used for that calculation is substantially prior art: Kozakova (2008) already reduces free-product percolation to factor-cluster quantities, so no novelty claim is made for the compiler itself;
- R08 has independently passed both the elementary periodic stem and the stronger strongly-connected finite-type witness; these two reports still count as **one independent auditor**, because they come from the same track;
- a targeted repository search still finds **no P26 Tang-Q4.11 audit**, so the owner-defined closure gate is not complete and no paper folder is created.

# 1. Continuity, source, ownership and current status

I continued from the newest own immutable report

`runs/R09/20260916T192944Z_tang_structural_counterexample_transitive_probe.md`

rather than restarting. That report retained the exact binary-stem counterexample, the unbounded-above curvature metric, the strongly-connected three-type directed-cover counterexample, and the structural finite-stem instability theorem. It also proved strict concavity for the transitive block graph `Cay(C3*C3)`.

Before new mathematics I reread or queried the controlling repository state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical claim `operations/claims/TANG-2020-Q4.11.md`, newest R09 history, newest R08 neighbor/audits, and the current P26 audit stream. The large intake JSONL trees cannot be literally rendered row-by-row through this connector before truncation; targeted Tang/source/ownership searches were used and that access limitation is recorded instead of claiming a fictitious complete visible reread of every intake row.

The canonical claim remains owned by R09 and retains its coordinator-side label `PENDING_ADMISSION`. Attacking workers are not authorized to mutate the shared claim file. Research-side source/status/ownership checks have nevertheless been completed to the accessible standard in the preceding Tang runs and were refreshed here: root `POSTED.md` contains no Tang-Q4.11 exclusion; repository searches for `2012.01135`, `TANG-Q411`, the exact concavity wording, the stem formulas and P26 audit identifiers find no competing owner or settled copy.

The current arXiv record remains `2012.01135v2`, last revised 1 March 2023. The PDF locator supplied by the owner is Question 4.11. The experimental HTML renderer has shifted the environment number in some renderings; the source statement is unchanged. Fresh bounded searches on 2026-09-16 for the exact question wording, periodic-tree concavity, directed-cover/free-product concavity, Tang's later work and citing material did not surface a later primary resolution. This is a bounded negative search, **not** a proof of novelty or worldwide absence.

# 2. Audit state recovered before research

Two independent R08 audit reports/certificates now exist:

- `R08-AUDIT-R09-TANG-Q411-PERIODIC-01 = PASS`;
- `R08-AUDIT-R09-TANG-Q411-STRONG-CONNECTED-02 = PASS`.

The second audit independently checked the strongly-connected three-type elimination identity, isolated the physical root, checked positive coordinates, verified `theta''(17/50)>4929/1000`, and checked the stem-unbounded formula. These are useful, but under the owner protocol both are still **one auditor**, namely R08.

A targeted repository search for `P26-AUDIT-R09` and `P26 Tang Q4.11` returns no Tang audit. Therefore the source-matching periodic-tree refutation is not fleet-closed yet. No paper folder is created prematurely.

# 3. B1 — CHANGE THE CATEGORY: free-product percolation as a two-type reliability/branching compiler

Let `Gamma=Gamma_1*Gamma_2` be a free product of finite groups, with finite symmetric generating sets on the factors. In its Cayley graph, factor cosets form finite blocks whose incidence structure is tree-like. Enter one factor-`i` block through a distinguished vertex. Let

`X_i = number of other vertices in the open component of the entry vertex inside that factor block`

and let

`F_i(p,z)=E_p[z^{X_i}]`.

If `u_i` is the extinction probability of the descendant exploration beginning with an entered type-`i` block, then the block-tree decomposition gives

`u_1=F_1(p,u_2),   u_2=F_2(p,u_1)`.

At a root lying in one block of each type, the two initial descendant systems use disjoint block-edge sets away from the root, so the root extinction probability is `u_1 u_2` and

`theta(p)=1-u_1u_2`.

The two-type offspring mean matrix is

`[[0,m_1],[m_2,0]]`,  where `m_i=partial_z F_i(p,1)`,

so its Perron root is `sqrt(m_1m_2)` and criticality occurs at `m_1m_2=1` when the product crosses one monotonically.

This compiler is **not claimed as new**. Iva Kozakova's 2008 paper *Critical percolation of free product of groups* already finds `p_c` of a free product in terms of expected factor-cluster sizes and explicitly uses a branching-process decomposition. The new use in R09 is to differentiate the exact physical branch and inspect concavity.

# 4. B15 — BREAK THE SYMMETRY ON PURPOSE inside a vertex-transitive graph

The previous transitive probe `Cay(C3*C3)` was highly symmetric between the two factor types and turned out strictly concave. I therefore broke the *local block symmetry* while keeping global vertex transitivity.

Take

`G = Cay(C2*C3,{a,b,b^{-1}})`,

where `a^2=e` and `b^3=e`, and interpret this as the **simple** Cayley graph: every vertex lies in one `a`-edge block and one `b`-triangle block. This graph is connected, simple, degree three and vertex-transitive.

For an entered `C2` edge block, the number of new vertices is Bernoulli(`p`), hence

`F_2(p,t)=1-p+pt`,   `m_2=p`.

For an entered triangle, let `X_3` be the number of the other two triangle vertices connected to the entry vertex using only triangle edges. Exact enumeration gives

`P(X_3=0)=(1-p)^2`,

`P(X_3=1)=2p(1-p)^2`,

`P(X_3=2)=p^2(3-2p)`.

Therefore

`F_3(p,t)=(1-p)^2+2p(1-p)^2 t+p^2(3-2p)t^2`

and

`m_3=2p(1+p-p^2)`.

The mean-product is

`M(p)=m_2m_3=2p^2(1+p-p^2)`.

Its derivative is

`M'(p)=2p(2+3p-4p^2)>0` on `(0,1)`,

because the quadratic is concave and is positive at both endpoints. Hence there is a unique critical point `p_c` satisfying

`H(p):=1-M(p)=2p^4-2p^3-2p^2+1=0`.

Exact rational evaluation gives

`63727/100000 < p_c < 3983/6250`.

## 4.1 Exact physical extinction branch

Let `u` be extinction after entering a `C2` block and `v` extinction after entering a triangle block. The fixed-point equations are

`u=1-p+pv`,

`v=(1-p)^2+2p(1-p)^2u+p^2(3-2p)u^2`.

Eliminating `v` gives exactly

`(u-1)[2p^4u-3p^3u+p^3-2p^2+1]=0`.

Thus the only possible `u`-coordinates of fixed points are the trivial value `1` and

`u_* = -(p-1)(p^2-p-1)/[p^3(2p-3)]`.

The corresponding second coordinate is

`v_*=(p-1)^2(2p^3-p^2-2p-1)/[p^4(2p-3)]`.

More revealingly,

`1-u_* = H(p)/[p^3(2p-3)]`,

`1-v_* = H(p)/[p^4(2p-3)]`.

For `p_c<p<1`, `H(p)<0` and `2p-3<0`. Thus `u_*,v_*<1`; their displayed formulas and the fixed-point equations give positivity. Since `M(p)>1`, the two-type Galton-Watson process is supercritical, so its extinction vector is strictly below `(1,1)`. There are only the two fixed points found above; consequently `(u_*,v_*)` is the **physical** extinction vector, not a spurious algebraic solution.

The two initial factor-block explorations are independent after the root, so

`theta_G(p)=1-u_*v_*`.

After simplification,

`theta_G(p) = H(p)(2p^5-3p^4-p^3+2p^2-1) / [p^7(2p-3)^2]`.

## 4.2 Exact curvature sign

Two differentiations give

`theta_G''(p) = 4(p-1)R(p)/[p^9(2p-3)^4]`,

where

`R(p)=4p^9-38p^8+106p^7-38p^6-254p^5+274p^4+171p^3-264p^2-84p+126`.

The sign is certified without numerical root finding. In the degree-nine Bernstein basis on `[0,1]`,

`R(p)=sum_{j=0}^9 b_j C(9,j)p^j(1-p)^(9-j)`

with

`(b_0,...,b_9) = (126,350/3,100,2185/28,3464/63,493/14,291/14,413/36,6,3)`.

Every coefficient is strictly positive, hence `R(p)>0` on `[0,1]`. Since `p-1<0` and the denominator is positive on `(p_c,1)`,

**`theta_G''(p)<0` for every `p in (p_c,1)`.**

So a second nontrivial globally vertex-transitive free-product example is strictly concave throughout the entire supercritical interval. This is a rigorous **PARTIAL** result for the transitive half, not a proof for all transitive graphs.

# 5. B23 — DO WHAT THE PROPOSER DID NOT EXPECT: compare against old free-product literature before trusting the candidate

Kozakova's primary 2008 free-product paper is the natural historical comparison. It proves, for its stated Cayley-graph convention on the modular group `PSL_2(Z)=C2*C3` with standard generators, a critical value approximately `0.5199`, the unique root of

`2p^5-6p^4+2p^3+4p^2-1=0`.

That is **not** the critical polynomial of the simple degree-three Cayley graph used in Section 4, whose exact polynomial is

`2p^4-2p^3-2p^2+1=0`.

The checker identifies the algebraic source of the discrepancy: if the order-two factor connection probability is replaced by

`1-(1-p)^2`

instead of the single-edge probability `p`, then multiplying it by the triangle offspring mean reproduces Kozakova's polynomial exactly. This is what would happen under a doubled-involution/parallel-bond convention.

I have **not** completed a source-level convention check proving that this is exactly how Kozakova's `standard generators` graph treats the involution, so I do not identify her model with that multiedge interpretation as a theorem. The safe conclusion is only: (i) her free-product branching mechanism is prior art; (ii) her published modular-group threshold uses a different edge-count convention from the simple degree-three graph certified here, or an equivalent convention distinction; and (iii) the exact polynomial discrepancy must be stated explicitly in any write-up rather than hidden.

Fresh bounded searches for `C2*C3`/modular-group percolation together with `theta(p)`, `concavity`, or `second derivative` did not surface a published curvature result. This is a bounded search, not a novelty certificate.

# 6. Metric and what actually moved

The frozen R09 metric is the greatest rigorous positive lower bound on `theta''` in the already-fixed periodic-tree candidate family. The preceding run proved this metric **UNBOUNDED ABOVE**. There is no larger finite value to report, and changing to a transitive subclass would be changing the metric.

Therefore:

- before: `UNBOUNDED_ABOVE`;
- after: `UNBOUNDED_ABOVE`;
- metric movement: **NO**;
- supported consecutive unchanged count: **2**.

The substantive progress is instead an exact transitive subclass theorem and a stronger prior-art map. This is recorded without disguising it as metric movement.

# 7. Exact self-check

Checker source:

`artifacts/R09/20260916T2030Z_tang_freeproduct_transitive_probe_checker.py`

creation/readback commit:

`4239108390c79e11d6109db0e6bcc33c193e3c2f`.

Archived PASS output:

`artifacts/R09/20260916T2030Z_tang_freeproduct_transitive_probe_checker.out`

creation/readback commit:

`b27d3ebc2442728f7338c43d8538eb56ca035d61`.

Executed-output SHA-256:

`33b3cf53e03ccd56702835c3ecd16b14c54b79e2ae56b1f012482d974091742f`.

The exact symbolic/rational checker verifies:

- both block reliability pgfs and their means;
- monotone critical mean product and exact rational `p_c` bracket;
- factorization of the fixed-point elimination polynomial;
- the explicit nontrivial fixed-point coordinates and their exact residuals;
- the closed form for `theta` and `theta''`;
- the positive Bernstein representation of `R`;
- exact recovery of Kozakova's published modular polynomial after replacing the order-two factor by the two-parallel-bond connection probability;
- the retained concrete periodic-tree sanity check `theta_3''=4`.

The checker is a **self-check**. The theorem-sized argument is written on this page.

# 8. Runtime/model and permission escalation

The limitation remains real. The task-control schema available to this worker exposes prompt, title, schedule, enabled-state and timing-mode controls, but no model field and no reasoning-effort field. Therefore this worker cannot honestly set or verify GPT-6/maximum from the current scheduler interface.

Making the request enforceable requires either (a) product/API support for explicit model/reasoning fields with runtime telemetry, or (b) editing the native task from the owning workspace/UI if that surface exposes those settings and then verifying actual runtime metadata. Prompt text alone is not verification.

The repository policy records that some native-task modification probes, including an earlier P26 probe, returned `You cannot modify this task`, while a later authorized context successfully updated P26. The legitimate workaround is the account/workspace/interface that actually owns the task, or platform support to repair ownership. Creating a duplicate job or bypassing the permission boundary is not authorized. No scheduler modification is attempted in this run.

# 9. Remaining obligation and next route

The periodic-tree source assertion already has a negative mathematical answer, and the metric is saturated. Closure priority is therefore sharply defined: **P26 must independently audit the source-matching periodic-tree refutation.** R08 supplies the distinct second auditor, but two R08 passes count as one auditor.

For research rather than packaging, the transitive-only variant remains genuinely open. Two natural free-product Cayley examples (`C3*C3` and the simple degree-three `C2*C3`) are now both strictly concave. The next run must not repeat B1/B15/B23. If the metric remains unchanged for one more consecutive run, the owner stuck protocol triggers. Planned next methods are **B7 TAKE THE LIMIT, B20 FIND WHY THE ALGORITHM FAILS, B30 ONE SCALE/ONE DIRECTION AT A TIME**: derive the curvature formula near `p_c` and `p=1` for a parameterized finite-block free-product family, identify the exact coefficient obstruction to positive curvature under vertex transitivity, and decide whether that obstruction is structural or whether a sporadic finite block can reverse it.

No email, Drive, public posting, purchase, permission change, scheduler modification, shared-root edit, peer-file edit or workflow execution is made.

```yaml
ledger_delta:
  source: "Pengfei Tang, A note on some critical thresholds of Bernoulli percolation, arXiv:2012.01135v2 / EJP 28 (2023), PDF Question 4.11"
  target: "Decide concavity of bond-percolation theta(p) on (p_c,1); source periodic-tree assertion first, transitive-only variant separately"
  metric: "greatest rigorously certified lower bound for theta'' at an admissible parameter in the fixed periodic-tree stem family"
  before: "UNBOUNDED_ABOVE"
  after: "UNBOUNDED_ABOVE"
  movement: false
  supported_unchanged_count: 2
  mathematical_status: "PERIODIC_TREE_REFUTED; TRANSITIVE_ONLY_OPEN; AUDIT_PENDING"
  new_result: "For the simple degree-three Cayley graph Cay(C2*C3,{a,b,b^{-1}}), theta''(p)<0 for every p in (p_c,1), with exact physical branch and positive Bernstein certificate."
  exact_evidence:
    checker_source_commit: "4239108390c79e11d6109db0e6bcc33c193e3c2f"
    checker_output_commit: "b27d3ebc2442728f7338c43d8538eb56ca035d61"
    output_sha256: "33b3cf53e03ccd56702835c3ecd16b14c54b79e2ae56b1f012482d974091742f"
  audit_ids:
    - "R08-AUDIT-R09-TANG-Q411-PERIODIC-01=PASS"
    - "R08-AUDIT-R09-TANG-Q411-STRONG-CONNECTED-02=PASS"
  audit_count_for_closure: "one distinct OTHER-track auditor (R08); repeated R08 audits do not count twice"
  missing_audit: "P26 end-to-end Tang Q4.11 periodic-tree audit"
  ownership: "operations/claims/TANG-2020-Q4.11.md; R09 owner; coordinator-side label remains PENDING_ADMISSION"
  next_methods: [7, 20, 30]
```
