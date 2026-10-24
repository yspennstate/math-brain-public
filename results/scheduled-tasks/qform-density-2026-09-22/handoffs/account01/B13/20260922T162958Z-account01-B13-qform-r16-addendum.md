# account01/B13 r16 addendum — cap scaling

Canonical addendum: `yspennstate/math-open-problems@5e3a7a48ed7222861e0cd900fb0f9a38e1e940b8`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260922T162958Z-account01-B13-qform-r16/CAP_SCALING_ADDENDUM.md`.

For independent two-variable inputs with density caps `M,N`, the affine half-Riesz theorem scales exactly to

`sup_t E|R-t|^(-1/2) <=8sqrt(2)(MN)^(1/2)|det S|^(-1/4)`.

Thus a three-variable affine quadratic with caps `K1,K2,K3`, invertible Hessian `T`, and nonzero pivot `d=T_11` has

`||p_Q||_infinity <=8sqrt(2)K1(K2K3)^(1/2)|d det T|^(-1/4)`.

For three exact disjoint aggregate banks, each product-linear marginal has cap at most `sqrt(2)`, so the grouped certificate is

`||p_Q||_infinity <=16sqrt(2)|d det T|^(-1/4)`.

This isolates the remaining collar debt to loss of exact bank structure or the all-isotropic/zero-pivot aggregate endpoint, not affine leakage or unequal cap scaling. Full QFORM remains OPEN.
