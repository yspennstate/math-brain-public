---
name: d0031_rho_mixing_bilateral_finite_state_open_2026_11_14
description: "[PROVISIONAL] D0031 (Bradley 2005 survey Q3: finite-state rho-mixing bilaterally deterministic stationary sequence?) still open 14 Nov; Codex D0031A (13 Nov) PARTIAL map of what is compatible and what is impossible"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T10:01:12+02:00
  status: provisional
  evidence: ""
---

D0031 = Bradley, Probability Surveys 2 (2005), arXiv math/0511078, Question 3, PDF p.11. Open as of 14 Nov 2026 (no resolution found; search outcome, not proof).

Read before working on it: 06_math_research/referee_reports/2026-11-13/D0031A/REPORT.md (421 lines, PARTIAL). Its map:
- compatible with bilateral determinism on a finite alphabet: trivial one-sided tails (Gurevic 1973), Bernoulli presentation (Ornstein-Weiss 1975 'Every transformation is bilaterally deterministic'), alpha-mixing (Burton-Denker-Smorodinsky 1996);
- rho-mixing with any rate: real (nondiscrete) state only, Bradley's 1985 construction (UNC TR 91B, DTIC ADA152856); its stationary version has infinite KS entropy, so no finite generator;
- impossible on any alphabet: absolute regularity, interlaced rho (rho* = 1 for all n); bilaterally deterministic finite-order finite-state Markov chains have zero entropy, while rho-mixing finite-state forces positive entropy (Prop 1);
- shortcuts that fail: rare exceptional events (rho normalises rarity away), observable periodic phases (rho = 1).
Why Ornstein-Weiss does not finish it: rho-mixing depends on the generator; an isomorphism does not preserve it. Open task: a finite-alphabet coding with exact exterior decoding AND a uniform past-future correlation bound.
Earlier: D0031-A001 (8 Sep, intake D) and open-problems-repo runs/R02 (17 Sep). Checked by an agent 14 Nov: no new idea beyond the report; not re-attacked.
