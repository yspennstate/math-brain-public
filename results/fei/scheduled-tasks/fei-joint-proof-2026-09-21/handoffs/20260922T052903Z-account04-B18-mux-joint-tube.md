# account04/B18 handoff — joint unequal-data MUX tube

Status: `PROVED_AUXILIARY / FULL_FEI_OPEN / WITHOUT_VERIFIED_BRAIN`.

Canonical source:
`yspennstate/math-open-problems/proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260922T052903Z-mux-joint-tube/`

Consumed newest account01/B18 complementary-data address tube (blob `ce379eac385c9f388d2a72f5c10f3a0f6611fca9`) for the fixed candidate
`C^dagger=6.521851214`, `a^dagger=0.268204856`, `Gamma^dagger=Gamma0+a^dagger p(1-p)`.

For one-bit MUX `M(a,x0,x1)` the exact Poincare currency is

`W_M = V_t(V_0+V_1)/16`.

New proved enlargement: for every `0<q<=1/2`,

`|t-1/2| <= q^2/8192`, `q0=q`, `q1=1-q+eta`, `|eta|<=q^2/8192`,

we have

`D_{Gamma^dagger}(M;t,q,1-q+eta) > q/135 > 0`.

The requested gate margin relative to `Gamma0` therefore satisfies

`c_M < a^dagger - 16/1215 = 0.2550361317201646... < a^dagger`.

Mechanism: exact six-mass biased MUX spectrum + account04/B12 child-slack currency identity + source-valid Lipschitz bounds + Fannes continuity, spending at most `117 q / 8192` of account01/B18's `178 q / 8192` complementary-data reserve.

Still unpaid: full unequal-data MUX outside this quadratic tube; arbitrary composition-prime gates/all biases; full FEI. Do not promote this tube to universal closure. Existing zero-depth one-point classification and refuted blind-induction/depth-O(J) bridges remain unchanged.
