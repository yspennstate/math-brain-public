---
name: t188_odlyzko_poonen_proof_core_checked_2026_11_12
description: "Odlyzko-Poonen conjecture proved unconditionally (Kogler, arXiv 2609.26771): twin factorizations are rare; core read and enumerated to n = 20; Breuillard-Varju and Dobrowolski inputs and the Lean code not verified; remove the row"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:59:44+02:00
  status: verified
  evidence: "06_math_research/t188_odlyzko_poonen_agent_2026_11_12/T188_CHECK.md, t188_check.out, t188_check2.out; push 99214ebb6dadd9576229c36cadc61bf757c78cd7"
---

Row T188 (Odlyzko-Poonen conjecture: a random 0-1 polynomial with constant term 1 is irreducible with probability tending to 1), 12 Nov 2026.

Proved unconditionally by Kogler, arXiv 2609.26771v2 (14 Oct 2026, 11 pages, proofs credited to GPT-6 Astra, Lean formalization of about 22,000 lines not inspected by us). P(reducible) = sqrt(2/(pi n)) + O(1/n); the noncyclotomic part is irreducible with probability 1 - C exp(-c n / (log n)^4).

The proof in one paragraph. Twin factorization (Ljunggren, Filaseta): if P = A B then Q = A B* is again a 0-1 polynomial with Q Q* = P P*, and Q is P or P* only when A or B is reciprocal. So a reducible P has a reciprocal factor or a non-trivial twin. Twins are rare (Theorem 1.3, at most 8 (3/4)^floor((n-1)/4)): reduce modulo 2, write P and Q as lifts of a b and a b*, and look at half the coefficients of P P* - Q Q* modulo 2; sampling b through b + b*, flipping b_k changes the k-th of them by a triangular linear function, which gives a factor 3/4 per index. Reciprocal non-cyclotomic factors are excluded by Dobrowolski and the Breuillard-Varju separation lemma; cyclotomic factors by Breuillard-Varju section 9.2; x + 1 gives the main term.

Checked: every step read; the elementary core by computer from the statements. Theorem 1.3 by enumeration to n = 20 (no twin mod 4 for n <= 10; fraction 0.0117 at n = 12 falling to 0.0032 at n = 20; the stated bound is above 1 there, so only the decay is tested). Proposition 2.1 and its proof steps on 698027 pairs. Lemma 3.1 for all reducible P, n <= 11. Lemma 3.5 for n <= 18 (the proof's sum is attained). Reducible fractions for n = 10..15 match Remark 3.4's expansion with B = 4(1 + sqrt 3)/pi and the parity term. Not verified: Dobrowolski, Breuillard-Varju Lemmas 26 and 45 and section 9.2, the Lean code.

Technique card: to show a factorization is unlikely, map it to a second object with the same invariant (here the autocorrelation P P*) and show collisions of the invariant are rare by reducing modulo 4 and revealing coefficients in an order that makes the constraint triangular.

Files: 06_math_research/t188_odlyzko_poonen_agent_2026_11_12/ (T188_CHECK.md, t188_check.py, t188_check2.py and outputs). Row proposal: remove; the earlier KEEP verdict in the review predates reading the paper. Candidates nearby, not vetted: Galois group of P_n without the Riemann hypothesis; 0-1 polynomials with few terms.

