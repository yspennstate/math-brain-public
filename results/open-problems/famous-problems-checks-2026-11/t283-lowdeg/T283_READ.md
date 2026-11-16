# Row T283 (the low-degree conjecture): what arXiv 2607.20318 proves and what is left

Read on 12 Nov 2026 from the text of arXiv 2607.20318v2 (S. Mao, "The Polynomial-Time Low-Degree Conjecture is
False", 28 Oct 2026): abstract, Section 1 to Theorem 1.2, Section 3.1, Lemma 3.5, Section 4. The proofs of
Lemmas 2.4, 3.3 and 3.4 were not checked. One preprint, not refereed as far as its arXiv record shows.

## The statement refuted

Conjecture 1.1 there (the graph-valued, polynomial-time form of Hopkins's Conjecture 2.2.4): Q_n uniform on graphs
on n vertices, P_n invariant under relabelling the vertices, and Adv_{<= D_n}(P_n, Q_n) = O(1) for some
D_n >= (log n)^{1+c}. Then for every fixed resampling rate eps in (0, 1) no polynomial-time test strongly
distinguishes T_eps P_n from Q_n.

## Theorem 1.2

For every fixed r >= 3 there are c_r > 0, eps_r in (0, 1) and vertex-relabelling-invariant P_n with:
1. every marginal of P_n on at most D_n = c_r (log_2 n)^{r-1} edges is exactly uniform (advantage 0 to degree D_n);
2. one deterministic O(n^2) algorithm (a rank test over F_2 on a monomial lift of the edges from sqrt(n) vertices
   to about a log n anchor vertices) strongly distinguishes T_eps P_n from Q_n for every fixed eps in [0, eps_r];
3. P_n is sampled exactly in expected polynomial time by a nonuniform algorithm with O(n log n + (log n)^{2r}) bits
   of advice.
Construction: a subspace of a Reed-Muller code whose nonzero polynomials have small bias, evaluation points with no
short linear dependencies, a uniformly random alternating bilinear form evaluated on pairs of the evaluation
vectors, then a uniform relabelling. Extensions stated in Section 4: symmetric tensors of any fixed order, and a
product Gaussian null with Ornstein-Uhlenbeck noise.

## What the theorem does not cover (each read off the paper)

- Noise. The distinguisher is proved only for eps <= eps_r. In Lemma 3.5 the constants satisfy a > 2 and
  a (-log_2(1 - eps_0)) < 1/4, so eps_r < 1 - 2^{-1/8} = 0.083 whatever r is. The conjecture quantifies over every
  eps, so it is refuted; the weaker statement "for every fixed eps above some eps* < 1 no polynomial-time test
  strongly distinguishes" is not touched by this paper, nor by arXiv 2505.17360, whose distinguishers are also
  stated for sufficiently small fixed noise.
- Uniform samplability. The sampler needs advice; the paper says that finding a good seed in polynomial time, and so
  a uniformly polynomial-time samplable example, "remains open" (Section 4, Explicitness).
- A repaired conjecture. Section 4: a repaired conjecture "should exclude such structure when it remains
  efficiently detectable after resampling. Finding natural assumptions that do so remains an open problem."
- Degree. Advantage is zero only to degree polylog(n); arXiv 2505.17360 reaches degree n^{Omega(1)} with a
  quasi-polynomial distinguisher. No example is known with polynomial degree and a polynomial-time test.

## Positive side quoted in the paper

Under invariance under all permutations of the coordinates (not only vertex relabellings), vanishing low-degree
advantage against the uniform null to high enough degree implies statistical indistinguishability after fixed
noise: Hsieh, Kane, Kothari, Li, Mohanty, Tiegel, "Rigorous implications of the low-degree heuristic", STOC 2026
(cited as [HKK+26]; not read here).

## Search

arXiv API, phrase "low-degree conjecture", newest first, 12 Nov 2026 (lit/search/s1.xml, 15 entries): nothing after
2607.20318 that restates or repairs the conjecture; the newest entry (2610.41995, 30 Oct 2026) is on graph
combinatorial testing gaps. The phrase search does not find papers that avoid the phrase ([HKK+26] is not in it),
so this is a lower bound on what exists.

## Proposal for the row

The row as written ("the low-degree conjecture") is reported false in its quasi-polynomial form (2505.17360, FOCS
2025) and its polynomial-time form (2607.20318). If it stays on the list it should be one of the questions the two
papers leave open, stated exactly:
(a) the large-noise form: is there eps* < 1 such that, under the hypotheses of Conjecture 1.1, no polynomial-time
    test strongly distinguishes T_eps P_n from Q_n for eps >= eps*; or does a counterexample exist at every fixed
    eps < 1;
(b) a uniformly samplable counterexample;
(c) a natural extra hypothesis under which the conjecture holds.
Our earlier card on the family of 2505.17360 (its guess size never reaches polynomial time for product nulls)
stays correct and is now beside the point for the polynomial-time question, which 2607.20318 settles by a different
family.

## How far the rank test can go in the noise (12 Nov, 00:38; my reading of Section 3, not in the paper, not audited)

The test takes T anchors and N0 other vertices, lifts each column y_j in F_2^T by the monomials of degree at most
s (R0 = binom(T, <= s) of them) and declares "planted" when the N0 lifted columns are dependent. Lemma 3.4 finds
the dependence among the clean columns only, those none of whose T anchor edges was resampled; their number has
mean mu = N0 (1 - eps)^T.

1. This argument (a dependence among clean columns) needs eps < 1/2. Under the null the lifted columns must be independent, so N0 <= R0 <=
   2^T, that is T >= log_2 N0. Then mu = N0 (1 - eps)^T <= N0^{1 - lam} with lam = -log_2(1 - eps), and mu -> infinity
   forces lam < 1.
2. With the paper's choices the bound is smaller. N0 = sqrt(n) and distinct columns under the null by a union bound
   need T = a log_2 n with a > 2, so mu = n^{1/2 - a lam} needs lam < 1/4, eps < 0.159; Lemma 3.5 asks
   a lam < 1/4 to leave room for the Reed-Muller dimension n^{b h_2(r sigma/b)}, which gives eps < 0.083.
3. So a counterexample at every fixed eps < 1, or even at eps >= 1/2, needs a test that uses columns with resampled
   entries. One structural fact that such a test could start from: before noise the adjacency matrix is
   Phi B Phi^t over F_2 with Phi of size n x K, K = dim W = Theta((log n)^r), so its rank over F_2 is at most K,
   against n - O(1) for G(n, 1/2). After noise this is a planted low-rank matrix over F_2 with random errors, a
   problem of the learning-parity-with-noise kind in dimension K. I know of no polynomial-time test for it when
   K = (log n)^r with r >= 3: a k x k minor with k > K is free of resampled entries with probability
   (1 - eps)^{k^2} = exp(-Theta((log n)^{2r})), so the plain rank of a minor does not work. This is a statement
   about what I found, not a hardness result. Whether the extra Reed-Muller structure of the row space allows a polynomial-time
   test at large noise is the open point of form (a).
