# FEI handoff — account04/B12 complementary-MUX address tube

Source scientific report:
`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T0612Z-complementary-mux-address-tube/REPORT.md`

Scientific report commit: `bdf543f8ef2b8d6a48491a5276b6a2cfc59fc549`; complete package head after checker/output: `1dc187f9a6cc68a6d2dfbdc10ba75cbea655ec0c`.

## Proved

For the fixed live candidate `Gamma^dagger`, on the one-bit MUX with complementary data biases `q_1=1-q_0`, write `m=min(q_0,1-q_0)` and address bias `t`. The exact six-mass law admits the entropy identity

`H_tau-H_0 = A h_2(4 tau^2) + V [H(rho_tau)-2]`,

so the four data atoms contribute a nonpositive correction and no six-letter Fannes payment is needed. Consuming account02/B12's quantitative balanced-address complementary-MUX theorem and account02/B14's source-valid center Lipschitz bound gives

`D_tau >= F(m) - 120(1-m)^2 |tau| + (V/2) h_2(4 tau^2)`.

Hence the live gate inequality holds whenever either

- `0<m<=2^-11` and `|t-1/2|<=m/64`, with `D>41m/40`; or
- `2^-11<=m<=1/2` and `|t-1/2|<=2^-14`, with `D>17/2048`.

For the owner's comparable base-potential margin this entire new tube satisfies `c_M < 0.201798606`.

## Dependencies and limitation

Consumed account02/B12 `20260922T045519Z-complementary-mux-fourstep` for `F(m)>(29/10)m` near the endpoints and `F(m)>1/64` on the compact branch; consumed the newest compatible account02/B14 zero-credit MUX tube for `|Gamma^dagger(1/2+x)-C^dagger|<=60|x|` on `|x|<=2^-14`.

Full FEI remains OPEN / NOT PROVED. The result is a restricted MUX theorem. The account04/B18 mixed-curvature identity is preserved separately; no `sum d_k=O(J)` claim is used or implied. Execution is `WITHOUT_VERIFIED_BRAIN`.
