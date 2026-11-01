# RESULTS — brain vs placebo on bank10k (R5 replication)

Lane M6_metric. Analysis run 2026-08-22 19:39–19:53 +0300 against the protocol frozen at
19:38:44 in `PROTOCOL_FROZEN.md`. Nothing in the protocol was changed after freezing.

---

## 1. The short version

**The 2026-08-17 result replicates on a second, independent bank.** On `bank10k`, the brain arm
scored 128/160 against the deranged-notes placebo's 117/160 on the pre-registered primary
stratum — a paired gain of **+6.9 percentage points, 95% CI [+0.8, +12.9]**, discordants 18 to 7,
**McNemar exact two-sided p = 0.0433**. The false-positive control moved the *right* way: the
brain arm raised fewer false alarms on clean control arguments than the placebo (1/40 against
2/41), so the gain is not an arm that simply became trigger-happy.

All three pre-registered success conditions are met, so by the frozen criterion this is
**REPLICATION SUCCEEDS**.

**And one thing that did not replicate, which matters more than the p-value.** The third arm —
`none`, no notes at all — sits between the two: brain 80.0%, none 77.4%, placebo 72.7%. Brain
against `none` is **+2.6 pp, p = 0.50: null**. About half the headline gap is the placebo arm
being dragged *below* the no-notes arm by misleading notes, not the brain arm being lifted above
it. So the defensible claim is *the right notes beat wrong notes*. The claim **"an agent
connected to the brain beats one that isn't"** — which is closest to the question the test was meant to answer —
**is not established by this run.**

---

## 2. Primary result (pre-registered)

Brain vs placebo, `instance` stratum only, solver `claude-haiku-4-5`, one bank (`bank10k`).

| | brain | placebo |
|---|---|---|
| full credit (verdict `flawed` AND exact fault step) | **128 / 160** (80.0%) | **117 / 160** (73.1%) |
| discordant items won | **18** | **7** |
| clean-control false positives | 1 / 40 (2.5%) | 2 / 41 (4.9%) |

- Paired difference **+6.88 pp**, 95% CI **[+0.84, +12.91]** pp.
- **McNemar exact two-sided p = 0.043285.**
- Of the 25 discordant items, 18 favour brain: 0.720, 95% Clopper–Pearson [0.506, 0.879].
- Maximum detectable effect 43 items — the instrument had room to show a much larger effect and
  did not, and room to show nothing and did not. This bank is not ceilinged; that was the defect
  that made the 2026-08-09 nulls uninformative.

### Success criterion, checked against section 4 of the frozen protocol

| condition | required | observed | verdict |
|---|---|---|---|
| (a) direction | brain > placebo | 128 > 117 | **PASS** |
| (b) significance | McNemar exact two-sided p < 0.05 | p = 0.0433 | **PASS** |
| (c) false-positive control | brain FP exceeds placebo FP by ≤ 1 item | brain 1, placebo 2 (brain lower) | **PASS** |

### How the discordants break down

On the 18 items brain won, the placebo arm called the flawed argument **VALID** on 15 and picked
the wrong step on 3. On the 7 items placebo won, the brain arm called it VALID on 6 and picked the
wrong step on 1. Both directions are dominated by the losing arm missing the fault entirely, so
the effect lives in *noticing* a fault rather than in *locating* one.

Stated plainly against the 2026-08-17 write-up: that node treated "the discordants read as one
mechanism" as corroboration. Here the same mechanism appears on **both** sides at nearly the same
rate (83% and 86%), which means it is simply what discordance looks like on this task. It is not
extra evidence for the effect and should not be quoted as if it were.

---

## 3. Sensitivity — does the stratum relabel explain it? No; it works against it

The bank was rebuilt after the sample was frozen (30,342 → 30,482 items) and the sample's
stratum labels moved: `instance` 191 → 181, `insufficient` 25 → 36. The relabel happened
**while the arms were running**, which is the single most dangerous fact in this run: if items
were moved out of the scored stratum after someone read model answers, the primary stratum would
be defined partly by the outcome.

Two things close it.

**Key labels themselves did not move.** Comparing the current keystore to its immediate
predecessor over all 300 sampled items: **0 changes to `truth`, 0 changes to `fault_step`**, and
1 stratum change. The clean/faulted split of the sample is 41/259 both at freeze and now.

**Re-including every possibly-moved item makes the result stronger, not weaker.**

| analysis | n paired | brain | placebo | b : c | McNemar exact p | paired diff (95% CI) |
|---|---|---|---|---|---|---|
| **PRIMARY** — `instance` only | 160 | 128 (80.0%) | 117 (73.1%) | 18 : 7 | **0.0433** | +6.88 pp [+0.84, +12.91] |
| SENS A — `instance` + `insufficient` | 191 | 140 (73.3%) | 126 (66.0%) | 23 : 9 | **0.0201** | +7.33 pp [+1.62, +13.04] |
| SENS B — all faulted, no stratum filter | 228 | 148 (64.9%) | 137 (60.1%) | 23 : 12 | 0.0895 | +4.82 pp [−0.22, +9.87] |

Sensitivity A is the conservative test of the relabel threat: it re-includes every item that
could have been moved out of the primary stratum, plus the 25 that were always `insufficient`.
It is **more** significant than the primary. The relabel did not manufacture the result.

**Sensitivity B must be reported beside the headline.** Pooling in the `generalization` stratum
takes p to 0.0895 and the interval crosses zero. The protocol pre-registered never merging that
stratum in — on those items a solver can be *correct* to answer VALID, so a miss is not a
reasoning failure — and that rule was set on 2026-08-17, before this data existed. The primary is
correct by design. But anyone shown this metric will ask what happens on all faulted items
pooled, and the honest answer is **+4.8 pp and not significant at n = 228**.

---

## 4. The third arm, and why it limits the claim

Pre-declared in the protocol as secondary and exploratory, not part of the success criterion and
not eligible for the metric card. Reported here because it is the contrast closest to the
question the test was meant to answer, and it qualifies the result.

| contrast (instance stratum) | n paired | scores | b : c | McNemar exact p |
|---|---|---|---|---|
| brain vs **none** | 155 | 124 (80.0%) vs 120 (77.4%) | 12 : 8 | **0.503** |
| placebo vs **none** | 154 | 112 (72.7%) vs 118 (76.6%) | 11 : 17 | 0.345 |

Ordering: **placebo 72.7% < none 77.4% < brain 80.0%.**

The +6.9 pp headline decomposes into roughly +2.6 pp of brain above no-notes and +3.9 pp of
placebo below no-notes. Neither half is individually significant, and the halves are not
independently estimated, so the split is descriptive rather than a decomposition to quote as
fact. What it establishes is the direction of the risk: **a meaningful share of the brain-vs-placebo
gap may be misleading notes hurting the placebo rather than good notes helping the brain.**

This is the mirror image of the 2026-08-09 confound. Then, a notes-present placebo inflated the
brain arm and killed a p = 0.001 headline. Here, a notes-deranged placebo may be deflating the
comparator. The deranged-notes placebo remains the right control for *content value given notes
are present* — it is not the right control for *connected vs not connected*.

The `none` null is **underpowered, not evidence of no effect**. With 20 discordant items, 15 of
20 would have had to favour brain to reach p < 0.05; 12 did. The point estimate favours brain.
The correct statement is that this run cannot separate brain from no-notes, not that they are
equal.

---

## 5. Integrity gates and threat checks

| check | result |
|---|---|
| G1 — all 300 sampled ids resolve in current items and keys | **PASS**, 0 missing |
| G2 — `sampled_text_hash` recomputed vs frozen | **PASS**, `7c4c7c924d518b9f` = `7c4c7c924d518b9f`; sampled item text is byte-identical to sample time |
| G3 — stratum stability | **DRIFT**, disclosed and handled in section 3 |
| G4 — out-of-sample verdicts | **0** in all three arms |
| independent re-derivation | **PASS** — a grader written from the protocol, not reusing `cmd_grade`, returns n=160, b=18, c=7, p=0.043285: identical |
| answer-key discipline (canon 7.3) | **PASS** — item records carry only `item_id, bank_version, schema, claim, argument_steps, prompt`; no `truth`, no `fault_step`. Keys live in a separate quarantined tree opened only by `sample`/`grade`/`screen`, never on the serving path. `build_prompt()` sends claim + numbered steps + notes only |
| notes actually delivered | **PASS** — 0 empty; every item got exactly 3 notes in both arms |
| placebo matched in kind and bulk | **PASS** — identical multiset of 82 note titles, identical mean body length (467 chars) in both arms |
| derangement no-ops | 7 of 300 items had placebo notes identical to brain notes. Only 2 fall in the paired set; dropping them leaves b=18, c=7, p=0.0433 unchanged. Immaterial, and it biases toward the null |
| non-random missingness | **DIFFUSE** — 21 of 181 instance items unpaired; no family reduced to zero, at most 3 lost from any family, and all 29 domains, all 5 fault mechanisms and all 3 fault-position bands remain represented |
| 2026-08-17 comparison figures | **VERIFIED against source, not against the memory node** — `...\eval\analytical_10x_v1\results\THREE_ARM.json` confirms brain 71/80, placebo 64/80, discordants 8:1, p = 0.0390625, FP 1/79 and 1/80, max detectable effect 16. The same file records `difficulty_status: author_target_only_unscreened`, so that bank was **not** difficulty-screened; only bank10k was. An earlier draft of the metric card claimed both were screened and was corrected |
| provenance of the earlier interim | The interim grade disclosed in the protocol scored **run1**, a superseded sample sharing exactly **1** item with this one. This run's 274–277 verdicts per arm were served 2026-08-17 20:55 → 2026-08-18 07:59 against the sample frozen at 20:39. The primary is a single grade of a single run, not a repeated look at accumulating data |

---

## 6. What was not run, and why

**The arms were not completed to 300/300.** They stand at none 276, placebo 277, brain 274 — the
counts recorded in the frozen protocol, so nothing was added silently. Completion was not attempted because the
machine was in use at analysis time. This is the fallback the protocol pre-registered, the maximal available
set with the shortfall stated. It is a deferral, not a data problem: the remaining items can be served
later and the grade re-run.

**No second solver tier was run.** The protocol scoped this to a replication at the 2026-08-17
tier (`claude-haiku-4-5`). Every number here is single-tier. A stronger or weaker solver could
show more, less, or nothing, and nothing here speaks to that.

---

## 7. What this does and does not show

**Does show.** On two independently constructed banks, at one solver tier, an agent given three
real math-brain notes retrieved for the item catches planted faults in proofs more often than the
same agent given three notes matched in kind and bulk but deranged in content. On `bank10k`:
+6.9 pp, p = 0.043, with a false-positive rate that went down rather than up. The content of the
store is doing something. That was genuinely in doubt: three banks and four months of this
campaign said otherwise, and the 2026-08-09 headline died on exactly this control.

**Does not show.** (1) That connecting an agent to the brain beats not connecting it — the direct
test of that, brain vs `none`, is null at n = 155. (2) That the effect holds when the ambiguous
`generalization` items are pooled in — it does not, at n = 228. (3) Anything about a solver tier
other than haiku. (4) Anything about how large the effect is in absolute terms: the interval on
the primary runs from +0.8 to +12.9 pp, which is the difference between negligible and large.
(5) Anything about real research work — these are planted single-fault items in a synthetic bank,
not open problems.

**The honest one-liner:** *the right notes beat wrong notes, twice, at one tier — and we still
cannot show that having notes beats having none.*

---

## 8. Files

- `PROTOCOL_FROZEN.md` — the frozen protocol, timestamped 2026-08-22 19:38:44 +0300.
- `audit_regrade.py` — the independent re-derivation and sensitivity analysis.
- `audit_regrade.json` — its machine-readable output.
- `THREE_ARM_interim_150served_20260817.json` — the superseded run1 interim, archived before the
  re-grade overwrote the shared results file.
- `METRIC_CARD.md` — the one-pager, written because the frozen criterion was met.

Shared files touched (mesh-claimed before writing):
`...\eval\bank10k\results\THREE_ARM.json` (re-graded in place; the prior contents were archived
first, both here and to `...\eval\bank10k\results\archive\`).
