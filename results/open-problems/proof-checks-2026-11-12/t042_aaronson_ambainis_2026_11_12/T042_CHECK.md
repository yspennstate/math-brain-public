# Row T042 (the Aaronson-Ambainis conjecture): the short proof read and checked

12 Nov 2026. Source read in full: arXiv 2611.12795v1 (T. Huffstutler, D. Miloschewsky, S. Podder, 9 Nov 2026,
"A short proof of the Aaronson-Ambainis Conjecture via the completion framework"). Of arXiv 2611.11626 (Blanc,
Docter, Strassle, Tan, an exposition of the first proof) only the abstract and the table of contents were read.
The first proof, arXiv 2611.09773 (D. Turturean, 6 Nov 2026, about 60 pages), was not read.

## The statements

Conjecture 7.1 of Aaronson and Ambainis (2014). A partial Boolean function f defined on a delta fraction of
{0,1}^n, with quantum query complexity Q(f), is computed correctly on a 1 - epsilon fraction of its domain by a
deterministic algorithm making poly(Q(f), 1/epsilon, 1/delta) queries.

Conjecture 1.7 of the same paper. A polynomial p of degree d with 0 <= p <= 1 on the cube and variance v has a
coordinate of influence at least poly(v/d).

The short paper proves both: D(F) = O(CAdv(f)^3 / (epsilon delta)^2) for a total F agreeing with f on a
1 - epsilon fraction of the domain (Theorem 2), hence O(Q(f)^6 / (epsilon delta)^2) queries; and
max_i I_i(p) = Omega(v^12 / d^12) (Theorem 7).

## What was checked by hand

Every step of the paper except the two quoted results listed below.

1. Lemma 3. From a feasible family lambda^x of the classical-adversary programme with cost A, put
   d_a(z) = sum of lambda^a_i over the coordinates where z differs from a, g(z) = min(1, min over 1-inputs a of
   d_a(z)) and G_t = 1[g < t]. For 1/4 <= t <= 3/4 the vector 4 lambda^x is a fractional certificate of G_t at
   every x of the domain, and averaging the total influence over t gives a threshold with I(G_t) <= 4A.
2. Lemma 4. If U_b, a set of b-inputs of a total G of density delta_b, has fractional certificates of cost at
   most gamma_b, then some coordinate has I_i(G) >= delta_0 delta_1 / (gamma_0 gamma_1). The proof marks pairs
   through the sets H_y, proves inequality (4), N_C <= sum_i w_i b_i on every subcube, and concludes by the
   determinant argument on the least-degree monomials. The statement restricts to subcubes with densities
   measured inside the subcube.
3. Theorem 2. Query a free coordinate of largest influence in G restricted to the current subcube C until
   m(C) = min(delta_0(C), delta_1(C)) is 0. Restricted certificates stay valid, so Lemma 4 on C gives
   I_i(G|C) >= delta_0 delta_1 / (16 CAdv^2) >= m(C)^2 / (16 CAdv^2), which is inequality (7). Identity (8),
   I(G|C) - (I(G|C_0) + I(G|C_1))/2 = I_i(G|C), makes the total influence a potential. e_t = E[m(C_t)] does
   not increase (concavity of min), so s e_s^2 <= sum_t E[m(C_t)^2] <= 16 CAdv^2 I(G) = O(CAdv^3). At a depth
   s of order CAdv^3 / (epsilon delta)^2 this gives e_s <= epsilon delta; answering the majority value of f on
   each leaf then errs on at most an epsilon fraction of the domain, so D(F) = O(CAdv^3 / (epsilon delta)^2).
4. Appendix A. Lemma 6 follows from the O'Donnell-Saks-Schramm-Servedio inequality with the factor 1/2.
   Theorem 7: with delta >= 3v/4 and epsilon = v/(16 delta) the tree has depth D = O(d^6 / v^5), Cov(p, h) >= 3v/8,
   and max_i I_i(p) >= 9 v^2 / (16 D^2) = Omega(v^12 / d^12).

No step fails.

Quoted and not verified here: CAdv(f) = O(Q(f)^2) and the error-dependent bound CAdv <= 4 pi^2 d^2 / v used in
the appendix (Anshu, Ben-David, Kundu, CCC 2021, with its Theorem 8); the OSSS inequality itself.

## The computer checks

`t042_check.py`, output `t042_check.out`; written from the statements, exact enumeration of the cube, fractional
certificates and the classical-adversary bound by linear programming.

- Part A, Lemma 4 as stated. All 268 nonconstant functions on 2 and 3 bits, named functions (AND, OR, parity,
  majority, dictator, threshold-2, tribes, address) on 3 to 7 bits, and 1500, 300 and 60 random functions on 4, 5
  and 6 bits: 8710 threshold pairs, the lemma never fails. The smallest value of
  max_i I_i gamma_0 gamma_1 / (delta_0 delta_1) is 4.0000 (n = 2, G = 1100, gamma_0 = gamma_1 = 1).
- Part B, inequality (4): 213351 subcubes, 114136 of them with N_C > 0; never fails, and it is attained with
  equality (smallest slack 0.0000).
- Part C, the determinant argument for all 254 nonconstant functions on 3 bits: 3980 determinants, none zero;
  3990 least-degree monomials, each with exponents beta_i <= b_i and weight at least N_C.
- Part D, Lemma 3 on 340 random partial functions on 3 to 5 bits: the largest value of min_t I(G_t) / CAdv(f) is
  1.0000 against the bound 4.

`t042_check2.py`, output `t042_check2.out`.

- Part E, the query procedure of Theorem 2 on 185 random partial functions on 3 to 6 bits, 960 subcubes queried:
  Lemma 4 holds on every subcube, identity (8) holds exactly, e_t never increases, and sum_t E[m(C_t)^2] is at
  most 0.0052 of 16 CAdv^2 I(G); the deepest tree has depth 6. The Lemma 4 test in this part is weak: with the
  certificates 4 lambda the smallest ratio seen is 64, so the constant 16 is far from tight on these sizes.
- Part F, Lemma 6 on 7500 random pairs (decision tree, p) on 3 to 7 bits: the largest value of
  |Cov(p, h)| / ((1/2) sum_i q_i E|p - p^i|) is 0.9612.

Both scripts end with "all assertions passed".

Limits of the computer checks. They cover up to 7 bits; they test the lemmas and the bookkeeping of the proof,
not the asymptotic statement. The exponents (6 in Q, 12 in v/d) were followed by hand only.

## Literature (12 Nov 2026, `lit/search/s1.xml`, `s2.xml`)

Two dated arXiv searches found no correction or objection to either proof. Related: arXiv 2611.09773
(Turturean, first proof), 2611.11626 (exposition; its authors state that the proof was found by D. Turturean
with a research system of Physical Superintelligence built on a non-public Anthropic model), 2609.35327 (Girish,
Mittal, Nehoran, Raz, distributional variants), 2609.05201 (Escudero Gutierrez), 2608.04411v4 (Slote, Volberg,
Zhang), 2402.13952 (Bhattacharya, random restrictions).

## Verdict for the list

The conjecture is proved in both forms. The short proof checks by hand and by computer, given the two quoted
results. The row should leave the open list. What remains open nearby, not vetted here: the comparison with
the Lovett-Zhang conjecture discussed in Section 2.2.3 of arXiv 2611.11626, and the optimal exponents.
