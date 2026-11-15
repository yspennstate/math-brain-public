You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/, sources/ of another run):
open problem I0103, Randomstrasse101: Open Problems of 2025 (Bandeira, Dmitriev, Lucca, Nizic-Nikolac, Roedder, arXiv:2603.29571;
verify version, entry and page), Conjecture 29: condition numbers of column restrictions of the (p+1)/2 x (p+1) Paley equiangular tight
frame at sparsity beyond sqrt(p), with whatever sub-dictionary alternative the source permits.

The claim is PARTIAL: for fixed 0 < rho < 1/16 and primes p = 1 mod 4, the interval sub-dictionary D_p = {0,...,L_p - 1, infinity},
L_p = floor(p^{9/16 - rho}), satisfies ||Psi^* Psi - I|| <= C_rho p^{-rho/3} + sqrt(L_p/p) = o(1), so every subset of D_p is uniformly
well conditioned; also for affine progressions a + d I_L. Proof: the finite Gram deviation is p^{-1/2} times the Toeplitz matrix
chi(i-j); its norm is bounded by the sup of the twisted character sum sum_{h<L} chi(h) e(h theta); that sup is bounded by
Heath-Brown and Pierce, Burgess bounds for short mixed character sums (J. London Math. Soc. 91 (2015); arXiv:1404.1677), Theorem 1.4,
with r = 3. The report also proves that the Kuemmerle-Mixon absolute-value method (arXiv:2611.14475) cannot work for Paley, because
|G_S - I| = p^{-1/2}(J - I) for every support S.

Break it if it is wrong.
1. Get the source and every work REPORT relies on into sources/ as plain text from arXiv, independently of claim_files/sources. State
   Conjecture 29 exactly, including the sub-dictionary alternative. Decide whether a TALL sub-dictionary (fewer columns than the
   dimension (p+1)/2, retained fraction tending to zero) is what the source's alternative means, or whether that reading makes the
   alternative trivial or out of scope. This decides how much of the problem the claim answers.
2. Check the proof line by line: (a) the Gram identity (2) and its sign and normalization; (b) the Toeplitz quadratic-form identity
   and the bound ||T_L|| <= sup |F_L|; (c) Heath-Brown-Pierce Theorem 1.4: its exact hypotheses, whether the bound is uniform over all
   real linear phases theta (not only rational ones, and with the implied constant independent of theta), the length restriction
   H < p^{1/2 + 1/(4(r-1))}, and whether the degree-1 case is unconditional; (d) the exponent arithmetic with r = 3 and eta = rho/3;
   (e) the special column and the triangle inequality; (f) whether a simpler route (Polya-Vinogradov, completion, or a classical
   Burgess bound plus a partial-summation step) already gives the same conclusion, which bears on novelty.
3. Small numerical checks in code/ (exact Gram norms for intervals at moderate p) are allowed as evidence only.
4. The hard question: is this interval statement, or an equivalent one (near-orthogonal intervals of Paley ETF columns, Burgess for
   Toeplitz character matrices, explicit beyond-square-root well-conditioned Paley supports), already in the literature: Bandeira-
   Fickus-Mixon-Wong, Bandeira-Mixon-Moreira, Satake, Mixon's chapter and blog, Kunisky, Kuemmerle-Mixon, Bourgain et al., Ford-
   Kutzarova-Shakan, and 2024-2026 work? Check every citation in REPORT against sources (title, authors, journal, year, theorem, page).
5. Verdict: correct or not, novel or not, exactly what is proved, and how much of Conjecture 29 it answers.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every error
or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts may go in
sources/ as plain text only; no PDFs kept, no page images. Work only in this directory. At most 4 threads, under 4 GB, nice 10.
No publication anywhere, no pushes.
