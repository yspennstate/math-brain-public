---
name: an07_sendov_proof_reduction_checked_2026_11_12
description: "Sendov's conjecture proved for all degrees (Mazur, Lean; Tao's exposition Aug 2026; An arXiv 2609.04246): reduction read and every step tested numerically, final function sup 0.704 against the needed 1; Lean code and certificate not run; remove the row"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T02:11:33+02:00
  status: verified
  evidence: "06_math_research/an07_sendov_agent_2026_11_12/AN07_CHECK.md, an07_check.out, an07_check2.out; push b532b06f00e70964f28e0fda430beee6b9c342ae"
---

Row AN07 (Sendov's conjecture) of the general-math top-200 list is solved: Mazur's AI-generated, Lean-verified proof (public version 5 Aug 2026, ProofAtlas), Tao's exposition with a second Lean formalization (What's New, 12 Aug 2026), An's rational certificate for the last scalar step (arXiv 2609.04246). The same argument gives the Phelps-Rodriguez strengthening.

What I did (12 Nov 2026): read Tao's introduction and Sections 1-2 in full and An's Sections 1-3; checked by hand the chain from the identity for F' to the raw origin inequality (19); tested every step by computer in floating point (an07_check2.py): the four identities of Lemma 6 on 1926 random polynomials, the AM-GM and Maclaurin bounds, the defect lemma and the step after it, (27), (17) implies (18), (35), the constants 0.1825 and 1.948, (19) implies (21), and (22) for 5 <= n <= 200 (largest value 0.8528 at n = 53, alpha = 17; the text says 0.853 at n = 53). The final function in An's form on 24 million grid points, n = 6..300: sup 0.7040 at n = 35, alpha = 10.11, against An's proved 0.966537.

Not verified by me: Mazur's text, the Lean code, An's certificate, Section 3 (a = 1, Rubinstein) and the n <= 4 section. A second arXiv search is owed (the API was rate-limited).

How to use: do not work on AN07 as open. Open neighbours: Borcea's conjecture for general q, Schmeisser's conjecture, Smale's mean value problem. The proof's toolkit is short and reusable: write the critical points as a - 1/q_j with q_j in the disk, compare p and p' at infinity, 1/a and 0, then AM-GM / Maclaurin on the products and a defect lemma (sinh superadditivity) for points off the circle.

Files: 06_math_research/an07_sendov_agent_2026_11_12/AN07_CHECK.md, an07_check.py, an07_check.out, an07_check2.py, an07_check2.out.
What would change this: an error found in the Lean statement (the formal statement not matching the conjecture), which I did not inspect.

