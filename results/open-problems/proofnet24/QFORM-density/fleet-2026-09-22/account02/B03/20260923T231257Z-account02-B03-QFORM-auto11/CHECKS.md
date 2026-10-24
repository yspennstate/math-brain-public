# Exact algebra checks for QFORM-CONJUGATE-DOUBLE-SINGULAR-PROMOTION-v1

Let `lambda>=1`, `|delta|<=lambda/2`, `a=lambda+delta`,

`P_- = lambda [[0,1],[1,0]]`, `P_+ = a I_2`,

`H=P_-+P_+=[[a,lambda],[lambda,a]]`,
`K=P_+-P_-=[[a,-lambda],[-lambda,a]]`,

and

`A=[[H,K],[K,H]]`.

All checks below are exact algebra.

1. `det H=det K=a^2-lambda^2=delta(2lambda+delta)`.

2. Since the block Hadamard change of basis diagonalizes `[[H,K],[K,H]]` algebraically into `H+K=2P_+` and `H-K=2P_-`,

`spec(A)={2a,2a,2lambda,-2lambda}`.

This spectral calculation is deterministic only; it is never used to rotate the product probability law.

3. The six physical 2x2 principal determinants are, up to order,

`0, 0, delta(2lambda+delta), delta(2lambda+delta), delta(2lambda+delta), delta(2lambda+delta)`.

For the three physical partitions into two 2-coordinate banks, the cross-block determinants are

`delta(2lambda+delta), 0, -delta(2lambda+delta)`.

Hence every determinant-based physical 2D certificate vanishes at `delta=0` and the largest such determinant tends to zero linearly in `delta`.

4. Every physical 3x3 principal block has characteristic polynomial

`(2a-t)(t^2-a t-2lambda^2)`.

Thus its eigenvalues are

`2a`, `(a+sqrt(a^2+8lambda^2))/2`, `(a-sqrt(a^2+8lambda^2))/2`.

For `a in [lambda/2,3lambda/2]`, the magnitude of the negative root is

`4lambda^2/(sqrt(a^2+8lambda^2)+a)
 >= 8lambda/(sqrt(41)+3) =: c0 lambda`.

The other two eigenvalues have larger modulus, so every physical triple has `min |eig| >= c0 lambda`, where `c0=8/(sqrt(41)+3)=0.8507810593...`.

5. The pinned localized Theorem A therefore yields

`||p_Q||_infty <= 6sqrt(pi)/(c0 lambda)
 = [3(3+sqrt(41))/4] sqrt(pi) lambda^{-1}
 = 12.4999528239... lambda^{-1}`.

6. If a scalar random variable Z has density cap M, layer cake gives

`sup_s E|Z-s|^{-1/2}
 <= int_0^infty min(1,2M u^{-2}) du
 = 2sqrt(2M)`.

With the preceding `M`, this becomes

`H_{1/2}(Q) <= pi^(1/4) sqrt(18+6sqrt(41)) lambda^{-1/2}
 = 9.99998112954... lambda^{-1/2}`.

For an independent whole copy Q', convolution gives `||p_{Q-Q'}||_infty<=M`; hence the same half-potential bound applies to `Q-Q'`. Using the positive-regularized identity

`int_R |t|^{-1/2}|phi_Q(t)|^2 dt = sqrt(2pi) E|Q-Q'|^{-1/2}`

gives

`int_R |t|^{-1/2}|phi_Q(t)|^2 dt
 <= 2 pi^(3/4) sqrt(9+3sqrt(41)) lambda^{-1/2}
 = 25.0662354451... lambda^{-1/2}`.

Also

`P(|Q-Q'|<=r) <= 2Mr
 = [3(3+sqrt(41))/2]sqrt(pi) lambda^{-1} r
 = 24.9999056478... lambda^{-1} r`.

At the exact singular point `delta=0`, each triple has spectrum `{-lambda,2lambda,2lambda}`, so the sharper constants are `M=6sqrt(pi)/lambda` and

`int |t|^{-1/2}|phi_Q|^2 <= 4sqrt(6) pi^(3/4) lambda^{-1/2}=23.1205425476... lambda^{-1/2}`.
