---
name: rr_constant_step_log_factor_referee_three_fixes_2026_11_14
description: "[VERIFIED] rr-constant-step-log-factor (random reshuffling log factor) post-posting referee 14 Nov: proofs correct; three fixes pushed cd5fd38 (six instances, x0=-D grid minimum, two missing citations)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T07:03:44+02:00
  status: provisional
  evidence: ""
---

Independent referee pass by an agent on github.com/yspennstate/rr-constant-step-log-factor (6085335). Every proof checked by hand (Lemma 2.1 mean/phi bounds, Lemma 2.2 via Mann-Whitney variance n1 n2 (n+1)/12, Theorem 1.1(a)(b), Prop 3.1, Theta constants 1/2048 and 2). Independent exact DP (B = sum c_t (r^q - 1), backward over stiff/flat counts) agrees with brute force and Monte Carlo; code/rr_check.py rerun byte-identical.

Fixes (cd5fd38): (1) Section 5 named 8 instances but the script runs 6; (100,50,1e3) has min 1.545 units, outside the stated 1.29-1.54. (2) The x0=-D minimum was a grid value: the error dips sharply at the root of E X_K (gamma mu T/Lambda 0.84-0.87); true minima 1.0e-4..0.017 units, code/minus_start.py added. (3) Cited Li arXiv:2609.04578 (constant-step last-epoch O~(T^-2+n^2T^-3)) and Liu-Zhou arXiv:2505.23056.

Lesson for numerics paragraphs: a minimum over a grid of a function with a cancellation dip is not the minimum; find the root and minimise next to it. Report: brain-repo/06_math_research/referee_reports/2026-11-14/RR_posted_referee/REPORT.md. Related [[urn_euclidean_contractivity_referee_one_sentence_fixed_2026_11_14]].
