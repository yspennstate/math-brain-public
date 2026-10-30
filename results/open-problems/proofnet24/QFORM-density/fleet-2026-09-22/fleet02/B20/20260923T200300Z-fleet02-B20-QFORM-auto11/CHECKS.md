# Deterministic checks for fleet02/B20 20260923T200300Z

All quantities below are coefficient-geometry checks; no random-coordinate rotation is used.

## Partner constants

`beta=0.01651671529470044`, `epsilon=0.0023595307563857772`, hence

`a_D=beta/sqrt(12)-epsilon=0.002408434254376076...`,

`a_H=beta/4-epsilon=0.0017696480672893325...`.

## Exact-collar stress constants

Take `q=32`, node scales `d=3/10`, `k=1/30`, and flat `32 x 2` Walsh frames `W_b`.

- common-plane leverage per K-coordinate: `(1/3)(2/q)=1/48<1/16`;
- combined arm singular value: `sqrt(3) d k=sqrt(3)/100=0.01732050807568877...>beta`;
- canonical arm singular values: `d k=1/100>a_D`;
- D1-D2 self-edge Frobenius norm: `sqrt(2)d^2=9sqrt(2)/100=0.1272792206135785...>0.11907425120090158`;
- K_a-K_b canonical block: `k^2 I_2=(1/900)I_2`;
- exact Schur cancellation:

`(1/900) * (1/(1/100)) * (9/100)=1/100`,

so `D_ab A_b^{-1}C=B_a`, `S_ab=0`, `R_ab=I_2`.

## N3(1/64) checks

The active same-bank diagonals are zero. The largest active physical cross coefficient is `9/100`; therefore every active two-coordinate principal determinant has modulus at most

`(9/100)^2=81/10000=0.0081<1/64=0.015625`.

For the 1024-coordinate exterior block `A_out=R_out R_out^T` with three flat orthonormal Walsh columns,

`(A_out)_{ii}=3/1024=0.0029296875<1/64`.

Every two-coordinate exterior principal block is positive semidefinite, hence its determinant lies in

`[0,(3/1024)^2]=[0,9/1048576]`,

and `9/1048576<1/64`. Active/exterior cross entries vanish, so mixed two-coordinate determinants are zero.

## Spectral and Fresnel checks

`A_out` has nonzero spectrum `{1,1,1}`. Therefore the direct-sum full matrix has `s_3(A)>=1`.

On the outside bank, the rank-three frame Gram matrix is `I_3` and each physical leverage is exactly `3/1024<1/2`. With the remainder zero on that bank, the pinned Theorem F applies and gives

`||p_(X^TAX)||_infinity<=12`.

## Exact common-Gram escape norm check

At exact zero defect define the rank-at-most-two Gram completion `S=ZEZ^T`. Then

`||A-S||_op>=s_3(A)>=sigma`.

Relative to `P direct_sum Q`,

`A-S=[[direct_sum_i Delta_i,PAQ],[QAP,QAQ]]`.

The block-diagonal part has norm `max(max_i||Delta_i||,||QAQ||)` and the off-diagonal part has norm `||PAQ||`. Hence

`sigma<=max(max_i||Delta_i||,||QAQ||)+||PAQ||`,

which forces at least one of `||PAQ||`, `max_i||Delta_i||`, `||QAQ||` to be at least `sigma/2`.

For the stress family specifically, the active self defects have norms `9/100` on D nodes and `1/900` on K nodes, `PAQ=0`, and the exterior block has norm `1`, so the theorem exits through `||QAQ||=1` as claimed.
