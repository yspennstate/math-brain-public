---
name: dg09_stable_bernstein_r7_claimed_section13_checked_2026_11_12
description: "Stable Bernstein in R^7 claimed (Hong-Li-Wang arXiv 2609.15720, 85 pages, Green-function moments to exponent 5/2 by rational certificates, then Brendle isoperimetry). Section 13 constants verified 8 of 8; 70 pages and certificates unread; authors' repo has Lean for the algebra, not built; no independent confirmation - keep REPORTED_SOLVED"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T04:12:39+02:00
  status: provisional
  evidence: "06_math_research/dg09_stable_bernstein_agent_2026_11_12/DG09_CHECK.md, dg09_check.out; push 08436890b5796d0ce8693f126dfa66e7b1c46757"
---

Row DG09 of the top-200 general list (stable Bernstein problem in R^7: a complete two-sided stable minimal hypersurface of R^7 is a hyperplane) is claimed solved by Hong, Li, Wang, arXiv 2609.15720 (14 Sep 2026, 85 pages), and not confirmed by anyone else as of 12 Nov 2026.

The proof: after reduction to bounded curvature, with G the minimal Green function and J(t) the integral of |grad G|^3 over {G = t}, all moments int J(t) t^(-sigma-1) dt with sigma < 5/2 are finite (from 2 to 2.46 by Bochner, Simons, stability and Codazzi; to 2.4962 by stability on a nonlinear norm of two test functions, fifteen rational parameter intervals; to every sigma < 5/2 with three more tensor identities; the algebra is checked in exact rational arithmetic), then Brendle's sharp isoperimetric inequality fixes the sign of a boundary term and forces A = 0. The authors say AI assistance played a substantial role.

Their repository github.com/wgaom/stable-bernstein-R7 (commit 619b75d4 on 12 Nov) holds the Mathematica notebook and 144 Lean files; the README says the two algebraic estimates are kernel-checked. We did not build it; it covers the algebra only.

Checked by us: Section 13 in full (8 exact symbolic checks: flat-model J(t) = 32 sqrt(w5) t^(5/2), volume constant 1/(48 sqrt(w5)), the Brendle chain, J_inf >= 32 sqrt(w5), all equalities in the flat model). Not checked: about 70 pages (Sections 3-12, 14) and the certificates. One paper uses the theorem as input (Z. Wang 2609.19120).

How to apply: do not attack DG09; keep it REPORTED_SOLVED. Cheapest upgrade: build the Lean folder on a worker machine after reading its lakefile. Same routine as [[dg08_cartan_hadamard_solved_2026_key_inequality_checked_2026_11_12]].

Evidence: 06_math_research/dg09_stable_bernstein_agent_2026_11_12/DG09_CHECK.md, dg09_check.out.

