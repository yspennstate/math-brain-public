---
name: ag10_cubic_fourfold_solved_2025_hassett_claim_unverified_2026_11_12
description: "Very general cubic fourfold irrational: solved 2025 (Katzarkov-Kontsevich-Pantev-Yu 2508.05105 Thm 6.8, atoms; numbers checked, theory not read). OpenAI 24 Sep 2026 claim that large admissible Hassett divisors are irrational (Kuznetsov's conjecture false) is UNVERIFIED: first half reproved by Guere 2610.40811, second half not followed; do not quote as a theorem"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T03:51:01+02:00
  status: provisional
  evidence: "06_math_research/ag10_cubic_fourfold_agent_2026_11_12/AG10_CHECK.md, ag10_check.out; push 50307bde20be26eb1b0f2c3dc48f9d0dfba8c571"
---

Row AG10 of the top-200 general list (irrationality of the very general cubic fourfold) is solved: Katzarkov, Kontsevich, Pantev, Yu, arXiv 2508.05105, Theorem 6.8 (2025; v2 6 Mar 2026; no journal reference on the arXiv record on 12 Nov 2026).

The argument in one paragraph: atoms (spectral pieces of cohomology under quantum multiplication by the Euler field) are additive under blowups, so a rational fourfold has only atoms of points, curves and surfaces; a surface atom with a p - q = 2 part carries at least 3 Hodge classes; for a very general cubic fourfold c_1* has eigenvalues 9, 9 zeta, 9 zeta^2 and 0, and the 0-piece is one atom of dimension 24 = 2 + 22 with h^{3,1} = 1 and only 2 Hodge classes. We checked the numbers (characteristic polynomial x^2 (x^3 - 27q), Jordan block of size 2 at 0) and Lemma 6.11; we did not read the general theory. Four groups build on it (Guere 2603.04518; Benedetti-Fay-Guere-Manivel-Perrin 2607.26718 recover it by a monodromy criterion).

Separate and UNVERIFIED: OpenAI, "Irrational cubic fourfolds with geometric K3 categories", 24 Sep 2026, 62 pages, claims the very general cubic in every admissible Hassett divisor of large discriminant is irrational, which would disprove Kuznetsov's conjecture. First half (Gromov-Witten, Theorem 3.3) was reproved by Guere, arXiv 2610.40811, from Iritani's formula; of the second half (Sarkisov program, Sections 4-6) the author writes the author could not follow all the arguments, and it is not in the Lean index. Do not quote it as a theorem.

How to apply: do not work AG10 as open. Kuznetsov's conjecture and rationality in C_62 are in flux, not good replacement rows now. See [[nt02_landau_siegel_zeros_excluded_proof_read_in_full_2026_11_12]] for the same routine on another row.

Evidence: 06_math_research/ag10_cubic_fourfold_agent_2026_11_12/AG10_CHECK.md, ag10_check.out.

