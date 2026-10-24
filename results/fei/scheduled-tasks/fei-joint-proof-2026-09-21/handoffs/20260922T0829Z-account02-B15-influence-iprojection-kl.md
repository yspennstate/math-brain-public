# account02/B15 FEI handoff — exact original-coordinate influence I-projection

Run: `20260922T0829Z-account02-B15-r11`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full unrestricted FEI: **OPEN**.

Scientific source: `yspennstate/math-open-problems`, report commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, report path `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`, report blob `5ce14eaaec34f0d91f2d430dba576e19dddc6894`.

Named peer consumed: account04/B15 `20260922T081139Z-bellman-packet-split` (report blob `f0dfc81f9de9df69cbcb5ca710312131a4a2b57f`). The scalar Bellman/packet split is refined, not contradicted.

For every nonempty spectral law `P=w+`, let `r_i=P(i in S)=It_i/v`. There is a unique maximum-entropy conditional-product law `Q_r` with these exact original-coordinate marginals. If `mu=sum r_i>1`, let `c` be the positive solution of

`1-c = product_i (1-c r_i)`.

Then `Q_r` is obtained by independent Bernoulli probabilities `c r_i` conditioned on nonempty, and

`Hmax(r) = [sum_i h2(c r_i)-h2(c)]/c`.

The exact negative credit is

`K_occ = D_2(w+ || Q_r) = Hmax(r)-H(w+)`.

For every conditional-product Gibbs reference `nu_Gamma+`, the full KL has the exact Pythagorean split

`D_2(w+||nu_Gamma+) = K_occ + D_2(Q_r||nu_Gamma+)`.

Thus the second term is **exactly paid by the actual normalized coordinate influences**; `K_occ` is the only product-reference KL not explainable by any original-coordinate first-moment tilt and is independent of the chosen potential.

For arbitrary symmetric `Gamma`, with `a_i=[Gamma(p_i)+h2(V_i)]/V_i` and `a_q=[Gamma(q)+h2(v)]/v`, the normalized all-gate residual is

`R_Gamma = B_inf^Gamma + K_occ`,

`B_inf^Gamma = sum_i r_i a_i - a_q - Hmax(r)`.

Hence any genuine violating gate must satisfy

`K_occ < -B_inf^Gamma`

and Pinsker forces

`TV(w+,Q_r) < sqrt((ln 2 / 2)(-B_inf^Gamma))`.

This reduces the surviving Shannon problem to quantitative Boolean rigidity inside a near-conditional-product spectral corridor, with signed convolution still required.

Exact peer applications: on dictator plus dummies, `K_occ=0`, so the peer's unbounded `log2 k` packet/shape credit is entirely coordinate-influence payment. On the peer's four-bit composition-prime witness with influences `(1/4,1/4,1/4,3/4)` and all signed valuation tails zero, the scalar-mean max-entropy relaxation loses a strict influence-anisotropy KL. High-precision sanity values are `K_occ=0.801287937850462...` and anisotropy payment `0.468283060030105...`; analytic strict positivity does not depend on those decimals.

The fixed `Gamma^dagger` seed is already refuted by newer prime-gate work; this theorem is potential-independent and is intended for the Bellman-repair architecture, not as revival of that fixed candidate.
