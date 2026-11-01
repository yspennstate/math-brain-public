# Direct audit of w483's core derivation

2026-10-10. Independent L01-L03 were saved in ATTEMPT.md before w483/ATTEMPT.md was read. This is a direct audit of the proposed derivation, not a review of a referee's review.

Verdict: KEEP the scoped conditional route; C0056 is not proved. The exact missing premise is a volume- and scale-uniform bound E C_{nu_L}(r)<=A r+B/N_L for the actual fixed-disorder Z^3 local spectral measures. Neither a bounded disorder-averaged density nor the Ward identity establishes it. My independent L01 satisfies both and has C_{mu_0}(r)=1 for all r>=0, so any volume-uniform linear bound with an atomic remainder tending to zero fails in that example. Its zero hopping explicitly prevents using it as an Anderson counterexample.

L1: Checked the Poisson semigroup identity P_eta*P_eta=P_{2eta}, the Fourier factor 1/(2 pi), and the diagonal coefficient 1/(2 pi eta). It uses the same sample measure twice; it does not multiply independent environment probabilities.

L2: The Fourier monotone-convergence argument is valid for finite positive measures. Uniform expected L2 control gives an L2 density and a finite expected squared norm. My separately derived Lp compactness argument corroborates the forward direction locally. Site transfer is countable; the nonzero-mass obligation is correctly separate.

L3: The layer-cake coefficient is 4 eta/pi. Integrating the Ar term gives A/2, and the B/N term gives B/(2 pi eta N). These constants are correct. The hardest inequality remains an assumption, which is stated honestly.

L4: Fixed-eta transfer from expanding Dirichlet cubes is sound for bounded iid potentials: the cut-bond operators converge strongly, spectral measures converge weakly, and the displayed compact-region and tail bounds dominate squared Poisson densities. The limit order L->infinity before eta->0 removes the atomic remainder; a coupled sequence alone would require another estimate. Primary GOE statistics use periodic finite volumes, so Dirichlet spectral transfer is confined to the AC branch.

L5: The Walsh/Cantor construction is a valid abstract operator obstruction. Orthogonality gives exactly flat finite-volume weights, weak spectral-measure convergence is insufficient for AC, and sharing the first m digits gives the claimed lower bound. It is explicitly outside the iid nearest-neighbor Anderson class. The tail also checks: eta_k=N_k^(-1/2)>=3^(-k), and the off-diagonal lower bound diverges as N_k^((1-alpha)/2) while the diagonal tends to zero.

The directly audited snapshot is review/w483_ATTEMPT_snapshot.md, SHA256 4f99ebdf4c964aacc446b9399db3eab0b6edcecf85ad00534470ccd9c9867338 (12629 bytes). This scoped Codex audit does not supply different-model served-identity evidence.

NEXT: Prove or refute the uniform resonant inverse-cavity estimate for the actual fixed-disorder lattice; it can complement w483's weighted-pair criterion. GOE requires a separate argument.
