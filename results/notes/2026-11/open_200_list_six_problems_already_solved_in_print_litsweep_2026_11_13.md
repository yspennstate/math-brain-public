---
name: open_200_list_six_problems_already_solved_in_print_litsweep_2026_11_13
description: "Is a 200-list problem still open? Six were solved in print (F0010 F0033 F0086 C0155 D0097 I0010); Codex lit sweep + paper check; F0127 only partial"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T23:13:09+02:00
  status: verified
  evidence: "abstracts of arXiv 2607.15294, 2610.13940, 1104.3531, 1204.2931, 2609.06818v2 and Theorem 1.2 of 2210.04779 read by an agent; ledger rows appended"
---

Is a problem on the 200 list still open, or already solved in print? A Codex literature sweep (LITSWEEP1/2 on Mac mini 1,
13 Nov, 63 problems each, one results.jsonl row per problem) found six solved within the first 43 rows; I checked each
against its paper (abstract, plus the PDF theorem for D0097) and appended resolved_in_literature rows to the intake ledgers:
- F0010 Vu normality conjecture: Young arXiv 2607.15294, P(normal) = 2^{-binom(n,2)+O(n)} (preprint).
- F0033 Jarai OQ 6.7, sandpile avalanches on Z^2 finite: Bou-Rabee arXiv 2610.13940 (preprint).
- F0086 HKPV Conjecture 40 DISPROVED: Branden 2012 (arXiv 1104.3531), alpha-determinant nonnegative on all real PSD
  matrices only for alpha in {2/m}.
- C0155 Szegedy's question, two Poisson processes quasi-isometric: yes, Basu-Sly PTRF 2014.
- D0097 Rolla, ARW on Z^2: Asselah-Forien-Gaudilliere Ann. Probab. 2024, zeta_c < 1 for all lambda and
  zeta_c <= |ln lambda|^{-a} as lambda -> 0.
- I0010 uniqueness of the extremal cubic graph: proved in v2 of the very paper the problem came from (Zhu 2609.06818v2).
F0127 (Aldous OP2) the sweep called RESOLVED; it is only partial (Oliveira 2013 gives sufficient conditions, question is
open-ended) - so a sweep verdict is a lead, not a ledger row, until the theorem is read.
Lessons: three of six were old (2012-2014) and should never have entered the list; one came from v1 of a paper whose v2
closed it - check the latest arXiv version of the source before attempting. Earlier the same day E0052 (Feige) turned out
proved (Fu et al. 2607.23980). Before attacking a list problem, run the sweep prompt on it first: agent_run/litsweep/PROMPT.md.
Related: [[f0127_aldous_op2_fast_mixing_uniform_not_enough_2026_11_12]], [[e0081_pitman_tang_first_passage_pattern_n_log_n_proved_2026_11_12]].


Update 13 Nov 01:2x +04 (laptop 23:2x): four more, checked the same way and recorded:
- F0080 LPS Q6.13 (FMSF degree depends on the Cayley graph): yes, Thom, Combinatorica 2016.
- D0019 Khoshnevisan OP4 (random exceptional projection of Brownian-sheet zeros): no, Chen-Woessner JTP 2025.
- C0122 Chatterjee sec.12 (5) (chaos gives multiple peaks without nonnegative correlations): Ding-Eldan-Zhai AoP 2015.
- G0001 Cerf Conj. 1.4: follows from theta(p_c)=0 for site percolation on Z^d, d>=3 (Kozma-Nitzan 2026, AI-found,
  site extension in Blanc-Renaudie arXiv 2610.10502) plus classical supercritical tails. PROVISIONAL: preprints only.
Ten of 102 swept problems were already settled; most were years old.
