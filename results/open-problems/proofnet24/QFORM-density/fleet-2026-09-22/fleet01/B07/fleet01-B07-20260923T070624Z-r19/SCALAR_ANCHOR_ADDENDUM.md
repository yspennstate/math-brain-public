# Addendum: scalar-anchor compound ladder gives rank-four tube or fifth-volume payment

This addendum preserves the immutable r19 coarse-role report and records a second, independent structural implication discovered before final publication. Full QFORM remains OPEN.

## Incoming physical block and sources

The newest available designated-partner checkpoint is

`yspennstate/math-open-problems@b72066231eb52c325a794f45135f9fb090ee9567`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/fleet02-B07-20260923T063044Z-r11/CHECKPOINT.md`.

Its current edge/core survivor contains a literal ORIGINAL-coordinate cross block

`B = [[b,u^T],[v,N]]`, with `b != 0`.

The completed designated-partner theorem applied below is fleet02/B07 `QFORM-CROSS-FIBER-PLANCHEREL-v1`, source

`yspennstate/math-open-problems@5266d24ea98d9bb5902c51a92eca0e3e38112e39`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T193347Z-b07-639234ec/REPORT.md`.

The fifth-volume receiver is the completed `D_5` theorem at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`:

`||p_Q||_infinity <= 5 sqrt(2e) E_5(C)^(-1/10)`

for any ORIGINAL-coordinate cross block `C`, with full ambient self blocks/outside couplings/affine terms retained; the density is continuous.

## 1. Exact scalar-anchor compound identity

Define the exact scalar Schur complement

`S=N-vu^T/b`.

For `q>=2`, let `H_q` be the sum of squared determinants of all physical `q x q` minors of `B` containing the distinguished anchor row and distinguished anchor column. Then

`boxed: H_q=b^2 E_{q-1}(S),`

where `E_k(S)=e_k(SS^T)` is the full squared `k x k` minor mass. Indeed, for every residual `(q-1)`-row set `I` and column set `J`,

`det [[b,u_J^T],[v_I,N_IJ]] = b det(S_IJ)`.

The same block elimination gives

`boxed: rank(B)=1+rank(S).`

No individual minor is selected or inverted.

## 2. Compound tail ladder

Let `mu_1>=mu_2>=...>=0` be the squared singular values of `S`, and set

`T_k(S)=sum_{j>k}mu_j=dist_F(S,{rank<=k})^2`.

For every `k>=1`,

`boxed: T_k(S) E_k(S) <= (k+1)E_{k+1}(S).`

Proof: expand

`(k+1)E_{k+1}=sum_{|I|=k}(prod_{i in I}mu_i)(sum_{j notin I}mu_j)`;

every complement sum is at least the tail after the top `k` singular squares.

Consequently, for every `m>=1`,

`boxed: E_{m+1}(S) >= T_m(S)^(m+1)/(m+1)!.`

Also `N=vu^T/b+S`; if `S_k` is best rank `k`, then `vu^T/b+S_k` has rank at most `k+1`, hence

`boxed: dist_F(N,{rank<=k+1})^2 <= T_k(S).`

## 3. Main structural theorem

### `QFORM-SCALAR-ANCHOR-LOWTAIL-OR-VOLUME-v1`

Put `G=||N||_F`. For every integer `m>=1` and every `delta>0`, either

`dist_F(N,{rank<=m+1}) <= delta G`,

or

`boxed: E_{m+2}(B) >= H_{m+2} > b^2 delta^(2m+2) G^(2m+2)/(m+1)!.`

If the rank-tube alternative fails, the preceding approximation inequality gives `T_m(S)>delta^2G^2`; the compound-tail lower bound and the exact anchored identity then yield the displayed estimate.

This is a dimension-free aggregate alternative. It is independent of the partner checkpoint's additional `E_2(N)` lower bound and therefore applies to the whole literal scalar-anchor block whenever `b !=0`.

## 4. Fifth-volume specialization

Take `m=3`, `delta=1/4`. Then either

`boxed: dist_F(N,{rank<=4}) <= G/4,`

or

`boxed: E_5(B)> b^2G^8/(3*2^19)=b^2G^8/1572864.`

In the second case the completed D5 theorem gives the full ambient continuous-density estimate

`boxed:
||p_Q||_infinity
 < 5sqrt(2e)(3*2^19)^(1/10)|b|^(-1/5)G^(-4/5)
 < 48.563 |b|^(-1/5)G^(-4/5).
`

On the current inherited edge-star-core scale, the partner branch has

`|b| ||s|| G > theta F^3/(36sqrt(2))`

and each of the three literal subobjects has norm at most `F`; therefore each individually exceeds

`cF`, `c=theta/(36sqrt(2))`.

Thus the paid fifth-volume branch satisfies

`boxed: ||p_Q||_infinity < (2472.401/theta) F^(-1).`

When the parent reduction supplies its already-recorded universal lower scale on `F`, this becomes an absolute universal constant. No such scale is silently assumed outside that parent branch.

## 5. Actual application of the completed designated-partner theorem

There is also a clean exact-rank-three endpoint. Assume

`H_3>0`, `H_4=0`.

Then `E_2(S)>0` and `E_3(S)=0`, hence `rank(S)=2` and therefore `rank(B)=3`.

If additionally

`dist_F(N,{rank<=2})>delta G`,

then `T_1(S)>delta^2G^2`. The `k=1` compound ladder gives

`2E_2(S)>=T_1(S)E_1(S)>=T_1(S)^2`,

so

`H_3=b^2E_2(S)>b^2delta^4G^4/2`.

Since `rank(B)=3`, `E_3(B)=pdet_+(BB^T)>=H_3`. Apply the completed fleet02/B07 cross-fiber Plancherel theorem at this actual inequality:

`boxed:
||p_Q||_infinity
 < 3e 2^(1/6) delta^(-2/3)|b|^(-1/3)G^(-2/3).
`

At `delta=1/4`,

`boxed: ||p_Q||_infinity < 6sqrt(2)e |b|^(-1/3)G^(-2/3).`

On the same inherited `|b|,G>cF` scale this becomes

`boxed: ||p_Q||_infinity < (432e/theta)F^(-1).`

The density is continuous on this exact-rank-three endpoint by the partner theorem.

## 6. What remains

This does **not** pay the nonzero rank-four-tube survivor by itself. A small Frobenius/operator tail cannot be deleted for arbitrary unbounded product inputs. The first new unpaid implication exposed by this addendum is therefore

`QFORM-SCALAR-ANCHOR-RANK4-TUBE-RECEIVER-v1`:

retain the literal physical anchor and original-coordinate product structure and pay

`dist_F(N,{rank<=4})<=||N||_F/4`

(or sharpen it until an existing stability/Plancherel receiver applies), while retaining the nonzero tail and arbitrary same-bank curvature.

The main r19 coarse-role theorem and this scalar-anchor theorem are complementary: the former extracts a global core-or-diffuse determinant packet directly from the three-large-eigenvalue hypothesis, while this addendum says that once an actual scalar anchor/core block is reached, failure of a bounded-rank tube automatically creates enough **aggregate higher compound volume** for an existing full-form Fourier receiver.