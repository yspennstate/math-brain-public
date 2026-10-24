# account01/B09 r32 deterministic checks

Run: `20260924T065224Z-account01-B09-QFORM-auto11-r32`.

These are finite algebra regressions only; they are not statistical evidence for the universal conjecture.

## 1. Promoted-Gram factorization

For each `r=1,2,3,4`, generated a random physical `12 x r` orthonormal-mode matrix `V`, nonzero signed diagonal `Lambda`, a random physical hub column `c`, and promoted literal set `S={0,2,5}`. With

`x_j=(V_j,c_j)`, `G_R=sum_(j notin S)x_jx_j^T`,

`B_S=[V_S Lambda,0]`, `M=[I;B_S]`, `E=[0;I]`,

checked

`Gbar=M G_R M^T+EE^T`.

Observed absolute errors in `det Gbar-det G_R`:

- `r=1`: `8.88e-16`
- `r=2`: `0`
- `r=3`: `0`
- `r=4`: `0`.

Maximum residual-leverage errors

`|(Mx_j)^T Gbar^-1(Mx_j)-x_j^T G_R^-1x_j|`

were respectively

- `1.11e-16`
- `5.55e-17`
- `2.22e-16`
- `3.33e-16`.

Every retained promoted-hub weight `e_s^T Gbar^-1e_s` was `1` to floating error (`<=2.22e-16`).

## 2. Constant simplification

Partner theorem with all promoted hubs retained has

`h'=1+k`, `B=k`, `alpha=1+r/2`,

and

`K=2^-1 (4pi)^alpha [det G_R prod|lambda_q|]^-1/2`.

Hence

`alpha/[pi(alpha-1)] K^(1/alpha)`

simplifies exactly to

`C_r [det G_R prod|lambda_q|]^-1/(r+2)`,

`C_r=4(r+2)/r 2^-2/(r+2)`.

Numerical constants:

- `C_1=7.559526299369239`
- `C_2=5.656854249492381`
- `C_3=5.052388555034661`
- `C_4=4.762203155904599`.

## 3. Rank-r fixed-hub Pluecker identity

For random `V`, random signed `lambda`, random `c`, scalar `a=0.7`, and every tested disjoint leaf quadruple `(i,j,k,l)`, compared

`det [[a,c_k,c_l],[c_i,S_ik,S_il],[c_j,S_jk,S_jl]]`

against

`a sum_(p<q)lambda_p lambda_q Delta_(ij)^(pq) Delta_(kl)^(pq)`
` -sum_p lambda_p W_(ij)^p W_(kl)^p`.

Maximum absolute discrepancies:

- `r=1`: `8.88e-16`
- `r=2`: `1.25e-16`
- `r=3`: `5.33e-15`
- `r=4`: `8.88e-15`.

## 4. Actual target-valid rank-two family

With `m=8`, use three flat orthonormal Walsh vectors `d1,d2,d3` and

`v1=sqrt(3/5)e0+sqrt(2/5)d1`, `v2=d2`, `z=d3`.

Checks:

`<v1,v1>=<v2,v2>=<z,z>=1`, all mutual inner products zero.

For

`Q=(v1^T X)^2+(v2^T X)^2+2U(z^T X)`,

direct eigendecomposition of its physical matrix gives

`{-1,0,0,1,1,1}`

up to `2.3e-16` roundoff, hence the nonzero spectrum is exactly `{-1,1,1,1}`.

The unpromoted base Gram is `I_3`; literal row `0` has leverage `3/5`.

After promoting row `0`,

`G_R=diag(2/5,1,1)`, `det G_R=2/5`,

and each of the eight residual normalized leverages is exactly `3/8`.

The `r=2` promoted theorem gives

`4 sqrt(2) (2/5)^(-1/4)=7.113117640155692`.

## 5. Rank-one-through-four target regression

For the family

`Q_r=sum_(q=1)^r(v_q^T X)^2+2U(z^T X)`

with one heavy physical row of squared leverage `3/5` and a flat Walsh residual bank, the nonzero deterministic spectrum is `r` copies of `+1` plus `+1,-1`. After promoting the heavy row, `det G_R=2/5` and a sufficiently large Walsh bank has residual leverage `(r+1)/m<=1/2`.

Resulting density constants:

- `r=1`: `10.25985568006018`
- `r=2`: `7.113117640155692`
- `r=3`: `6.068547343420268`
- `r=4`: `5.547933582891972`.
