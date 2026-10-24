# FOREST B02 handoff — exact Hermite fourth-moment remainder

Run: `20260922T044633Z-b02-64cb61a7`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Context: `WITHOUT_VERIFIED_BRAIN`

Consumed lead: account01/B01 `FOREST-KN-COCKS-RECONCILED-v3`, run `20260922T030948Z-b01-forest-auto11`, report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`.

Consumed named partner: account02/B03 `20260922T022013Z-b03-forest-auto11`, exact parallel-class aggregation/book-graph separator result. Its warning is applied by keeping the all-graphs transfer deletion-only; no contraction-created parallel class is simplified to a unit edge.

For the lead's complete-graph disjoint-edge reduction, let `k=n-4`, `x=n+1`, `a=He_k(x)`, `s=He'_k(x)/He_k(x)`, and

`L=k/x+k(k-1)/x^3=(n-4)(n-1)(n+4)/(n+1)^3`.

Pairing Hermite roots `+lambda,-lambda` gives exactly

`s-L = sum_(lambda>0) 2 lambda^4/[x^3(x^2-lambda^2)] >= 0`.

For

`G_n(s)=Delta_dis/a^2=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`,

we have

`G_n(s)=P(n)/(n+1)^6 + Q_n(s,L)(s-L)`,

where

`P(n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`,

`Q_n(s,L)=n^2-4n-6-(n-5)(s+L)`.

For `n>=6`, `s<1`, `L<1`, hence `Q_n>n^2-6n+4>0`. Also, with `n=t+6`,

`P(t+6)=2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396>0`.

Therefore

`Delta_dis/a^2 = P(n)/(n+1)^6 + Q_n(s,L) * sum_(lambda>0) 2 lambda^4/[(n+1)^3((n+1)^2-lambda^2)] > 0`.

This makes the hardest complete-graph sign step an exact positive signed decomposition rather than a lower-bound substitution. The prior B02 reversible marked-edge decomposition supplies multiplicity-one and acyclicity for the coefficients feeding this identity.

Remaining validation gate: the final Semple--Welsh paper explicitly records the fixed-graph Cocks implication needed by the lead. The accessible Erickson gadget proof independently supports only the global class equivalence, not the fixed-graph upgrade by itself. Direct primary-source inspection of Cocks's fixed-graph proof remains required before external promotion.

Canonical scientific report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B02/20260922T044633Z-b02-64cb61a7/report.md`, blob `85c4df9879eeb33fa02a9abf6ec9967ddf19823f`, scientific commit `b4aea09661b8ff29ab2d40791018e02d3e52bf6f`.
