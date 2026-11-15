# WBAB3: third writing-brain A/B, rules fixed before any page is written

14 Nov 2026. Written before WBAB3 has a brief, a writer or a page. Any change after the first
page exists is recorded below this file's first commit with its reason, and the result is reported under both rules.

## Why a third test
WBAB1 (8.83 vs 8.83 on 1-10 scores) hit the ceiling. WBAB2 ranked brain pages below plain ones (mean rank 5.08 vs
3.92 of 8, one-sided p 0.92) at 2.65x the tokens, with two judges agreeing at Spearman 0.05-0.48. The judges named
repeated physical business; another agent found after the fact that word stems recurring in 3+ paragraphs per 100
content words track worse rank (Spearman +0.46 over 24 pages). That measure was chosen after seeing ranks, so here it
is a prediction, not a finding.

## Arms (Codex gpt-6.1-sol high, normal speed, same task briefs, same length limit)
- C: no brain.
- B: writing brain as in WBAB2 (practice warm-up, writing_recall, after_page, word_walk).
- B-: writing brain without word_walk, and after_page must print the stem-repeat count and the writer revises once if
  it is above 4.0.
Four writers per arm per task, three tasks, 36 pages.

## Judging
Four blind Codex judges, letters reshuffled per judge per task, BOM and whitespace normalised, key in the session
scratchpad only (never GitHub). Each judge ranks all 12 pages of a task and flags misfits.

## Primary rule
B- beats C if the one-sided Mann-Whitney on mean rank across judges gives p < 0.10 AND B- carries no more misfit
flags than C. Same rule for B vs C, reported second. No other comparison is called a win.

## Secondary prediction (from WBAB2, stated here so it can fail)
Stems in 3+ paragraphs per 100 content words: B- lower than B, and across all 36 pages the measure correlates with
worse mean rank (Spearman > 0). If either fails, the WBAB2 pattern did not replicate.

## Records
Tokens for every writer and judge in both arms; inter-judge Spearman per task; ledger row and a memory either way.
