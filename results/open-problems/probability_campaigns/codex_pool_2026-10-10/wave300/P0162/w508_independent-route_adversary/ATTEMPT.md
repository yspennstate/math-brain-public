# P0162 independent route (saved before reading w507)

2026-10-10. No w507 mathematical artifact has been read. This is a method declaration, not a proof of FEI.

Work with uniform measure on {-1,1}^n, real Walsh coefficients, base-2 Fourier Shannon entropy H(f) and total influence I(f). The target is one absolute C with H(f) <= C I(f) for every Boolean sign function and every dimension.

Independent method: exact spectral distributions and entropy defects, rather than a direct hypercontractive estimate. Use a quadratic bent function on an even number m of bits, flip its value at exactly one input, and attach one selector bit choosing between the original and the flipped function. Both restrictions are Boolean. Compute the selector influence and the entropy difference H(f) - (H(f_+) + H(f_-))/2 exactly. This tests whether a dimension-free entropy charge to each individual coordinate can be valid. A proposed local estimate must be distinguished from a claim that at least one good coordinate exists.

Second diagnostic: for the AND sign function, compare true spectral entropy with the sum of its marginal spectral entropies. The marginal relaxation can lose a factor growing with dimension even when the actual FEI ratio stays bounded. This supplies a concrete obstruction to discarding spectral dependencies.

Hardest open piece: obtain a dimension-free global bound on the full joint spectral entropy using Boolean Fourier constraints. Refuting an overstrong local inequality or a marginal relaxation does not solve that piece.

Checkpoint: the independent one-point derivation was saved before reading w507. The paired prover independently found the same family using a different entropy argument. Its narrow L1-L3 passed the analytic adversarial audit. A later, separately labeled extension treats every sufficiently sparse flip set E by support size; SHARP_COORDINATE_BOUND.md gives the logarithmic upper estimate and its optimal additive constant. Canonical owner records already cover related upper bounds and arbitrary-coordinate obstructions, so no novelty claim is made.

The planned finite checker was stopped by its gate before any spectra were computed. A subsequent governor snapshot showed distress/process_critical. The resulting packet contains analytic drafts and an unrun checker, not numerical evidence or a solved FEI theorem.

NEXT: Integration contact codex-01a12190 resolves served-model evidence and deduplication for the three scoped analytic KEEP claims; global coordinate-selection remains unproved.
