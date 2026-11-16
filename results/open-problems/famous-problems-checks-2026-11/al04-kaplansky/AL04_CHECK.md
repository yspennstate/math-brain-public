# Row AL04 (Kaplansky's zero-divisor conjecture): what the positive-characteristic preprints prove, and the finite parts recomputed

12 Nov 2026. Sources read from their text: arXiv 2610.17662v1 (S. V. Ivanov, 13 Oct 2026, "Zero divisors in group
algebras of torsion-free groups in odd characteristic") in full except Section 6; arXiv 2611.04599v1 (N. Mghirbi,
S. Douglas, 3 Nov 2026, "Kaplansky's conjectures fail for torsion-free hyperbolic groups in positive
characteristic"): abstract, introduction, Appendices B and C. Not read: the characteristic-two source, OpenAI,
"A torsion-free group algebra with zero divisors" (23 Sep 2026, a preprint on GitHub, not on arXiv), on whose
Sections 3 to 5 both papers rest.

## The claims

- OpenAI (p = 2): a finitely presented torsion-free group G with a finite two-dimensional classifying space and
  nonzero a, b in F_2[G] with ab = 0. The proof is probabilistic (random labelled graphs coned off in a rose).
- Ivanov (odd p), Theorem 1.1: the same for F_p[G_p], every odd prime p. Corollary 1.2: the conjecture fails over
  every field of positive characteristic.
- Mghirbi and Douglas: for every prime p a torsion-free word-hyperbolic group with a, b in F_p[G], ab = 1 and
  ba not 1; so the zero-divisor, idempotent, unit and direct-finiteness conjectures all fail there. Their Appendix C
  states that the existence of G, a, b for every prime p is formalized in Lean 4, with the random-graph estimates in
  existence form ("for all large sizes some outcome has the stated properties"). Not formalized: the probability
  statement of their Theorem A, their Section 6 (the zero-divisor model) apart from Lemma 6.1, Section 8, Theorem D.
- All three constructions are existence proofs. No presentation and no explicit pair of elements is given; for
  p = 3 Ivanov's alphabet alone has 760 letters.

## How Ivanov's argument is put together

1. Signed cancellation (Lemma 2.2). Two immersed labelled graphs, the first bipartite with signs alternating along
   edges; if every pair of vertex types meets in d letters modulo p with p not dividing d, then
   alpha = sum of eps(x) g_x and beta = sum of h_y^{-1} satisfy alpha beta = 0 over F_p. The proof is a signed
   handshake count on the components of the step graph.
2. A design (Section 3): letters are the points of PG(2, q), q = p^3, and p extra letters; a type is a line, with
   or without all the extras. Two types meet in 1, q + 1, 1 + p or q + 1 + p letters, all 1 modulo p.
3. A decay estimate (Proposition 5.3): the sum of P(W)^2 over words of length h decays like (1 - 1/(4(q+1)))^h,
   proved with the test vector (p + 1, 1, 1) on a 3 x 3 lumped matrix.
4. The geometric part (torsion-free, aspherical, roots separated) is taken from Sections 3 to 5 of the OpenAI
   preprint with one extra bounded factor (Section 6, Appendix A).

## What was recomputed here (al04_check.py, output al04_check.out, 5 seconds)

Items 1 to 3 are finite and were recomputed with a program written from the paper's definitions.

- Proposition 5.3: M phi <= theta phi holds exactly for all 167 odd primes below 1000 and q = p^3, p^4, p^5.
- p = 3: PG(2, 27) built from F_27 = F_3[x]/(x^3 + 2x + 1), 757 points, every two lines meeting in one point.
  At n = 2 v^2 every letter lies in 42392 = f n types of B (Lemma 3.3); the cross-intersections are 1, 4, 28, 31
  (Lemma 3.4); the turn weights are 1/28, 28/757 and 1 (Lemma 5.1); every row of the 760 x 760 matrix lumps
  exactly to the 3 x 3 matrix of Lemma 5.2; both spectral radii are 0.976461, the value in the paper's Appendix B.
- Table 2: spectral radii 0.97646, 0.99366, 0.99751, 0.99932, 0.99958 for p = 3, 5, 7, 11, 13, as printed. The gap
  for p = 11 comes out 6.82e-4 against the printed 6.83e-4, a rounding difference. Remark 5.4: at q = p, p = 3 the
  radius is 1.326; at q = p^2 it is below 1 for p up to 13 and the test vector fails, as stated.
- Lemma 2.2 on random instances at p = q = 3 with 338 vertices a side (small girth, no group is claimed): in
  three samples the step graph has 28245, 28197 and 28172 components; every component has signed degree sum 0 and
  signed vertex count divisible by 3; about 2500 components have a nonzero signed count over Z, and all but one to
  three have size not divisible by 3, so the unsigned count does not vanish. (The paper reports 28,245 components
  for its own sample; the largest components differ, 37757 here against 38,808 there, so the samples are not the
  same.)
- Two controls. With the first graph sampled without the bipartition the signed degree sum is nonzero on 16410
  components and the congruence fails on 15489. With one extra letter in place of three (cross-intersections 1, 2,
  4, 5) the degree sum still vanishes and the congruence fails on 6325 components. Both hypotheses of Lemma 2.2
  are needed, and the program detects a failure when there is one.

## What was not checked

The step that makes the group torsion-free and the two elements nonzero: the bounded-pattern estimate, the
exclusion of reduced spherical arrangements and root separation (Ivanov's Section 6, the OpenAI preprint's
Sections 3 to 5). The Lean development was not built or read here; the verification repository named in
2611.04599 answers (HTTP 200 on 12 Nov). The arXiv search of 12 Nov (lit/search/s1.xml, phrase "zero divisor
conjecture", newest first) shows no comment or correction on either paper.

## Proposal for the row

Positive characteristic: reported disproved by three preprints, one of them with a Lean formalization of the
existence statement for every prime; the finite arithmetic of the odd-characteristic paper holds. The row should be
restated to characteristic zero: for a torsion-free group G and a field K of characteristic zero, does K[G] have no
zero divisors (the usual forms are K = Q and K = C; a zero divisor over C specializes to one over the algebraic
closure of Q).
Two facts from the papers that belong beside it:
- a counterexample over Q would contradict the strong Atiyah conjecture for that group;
- the mechanism does not lift: over Z the cancellation needs every cross-intersection equal to d exactly, the
  line-line intersection matrix qI + J has rank one only modulo p, and the obvious designs with constant
  intersections destroy the decay estimate (Ivanov 8.2; Mghirbi and Douglas, Theorem 8.1). Ivanov 8.3: one group
  with fixed supports working for infinitely many primes would give zero divisors over the algebraic closure of Q,
  hence over C; the constructions give no such uniformity.
