# r54 deterministic regression checks

These computations are regression evidence for the algebra in `REPORT.md`; they are not used in place of the analytic proof.

Seed: `20260924`.

For 5,000 random trials I generated an invertible symmetric `2 x 2` matrix `Lambda`, a vector `c`, scalar `a`, and `beta in [10^-6,10^-1]`, and formed

`K0=[[a,c^T],[c,Lambda]]`,

`K=[[K0,beta e1],[beta e1^T,0]]`.

Trials with `s3(K)<=beta` or numerically singular `K0` were skipped, leaving 4,988 admissible tests. I checked:

1. Weyl skeleton inequality `s3(K0)>=s3(K)-beta`.
2. Quadratic fourth-mode inequality `s4(K)*s3(K)/beta^2<=1`.
3. Strong Schur inequality
   `|sigma|>=(s3(K)-beta)*sqrt(1+||Lambda^-1 c||^2)`,
   where `sigma=a-c^T Lambda^-1 c`.
4. Exact block congruence
   `S^T K S = K0 direct_sum (-beta^2 e1^T K0^-1 e1)`
   with `S[:3,3]=-beta K0^-1 e1`.

Observed output:

- admissible tests: `4988`
- Weyl violations: `0`
- quadratic-s4 violations: `0`
- Schur-lower-bound violations: `0`
- maximum observed `s4(K)*s3(K)/beta^2`: `0.9999483451629798`
- minimum observed ratio of the left side to the Schur lower bound: `1.00005099571933`
- maximum absolute congruence-entry error: `1.1102230246251565e-15`

The near-one maximum in the fourth-mode ratio is consistent with sharpness of the analytic constant one.

Live constants independently evaluated:

`beta0=4*sqrt(2)*2^-20=5.3947966093944364e-6`,

`beta0^2=2.910383045673371e-11`,

`beta0/rho_*=0.008635075971933174`,

`128*64^(1/4)/(1-beta0)=362.04062510304914`,

`beta0/(1-beta0)=5.3948257133819034e-6`,

`beta0^2/(1-beta0)=2.910398746682662e-11`.

Regression status: `QFORM_B08_R54_QUADRATIC_S4_CHECK_PASS`.
