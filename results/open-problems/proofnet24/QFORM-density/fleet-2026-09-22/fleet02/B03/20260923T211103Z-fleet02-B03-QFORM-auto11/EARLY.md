# fleet02/B03 early calculation — marginal-free two-volume half-Riesz

Programme `QFORM-DENSITY-3EIG-20260922`. Full conjecture remains OPEN.

Let `Q=X^T A X+b^T X+c` with independent scalar densities at most 1. For a physical cut `I|J`, put `M=A[I,J]` and

`Z_2=e_2(MM^T)=sum_{|S|=|T|=2} det(M_{S,T})^2`.

I obtain the following candidate supporting theorem, now being checked branch-by-branch:

`H_{1/2}(Q):=sup_s E|Q-s|^{-1/2} <= 8 e^{1/4} Z_2^{-1/8}` whenever `Z_2>0`, with no two-volume row-marginal condition and arbitrary same-side quadratic terms.

Proof skeleton. Use the two-volume sampling row marginals `alpha_i`.

1. If every `alpha_i<=1/2`, the pinned volume-sampling decoupling proof with `k=2,q=1` gives

`|phi_Q(t)| <= min(1, 2 pi sqrt(e) Z_2^{-1/4}|t|^{-1})`.

The one-copy Riesz representation is absolutely integrable under this envelope, so

`H_{1/2}(Q) <= (2pi)^(-1/2) int |t|^{-1/2}|phi_Q(t)|dt <= 8 e^{1/4} Z_2^{-1/8}`.

2. If some physical row `m=M_i` has `alpha_i>1/2`, set `S=||m||_2`, project all remaining rows orthogonally to `m`, and let `F^2` be their squared Frobenius norm. Exterior-volume expansion gives the exact identity

`S^2 F^2 = alpha_i Z_2 > Z_2/2`.

If every projected one-volume row marginal is <=1/2, apply the fresh grouped projected-crossing theorem with `(k,ell)=(1,1)` and the genuine original coordinate `i` as hub. It gives

`|phi_Q(t)| <= min(1,2pi(SF)^(-1/2)|t|^{-1})`, hence

`H_{1/2}(Q) <= 8(SF)^(-1/4) < 8*2^(1/8) Z_2^(-1/8)`.

3. Otherwise one projected physical row `c_j` has `||c_j||^2>F^2/2`. Condition on the other same-side coordinates and promote `i,j` together. Their literal physical crossing to `J` has exact rank two and singular-value product

`Delta=S||c_j||`, so `Delta^2>Z_2/4`.

The exact-rank-two arbitrary-internal-functions crossing theorem has projection caps `M_X<=1`, `M_Y<=2`, hence

`|phi_Q(t)| <= min(1,pi sqrt(2) Delta^(-1/2)|t|^-1)`

and therefore

`H_{1/2}(Q) <= 8*2^(-1/4) Delta^(-1/4) < 8 Z_2^(-1/8)`.

Thus the spread branch dominates and the claimed constant is `8e^(1/4)=10.2722033335...`.

If this survives the source/correction audit, an immediate square-peel corollary is: after exact completion in any physical coordinate with diagonal `d!=0`, if the Schur residual has a physical cut with two-volume `Z_2>0`, then

`||p_Q||_infty <= 8 e^(1/4)|d|^(-1/2) Z_2^(-1/8)`, hence linear one-copy small-ball scale. This would remove the two-volume marginal gate entirely from the square-plus-crossing receiver.

No post-rotation independence is used; rotations appear only in deterministic projection-density bounds. The independent-copy identity remains whole-copy only.
