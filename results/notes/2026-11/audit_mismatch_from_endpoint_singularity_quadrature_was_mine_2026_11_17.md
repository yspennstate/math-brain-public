---
name: audit_mismatch_from_endpoint_singularity_quadrature_was_mine_2026_11_17
description: "Auditor's recomputed coefficient disagrees with the worker's by 0.01-0.05 pct? Check your own quadrature first: an x^-0.9 endpoint singularity under mpmath tanh-sinh came out 0.04 pct low (COSMO12); substituting x=u^10 matched to 1e-14"
metadata:
  type: feedback
  created: 2026-11-17
  created_at: 2026-11-17T00:24:56+02:00
  status: verified
  evidence: "codex_swarm_1115/checks/cosmo12_coeffs_subst.out, commit f4f03068"
  lesson: true
---

COSMO12 audit, 17 Nov 00:1x JST. My first recomputation of the ST p=.3 coefficient C_{2/5} gave 102.9596 against the worker's 102.9988, and ST p=.2 B_5 gave 154.8571 against 154.8805; the four other coefficients matched to 1e-14. The two that missed were exactly the two whose integrands behave like x^-0.9 at 0 (J^2/(sqrt(x) g^beta) with beta=.4; (kappa/nu)^(1/2) f(nu) with the ST nu^-0.4 cusp). mp.quad with a breakpoint at 1e-6 under-resolved them. With x = u^10 the integrand is smooth and both matched to 1e-14.

**Why:** an auditor who reports a 0.04 pct discrepancy as the worker's error, when it is the auditor's quadrature, damages a correct result and wastes the next reader's time.
**How to apply:** when only some recomputed numbers disagree, look at what the failing ones share (here, the strength of the endpoint singularity) before blaming the worker; remove algebraic endpoint singularities by a power substitution (exponent 1/(1-alpha) or larger) and re-run before writing a finding. Related: [[an_authors_own_read_is_not_a_review_and_a_name_is_a_family_of_names_2026_09_03]].
