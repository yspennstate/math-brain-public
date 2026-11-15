---
name: nt02_landau_siegel_zeros_excluded_proof_read_in_full_2026_11_12
description: "Landau-Siegel zeros excluded (OpenAI 1 Oct 2026; Kerr 2610.21099, Banks 2610.15483, Guo 2610.30476): (1-beta) log q >= c absolute; 9-page proof and Kerr's variant read in full and redone by hand, no error; divisibility lemma tested 15 of 15; Lean statement listed; do not work NT02 as open; NT01 lead: Quasi-RH preprints unread"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T03:44:14+02:00
  status: verified
  evidence: "06_math_research/nt02_landau_siegel_agent_2026_11_12/NT02_CHECK.md, nt02_check.out; push 5983739414e04861b7b4a47efad3e6b9f1eebdd6"
---

Row NT02 of the top-200 general list (non-existence of Landau-Siegel zeros) is reported solved, and the report holds up.

Statement: there is an absolute c > 0 with (1 - beta) log q >= c for every real zero beta of L(s, chi), chi primitive real modulo q >= 3.

Sources: OpenAI, "Uniform exclusion of Landau-Siegel zeros", 1 Oct 2026, 9 pages (openai/math, preprints folder of that name, file paper.pdf); Kerr arXiv 2610.21099 (6 pages, auxiliary polynomial variant); Banks arXiv 2610.15483 (explicit constants, 0.003 for q >= 10^10); Guo arXiv 2610.30476 (elementary, c = 1/100). Lean: declaration OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap listed in lean/formalization.yaml; statement read, matches; not compiled by us.

What we did (12 Nov 2026): read the original and Kerr's variant in full and redid every step by hand, no error. Computer tests: retained-row construction identical modulo two primes in 15 of 15 cases; the divisibility lemma (p^(4 E_p) divides Norm Delta for primes with chi(p) = -1) holds in 15 of 15 covered cases at N = 3, close to sharp in three (88 against 84, 36 against 32, 92 against 84), and fails where the lemma does not claim it (Frobenius tau: 188 against 220 and against 344).

The idea, for reuse: K = Q(sqrt d, sqrt 2); points theta_n in a box of the rank-4 lattice sent to three conjugates; a determinant of monomials ordered by weight alpha_1 + H(alpha_2 + alpha_3); Hadamard above; below, divisibility from theta^p = g(theta) mod p for the Frobenius classes sigma and sigma tau. Balance check: with k usable conjugates out of n the usable prime density k/n times the exponent n/k is exactly 1 in the generic case, so the method contradicts nothing unless the usable primes are denser than generic, which is what a zero near 1 forces.

How to apply: do not work NT02 as open. Rows stated conditionally on no Siegel zeros change status. Lead: openai/math also holds two preprints "The Quasi-Riemann Hypothesis" (30 Sep and 5 Oct 2026) claiming a zero-free half-plane Re s > 7/8, unread; row NT01 should be checked against them.

Evidence: 06_math_research/nt02_landau_siegel_agent_2026_11_12/NT02_CHECK.md, nt02_check.out, nt02_check2.out.

