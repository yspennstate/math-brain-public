You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem D0028, Conjecture 3 of Martinelli-Shapira-Toninelli, "Long time behaviour of one facilitated kinetically
constrained models: results and open problems" (arXiv:2510.20461v1, PDF p. 8): every stationary measure mu of a kinetically
constrained model is a mixture, over bootstrap-stable configurations beta, of the product measure pi conditioned on
{BP(eta) = beta}. The source proves it for the d-dimensional East model, in d = 1, and for translation-invariant mu.
The claim (PARTIAL) proves, without translation invariance:
(1) on every strip Z x H (H finite connected), every stationary law of FA-1f is lambda pi + (1 - lambda) delta_1, for every
    0 < q < 1, and likewise for finite-range monotone binary heat-bath constraints that allow every FA-1f move and forbid updates
    in the all-filled configuration; no finite-energy assumption (Section 3: an entropy argument plus identification by
    internal spanning);
(2) on Z^2, for any finite-range binary heat-bath KCM, a stationary law with uniformly bounded single-site conditional odds
    satisfies detailed balance, and if the model internally spans large boxes with probability -> 1 at every positive vacancy
    density, the law equals pi; this covers planar FA-1f and FA-2f (Section 4, with an elementary proof of the FA-2f bootstrap
    fact (4.4)).

Break it if it is wrong.
1. Get arXiv:2510.20461 into sources/ as plain text and state Conjecture 3 and Theorem 2.13 exactly (what "stationary" means,
   finite versus infinite volume, how pi_beta is defined on null events). Check that the claimed form lambda pi + (1-lambda)
   delta_1 agrees with the conjecture on a strip (what are the BP-stable configurations of FA-1f on Z x H?). Search for prior
   results covering (1) or (2): Mountford ("A complete convergence theorem for attractive reversible nearest particle systems"
   / FA-1f invariant measures), Cancrini-Martinelli-Roberto-Toninelli, Blondel, Shapira, Hartarsky ("bootstrap percolation and
   kinetically constrained models", the 2025-26 book/survey), Holley-Stroock style entropy arguments for non-translation-
   invariant stationary measures (Holley 1971, Moulin-Ollagnier-Pinchon, Georgii), and 2025-2026 citers of the source.
2. Check the strip entropy proof line by line: the relative entropy production for a non-translation-invariant stationary law
   on Z x H (how boundary terms at +-infinity in the Z direction are controlled without translation invariance; the box size
   versus surface growth in a quasi-one-dimensional strip), the conclusion of detailed balance or of reversibility, and the
   identification step by internal spanning.
3. Check the planar proof: exactly where bounded conditional odds is used, whether the surface-to-volume entropy argument works
   in d = 2 (it is classically borderline at d = 2: check the counting carefully), and the step from detailed balance plus
   spanning to mu = pi. Check the FA-2f bootstrap fact (4.4).
4. Write your own independent code (do not reuse claim_files/code): exact stationary measures of FA-1f on small Z_n x H tori and
   boxes with boundary conditions, by solving the generator kernel in rationals or high precision, and check the claimed form.
5. Verdict on value: are (1) and (2) correct, are they new, and what remains of Conjecture 3.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
