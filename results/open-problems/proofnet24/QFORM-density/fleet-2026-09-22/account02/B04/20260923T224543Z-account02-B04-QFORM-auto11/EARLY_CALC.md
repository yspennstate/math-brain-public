# Early calculation — clean-bank top-two projection

Run `20260923T224543Z-account02-B04-QFORM-auto11`.

Let `X=(X_i)_{i in I}` and `Y=(Y_j)_{j in J}` be disjoint original-coordinate product banks, each one-dimensional marginal having density at most one. Consider, after conditioning arbitrary outside original coordinates,

`Q = F(X) + <2 M^T X + b, Y> + c`,                         (E1)

where there is **no quadratic `Y-Y` term** and `M` has singular values `s1>=s2>0` (further singular values arbitrary).

Conditional on `X=x`, the sharp one-dimensional product projection bound gives

`||p_{Q|X=x}||_infinity <= sqrt(2)/||2M^T x+b||_2`.          (E2)

Let `u1,u2` and `v1,v2` be the first two left/right singular vectors. With `Z=(<u1,X>,<u2,X>)`, the two-dimensional product projection theorem gives `||p_Z||_infinity<=2`. Projecting the coefficient vector onto `span(v1,v2)` gives

`||2M^T X+b|| >= |2 diag(s1,s2) Z + d|`,                     (E3)

where `d=(<v1,b>,<v2,b>)`. The affine image `T=2 diag(s1,s2) Z+d` therefore has a probability density bounded by

`K = 1/(2 s1 s2)`.                                           (E4)

For every probability density `g<=K` on `R^2`, planar decreasing rearrangement gives

`int g(t)/|t| dt <= 2 sqrt(pi K)`.                            (E5)

Combining (E2)-(E5), uniformly in `b,F,c`,

`||p_Q||_infinity <= 2 sqrt(pi) (s1 s2)^(-1/2)`.              (E6)

This uses a deterministic coefficient-space projection only; no rotated random variables are asserted independent.

Stress packet for the full report: for `m=6`, `theta_r=2 pi r/6 + pi/24`,

`U_r=(cos(theta_r)/sqrt(3), sin(theta_r)/sqrt(3), 1/sqrt(6))`,

`V=I_3-(2/3) 11^T`,

`M_epsilon=U diag(2,2,epsilon) V^T`, and `B=J_6/24`. Then `U^T U=V^T V=I`, the singular values of `M_epsilon` are `2,2,epsilon`, and for

`A_epsilon=[[B,M_epsilon],[M_epsilon^T,0_3]]`

the exact spectrum is

`{2,2,-2,-2,(1+sqrt(1+64 epsilon^2))/8,(1-sqrt(1+64 epsilon^2))/8,0,0,0}`.

Thus the owner target holds with four eigenvalues of modulus two. The clean-bank estimate is the uniform bound `sqrt(pi)`.

For the natural physical cut, `E3(M_epsilon)=16 epsilon^2`. Since every physical left row of `U` has leverage `1/2`, the canonical squared-third-minor law is admissible for the pinned e5 Theorem D and has every row marginal exactly `1/2`. It also globally maximizes determinant-entropy currency: for every supported weight `w`, `G(w)=16 epsilon^2 exp(-KL(w||nu))<=16 epsilon^2`. Since the six row marginals always sum to three, no threshold `<1/2` is feasible. Hence the globally optimized D/D' certificate on this cut is exactly

`6 sqrt(e) 2^(-2/3) epsilon^(-1/3)`.

The newest account03/B04 r42 incident receiver sees `J_i=(1/2)E3=8 epsilon^2` and gives

`3*2^(5/6) epsilon^(-1/3)`.

For direct ridge, `K_gamma=U diag(k,k,h)U^T`, `k=4/(4+gamma^2)`, `h=epsilon^2/(epsilon^2+gamma^2)`, so every physical leverage is `k/3+h/6<=1/2`, while `theta=2k+h`. Whenever the completed q=1 ridge gate `theta>2` is valid, its simplified certificate

`R=sqrt(e)/(sqrt(2) gamma) * theta/(theta-2)`

obeys `R>=2 sqrt(2e)/epsilon`; choosing `gamma=sqrt(3/2) epsilon` gives `(2 sqrt(3e)+o(1)) epsilon^(-1)`. Thus the clean-bank top-two rearrangement ignores the weak third singular direction that both globally optimized third-volume and direct ridge still pay.
