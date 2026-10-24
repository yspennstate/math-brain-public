# r36 deterministic checks

These are algebra/constant checks only; they are not probabilistic evidence for the unrestricted conjecture.

## 1. Symmetric 3D BL kernel identity

For

`A=[[0,a,b],[a,0,c],[b,c,0]]`

the kernel generators used in Proposition 2.1 are

`k1=(0,-b,a)`, `k2=(c,0,-a)`, `k3=(-c,b,0)`.

Direct coordinate addition gives

`k1+k2+k3=(0,0,0)`.

Also `L1 k1=(0,0)`, `L2 k2=(0,0)`, `L3 k3=(0,0)` exactly.

## 2. Bipartite change-of-variables scaling

For invertible `k x k` `B`, `u=t B dY` has Jacobian

`ddY = |t|^{-k}|det B|^{-1} du`.

The quadratic same-bank term `C dX` enters only as translation `u -> u+t C dX`, so it produces no determinant factor. The same check applies to `v=t B^T dX` on the other Cauchy--Schwarz factor.

Thus each squared factor integral is bounded by

`pi^k |t|^{-k}|det B|^{-1}`,

and their geometric mean has the same value, proving the constant in (3.2).

## 3. Weighted-time integration

Set `T=pi |det B|^{-1/k}`. Then

`min(1,T^k t^{-k})`

switches branches at `t=T`, and

`2*[ integral_0^T t^(-1/2)dt + T^k integral_T^infty t^(-k-1/2)dt ]`

`= 4 sqrt(T) + 4 sqrt(T)/(2k-1)`

`= [8k/(2k-1)] sqrt(pi) |det B|^(-1/(2k))`.

At `k=2` the numerical outer constant is

`(16/3)*sqrt(pi) = 9.453087204829417...`.

Dividing by `sqrt(2pi)` in the whole-copy Riesz identity gives collision constant

`8sqrt(2)/3 = 3.7712361663282534...`.

## 4. One-copy half-Riesz at k=2

For `K=pi |det B|^-1/2`,

`integral_R |t|^-1/2 min(1,K|t|^-1) dt = 8 sqrt(K)`.

Multiplying by `(2pi)^-1/2` gives exactly

`4sqrt(2)|det B|^-1/4 = 5.656854249492381... |det B|^-1/4`.

The account02/B03 aggregate `Z2` theorem gives instead, on a literal 2x2 crossing,

`8 e^(1/4)|det B|^-1/4 = 10.272203333501931... |det B|^-1/4`.

The local square-invertible theorem is sharper, while the partner theorem covers rectangular/high-dimensional rank-two packets.

## 5. L1 time integration at k>2

For the one-copy envelope `min(1,T^(k/2)t^(-k/2))`,

`integral_R |phi(t)| dt <= 2T[1+2/(k-2)] = 2kT/(k-2)`.

After division by `2pi`,

`||p||_infty <= [k/(k-2)] |det B|^-1/k`.

For `k=3`, this is `3 |det B|^-1/3`.

## 6. Target-valid rank-two stress family

For even `m=2r`,

`A_m=[1] direct_sum (J_m/m) direct_sum (-J_m/m)`

has nonzero eigenvalues exactly `{1,1,-1}` because `J_m/m` has spectrum `{1,0,...,0}`.

Splitting both rank-one banks into `r+r`, the cross block is

`M=diag(J_r/m,-J_r/m)`.

Each nonzero singular value is `r/m=1/2`. Hence

`Z2=e2(MM^T)=(1/4)(1/4)=1/16`.

The partner square-plus-Z2 theorem with `d=1` gives

`8 e^(1/4) (1/16)^(-1/8) = 8sqrt(2)e^(1/4)`

`=14.52708926969255...`.
