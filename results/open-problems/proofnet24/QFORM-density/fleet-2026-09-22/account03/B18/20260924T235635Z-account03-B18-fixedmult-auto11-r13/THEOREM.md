# QFORM-SHARP-ZERO-TWOHUB-v1

Let H={h1,h2} be two literal original coordinates and R their complement. Let all original coordinates be independent real random variables with densities bounded by K. Suppose A_HH=0 and define
G=A_HR A_HR^T.
If det G>0, then for arbitrary A_RR, b and c,
[
|p_{X^TAX+b^TX+c}|_inftyle 2sqrt{pi},K^2det(G)^{-1/4}.
]
The law has a continuous C0 density.

## Proof
Condition on X_R=Y. Put C=A_HR and V=2CY+b_H. Given Y, the variable is a translate of V dot X_H.

Livshyts--Paouris--Pivovarov (arXiv:1507.07949, Theorem 1.1) gives the sharp d-dimensional orthogonal marginal cap 2^(d/2) for a cap-one product density. By scaling, for v!=0,
[
|p_{vcdot X_H}|_inftyle sqrt2 K/|v|.
]
By a thin SVD of C and the d=2 case of the same theorem,
[
|p_{CY}|_inftyle 2K^2/sqrt{det(CC^T)}
=2K^2/sqrt{det G}.
]
Since V=2CY+b_H, scaling in dimension two gives
[
|p_V|_inftyle M:=K^2/(2sqrt{det G}).
]

For every probability density h<=M on R^2,
[
int |v|^{-1}h(v),dvle2sqrt{pi M}.
]
Indeed, by symmetric decreasing rearrangement the maximum is attained by h=M on the centered disc of area 1/M, and its integral is M*2*pi*r with pi*r^2=1/M.

Therefore, uniformly in t,
[
p_Q(t)le E[sqrt2K/|V|]
lesqrt2K,2sqrt{pi M}
=2sqrtpi K^2det(G)^{-1/4}.
]
This also proves absolute continuity.

For continuity, except on the V-null set {v1*v2=0}, the conditional linear form v1 X_h1+v2 X_h2 has a density which is a scaled convolution of two L1 densities, hence belongs to C0. The conditional density is dominated by sqrt(2)K/|V|, whose expectation is finite by the bound above. Dominated convergence gives continuity and vanishing at infinity after averaging over Y.

No rotated-coordinate independence is asserted. The arbitrary leaf quadratic block A_RR and all affine terms are retained exactly because conditioning only translates the conditional linear law.

## Live s4 application
account01/B06 commit 5af124af3d32cfc95682ed42de0f1aaabbc3eb81 proves a five-way structural router for s4(A)>=1. In its fifth branch,
[
lambda_{min}(A_{HR}A_{HR}^T)>9cdot10^{-5}.
]
At the exact endpoint A_HH=0, det G>(9e-5)^2, hence for K=1
[
|p_Q|_infty<2sqrtpi/sqrt{9e-5}=373.666081094.
]
Thus the exact-zero two-hub endpoint is paid with C0 regularity. The same structural branch with a small nonzero A_HH remains open.
