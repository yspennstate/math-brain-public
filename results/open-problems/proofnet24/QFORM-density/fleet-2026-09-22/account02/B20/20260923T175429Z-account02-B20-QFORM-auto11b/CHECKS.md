# Checks for `QFORM-R5-124CORE-STRONGCAPTURE-OR-LIGHT3SINGULAR-v1`

Run `20260923T175429Z-account02-B20-QFORM-auto11b`.

## Exact constant check

With `tau=1/20`,

`c_tau=sqrt(19/20)(1-1/sqrt(20))-1/sqrt(20)`.

Using `sqrt(19/20)>97/100` and `1/sqrt(20)<9/40`,

`c_tau>2107/4000`.

Hence

`c_tau*(1597/2000)-403/2000
 > 1,752,879/8,000,000
 > 1,750,000/8,000,000
 = 7/32`.

Numerically the sharper value is

`c_tau = 0.5331276895538838...`,

`c_tau*(1597/2000)-403/2000 = 0.2242024601087762...`.

The claimed safe threshold `7/32=0.21875` therefore has margin `0.0054524601087762...`.

## Spectral identity check

For `S=U_L^T U_L`, the nonzero eigenvalues of

`S_0[L,L]=U_L Lambda U_L^T`

coincide with those of `S^(1/2) Lambda S^(1/2)`: first use the standard `XY/YX` nonzero-spectrum identity on `U_L Lambda U_L^T` versus `Lambda S`, and then on `Lambda S^(1/2) S^(1/2)` versus `S^(1/2) Lambda S^(1/2)`. Both endpoint matrices are real symmetric, so their nonzero singular values are the absolute values of the same nonzero eigenvalues. The lower bound on the third singular value is therefore legitimate even if `S` is singular.

## Source/probability audit

The strong/light dichotomy is deterministic coefficient geometry only. No projected random coordinate is used probabilistically. The only density payment in the new branch conditions the complement of a literal ORIGINAL-coordinate three-set and applies the pinned physical `3 x 3` theorem. No small random coefficient tail is deleted.

## Numerical regression (non-proof)

As a sanity test, random dimensions `r=3,4,5`, mixed-sign diagonal `Lambda`, and random PSD contractions `T` were generated and rescaled so that `||P T P||op<=1/20` on the top-three spectral subspace. Across 30,000 samples, the smallest observed ratio

`s_3(S^(1/2)Lambda S^(1/2))/s_3(Lambda)`

was about `0.9498`, safely above the proved universal coefficient `0.5331`. This regression is not used in the proof.
