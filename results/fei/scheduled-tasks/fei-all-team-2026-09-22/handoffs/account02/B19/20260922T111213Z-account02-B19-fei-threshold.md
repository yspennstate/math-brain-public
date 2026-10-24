# FEI handoff — account02/B19 threshold-flexible terminal proof

Run `20260922T111213Z-account02-B19-fei-threshold`; classification `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`; recipient `account04/B20`; named partner consumed `account03/B19` bundle `yspennstate/math-open-problems@144ea823b604785a77b638b03b0c5d7909676d52`, report blob `c291157149243f0d2dcb73640be652db670ff393`.

Canonical B19 science bundle: `yspennstate/math-open-problems@57a1d59cac73a9ef03bc65a24d9832b4ae6548ff`, root `proofnet24/P03-fei/fleet-2026-09-22/account02/B19/20260922T111213Z-account02-B19-fei-threshold/`; immutable main report blob `f0d5d9c91e6e6f6f6ae7c1a331c3a6952c85c09c`, claims blob `28c5a3e1dfc62dc93dddeda84e6306b0dfdbe5ab`. Checker SHA-256 `263fff5316f415922d30b4d22993aa276901eeb345fcb8c093b298c2441b1a0f`; output SHA-256 `735002dc0b48ac2281b59d1c0db5bb4fa5be046f3e1b2d17979cf19f8a2f6f81`.

New theorem: for every finite `K>2`, if `a_K` solves `h2(a_K)=K a_K` and `lambda_K=log2(1+2^-K)/(K+j'(a_K))`, then every genuine ratio-`rho>K` minimum-dimensional core obeys `sigma_K(q_i)<=lambda_K[K+j'(q_i)]`, hence

`sum sigma_K d <= (lambda_K/2)(P-DTC)+(lambda_K/4)U_K`

and at robust-row parameter `eta=1/16`,

`sum_R q_i^2[K+j'(q_i)] <= (128 lambda_K/105)(P-DTC)+(64 lambda_K/105)U_K`.

At `K=8`, `lambda_8=0.000517684914618024...`, so the hidden coefficient is `0.000315541281290986...`. This is a reduction, not FEI closure.

All-finite-K barrier: for integer `d>=max(6,ceil(K+3))`, the `d`-bit one-point defect is strictly all-block `K`-terminal; its tensor powers have `U_K/J -> infinity`. A one-point surgery makes sufficiently large powers tensor-primitive while preserving strict `K`-terminality and the divergence. These functions are not asserted ratio-critical.

Partner application: on the exact tensor cross-factor bulk, `s=q^2`, `omega=4q^2`, while the account03/B19 I-projection baseline satisfies `b=(c/v)q^2>=q^2`; therefore the partner positive-excess charge `Psi_b(omega)` is exactly zero there. The obstacle is the conditional-product baseline, not unpaid above-baseline KL.

Exact next implication for recipient: use full ratio-extremality to eliminate/monetize the I-projection baseline or force physical ratio descent, and construct a realizable adaptive nonreused selector for any above-baseline excess; the small/nonrobust branch must be included or separately closed. Do not use a universal fixed positive `K_occ` reserve: late correction event `FEI-B01-FIXED-CREDIT-RESERVE-NOGO-v1` refutes that stronger invariant and has been consumed.

Execution status: `WITHOUT_VERIFIED_BRAIN`; full FEI remains open.
