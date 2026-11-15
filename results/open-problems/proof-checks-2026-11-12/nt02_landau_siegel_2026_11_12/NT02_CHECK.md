# Row NT02: non-existence of Landau-Siegel zeros

Checked 12 Nov 2026. Verdict: the row is reported solved and the report holds up under a full reading of two
proofs. It should leave the list of problems to attack.

## The statement

There is an absolute constant c > 0 such that for every primitive real Dirichlet character chi modulo q >= 3 and
every real zero beta of L(s, chi),

    (1 - beta) log q >= c.

## Sources

- OpenAI, "Uniform exclusion of Landau-Siegel zeros", 1 Oct 2026, 9 pages (repository openai/math, folder
  `preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026`, file `paper.pdf`). Read in full.
- B. Kerr, arXiv 2610.21099, 6 pages: a shorter variant by an auxiliary polynomial. Read in full.
- W. Banks, arXiv 2610.15483, 19 pages: a detailed account with explicit constants. Statement, Remark 7.2 and the
  closing sections read.
- Guo, arXiv 2610.30476, 17 pages: an elementary proof with c = 1/100 for all q >= 3. Opening and references read.
- Not read: Kimura, arXiv 2610.21511; Banks, arXiv 2610.31402; Tao's note of 19 Oct 2026 and the notes of Green and
  van Dijk that Guo cites; Masser's 1981 zero estimate, which Kerr quotes.

## The argument

Let d be the fundamental discriminant of chi, K = Q(a, b) with a^2 = d, b^2 = 2, R = Z[a, b], sigma: a -> -a,
tau: b -> -b. For n in {0, ..., N-1}^4 put theta_n = n_1 + n_2 a + n_3 b + n_4 ab; there are M = N^4 such points,
and each is sent to the triple (theta_n, sigma theta_n, sigma tau theta_n) in C^3.

1. (Lemma 2) A zero with delta = (1 - beta) log q small makes the primes with chi(p) = 1 scarce:
   sum over p <= X with chi(p) = 1 of (log p)/p is at most C log q + C delta (log X)^2 / log q. So the primes with
   chi(p) = -1 carry almost all of sum (log p)/p up to X = q^A.
2. (Lemma 3, Corollary 4) The monomials x^alpha with alpha_1 <= T_1, alpha_2, alpha_3 <= T_2, where
   T_1 = 32 H^(2/3) U, T_2 = 32 H^(-1/3) U, U = N^(4/3), already separate the M points: evaluation is onto.
3. Order the monomials by the weight alpha_1 + H (alpha_2 + alpha_3) and retain a row whenever it enlarges the span.
   The M retained rows give a determinant Delta in R, nonzero by construction. With S_1 = sum of alpha_1 and
   S_2 = sum of alpha_2 + alpha_3 over the retained rows, S_2 / S_1 <= C / H (Lemma 6).
4. (Upper bound) Hadamard gives (1/4) log |Norm Delta| <= (M/2) log M + (S_1 + S_2)(log N + (1/2) log q + log 8).
5. (Lemma 7, lower bound) For a prime p > H not dividing 2q with chi(p) = -1 the Frobenius is sigma or sigma tau, so
   theta^p = g(theta) mod pR with g one of the two other coordinates. Writing alpha_1 = pk + r and replacing
   theta^(alpha_1) by theta^r (theta^p - g theta)^k changes the row only by earlier rows of smaller weight, which
   lie in the span of earlier retained rows. The determinant is unchanged and the row is divisible by p^k. Hence
   p^(4 E_p) divides Norm Delta, E_p = sum of floor(alpha_1 / p).
6. Summing over those primes, step 1 turns the lower bound into S_1 (log U - C log q - small) - C M U, with
   log U = (4/3) log N. Against the upper bound S_1 log N (1 + C/H) + ..., taking N = q^gamma with gamma large and
   H large, the two sides are 1 and 13/16 + 1/16 times S_1 log U. That is a contradiction once delta is small.

## What was checked by hand

Every step of the nine pages, with the computations redone rather than read:

- the kernel of n -> (theta_n, sigma theta_n, sigma tau theta_n), spanned by (ab, b, -a, -1), and the Q-independence
  used at the end of Lemma 3;
- Lemma 2 from the zero, including the (log X)^2 term;
- Lemma 3 line by line: the annihilating vector v, P the convex hull of its support, the polynomial R of degrees
  t_j - 3(N-1) vanishing on the image of 4P (the count (4N-3)^4 < product of (b_j + 1)), the nearest lattice point
  m with R(Am) nonzero, the face G, the vertex u from Caratheodory with y - u in 3P, vanishing of R at
  A(m + n - u) for n outside G, and the Lagrange factor of degree at most 3(N-1) that isolates u;
- Corollary 4 and Lemma 6, including the counting bound S_1 >= c M H^(2/3) U;
- the Hadamard bound, with |theta| <= 8 N sqrt(q) in every embedding;
- Lemma 7: the congruence for both Frobenius classes, the weight drop m(p - H) of the extra rows, the unitriangular
  change of rows, and the exponent 4 E_p in the norm;
- the closing arithmetic 1 against 13/16 + 1/16.

No error was found. Kerr's variant was checked the same way (weights i + 8(j + k) <= D, the basis
x_1^v (x_1^p - x_l)^e x_2^j x_3^k, the residue count, the pigeonhole step with r = D^3/384, W = 5 D^4 / 6144,
E_p = D^4 / (1536 p), ratio 5/4); it holds, granted the zero estimate it quotes from Masser.

Two remarks that make the result easier to believe.

The method does not prove too much. The replacement in step 5 works for any prime whose Frobenius moves theta to
one of the three coordinates, that is for three of the four classes. In a field where Frobenius is equidistributed
those primes have density 3/4, and (3/4) log U = (3/4)(4/3) log N = log N: the lower bound then equals the size of
the determinant to leading order and nothing is contradicted. A contradiction needs the usable primes to have
density above 3/4, which is what a zero near 1 supplies. For k of n conjugates the same count gives density k/n
against exponent n/k, balanced in the same way.

The second square root is needed. With Q(sqrt d) alone the lattice has rank 2 in 2 variables and there is no gain;
adjoining sqrt 2 gives rank 4 in 3 variables, U = N^(4/3), and keeps both usable classes nontrivial on Q(sqrt d).

## Computer tests

`nt02_check.py`, output `nt02_check.out`; `nt02_check2.py`, output `nt02_check2.out`. Exact arithmetic modulo
primes that split completely in K, and the Chinese remainder theorem for the integer Norm Delta.

- Retained rows (15 cases, d in {13, -7, 5}, N from 2 to 6, H from 1 to 4). The retained set is the same modulo two
  different primes in all 15 cases. Largest weight over H^(2/3) U between 1.25 and 1.89 (the paper allows 96);
  largest alpha_1 at most 0.059 T_1; H S_2 / S_1 between 0.89 and 1.77, so S_2 / S_1 <= C / H with C below 2.
- Interpolation. The smallest cube of degrees (t, t, t) on which evaluation is onto is t = 2, 4, 6, 8 for
  N = 2, 3, 4, 5, equal to the counting bound each time. Lemma 3 asks for 11, 24, 39, 55; it is far from sharp at
  these sizes and true.
- Divisibility. Norm Delta was computed exactly for five cases with N = 3 (M = 81; 247 to 310 primes of 30 bits,
  3221 to 4405 bits, an independent check prime agreeing each time). For the primes 3 to 13 covered by Lemma 7:
  15 cases, 0 failures, 11 of them with E_p > 0. The inequality is close to sharp in places: d = -7, p = 5 has
  valuation 88 against 4 E_p = 84; d = 5, p = 7 has 36 against 32; d = 13, H = 2, p = 5 has 92 against 84.
- Control. For d = 13 the prime 3 has Frobenius tau, which the lemma does not cover (chi(3) = 1). There the
  valuation is 188 against 4 E_3 = 220 for H = 2, and 188 against 344 for H = 3: the divisibility fails where the
  lemma does not claim it. (For H = 1 the valuation is 204 against 128, so that case separates nothing.)
- Size. (1/4) log |Norm Delta| lies between the sum of E_p log p and the Hadamard bound in all five cases
  (for example 623.8 between 21.6 and 1819.4). At N = 3 both bounds are loose; this confirms the order only.
- Zero estimate. The largest D such that no nonzero polynomial of total degree at most D vanishes on all N^4
  points is 2, 5, 8, 12, 17 for N = 2, ..., 6, against 2, 5, 9, 13, 17 from counting monomials. A vanishing
  polynomial therefore has degree at least 3, 6, 9, 13, 18, which grows like N^(4/3) as Masser's estimate says.

The divisibility test at N = 4 (M = 256), run afterwards on one core of a Mac mini in 50 minutes
(mini1/nt02_check_n4.py, mini1/nt02_check_n4.out). Four cases: d = 13 with H = 2 and H = 1, d = -7 with H = 2,
d = 5 with H = 3. Norm Delta is nonzero each time and has 20,191 to 22,164 bits (1,395 to 1,516 primes of 30
bits, the check prime agreeing each time).

- Lemma 7, primes 5 to 17 in the classes it covers: 12 cases, 0 failures. With the five cases at N = 3 that
  makes 27 cases and no failure. The inequality is attained twice: d = -7, p = 13 has valuation 32 against
  4 E_p = 32, and d = 5, p = 13 has 120 against 120. Near misses: d = 5, p = 17 has 40 against 36 and
  d = 5, p = 7 has 508 against 500.
- Control (Frobenius class tau, not covered): the valuation falls short of 4 E_p in four of five instances
  (d = 13, H = 2, p = 3: 1176 against 1192; d = -7, p = 11: 4 against 80; d = 5, p = 11: 4 against 200;
  d = 5, p = 19: 0 against 12) and exceeds it in one (d = 13, H = 1, p = 3: 1284 against 716).
- Size: (1/4) log |Norm Delta| is 3499 to 3841, between the sum of E_p log p (170 to 572) and the bound (5.1)
  (9532 to 10378) in all four cases.

## Formalization

`lean/formalization.yaml` of openai/math lists the theorem as formalized: declaration
`OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap` in
`lean/OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean`, with a comparator configuration that permits only the
axioms propext, Classical.choice and Quot.sound. The statement reads: there is c > 0 such that for all q >= 3, all
primitive nontrivial real-valued chi modulo q and all beta in (0, 1) with L(beta, chi) = 0, c <= (1 - beta) log q.
It is the theorem above. The statement was read; the development was not compiled here.

## Reception

In the six weeks after 1 Oct 2026 five papers build on the theorem and none found in three searches disputes it
(`lit/search/s1.xml`, `s2.xml`, `s3.xml`). Banks gives explicit constants ((1 - beta) log q >= 0.003 for
q >= 10^10) and writes that every line has been verified by the author, while asking for independent scrutiny; his
range of small conductors rests on a computation of Lu, Zaman and Zhao that he did not verify. Kerr gives the
auxiliary-polynomial variant. Guo gives an elementary route with c = 1/100. Kimura and Banks (2610.31402) treat
consequences: class numbers of imaginary quadratic fields, a version over a base field and an effective
Brauer-Siegel theorem. Several of these papers acknowledge the help of language models in their preparation.

## For the list

- Take NT02 off the problems to attack. Mark it solved (OpenAI 2026; variants by Kerr, Banks, Guo). Check level:
  full reading of the original and of Kerr's variant by one reader, a computer test of the two central lemmas, a
  listed formalization whose statement matches.
- Still open next to it: the best constant c; the explicit range of small conductors without a machine
  computation; how far the method reaches for zeros of other L-functions, where the balance count above is the
  obstacle to watch.
- Rows that assume a possible Siegel zero, or that are stated "conditionally on no Siegel zeros", change status:
  effective lower bounds for class numbers of imaginary quadratic fields and effective Brauer-Siegel for quadratic
  fields follow.
- Row NT01 should be checked against two preprints in the same repository,
  `The-Quasi-Riemann-Hypothesis-September-30-2026` and `...-October-5-2026`, which claim a zero-free half-plane
  Re s > 7/8. Unread.
