# Referee report: a flux plateau for site-disordered finite-capacity exclusion

Paper: yspennstate/flux-plateau-disordered-k-exclusion at 8f2c93c (main.tex, 849 lines, 11 pages). Referee:
an agent, 14 Nov 2026.
Claim: totally asymmetric K-exclusion on Z with i.i.d. site rates alpha_i on [r,1], ess inf r > 0, law not constant:
the hydrodynamic flux is f_K(rho) = r M_K for |rho - K/2| <= mu r M_K, where mu = 1/r - E[1/alpha_0] and M_K is the
maximum of the homogeneous rate-one flux. This answers Seppalainen's survey (math/9906194), Section 4, Problem 4,
for every finite K. For K = 1 it is Sly's Theorem 1 (arXiv:1609.06589).

## Verdict

SOUND. No change made.

## Proofs checked (re-derived)

- Passage recurrence with steps (0,1), (1,0), (-1,K) and Lemma 2.1: the weights are conditionally independent given
  the environment, from the predecessor ordering and the strong Markov property.
- Tail bound 3 * 6^L e^{-ru/2}, with L = |i| + 2j.
- Coupling order. The reflection S(x,y) = (-x, y + Kx) is an involution that swaps the two horizontal steps.
- Lemma plane: concavity at the midpoint.
- Delay identity: Exp(alpha) + Ber(1 - r/alpha) * Exp(r) has law Exp(r), and E d_i = mu.
- Proposition comparison (mandatory columns). Lemma slow intervals.
- Proposition capacity: strip copies are disjoint except at the shared vertex; connectors; strong law;
  E V_m / m -> tau_1(0,1).
- Lemma line and the proof of the theorem: the interval lies in [0,K], and A |K/2 - rho| <= mu.
- Corollary binary: (1 - p)(1 - r/s) M_K.

## Citations checked against the sources

- Sly (1609.06589v1): Theorem 1 gives f = r/4 on [1/2 - mu r/4, 1/2 + mu r/4], which is the K = 1 case. The coupling
  Z = Y + U with U ~ Ber(1 - r/alpha) * Exp(r) is the delay identity used here.
- Seppalainen survey (math/9906194): the generator (3.1), Theorem 3, and Problem 4 as quoted. The paper writes
  k_alpha = -f_K^* "in equation (3.2)"; the conjugate is defined just before (3.2), so this reading is fair.
- Seppalainen, Translation invariant exclusion processes (book manuscript, 11 Dec 2008; the URL answers 200):
  - Theorem 9.5 (printed p. 141) states that f is concave and continuous on V, that 0 < f <= 1 in the interior, and the
    reflection symmetry (9.21). That is what the paper cites it for.
  - Lemma 9.11 and (9.40)-(9.44) are on printed pp. 148-150, as cited.
- Bahadoran-Bodineau (1602.06718v4):
  - Theorem 3.4 is on p. 13. The K-exclusion remark follows it in Section 3.2, so the locator is right.
  - Theorems 2.4 and 2.6 and condition (H) are present.
  - The remark itself opens by extending Theorem 3.3. A reader looking for "the remark on Theorem 3.4" may pause, but
    the position cited is exact.
- Crossref:
  - 10.1214/18-EJP137: Electron. J. Probab. 23 (2018), pp. 1-44. Project Euclid gives it as no. 44.
  - 10.1214/aop/1022677266: Ann. Probab. 27 (1999), no. 1, 361-415.
  - Authors and titles match for both.
- Prior-work search (web, two wordings): the plateau results found are all for K = 1. Nothing found settles K >= 2.

## Build

- A fresh pdflatex build gives 11 pages (README says 11), no overfull boxes and no undefined references.
- Its text is identical to the committed main.pdf (pdftotext diff empty).

## Minor (not acted on)

- The affiliation and email differ from the other recent repositories.
  That is the author's choice.
- The repo has no code, consistent with "No data were used".
- Lint notes:
  - \PP at l.376 is used without a gloss.
  - \mid and \vert are mixed for the conditioning bar.
  - One "the above inequality" reference (l.695) could carry an \eqref.
