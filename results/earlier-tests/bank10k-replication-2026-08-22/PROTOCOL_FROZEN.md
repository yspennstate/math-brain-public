# PROTOCOL_FROZEN — brain vs placebo on bank10k (R5 replication)

**Frozen at: 2026-08-22 19:38:44 +0300 (Asia/Jerusalem).**
Lane M6_metric, campaign 2026-08-22_30h.
Nothing below may be changed after this timestamp. Any change is a new protocol with a new
timestamp, and the old one stays on disk.

---

## 0. What this is, in one paragraph

On 2026-08-17 a pre-registered blind test on the bank `analytical_10x_v1` found the brain arm
beating a deranged-notes placebo 71/80 to 64/80, McNemar exact two-sided p = 0.0391, with
identical false-positive rates. That result named its own limits: one bank, one solver tier,
n = 80, and a p-value one discordant item away from 0.109. This protocol governs the
replication on a second, independently constructed bank (`bank10k`) that was screened into a
comparable difficulty band the same night.

## 1. Disclosure — read this before believing anything downstream

This is **not** a fresh pre-registered experiment. The data already exists on disk. I am
pre-registering an **analysis** of an already-collected run. The distinction matters and it is
stated here rather than buried.

What protects it: every design element in section 2 was frozen by the 2026-08-17 harness author
**before the data existed** — the sample, the seed, the strata, the arms, the scoring rule, the
primary contrast, and the test statistic are all written into `run_bank10k.py` and
`run/SAMPLE.json`, not chosen by me. I am changing none of them and adding no new analysis
degree of freedom.

What does not protect it, and must be declared: **before freezing this protocol I read
`results/THREE_ARM.json`** (file mtime 2026-08-17 20:22), which holds an *interim* grade taken
when each arm had served 150 of 300 items. It reported:

| interim, 150 served/arm | brain | placebo |
|---|---|---|
| instance stratum full credit | 75 / 98 | 69 / 98 |
| discordants | 14 | 8 |
| McNemar exact two-sided p | 0.286 | |
| clean-control false positives | 3 / 24 | 0 / 24 |

I had to read that file to discover the run's state at all. I did **not** open any individual
verdict file, any answer key, or any per-item record. A reader should treat the numbers above as
information I possessed when writing section 4, and judge section 4 accordingly.

## 2. Design — INHERITED UNCHANGED from the 2026-08-17 harness

Machinery being resumed, not rebuilt:

- Runner: `<local>/run_bank10k.py`
- Items: `...\eval\bank10k\items\bank10k.jsonl`
- Answer keys: `<quarantined keys file>` (separate tree, quarantined)
- Frozen sample: `...\eval\bank10k\run\SAMPLE.json`
- Verdicts: `...\eval\bank10k\run\verdicts\{none,placebo,brain}\*.json`

Frozen sample, as recorded in `SAMPLE.json`:

- seed 20260817; requested 300; item_ids 300
- 259 faulted + 41 clean controls
- faulted by ambiguity stratum: **instance 191**, insufficient 25, generalization 43
- 184 reasoning cells, all 184 covered, per_cell = 1
- bank_fingerprint at sample time: n_items 30342, id_hash `472f8cb88e65b980`
- sampled_text_hash at sample time: `7c4c7c924d518b9f`

Arms (three, all served against the same frozen sample):

- `none` — no reference notes.
- `placebo` — three real notes, matched in kind and bulk, with relevance destroyed by a
  deterministic derangement. **This is the confound-killer.** It is the arm that killed the
  2026-08-09 headline, where a placebo reproduced the brain arm 48/48 and showed the gap had
  measured notes being PRESENT rather than the store knowing anything.
- `brain` — three notes retrieved from the math-brain population store
  (`<local>/brain.sqlite3`).

Solver: `claude-haiku-4-5`, fresh context per item, one subprocess invocation per item. Matched
to the 2026-08-17 tier so this is a replication claim and not a generalization claim. No second
tier is run in this protocol.

Answer-key discipline (verified before freezing, canon 7.3): item records in `bank10k.jsonl`
carry exactly `item_id, bank_version, schema, claim, argument_steps, prompt`. There is no
`truth`, no `fault_step`, no verdict field. `build_prompt()` sends only the claim, the numbered
argument steps, and the notes block. The keys file is opened only by `sample`, `grade` and
`screen` — never on the serving path. **The solver cannot see the key.**

Scoring, unchanged: full credit on a faulted item requires verdict `flawed` **and** the exact
first-invalid step number. Clean controls are the false-positive control and are never a
scoring opportunity.

Primary contrast, unchanged: **brain vs placebo on the `instance` stratum only.** The
`generalization` and `insufficient` strata are reported beside it and never merged in, because
on those a solver can be correct to answer VALID.

Test statistic, unchanged: **McNemar exact, two-sided**, on the paired discordants.

## 3. Integrity gates — run BEFORE the grade, and a failure stops the lane

The bank was rebuilt after this sample was frozen: `SAMPLE.json` records 30,342 items,
`status` reports 30,482 today. That is a real, disclosed drift and it must be cleared before any
number is quoted.

- **G1 — id survival.** All 300 sampled item_ids must still resolve in both the current items
  file and the current keys file. Any missing id is named and counted.
- **G2 — text identity.** `sampled_text_hash` recomputed over the 300 sampled ids against the
  CURRENT items file must equal `7c4c7c924d518b9f`. If it does not, the verdicts on disk were
  produced against different item text than the keys now describe, and **the run is not
  gradable**: report DATA INCOMPLETE and stop.
- **G3 — stratum stability.** Recount the sampled ids by `ambiguity_stratum` against the current
  keys. Must equal instance 191 / insufficient 25 / generalization 43. Any drift is reported
  verbatim, because the 2026-08-17 correction on this exact bank moved 1,029 items between
  strata and crossed a band edge.
- **G4 — out-of-sample verdicts.** `grade` already excludes verdicts whose item_id is not in the
  frozen sample. Whatever it excludes is reported, per arm, in RESULTS.md.

## 4. Analysis plan and the success criterion — written before the grade is run

Verdict counts on disk **at this timestamp**, from `run_bank10k.py status`:
**none 276, placebo 277, brain 274**, of 300 each. These are stated here so nothing can be
added silently later.

Order of operations:

1. Run the integrity gates G1–G4.
2. **Attempt to complete the three arms to 300/300** using the harness's own resumable `serve`
   mechanism, unchanged. If the serving path needs credentials, an endpoint, or config that is
   not already in place and working, that arm is stopped and reported **DATA INCOMPLETE** — no
   key hunting, no copying credentials, no substituting a different model.
3. Run `grade` **once** for the primary result, on whatever complete-or-maximal verdict set
   exists after step 2, with the per-arm served counts stated beside every number.

The primary is a **single** grade run. If step 2 cannot finish, the primary is the maximal
available set with its shortfall stated — it is not an excuse for a second look.

**REPLICATION SUCCEEDS** only if all three hold on the `instance` stratum:

- **(a) Direction.** brain full-credit count > placebo full-credit count.
- **(b) Significance.** McNemar exact two-sided p < 0.05.
- **(c) The false-positive control holds.** brain's clean-control false positives exceed
  placebo's by **at most 1 item**. This is not decoration. The 2026-08-17 finding's own defence
  against "the brain arm just got trigger-happy" was that false-positive rates were identical
  between arms (1/80 vs 1/79). An arm that wins on faulted items by calling everything flawed
  has not shown content value, and a metric shown to other people must survive that objection.

**DIRECTIONAL, NOT REPLICATED** — (a) holds, (b) fails. Reported as a failure to replicate the
significance claim, with the direction noted and the interval given.

**CONFOUNDED** — (a) and (b) hold but (c) fails. Reported as a false-positive shift, **not** as a
brain win. No METRIC_CARD.

**FAILED** — (a) fails.

**No pooling.** The `analytical_10x_v1` result (71/80 vs 64/80) and this bank10k result are
reported side by side and are never combined into a single test. Pooling was not pre-registered
on 2026-08-17 and is not pre-registered here.

**Secondary, explicitly exploratory, not part of the criterion and not eligible for the metric
card:** the `none` arm (notes-absent) against both other arms; the `generalization` and
`insufficient` strata; and per-arm served/excluded counts. These are descriptive. They carry no
success criterion and no claim.

## 5. Deliverable rule

`RESULTS.md` is written whichever way the result falls — a null replication is a finding and gets
the same care as a positive one. `METRIC_CARD.md` is written **only** on REPLICATION SUCCEEDS as
defined in section 4, and if written it carries every caveat on its face: banks, solver tier, n,
confidence interval, false-positive rates, and the fact that it is one tier.
