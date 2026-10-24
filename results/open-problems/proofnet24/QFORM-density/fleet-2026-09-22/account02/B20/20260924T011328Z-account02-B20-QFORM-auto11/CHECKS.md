# Deterministic checks — account02/B20 20260924T011328Z

All checks are exact-algebra checks for `REPORT.md`; no Monte Carlo claim is used as proof.

Let

- `delta=2^-18=1/262144`,
- `tau=27/2^20=27/1048576`,
- `r0=1/64+tau=16411/1048576`,
- `c2=4/9-1/2048-tau^2/2`,
- `c1=4/9-r0^2/2`.

Numerical evaluations:

- `tau = 0.00002574920654296875`;
- `r0 = 0.01565074920654297`;
- `c2 = 0.4439561628629336...`;
- `sqrt(c2) = 0.666300354842269...`;
- `1/(512 sqrt(c2)) = 0.0029312981537618367...`;
- `c1 = 0.44432197146908137...`;
- `sqrt(c1) = 0.6665748056063036...`;
- `2 delta/c1 = 0.000017170869372101035...`;
- `sqrt(c1/2) = 0.47133956521232195...`;
- `4 delta/c1 = 0.00003434173874420207...`;
- `c1^2/(4 delta) = 12938.249131142098...`;
- `sqrt(c1^2/(4 delta)) = 113.7464246960848...`.

Algebraic identities checked:

1. `E2=x1*x2+(x1+x2)T+e2_tail`.
2. `E3 >= x1*x2*T` by restricting to triples `{1,2,k}`, `k>=3`.
3. In R2, `x2>=1/64` and `E3<delta` imply `x1*T<1/4096`; since `x2<=x1`, also `x2*T<1/4096`.
4. `e2_tail<=T^2/2` follows from `e2(z)=((sum z)^2-sum z^2)/2`.
5. For residual `y=(x2,x3,...)`, with `R=sum y` and `T=sum_(k>=3)xk`, `T*R<=2e2(y)` because every singleton outside-sum is at least `T`; equivalently `2e2(y)-TR=x2*T-sum_(k>=3)xk^2>=0`.
6. If `x2<T`, then `x2<R/2`, `sum y_i^2<=x2*R<R^2/2`, hence `e2(y)>R^2/4`.
7. For a rectangular block `F`, the symmetric embedding `[[0,F],[F^T,0]]` has operator norm `||F||op`.
8. Any rank-at-most-two matrix `B` obeys `||A-B||op>=s3(A)`.

Stress-family check for `c=1/2`, three equal residual singular values `a=1/(sqrt(6)L)`:

- singular squares are `L^2, 1/(6L^2),1/(6L^2),1/(6L^2)`;
- `E2=1/2+1/(12L^4)>4/9`;
- `E3=1/(12L^2)+1/(216L^6)`;
- `x2=1/(6L^2)` and `T2=1/(3L^2)=2x2`;
- `s1*dist_F(rank<=1)=L*sqrt(1/(2L^2))=1/sqrt(2)`;
- for sufficiently large `L`, `E3<2^-18` and `s2<1/8`.

Pinned D5 arithmetic:

`e5(M^TM)>=1/1024=2^-10`
`=> e5^(-1/10)<=2`
`=> ||p_Q||infinity <=5 sqrt(2e)*2=10 sqrt(2e)=23.316... <23.317`.
