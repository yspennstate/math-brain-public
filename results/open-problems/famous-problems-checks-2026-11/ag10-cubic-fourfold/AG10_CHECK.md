# Row AG10: irrationality of the very general cubic fourfold

Checked 12 Nov 2026. Verdict: solved in 2025 by Katzarkov, Kontsevich, Pantev and Yu. The row should leave the list
of problems to attack. A stronger claim of 2026 about special cubic fourfolds is recorded below as unverified.

## The statement of the row

A very general smooth cubic hypersurface in P^5 over C is not rational.

## Sources

- L. Katzarkov, M. Kontsevich, T. Pantev, T. Y. Yu, "Birational invariants from Hodge structures and quantum
  multiplication", arXiv 2508.05105 (v1 7 Aug 2025, v2 6 Mar 2026), 82 pages. Theorem 6.8 is the statement of the
  row. Read: the introduction, Section 6.2 (Theorem 6.8, Lemma 6.11, Corollary 6.12) and the table of atoms of
  varieties of dimension at most 2. The general theory of atoms (Sections 2 to 5) was not read line by line.
- J. Guéré, arXiv 2603.04518: every rational smooth cubic fourfold has primitive cohomology isomorphic, as a
  rational Hodge structure, to the twisted middle cohomology of a projective K3 surface. Abstract read.
- V. Benedetti, A. Fay, J. Guéré, L. Manivel, N. Perrin, arXiv 2607.26718: a criterion from the theory of atoms
  that uses only monodromy, and recovers the irrationality of the very general cubic fourfold without computing
  quantum products. Abstract read.
- J. Guéré, arXiv 2610.40811, 16 pages. Introduction and Section 1 read.
- OpenAI, "Irrational cubic fourfolds with geometric K3 categories", 24 Sep 2026, 62 pages (openai/math, folder
  of that name). Introduction, Proposition 3.10, Theorem 6.6 and Proposition 7.1 read.

## The argument of Theorem 6.8, and what was checked

An atom is a piece of the spectral decomposition, under quantum multiplication by the Euler field, of the
cohomology with its Hodge structure. Atoms are additive under blowups (through Iritani's blowup theorem), so by
weak factorization the atoms of a rational fourfold are atoms of points, curves and surfaces. A surface atom whose
Hodge structure has a part with p - q = 2 carries at least three rational Hodge classes (H^0, an ample class, H^4).

For a cubic fourfold X whose only rational Hodge classes are the powers of the hyperplane class P:

- the even cohomology has dimension 27 = 5 + 22 (powers of P, and the primitive part of H^4);
- quantum multiplication by P on the span of the powers of P is P*1 = P, P*P = P^2, P*P^2 = P^3 + 6q,
  P*P^3 = P^4 + 15qP, P*P^4 = 6qP^2; it kills the primitive classes (Lemma 6.11);
- so c_1* = 3P* has eigenvalues 9, 9 zeta, 9 zeta^2 and 0, the last with a generalized eigenspace of dimension
  2 + 22 = 24 that contains the whole primitive part, which is irreducible for a very general X and has
  h^{3,1} = 1;
- that 24-dimensional piece is one atom with p - q = 2 part and only two rational Hodge classes. No point, curve
  or surface has such an atom. Hence X is not rational.

Checked here (`ag10_check.py`, `ag10_check.out`): the characteristic polynomial of P* is x^2 (x^3 - 27q), the
relation P^5 = 27 q P^2 holds, the eigenvalue 0 of c_1* has algebraic multiplicity 2 and a one-dimensional kernel
on the ambient part (one Jordan block of size 2), and the count 2 < 3. The proof of Lemma 6.11 (a dimension count
and the fact that P and the class of a point come from the ambient space) was read and is correct.

Not checked: that atoms are well defined and additive under blowups. That is the content of Sections 2 to 5 and
rests on Iritani's blowup theorem and on the theory of F-bundles.

## How far the result can be trusted

It has not been confirmed line by line by us, and the arXiv record carries no journal reference. Against that:
within fifteen months at least four groups not sharing all authors have built on the theory and on this theorem
(Guéré; Benedetti, Fay, Guéré, Manivel and Perrin, who recover the theorem by a shorter route inside the same
framework; Fay on Verra and Gushel-Mukai fourfolds; Cavenaghi, Katzarkov, Pomerleano and Zhang on Shokurov's
conic-bundle conjecture). The literature is being read critically: the arXiv comment on Fay's 2604.14850 withdraws
its main proof because weak factorization was used as if it were equivariant. Three searches of 12 Nov 2026
(`lit/search/s1.xml`, `s2.xml`, `s3.xml`) found no paper disputing Theorem 6.8.

## A stronger claim, unverified: special cubic fourfolds

The OpenAI preprint claims: there is d_0 such that for every admissible Hassett discriminant d > d_0 a very general
cubic fourfold in the divisor C_d is irrational, although its Kuznetsov component is the derived category of a K3
surface. This would disprove Kuznetsov's rationality conjecture and the sufficiency half of the associated-K3
prediction. The threshold is ineffective; C_14, C_26, C_38 and C_42 consist of rational cubics, so d_0 >= 42.

The proof evaluates one integer c_u(f), a signed count of divisors whose maximal rationally connected quotient is a
K3 surface in a fixed Hodge-isometry class, on a hypothetical birational map f from P^4 to X in two ways.

1. Through a smooth weak factorization and genus-zero Gromov-Witten theory: c_u(f) = 1 (Proposition 3.10, from
   Theorem 3.3).
2. Through a Sarkisov factorization: c_u(f) = 0 once d is large (Theorem 6.6, Sections 4 to 6, about 45 pages).

Status of the two halves. Guéré (2610.40811) reproves Theorem 3.3 from Iritani's formula and shows that the
invariant is part of the theory of atoms; he obtains the integral version of his earlier theorem. Of the second
half he writes that the preprint "has not yet been implemented in Lean and we were not able to follow all the
arguments in the proof". No entry for this preprint appears in `lean/formalization.yaml` of openai/math at commit
1581d4cb. We read the statements of the second half and none of its proofs.

Checked here: the admissibility condition as stated in the preprint gives 14, 26, 38, 42, 62, 74, 78, 86, 98, ...
and agrees with Hassett's description (d divides 2(n^2 + n + 1)) for all d up to 200; the four divisors known to be
rational are admissible, so the claim does not contradict a known rationality theorem.

So the claim stands as: first half confirmed by a specialist, second half read by nobody we could find. It should
not be quoted as a theorem.

## For the list

- Take AG10 off the problems to attack. Mark it solved (Katzarkov, Kontsevich, Pantev, Yu 2025). Check level:
  statement and the cubic computation checked, the general theory not read; four groups build on it.
- The natural open problems next to it are in flux and are poor replacement rows for the moment: Kuznetsov's
  conjecture (claimed false above a threshold, half verified), rationality of the very general member of C_d for
  the first open admissible value d = 62, irrationality of a specific smooth cubic fourfold over the rationals.
- A verification of Sections 4 to 6 of the OpenAI preprint would be worth more than a new row. The points where
  it can fail are the uniform genus bound for pencils on K3 surfaces of Picard number one and the independence of
  the correction s on conic-bundle nodes from the chosen presentation (Section 6).
