# B14 r39 early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`; full target remains open.

## First unpaid implication

`QFORM-FINAL-CAP-BEFORE-FRACTIONAL-SCALE-v1`: after arbitrary random translation labels are averaged for the full Gaussian-mixture theorem, the k=3 endpoint still pays the fractional component-scale moment `E T^{-1/3}`. Either replace that reciprocal scale by a quantity controlled by the final rough cap-one marginal, with no fragment/support/moment parameter, or force a whole-law QFORM certificate before active component normalization.

## Center labels are exactly zero-tax

For the proved full Gaussian-mixture theorem, condition on `T=(T_i)` but not the random centers. Its conditional Gaussian calculation gives, for every center vector `M`,

`||p_{Q|M,T}||_infinity <= I_k/(2 pi) W_k(T)^(-1/(2k))`,

where `W_k(T)=e_k((D^(1/2) A D^(1/2))^2)` and the right side is independent of `M`. Averaging the conditional laws in `M` therefore gives

`||p_{Q|T}||_infinity <= I_k/(2 pi) W_k(T)^(-1/(2k))`,

and hence

`||p_Q||_infinity <= I_k/(2 pi) E W_k(T)^(-1/(2k))`.

Thus arbitrary component-center translations, including arbitrarily remote and T-dependent centers inside each coordinate pair, cost exactly zero before reciprocal scale is paid.

For `A=I_3`, `W_3=(T_1 T_2 T_3)^2`, so independence across coordinate pairs yields

`||p_Q||_infinity <= I_3/(2 pi) prod_i E T_i^(-1/3)`.

This is strictly weaker than the theorem's sufficient inverse-half-scale hypothesis and isolates the actual k=3 rough-law debt.

## Fractional Besov obstruction at exactly the required exponent

Let `g(x)=E phi_T(x-M)` be any one-dimensional Gaussian location-scale mixture, with arbitrary dependence between `M,T`. For `0<s<1`,

`||tau_h phi_T-phi_T||_1 = 4 Phi(|h|/(2 sqrt(T)))-2 <= min(2, sqrt(2/pi)|h| T^(-1/2))`.

Since `min(2,x) <= 2^(1-s) x^s`, averaging gives

`||tau_h g-g||_1 <= C_s |h|^s E T^(-s/2)`,

`C_s=2^(1-s)(2/pi)^(s/2)`.

At `s=2/3`,

`||tau_h g-g||_1 <= (4/pi)^(1/3)|h|^(2/3) E T^(-1/3)`.

Now set

`E_N = union_{j=1}^N [4j,4j+1/N]`, `f_N=1_{E_N}`, `h_N=1/(2N)`.

The components remain disjoint after this shift and

`||tau_{h_N} f_N-f_N||_1=1` exactly. Therefore, if `delta=||g-f_N||_1<1/2`, translation invariance and the triangle inequality give

`1-2 delta <= ||tau_{h_N}g-g||_1 <= pi^(-1/3) N^(-2/3) E T^(-1/3)`,

so

`E T^(-1/3) >= pi^(1/3) N^(2/3)(1-2 delta)`.

For three independent Gaussian-mixture approximants to the three copies of `f_N`, the center-aggregated `A=I_3` certificate is therefore forced to be at least

`(I_3/2) N^2 (1-2 delta)^3`,

where `I_3/2=1.471234099084729...`. Hence averaging random centers repairs the translation loss completely, but no L1 approximation of arbitrary finite-fragment cap-one extremes can keep the remaining k=3 fractional-scale certificate uniformly bounded.

This is a proof-interface obstruction, not a QFORM counterexample or an output-density lower bound.