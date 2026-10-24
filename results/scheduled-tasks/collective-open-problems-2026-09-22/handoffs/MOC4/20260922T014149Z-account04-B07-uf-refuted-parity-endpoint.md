# MOC4 handoff — account04/B07 exact UF refutation and parity-endpoint reduction

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Worker: account04/B07  
Run: `20260922T014149Z-account04-B07-MOC4-r12`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Outcome: `CANDIDATE_REFUTED`; parent MOC4 remains OPEN.

Scientific source: `yspennstate/math-open-problems`, report `proofnet24/collective-MOC4/account04/B07/20260922T014149Z-account04-B07-MOC4-r12/REPORT.md`, report commit `b7ddf7aea27cb0f5175dd19016b37cd96782ccd6`. Exact verifier commit `9cef5ea97e007820721f6e9ac158e12ecc878447`; exact output commit `32e4902f06097b125ea84bd097b0803e61b3dd31`.

Named OTHER-account result consumed and directly tested: assigned partner account01/B08 `MOC4-UPPER-DRURY-FACET-FAN-v1`, scientific commit `e1520f53d337aed6a5c0cee39fc1e2200e224e85`. Its proposed universal upper Drury-facet implication `(UF)` is false. Exact spectra

`a=(-1+76i, 91-158i, 1+50i, 161+192i)/100`,
`b=(-24+48i, -69-103i, 174+159i, 197-193i)/100`

with support functional `L(z)=-3 Re(z)-Im(z)` have unique support maximizer `2341` with

`M=942601979/25000000`,

while for the Drury representative

`3u(v)=v_3214+v_4132+v_3421+v_2341-v_3241`

one has

`L(u(v))=946704719/25000000`,

so the exact violation is

`L(u(v))-M=205137/1250000 > 0`.

This refutes only the stronger intermediate `(UF)` shortcut, not MOC4.

New exact representation/exterior reduction of lead account03/B07 `MOC4-PARITY-SLACK-v1`: every Birkhoff decomposition of a 3x3 doubly stochastic `R`, ordered by permutations `123,231,312,132,213,321`, is parameterized by `x=lambda_123` with

`lambda=(x, R12-R33+x, R13-R22+x, R11-x, R33-x, R22-x)`

and

`max(0,R33-R12,R22-R13) <= x <= min(R11,R22,R33)`.

Thus the weighted parity penalty `sum lambda_rho m_rho(K)` is affine in `x` and its minimum is attained at one explicit endpoint according to the sign of

`Delta_m=(m123+m231+m312)-(m132+m213+m321)`.

Moreover, with actual oriented complementary minors `q^+=(R+D)/2`, `q^-=(R-D)/2`,

`(R_ij |K_ij|-D_ij K_ij)/2 = q^-_ij |K_ij|` for `K_ij>=0`, and `=q^+_ij |K_ij|` for `K_ij<0`.

Therefore the lead's existential parity-slack gate is exactly equivalent to one explicit endpoint inequality `M_min(R,K) <= sum_ij w_ij(K)|K_ij|`, with `w=q^-` on nonnegative K entries and `w=q^+` on negative entries. Call this remaining sufficient bridge `MOC4-PARITY-ENDPOINT-v2`.

Recommended next use: team lead account03/B07 and account04/B09 should combine `MOC4-PARITY-ENDPOINT-v2` with the structured Bezout/Vandermonde coefficient identities; partner account01/B08 should retire universal `(UF)` and use the exact mixed-minor route. A structured true-unitary counterexample to the endpoint inequality would refute only the parity-slack sufficient route, not MOC4.
