# Controlling addendum — 1/39 window and heavy-coordinate currency

This addendum is later than `REPORT.md` in the same immutable run and controls its Section 5 constants. The square-assisted ridge theorem in Sections 3-4 of `REPORT.md` is unchanged.

## New named-partner dependency actually applied

After the primary report was committed, the assigned partner account03/B04 completed `QFORM-SPECTRAL-WINDOW-1OVER39-v1`:

- repository/commit: `yspennstate/math-open-problems@093c15486c794a2e8b23978ca7b289feabf999a7`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260922T154859Z-r13/REPORT.md`

The partner independently checks the ridge-perturbation and MSS/spectral-window passage, while explicitly not claiming a new independent review of the free-regularizer graph/Fourier core. Its proved source-pinned consequence is:

> Let `P_39` be the spectral projection onto all eigenspaces with `|lambda(A)|>=1/39`. Under the full target hypothesis, if `max_i (P_39)_ii<=1/32`, then for every admissible independent product law the quadratic form has a continuous `C_0` density and
>
> `||p_(X^TAX)||_inf < 35.27`.

This compatible completed partner result is now applied directly.

## `QFORM-WINDOW39-HEAVYCOORD-DICHOTOMY-v1`

For every target matrix `A` (at least three eigenvalues of modulus at least one), one of the following holds:

1. for every admissible product law,

   `||p_(X^TAX)||_inf <35.27`;

2. there is an original coordinate `i` such that, writing

   `a=A_ii`, `b=A[i,i^c]`,

   one has

   `boxed: max(|a|, ||b||_2) >= 1/312.`

### Proof

If `max_i(P_39)_ii<=1/32`, apply the partner theorem and obtain branch 1.

Otherwise choose `i` with `(P_39)_ii>1/32`. In an orthonormal eigenbasis,

`||Ae_i||_2^2
 = sum_alpha lambda_alpha^2 |u_alpha(i)|^2
 >= (1/39)^2 (P_39)_ii
 > 1/(39^2*32).`

But `||Ae_i||_2^2=a^2+||b||_2^2`. If both `|a|<1/312` and `||b||_2<1/312`, then, since `312=39*8`,

`a^2+||b||_2^2 < 2/(39^2*64)=1/(39^2*32)`,

a contradiction. QED.

This improves the provisional `1/64` / `1/512` heavy-coordinate split in the primary report to the source-pinned `1/39` / `1/312` split.

## Updated first unpaid implication

The live structural obligation is now `QFORM-RIDGE-SQUARE-OR-HEAVY-BANK-ROUTING-v2`:

- the diffuse `1/39` spectral-window branch is already paid by the named partner with density `<35.27`;
- every remaining target matrix has an original coordinate carrying at least `1/312` either as a scalar square coefficient or as off-diagonal `l2` bank mass;
- in the scalar-square subbranch, the new theorem `QFORM-SQUARE-ASSISTED-RIDGE-L32-v1` only asks for a residual physical ridge certificate with `theta>4q/3`, rather than the direct-ridge threshold `theta>2q` or ordinary range leverage;
- in the heavy-bank subbranch one must invoke or strengthen a product-preserving aggregate hyperbolic/fresh-square mechanism without selecting a vanishing local minor.

No exhaustive routing theorem is proved here, so the full conjecture remains OPEN. No peer review status is upgraded beyond the partner's stated scoped checks.
