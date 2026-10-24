# Addendum — latest completed account03/B12 result consumed

This addendum is part of run `account02-B12-20260922T141839Z-7c88d8ee`. It was created after the main immutable report because a newer completed partner artifact became visible before finish.

Newest partner source actually read:

`yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`.

The compatible statements used are:

1. `QFORM-PIVOT-E2-CROSS-v1`: after an original-coordinate scalar Schur pivot `a`, if the residual physical cross block `C` has range leverage at most `1/2` and `E_2=e_2(CC^T)>0`, then

   `||p_Q||_infinity <= 8.153 |a|^(-1/2) E_2^(-1/8)`.

   This is monotone under added residual singular directions through `E_2` and does not treat the remainder as an independent convolution.

2. `QFORM-TWO-SAMESIGN-THREEBLOCK-v1`: if a physical principal `3x3` block has two eigenvalues of one sign and magnitude at least `L`, with the third eigenvalue arbitrary, then

   `||p_Q||_infinity <= C_*/L`,

   `C_*=24.183038289961516...`,

   uniformly under arbitrary outside completion and cross coupling.

## Combined additional-eigenvalue interface

Together with Theorem 2.1 of the main report, there are now three source-valid ways to add arbitrary spectral directions without post-rotation independence:

- **diffuse physical core:** keep a leverage/exterior-power-certified principal core fixed and allow an arbitrary symmetric completion outside it;
- **localized same-sign core:** keep a physical `3x3` block with two same-sign eigenvalues at scale `L`; its third eigenvalue and the entire outside completion are arbitrary;
- **mixed pivot/cross packet:** after a physical scalar pivot, retain the aggregate rank-two cross energy `E_2`; any extra cross singular directions help rather than hurt.

These mechanisms are complementary to the main report's exact counterexample `QFORM-OPERATOR-NORM-RELATIVE-LINF-STABILITY-FALSE-v1`: they give **absolute geometric certificates** and therefore do not rely on false relative continuity of `||p_{X^TAX}||_infinity` in operator norm.

The newest partner also supplies exact overlap-channel bookkeeping

`M_0+M_1+M_2+M_3=e_3(A^2)>=1`

and an analytic payment for an individual overlap-one packet. The remaining target-level debt is now sharpened to **aggregate the dominant overlap channel before applying inverse local powers**. In particular, the `M_1` channel cannot be closed merely by selecting the largest pivot/minor, because determinant mass may be spread over many tiny packets. The main report's physical-completion theorem closes the completion step once a good packet/core is identified; the missing step is the dimension-free product-preserving aggregation/extraction from the global three-large-eigenvalue hypothesis.

Full QFORM remains OPEN / NOT PROVED.
