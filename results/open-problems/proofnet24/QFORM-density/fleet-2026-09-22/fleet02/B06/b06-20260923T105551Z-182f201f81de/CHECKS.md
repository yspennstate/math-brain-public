# Deterministic arithmetic checks

These are sanity checks only; the report contains the proofs.

Constants used in Theorem 2.1:

- `beta=sqrt(3)/(16sqrt(380)) = 0.005553270728991491`
- `delta=beta/sqrt(2) = 0.0039267553902346455`
- `gamma=1/(16sqrt(2)) = 0.044194173824159216`
- pivot coefficient `128(64/delta)^(1/4) = 1446.2604201069921`
- pair coefficient `8sqrt(5)[(beta^2-delta^2)(beta-delta)]^(-1/4) = 1421.4890679538598`

For the obstruction family with `N=128`, `u=(1,...,1)/sqrt(N)` and balanced-sign `v`, direct symmetric eigendecomposition of

`A=[[0,u^T],[u,vv^T]]`

returns the nonzero eigenvalues `[-1,1,1]` to machine precision. Also `u.v` is zero to machine precision and every light range leverage is `u_l^2+v_l^2=2/N=0.015625=1/64`.

The newest-Claude mixed-Fresnel constant in the two-heavy grouped family is

`12*2^(-1/3)=9.524406311809196...`.

The transverse row-area universal coefficient at `eta=1/128` is

`gamma*eta/sqrt(binomial(191,2)) = 2.563164996691298e-6`.
