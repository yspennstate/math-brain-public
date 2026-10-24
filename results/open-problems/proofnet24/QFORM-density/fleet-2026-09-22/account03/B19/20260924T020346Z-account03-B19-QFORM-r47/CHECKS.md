# account03/B19 r47 deterministic checks

These computations are diagnostics only. Every theorem used in `REPORT.md` has an exact algebraic proof there; no Monte Carlo or floating computation is used as mathematical proof.

## Constants independently recomputed

- `E0=(55/128)^2=3025/16384=0.18463134765625`.
- E3 gate `eta=2^-64=5.421010862427522e-20`.
- In the `sigma_2>=1/64` branch,
  `sigma_1 sigma_2 > 28159/(4194304 sqrt(2)) = 0.00474725242887306`.
- In the `sigma_2<1/64` branch,
  `dist_F(N,rank<=1)<sqrt(2^-12+2^-32)=0.01562500745057882` and
  `sigma_1>sqrt(E0-2^-12-2^-32)=0.42940331484330596`.
- For the strong-top-four compiler with `beta=63/64`, `E>=E0` and `e3<2^-64`,
  `dist_F(W,rank<=2)<(4*2^-64/((63/64)*E0))^(1/4)=3.3049779278725826e-5`.
- At `beta=7/8`, the analogous deterministic number is `3.403742473585087e-5`.
- Designated account04/B19 gate:
  `34*sqrt(log(e*2^64))=228.99301519161452<229`.
- Designated account04/B19 moving-ridge barrier at `epsilon=2^-16`:
  `1/(9 epsilon)=2^16/9=7281.777777777777`.

## Randomized algebra diagnostics

Using independent pseudo-random nonnegative singular-square arrays (`seed=20260924`), 200,000 arrays of lengths 3 through 29 were checked against

`e3(p) >= (1/2) tau^2 (1-tau)`,

where `p` is normalized to sum one and `tau=sum_{j>=3}p_j`. There were zero violations. The minimum observed margin was approximately `1.90e-6`; the maximum observed RHS/LHS ratio was approximately `0.99857`.

Using independent random rectangular matrices and appended star rows (`seed=20260924`), 5,000 instances were checked against the exact identity

`e3([v;N][v;N]^T)-e3(NN^T)=||v||^2 e2((N P_{v^perp})(N P_{v^perp})^T)`.

The maximum normalized floating residual was approximately `6.65e-14`.

Terminal diagnostic marker: `QFORM_B19_R47_LEAFCURVATURE_ALIGNEDR2_CHECK_PASS`.
