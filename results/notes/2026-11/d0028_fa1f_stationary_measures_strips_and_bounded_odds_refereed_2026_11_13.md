---
name: d0028_fa1f_stationary_measures_strips_and_bounded_odds_refereed_2026_11_13
description: "[PROVISIONAL] FA-1f stationary measures (D0028, Conjecture 3): on strips Z x H all are lambda pi+(1-lambda) delta_1; on Z^2 bounded conditional odds forces pi (FA-1f, FA-2f); refereed MINOR, conjecture still open"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T07:46:47+02:00
  status: provisional
  evidence: ""
---

D0028: Conjecture 3 of the source (stationary measures of the Fredrickson-Andersen one-spin facilitated model on Z^d, d>=2, are only mixtures of the product measure pi and the all-occupied delta_1).

Result (Codex run D0028A on mini1, referee D0028AR MINOR, 13 Nov 2026), status PARTIAL, two audits:
(1) On strips Z x H (H finite), every stationary law of FA-1f is lambda pi + (1-lambda) delta_1. Referee: this is a direct corollary of the source's Theorem 2.5 and Lemma 2.8, obtained by enumerating the strip as a one-dimensional system ((k,h_i) -> mk+i) with site-dependent finite-range constraints, which the source allows. Present it as a corollary.
(2) On Z^2, a stationary law with two-sided bounded conditional odds equals pi, for FA-1f and FA-2f and every q. This adapts Holley-Stroock (1977) entropy production to degenerate rates; Jahnel-Koppl's general theorem needs strictly positive rates, so it does not cover kinetically constrained models directly. The planar proof handles the borderline shell count properly. No existing theorem with exactly these hypotheses was found; novelty not certified.
Open: Conjecture 3 without the bounded-odds hypothesis. Related refereed result the same day: FA-1f convergence for q>1/2 (fa1f_q_above_half_convergence_and_relaxation_refereed_d0026_d0027_2026_11_13).
Files: brain archive 06_math_research/codex_runs (D0028A, D0028AR); row in probability_1000_intake_D_20260908/problems.jsonl.

Published 13 Nov 2026: github yspennstate/kcm-planar-stationary-bounded-odds 63e47fe, Zenodo 10.5281/zenodo.24190630 (PDF md5 fbd03659 matches); queued for ResearchGate in researchgate_queue/q4. Fresh-reader audit owed after 19 Nov.
