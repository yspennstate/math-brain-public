# Early implication — two heavy E3 carriers

Programme `QFORM-DENSITY-3EIG-20260922`; fleet02/B04. Full unrestricted QFORM remains OPEN.

First unpaid implication attacked: `QFORM-HIGHLEVERAGE-RESIDUAL-TO-CARRIER-DELETION-DICHOTOMY-v1`.

Fresh pinned input: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, where Theorem D permits arbitrary supported physical 3-minor weights with row marginals at most `1/2`, replacing `Z` by `G=exp(E log det^2+H)`. The D' extension permits cap `h<3/4`. Fresh designated partner fleet03/B04 r47 is `math-open-problems@24476f8abf801b3e862fd227748790459d731340`, proving rank-free higher-compound downshift, in particular `||p_Q||inf <=7.659094523616393 E4(M)^(-1/8)` on any literal cross block with `E4(M)>0`.

New calculation. Coarsen a physical 3-minor law by two distinguished row carriers `i,j`; let `W_ab` be the total squared-minor mass in category `1{i in S}=a,1{j in S}=b`. Conditional Gibbs optimization shows the global entropy-determinant problem reduces exactly to

`max_q H(q)+sum_ab q_ab log W_ab`

under the carrier marginal constraints. In the symmetric case `W_10=W_01=A`, at the Theorem-D cap `1/2` both active constraints force `q_00=q_11=r`, `q_10=q_01=1/2-r`. The unique optimum obeys

`r/(1/2-r)=sqrt(W_00 W_11)/A`,

and therefore

`G_* = 2(A+sqrt(W_00 W_11)).`

This is a genuine two-carrier analogue of the previous one-carrier currency `2 sqrt(W_0 W_1)`: two individually over-heavy carriers can still be paid without selecting a small local minor when the four face masses interact at geometric-mean scale.

Concrete rank-four target family for the full optimization: let `U=H_8[:,1:4]/sqrt(8)` together with the constant Hadamard column, so `U^T U=I_4`; stack rows `L e_1,L e_2` above the eight rows of `U`, and right-multiply by a fixed dense orthogonal 4x4 Householder matrix. Then

`W_00=4, W_10=W_01=3L^2, W_11=2L^4`,

so

`G_* = 2(3+2sqrt(2))L^2 = 2(1+sqrt(2))^2 L^2.`

The eight light-row marginals under this optimizer are exactly `1/4`; hence no hidden third carrier constraint appears. The same block has singular squares `L^2+1,L^2+1,1,1`, hence `E4=(L^2+1)^2`, so partner r47 applies positively on the identical physical matrix. Next: prove the full supported-weight optimum, include D' endpoint optimality at a concrete `L`, and compare the direct ridge gate on the same matrix.
