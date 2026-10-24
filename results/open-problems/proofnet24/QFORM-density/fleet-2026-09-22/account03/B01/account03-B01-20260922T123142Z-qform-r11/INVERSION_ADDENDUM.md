# Addendum: rigorous inversion for the averaged-frequency theorem

This addendum belongs to run `account03-B01-20260922T123142Z-qform-r11` and the theorem `QFORM-DIFFUSE-AVERAGED-LP-v1` in `REPORT.md`.

The `q=1` case uses ordinary Fourier inversion and yields a bounded continuous density. For the new rank-two case one has `1<q<=2`, so `phi_T` need not be integrable and the notation `p_T=(2pi)^(-1) hat(phi_T)(-x)` must be understood through the Hausdorff--Young extension rather than pointwise Fourier inversion. Here is the complete justification.

Let `mu` be the probability law of `T` and `phi(t)=int exp(i t x) dmu(x)`. Assume `phi in L^q(R)` for some `1<q<=2`, and let `p=q/(q-1)`. Hausdorff--Young defines an inverse Fourier transform `g in L^p(R)` with

`||g||_p <= (2pi)^(-1/q)||phi||_q`.

To identify `g dx` with `mu`, take any Schwartz function `psi`. Fourier inversion for `psi`, followed by Fubini (permitted because `hat psi in L^1` and `|phi|<=1`), gives

`int psi(x) dmu(x) = (2pi)^(-1) int hat psi(t) phi(t) dt`,

up to the harmless sign convention in `hat psi`. By the defining duality of the Hausdorff--Young inverse transform, the right-hand side equals

`int psi(x) g(x) dx`.

Therefore `mu` and `g(x)dx` are equal as tempered distributions, hence as finite Borel measures. Thus `mu` is absolutely continuous with density `g in L^p`, and the Hausdorff--Young norm estimate in the report is rigorous.

Equivalently one may insert the Gaussian multiplier `exp(-epsilon t^2)`, obtain smooth densities for `mu` convolved with a Gaussian, use the same uniform `L^p` bound, and pass weakly in `L^p`; the distributional argument above is shorter and keeps the constant unchanged.

No continuity of `g` is claimed for the rank-two `L^p` theorem. Continuity is asserted only after convolution with the independent square in Corollary `QFORM-DIFFUSE-RANK2-PLUS-SQUARE-v1`, where standard `L^3 * L^(3/2)` translation-continuity gives a continuous function vanishing at infinity.
