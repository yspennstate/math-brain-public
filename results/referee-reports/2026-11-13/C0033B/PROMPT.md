# Open problem C0033: concavity of the entropy of determinantal measures in the kernel

Source: R. Lyons, "Determinantal probability measures", Publ. Math. IHES 98 (2003), Section 5 (entropy; the conjecture on
concavity of the entropy rate of stationary determinantal processes in the symbol, recorded as Conjecture 5.3 in our ledger).
Partial result: Yuzhou Gu, "Entropy of determinantal point processes" (unrefereed report, https://sevenkplus.com/data/dpp.pdf):
concavity along segments with rank(K_1 - K_2) = 1 (Theorem 7) and H(X(tK)) >= t H(X(K)) (Corollary 6). Fetch both if you can.

Setting. E finite, |E| = n. For a positive contraction Q on l^2(E) (0 <= Q <= I, Hermitian), P_Q is the determinantal measure on
subsets of E: P_Q[S subset X] = det Q_{S,S}; equivalently P_Q[X = S] = |det(Q - I_{E\S})|. Ent(P_Q) = - sum_S P_Q[X=S] log P_Q[X=S].

QUESTION (finite form): is Q -> Ent(P_Q) concave on positive contractions? A first attempt is in ../C0033A (read REPORT.md,
LOG.md and its code first; reuse its exact enumeration and Hessian code). It proved: n = 2; changes supported on at most two
coordinates in any n (conditional lifting); negative semidefinite Hessian at block-diagonal kernels with blocks <= 2; an
explicit fourth variation at product kernels. Its formula (16) is a starting point for three points. No counterexample.

TASK for this attempt, in order:
1. n = 3, real symmetric and complex Hermitian: prove concavity of H on all 3x3 positive contractions, or find a
   counterexample (verify at 100+ digits). Reduce by unitary-diagonal conjugation and permutation; consider a certificate
   for the sign of D^2H via sum-of-squares or interval arithmetic on a compact parametrisation if a closed form fails.
2. General rank-two directions A = a a* - b b* (or rank(Q_1 - Q_2) = 2) in any n: prove or refute concavity along them,
   extending Gu's rank-one argument (Y. Gu, "Entropy of determinantal point processes", sevenkplus.com/data/dpp.pdf).
3. Commuting kernels (Q_1, Q_2 simultaneously unitarily diagonalisable, not coordinate-diagonal): the measure is then not a
   product; settle concavity along such segments.
Keep peak memory under 4 GB; no worker pools larger than 4 threads.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written as for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem/proof text.
