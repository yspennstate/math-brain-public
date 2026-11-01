Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. NO SOURCE-METRIC MOVEMENT: `7/sqrt(17) -> 7/sqrt(17)`; successor availability `E_ready: 0 -> 0`; methods #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES, #30 DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME.**

# R02 — successor gate + published dimension-six covering-radius barrier for the linear antipodal route

Worker: **R02**  
Lane: **CLOSABLE OUTSIDE**  
Canonical source: Afonso S. Bandeira, Anastasia Kireeva, Antoine Maillard, Almut Rödder, *Randomstrasse101: Open Problems of 2024*, arXiv:2504.20539v1, Open Problem 11 / intake `I0095`.  
Operational status after this run: **SUCCESSOR_ADMISSION_HOLD / NO ACTIVE MATHEMATICAL TARGET**. The retired I0095 route is not reopened by this handoff result.

## 1. Continuity, required reads, and ownership

I continued from the newest complete R02 report

`runs/R02/20260919T2130Z_successor_gate_linear_antipodal_dim5_obstruction_1_12_27_6f3a2c91.md`

created at commit `d3870ecc1fd64a2af32077442eb1b603d2708e24`. I did not restart from the stale native KLS title or from small sign matrices.

Before new mathematics I read/reconciled the current controlling material required by the owner:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical `operations/claims/I0095.md`;
- the current intake/search history for `I0095` and its old exact artifacts;
- the newest R02 report and the newest neighboring R13 discrepancy report;
- current CLOSABLE successor-gate/coordinator reports.

Canonical `operations/claims/I0095.md` still says **`PENDING_ADMISSION, not READY`**. The R02 source attack had already reached its six-unchanged-run retirement/handoff condition, so this run does not silently reset its stagnation count or reactivate it.

The exact repository comparison from the preceding R02 report commit `d3870ecc1fd64a2af32077442eb1b603d2708e24` to the frozen pre-report head `d35557f0ed632ab0778b904ccff86e72433b5604` is **94 commits ahead / 0 behind**, with `too_large = null`. The only canonical `operations/claims/*.md` mutations in that interval are `G0004.md` and `H0021.md`. Current gate reports reconcile `G0004` as explicitly released but **HARD OUTSIDE**, and `H0021` as assigned to R17 / **HARD OUTSIDE**. The latest independent CLOSABLE admission screens still certify no free `READY + CLOSABLE OUTSIDE + owner-clear + nonretired` successor. Therefore

`E_ready: 0 -> 0`.

No shared root, peer track, scheduler, workflow, email, Drive, permission, purchase, or public-posting state was changed.

## 2. Source/current-literature check

The official arXiv record for `2504.20539` still exposes only **v1**, submitted **29 April 2025**. Its current HTML renders Open Problem 11 exactly as

\[
C^*=\sup_{n\in\mathbb N}\sup_{A\in\{\pm1\}^{n\times n}}
\frac{\operatorname{disc}(A)}{\sqrt n},
\]

and asks for its value. I found no later arXiv version that closes this exact real flat sign-matrix constant. This is a bounded current-source check, not a claim of worldwide openness.

The nearby real Boolean Komlós landscape has changed in September 2026: Akbas--Sra, arXiv:2609.20785 (17 September 2026), give Boolean small-ball discrepancy machinery and recover Komlós among their applications; the neighboring R13 track also records current real Komlós dimension-free results. These concern the larger unit-column class and do not determine the exact flat sign-matrix lower-witness constant in Open Problem 11.

## 3. Stable R02 source metric

The retained explicit order-17 matrix remains independently audited by R01 over all `2^16 = 65,536` projective signings:

- discrepancy `7`;
- ratio squared `49/17`;
- independent audit verdict `PASS`.

Thus the frozen source metric remains

\[
\boxed{C^*\ge \frac7{\sqrt{17}}=1.697749375\ldots}.
\]

No stronger explicit sign matrix was certified this run. Open Problem 11 remains **PARTIAL / OPEN**, not PROVED or REFUTED.

## 4. Method #17 — look for the same numbers in coding theory

The preceding R02 run translated a complement-closed linear antipodal construction into a low-dimensional binary linear covering-code question and then independently proved a dimension-at-most-five obstruction by a Walsh-support argument.

Instead of extending that finite enumeration, I searched for the least-covering-radius function itself. The relevant primary source is:

Tsonka Baicheva and Iliya Bouyukliev, **“On the least covering radius of binary linear codes of dimension 6,”** *Advances in Mathematics of Communications* 4 (2010), 399–404, DOI `10.3934/amc.2010.4.399`.

They define `t_2[n,k]` as the minimum covering radius among binary linear `[n,k]` codes. Their Theorem 4.1 proves the exact formula

\[
\boxed{t_2[n,6]=\left\lfloor\frac{n-8}{2}\right\rfloor\qquad(n\ge18).}
\]

The same paper explicitly says that the values of `t_2[n,k]` for dimensions up to five had already been determined in earlier literature. That gives an important provenance correction: R02's previous dimension-at-most-five Walsh proof can remain as an independent, self-contained complement-closed derivation, but its broad low-dimensional covering-radius content must **not** be marketed as a novelty claim.

## 5. Method #22 — read the failure mechanism, not just the theorem statement

Baicheva--Bouyukliev's proof section explains why dimension six is a sharp finite classification problem rather than a place to continue blind R02 enumeration. They reduce the remaining range through projective-code classifications and covering-radius checks, obtain the exact values through length 63, and then use repeated coordinates for the recurrence beyond 63. In particular they record

\[
t_2[62,6]=t_2[63,6]=27.
\]

So the exact published obstruction already contains the information R02 would otherwise have tried to rediscover one order at a time.

This also exposes the correct next boundary: a linear antipodal code with at most `2n` codewords cannot have dimension seven until `2n>=128`, i.e. until `n>=64`.

## 6. Method #30 — localize one dimension/range and close it completely

Use the exact R02 sign-matrix/covering-code dictionary. If a sign matrix produces an antipodal row code `C_A`, then

\[
\operatorname{disc}(A)=n-2R(C_A).
\]

Suppose `C_A` is binary linear and has at most `2n` codewords. For every `32<=n<=63`,

\[
|C_A|=2^k\le2n<128,
\]

so `k<=6`.

If `k<=5`, the preceding R02 theorem gives discrepancy at most `6` for even `n` and at most `5` for odd `n`. If `k=6`, the published exact theorem gives

\[
R(C_A)\ge t_2[n,6]=\left\lfloor\frac{n-8}{2}\right\rfloor,
\]

hence

\[
\operatorname{disc}(A)\le
\begin{cases}
8,&n\text{ even},\\
9,&n\text{ odd}.
\end{cases}
\]

These caps are already strictly below the normalized A17 certificate. For even `n>=32`,

\[
\frac8{\sqrt n}\le\frac8{\sqrt{32}}=\sqrt2<\frac7{\sqrt{17}}.
\]

For odd `n>=33`,

\[
\left(\frac9{\sqrt n}\right)^2\le\frac{81}{33}=\frac{27}{11}
<\frac{49}{17},
\]

with the exact integer comparison

\[
27\cdot17=459<539=49\cdot11.
\]

Combining with the preceding dimension-at-most-five range gives the handoff theorem:

> **LINEAR-ANTIPODAL ROUTE ELIMINATION THROUGH ORDER 63.** No complement-closed binary linear covering-code construction with at most `2n` codewords can improve the explicit A17 normalized discrepancy bound at any order `n<=63`.

This is a **route-elimination synthesis**, not a new covering-code theorem. The dimension-six input is published prior art. Novelty is **not claimed**.

## 7. Exact corollary check

I wrote the mathematical idea before code, then made only the small exact checker warranted by the new synthesis:

- `artifacts/R02/20260919T2208Z_linear_dim6_covering_radius_bridge_idea.md`
- `artifacts/R02/20260919T2208Z_linear_dim6_covering_radius_bridge_check.py`
- `artifacts/R02/20260919T2208Z_linear_dim6_covering_radius_bridge_check.out`

The checker uses exact rational arithmetic for every order `32..63`. It verifies all 32 normalized comparisons against `49/17`, finds the worst dimension-six cap at `n=33`, ratio squared `27/11`, and returns `PASS`. This checker validates the elementary corollary from the published theorem; it does not purport to re-certify the 2010 classification proof.

## 8. What this changes in the handoff

Do **not** spend a future R02 run searching complement-closed binary linear codes of dimension at most six or orders at most 63. That entire linear route is now covered by the preceding R02 dim<=5 proof plus published exact dim-6 covering-radius prior art.

If I0095 is deliberately and lawfully reactivated later, the linear branch first becomes nontrivial again at **dimension 7 / order 64**. The more promising alternatives remain nonlinear antipodal codes, a genuinely different flat-matrix orbit, or an asymptotic central-shell construction. This report does not authorize reopening the retired route now.

The newest R13 neighboring report moves its finite general Boolean-Komlós obstruction at `n=86` from `2.264655` to `2.2647288`, while its owner-fixed upper metric remains unchanged. That is real neighboring progress but remains in the larger general unit-column class and does not move R02's explicit flat-sign lower-witness metric.

## 9. Stuck/rotation status

The old I0095 source metric itself has already exceeded the CLOSABLE six-unchanged-run limit and is retired/handoff. This run therefore does not increment a synthetic fresh stagnation count for the retired target. The active slot remains a successor-admission hold with `E_ready=0` because no lawful free READY CLOSABLE successor was present in the frozen gate state.

## 10. Model / scheduler control truth

The scheduler/control surface exposed to this context still provides task identity/title, prompt, schedule/timing, enabled state and ordinary update operations, but **no binding model-family selector, no reasoning-effort selector, no authenticated applied-runtime model/effort receipt, and no guaranteed-duration field**. GPT-6/maximum therefore remains prompt-only here.

The historical P26 `You cannot modify this task` case is an authorization-context issue. The compliant workaround is to use that same task from its owning/authorized workspace/API/admin context or platform support. Do not duplicate it or bypass permissions. No scheduler change was attempted in this run.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R02
  actual_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  requested_model: GPT-6 maximum
  requested_model_verified: false
  lane: CLOSABLE_OUTSIDE
  canonical_target: I0095
  canonical_claim_state: PENDING_ADMISSION_NOT_READY
  operational_target_state: RETIRED_HANDOFF
  slot_state: SUCCESSOR_ADMISSION_HOLD
  source_status: OPEN_PARTIAL
  fixed_metric: greatest certified explicit sign-matrix lower bound for C_star
  metric_before: 7/sqrt(17)
  metric_after: 7/sqrt(17)
  witness_order_before: 17
  witness_order_after: 17
  witness_discrepancy_before: 7
  witness_discrepancy_after: 7
  movement: NO_SOURCE_METRIC_MOVEMENT
  successor_metric: E_ready
  successor_before: 0
  successor_after: 0
  methods: [17, 22, 30]
  preceding_methods: [1, 12, 27]
  new_handoff_result: LINEAR_ANTIPODAL_NO_IMPROVEMENT_THROUGH_N63
  result_scope: complement-closed binary linear antipodal codes with at most 2n words
  published_input: "Baicheva-Bouyukliev 2010, t_2[n,6]=floor((n-8)/2) for n>=18"
  exact_corollary_check: PASS
  novelty: NO_COVERING_CODE_NOVELTY_CLAIM_PRIOR_ART_SYNTHESIS
  prior_art_correction: "dimension<=5 least-covering-radius values were already determined in earlier literature"
  next_linear_boundary_if_reactivated: "dimension 7, n>=64"
  predecessor_commit: d3870ecc1fd64a2af32077442eb1b603d2708e24
  frozen_pre_report_head: d35557f0ed632ab0778b904ccff86e72433b5604
  compare_ahead: 94
  compare_behind: 0
  compare_too_large: null
  canonical_claim_mutations_seen: [G0004, H0021]
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_changed: false
  email_or_drive_used: false
  public_posting: false
```
