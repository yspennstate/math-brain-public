SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-23T06:56:57Z.
attacking: factorization-invariant two-area smoothing for a grouped bilinear packet, then transfer to signed Fejer.

# account03/B01 handoff — determinant-area affine receiver

Outcome: `PROVED_SUPPORTING_TARGET_LEVEL_THEOREM`; full QFORM remains `OPEN`; execution `WITHOUT_VERIFIED_BRAIN`; continuity not proved by this branch.

Fresh source control was resolved through `yspennstate/math-research-brain@f45849f497c7d817fc46e725e6a0b09973b39573`; live OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only.

Canonical mathematics: `yspennstate/math-open-problems@e37f094a72721e92fa82334f3b55ee4dd6d6695b`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T065657Z-auto11-detarea/REPORT.md`. Deterministic algebra/scaling checks in the same folder end `STATUS=PASS`.

## New theorem

Partition original independent coordinates into disjoint banks `I,J,D,W`. Let `K` be the `I x J` cross matrix with two largest singular values `kappa_1>=kappa_2>0`. Let `c=c(X_D,X_W)` and arbitrary measurable `H=H(X_I,X_D,X_W)`. For

`Q=2 X_I^T K X_J + c^T X_J + H`,

one has

`||p_Q||_infinity <= 2 sqrt(pi) (kappa_1 kappa_2)^(-1/2).`

Equivalently `2 sqrt(pi)||wedge^2 K||_op^(-1/2)`. If rank `K=2`, this is

`||p_Q||_infinity <=2sqrt(pi)e_2(KK^T)^(-1/4).`

The proof conditions on the entire nonlinear side, applies the one-dimensional product-projection cap to the untouched receiver bank, projects the random coefficient onto the top two right singular directions, and averages the resulting inverse-radius singularity against the bounded density of the corresponding two-dimensional orthogonal projection of the original product source. The planar anisotropic lemma is

`E|S(Y-a)|^(-1) <=2sqrt(pi K0)|det S|^(-1/2)`

for any planar density `<=K0`, uniformly in translation.

For a latent factorization `K=M^T N`, the same theorem is

`||p_Q||_infinity <=2sqrt(pi)[det(MM^T)det(NN^T)]^(-1/4),`

removing the r23 `sigma_min(N)^(-1)` condition-number loss and making the bound invariant under `M->TM, N->T^(-T)N`.

## Partner application

Applied the completed account04/B01 signed-Fejer theorem at `yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`. Therefore

`sup_{T>0,y} D_T law(Q)(y) <=2sqrt(pi)(kappa_1 kappa_2)^(-1/2).`

Also directly, every interval `I0` satisfies

`P(Q in I0)<=2sqrt(pi)|I0|(kappa_1 kappa_2)^(-1/2).`

The phase-aligned fragmented-support counterexample to law-uniform pointwise Fresnel decay is preserved; no pointwise quadratic-phase decay or absolute Fourier `L1` assumption is used.

## Exact boundary / next implication

The theorem pays every one-sided-affine rank-two cross packet with aggregate exterior area and arbitrary nonlinear curvature on the conditioned side. It does not pay simultaneous nonlinear self-curvature on both active banks, and the bare three-large-eigenvalue hypothesis does not force one uniformly large fixed cross packet. Next: either route concentrated strict-N3 states into this one-sided-affine packet before inversion, or extend the signed-Fejer receiver to a genuinely two-sided-curved bicore while preserving original-coordinate product provenance.
