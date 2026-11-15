---
name: pd15_schiffer_certificates_replayed_n8_10_14_2026_11_13
description: "[PROVISIONAL] Schiffer/Pompeiu counterexample repo (arXiv 2609.35419): n=8,10,14 certificates replay PROVED + PROVED_CONVEX on Windows Py3.14 flint 0.9.0; CRLF checkout trips their hash (use autocrlf=false); n=2 is numerical gates only; Macs' Python 3.9 too old"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T01:50:17+02:00
  status: provisional
  evidence: ""
---

13 Nov 2026, an agent. Replayed github.com/aster2024/schiffer-pompeiu-counterexamples verification r8, r10, r14 on the laptop: all PROVED and PROVED_CONVEX, r10 fail-closed tests pass. This is the authors' code on a second platform, not an independent proof (the reductions and tail bounds were not re-derived). A CRLF checkout makes every verifier refuse with 'frozen bundle missing or changed' - check out with core.autocrlf=false. The planar n=2 verifier ends in NUMERICAL_GATES_PASS with analytic lemmas in the text. Mac minis 1 and 2 have only Python 3.9, too old for python-flint 0.9. Record: 06_math_research/top200_vet_agent_2026_11_11/PD15_SCHIFFER_REPLAY_1113.txt. Not run: n=2,3,5,7 and gd/. status: provisional.
