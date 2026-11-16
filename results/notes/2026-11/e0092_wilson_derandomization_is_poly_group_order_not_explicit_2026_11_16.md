---
name: e0092_wilson_derandomization_is_poly_group_order_not_explicit_2026_11_16
description: "E0092 Diaconis explicit Wilson generators: package proof correct but 2^{O(n)} = poly(|G|) Toeplitz derandomization, not explicit; open per Hermon-Olesker-Taylor OP2; not posted"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T05:35:00+02:00
  status: provisional
  evidence: ""
---

E0092 (Diaconis 2013, arXiv:1309.7754, Question 1: an explicit generator set for item 2 of Wilson's theorem on F_2^n, e.g. N=2n) is NOT a postable resolution, though the package's proof is correct.

What the internal package proves: one deterministic algorithm fixes the 3n-1 bits of an n x 2n Toeplitz matrix by conditional expectations on Phi = sum_w Q_w/eta_w (shell collision energies); E Phi = (1-2^-n)/2 by two-universality, so every Q_w < eta_w, and the shell decomposition of the 2n-cube walk gives TV < eps after (1+eps) 0.24853 n steps. Read line by line on 16 Nov; rerun exactly for n=4,5,6 (E Phi identity, every step monotone, max Q_w/eta_w about 0.05).

Why not posted: the algorithm sums over all 2^{2n} vectors y at each of 3n-1 steps, so it runs in time polynomial in |G| = 2^n, the textbook Toeplitz/Gilbert-Varshamov derandomization class that coding theory does not call explicit; the lexicographically first seed with Phi < 1/2 is equally deterministic. Hermon and Olesker-Taylor (arXiv:2102.02809, Open Problem 2) restate Diaconis's question as explicit generators with cutoff at the entropic time and call it open even for Z_p. The walk's eigenvalues are 1 - 2 wt(M^T a)/N and T_W is the rate-1/2 GV point, so a strongly explicit answer sits next to explicit GV codes.

How to apply: before calling any "almost all choices" result answered by a deterministic construction, compare its running time with exhaustive search over a finitely checkable certificate; same class means not explicit. A poly(n) construction would reopen this.

