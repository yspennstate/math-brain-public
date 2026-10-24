# HARD7-05 route note — four-cycle sign census + fourth-moment Temple bound

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

This note is intentionally written **before** constructing the exact checker. The preceding degree-24 edge-Ritz certificate reached `theta_{2,1/4}>0.148`; its quasimode is already extremely accurate (`mu≈0.874089735`, residual squared `≈1.54954e-4`). The evident waste is not the trial polynomial but the use of `tr(T^2)` to bound every non-Perron eigenvalue.

New triple: **B23 / B25 / B26**.

- **B23 (do what the proposer did not expect):** assume the degree-24 quasimode is already good enough and attack the *certificate tail* rather than optimizing the quasimode again.
- **B25 (count the same thing twice):** compute the four-edge Gaussian-loop cone probability once by a complete sign-pattern census and once from the bivariate orthant formula for two adjacent edge sums.
- **B26 (hunt the sporadic case):** the four-cycle is exceptional because its four edge sums satisfy one alternating linear relation. The two alternating sign patterns are therefore impossible, and this closes the cone probability exactly.

Let `T=T_{4/5}` be the self-adjoint edge operator from the previous checkpoint and let `(X_0,...,X_3)` be the normalized four-step Gaussian loop appearing in the trace formula. Put `S_i=X_i+X_{i+1}` cyclically. Then

`S_0-S_1+S_2-S_3=0`, equivalently `S_0+S_2=S_1+S_3`.

Write `a=P(S_0,S_1,S_2,S_3<0)`, let `b` be the probability of a specified exactly-three-negative sign pattern, and let `c` be the probability of a specified adjacent exactly-two-negative pattern. Cyclic symmetry and sign reversal give

`2a+8b+4c=1`,

because the two alternating two-negative patterns are impossible. Also

`p:=P(S_0<0,S_1<0)=a+2b+c`.

Hence exactly `a=2p-1/2`. For a centered bivariate Gaussian pair with correlation `rho`, `p=1/4+asin(rho)/(2*pi)`, so

`a=asin(rho)/pi`.

For the four-step loop at `r=4/5`, direct covariance algebra gives `rho=41/42`. Therefore the proposed exact fourth trace is

`tr(T^4) = (625/369) * asin(41/42)/pi`.

This should be dramatically sharper than `tr(T^2)=25/18` for bounding the non-Perron spectral tail. The target is the clean threshold

`x_*= (4/5)^(3/5)`,

because `lambda_1<x_*` implies

`theta_{2,1/4}> -log(x_*)/(4 log(5/4)) = 3/20`.

The intended contradiction is a fourth-moment Temple bound. If `lambda_1>=x`, then

`max_{j>=2}|lambda_j|^4 <= tr(T^4)-x^4`.

If this makes every non-top eigenvalue `< beta < mu`, the spectral identity gives

`epsilon^2 >= (lambda_1-mu)(mu-beta)`.

I will now test whether exact rational enclosures around the previous certified `(mu,epsilon^2)` and the exact four-cycle trace produce a positive margin at a rational `x<x_*`. If the margin fails, this route is abandoned rather than manufacturing another checker for the old bound.