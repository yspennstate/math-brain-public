---
name: t104_alon_two_thirds_conjecture_n4_proved_dual_form_2026_11_11
description: "Alon's 2/3 Specht-module conjecture (arXiv 2610.22151, implies Oliveira, row T104) at n=4? Proved 11 Nov (candidate, one author): lambda_max(L_G) <= (4/3)W + (2/3)D, equality on K_{1,3}; plus a dual form of C(tau,sigma) for any n and a transfer idea; search n<=6 finds nothing below 2/3. Folder 06_math_research/t104_alon_agent_2026_11_11"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T02:00:58+02:00
  status: provisional
  evidence: "N4_PROOF.md, n4_check.out (0 failures of 200000), dom_n4/5/6 tsv in the folder"
---

Row T104 (Oliveira's conjecture on the interchange process). G. Alon, arXiv 2610.22151 (15 Oct 2026), Theorem 1.8:
Conjecture 1.5 there (lambda_min(G, tau) >= (2/3) lambda_min(G, sigma) on Specht modules whenever sigma != [n]
dominates tau, every weighted graph G) implies Oliveira. Known there: quasi-complete graphs, a general constant 1/n^3,
2/3 attained on stars for unbounded n.

What we have, in 06_math_research/t104_alon_agent_2026_11_11 (brain repo):

1. N4_PROOF.md, Theorem 3: the conjecture holds for n = 4. The only pair that needs work is tau = 211, sigma = 22,
   where lambda_min(G, 211) = 2W - lambda_max(L_G) and lambda_min(G, 22) = W - D, D = sqrt(a^2+b^2+c^2-ab-bc-ca) with
   a, b, c the weights of the three perfect matchings. The inequality lambda_max(L_G) <= (4/3)W + (2/3)D is proved
   edge by edge with an explicit three-case certificate; equality on K_{1,3}. Checked numerically (n4_check.py,
   200,000 weights and 200,000 vectors, no failure). One author, no outside audit yet: candidate.

2. N4_PROOF.md, Proposition 1 (dual form, any n): C(tau, sigma) >= c iff for every unit psi in V_tau there is a
   density matrix rho on V_sigma with 1 - <psi, tau(ij) psi> >= c (1 - tr(rho sigma(ij))) for all pairs ij.
   Proof: von Neumann minimax over weights and states.

3. TRANSFER_IDEA.md: pair energies split over isotypic components (Lemma A), pointwise 1-Lipschitz maps on a
   permutation module do not raise any pair energy (Lemma B), tensor-power bound
   C >= sup_k inf_psi |P_sigma psi^{tensor k}|^2 / k. Pure transferred states vanish at psi whose line is fixed by a
   subgroup with a character absent from V_sigma (n = 4: the body diagonal of the cube, which is the star
   eigenvector); the matching state there is maximally mixed. No constant obtained from this yet.

4. alon_search.py: minimisation of the ratio over weights (Young's orthogonal form, L-BFGS). Smallest ratios found:
   n = 4: 0.6667 (211, 22); n = 5: 0.75 (2111, 221); n = 6: 0.6667 (2211, 222 and 21111, 222). On the star,
   tau = [a, 1^{n-a}], sigma = [a^{n/a}] gives exactly a/(a+1).

How to apply: before working T104 again read STATE.md there. A universal constant in place of 2/3 would already
give Oliveira; the n = 5 pairs left are (32; 311, 221, 2111), (311; 221, 2111), (221; 2111). Do not claim the n = 4
theorem as audited until a second reader has checked N4_PROOF.md.

