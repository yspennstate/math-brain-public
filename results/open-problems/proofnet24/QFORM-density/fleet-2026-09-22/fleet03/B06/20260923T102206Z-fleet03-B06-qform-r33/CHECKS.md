# Checks for fleet03/B06 r33

Run: `20260923T102206Z-fleet03-B06-qform-r33`.

These are finite sanity checks, not substitutes for the proof in `REPORT.md`.

## Constants

For

`C0=96e/(7sqrt(2))`,

we obtain

`C0 = 26.36044133594823...`.

At `theta=1/2`, the conditioned-diffuse constant is

`2C0 = 52.72088267189646... <53`.

The physical-pivot constant is

`512 theta^(-3/8) = 512*2^(3/8)
 =663.9818519813169... <664`.

The fleet04/B18 square-smoothing coefficient applied to the diffuse base is

`2 sqrt(2C0) =14.521829453880315...`.

The robust-star / scalar-pivot threshold is

`s sqrt(theta)/8=s/(8sqrt(2))=0.08838834764831843... s`.

## Algebraic identities checked

For an exact-rank-three factorization `B=U Lambda U^T`, `U^T U=I_3`:

1. `sum_i ||u_i||^2=3` exactly by trace.
2. With `H={i:||u_i||^2>theta/32}`, `|H|<96/theta` follows immediately.
3. `M_H+M_L=I_3` exactly.
4. If `lambda_min(M_L)<theta`, the minimizing unit eigenvector `z` satisfies `z^T M_H z>1-theta` exactly.
5. If `M_L>=theta I`, the whitened frame `V=U_L M_L^(-1/2)` satisfies `V^TV=I_3` and each light leverage is at most `ell_i/theta<=1/32`.
6. `||Be_i||^2=u_i^T Lambda^2 u_i>=s^2 ell_i`, where `s=min_j|lambda_j|`.
7. Hence for every heavy coordinate, `max(|B_ii|,||B_{-i,i}||_2)>=s sqrt(theta)/8`.

## Randomized finite check

Seed: `20260923`.

1000 Gaussian random `n x 3` matrices with `100<=n<1000` were orthonormalized to Parseval frames. With `theta=1/2`:

- diffuse-light cases (`lambda_min(M_L)>=1/2`): 761;
- hub cases: 239;
- maximum observed whitened light leverage in diffuse cases: `0.029963000235037413 <1/32`;
- violations of the light-leverage or hub-mass inequalities: 0.

No probabilistic inference is made from this test.
