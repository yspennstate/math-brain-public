# Deterministic checks for environment-adaptive difference localization

Run `20260924T111014Z-fleet01-B14-auto11`. Full QFORM remains open.

## C1. Active block spectrum

For

`M=(1/sqrt(2))*[[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1],[0,0,1]]`,

`M^T M=I_3`. Therefore the singular values of `M` are `(1,1,1)` and the block matrix

`B=[[0,M],[M^T,0]]`

has eigenvalues `(+1,+1,+1,0,0,0,-1,-1,-1)`. A direct numerical eigensolve gave

`[-1,-1,-1,1.12e-16,1.12e-16,1.12e-16,1,1,1]`,

with the `1e-16` entries numerical zero.

## C2. Volume-sampling data

A nonzero `3x3` row minor chooses exactly one row from each duplicated standard-basis pair, so there are `2^3=8`. Each determinant has magnitude `(1/sqrt(2))^3=1/(2 sqrt(2))`; squared determinant is `1/8`. Thus

`Z=e_3(M^TM)=8*(1/8)=1`.

Every physical row belongs to `2^2=4` nonzero minors, so its volume-sampling marginal is

`4*(1/8)/1=1/2`.

This is exactly the endpoint allowed by theorem D.

## C3. Constant

`6*sqrt(e)=9.89232762420077...`.

## C4. Fiberwise cap repair

For every environment value `t`, copied-side subdensity

`rho_{j,a,t}(y)=f_j(y) theta_{j,a}(t,y)`

has mass `m_{j,a}(t)`. Since `0<=f_j<=1`,

`G(w)=int f_j(w+y) rho_{j,a,t}(y)dy <= m_{j,a}(t)`

and Tonelli gives `int G=m_{j,a}(t)`. Hence `G/m` is a cap-one probability density whenever `m>0`; zero-mass cells vanish. No lower bound on `m` is used.

For coordinatewise product partitions, the cell weights multiply and sum to one for every `t`:

`sum_alpha prod_j m_{j,alpha_j}(t)=prod_j sum_a m_{j,a}(t)=1`.

Thus any uniform linear/nonnegative decoupled receiver bound is preserved exactly after summing the labels and then the environment.

## C5. Scope guard

The argument does **not** cover a single label depending jointly on several copied coordinates, because the normalized conditional difference law need not remain product. It also does not permit localization of the undecomposed active copy before the receiver norm. These remain outside the theorem's scope.
