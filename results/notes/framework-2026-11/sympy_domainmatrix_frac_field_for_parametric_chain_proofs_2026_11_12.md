---
name: sympy_domainmatrix_frac_field_for_parametric_chain_proofs_2026_11_12
description: "[VERIFIED] sympy symbolic proof for all t of a parametric Markov chain identity hangs? Use DomainMatrix over QQ.frac_field: 0.3 s vs >2 min"
metadata:
  type: reference
  created: 2026-11-12
  created_at: 2026-11-12T19:36:46+02:00
  status: verified
  evidence: "lumping-mixing-time 43e9c87 code/four_state_family.py"
---

A symbolic check of a small Markov chain identity for every value of a parameter (hitting times of a 4-state chain whose weights are polynomials in t) ran past two minutes with sympy Matrix.LUsolve plus cancel and was killed with no output. The same computation over the exact field Q(s) with `sympy.polys.matrices.DomainMatrix` and `sp.QQ.frac_field(s)` finished in 0.3 s for both chains.

**Why:** Matrix.LUsolve on expressions builds unsimplified rational expressions and every cancel re-factors them; DomainMatrix keeps each entry as a reduced numerator/denominator pair in the field, so elimination stays small.

**How to apply:** for exact linear algebra whose entries are rational functions of one or two parameters (hitting times, Green functions, stationary laws of a parametric chain), build the matrix with DomainMatrix over QQ.frac_field(...) and call lu_solve; read entries with `.element`, numerator/denominator with K.numer / K.denom. To prove an inequality for all t >= t0, substitute t = t0 + s and check that numerator and denominator have nonnegative coefficients in s, then run a negative control (a wrong claimed maximum must fail). Used in lumping-mixing-time code/four_state_family.py (commit 43e9c87, 12 Nov 2026).

