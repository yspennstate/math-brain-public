Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / no mathematical movement; Section-B methods #2/#16/#25 were NOT attempted because no source crossed admission.**

# NM13-02 — first admission screen

Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: `CLOSABLE OUTSIDE`  
Own namespace: `proofnet24/NM13-02/`  
Run date: 2026-09-17 UTC

## 1. Runtime and controlling policy

The requested `GPT-6 / maximum` line is prompt text only. The exposed scheduler surface has no binding model selector or reasoning-effort selector; I therefore report the actual model family visible to this invocation as GPT-5.6 Sol and reasoning effort as UNVERIFIED. I do not claim a guaranteed hour-long run or an external escalation.

Before screening I reread/recovered the controlling repository state, including:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- current intake ledgers inspected below;
- current claim/search evidence for candidates that survived long enough to reach the ownership gate;
- the newest neighboring admission report I found, `runs/R15/20260917_2103Z_successor_admission_d0036_k40d7a.md`.

No prior report under `proofnet24/NM13-02/runs/` was recovered by repository search, so this is the first NM13-02 state. A search for `proofnet24/NM13-03/runs` likewise returned no neighboring NM13-03 report at the captured master. Missing history is not treated as permission to invent a baseline.

The current policy requires source statement, fresh status review, prior-history recovery and exclusive ownership before dispatch. `PENDING` is not `READY`; an old `admitted=true` intake bit is not current permission to claim.

## 2. Shard rule and canonicalization

For rows carrying a canonical `dedup_key`, I used exactly that key. For the I-series rows whose schema omits `dedup_key`, I followed the established fleet fallback used by other NM13 workers: `source_id::locator`, preserving the source's exact locator rather than hashing the intake ID. Candidate eligibility requires

`int(SHA256(UTF-8 canonical_dedup_key).hexdigest(), 16) mod 13 = 1`.

The hexadecimal prefixes below are included to make the shard calculation reproducible. Every listed row evaluates to residue 1.

| ID | canonical key | SHA256 prefix | disposition in this run |
|---|---|---|---|
| `I0006` | `arxiv_2609_02820::Section 3, after the statement of the odometer asymptotics` | `6818de44674ed2a2` | queue `HOLD_SOURCE`; residual source clause not yet narrowed to a lawful finite/constant target |
| `I0053` | `beta_splitting_overview::Open Problem 13` | `1ac92f03399818a4` | `OWNERSHIP_HOLD` in current queue; not free inventory |
| `I0077` | `burdzy_scheutzow_2014::Problem 7.8` | `2d4d3b44cd7e1867` | canonical claim `operations/claims/I0077.md` exists for R07; extensive current R07 work; unavailable |
| `I0085` | `free_unimodality_journal_2018::Problem 1.1` | `9b8b057e3b855e7b` | source row itself immediately says the paper answers the problem via Theorem 1.2 / Proposition 3.4; obsolete as open inventory |
| `I0093` | `randomstrasse_2024_v1::Conjecture 14` | `2b1116993498ccb6` | Hadamard conjecture; hard/famous and already represented in the hard fleet, not a CLOSABLE NM13-02 admission |
| `I0108` | `salez_markov_2025::Problem 1.1` | `3b985282b07b212d` | source's model-independent cutoff “Holy grail”; broad hard target, not closable-shaped |
| `I0117` | `tree_automata_2019::Question 1.1` | `536c1d5a1249e130` | source row says the paper answers the question negatively by its main theorem; resolved-in-source inventory defect |
| `D0065` | `rhodes_vargas_gmc_review_2014::conjecture_6.5` | `e5083cda6d694390` | exact Laplace-law identification in general log-correlated fields; asymptotic hard target with major later-literature pressure, not a bounded closable source |
| `C0050` | `C0050` | `17943f59d17b532b` | critical FK parafermionic-observable scaling limit; theorem-sized hard conformal-limit problem |
| `E0005` | `kesten_percolation_highlights_2002::open_problem_5` | `c544fbc2e460c5ef` | missing power bounds for 3D–5D percolation; hard asymptotic target |
| `E0009` | `durrett_coexistence_2009::problem_3` | `59fd8b4bd992afc4` | full host-pathogen noncoexistence theorem in an infinite interacting system; no bounded deciding metric recovered |
| `E0026` | `hunts_hypothesis_survey_2019::question_6` | `d98704930c44fda8` | Hunt's hypothesis for all one-dimensional infinite-variation Lévy processes; campaign INDEX already classifies the Hunt Q4/Q6/Q7 line as PARTIAL/REDUCED; not a new closable source |
| `E0032` | `chatterjee_lower_bounds_2017::open_problems_item_4` | `41b2f5cf6087e7be` | uniform-letter LCS fluctuation lower bound; current literature route remains an asymptotic variance problem, not a finite certificate/short constant target |
| `E0059` | `qso::problem_2` | `f4defcc7bd0ec382` | asks for a general definition/classification of transversality for arbitrary QSOs; broad classification, not a source-bounded closable target |
| `E0063` | `qso::problem_10` | `3464d5781504d733` | campaign ledger records the source question PROVED; excluded |
| `E0064` | `qso::problem_11` | `67f4842d656d60e7` | campaign already has source-level counterexamples/partial scope and a written-up QSO package; do not reopen under a new worker |
| `G0008` | `campos_delima_nonmonotone_2026::monotone_two_point_z2` | `f68b01f170e7776c` | closest current shard-1 discrete-probability lead, but literal source scope is all `p` and all distances on `Z^2`/`Z^d`; prior G0008 attempts exist and the fresh R15 21:03Z admission screen independently classifies it as HARD rather than CLOSABLE |

I also advanced through the remainder of the E intake. `E0095`–`E0113` contain no shard-1 row under their canonical keys, so none can be dispatched by NM13-02. The G front was checked far enough to recover `G0008`; current neighboring work also records G0010–G0013 as owned/reserved and G0014 as theorem-sized rather than a finite closable residual.

## 3. Freshest-front cross-check

The newest neighboring report recovered in this invocation is R15's `20260917_2103Z_successor_admission_d0036_k40d7a.md`. It reread the current task-health state and records **zero currently free `READY + CLOSABLE + UNASSIGNED` successors on its screened front**. That is not a universal proof that the entire repository has zero candidates, but it is important current ownership evidence and prevents this worker from treating an older queue label or search miss as dispatch permission.

The same report specifically notes that `G0008` has no canonical claim in the checked search but remains source-wide and hard; it also records that many superficially attractive D/G rows already have owners or handoff history. I preserve that diagnosis rather than manufacturing a narrower problem and calling it the source question.

## 4. Current-status/literature checks that materially affected admission

This was an admission run, so I spent literature effort only where a candidate could plausibly survive the category/ownership gates.

- `I0085`: no external negative search can make it open, because the intake's own extracted source text says the authors answer the problem immediately in their Theorem 1.2 and Proposition 3.4. It is excluded at the source-reading stage.
- `I0117`: likewise, its own intake statement says “We answer this question in the negative” and cites the paper's main theorem. It is excluded before research.
- `I0077`: ownership is decisive; current repository search returns `operations/claims/I0077.md` owned by R07 plus a long sequence of R07 reports with real metric movement. A different scheduler context or disabled historical slot would not release that source.
- `E0032`: the bounded current-literature check recovered the Houdré–Işlak central-limit route as conditional on the variance lower bound rather than a source-matching resolution. That keeps the mathematical question open-looking, but also confirms why it is a hard asymptotic problem rather than a lawful CLOSABLE assignment for this worker.
- `G0008`: repository history contains a withdrawn overclaim, a corrected partial result, and current admission work. Its universal all-`p`, all-distance quantifiers survive; no finite cutoff or exact constant was recovered that would honestly turn it into the requested closable source.

A bounded negative literature search is not a novelty certificate, and none is represented as one here.

## 5. Admission decision and metric

**Decision: `ADMISSION_PENDING`. No canonical claim file was created.**

There is no lawful admitted source, so the requested mathematical metric remains:

- before: `UNMEASURED`;
- after: `UNMEASURED`.

I do not replace that with a screening count. Candidate exclusions, hashes, repository reads, or commits are not mathematical movement.

The initial Section-B triple **#2 ATTACK THE NEGATION / #16 COMPUTE EVERY SMALL CASE / #25 COUNT THE SAME THING TWICE was not attempted**, because those are research methods on an admitted source. Reporting them as tried during intake screening would violate the prompt.

## 6. Screening cursor and next action

The durable cursor for the next NM13-02 invocation is:

1. do **not** repeat the I/D/C/E/G candidates above absent a status or ownership change;
2. resume with the remaining unreviewed **F-series, remaining C-series, and Codex/raw-catalog admitted rows**, using the same canonical-key residue-1 rule;
3. prefer a source whose exact answer is a probability, expectation constant, finite counterexample, or short exact theorem;
4. before a claim, rerun exact-source, current-literature, attempt-history, and ownership checks against the then-current master;
5. if one passes, create `operations/claims/<canonical-id>.md` create-only and begin #2/#16/#25 mathematics in that same run.

The repository is moving quickly; this cursor is a continuity aid, not future permission to claim.

## 7. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-02
  category: CLOSABLE_OUTSIDE
  source_target: UNASSIGNED
  status: ADMISSION_PENDING
  metric:
    name: UNFROZEN_UNTIL_ADMISSION
    before: UNMEASURED
    after: UNMEASURED
  mathematical_movement: false
  section_B_methods:
    attempted: []
    reserved_first_after_admission: [2, 16, 25]
  claim_created: false
  key_screen:
    shard_modulus: 13
    required_residue: 1
    notable_exclusions:
      - I0077: OWNED_R07
      - I0085: ANSWERED_IN_SOURCE
      - I0117: ANSWERED_IN_SOURCE
      - E0063: CAMPAIGN_PROVED
      - E0064: CAMPAIGN_PARTIAL_WRITTEN_SCOPE
      - G0008: HARD_NOT_CLOSABLE
  unchanged_run_count: UNKNOWN
  stuck_recovery_count: 0
  next_cursor: "remaining F-series, remaining C-series, then Codex/raw catalog shard-1 candidates; skip screened rows unless state changes"
  audit_status:
    P26: NOT_REQUESTED
    NM13-03: NOT_REQUESTED
  shared_root_edits: none
```

No email/Gmail, Drive, public posting, workflow execution, paid compute, permission change, peer-file edit, shared-root edit, or schedule creation/modification was performed.
