# Open problem C0033: concavity of the entropy of determinantal measures in the kernel

Source: R. Lyons, "Determinantal probability measures", Publ. Math. IHES 98 (2003), Section 5 (entropy; the conjecture on
concavity of the entropy rate of stationary determinantal processes in the symbol, recorded as Conjecture 5.3 in our ledger).
Partial result: Yuzhou Gu, "Entropy of determinantal point processes" (unrefereed report, https://sevenkplus.com/data/dpp.pdf):
concavity along segments with rank(K_1 - K_2) = 1 (Theorem 7) and H(X(tK)) >= t H(X(K)) (Corollary 6). Fetch both if you can.

Setting. E finite, |E| = n. For a positive contraction Q on l^2(E) (0 <= Q <= I, Hermitian), P_Q is the determinantal measure on
subsets of E: P_Q[S subset X] = det Q_{S,S}; equivalently P_Q[X = S] = |det(Q - I_{E\S})|. Ent(P_Q) = - sum_S P_Q[X=S] log P_Q[X=S].

QUESTION (finite form): is Q -> Ent(P_Q) concave on the convex set of positive contractions, i.e.
Ent(P_{(Q_1+Q_2)/2}) >= (Ent(P_{Q_1}) + Ent(P_{Q_2}))/2 for all Q_1, Q_2? (Real symmetric and complex Hermitian both matter;
the stationary/Toeplitz case, Q = Fourier multiplier with symbol f on Z_n, is the one behind the entropy-rate conjecture.)

TASK: settle it, or settle the strongest piece you can.
1. Exact search for a counterexample. Ent is computable exactly for n <= 14 or so (2^n subsets; use compiled code, or the
   formula via principal minors). Test midpoint concavity and the sign of the second derivative d^2/dt^2 Ent(P_{Q+tA}) over
   random and optimised directions (gradient descent / Nelder-Mead on the second derivative, starting near extreme points:
   projections, Q with eigenvalues near 0 and 1, rank-2 differences, real vs complex). Also the Toeplitz family on Z_n.
   A counterexample must be verified in exact or high-precision arithmetic (mpmath / rationals) and reported with its matrices.
2. If no counterexample appears, try to prove: rank-2 directions; the Toeplitz/circulant case (where the eigenbasis is fixed
   and Ent is a function of the symbol values); small n (n = 2 and n = 3 in closed form); concavity in the commuting case
   (Q_1, Q_2 simultaneously diagonal: then P_Q is a product of Bernoullis - check). Extend Gu's rank-one argument if possible.
3. Check the literature (citations of Lyons 2003 on entropy, any 2010-2026 papers on entropy of DPPs / log-concavity /
   strong Rayleigh entropy) before claiming novelty.
Keep peak memory under 4 GB; no worker pools larger than 4 threads.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written as for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem/proof text.
