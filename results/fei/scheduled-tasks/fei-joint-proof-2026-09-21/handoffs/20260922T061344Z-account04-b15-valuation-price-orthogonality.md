# FEI handoff — valuation tails do not recover coordinate-price KL

Source scientific report: `yspennstate/math-open-problems` commit `a51468ea0f41b6259dedecb6df01db749bc0aeef`, path `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T061344Z-zero-valuation-price-orthogonality/REPORT.md`, report blob `886d4445c63099fefe84ad11314bd2a83b5fe229`.

Consumed source: account02/B15 `20260922T054027Z-packet-price-kl-numaro/REPORT.md`, report blob `8f6afebd4c7f6ba33533a660e380fd06aefe6488`.

Exact live balanced source expression retained:

`H = H(K) + C_coll - D_mag - D_price|mag`, so the current balanced all-gate payment is

`H(K) + C_coll - D_mag - D_price|mag <= C_* (I-1)`.

New exact cell identity: within a fixed `(level, Fourier magnitude)` cell, the actual source is uniform and the `q`-weighted reference is proportional to `L(A)=prod_{i in A} q_i`; hence

`D_price(cell) = log_2( AM_C(L) / GM_C(L) )`.

New Boolean obstruction: the balanced four-bit gate with negative truth-table set `{0,1,2,3,4,5,6,8}` has exact Walsh vector

`(0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0)`,

influences `(1/4,1/4,1/4,3/4)`, and normalized occurrence law `(1/6,1/6,1/6,1/2)`. Both signed magnitude-packet valuations are exactly zero, so every positive valuation-tail reserve from the account02 theorem vanishes. Nevertheless the `(k=3, |W|=4)` cell has source law `(1/4)^4` and price-reference law `(1/10,3/10,3/10,3/10)`, yielding

`D_price|mag = (1/4) log_2 5 - 1/4 - (3/16) log_2 3 = 0.033301554836624... > 0`.

The same gate is disjoint-composition-prime by an exact row-pattern certificate: every coordinate subset of size two or three produces at least three distinct complement rows. It is very safe for the live all-gate candidate (`c_G=-8.0838625...` at uniform bias), so this is a proof-transfer obstruction, not an FEI counterexample.

Converse separation: even-variable bent functions have packet valuation `m/2` but `D_price|mag=0` because `q_i=1/m` and price is constant on every level. Thus valuation depth and coordinate-price relative entropy are genuinely distinct currencies in both directions.

Implication: account02's valuation tails can pay the signed arithmetic reserve but cannot themselves certify the indispensable coordinate-price KL. A surviving source-exact argument must retain direct price dispersion/hazards (and any unspent conditional KL) separately. Do not collapse `D_price|mag` into valuation depth.

Status: `CANDIDATE_REFUTED / SOURCE_PRICE_CREDIT_SEPARATED`; full FEI remains OPEN. Execution `WITHOUT_VERIFIED_BRAIN`. No novelty claim.
