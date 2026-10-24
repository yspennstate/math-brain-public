# Deterministic check ledger

Run: `account02-B18-20260924T100529Z-r11`.

The construction uses the orthonormal active basis `(u,v,w,u2,v2)`. In that basis the matrix is exactly

`diag_blocks( [[0,1],[1,0]], [1], [[0,eps],[eps,0]] )`,

so its nonzero spectrum is `{-1,1,1,-eps,eps}`.

Numerical diagonalization at `m=8` agrees:

- `eps=0.5`: `[-1,-0.5,0.5,1,1]`;
- `eps=0.01`: `[-1,-0.01,0.01,1,1]`;
- `eps=1e-6`: `[-1,-1e-6,1e-6,1,1]`.

The source-valid dependent-pair constant is

`3*(2*2*sqrt(2))^(2/3)=3*2^(5/3)=9.524406311809198...`.

The latest account03/B18 full-cross receiver sees `d1=1,d2=eps`, hence gives `2*sqrt(pi)/sqrt(eps)`.

For the main core, spectral-subspace leverages are exactly `1/m` on the `u` bank and `2/m` on the `(v,w)` bank. At `m>=4`, pinned Theorem F's leverage gate `<=1/2` is satisfied and its bound is `12`.

Every physical coefficient of the full matrix has modulus at most `1/m`. Thus a `k x k` physical principal block has both induced `1`- and `infinity`-norm at most `k/m`, and therefore operator norm at most `k/m`.

Status: PASS for the displayed algebra and constants. These checks are finite verification only, not evidence for the full conjecture.
