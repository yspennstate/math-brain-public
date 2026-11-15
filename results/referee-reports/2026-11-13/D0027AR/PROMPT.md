You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem D0027, Martinelli-Shapira-Toninelli, "Long time behaviour of one facilitated kinetically constrained models: results
and open problems", arXiv:2510.20461, Conjecture 2, Section 1.1, PDF p. 2: for FA-1f on Z, if nu(no infected vertex in [-l,l]) =
O(exp(-kappa l)), then for all q the convergence E_nu f(eta_t) -> pi(f) is exponentially fast. The claim says PARTIAL:
Theorem A (its Section 4): for every q in (1/2,1) and finite S there are gamma, c, C depending only on q and S such that for
EVERY law nu and every f supported on S, |nu P_t f - pi f| <= ||f|| (C e^{-ct} + 2 nu(R > gamma t)), R = distance from 0 to the
nearest infection; so the centered gap hypothesis gives exponential relaxation for q > 1/2, for arbitrary correlated nu,
including a single infection at the origin. It also gives an all-q result under a local absolute-continuity assumption
(Section 5), and says both are consequences of existing methods (BCMRT 2013 Theorem 2.1 under the uniform hypothesis
sup_x nu(theta^{D_x}) < infinity; Mountford-Valle 2019 for q near 1 with Remark 1.2; CMST 2010 Theorem 2.1).

Break it if it is wrong.
1. Download arXiv:2510.20461, the BCMRT preprint (arXiv:1205.4584 or the author copy; Markov Process. Related Fields 19 (2013)
   383-406), Mountford-Valle arXiv:1609.01364 and CMST arXiv:0810.4237 into sources/ as plain text. Read Conjecture 2 and what
   the survey says is known, BCMRT Theorem 2.1 and Sections 3-5, and Mountford-Valle Theorem 1.1 and Remark 1.2.
2. Check Theorem A line by line: the finite-propagation lemma (FP), the reduction from the centered hypothesis to the uniform
   block condition BCMRT needs (how the initially empty region far from 0 is handled in time t, the inward drift for q > 1/2
   and its exact sign and rate, whether the constants really depend only on q and S), every probability estimate and union
   bound, and whether any step silently uses independence, stationarity or the uniform hypothesis (U). A single infection at
   the origin must be covered: check that case directly.
3. Check Section 5 (all q, local density control) the same way, and whether its hypotheses are ever met by laws that BCMRT,
   CMST or Mountford-Valle do not already cover.
4. Simulate independently with your own code (do not reuse claim_files/code): FA-1f from a single infection at the origin for
   q = 0.55, 0.6, 0.75, measure |E f(eta_t) - pi f| for f = 1{eta_0 = 0} and check the decay is exponential, as evidence.
5. Verdict on value: is Theorem A correct, and is it already in print (BCMRT, Mountford-Valle, Blondel, Ertul, Shapira,
   Hartarsky, 2025-2026 papers citing 2510.20461)? Does it genuinely settle Conjecture 2 for q > 1/2? What remains open?
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
