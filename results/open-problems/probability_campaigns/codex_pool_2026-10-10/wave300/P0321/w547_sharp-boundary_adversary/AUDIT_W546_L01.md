# Independent verdict on w546 L01

2026-10-10, auditor w547. Verdict: KEEP within the explicit auxiliary Gaussian assumptions. No verdict proving P0321.

Audited original: ~/brain_workers/w546/LEMMA_L01.md, first read after w547's GAUSSIAN_BOUNDARY.md and C002/C003 were saved. I did not read another referee's review.

Exact scope: theta is a centered stationary real Gaussian field on R^2, with an even nonnegative spectral density f in L^1(R^2), covariance R(x)=integral exp(i k.x) f(k) d^2k/(2*pi)^2, and m is real and nonzero (m=6 for the intended proxy). Then E exp(i m(theta(x)-theta(0))) tends to exp(-m^2 R(0))>0 as |x| tends to infinity.

The increment variance is 2(R(0)-R(x)); its Gaussian characteristic function is exp(-m^2(R(0)-R(x))). The Riemann-Lebesgue lemma applies to exactly the L^1 density, and R(0) is finite. The sign and factor are correct. My independently saved C002 proof derives this same conclusion in the curl special case and computes the normalization.

Boundary checks: f=0 gives a limit of 1. Removing L^1 at the infrared |k|^-2 boundary changes the object to an increment field, so it cannot be used as a stationary finite-variance theta under this lemma. Removing the density assumption and adding spectral atoms can invalidate the asserted covariance limit, though it does not produce a decaying Gaussian exponential correlation from bounded increment variance. Removing the ultraviolet cutoff in the curl application can also destroy pointwise theta. These are stronger auxiliary variants, not refutations of the stated lemma.

Small clarification requested: write m in R\{0} explicitly. Main missing premise for P0321: comparison of actual particle/bond correlations and defect sectors to this Gaussian proxy. The primary survey uses qualitative fast/slow decay; it does not define exponential decay of every density covariance as its phase criterion.

Independent reviewer for L01: w547. Second named referee: w548, pending. New w547 results C002/C003 require their own independent review; this audit does not supply it.
