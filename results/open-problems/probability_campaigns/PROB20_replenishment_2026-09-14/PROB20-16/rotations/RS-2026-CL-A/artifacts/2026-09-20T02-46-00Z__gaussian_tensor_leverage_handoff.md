# RS-2026-CL-A cross-role handoff — Gaussian/Hermite leverage trimming

Source ownership remains with `RS-2026-CL-A` / native ID `6aa7b4b639a08191b893e2b7dd6cdf59`. This note is a reusable lemma for registered probability roles **P08 Gaussian Phase Retrieval** and **P09 Gaussian Tensor Bounds**; it is not a claim on either source problem.

## 1. Generic contamination transfer

For a null law `Q` and centered degree-`<=D` polynomial space `V_D^0`, let `{phi_j}` be any `L2(Q)`-orthonormal basis and

`kappa_D(x)=sum_j phi_j(x)^2`.

If

`P=(1-eps)P^circ+eps H`,

then

`Adv_Q^{<=D}(P^circ,Q)`

`<= [Adv_Q^{<=D}(P,Q)+eps(E_H kappa_D)^(1/2)]/(1-eps)`.

Thus a bad event/component may be discarded without losing the source low-degree hypothesis whenever

`eps(E_H kappa_D)^(1/2)=o(1)`.

This is sharp for point-mass contamination: `sup_{||f||_Q=1,f in V_D^0}|f(x)|=sqrt(kappa_D(x))`.

## 2. Exact Gaussian leverage bound from Mehler

Let `Q=gamma_m=N(0,I_m)`. With normalized probabilists' Hermites

`h_alpha(x)=He_alpha(x)/sqrt(alpha!)`,

the total-degree Christoffel/leverage function is

`kappa_{m,D}(x)=sum_{1<=|alpha|<=D} h_alpha(x)^2`.

For every `rho in (0,1)`, classical Mehler gives the diagonal identity

`sum_{alpha>=0} rho^{|alpha|}h_alpha(x)^2`

`=(1-rho^2)^(-m/2) exp(rho||x||^2/(1+rho))`.

Since `rho^{|alpha|}>=rho^D` for `|alpha|<=D`,

`1+kappa_{m,D}(x)`

`<= rho^{-D}(1-rho^2)^(-m/2) exp(rho||x||^2/(1+rho))`.

Therefore for an exceptional component `H`,

`E_H kappa_{m,D}`

`<= rho^{-D}(1-rho^2)^(-m/2) E_H exp(rho||X||^2/(1+rho))`.

This is directly compatible with Gaussian norm/singular-value truncations: choose the bad event, compute its mass `eps`, and optimize `rho` so that

`eps * rho^{-D/2}(1-rho^2)^(-m/4)`

`* [E_H exp(rho||X||^2/(1+rho))]^(1/2) ->0`.

Then low-degree signal of the dominant core is inherited from the original pair, while all difficult tail estimates may be proved only on the core.

## 3. Suggested use in P08/P09

- **P08:** if a hard-edge argument introduces rare common-core or conditioning failures with huge likelihood ratios, do not force global `L2`/Renyi control on those failures. Trim them, bound their probability and Hermite leverage, then keep the dependence calculation on the dominant Gaussian core.
- **P09:** in tensor chaining/decoupling, rare large Gaussian norm or bad contraction events can be removed if their probability beats the degree-`D` Hermite leverage. The Mehler formula gives a clean quantitative test before spending effort on global high-moment bounds.

The result is especially useful when the exceptional event is negligible in total variation but destroys every fixed-order `L^r` bound. It complements, rather than replaces, each role's source-specific Gaussian estimates.

Prior art: Mehler's formula and Christoffel/leverage functions are classical; see Pauwels--Bach--Vert, arXiv:1805.07943 for the leverage/Christoffel connection. The source-directed trimming application is from the current RS-2026-CL-A proof line. Novelty is not asserted.