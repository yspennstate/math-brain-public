---
name: method_max_term_inequality_find_where_it_is_small_then_perturb_2026_11_11
description: "Inequality with a max term to prove for every n (T104 Psi >= 0)? Do not build one bound: find where the max term is small, show x is there a perturbation of the extremal vector, compare orders in n; and give every side remark the exact check the theorem got"
metadata:
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T08:47:31+02:00
  status: provisional
  evidence: "T104 Psi>=0 all n: uniform bound failed at n=14, the split by small m closed from n=14; peer read no gap + Lean; Codex referee SOUND with four written slips (AUDIT_CODEX_ALLN_REPORT.md)"
---

Proving f(x) >= 0 for every n when f carries a max term (here m = max over pairs of x_i x_j, T104 two-eigenvalue family, Psi >= 0): do not look for one polynomial bound that holds everywhere. Ask first where the max term is small, because that is the only place the inequality can fail, and prove it there by perturbation.

What worked (11 Nov 2026, an agent; note 06_math_research/t104_alon_agent_2026_11_11/GAP_STATE_FORM.md, section "Psi >= 0 for every n"):
1. An exact identity writing the form as (a Gram determinant, so nonnegative) + C m T^2 - (a term that is small when m is not). The Gram part costs nothing and removes the fourth-moment terms.
2. The remainder is negative only when m is below a threshold of order 1/n^2. Translate "m small" into the shape of x: after sorting and scaling, every inner coordinate is below eps of order 2/n^2, so x is the extremal vector (the single edge) plus a small perturbation. Two cases, by which end pair carries the max.
3. On that set compare orders in n: the positive term is of order n^3 eps, the negative ones of order n eps. Crude bounds close with room from n = 14, and the finite range below is a certificate.

What had failed before it: a uniform auxiliary polynomial bound, valid for n = 5..10 by certificate, fails at n = 14 ([[t104_two_eigenvalue_family_n5_to_10_certified_aux_bound_fails_n14_2026_11_11]]). The extremal vectors (edge and star) sit at opposite ends of the range of m, and a single bound has to be tight at both.

What two readers then found in the written proof, none of it fatal, all of it the same kind of slip:
- "sort, flip the sign if needed, scale": the flip reverses the order, so sort again. A normalisation is part of the proof and gets executed on a bad example ((1, ..., 1, -(n-1))) before it is trusted.
- "holds at n = 14 and the ratio grows": a comparison checked at the first n needs a monotonicity argument in n (here four one-line facts), not the word "grows".
- equality cases listed without proving the list is complete.
- a side remark ("the same constants work from n = 10") written from the size of the margin without rerunning the constants: false, they close from n = 13. A remark gets the same exact check as the theorem.

How to apply: before building a bound, find the zero set (equality cases) and the region where the helpful term degenerates; split there; treat each extremal vector by its own local argument; check every numeric comparison exactly at the first n and prove it monotone; run the normalisation on an adversarial vector; rerun the constants for every sentence that names an n. A Codex referee with no history and a hostile peer read caught different things (the peer: nothing; the referee: four), so both are worth their cost (a separate referee run).

Size of the doubt: one problem. The split by "where is the max term small" is general; the orders n^3 eps against n eps are specific to this form.

