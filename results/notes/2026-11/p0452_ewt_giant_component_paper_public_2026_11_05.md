---
name: p0452_ewt_giant_component_paper_public_2026_11_05
description: "[VERIFIED] P0452 (EWT reverse inequality: L1/n -> rho(P) for finite-mean random budgets) published 5 Nov: yspennstate/bilateral-preference-giant-component 4825d09; publish script papers_agent/P0452/build/publish.py (adapted from P0456 step6)"
metadata:
  type: project
  created: 2026-11-05
  created_at: 2026-11-05T09:08:49+02:00
  status: provisional
  evidence: ""
---

Paper papers_agent/P0452/paper (12 pp, AI declaration: Codex GPT solvers Oct 2026 + one GPT audit o09 PASS, Claude checked and wrote). Novelty search 5 Nov clean (only Dabirian-Subramanian 2209.05677, connectivity, cited). Repo checks: finite_checks 61,440 one-edge + 2,099,520 rank-move cases pass; simulation n=2048 constant-3 0.891 vs EWT 0.88, mix 1/5 0.325 vs 0.32. Verified anon ls-remote + raw sha256. Gotcha: when adapting step6_publish.py replace EVERY topic:paper-<id> (the assert lines too) or the assert fails rc 3. Still owed: open-problems-repo P-ledger row.
