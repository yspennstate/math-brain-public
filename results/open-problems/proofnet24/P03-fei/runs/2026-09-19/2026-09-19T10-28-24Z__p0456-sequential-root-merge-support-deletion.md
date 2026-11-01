Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`, and no saturated zero is converted into a stuck count. This run uses **#6 DEFORM TO A POINT YOU CAN SOLVE, #10 DERANDOMIZE, #25 COUNT THE SAME THING TWICE**. It independently rederives Claim 309's root-merge prefix by a sequential insertion/exchange argument, isolates the exact conservative over-omission in `d_a`, and packages the interaction proof into a deterministic support-deletion lemma whose probabilistic input is only codimension estimates plus Claims 308/303.

# P03 / P0456 run report — sequential root merge and deterministic support deletion

Run timestamp: **2026-09-19T10:28:24Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, audit-first screen, and source status

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run is

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T09-30-28Z__p0456-root-merge-sigma-completeness.md`,

creation commit `d154884c393a71364f35c2270c16bf4241059d85`, blob `a83631dddd8f83a8265905c3638ac3fb2fb7fc95`; its earlier exact-commit tail readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286, 288--309. Claim 309 remains the controlling repair for the false `r>=3` shortcut in Claims 302/304. This run does not reinstate that shortcut.

Before new mathematics I reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, current owner directive, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical P0456 claim, the newest complete P03 report, current task-health/ownership evidence, incoming P26 evidence, and neighboring P0457 only for nonduplication. The connector-rendered `FLEET_RULES.md`, owner directive, `POSTED.md`, `RESULTS.md`, `QUEUE.md`, and the long newest P03 report are large surfaces and were truncated by the connector; I do **not** represent those reads as byte-for-byte rereads. Exact target paths and current target-scoped records were recovered directly. The current coordinator snapshot `operations/task_health/runs/2026-09-19T101100Z/status.md` does not release or reassign P0456. `operations/claims/P0457.md` remains a distinct diameter problem owned by NM13-04.

### 1.1 Incoming outside-audit screen

The newest concrete P26 report recovered remains

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_11-59-00__run-report.md`,

blob `481a3f44b96cdd9639a2fc5e24fb6370b76592e7`.

It audits R06's Romero max-minus-three diagonal, not P0456. Fresh exact-string repository searches for `P0456`, `P0456 PASS`, `P03-P0456-POISSON-CRITICAL-WINDOW-288`, and the repaired source chain recover no P26 or genuinely distinct OTHER-track end-to-end P0456 PASS. The closure gate therefore remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No source-CLOSED label and no final paper package are created.

### 1.2 Fresh primary-source and literature check — 19 September 2026

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* **63**(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge PDF text and page screenshots were recovered successfully in this run. Section 1.1 on page 553 still says that connectivity is unknown throughout

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`

and explicitly attributes the gap to analytically simpler sufficient conditions, including the no-intersection condition used for isolated vertices. The same source says that a more elaborate or exact set of sufficient conditions could close the gap.

The requested source checkpoints were freshly verified:

- Lemma 10: the pair bad event satisfies `P(B)=O(k^3/n)`.
- Lemma 11: on each bad branch the one-root isolation probability has the source exponential upper bound `exp(-k + (1/2)sqrt(k) log k + O(sqrt(k)))`.
- Lemma 12: `P(I_1 I_2 \cap B)` has the corresponding extra `exp(-log n)` suppression.
- Lemma 13: exact conditional independence holds on the source good event `B^c`.
- Lemma 14: under the lower-window hypothesis `t'<-1/2`, `limsup E[I_1 I_2]/E[I_1]^2 <= 1`.
- Theorem 3: disconnectedness with high probability below the source `-1/2` coefficient frontier.
- Theorem 4: above the source `+1/2` frontier, every fixed bounded degree is absent with high probability.
- Theorem 5: for `k=floor(t log n)`, components from the source threshold `ceil(8.24/t)` through `n/2` are absent with high probability.
- Theorem 6: connectivity with high probability above the source `+1/2` coefficient frontier.

Fresh bounded searches for the exact title, DOI, authors, `bilateral preference random graphs`, connectivity/Poisson/isolated-vertex follow-ups, and current author pages recovered the Cambridge article, its 2022 arXiv predecessor, current bibliographic records, and Hossein Dabirian's current page listing this work, but no later source-matching constant-window connectivity/Poisson theorem. This is bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

---

## 2. Inherited root-merge repair and the exact question for this run

Fix `r` distinguished roots

`R={v_1,...,v_r}`.

Delete every root--root edge. At root `a`, order the outside incident raw edge weights increasingly:

`x_{a,1}<x_{a,2}<...<x_{a,n-r}`,

and let `u_{a,j}` be the outside endpoint of `x_{a,j}`. The deleted-array proposal deadlines are

`D_{a,j}=x_{a,j}`, `1<=j<=k`,

with terminal threshold

`T_a=x_{a,k}`.

For a root--root edge `e={v_a,v_b}`, Claim 309 calls it endpoint-active at `a` when

`W(e)<=T_a`,

and active if it is endpoint-active at at least one endpoint. Let

`d_a = #{e incident to v_a : W(e)<=T_a}`

and let `p` be the number of **unique** active root--root raw edges.

Claim 309 proved the safe simultaneous statement: after restoring every root--root edge, the outside prefix of ranks `1,...,k-d_a` is certainly still in root `a`'s final top `k`. The question in this run is whether a sequential deformation from root weights `+infinity` to their realized values gives exactly the same omission rule, and whether the whole collision/active-edge bookkeeping can be stated as a deterministic finite support-deletion theorem before any probability is used.

---

## 3. #6 DEFORM TO A POINT YOU CAN SOLVE — sequential root-edge insertion

The solvable point is the deleted-root graph: set every root--root weight to `+infinity`. Then each root's top `k` list consists exactly of its first `k` outside edges.

Now lower the root--root weights to their realized values **one edge at a time, in an arbitrary order**. Equivalently, insert the realized finite root edge into the current sorted incident list.

### Lemma 310.1 — sequential exchange/rank-stability lemma

Assume all incident weights are distinct. Fix a root `a`. After any number `t` of incident root--root edges have been restored, let `q_a(t)` be the number of restored root--root edges currently lying in root `a`'s top `k`. Then the outside edges in the current top `k` are **exactly**

`x_{a,1},...,x_{a,k-q_a(t)}`.

Moreover:

1. `q_a(t)` is nondecreasing and each insertion changes it by either `0` or `1`;
2. when `q_a` increases, the unique outside edge expelled is the current terminal outside edge `x_{a,k-q_a(t-)}`;
3. an edge whose realized weight exceeds the initial deleted-array threshold `T_a` can never enter the top `k` at any later stage;
4. if `q_a^*` is the final number of root--root edges in the merged top `k`, then the final selected outside set is exactly
   `x_{a,1},...,x_{a,k-q_a^*}`,
   and `q_a^*<=d_a`.

#### Proof

At time zero, `q_a(0)=0` and the statement is true by definition.

Suppose it is true immediately before inserting a root edge of weight `z`. The current top `k` contains `q=q_a(t-)` root edges and the first `k-q` outside edges. If `z` is heavier than the current `k`th order statistic, nothing changes.

If `z` is lighter than the current `k`th order statistic, it enters the top `k` and expels the current heaviest selected edge. There are only two possibilities.

- The expelled edge is a root edge. Then one root edge enters and one root edge leaves, so `q` is unchanged; the outside prefix is unchanged.
- The expelled edge is outside. Since the selected outside set is a prefix, its heaviest member is exactly `x_{a,k-q}`. The insertion expels that edge and increases the number of selected root edges from `q` to `q+1`. The selected outside set is therefore exactly `x_{a,1},...,x_{a,k-q-1}`.

This proves the induction and (1)--(2).

The current `k`th order statistic can only stay fixed or decrease as extra candidate edges are inserted. Hence if `z>T_a`, then already at time zero there are `k` outside weights below `z`, and later insertions cannot improve its rank into the top `k`. This proves (3). Therefore every root edge that is ever selected is endpoint-active relative to the original threshold, so `q_a^*<=d_a`. The exact final prefix statement is the induction at the terminal time. `square`

### 3.1 The safe omission count is generally not exact

The sequential proof exposes a useful distinction hidden by the simultaneous upper bound:

`d_a` = number of root edges below the **initial** outside threshold `T_a`,

whereas

`q_a^*` = number of root edges actually present in the **final** merged top `k`.

They need not be equal. Example: take `k=2`, outside weights `x_1=0.1`, `x_2=0.4`, and two root edges with weights `0.2` and `0.3`. Both are endpoint-active because both are below `T=0.4`, so `d=2`. Lower the `0.2` edge first: it enters and expels `0.4`; the current top two are `0.1,0.2`. The `0.3` edge then never enters. Thus `q^*=1<d=2`.

This is **not** a gap in Claim 309. It explains why Claim 309 deliberately omits the last `d_a` outside deadlines: it is a conservative deterministic suffix that is measurable from the deleted-array threshold and the finite active root-edge set, without solving the final root-edge exchange problem. Since `r` is fixed, `d_a<=r-1` is a bounded omission and Claim 303 is designed precisely for such bounded arbitrary omissions.

---

## 4. #25 COUNT THE SAME THING TWICE — simultaneous rank counting

The same final rule has a second derivation that does not use insertion history.

Let `q_a^*` be the number of root--root edges in root `a`'s **final** top `k`. Then exactly `k-q_a^*` outside edges occupy the remaining top-`k` positions. Because the outside weights are already ordered, those positions must be occupied by the first `k-q_a^*` outside weights. No later outside weight can appear while an earlier one is absent.

Also, every selected root edge has weight below `T_a`: otherwise the original first `k` outside weights would all be lighter, preventing it from entering the top `k`. Therefore `q_a^*<=d_a` and hence

`{x_{a,1},...,x_{a,k-d_a}} subseteq final top-k at a`.

This is exactly Claim 309's simultaneous prefix lemma.

The two counts agree:

- **sequential exchange** identifies each actual outside loss with a distinct insertion that raises `q_a` by one;
- **simultaneous rank counting** identifies the number of outside losses as the final root occupancy `q_a^*`.

The agreement is exact and insertion-order independent. No new repair is required.

The old `r>=3` counterconfiguration from Claim 309 must remain in the auditor-facing proof because it shows why one must count root-edge rank effects rather than declare a root edge that is initially early at both endpoints automatically bilaterally selected. The sequential lemma never makes that false inference.

---

## 5. #10 DERANDOMIZE — deterministic finite support-deletion lemma

The probability and the combinatorics can now be separated completely.

### 5.1 Finite deterministic data

Continue with the deleted root arrays. An **outside proposal occurrence** is a triple

`alpha=(a,j,u)`

meaning that root `v_a` has outside label `u=u_{a,j}` at rank `j<=k`, with deadline

`D_alpha=W(v_a,u)=x_{a,j}`.

Let `S` be the set of all outside labels appearing in the `rk` deleted-array proposal occurrences, and let

`E=V \ (R union S)`

be the completely external pool.

The deterministic input consists of:

1. the partition of the proposal occurrences into blocks of equal outside label;
2. the endpoint-active root-edge set and the counts `d_a`;
3. a set `H_S` of unique nonexternal raw competitor edges involving retained selected labels and vertices in `R union S`;
4. an omission map `O` satisfying the rules below.

### 5.2 Admissible omission rules

The omission map is required to obey four purely deterministic rules.

**(R) Root-merge suffix.** For each root `a`, all terminal deleted-array ranks

`k-d_a+1,...,k`

belong to `O`.

**(C) Collision blocks.** In every equal-label block, either every occurrence is omitted, or the unique retained occurrence is the occurrence with the **globally smallest proposal deadline in that whole block**, and every other occurrence is omitted. In particular, if the globally smallest occurrence was already removed by rule (R), the whole collision block is omitted; a later occurrence is never promoted.

This global-minimum clause is essential: it ensures that every other root-to-the-same-label proposal edge is at least as heavy as the retained deadline, so an omitted same-block root proposal cannot reappear as an uncharged lighter competitor.

**(A) Active selected-label support.** Consider a retained occurrence `alpha=(a,j,u)`. If a raw edge

`e={u,y}`, `y in (R union S)\{u}`,

with `e != {u,v_a}` has weight below `D_alpha`, then `e` belongs to `H_S` and **every** retained deadline for which `e` is a lighter competitor is omitted. One raw edge is listed and charged only once even if it contaminates two retained deadlines.

**(N) No promotion after active deletion.** When a retained occurrence is removed by rule (A), no previously omitted occurrence in the same collision block is promoted. Thus deletions only shrink the retained set. The closure terminates after finitely many deletions.

### Claim `P03-P0456-SEQUENTIAL-MERGE-SUPPORT-DELETION-310`

**Status:** `PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

For any finite realization satisfying the data/rules above, every raw edge lighter than a surviving retained deadline `D_alpha` at its selected outside label `u` has its other endpoint in the completely external pool `E`, except for the owner proposal edge itself, which has weight exactly `D_alpha` and is not a lighter competitor. Consequently all unintegrated rejection randomness for label `u` is supported on

`B_u = {{u,x}: x in E}`.

For distinct surviving selected labels `u != z`, the raw-edge blocks `B_u` and `B_z` are disjoint. They are also disjoint from the deleted root-to-outside proposal arrays, the root--root raw family, and the explicitly integrated active finite-edge set. Hence the residual rejection blocks are **exactly independent** once the finite exposed/active data are fixed.

#### Proof

Fix a surviving retained occurrence `alpha=(a,j,u)` and a raw edge `e={u,y}` lighter than `D_alpha`.

If `y` is another root that also proposed `u`, then `e` is another proposal occurrence in the same collision block. Rule (C) says that `alpha` is the globally minimum deadline in that entire block. Therefore `W(e)>=D_alpha`, contradicting the assumption that `e` is lighter.

If `y` is a root that did **not** propose `u`, or if `y` is another selected outside label in `S`, then `y in R union S` and `e` is a nonexternal competitor. By rule (A), if it were lighter than `D_alpha`, every deadline it contaminates, including `alpha`, would be omitted. Since `alpha` survives, this is impossible.

Thus every lighter competitor has `y notin R union S`, i.e. `y in E`. This proves the support statement.

Now take distinct surviving labels `u` and `z`. If a raw edge belonged to both `B_u` and `B_z`, it would have to be `{u,z}`. But `z notin E` because `z in S`. Hence the blocks are disjoint. By construction they contain no root--outside proposal edge, no root--root edge, and no explicitly integrated nonexternal active edge. Since the base model uses independent raw edge weights, disjoint blocks are exactly independent. `square`

### 5.3 What the lemma does and does not claim

This is deliberately a **support-deletion lemma for necessary rejection constraints**, not an equivalence characterization of joint isolation. A root--root edge that enters one root's final top `k` creates an additional requirement for joint isolation: it must fail bilateral selection at the other endpoint. In an upper bound we may ignore that extra necessary condition. The lower bound remains the clean sufficient event from Claim 306, where all root--root edges are late and no such issue occurs.

This distinction prevents the false `r>=3` shortcut from re-entering the proof through a different name.

---

## 6. Probabilistic layer after derandomization

Once Claim 310 is stated deterministically, the probabilistic fixed-`r` proof has only three defect costs plus the analytic rejection input.

### 6.1 Collision excess `c`

After root--root deletion, each root's outside proposal labels are a uniform ordered sample without replacement from the outside vertices; different root arrays are independent at the raw-edge level. For fixed `r` and `k=O(log n)`, a prescribed equality pattern with collision excess `c` costs

`n^{-c+o(1)}`.

### 6.2 Active selected-label edges `q`

Each unique active selected--selected raw edge has an independent Uniform`[0,1]` weight and must fall below an `O(k/n)` proposal deadline on the threshold guard, so it costs `O(k/n)`.

A root-to-selected-label cross edge at a root that did not select that label is, conditional on the exposed terminal threshold `T=t` and nonselection, exactly Uniform`[t,1]`. Hitting an applicable `O(k/n)` deadline therefore again costs `O(k/n)` on the guard. A unique raw edge that contaminates two deadlines is charged once and both deadlines are omitted.

Thus a prescribed set of `q` unique active nonexternal selected-label edges costs `n^{-q+o(1)}`.

### 6.3 Active root--root edges `p`

Conditional on all deleted-array outside proposal data, the root--root raw family is independent. An edge `{v_a,v_b}` is active only if

`W(e)<=max(T_a,T_b)`.

On the threshold guard this has probability `O(k/n)`. Therefore a prescribed set of `p` unique active root--root edges costs `n^{-p+o(1)}`. An edge endpoint-active at both roots is still one raw variable and is charged once, although rule (R) may omit one terminal slot at each endpoint.

### 6.4 Residual rejection cost

After the deterministic omissions, Claim 310 gives literal disjointness of the residual external blocks. Claim 303's arbitrary bounded-omission estimate therefore applies root by root and gives, for every fixed repaired positive skeleton,

`P(residual necessary rejections | skeleton) <= exp[-rk+o(k)]`.

The witness-labelled count for fixed defect complexity `K=c+q+p` is `k^{O(K)}=n^{o(1)}`. Hence every positive-complexity skeleton has total mass at most

`e^{-rk+o(k)} n^{-1+o(1)} = o(e^{-rk})`.

The high-complexity tail remains controlled exactly as in Claims 304/305: each extra unique defect contributes another `O(k^A/n)` factor while witness choices are polynomial in `k`.

The zero-complexity branch uses Claim 308 at the actual clean quota `h=k`, while the lower fixed-root bound uses Claim 306's sufficient clean event. Therefore, with Claims 309 and 310 explicitly in force, for every fixed `r,C`, uniformly on `|k-log n|<=C`,

`P(I_{v_1}=...=I_{v_r}=1)=e^{-rk}(1+o_C(1))`.

This is a reorganization/self-audit of the existing source-matching proof, not a new source-level theorem claim.

---

## 7. Consequence chain and component check

The auditor-facing source chain remains:

1. Claim 308: clean one-root marked integral at actual quota `h=k` is `e^{-k}(1+o_C(1))`.
2. Claims 302/303/304/309/310: all fixed positive interaction clusters are lower order and the repaired fixed-`r` joint isolation asymptotic holds.
3. Fixed-r factorial moments of the isolated count `Z_n` converge uniformly to the factorial moments of `Poisson(lambda_n)`, `lambda_n=n e^{-k}`.
4. Claim 305's finite Brun/Bonferroni inequality is the sole TV conversion:
   `d_TV(Law(Z_n),Poisson(lambda_n))->0` uniformly on fixed `C` windows.
5. Literal nontrivial-component elimination implies
   `P(LK(n,k) connected)=e^{-lambda_n}+o_C(1)`.

The component layer was rechecked for scope only and is unchanged. For sizes `2--6`, delete all internal candidate-component edges before ordering external proposals; the light spanning-tree event uses internal raw edges and the external rejection event uses disjoint external raw edges. For sizes `7--n/2`, the one-global two-sided threshold envelope with `a=5/32`, `b=32/5` is paid once. The fixed `7--12` and geometric `13+` ranges remain as in Claim 306. No argument infers connectivity from mean degree.

---

## 8. Methods used, failures, and exact lessons

### #6 DEFORM TO A POINT YOU CAN SOLVE — success

Starting with root--root weights at `+infinity` makes the outside proposal arrays exact. Lowering root edges one at a time gives a one-exchange rank process. The process proves the exact prefix invariant and shows why endpoint activity controls only a bounded suffix.

The attempted stronger identity `number of lost outside proposals = d_a` **fails**. Endpoint-active edges can eject one another or fail to enter after an earlier insertion has lowered the current `k`th threshold. The correct exact count is the final root occupancy `q_a^*<=d_a`. Claim 309's use of `d_a` is therefore safely conservative, not exact.

### #10 DERANDOMIZE — success

The combinatorial core is now Claim 310, a deterministic finite support-deletion statement. Once its input partition/active sets/omission map are fixed, disjointness and independence follow solely from raw-edge support. Probability enters only through the codimension estimates `n^{-c}`, `n^{-q}`, `n^{-p}` and the analytic residual rejection bounds.

A key rule is **no promotion** after the global minimum of a collision block is deleted. Promoting a later same-label occurrence would reintroduce the lighter omitted root proposal as a hidden competitor. This is why Claim 302's minimum-deadline rule and Claim 310's deletion-only closure fit exactly.

### #25 COUNT THE SAME THING TWICE — agreement

Sequential insertion counts an outside loss whenever `q_a` increases. Simultaneous ranking counts outside losses as the final root occupancy `q_a^*`. Both give the same final outside prefix and the same safe `k-d_a` prefix. No discrepancy and no new gap were found.

No exact checker was manufactured. Claim 310 is a universal deterministic order-statistic/support theorem with no finite enumerative core whose verification would be strengthened by checking sample values; a finite script would only be a self-check and would violate the run's proof-first purpose.

---

## 9. Cumulative claim ledger delta

Preserve the existing ledger and add only the following interpretation/delta.

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 290 remains marked PPP; Claims 291--300 remain supporting self-audit/strengthening kernels.
- Claim 301 remains proved only with explicit repairs/strengthenings Claims 302--310.
- Claim 302 remains `PROVED / SELF-AUDIT-REPAIR / ROOT-MERGE-CLAUSE-REPAIRED-BY-309 / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 304 remains `PROVED / SELF-AUDIT-STRENGTHENING / ROOT-MERGE-CLAUSE-REPAIRED-BY-309 / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 308 remains `PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 309 remains `PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- New:
  `P03-P0456-SEQUENTIAL-MERGE-SUPPORT-DELETION-310 = PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

No source-level coefficient metric moves. `c_LK^cert=a_LK^fine=b_LK^sqrt=0` remain saturated and HARD recoveries remain `0/2`.

---

## 10. Exact remaining obligation and next attack

The mathematical source chain is still **audit-pending**, not CLOSED. The exact closure obligation remains:

1. one full independent P26 source-chain audit of the repaired Claims 288/289 path through the current capsule/repairs; and
2. one genuinely distinct OTHER-track full-proof audit of the same source-matching chain.

Self-checks, including Claims 301--310, count as neither outside audit.

The most useful next internal run should not create another correction coefficient. It should attack the repaired fixed-r proof at the **cluster-to-factorial-moment interface** with a finite adversarial normal form: prove that every positive-complexity interaction realization has a unique canonical charged support after deletion, or exhibit two different charge assignments for the same raw-edge realization that cause overcounting in the skeleton union bound. The source theorem needs only an upper cover, so nonuniqueness may be harmless; the exact task is to determine and state this without ambiguity.

A second useful route is to formalize the deterministic support lemma as a bipartite incidence graph between retained deadlines and nonexternal raw edges and prove the deletion operation is a monotone closure operator. That would expose whether the present `k^{O(K)}` witness count ever double-counts an unbounded family in a way that matters at `n^{-K+o(1)}` scale.

Suggested nonconsecutive Section-B triple for that audit: **#12 FIND WHAT IS CONSERVED, #19 MAKE IT AN ALGORITHM, #28 REPLACE FOR ALL WITH FOR TYPICAL**.

---

## 11. `ledger_delta` for P26/shared reconciliation

P03 does not edit shared root ledgers. The following is only the requested delta for P26/coordinator reconciliation:

```yaml
ledger_delta:
  track: P03
  source: P0456
  state: P0456_ACTIVE_AUDIT_PENDING
  outside_audits_found: 0/2
  fixed_metrics:
    c_LK_cert: 0
    a_LK_fine: 0
    b_LK_sqrt: 0
    hard_recoveries: 0/2
  preserve_claims: [274, 276, 278, 280, 282, 284, 286, 288-309]
  add_claim:
    id: P03-P0456-SEQUENTIAL-MERGE-SUPPORT-DELETION-310
    status: PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED
  repaired_chain_note:
    - Claims 302 and 304 must retain the Claim-309 root-merge repair.
    - Claim 310 independently rederives the safe terminal-suffix omission by sequential exchange and packages exact residual-support disjointness.
    - The old r>=3 both-end-impossible shortcut remains false and must never be restored.
  p26_request:
    action: full independent audit of repaired P0456 source-matching chain
    owner_self_audits_count: 0
  close_source: false
  create_paper_package: false
```

---

## 12. Runtime/model/tool boundary

The currently exposed scheduler/task-control surface still does not provide a binding model-family selector, binding reasoning-effort selector, or authenticated per-run reasoning attestation. The requested `GPT-6 / maximum` therefore remains prompt-only. This run actually identifies as **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**, so I do not claim GPT-6 at maximum.

No Gmail/email, Drive, public posting, paid compute, access/permission change, workflow execution, force push, unreviewed external script, or additional schedule was used.

Current protocol state after this run:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_310_SEQUENTIAL_SUPPORT_DELETION_READY`.

**End of complete run report.**