# Deterministic checks for account02/B04 grouped clean-bank receiver

Run: `20260923T211520Z-account02-B04-qform`.

These are exact/symbolic arithmetic checks, not a benchmark or Monte Carlo experiment.

## 1. Frame and spectrum

Let

`b0=(1,1,1)/sqrt(3)`, `c0=(1,2,-3)/sqrt(14)`.

Then `||b0||=||c0||=1`, `b0.c0=0`, and

`d=b0 x c0=(-5,4,1)/sqrt(42)`.

For

`K_m=[2 b0, (2/sqrt(m))c0,...,(2/sqrt(m))c0]`,

there are `m` repeated `c0` columns and

`K_m K_m^T = 4 b0 b0^T + 4 c0 c0^T`.

Hence the nonzero singular values of `K_m` are exactly `2,2`. For

`A_m=[[0,K_m],[K_m^T,0]]`,

`spec(A_m)={2,2,-2,-2,0^(m)}`.

## 2. Anchored overlap-one compound mass

Write `b=2b0` and `c_z=2c0/sqrt(m)`. The complementary 2x2 minors of `[b,c_z]` are the components of

`b x c_z=(4/sqrt(m))d`.

Since each `b_n^2=4/3`,

`sum_n b_n^2 det([b,c_z]_{N\{n}})^2
 =(4/3)*(16/m)*||d||^2
 =64/(3m)`.

There are `m` choices of `z` and both row/column orientations in the ordered C1 compound sum. Therefore

`C_{1,h}=2*m*64/(3m)=128/3`.

A direct enumeration for `m=1,2,5` gives the same value and respectively `6,12,30` nonzero ordered anchored minors.

Every individual `{h,z}` rank-two area is

`||b wedge c_z||=4/sqrt(m)`.

## 3. Projection cap and density constant

The largest coordinate of the unit normal `d` has modulus `5/sqrt(42)`. For the two-dimensional projection

`Z=(b0^T X_N,c0^T X_N)`,

a fibre parameterization `x=U z+t d` and one original coordinate density cap give

`||p_Z||_infinity <= 1/max_i |d_i| = sqrt(42)/5`.

With `s1 s2=4`, the clean-bank theorem therefore yields

`||p||_infinity <= sqrt(2*pi*(sqrt(42)/5)/4)
                 = sqrt(pi*sqrt(42)/10)
                 = 1.426879370091898...`.

The dimension-free projection cap `2` instead gives `sqrt(pi)=1.772453850905516...`.

## 4. Exact physical pair-volume optimization

The only nonzero physical 2x2 minors of `K_m` use columns `{h,z}`. After summing over `z`, the squared-minor masses on row pairs `(23),(13),(12)` are proportional to

`25 : 16 : 1`,

so

`Z2=e2(K_m^T K_m)=16`,

and the canonical aggregated pair law is

`nu=(25/42,16/42,1/42)`.

For an arbitrary supported weight, entropy is maximized at fixed row-pair masses by taking the `z` coordinate uniformly inside each row-pair class. If `x=(x23,x13,x12)`, then exactly

`G2=16 exp[-D_KL(x||nu)]`.

The row marginal gate `alpha_i<=q/2` is equivalent to

`x23,x13,x12 >= ell:=1-q/2`,

hence it is feasible iff `q>=4/3`. The KL projection is

- `x=(q-1,1-q/2,1-q/2)` for `4/3<=q<=82/57`;
- `x=(25q/82,8q/41,1-q/2)` for `82/57<=q<=41/21`;
- `x=nu` for `41/21<=q<2`.

At the feasibility endpoint `q=4/3`, `x=(1/3,1/3,1/3)` and

`G2,opt=16*(50/343)^(1/3)=8.42064342546374...`.

For the previously proved entropy-weighted rank-two half-Riesz compiler,

`B(q)=4 sqrt(2e) q^(-1/4)(2-q)^(-1) G2,opt(q)^(-1/8)`,

direct differentiation on the three KL branches shows `B` is strictly increasing; hence the global optimum is

`B(4/3)=9.97494811429056...`.

This is a half-Riesz certificate, not by itself an L-infinity density certificate for the pure bilinear form.

## 5. All-cut volume and ridge obstruction

For any disjoint physical cut `I,J`, with each split into `N` and `L` parts, reordering rows and columns gives

`A_m[I,J] = diag(K_m[I_N,J_L], K_m[J_N,I_L]^T)`.

Thus

`rank A_m[I,J] <= |I_N|+|J_N| <=3`.

Consequently every fifth cross volume is zero. A nonzero third volume requires rank exactly three, which forces `|I_N|=1` or `2`; every supported full-rank 3x3 minor then contains every row in `I_N`, so at least one constrained row marginal equals one. Thus no weighting can satisfy the pinned D gate `alpha<=1/2` or D' gate `alpha<3/4`.

For the direct ridge gate, write `K_gamma=B B^T(gamma^2 I+B B^T)^(-1)` and `theta=tr K_gamma`. If the cut rank is at most two then `theta<2<=2q` for every `q>=1`. At rank three:

- if `|I_N|=2`, the rank-two block is supported on exactly those two constrained rows, so the leverage gate gives trace at most `q`; the remaining rank-one block has trace `<1`, hence `theta<q+1<=2q`;
- if `|I_N|=1`, the rank-one block contributes at most `q/2`. Rank three forces `h in I_L`; after removing its row, all `z` rows of the other rank-two block are proportional, so the `z` compression of its ridge matrix has rank at most one and trace `<1`, while the `h` diagonal is at most `q/2`. Again `theta<q+1<=2q`.

Therefore the completed direct ridge condition `theta>2q` fails on every physical cut and every regularization scale.

Manual narrow privacy scan: mathematical content only; no credentials, tokens, scheduler identifiers, machine paths, private personal data, benchmark answers, or unrelated material.
