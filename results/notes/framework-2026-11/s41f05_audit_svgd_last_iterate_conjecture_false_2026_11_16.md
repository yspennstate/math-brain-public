---
name: s41f05_audit_svgd_last_iterate_conjecture_false_2026_11_16
description: "Frontier T310 (SVGD finite-particle rate): Codex auditor disproved the worker's proposed expected last-iterate W2 conjecture with a fixed 1-d counterexample"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T13:05:31+02:00
  status: provisional
  evidence: ""
---

Swarm S41F05 (row T310, polynomial finite-particle rate for Stein variational gradient descent). The original KSD question retires as known (ICLR 2025 / arXiv 2409.08469 v4 give polynomial time-averaged KSD bounds). The worker proposed a successor: an expected last-iterate W2 rate. AUD_S41F05 shows it false for standard discrete SVGD with self-interactions, d=1, target V(x)=x^2/2+cos(x)/4 (strongly convex, non-Gaussian), kernel 1+xy+Matern-7/2, init N(0,2). Proof is exact arithmetic, not floating overflow; not Lean-checked and re-checked by nobody beyond the auditor, hence provisional. Files: 06_math_research/frontier/swarm_s41_20261116/AUD_S41F05/COUNTEREXAMPLE.md and AUDIT.md (commit d74bd1a578fe); full tree release swarm-s40s41-20261116. Lesson: a successor conjecture written by the worker that answered the row needs an adversarial audit before it goes on a frontier card.
