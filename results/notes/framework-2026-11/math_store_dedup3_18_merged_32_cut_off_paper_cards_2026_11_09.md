---
name: math_store_dedup3_18_merged_32_cut_off_paper_cards_2026_11_09
description: "[VERIFIED] Does the math store hold duplicates under different titles? Few (9 Nov, DEDUP3): 103 vector-close groups (cos>=0.96, 271 cards), two Codex reads agree on 99 verdicts, 18 merges landed; the bigger find is 32 cards both reads call wrong, mostly arXiv cards cut off where a displayed equation began"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T02:20:08+04:00
  status: provisional
  evidence: ""
---

Question: after DEDUP2 merged same-title cards ([[math_store_118_same_title_groups_254_cards_dedup2_two_reads_2026_11_09]]), how many duplicates hide under different titles?

Census (neardup_census.py, read-only, 9 Nov 01:5x): store bge-small body vectors (claim_embeddings.npz) over 9,855 live claims. Pairs at cosine >= 0.90 with different folded titles: 2.0M, of which 1.2M+ come from the 2,000 generated 'There are exactly N self-avoiding walks ...' cards of 30 Aug (deliberate test material, [[math_store_isolated_cards_are_saw_enumeration_batch_2026_11_01]]; the embedding cannot see the numbers). Without them: 3,364 pairs >= 0.90, 242 >= 0.96, joined into 103 groups / 271 cards (inputs dedup3).

Two Codex reads (DEDUP3A, DEDUP3B, gpt-6.1 high, 02:0x-02:14): A same 17 / different 60 / wrong 25 / partial 1; B 18 / 63 / 21 / 1; verdicts match on 99 of 103. Landed 02:18 (dedup3_land.py = dedup2_land with proposal dedup3-agreed-2026-11-09, backup brain.sqlite3.bak_dedup3_20261109_0218): 18 supersedes edges in 17 groups where both named the same keeper and merged card and neither called either wrong, 46 links carried. Merges are mostly renamed classics (Infinitude of Primes / (Euclid), Abel-Ruffini, Liouville, Green-Tao Wikipedia intro) and a few same-paper restatements. Recall check on each merged title: keeper first 11, top 3 15, top 5 17 of 18, merged card shown 0; H094's keeper ranks 6th for the old title behind four same-topic cards and 4th on a plain query.

So cross-title duplication is small (18 of 271 candidates). Most vector-close groups are different results that read alike: sibling theorems of one paper, duals (Dilworth and Mirsky, both correct), neighbouring open problems.

The real find: 32 cards both reads call wrong, 28 of them paper cards ('Theorem X of arXiv:...'). Most bodies stop where a displayed equation began ('Define the total varaince σ2 as: σ2 def=.', 'we have following two inequalities: Pr.', 'sup h∈H.', a scaling-limit theorem with no limit). Ingestion dropped display math, so siblings like the T-product tensor Bernstein theorems 1.7-1.10 (arXiv 2107.06224, 9 cards; 2012.15428, 7) collapse to the same hypotheses with no conclusion, which is why their vectors coincide. A few are plain errors: a 'fixed-strike lookback put' card whose payoff (M_T-K)^+ is the call; a Bowen entropy card claiming the two-sided window gives the same number under 1/n. An end-of-body regex (trunc_census.py) flags 39 of 1,049 live paper cards but catches only 10 of the 28 known cut-offs, so the true count across the store is likely several times 39: finding them needs a reader, not a pattern.

Files: dedup3_agree.py, dedup3_land.py, dedup3_check.py, trunc_census.py; workers DEDUP3A, DEDUP3B (MERGE_PLAN.jsonl, WRONG_CARDS.jsonl, REPORT.md).
