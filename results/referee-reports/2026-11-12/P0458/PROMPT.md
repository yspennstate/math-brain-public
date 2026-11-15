You are refereeing a mathematical paper that has been posted. Be a hard, independent referee: your job is to find a gap or an error if there is one, not to confirm.

Rules for this run (the author's standing laws): work only inside your own folder (the current directory); READ anything in it, but never edit or delete anything outside it, never git push, never start other agents, never open a visible window. Do not use web search or browsing. This machine is shared and busy: run nothing that needs more than 1 GB of RAM, keep every computation under five minutes, and use at most two processes at a time. Write your own programs (Python with fractions, mpmath, sympy, numpy or scipy if they are installed; C if you need speed); do not assume any program of the authors is correct. Save every program you run in this folder.

What to referee: PAPER.tex in this folder (the LaTeX source, about 13 pages). The authors' checks and a Lean file are in code/; you may read them, but check the claims yourself.

The bilateral preference graph LK(n,k): independent uniform scores on the edges of K_n, each vertex prefers its k incident edges of smallest score, and an edge is kept when both endpoints prefer it. D is the degree of a fixed vertex. The paper claims:
- Theorem 2.1 (interior regime, k -> infinity and n - k -> infinity): (k - D)/s_n with s_n^2 = k(n-k)/n converges in law and in its first two moments to phi(Z) + Z Phi(Z), Z standard normal; hence E D = k - s_n/sqrt(pi) + o(s_n) and Var D = (1/3 + (sqrt3 - 2)/(2 pi)) s_n^2 + o(s_n^2); the standardized degree has a law bounded above, so not normal.
- Section 2 lemmas (the representation of H, Lemma 2.2 covariance of two neighbours, Lemma 2.3 variance, Lemma 2.4 small variance given X, Lemma 2.5 conditional mean), Section 3 (the limit law).
- Theorem 4.2 (fixed r = n - 1 - k >= 1): k - D converges in law and in all moments to a mixed Poisson variable whose mean is an explicit function of a gamma variable of shape r; Lemma 4.1, Proposition 4.3.
- Theorem 5.1 (the fixed-r limits converge, after standardization, to the interior law as r -> infinity).
- Proposition 6.1 and Theorem 6.2 (fixed k via the Erlang weighted tree; every subsequential limit of the standardized degree is identified).
- Proposition 7.1 and Corollary 7.2 (E(k - D) is the same at budgets k and n - 1 - k for every n).
- Section 8 (computations).

What to do:
1. Check every lemma, proposition, theorem and corollary line by line: every conditioning step, every covariance and error term, the passage from conditional mean and small conditional variance to the limit law, the moment convergence claims (uniform integrability), and the classification argument in Section 6 (does it really cover every sequence k(n), including k bounded but not fixed, and r bounded but not fixed, by passing to subsequences?). For each result write SOUND, GAP (a missing step that can be filled: give the fix) or ERROR (false as stated: give a counterexample or the failing step).
2. Check the constants: E[phi(Z) + Z Phi(Z)] = 1/sqrt(pi) and Var[phi(Z) + Z Phi(Z)] = 1/3 + (sqrt3 - 2)/(2 pi), by exact or 30-digit integration.
3. Check Proposition 7.1 exactly: compute E(k - D) for small n (n up to 8 or 9) and every k by an exact method (for example symbolic integration over the order statistics, or exact enumeration of score orderings with fractions), and confirm the symmetry k <-> n - 1 - k; also confirm by simulation for a larger n.
4. Simulate LK(n,k) yourself (n from 1,000 to 20,000 as time allows) in the interior regime (k = n/4, n/2, sqrt n) and for fixed r = 1, 2, 5, and compare the empirical law, mean and variance of k - D with the claimed limits; say how large the finite-n deviations are and whether the paper's Section 8 numbers agree with yours.
5. Say whether the Lean file proves what the paper says it proves, and report wording problems only where they make a statement wrong or ambiguous; say whether the cited earlier results (La-Kabkab, Dabirian-Subramanian, Moharrami-Subramanian-Liu-Sundaresan) are used for what they state as far as the text shows.

Write your report to REPORT.md in this folder: first line "Overall verdict: SOUND", "Overall verdict: SOUND WITH GAPS" or "Overall verdict: NOT SOUND"; then one section per numbered result with its verdict and reasons; then the checks with the programs' names and outputs; then a list of corrections, each with the line or display it concerns.
