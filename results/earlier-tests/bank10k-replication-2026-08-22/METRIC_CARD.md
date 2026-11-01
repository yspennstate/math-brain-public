# Does the math brain's content help an agent find mistakes in proofs?

A controlled measurement, replicated on two independently built banks.
Prepared 2026-08-22. Pre-registered protocol and full results accompany this card.

## The question

Give a model a mathematical argument that contains exactly one planted error, hidden from it.
Ask for a verdict and the first invalid step. Then vary only one thing: whether the reference
notes attached to the item are the ones the math brain retrieved for that item, or notes matched
in kind and bulk whose content has been scrambled. If the store knows anything, the first arm
should do better.

The scrambled-notes comparator is the point of the design. An earlier version of this measurement
compared notes against no notes, reported p = 0.001, and did not survive: a scrambled-notes arm
reproduced the brain arm's verdicts 48 out of 48. That gap had measured notes being present, not
the store knowing anything.

## The result

| | bank10k (2026-08-22) | analytical_10x_v1 (2026-08-17) |
|---|---|---|
| brain arm | 128 / 160 (80.0%) | 71 / 80 (88.8%) |
| scrambled-notes arm | 117 / 160 (73.1%) | 64 / 80 (80.0%) |
| paired difference | +6.9 pp, 95% CI [+0.8, +12.9] | +8.8 pp |
| discordant items | 18 to 7 | 8 to 1 |
| McNemar exact, two-sided | p = 0.043 | p = 0.039 |
| false alarms on clean controls | brain 1/40, comparator 2/41 | brain 1/79, comparator 1/80 |

Both banks were pre-registered before the arms were scored, and both had room to move. bank10k
was screened into its difficulty band in advance, and its comparator missed 43 of the 160 scored
items, so an effect of any size up to 43 items could have appeared. analytical_10x_v1 was not
screened — its own result file records the difficulty as author-target-only — and its comparator
sat at 80%, leaving 16 items of room. Neither run is a comparison between two arms that were
already near-perfect, which is the defect that made this campaign's earlier null results
uninformative, but the 2026-08-17 bank had thin room by construction and the 2026-08-22 bank did
not.

Full credit requires both the verdict "flawed" and the exact first invalid step. The two banks
were built by different generators, and the results are reported side by side; they are not
pooled into a single test.

## What it does not show

**It does not show that an agent connected to the brain beats one that is not.** bank10k ran a
third arm with no notes at all. It landed between the two: scrambled 72.7%, no notes 77.4%,
brain 80.0%. Brain against no-notes is +2.6 pp, p = 0.50 — no separation at this sample size.
Roughly half the difference in the table above may be scrambled notes hurting the comparator
rather than real notes helping the brain arm. The measurement establishes that the *content* of
the notes matters given notes are present. It does not yet establish that attaching the brain
beats attaching nothing.

**The effect does not survive pooling in the ambiguous items.** Items where a solver can
legitimately answer "valid" are scored separately by design, a rule fixed before the data
existed. Pool them in and the difference is +4.8 pp, p = 0.089, at n = 228.

**One solver tier.** Both runs used claude-haiku-4-5. Nothing here speaks to a stronger model.

**Synthetic items, not research.** These are generated arguments with one planted fault each,
across 29 mathematical domains. They are not open problems, and no claim is made that the effect
transfers to real research work.

**The interval is wide.** +0.8 to +12.9 percentage points spans negligible to large. The
direction has now held twice; the magnitude is not pinned down.

## How it was measured

- Bank: 30,482 generated items, 26,303 with a planted fault, 4,179 clean controls.
- Sample: 300 items drawn by a frozen seed, stratified across 184 reasoning cells so no single
  family dominates. Scored on the 160 items both arms completed within the primary stratum.
- Arms differ only in the notes block. Every item in both arms received exactly three notes, with
  an identical multiset of note titles and the same mean note length (467 characters).
- The solver never sees the answer key. Item records carry the claim and the numbered steps and
  nothing else; keys live in a separate quarantined store that the serving path never opens.
- Statistic: McNemar's exact test, two-sided, on the paired discordant items.
- Clean controls are the false-alarm check and are never a scoring opportunity. An arm that wins
  by calling everything flawed would show it there. On bank10k the brain arm raised fewer false
  alarms than the comparator, not more.

## Status

Two banks, one tier, direction consistent, both nominally significant, neither by a wide margin.
The next measurements that would change what can be claimed: complete the bank10k arms from 275
to 300 items each, run a second solver tier, and power the no-notes contrast properly, since that
is the comparison most people will assume is being made.
