---
name: i0003_manhattan_paper_posted_2026_11_13
description: "I0003 Bou-Rabee-Peres Problem 3 (Manhattan walk orientation fields): paper posted 13 Nov 2026, repo manhattan-orientation-fields-recurrence b1e5fc57, 13 pp; general question open"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T21:51:31+02:00
  status: verified
  evidence: "repo manhattan-orientation-fields-recurrence b1e5fc57; remote blob hashes match local"
---

I0003 (Bou-Rabee-Peres arXiv:2609.07621, Section 7 Problem 3: which Manhattan orientation fields are recurrent) is posted as a paper on 13 Nov 2026: https://github.com/yspennstate/manhattan-orientation-fields-recurrence, commit b1e5fc57, 13 pages, "Recurrence and transience of the Manhattan walk for deterministic orientation fields".

What it proves: bounded change of primitives preserves type (uniform resolvent comparison); divergence of sum 1/(1+M(2^m)^2) gives recurrence; four-tail eventually constant fields classified (recurrent exactly in the two circulating arrangements); one probability-one event of iid horizontal signs gives transience against every bounded-primitive vertical field (extends Bosi Thm 9(i)); power classes: only a=b=0 forces recurrence (consequence of Bosi 9(iii)). The general question stays open.

Prior work credited in the paper: Bremont ALEA 14 (2017) Thm 2.4 and Prop 7.1 (stratified model, bidirectional vertical edges, a different kernel); Bremont ECP 24 (2019) paper 47; Pene ESAIM Proc 68 (2020) Sec 3.5; Gaudilliere-Landim Lemma 5.5 covers the bounded-stream recurrence subcase.

Checks before posting: release guard ok, paper_lint 0 MUST; remote README/main.tex/main.pdf matched local size and git blob hash. Ledger row PAPER_POSTED in probability_1000_intake_I_20260914/problems.jsonl. Zenodo (agent) and ResearchGate (agent) told.
Builds on [[i0003_manhattan_orientation_fields_recurrence_partial_two_audits_2026_11_13]].


Post-posting referee, 14 Nov 02:2x: ACCEPT, no correction; Lemma 2.1 through Cor 1.5 rechecked by hand, constants (C = 2+2K, 12*4^m, 192/D_N, 16W) all hold. Report in brain repo 06_math_research/referee_reports/2026-11-14/I0003_posted_referee/REPORT.md. Open case for a v2: e = g with f alternating is outside all four theorems; exact evolution gives n^{3/2} P^n(0,0) -> 0.796 (Green sum ~1.357), confirmed by an independent run-decomposition DP, so likely transient by the Campanino-Petritis occupation-time mechanism (sketch only; lattice tie step unwritten). Check Bosi thesis Thm 9 before claiming it new.
