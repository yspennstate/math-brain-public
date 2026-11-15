Open problem D0037. Source: R. C. Bradley, "Basic properties of strong mixing conditions. A survey and some open questions",
Probability Surveys 2 (2005) 107-144 (arXiv:math/0511078), Question 9, Section 7, PDF p. 29: "What condition on a spectral
density is necessary and sufficient for a stationary Gaussian sequence to be rho*-mixing?" (rho*(n) = sup of correlations
between functions of the variables indexed by two sets S,T with dist(S,T) >= n, not necessarily past/future; read the source for
the exact definitions and whether "rho*-mixing" means rho*(n) -> 0 or rho*(n) < 1 for some n).

Do this, in order, saving as you go:
1. Literature first. Download the source into sources/ and read Section 7 and the definitions. Search later work: Bradley's
   own papers on rho* for Gaussian sequences and random fields (Bradley 1992 "On the spectral density and asymptotic normality
   of weakly dependent random fields" J. Theoret. Probab.; Bradley 1993 "Equivalent mixing conditions for random fields"; Bradley
   2007 book "Introduction to Strong Mixing Conditions" vols 1-3, especially the Gaussian chapters), Kolmogorov-Rozanov,
   Helson-Sarason, Sarason (functions of vanishing mean oscillation), Ibragimov-Rozanov "Gaussian random processes", Peller,
   Miller (rho* and Gaussian), any 2005-2026 paper. Note Bradley's survey may itself state partial results (e.g. a sufficient
   condition: continuous positive spectral density). If the question is answered in print, give the exact theorem and reference
   and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Translate rho* for Gaussian sequences into an operator/angle statement in L^2(f) on the circle: for disjoint index sets S,T
   at distance n, rho* equals the cosine of the angle between closed spans of {e^{ik.}: k in S} and {e^{ik.}: k in T} in L^2(f).
   Prove this reduction (or cite it).
3. Try to prove a characterisation. Natural candidates: (a) rho*(n) -> 0 iff f is continuous and positive (bounded away from 0
   and infinity) up to ... ; (b) rho*(n) < 1 for some n iff f is bounded above and below (log f in L^infinity) - compare with
   the rho-mixing case f = |P|^2 exp(u + v~) with u, v continuous. Test candidates against examples: f with a zero (|1-e^{it}|^2),
   f discontinuous but bounded away from 0 and infinity, f = exp(continuous unbounded-conjugate). Prove necessity and sufficiency
   directions you can; give counterexamples to wrong candidates with full proofs.
4. Numerics may help: compute rho* restricted to finite index sets via generalized eigenvalues of Toeplitz blocks for test
   spectral densities.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE (PROVED =
a full necessary-and-sufficient condition with proof). Then statement, proofs, checks, literature with exact references. Keep
LOG.md. Code in code/, data in data/. Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication, no pushes.
