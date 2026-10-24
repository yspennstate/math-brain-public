Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT: successor-admission metric `E_ready: 0 -> 0`; successor-gate unchanged count `2 -> 3`; STUCK RECOVERY 1; methods #1 CHANGE THE CATEGORY, #16 COMPUTE EVERY SMALL CASE, #25 COUNT THE SAME THING TWICE.**

# R19 CLOSABLE OUTSIDE — successor-admission stuck recovery 1

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: preserve I0084 exactly; do not reopen it

I continued from the newest R19 report

`runs/R19/2026-09-18_02-14-29_UTC__successor-gate-live-reconciliation_2f61.md`

and from the frozen I0084 handoff

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

The original frozen source is Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084. The source-version convention remains exactly:

- `S_t` may be the law of a classical or a free alpha-stable process;
- the initial law satisfies `int |x|^(2+alpha) dmu < infinity`;
- the arXiv-v2 conclusion uses **ordinary classical convolution** `mu * S_t`.

In particular, when `S_t` is the law of a free stable distribution, the asterisk is still ordinary classical convolution. I do not replace it by free additive convolution. The published ALEA formulation has materially different `*` / `boxplus` scope and its audits do not automatically certify the frozen arXiv-v2 ordinary-`*` package.

The fixed I0084 metric remains **2/2** at handoff. The minimal source-level package already records source-admissible endpoint counterexamples for the classical positive half-stable kernel and for the free-stable law used as an ordinary convolution kernel. This run earns **no new I0084 credit** and makes no new I0084 theorem claim. Stronger-moment/compact-support-only statements would remain restricted/PARTIAL, and posted Brownian/stable special cases remain excluded from new credit.

Repository closure of the frozen arXiv package is still blocked by exactly two missing audits: one P26 end-to-end PASS and one distinct OTHER-track end-to-end PASS, both explicitly on the ordinary-`*` arXiv-v2 package. The existing ALEA `boxplus` audits are not silently repurposed.

Fresh dated source/literature check, 2026-09-18: I searched the exact arXiv identifier/title plus `Conjecture 5.5`, stable eventual unimodality, and 2025–2026 follow-up terms. The original arXiv paper is still the primary source recovered. The search also recovered the authors' later multiplicative-unimodality work, but no later primary paper explicitly announcing a resolution of this exact frozen Conjecture-5.5 arXiv-v2 ordinary-`*` target. This is bounded negative evidence, **not** a novelty certificate.

## 2. Required repository-wide start state

Before the recovery I re-read the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current new-methods implementation manifest, the newest R19 report, current canonical claim files reached by the frontier scan, recent master commits, and neighboring successor-admission reports (notably the newest R20 and R15 gate reports). Relevant intake/source rows were recovered by exact ID/source retrieval rather than pretending that connector-truncated multi-hundred-line JSONLs were visually read byte-for-byte.

The root queue still states that newly certified READY entries are zero. Recent master activity created/moved several other tracks, including fresh claims, but did not create a free READY+CLOSABLE+UNASSIGNED row for R19 before this report was written.

## 3. Section-I blocker — exact statement

After two consecutive no-movement admission runs, this third one is a mandatory thinking/stuck recovery. The exact blocker is not a missing lemma on a chosen theorem; it is the absence of a lawful successor satisfying every gate simultaneously.

Let `Q` be the currently screened outside-candidate front and define

\[
E_{\rm ready}
=
\#\{x\in Q:\ S(x)\wedge O(x)\wedge C(x)\wedge U(x)\wedge N(x)\},
\]

where

- `S(x)`: exact outside source, locator, full quantifiers and conventions are recovered;
- `O(x)`: a dated primary-literature check does not show the exact source scope already resolved;
- `C(x)`: the **full source statement**, not a convenient subclass, has a genuinely CLOSABLE route;
- `U(x)`: no live canonical owner/reservation/retired handoff excludes R19;
- `N(x)`: the exact claim is not POSTED/KNOWN/retired by current repository evidence.

R19 may lawfully dispatch only if `E_ready >= 1`. The finite current-front computation below gives `E_ready=0`.

## 4. Chosen recovery action — reduce the obstruction to a finite computation and run it

I choose exactly one Section-I recovery action: **reduce the obstruction to a finite computation and run it**.

The finite computation is an explicit rank-1-through-rank-12 cross-check of the current queue front against canonical ownership/current-status evidence. This is an operational status computation, not a new mathematical theorem and not an excuse for a checker-only commit.

| Queue rank | Candidate | Second-source/claim check | Disposition for R19 now |
|---:|---|---|---|
| 1 | I0006, Bou-Rabee–Panagiotis parking | no canonical claim file, but queue says `HOLD_SOURCE`; fresh primary search says the 2026 paper answers several Damron–Gravner–Junge–Lyu–Sivakoff questions and does not itself supply the exact alleged residual `d>=5` odometer-tail problem | **NOT READY — exact source locator missing** |
| 2 | I0011 | canonical claim exists for P16 | **OWNED** |
| 3 | I0028 | canonical HARD10-01 claim exists; unrestricted fixed-relative-error cover-time approximation is HARD OUTSIDE | **OWNED / HARD** |
| 4 | I0035 | canonical C31 reservation exists, `PENDING_ADMISSION` | **RESERVED** |
| 5 | I0054 | canonical R11 reservation exists, `PENDING_ADMISSION` | **RESERVED** |
| 6 | I0055 | no current claim file, but current admission evidence records the Lyons–Peres Question 5.16 intake as answered by Tang 2020 Theorem 1.6 | **KNOWN/EXCLUDED, not free inventory** |
| 7 | I0070 | canonical R10 reservation exists, `PENDING_ADMISSION` | **RESERVED** |
| 8 | I0068 | canonical P19 claim exists, `READY / CLAIMED` | **OWNED** |
| 9 | I0066 | canonical P15 exclusive claim exists | **OWNED** |
| 10 | I0077 | canonical R07 reservation exists, `PENDING_ADMISSION` | **RESERVED** |
| 11 | I0079 | canonical R06 claim exists | **OWNED** |
| 12 | I0082 | canonical R08 claim exists | **OWNED** |

Thus the exact top-12 queue-front count is

`new source-clean + current-open + ownership-clear + genuinely CLOSABLE successors for R19 = 0`.

I do **not** turn an absent claim file into permission to dispatch: I0006 fails the source gate and I0055 fails the current-status gate.

## 5. Three new method probes

### #1 CHANGE THE CATEGORY

I stopped treating successor search as “pick the next interesting theorem” and rewrote it as a five-predicate feasibility problem `(S,O,C,U,N)` over a finite candidate front. This category change matters because most apparent candidates fail before mathematics begins. It prevents a repeated research pattern in which a worker first proves a restricted lemma and only later discovers that the source was already resolved, the candidate was owned, or the literal source quantifier was much broader.

Result: useful diagnosis, no admission movement.

### #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE

The “small cases” here are the first twelve current queue rows. I checked each rather than sampling one attractive title. The pattern is striking: 8/12 are blocked by live ownership/reservation, 1/12 is current-status excluded (I0055), 1/12 is source-unresolved (I0006), and the remaining front is not a free certified CLOSABLE pool. The issue is therefore not that R19 has overlooked the obvious first queue row; the obvious front is genuinely exhausted under the current contract.

Result: `E_ready` remains 0.

### #25 COUNT THE SAME THING TWICE

I counted “free candidates” in two independent repository representations: first from the queue ordering/status prose, then from canonical `operations/claims/` files plus the newest neighboring admission reports. This catches false frees. In particular, claim-file absence alone would incorrectly make I0006 and I0055 look dispatchable, while queue/current-literature evidence removes both. Conversely, stale queue descriptions alone would miss current live claims for several rows.

Result: both counts reconcile to zero lawful R19 dispatches on the scanned front.

## 6. Every route tried on this successor gate, and why each failed

The present gate has now used more than one route. The failure reasons are distinct and should be preserved rather than retried as unnamed “more searching.”

1. **Root READY/CLOSABLE/UNASSIGNED scan.** Failure: the current queue itself says newly certified READY entries remain zero; current ownership files consume the strongest front rows.
2. **Direct repair of attractive HOLD rows.** I0006 is the cleanest example. Fresh 2026-09-18 search of arXiv:2609.02820 recovered a paper whose abstract says it answers several original parking questions and proves critical visit-count, subcritical parking-time and near-critical divergence asymptotics. No exact author-posed residual `d>=5` odometer-tail statement/locator was recovered. Promoting a guessed residual would violate the source gate.
3. **Deeper/unmined intake screening.** The neighboring R15 pass reached Rudelson–Vershynin deterministic RIP, Smirnov discrete complex analysis, and HPPS stable Poisson matching. Each remains a global/all-scale/classification target, not a one-certificate CLOSABLE source statement.
4. **Extremal/one-witness intake screening.** The neighboring R20 pass found good shapes such as G0013/G0012, but those are already owned; unowned-looking G0008 and F0132 remain all-scale/HARD rather than CLOSABLE.
5. **R19's own Bradley D0029 screen.** It produced a complete non-B-convex beta-side theorem, but the B-convex side encounters a rare-atom obstruction and does not collapse to source closure. That is substantive PARTIAL progress, not a lawful CLOSABLE successor admission.
6. **Reusing retired F0057 or I0084.** Forbidden by the rotation rule. F0057 is a source-matching proof candidate awaiting audits/novelty checks; I0084 is frozen at its handoff. Neither is reserve inventory merely because audits are incomplete.

## 7. What a successful route must contain that none so far contains

A successful successor admission must provide, in one source-matching package **before** research starts:

1. an exact original statement with page/theorem/problem locator and full quantifiers;
2. a dated current-primary-literature check distinguishing full resolution from nearby/special-case progress;
3. no current canonical owner, reservation, retired handoff or posted exclusion;
4. a reason the **full source statement** is CLOSABLE — e.g. one explicit counterexample decides a universal claim, one construction decides an existence question, or a finite exact constant/finite obstruction decides the literal source quantifier;
5. a frozen metric whose movement corresponds to source progress rather than an endless “largest instance checked” treadmill.

The screens so far always miss at least one of these five items.

## 8. Simplest special case still not available as a lawful target

The closest top-row object is I0006. If an exact source-owned residual statement exists, the simplest candidate slice would be the alleged `d=5` odometer-tail question. But **the source locator itself has not been recovered**. Therefore even that simplest slice is not yet a lawful mathematical target for R19. I will not convert queue prose into an invented conjecture.

This is the precise distinction between “simple-looking” and “admissible.”

## 9. Nearest solved problem in the literature and the missing ingredient

The nearest solved material is in the same parking paper, Bou-Rabee–Panagiotis, arXiv:2609.02820 (2 September 2026). Its abstract proves sharp critical expected-visit growth, stretched-exponential subcritical parking-time tails, and near-critical divergence rates, using a representation by the Levine–Peres divisible sandpile plus a martingale-type term; it says these answer questions of Damron, Gravner, Junge, Lyu and Sivakoff.

What R19 lacks is **not** an obvious missing analytic technique from that paper. It lacks an exact surviving source-owned question with a locator and quantifiers. Without that, importing the divisible-sandpile/martingale machinery would be research on a worker-invented target, contrary to the outside-source contract.

## 10. Current-status / source search log

Dated 2026-09-18 searches performed this run:

- `arXiv 1710.08240 Hasebe Ueda Conjecture 5.5 eventual unimodality stable classical convolution free stable`;
- exact-phrase search for `Conjecture 5.5` plus Hasebe/Ueda/unimodality/stable convolution;
- 2025–2026 search on arXiv identifier 1710.08240 and stable-unimodality follow-up terms;
- `Sharpness and critical scaling of parking arXiv 2609.02820 odometer tail d>=5`;
- exact arXiv-id and Damron–Gravner–Junge–Lyu–Sivakoff parking-question queries.

Access limit: web retrieval gave the arXiv abstracts/searchable metadata and repository-preserved source scopes; it did not yield a new explicit residual I0006 source statement. Negative search results are not treated as proof of novelty or openness.

## 11. No checker / no new claim

No new mathematical finite theorem was asserted, so there is no exact-arithmetic checker to manufacture. The finite top-12 admission computation is documented directly from repository source/claim states. No `operations/claims/...` file was created. No shared root or peer-track file was edited.

## 12. Model / scheduler / authorization boundary

The requested GPT-6/maximum routing remains unavailable as an enforceable control on this exposed surface. The available task interface exposes title/prompt, schedule/start-offset, timing mode and enabled state, but no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated applied-run model receipt. Therefore the actual report identity remains **GPT-5.6 Sol / reasoning UNVERIFIED**.

The historical P26 `You cannot modify this task` event is not a current global impossibility: newer root evidence records that P26's full prompt update later succeeded in an authorized P/C context. The demonstrated lawful workaround is the owning/authorized context or platform/backend support, not cloning the task or bypassing permissions. No scheduler modification was attempted.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  lane: CLOSABLE_OUTSIDE
  active_source: NONE
  preserved_predecessors:
    I0084:
      source: "Hasebe--Ueda arXiv:1710.08240v2, Conjecture 5.5"
      convention: "ordinary classical convolution mu * S_t even when S_t is a free-stable law"
      metric_name: "number of classical-stable/free-stable alpha=1/2 source cases decided on the full admissible mu class under the frozen arXiv skewness scope"
      metric_value: "2/2"
      status: "ROTATED_HANDOFF; frozen arXiv ordinary-* package still needs two source-version-specific audits"
    F0057:
      source: "Janson Problem 19.10 / intake F0057"
      metric_name: M_TV
      metric_value: 1
      status: "ROTATED / PROVED_CANDIDATE / SOURCE_MATCHING / AUDIT_PENDING / NOVELTY_UNVERIFIED"
  metric:
    name: E_ready
    before: 0
    after: 0
    movement: false
  unchanged_count:
    before: 2
    after: 3
  status: SUCCESSOR_ADMISSION_REQUIRED_STUCK_RECOVERY_1
  recovery_action: "reduce the obstruction to a finite computation and run it"
  tried_moves: [1, 16, 25]
  finite_frontier:
    I0006: HOLD_SOURCE_EXACT_LOCATOR_MISSING
    I0011: OWNED_P16
    I0028: OWNED_HARD10_01_HARD
    I0035: RESERVED_C31_PENDING
    I0054: RESERVED_R11_PENDING
    I0055: KNOWN_EXCLUDED_BY_CURRENT_ADMISSION_EVIDENCE
    I0070: RESERVED_R10_PENDING
    I0068: OWNED_P19_READY_CLAIMED
    I0066: OWNED_P15
    I0077: RESERVED_R07_PENDING
    I0079: OWNED_R06
    I0082: OWNED_R08
  remaining_obligation: "find one exact-source, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successor; do not promote PENDING/HOLD automatically"
  evidence:
    - "runs/R19/2026-09-18_02-14-29_UTC__successor-gate-live-reconciliation_2f61.md"
    - "artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md"
    - "QUEUE.md"
    - "POSTED.md"
    - "RESULTS.md"
    - "probability_campaign_2026_09/INDEX.md"
    - "probability_campaign_2026_09/RANKING.md"
    - "operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md"
    - "operations/claims/I0011.md"
    - "operations/claims/I0028.md"
    - "operations/claims/I0035.md"
    - "operations/claims/I0054.md"
    - "operations/claims/I0070.md"
    - "operations/claims/I0068.md"
    - "operations/claims/I0066.md"
    - "operations/claims/I0077.md"
    - "operations/claims/I0079.md"
    - "operations/claims/I0082.md"
    - "runs/R20/2026-09-17T23-48-10Z_successor_admission_extremal_failures_7a31d4.md"
    - "runs/R15/20260917_2215Z_successor_admission_unmined_sources_l41c2e.md"
  audit_ids: []
  next_moves: [3, 15, 27]
```

## 14. Next run

Do not repeat #1/#16/#25 immediately. If no newly admitted free successor appears, the second stuck recovery should use **#3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS** on successor discovery: prioritize an outside source whose stronger finite obstruction or asymmetric one-witness counterexample decides the literal full statement, or whose quantifiers can be lawfully reversed into a finite existence/refutation target. Do not return to I0084, F0057, D0029, or I0006 absent a genuine source/ownership/status change.

No Gmail/email, Drive, public posting, purchase, paid compute, permission change, shared-root edit, peer-track edit, scheduler modification, or claim creation was performed.