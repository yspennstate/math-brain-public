# Harder recall and agency: results snapshot, 2 November 2026

**Evidence cutoff: 21:49 UTC. These are producer-reported evaluations, not independently rerun or externally reviewed results.**

The newer recall bank shows a modest accuracy improvement with substantial time overhead. A harder recall pilot does not yet show a statistically detectable gain. The completed claim-audit exercise was too easy to establish a benefit. **No completed controlled hard-agentic evaluation was verified at this cutoff.**

## Completed recall comparisons

| Evaluation | Valid paired items | Brain correct | Direct/git-only correct | Reported paired test | Mean time per item, Brain / direct |
|---|---:|---:|---:|---|---|
| R5 final | 809 | 690 (85.3%) | 656 (81.1%) | Exact McNemar p = .00187; 74 Brain-only vs 40 direct-only successes | 68 s / 23 s |
| R6 harder pilot | 80 | 61 (76.2%) | 59 (73.8%) | Exact McNemar p = .727; 5 Brain-only vs 3 direct-only successes | 33 s / 15 s |

### R5: encouraging but bounded recall result

The bank contained 889 questions; 809 received answers from both arms across 20 launched worker pairs. The remaining 80 questions belonged to two pairs that were not launched, rather than scored failures. The report describes matched Codex model/medium effort and a 12-command allowance per question, with repository search available to the control.

Questions included vocabulary shifts and linked-note retrieval. In the vocabulary-shift subgroup (219 items), accuracy was 85.4% versus 76.7%; this is a subgroup result, not a separate general capability claim. The authors still judge the bank too easy: direct search answered about 81% correctly.

The Brain configuration changed during execution. The report separates 358 earlier partial-configuration items from 451 later full-configuration items. These were different questions run at different times and loads, **not a randomized graph ablation**. The overall result cannot establish which configuration caused the difference. Mean command counts were 4.1 versus 4.5; higher accuracy came with roughly three times the elapsed time.

### R6: harder pilot, inconclusive

The pilot included superseded facts, three-hop links, joins across notes and indirect descriptions. Of 100 planned pilot questions, one entire 20-question worker pair was voided for prohibited configuration/history-directory access. The remaining 80 paired items produced the table above. The small sample and p = .727 provide no demonstrated advantage; they do not establish equivalence.

There is an unresolved configuration discrepancy: the report header says medium effort and 12 commands, while the preregistration/memory description says high effort and 10 commands. Treat configuration as **not fully reconciled**. Mean command counts were 4.0 versus 4.4. A larger 436-question, four-command follow-on was reported started, but no completed scores were verified at the cutoff. That tighter budget was selected after inspecting the pilot; it is not a preregistered property of the pilot, and replaying capped pilot traces is not a new evaluation.

## BTQ1: history retrieval and claim auditing

Two paired repetitions used the **same 144-item bank**: 84 Bitcoin research-history questions and 60 claim audits (30 planted errors, 30 clean controls). Thus there were 288 paired item-observations, not 288 distinct questions. This is not the separate proposed mathematical proof-audit suite.

| Scoring | Pair 1: Brain / control | Pair 2: Brain / control |
|---|---:|---:|
| Frozen exact-match scoring | 124 / 119 | 122 / 120 |
| Reported posthoc blinded rescoring | 143 / 140 | 141 / 137 |

The posthoc results had reported exact paired p-values .375 and approximately .34, respectively. Median time was 3.6–4.6 seconds per item across workers. The report says no planted-error verdict was missed and no clean control falsely flagged; remaining errors involved corrections or history answers. This near-ceiling exercise **does not demonstrate a reliable Brain benefit**.

Preserve both scoring versions: the posthoc rubric must not silently replace the frozen scores. The source prose claims a net gain of five out of 288, but its rescored table gives seven; this inconsistency remains flagged. The repetitions are not independent distinct question samples. Isolation is producer-reported, not independently established here, and released bank/key material must not later be described as unseen.

## Hard agency and external benchmarks: not yet completed

- **32-task agency/trap suite:** fixtures and checkers were prepared, but the inspected report explicitly states no model workers were launched. No scored controlled outcomes are available.
- **Historical 1,776-session agency audit:** observational and confounded, not a controlled test of improved agency. Waits dominated candidate loop flags; this does not prove harmful loops never occur. Task matching and semantic completion verification were insufficient for a causal comparison.
- **ProcessBench and LongMemEval pilots:** no benchmark items or model outputs were obtained in the inspected package, and scores are null. Eleven synthetic infrastructure checks passed; these are not benchmark scores.
- **Separate proposed 60-proof mathematical audit:** no completed result was located in this bounded review.

Hard-agentic evidence requires verified multi-step goal completion, recovery, constraint adherence and final-artifact checks—not a plan, a question bank or a successful retrieval call.

## Interpretation and evidence limits

These results distinguish completed measurements from planned tests and preserve exclusions, null findings and scoring discrepancies. R5 supports a limited recall improvement on its measured bank, with meaningful latency cost; R6 and BTQ1 do not yet establish a benefit. None establishes broad reasoning or autonomous-agent superiority.

This public page is a sanitized report-level summary. Private corpora, raw records, question banks, answer keys and internal configuration identifiers are not published here; consequently this page alone is not a reproducibility package. Counts and statistics above were transcribed from the producers' reports, not independently regenerated from raw outputs. Further evaluation should freeze held-out tasks, scoring, access rules and budgets before execution; audit contamination; compare equal underlying evidence and tools; and report accuracy, time, tokens, failures and uncertainty together.
