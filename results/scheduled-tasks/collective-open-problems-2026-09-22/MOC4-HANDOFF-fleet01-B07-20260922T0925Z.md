# MOC4 source-bound handoff — fleet01/B07 — covariance commutator closure

Outcome: **ESSENTIAL_STEP_APPLIED**. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**. Execution remains `WITHOUT_VERIFIED_BRAIN`.

Canonical immutable scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/fleet01/B07/20260922T090511Z-b07-moc4-r11-29b5bc/REPORT.md`, creation commit `895f70e83701d4237510e7b8eb9a476126df8e51`, report blob `1667b6e83ade4cbc78c67c8a628dd4c8eba32b65`.

## Dependencies consumed

- Latest complete campaign lead: fleet03/B07 r13, `MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1` + `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`, shared handoff commit `73578304570fda959a94d9788b739fe9690586cd`. It gives the generic positive-gap split MSQR/NDI and, on a mixed-Schur kernel, full-Hessian annihilation plus a nonnegative cross-split Schur-complement reserve.
- Assigned OTHER-account partner: fleet02/B08 `MOC4-2PLUS2-EVC-TRANSVERSAL-CLOSURE-v1`, run `B08-20260922T053946Z-bf1307`, report blob `a361d4996c79854aa569c85a83b94ea43367b66d`; it closes the exact-four `2+2` common-block face outside its explicit double-interlacing chamber. No later completed fleet02/B08 result was visible at final peer scan.
- Immediate predecessor: fleet01/B07 `MOC4-EXACT-SPECTRAL-COVARIANCE-RECONSTRUCTION-v1`, which isolated the covariance cross-inner-product as the missing local datum.

## New exact theorem

For one block row of `O=Lambda^2 U`, put

`V_beta=tf(B_beta B_beta^T)`, `rho(V)^2=tr(V^2)/2`, so `sum_beta V_beta=0`.

For coefficient vectors `c,d`, write `W(c)=sum c_beta V_beta`, `W(d)=sum d_beta V_beta`, and `S=[c;d](I-11^T/3)[c;d]^T`. Then

`rho(W(c))^2 rho(W(d))^2 - <W(c),W(d)>_rho^2`

`= (3 det S / 8) ||[V_1,V_2]||_F^2`.

This is `MOC4-COVARIANCE-COMMUTATOR-CLOSURE-v1`. The identical column theorem holds with `tf(B^T B)`.

Writing `q_beta=rho(V_beta)^2=R_beta^2-D_beta^2`, the cross-angle is explicitly

`<W(c),W(d)> = ar q_1 + bs q_2 + (as+br)(q_3-q_1-q_2)/2`,

where `a=c1-c3`, `b=c2-c3`, `r=d1-d3`, `s=d2-d3`. Hence the previously missing cross-inner-product is fully determined by the three observable nonconformality variables.

The row-local ceiling also has an exact slack decomposition. If `u=rho(W(c))<=U`, `v=rho(W(d))<=V`, `t=<W(c),W(d)>`, and `G=S^{-1}`, then with `eps=sign(G12)`,

`B-E = G11(U^2-u^2)+G22(V^2-v^2)+2|G12|(UV-uv)+2|G12|(uv-eps t)`.

The last term obeys

`2|G12|(uv-eps t) >= (3|G12| det S/(8uv)) ||[V_1,V_2]||_F^2`,

so every noncommuting covariance row/column supplies a strict quantitative reserve.

## Genuine true-unitary sharpness/no-go

This local reserve cannot be forced positive by genericity. For every real `U in SO(4)`, `Lambda^2 U` commutes with the Hodge star; in the signed complementary-pair basis every `2 x 2` block is `[[m,n],[n,m]]`. Thus all row and column covariance defects commute.

An exact rational `SO(4)` witness in the canonical report has all 16 entries nonzero, all 36 two-minors nonzero, all nine exterior blocks invertible and nonconformal, yet every row/column covariance commutator is exactly zero. Therefore the implication `generic true-unitary interior => positive covariance-commutator reserve` is false. This refutes only that proof mechanism, not MOC4.

## First surviving implication

`MOC4-GLOBAL-COMMUTING-COVARIANCE-PAYMENT-v1`: at a positive-gap global maximizer, either a row/column commutator reserve plus current subgroup/Hessian roofs pays the gap, or the covariance triples commute and their common singular-axis structure must be combined with the lead's full-Hessian cross-split equations on MSQR (or the six negative-definite pair blocks on NDI) to force target safety.

In particular on MSQR, express the lead cross residual `r` in these covariance variables and prove `r=0` plus covariance commutation forces a safe Spin(4)/boundary configuration, while `r!=0` yields a strictly positive global Schur-complement reserve. Another row-local norm/angle inequality cannot close the target uniformly.

No target-level proof or target-level counterexample is claimed.
