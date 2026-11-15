---
name: d0056_bare_critical_refuted_twice_published_conjecture_open_2026_11_13
description: "D0056 Derrida-Retaux n^-2 law: refuted only without the third tilted moment (refereed MINOR 13 Nov); the published conjecture stays open"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T01:02:11+02:00
  status: verified
  evidence: "brain 06_math_research/referee_reports/2026-11-13/D0056AR/REPORT.md (MINOR, commit 6705bd1a); ledger row commit 4dd9fd31"
---

D0056 (Derrida-Retaux critical recursion, P(X_n>0) ~ (4/(m-1)^2) n^-2) as written in our intake D ledger drops the published
hypothesis E[X^3 m^X] < infinity. Under bare criticality alone it is false twice over: the 11 Oct route via Chen-Shi 2020
Theorem 1.1, and the 13 Nov self-contained route (D0056A, Theorem A: a sparse critical law with atoms at 2^j has
limsup n^2 P(X_n>0) = infinity), refereed MINOR by an independent Codex referee (D0056AR). The published conjecture, with the
third tilted moment, is still OPEN; neither refutation touches it.

Referee fixes owed before any paper: (1) the certificate's lower endpoint (v_n-1)/S is justified for the untruncated law, not the
deleted law, so either use the two-sided error or prove the stochastic-order claim for the untruncated recursion; (2) package
paths; (3) FFT digits in the {0,5} and b=4 rows; (4) cite Chen-Hu-Shi arXiv 2306.12717 Remark 1.2 for the leaf inequality.

**Why:** a ledger statement that drops a hypothesis makes a refutation look like a solved open problem.
**How to apply:** before announcing a D0056-type result, compare the ledger statement word for word with the source's hypotheses;
say "refutes the bare-critical version; the published conjecture stays open".
Record: brain 06_math_research/referee_reports/2026-11-13/D0056A, D0056AR (commit 6705bd1a); ledger row 4dd9fd31.

