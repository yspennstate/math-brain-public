# account02/B18 handoff — fixed multiplicity audit

Run: `20260924T2105Z-account02-B18-fixedmult-auto11`.

Historical source pin: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Current nine source pin: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, paper blob `19fb119877426b640b2c0dae19ec2f78a399fe11`, SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`.

Verdict: historical s17/10000 and current s9/400 are PASS after one local hyperbolic-tail proof-text repair: the negative tail must choose its own large original coordinate. The witness to the written inference is `u=(rho,0), w=(0,rho)`; constants are unchanged.

Primary-source transfer checked: Rudelson--Vershynin Thm 1.2 gives the sharp scalar `sqrt(2)K` cap under exactly independent bounded-density hypotheses; Livshyts--Paouris--Pivovarov Thm 1.1 gives cap-one q-dimensional product marginals `<=2^(q/2)`; no projected independence is inferred.

New complete B18 replacement proof: with inner half-potential parameters `d=11/40,p=9/1000,h=107/1000` and outer parameters
`eta=16333/500000`, `kappa=56351/10000000`,
[
s_8(A)ge s>0Longrightarrow |p_Q|_{infty,mathrm{ess}}<rac{7262}{25}rac{K^2}{s}=290.48,K^2/s.
]
The proof closes scalar/definite/indefinite pivots, large V3 by the source-sharpened `6^(4/3) Z3^(-1/6)` receiver, and small V3 by robust two-anchor aggregation, two-high leverage exclusion, one-exception completion and product-safe incident third volume. Exact thin margins were recomputed as positive.

Status: mathematically complete B18 candidate; another genuinely separate end-to-end review is still required for owner-level validation of the exact 290.48 retuning. Multiplicity seven remains OPEN at a dependence-safe shared-coordinate overlap receiver. The unrestricted three-eigenvalue QFORM conjecture remains OPEN.

Persistent substantive writes to math-open-problems were blocked by the platform safety guard. Local read-back artifacts have SHA-256:
- audit: `990d10019cc859f12bb7badb88e4c36455048d8c51adc5146dcdc668064fcc7a`;
- s8 replacement: `9f199641dd0701a7ecdc6827c488f8e2d4dc6e6e9c53661fa2aa5d802bdb7db8`.
