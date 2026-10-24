# Route 19 — character-gauge normalization and multiscale spectral dependence

**Role:** account03/B17, FEI new proof mechanisms.  
**Status:** route opened; full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.  
**Novelty:** no publication-priority claim.

## Mechanism

For a Boolean `f` with Fourier spectral law `p(S)=fhat(S)^2`, multiplication by a character `chi_T` translates the spectral law by symmetric difference with `T` while preserving spectral entropy. Therefore the universal FEI problem can be put in a canonical **character gauge** minimizing expected Hamming weight of the spectral sample. In that gauge every spectral membership bit has marginal at most `1/2`.

The proposed attack is then to rewrite the entire FEI gap as a **total-correlation payment problem** for those median-normalized spectral bits. Generic subadditivity pays all coordinates except very rare marginals; Booleanity must force enough multiscale dependence among the rare bits. The Boolean convolution identity `fhat * fhat = delta_empty` supplies exact signed translation-orthogonality constraints that arbitrary subset laws do not satisfy.

## First statements to prove or kill

1. Prove the exact character-gauge equivalence
   `FEI(C) <=> H(p) <= C sum_i min(q_i,1-q_i)`, where `q_i=P(i in S)`.
2. Rewrite it exactly as a lower bound on total correlation `TC(p)`.
3. Test whether the required dependence can be certified using only pairwise mutual informations (the maximum-spanning-tree / Chow–Liu lower bound on `TC`).
4. If pairwise dependence is insufficient, quantify the obstruction on an exact admissible Boolean family and move immediately to growing-block / multiscale conditional mutual information rather than another pairwise checker.

## Kill criterion

The pairwise subroute is dead if an explicit Boolean family has the required FEI total-correlation deficit asymptotically larger than the strongest tree-summable pairwise mutual-information lower bound. The full Route 19 remains alive only if higher-order dependence has an exact Boolean source (for example the convolution/cancellation constraints) rather than being inserted as an unproved generic assumption.
