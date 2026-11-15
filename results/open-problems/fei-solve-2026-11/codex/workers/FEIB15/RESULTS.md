# FEIB15 results

Completed literature audit, proofs, and census. The requested dimension-free base-camp proof remains unavailable for the mathematical reason below. Logs are base 2 unless marked ln. A literature search is not a novelty certificate.

Primary-source lead: Gonzalez–MacManus–Pereyra, arXiv:2606.00246v2, explicitly studies the entropy decrement under one-coordinate restriction and induction on a stopping binary tree. Its exact overlap is being checked.

KKLMS Theorem 1.3 has a degree logarithm inside a weighted spectral moment; it must not be silently replaced by I log I.

CHECKED overlap: Gonzalez–MacManus–Pereyra (2026), Corollary 4.2, equation (22), is exactly the one-coordinate erasure entropy inequality after substituting fhat+=(a+b), fhat-=(a-b). Appendix B, equation (32), is exactly D_i=E_i+JS_i. It already treats the second term as influence-bounded. The erasure terminology and sharp additive constant need separate attribution, but the algebraic criterion is already published.

CHECKED census (`census.json`): n=4 has 65,536 functions, 2,104 NA samples, 6,168 pairwise-NC samples, and 3,544 globally log-submodular samples. NA is tested using all increasing indicator events on disjoint blocks, with integer arithmetic. Pairwise NC is weaker. The maximum measured H^-/I is 2.704153205629417 bits per unit influence, at table 19. These are finite-census results, not universal constants.

PROVED obstruction to requested base camp: a selector between f and an independent dictator has bounded influence and retains exactly p H^-(f) in its original-coordinate edges. Consequently a dimension-free O(I log(I+2)) or O(I^2+I) erasure bound would imply FEI itself, even if the proposed base camp is restricted to balanced functions. Pure O(I^2) for all functions is false as I tends to zero (AND_n). The full proofs are in PROOFS.md.

PROVED and CHECKED: all 2,104 NA spectral samples at n=4 are positive-contraction DPPs and therefore strongly Rayleigh. `dpp_certificates.json` gives exact rational kernels for all 14 NA spectrum types modulo coordinate permutations. The certificate checks exact generating-polynomial determinants and all principal minors of K and Id-K. The converse follows from the published DPP/SR=>NA theorem. This is only a finite census classification.

PROVED: H^-<=I log2(e n/I), the erasure/FEI equivalence with additive 2/ln 2, KKLMS's internal-edge bound with its weighted degree logarithm, and the precise hypercontractive small-influence/large-sample estimate. A scalar constant in FLOW 10(a)'s gentle-edge estimate also needs adjustment; PROOFS.md gives a valid coefficient.

CHECKED lower record (`audit.json`): reconstructed PM(K3,3)+nine-coins is balanced, has exact I=261/128 by both Fourier degree and direct pivotal counts, H=6.7766053090059780825 bits, and amplification ratio 6.5218457109230465756581. This matches the opened public record's value. Our high-precision evaluation is not claimed as a new interval certificate.

Validation: dense integer character sums independently reproduce every spectrum through n=4 with zero integer error. Census entropy checks find no violations at floating-point precision. Selector formulas are checked on directly built truth tables. Each numerical process inherited niceness 10 and used one numerical thread; the largest recorded peak RSS is 177,438,720 bytes in census.json.

The brain helped identify relevant prior audit scars. Math recall returned `math store not found`. No memory was published outside this folder.
