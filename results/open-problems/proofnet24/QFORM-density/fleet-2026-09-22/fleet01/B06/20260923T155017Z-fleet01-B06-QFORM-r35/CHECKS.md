# r35 deterministic checks

Status: algebra/scaling sanity checks only; **not** an independent proof review.

## Identities checked

For random `R in R^{8 x 3}` with orthonormal columns and `Lambda=diag(3.2,-2.1,1.3)`, form `A=R Lambda R^T`, choose the first two original coordinates as `I`, and whenever `B=A[I,I]` is invertible compute

- `P=R_I`, `c=p_1 x p_2`, `tau=||c||^2`, `n=c/sqrt(tau)`;
- `S=A[J,J]-A[J,I]B^{-1}A[I,J]`;
- `h=R_J n`;
- `lambda=det(Lambda) tau/det(B)`.

Five fixed-seed trials gave the following maximum absolute residuals for

1. `S-lambda h h^T`,
2. `||h||-1`,
3. each triple identity `det A[I union {k}]-det(Lambda)tau h_k^2`,
4. `sum_k |det A[I union {k}]|-|det Lambda|tau`.

```
trial 1: 7.71e-16, 0.00e+00, 1.39e-17, 2.78e-17
trial 2: 7.70e-15, 2.22e-16, 2.78e-17, 4.16e-17
trial 3: 2.53e-15, 1.11e-16, 5.55e-17, 1.11e-16
trial 4: 1.25e-15, 1.11e-16, 2.22e-16, 4.44e-16
trial 5: 3.58e-15, 0.00e+00, 1.11e-16, 3.33e-16
```

The first trial, for example, had `det(B)=-0.0519345670091`, `tau=0.0192524040461`, `lambda=3.23847894443`.

## Constant checks

```
4 sqrt(6) e^(1/4) = 12.580828350598074
16 * 2^(1/4) * sqrt(30) = 104.216889989...
```

The homogeneity of the compiler is correct: scaling `A -> cA` sends `D -> c^2 D`, `|det Lambda| -> |c|^3 |det Lambda|`, while `tau` is unchanged, so

`D^(-1/8)(|det Lambda|tau)^(-1/4) -> |c|^(-1)`

as required for a density bound.

## Manual source/privacy allowlist review

Changed mathematical files in this run contain only QFORM mathematics, repository source pins, harmless run identifiers, and control/correction hashes. No credentials, tokens, financial/client data, private personal archives, signed URLs, or public-release operations are included. No dependency-backed repository secret scanner was exposed in this connector, so this is a narrow manual allowlist review rather than a full repository scan.
