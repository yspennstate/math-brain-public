---
name: e0018_switching_rate_instability_two_intervals_resolved_unrestricted_2026_11_13
description: "Malrieu OQ3 (switched 2x2 linear, instability set in r a union of intervals?): YES in the literal wording, A0 Hurwitz, A1=diag(5/4,-11/4) not Hurwitz; both-Hurwitz version open"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T03:24:00+02:00
  status: verified
  evidence: "E0018A certificates + referee E0018AR MINOR + independent FV check (3 digits)"
---

E0018 (Malrieu, Ann. Fac. Sci. Toulouse 2015, arXiv:1412.7516, Open question 3: can two 2x2 matrices be chosen so that the set of switching rates r with an unstable switched linear process is a union of several intervals?) is resolved in its literal wording, 13 Nov 2026.

Pair: A0 = [[-3/4,-1],[1,-3/4]] (Hurwitz), A1 = diag(5/4,-11/4) (NOT Hurwitz), symmetric flip rate r.
Top exponent: lambda(0.1) = 0.216 > 0, lambda(2..5) about -0.045..-0.041 < 0, lambda(20) = 0.077 > 0, lambda(inf) = 0.116 (top eigenvalue of the average). So {r: lambda(r) > 0} has at least two components.

Audits: Codex E0018A (certificates: lambda(0.1) > 0.18, lambda(5) in [-0.0714,-0.0097] by an exact rational audit, lambda(20) in [0.0703,0.0850]); referee E0018AR MINOR (rules the question literally allows general matrices; the Hurwitz restriction is context, not a hypothesis); my own upwind finite-volume CTMC check, N=2000/8000/32000, agreeing to 3 digits.

Scope, say it every time: this does NOT answer the both-Hurwitz version (1,545 shifted Hurwitz pairs searched, no two-component case); exactly two components is not proved. Referee's minor fixes: the second-branch coordinate is x = -log|tan theta|; cite Lagasquie arXiv:1612.01861 (multiple blow-up regions with Gamma holding times) and Porfiri-Jeter-Belykh 2019/2021; fix the source manifest. The paper is by Malrieu alone (an earlier citation named four authors).

Records: brain 06_math_research/referee_reports/2026-11-13/E0018A (6493d7d2) and E0018AR; ledger intake E row. Paper handed to an agent.

