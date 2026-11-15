Open problem C0122. Source: S. Chatterjee, "Chaos, concentration, and multiple valleys" (2008), arXiv:0810.4221,
Section 12, open problem (5), p. 59: show that chaos implies the multiple-peaks (multiple valleys) property for Gaussian
fields whose correlations are not all nonnegative; the paper's argument needs a second-moment bound on the overlap
R(I_0, I_t) between the maximiser at time 0 and at time t (Ornstein-Uhlenbeck perturbation), which it obtains only under
nonnegative correlations. Read the source for the exact definitions of chaos and multiple peaks and the theorem that
holds under nonnegative correlations.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:0810.4221 into sources/ (text only) and read the relevant sections and Section 12. Search
   2008-2026 for later work: Chatterjee's book "Superconcentration and related topics" (2014), Ding-Eldan-Zhai, Eldan,
   Chen-Handschy-Lerman, Auffinger-Chen, Chen-Panchenko "temperature chaos", Gaussian disordered systems, "multiple
   peaks"/"multiple valleys", and anything citing this open problem. If it is answered in print, give the exact reference
   and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Decide the direction. Either (a) prove the implication without nonnegative correlations, possibly under an extra mild
   hypothesis, by bounding E R(I_0,I_t)^2 via the covariance structure (e.g. through E max representation, Gaussian
   interpolation, or a different route than the paper's), or (b) construct a counterexample: a sequence of centred Gaussian
   fields (X_n(i))_{i in S_n}, with some negative correlations, that is chaotic in Chatterjee's sense but lacks multiple
   peaks. Natural candidates: fields built from a few nearly antipodal directions, signed sums, X(sigma) = -X(-sigma)
   symmetric fields (e.g. SK-type with odd interactions), block constructions combining a superconcentrated part with an
   anticorrelated part.
3. Compute. Simulate candidate fields (finite S_n, exact maximiser by enumeration or GPU-friendly vectorised sampling) to
   estimate E R(I_0,I_t), the near-maximiser overlap distribution, and Var(max), checking chaos and multiple peaks as n
   grows; use this to guide 2(a) or 2(b). Keep simulations modest (CPU, at most 4 threads).
4. Give a rigorous proof of whatever you claim (the implication, or the counterexample's two properties).
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result. Keep LOG.md as you go. Code in code/,
data in data/. Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
