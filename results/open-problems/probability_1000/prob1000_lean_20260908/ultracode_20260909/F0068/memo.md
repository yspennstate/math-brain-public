# F0068 - Janson, Problem 20.8 (width of subcritical simply generated trees)

Status: literature_resolved. The problem was answered, in the affirmative, by
Addario-Berry, Brandenberger, Hamdan and Kerriou, "Universal height and width
bounds for random trees", Electron. J. Probab. 27 (2022), paper 118,
doi 10.1214/22-EJP842, arXiv 2105.03195 (v1 May 2021, v2 April 2022).
The companion height problem (Problem 20.7) was answered by Addario-Berry and
Donderwinkel, "Random trees have height O(sqrt n)", Ann. Probab. 52 (2024),
doi 10.1214/24-AOP1694, arXiv 2201.11773.

## The problem as the source states it

Janson, "Simply generated trees, conditioned Galton-Watson trees, random
allocations and condensation", arXiv 1112.0510 (Probab. Surveys 9, 2012),
Section 20.3, PDF page 136:

> Conjecture 20.5. If nu = 1 and sigma^2 = infinity, then H(T_n)/sqrt n ->_p 0.
> Conjecture 20.6. If nu = 1 and sigma^2 = infinity, then W(T_n)/sqrt n ->_p infinity.
> Problem 20.7. Does nu < 1 imply that H(T_n)/sqrt n ->_p 0?
> Problem 20.8. Does nu < 1 imply that W(T_n)/sqrt n ->_p infinity?

with, from the same page, "the height H(T) := max{k : l_k(T) > 0}, the maximum
distance from the root, and the width W(T) := max_k {l_k(T)}, the largest size
of a generation." T_n is the simply generated tree with n vertices and weight
sequence w (w_0 > 0 and w_k > 0 for some k >= 2 throughout the paper),
nu = Psi(rho) with Psi(t) = t Phi'(t)/Phi(t), and nu = 0 when rho = 0. The
convergence is along n with Z_n > 0.

Numbering: the journal version of Janson's survey has these as Conjectures
21.5-21.6 and Problems 21.7-21.8 (one extra section); the arXiv version the
ledger cites has them in Section 20. Both later papers cite the journal
numbers. The ledger row's paraphrase is accurate; nothing is misstated.

## Finding

Problem 20.8 has the answer YES, for every weight sequence with nu < 1
(including nu = 0), and this is in print. Quoting ABHK, Section 5, after they
restate the four items as "Conjecture 1 ([13])" with item (4) being "If nu < 1
then wid(T_n)/n^{1/2} -> infinity in probability":

> The results of this work establish points (2) and (4) of this conjecture,
> and establish (1) and (3) up to polylogarithmic factors.

and, after Corollary 5.3:

> Corollary 5.3 implies that if nu < 1, or if nu = 1 and sigma^2 = infinity,
> then ht(T_n)/(n^{1/2} log^3 n) -> 0 and wid(T_n)/n^{1/2} -> infinity in
> probability. This proves the second and fourth points of the above
> conjecture and nearly proves the first and third points, up to the
> polylogarithmic factors.

The remaining logarithm in the height statements was removed by Addario-Berry
and Donderwinkel (2024), Theorem 19: "Let w = (w_k, k >= 0) be a weight
sequence with w_0 > 0 and with w_k > 0 for some k >= 2. If either
sigma-hat^2 = infinity or nu < 1 then n^{-1/2} ht(T_{w,n}) -> 0, where the
convergence is in both probability and expectation". Their abstract says the
paper settles "three conjectures of Janson [30]"; the text says Theorem 19
"resolves Conjecture 21.5 and Problem 21.7". So all four of 20.5-20.8 are now
theorems.

## The argument, as published (so a referee can check the chain)

The route is exactly the one the integrator's hint suggested, and it is the
route the earlier attempt F0068-A001(c) stopped short of: condition on the
degree statistics, count with Lemma 18.31, then use a bound that holds for
every fixed degree sequence.

1. Conditional on its degree statistics n = (n(c))_{c >= 0} (n(c) = number of
   vertices with c children), a simply generated tree is uniform on the set
   of plane trees with those statistics, because its weight prod w_{d(v)}
   depends only on n. (ABHK, end of Section 1; Janson, Sections 15-16.)

2. ABHK Theorem 1.1 (verbatim): "Fix degree statistics n = (n(c), c >= 0) and
   let (T, V) be uniform on the marked trees with statistics n. Then for all
   beta > 17^{3/2},
   P{ |V| > beta |n|_1 / (|n|_2^2 - n(1))^{1/2} }
     <= exp( -(beta^{1/3}/3) |n|_1 / (|n|_2^2 - n(1))^{1/2} ) + 2 exp( -beta^{2/3}/24 )",
   where |n|_p = (sum_c c^p n(c))^{1/p}, so |n|_1 = n - 1 and
   |n|_2^2 = sum_c c^2 n(c). In words: a uniformly random vertex sits at height
   of order n / |n|_2 with stretched-exponential tails, uniformly over all
   degree sequences.

3. Counting (ABHK Corollary 5.3, proved from Janson's Theorem 11.4 restated as
   their Theorem 5.1, and from their Theorem 5.2 for rho = 0). For nu in (0,1):
   Janson's law of large numbers n(k)/n -> pi(k) for each fixed k, with
   sum_k k pi(k) = nu < 1, gives, for any fixed K, with very high probability
   sum_{k <= K} k n(k) <= nu n - 1, hence sum_{k > K} k n(k) >= (1 - nu) n, hence
   |n|_2^2 >= sum_{k > K} k^2 n(k) > K sum_{k > K} k n(k) >= K (1 - nu) n.
   Since K is arbitrary, |n|_2^2 / n -> infinity in probability. This is the
   "Lemma 18.31 counting" of the hint (Lemma 18.31(i) with lambda = 1 is the
   same inequality sum_{k > K_n} k N_k >= (1 - nu) n - o_p(n)). For nu = 0 the
   same conclusion follows from Theorem 5.2 (n(0)/n -> 1): with fewer than
   n/(2C^2) vertices of outdegree in [1, C], at most n/(2C) children come from
   them, so at least n - 1 - n/(2C) children come from outdegrees > C, and
   |n|_2^2 >= (C+1) sum_{k > C} k n(k) > C (n - 1).

4. From 2 and 3 to the width (ABHK, proof of Theorem 1.2, applied verbatim
   to simply generated trees through Section 5): on the event
   |n|_2^2 >= C |n|_1 with C = 1 + eps^{-4}, the tail bound of Theorem 1.1
   integrates to E|V_n| = O(eps n^{1/2}), so E|V_n| = o(n^{1/2}). A uniformly
   random vertex at expected height o(n^{1/2}) means that at least half the
   vertices lie within height h_n = 2 E|V_n| = o(n^{1/2}) of the root
   (Markov), and those n/2 vertices occupy at most h_n + 1 levels, so some
   level has at least (n/2)/(h_n + 1) vertices: W(T_n) / n^{1/2} -> infinity in
   probability. Nothing else about w is used.

The dependence on the weights enters only through step 3; the only algebra is
the inequality sum_{k > K} k^2 n(k) >= K sum_{k > K} k n(k) and the pigeonhole
W (h + 1) >= (number of vertices at height <= h).

## What is not done here

Nothing new is claimed. I did not re-prove Theorem 1.1 of ABHK (the
size-biased-ordering equivalence and the Camarri-Pitman Poissonization are
theirs). No Lean file: the only steps outside the cited theorems are the two
one-line inequalities above, and the machine was under a compute-distress
flag during this run; a Lean certificate of those two lines would not add
evidence about the published theorem, which is where the content is.

## Checks

1. Coverage of nu = 0. Problem 20.8 says nu < 1, which includes rho = 0. ABHK
   Theorem 5.1 assumes nu in (0, 1], so I checked that Corollary 5.3 treats
   nu = 0 separately: it does, via Theorem 5.2 (quoted in step 3). So the
   published answer covers the whole range of the problem.

2. Direction of every inequality in the chain: the tail bound of Theorem 1.1
   is an upper bound on the height of a random vertex; the counting gives a
   lower bound on |n|_2^2; a small typical height forces a large width. All
   three point the way the problem needs.

3. Mechanism check by simulation, check_width_fixed_degrees.py (single
   process, 62 s, output in check_width_fixed_degrees.out). Uniform plane
   trees with fixed degree statistics on N = 40,000 vertices, 80 percent of
   the children under vertices of outdegree a (the analogue of the (1 - nu) n
   children of Lemma 18.31), sampled exactly by the cycle lemma, 5 samples
   per profile:

       a    |n|_2^2/N   wid/sqrt N   ht/sqrt N   wid*ht/N
       2        1.9        0.90        3.01       2.70
       8        6.7        2.80        0.92       2.45
      32       25.9        6.05        0.50       2.97
     128      102.7        9.87        0.31       2.94
     512      406.6       18.34        0.15       2.66

   wid/sqrt N is about 0.9 sqrt(|n|_2^2 / N) across a 200-fold range of
   |n|_2^2 / N, and ht/sqrt N shrinks like its reciprocal, as Theorem 1.1
   predicts; the product wid*ht/N stays between 2.4 and 3.0, consistent with
   the trivial W (H + 1) >= N and with the O(n log n) product bound of
   Donderwinkel and Khanfir (PTRF 2026, arXiv 2501.00458). The second reading
   of the same numbers is the height column: it is computed from the
   depth-first heights directly, not from the width, and the two columns move
   inversely as they must. This is a check of the mechanism, not of the
   theorem; the theorem is taken from the paper.

4. The strongest case that I am wrong: that ABHK's Section 5 claim rests on a
   hypothesis Janson's problem does not grant. The hypotheses of Theorems 5.1
   and 5.2 are w_0 > 0 and w_k > 0 for some k >= 2, which are Janson's own
   standing assumptions (Section 2 of the survey; without them Z_n = 0 for
   n >= 2 or T_n is a path). Convergence is along n with Z_n > 0, as in the
   problem. I found no gap. What would break the finding is a flaw in the
   proof of ABHK Theorem 1.1 itself; that theorem has since been re-proved in
   stronger forms (Marzouk, cited by ABHK as Proposition 5 of his paper;
   Addario-Berry and Donderwinkel 2024; Donderwinkel and Khanfir 2026), which
   makes such a flaw unlikely.

## Prior art

The session's web search budget was exhausted (200/200) before this task, so
the search was done through the arXiv abstract pages, the arXiv author
listing for Addario-Berry (arxiv.org/a/addarioberry_l_1), and the Crossref
API for journal references. What found it: the author listing for
Addario-Berry, then the abstracts of arXiv 2105.03195 ("Our results allow us
to prove a conjecture and settle an open problem of Janson, and nearly prove
another conjecture and settle another open problem from the same work (up
to a polylogarithmic factor)") and arXiv 2201.11773 ("settling three
conjectures of Janson"). The exact statements were then read from the PDFs
(text copies in this directory as evidence_*.txt).

Citations:
- L. Addario-Berry, A. Brandenberger, J. Hamdan, C. Kerriou. Universal height
  and width bounds for random trees. Electron. J. Probab. 27 (2022), no. 118.
  doi 10.1214/22-EJP842. arXiv 2105.03195. Settles Conjecture 20.6 and
  Problem 20.8 (their 21.6, 21.8); Conjecture 20.5 and Problem 20.7 up to
  log^3 n.
- L. Addario-Berry, S. Donderwinkel. Random trees have height O(sqrt n).
  Ann. Probab. 52 (2024). doi 10.1214/24-AOP1694. arXiv 2201.11773. Theorem 19
  settles Conjecture 20.5 and Problem 20.7; Theorem 20 answers Problem 20.9.
- L. Addario-Berry. Most trees are short and fat. Probab. Theory Related
  Fields 173 (2019). doi 10.1007/s00440-018-0829-x. arXiv 1703.10652. The
  earlier bounds (H/W sub-exponential, H/|T|^{1/2} sub-Gaussian for
  unconditioned trees); not by itself enough for 20.8.
- S. Donderwinkel, R. Khanfir. Tight universal bounds on the height times the
  width of random trees. Probab. Theory Related Fields (2026).
  doi 10.1007/s00440-025-01462-w. arXiv 2501.00458. H W = O(n log n).
- L. Addario-Berry, S. Donderwinkel, I. Kortchemski. Critical trees are
  neither too short nor too fat. Ann. Henri Lebesgue 8 (2025), 113-149.
  Critical case only.

The ledger's status_search had already found Addario-Berry 2019 and the 2023
and 2025 papers but not the 2022 EJP paper, which is the one that names
Problem 21.8 and proves it. The earlier attempt F0068-A001 recorded the
problem as strictly weaker than Problems 20.7 and 18.39; in fact all of
20.5-20.8 are proved, and Problem 18.39 (is Y(1)/n -> 0 possible for
0 < nu < lambda) is not needed for any of them.

(This was the F0068 ask: attack Janson Problem 20.8, nu < 1 implies
W(T_n)/sqrt n -> infinity, via Lemma 18.31 counting; up to two hours.)
