# Row NT01 (the Riemann hypothesis): state of the check

Started 12 Nov 2026, 04:53. Not finished. Nothing pushed yet.

## What the sources are

- OpenAI, "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s) > 7/8", 30 Sep 2026, 199 pages
  (openai/math, folder `The-Quasi-Riemann-Hypothesis-September-30-2026`, `paper.pdf`; local `lit/openai_sep30/`).
  Unread.
- OpenAI, "The Quasi-Riemann Hypothesis", 5 Oct 2026, 49 pages (folder `...-October-5-2026`, `paper2.pdf`; local
  `lit/openai_oct5/paper_c.txt`, 2179 lines). A separate, shorter paper: Theorem 1.1, every finite-order Hecke
  L-function over Q(sqrt -3), hence every Dirichlet L-function and zeta, has no zero in Re s > 11/12. Sections 1 to 3
  read (lines 1 to 526).
- Follow-ups found in three dated searches (`lit/search/s1.xml`, `s2.xml`, `s3.xml`): B. Liu 2610.12234 (7/8 to
  0.874957, by varying parameters, "following the same strategy"; says a Lean check of the exponent system exists);
  Xu and Sang 2610.15291 (0.8748867, "assuming the analytic inputs of that work"); Frei, Sofos, Widmer 2610.18491
  (applications, treats the result as proved); B. Liu 2610.26835 (all number fields, 0.874886...); M. Visser
  2610.20058 ("there are good reasons to be cautious regarding these claims"; consequences if true).
  None is an independent verification of the analytic core. No dispute found.
- Lean index of openai/math: the 7/8 paper is listed as an article; no formal declaration seen for it (to confirm).

## The route of the 49-page paper, as read

1. Zero-free half-plane from A_1(D) = sum mu(n) nu(n) W(N n / D) << D^(11/12 + eps) (Section 3, read in full; the
   Mellin argument and the base change L_K(s, chi o N) = L(s, chi) L(s, chi chi_-3) are standard and correct).
2. A_1 is embedded in the family A_u(D) with sextic twists chi_n(u) = (u/n)_6. Proposition 3.1:
   sum over 0 < N(u) <= D^(1+theta) of |A_u(D)|^2 << D^(2+theta+eps), theta <= 1/10. Sixth powers u = p^6 give
   A_u = A_1 + O(D/Y); there are about H^(1/6) of them; (3.2) gives |A_1|^2 << D^(11/6 + 5 theta/6) + D^(5/3 - theta/3).
   Arithmetic rechecked by hand: correct.
   Remark: Proposition 3.1 is the ideal large sieve bound for this coefficient sequence. It is false for a_n = 1
   (sixth-power rows give H^(1/6) D^2 > D H when theta < 1/5), so the proof must use mu, and it follows from GRH.
3. Poisson in u; Gauss-Jacobi: mu(n) gamma_-1(n) = chi_n(-1) G(n)^-1 alpha(n) gamma_2(n), alpha(n) = conj(n)/|n|.
   The sign mu comes from J(psi, psi) = -pi for primary pi = 1 mod 3. Dual sums B_h(X) are sums of cubic Gauss
   sums = coefficients of Kubota's cubic theta function, twisted by chi_n(h).
4. Theta automorphy: the twist becomes the quadratic character chi_h^3 (chi^-1 chi^-2 = chi^-3), and the quadratic
   large sieve of Goldmakher-Louvel gives the completed bound (2.15): sum_h |T_h(X)|^2 << H + H^2/X.
5. Cube factors removed by Moebius inversion and a recursion with two Poisson summations (Heath-Brown's method);
   scaling of the recursion in the outline rechecked by hand: consistent.

## Not done

- Sections 4 to 7 and the appendices (lines 527 to 2067): unread. The weight of the proof is Proposition 6.2
  (theta transformation with twists, Appendix A.2), Lemma 6.3 (uniformity in the twist) and Section 5.
- Computer check planned: Lemma 4.1 / Appendix A.1 (the Gauss-Jacobi identity for squarefree primary n of small
  norm in Z[omega]); a small-scale look at Proposition 3.1 with the controls a_n = 1 and random signs.
- The 199-page paper: statement, and whether it depends on other preprints.
- Note NT01_CHECK.md, push 66, message to an agent.

## For the list (provisional)

RH itself is not claimed. Row NT01 keeps DESERVES. The row's note should say: a zero-free half-plane Re s > 7/8
(and later about 0.8749) is claimed by OpenAI (Sep/Oct 2026), unconfirmed; five follow-up papers assume it.

## 12 Nov 05:28 - computer check of Lemma 4.1 (nt01_check.py)
227 squarefree primary n with N(n) <= 1500, 168 coprime pairs. As the text extraction prints the lemma
(nt01_check_asextracted.out): |gamma_j| = 1, (4.2a) gamma_2^3 = mu n/|n|, (4.3), |G| = 1, (4.1), (4.6) hold in
every case; (4.2b), (4.4), (4.5) hold in 81 of 227 only. Reading: overlines lost by pdftotext. The duplication
formula for Gauss sums gives gamma_1 gamma_2 = mu alpha conj(chi_n(4)) gamma_3, so G(n) = conj(chi_n(4)) gamma_3(n),
and (4.4), (4.5) then carry conj(alpha). Second run with that G is nt01_check.out. Still to do: look at the PDF
page of Lemma 4.1 (page 13) to see whether the bars are printed; NT01_CHECK.md; push 68; message to an agent.

## 12 Nov 05:30 - page 13 looked at; check file written
The printed page has the bars: alpha(n) = n/|n|, G(n) = conj(chi_n(4)) gamma_3(n), conj(alpha) in (4.4), (4.5)
and in a_xi, conj(G(a)) in (4.7). With them every identity (4.1) to (4.6) holds in all 227 cases and 168 pairs
(nt01_check.out); three planted wrong forms fail. NT01_CHECK.md written. Not done: (4.7) (equivalent to
R(a, a) = chi_a(-1), testable with a prime in the class of a); Sections 4.2 to 7; Appendices; the 199-page
preprint. paper_c.txt loses every overline: compare with the page before testing any further identity.

## 12 Nov 05:41 - identity (4.7) tested
nt01_check47.py: (4.7) is equivalent, given (4.1), to R(a, a') = chi_a(-1) for a prime a' in the ray class of a.
Tested for 44 primes a of norm up to 200 against primes a' of norm up to 2500 congruent to a modulo M. It holds
on every pair for M = 4, 12, 24, 36 (1283, 1283, 275, 114 pairs) and fails for M = 1, 2, 3, 6, 9 (for M = 1 on
6272 of 15928 pairs). So the "sufficiently large" modulus has to be divisible by 4, as quadratic reciprocity in
Z[w] predicts (the ratio is the Hilbert symbol at 2). Lemma 4.1 is now checked in full except the statement that
G factors through the ray class group. Next: Sections 4.2 to 4.5 (lines 583 to 788 of paper_c.txt) against PDF
pages 13 to 17, by part; then Appendix A.1.

## 12 Nov 05:47 - Section 4 checked
Lemma 4.2: derived independently and tested numerically (nt01_check42.py: 240 of 240 cases to 4.9e-14; the two
wrong forms fail on every nonvanishing case). Page 14 looked at: the text file drops the square root over N(m)
and the bar on chi(h) in (4.8). Lemma 4.4 and the algebra of Proposition 4.5 down to (4.16) and (4.17) checked
by hand; (4.15) is where (4.7) is used. Section 4 is correct as printed, given Lemma B.2. Next: Lemma B.2
(Appendix B, from line 1974 of paper_c.txt), then Section 5 (from line 789), each against the PDF pages.

## 12 Nov 05:56 - Lemma B.2 and Section 5 checked
Lemma B.2 (page 45): correct as printed; the text file drops the square root in (B.4). Section 5 (pages 18 to
22): the completed sum (5.3), Lemma 5.3 (cube inversion: (5.8), the short part (5.9), the long part, the two
edge cases), the induction of Section 5.5 and Section 5.6 checked line by line; all correct. The chain from the
mean square of Proposition 3.1 now rests on two unread statements: Proposition 5.2 (Section 6, from line 991 of
paper_c.txt) and Proposition 5.4 (Section 7, from line 1299). Next: Section 6, by part, against the PDF pages
from page 22.

## 12 Nov 06:07 - Section 6 checked
Section 6 (pages 22 to 29, page 6 for (2.10)): Lemma 6.1, Lemma 6.6 (the exponents (6.17), the quadratic
character (6.18), the normalisation, the local identity at j_p = 4 and the three-term reindexing, the update
table and (6.16), the large sieve step (6.20), the dyadic and geometric sums) and the proof of Proposition 5.2
checked line by line; all correct as printed. Section 6 rests on three things it does not prove in place:
Patterson's formula (2.10), the theta transformation (Proposition 6.2, Lemmas 6.3 and 6.4, proved in Appendix
A.2, from line 1650 of paper_c.txt) and the Goldmakher-Louvel quadratic large sieve (reference [13]). Next:
Section 7 (Proposition 5.4, from line 1299, PDF from page 29), then Appendix A.

## 12 Nov 06:12 - Section 7 checked
Section 7 (pages 29 to 34): Lemma 7.1 (first Poisson summation; prefactor w_{C,d}, frequency range, the bound
N(y) <= Y_{C,d}), the paired identity (7.3) and its converse (derived by hand from (4.1), (4.3), (4.4), (4.7) and
the Chinese remainder theorem), Lemma 7.2 (second Poisson summation) and Lemma 7.3 (the regrouping
r = tg/e, f' = Cew, k' = deh; the count of preimages that leaves f' | k'; the dyadic parameters against (5.12))
checked line by line; all correct as printed. Sections 4 to 7 and Appendix B are now checked. Left: Appendix A
(A.1 from line 1552 of paper_c.txt, the proof of Lemma 4.1; A.2 from line 1650, the theta transformation, PDF
from page 34), Patterson's formula (2.10) against its source, the Goldmakher-Louvel large sieve against its
source, and a line-by-line pass of Sections 2 and 3 (mean square to zero-free half-plane).

## 12 Nov 06:19 - Appendix A.1 checked
Appendix A.1 (pages 35 to 37), the proof of Lemma 4.1: the Jacobi-sum argument for (4.2) (the count for
4x(1 - x), Gauss-Jacobi, J(chi_p^2, chi_p^2) = -p by the power-sum congruence and the unit mod 3), (4.6), the
quadratic Gauss sum and the bicharacter R for (4.1), (4.7) and (4.3) to (4.5) checked by hand; all correct as
printed. The Poisson limiting argument for (A.1) was not reworked; (A.1) and its closed form were tested by
computer instead (nt01_checkA1.py, 564 of 564 values of c; J = -p on 118 of 118 primes). Sections 4 to 7 and
Appendices A.1 and B are now checked. Left: Appendix A.2 (from line 1650 of paper_c.txt, PDF from page 37: the
theta transformation, Proposition 6.2, Lemmas 6.3 and 6.4), Patterson's formula (2.10) against its source, the
Goldmakher-Louvel large sieve against its source, and a line-by-line pass of Sections 2 and 3.

## 12 Nov 06:29 - Appendix A.2 checked
Appendix A.2 (pages 37 to 44), the cubic theta transformation with fixed ray class twists (proofs of Proposition
6.2 and Lemmas 6.3 and 6.4): the finite Fourier expansion (A.3) to (A.5), the reduced denominators, the matrices
g, H, g_1, (A.8) to (A.12), the Mellin transform (A.13) to (A.19), the scalar 1/81, the contour shifts and (A.20)
checked by hand, first from the text and then against the pages; all correct as printed, and the output agrees
with (6.5), (6.6), (6.9). Lemma B.1 (page 44) read, correct. Read and not reworked: the Phragmen-Lindelof step.
Sections 4 to 7 and Appendices A and B are now checked. Left: the cited results against their sources
(Patterson's formula (2.10) and cusp expansions, Kubota's automorphy law as used by Dunn-Radziwill, the
Goldmakher-Louvel large sieve) and a line-by-line pass of Sections 2 and 3.

## 12 Nov 06:37 - Section 3 and the cited results
Section 3 (pages 11, 12) reworked by hand: Proposition 3.1 implies Theorem 1.1, correct as printed. The cited
results compared with their sources: (2.10) against Dunn-Radziwill arXiv 2109.07463 (5.6), (5.7) (agrees; the
preprint's e(z) is their e-breve(z/lambda), which gives the factor chi_n(lambda)^2); Kubota's character (5.4),
the cosets gamma_10, gamma_19 and the table on their page 78 against (A.6), (A.8) (agree); Lemma 6.5 against
Goldmakher-Louvel arXiv 1112.1642 Definition 1 and Theorem 1.1 (hypotheses match). So every step the 49-page
paper proves itself is checked with no error found, and its cited results are used as stated. Not done: the
proofs of the cited results, Patterson 1977 itself, the Poisson limit for (A.1) (tested only), the
Phragmen-Lindelof step, the 199-page preprint of 30 Sep, and any second independent audit. The claim stays
unconfirmed here. Scratch notes: fillq_ctl/nt01_src_note.txt.

## 12 Nov 06:46 - the follow-up papers
All five build on the 199-page preprint of 30 Sep (the 7/8 half-plane), not on the 49-page one of 5 Oct (11/12):
- Liu 2610.12234 (8 Oct): varies the parameters b, l, kappa of the 7/8 argument, gets 0.874957...; same strategy, same inputs.
- Xu-Sang 2610.15291 (11 Oct): "assuming the analytic inputs of that work", 0.8748867 by an amplified first moment.
- Liu 2610.26835 (19 Oct): extends to cyclotomic fields containing mu_12 and by class-field descent to abelian fields; boundary 0.874886647...
- Frei-Sofos-Widmer 2610.18491 (13 Oct): applications (effective Chebotarev, l-torsion in class groups) "drawing on recent breakthroughs of OpenAI and Cureton-Thorner".
- Visser 2610.20058 (14 Oct): consequences "if true" (primes between eighth powers); says there are good reasons to be cautious.
None of the five is an independent verification of the analytic inputs. The Cureton-Thorner paper was not found by an arXiv author search (one try); not pursued.
Consequence for our record: the 49-page paper checked in NT01_CHECK.md is the shorter, weaker argument (11/12 > 7/8); the literature rests on the 199-page one, which is unread here. Our pass says nothing about 7/8.
