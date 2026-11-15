---
name: t021_han_question_3_1_constant_at_least_4_tribes_2026_11_03
description: [PROVISIONAL] T021 FEI: Han's Question 3.1 constant (sum |f^(S)f^(S u k)| <= c I_k) is at least 4, not 2 - biased uniform tribes; exact check; brain main b896e59f
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T03:14:41+02:00
  status: provisional
  evidence: ""
---

Han 2312.08271 Question 3.1 asks for c such that every Boolean f has a coordinate k with sum_{S not containing k} |f^(S) f^(S u k)| <= c I_k(f); his AND example gives c >= 2. Uniform disjoint tribes T_{s,w} give, at every coordinate, Q_k = 2 - 2^(2-w) when alpha^s >= 1/2 and 4 - 2^(2-w) - 4 alpha^s when alpha^s < 1/2 (alpha = 1 - 2^-w). With w large and alpha^s -> 0 (a strongly biased function) Q_k -> 4, so the best constant is at least 4. Example: s = 10, w = 2 gives 2.7747. Checked as exact fractions against full truth tables for 23 (s,w) pairs, n <= 16. Small n tells a different story: over all monotone f on n <= 5 and all Boolean f on n <= 4 the worst case is AND, 2 - 2^(2-n), so the extremes only show up in large, biased functions. This is a lower bound on the constant, not a disproof; GMP 2606.00246 Theorem 6.8 bounds the ratio by 8 for disjoint tribes. Priority has been checked only against Han and GMP. Files are under 06_math_research/frontier/rows/T021/exp/q31/, with the card in rows/T021/BRAIN_CARDS.jsonl. Next: look for a family with sup min_k Q_k > 4. Landing lesson: api_land refuses a file whose rewritten lines are missing from the tip, so edit dossiers append-only. Related: [[t021_fei_dossier_written_li_han_2512_03117_is_withdrawn_2026_11_03]]
