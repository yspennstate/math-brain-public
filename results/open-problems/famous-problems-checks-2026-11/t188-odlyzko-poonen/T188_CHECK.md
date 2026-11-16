# Row T188 (the Odlyzko-Poonen conjecture): the proof read and its elementary core checked

12 Nov 2026. Source read in full: arXiv 2609.26771v2 (C. Kogler, 14 Oct 2026, "The Odlyzko-Poonen Conjecture on
Irreducibility of Random Polynomials", 11 pages). The paper credits the proofs to GPT-6 Astra and comes with a
Lean formalization of about 22,000 lines (github.com/ckkogler/odlyzko-poonen-lean); the Lean code was not
inspected here.

## The statement

P_n is a uniformly random polynomial of degree n with coefficients in {0, 1} and constant term 1. Odlyzko and
Poonen (1993) conjectured that P_n is irreducible over Q with probability tending to 1. Konyagin (1999) had
the lower bound c / log n; Breuillard and Varju (2019) proved the conjecture under the Riemann hypothesis for
Dedekind zeta functions.

Theorem 1.1: P(P_n reducible) = sqrt(2 / (pi n)) + O(1/n), with no hypothesis.
Theorem 1.2: with probability at least 1 - C exp(-c n / (log n)^4), P_n = Phi I with Phi a product of cyclotomic
polynomials and I irreducible and noncyclotomic.
Theorem 1.3: the probability that P_n has a non-trivial twin, a Q in P_n other than P_n and P_n* with
Q Q* = P_n P_n*, is at most 8 (3/4)^floor((n-1)/4).

## What was checked by hand

1. Lemma 3.1 (the twin factorization, after Ljunggren and Filaseta). If P = A B with A, B monic, then Q = A B*
   has Q Q* = P P*, and Q is P or P* only if A or B is reciprocal. So a reducible P either has a reciprocal
   factor or a non-trivial twin.
2. Proposition 2.1 and Theorem 1.3. Work over F_2 with a in B_d, b in B_e, P and Q the lifts of a b and a b*.
   The coefficients of P P* - Q Q* are even; D_k is half the k-th coefficient modulo 2. Sample b through
   c = b + b*: then D_k depends only on b_1..b_k, and flipping b_k changes D_k by lambda_k = [(a + a*) c]_k. The
   map c -> lambda is triangular, so each index after the first j with a_j != a_(d-j) contributes a factor
   3/4, and summing over j gives P(a != a*, P P* = Q Q* mod 4) <= 2 (3/4)^m, m = floor((e-1)/2). Theorem 1.3 follows by taking the gcd over F_2, with the bound 8 (3/4)^floor((n-1)/4).
   Corollary 2.2 likewise.
3. Lemma 3.3 (Dobrowolski's bound in the form of Breuillard-Varju, Lemma 26), Proposition 3.2 (a monic
   reciprocal divisor that is not a product of cyclotomic polynomials has probability at most
   C exp(-c n / (log n)^4)), and the proof of Theorem 1.1, which takes the cyclotomic estimates from
   Breuillard-Varju (Lemma 45 and Section 9.2) and ends with P(P_n(-1) = 0) = sqrt(2/(pi n)) + O(n^(-3/2)).
4. Lemma 3.5. The monic gcd of the reductions of P_n and P_n* modulo 2 is reciprocal with constant term 1;
   there are 2^floor(h/2) such polynomials of degree h, each divides P_n mod 2 with probability at most 2^(1-h),
   and the sum over h >= L is at most 6 * 2^(-L/2) (the lemma states 8 * 2^(-L/2)).
5. Proof of Theorem 1.2. Outside the two exceptional events, a factorization I = A B of the noncyclotomic part
   would make neither A nor Phi B reciprocal, and Lemma 3.1 would give a non-trivial twin. Lemma 3.5 with L = n
   and L = floor(n^alpha) + 1 gives the two assertions.

No step fails.

Quoted and not verified here: Dobrowolski's theorem, Lemmas 26 and 45 and Section 9.2 of Breuillard-Varju. The
Lean formalization was not built or read.

## The computer checks

`t188_check.py`, output `t188_check.out`; `t188_check2.py`, output `t188_check2.out`. Both end with "all
assertions passed".

- Theorem 1.3 by enumeration, n = 2..20. No P in P_n has a non-trivial twin modulo 4 for n <= 10. For
  n = 11..20 the counts are 8, 24, 48, 64, 148, 220, 424, 640, 1152, 1700 out of 2^(n-1), a fraction falling
  from 0.0117 to 0.0032. Exact twins have the same counts except at n = 20 (1696). The stated bound is above 1
  for every n <= 20, so at these sizes the enumeration tests the decay and not the constant.
- Proposition 2.1 and the steps of its proof for all 1 <= d <= e <= 10, 698027 pairs (a, b): the coefficients
  of P P* - Q Q* are always even, the conditional bound (3/4)^(m-j) and the proposition hold for every (d, e)
  (largest probability over bound 0.1875), and the flip rule for D_k holds in all 127476 cases tried.
- Lemma 3.1 for every reducible P with n <= 11: every twin A B* is again in P_n (1768 twins at n = 11).
- Formula (1.1) and Remark 3.4. The reducible fraction for n = 10..15 is 181/512, 410/1024, 631/2048,
  1458/4096, 2684/8192, 5510/16384. Then n (fraction - sqrt(2/(pi n))) is 1.01, 1.76, 0.93, 1.75, 1.60, 1.95,
  against the next two terms of Remark 3.4, B + A (delta_n - 2B) / sqrt(n) with A = sqrt(2/pi),
  B = 4 (1 + sqrt 3) / pi, delta_n = -17/4 (n even), 1/4 (n odd): 0.65, 1.86, 0.90, 1.99, 1.09, 2.10. The
  parity pattern and the size agree; the remaining gap is of the order 1/n the remark allows.
- Lemma 3.5 for every n <= 18 and every L: the fraction of P with deg gcd(P, P*) >= L over F_2 never exceeds the
  sum in the proof, and equals it in some cases; it is at most a quarter of the stated 8 * 2^(-L/2). The count
  2^floor(h/2) of reciprocal polynomials was confirmed for h <= 12.

## Literature (12 Nov 2026, `lit/search/s1.xml`, `s2.xml`)

Two dated arXiv searches (the conjecture by name; random polynomials, irreducible, coefficients) return no
correction, comment or competing claim after 2609.26771. The acknowledgements thank Breuillard, Varju and
Filaseta for checking the argument.

## Verdict for the list

The conjecture is proved. The elementary core (twin factorizations are rare) checks by hand and by computer;
the cyclotomic and Mahler-measure inputs are published results of Breuillard-Varju and Dobrowolski. The row
should leave the open list. Open nearby and candidates for the slot, not vetted here: the Galois group of
P_n (that it contains A_n is known under the Riemann hypothesis, Breuillard-Varju), and irreducibility for
0-1 polynomials with few terms.
