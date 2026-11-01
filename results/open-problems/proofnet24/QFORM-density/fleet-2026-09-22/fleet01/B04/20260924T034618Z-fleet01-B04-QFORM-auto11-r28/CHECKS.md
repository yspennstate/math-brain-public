# Exact / deterministic checks for fleet01/B04 r28

Run: `20260924T034618Z-fleet01-B04-QFORM-auto11-r28`.

## Dual identity

For row-triple masses `z_S`, the finite Gibbs objective is

`F(p)=H(p)+sum_S p_S log z_S`.

With row constraints `alpha_i<=h`, its Lagrange dual is

`inf_(lambda>=0) [ log sum_S z_S exp(-sum_(i in S)lambda_i)+h sum_i lambda_i ]`.

Under `x_i=e^-lambda_i`, weighted Cauchy-Binet gives exactly

`sum_S z_S prod_(i in S)x_i = e_3(M^T diag(x) M)`.

## Three-heavy family

With `R_L=[L e1; L e2; L e3; U]`, `U^T U=I_4`, the face masses by heavy subset are

- empty: `4`;
- each singleton: `3 L^2`;
- each pair: `2 L^4`;
- triple: `L^6`.

Hence with equal heavy fugacity `x=y/L^2`,

`Z(y)=4+9y+6y^2+y^3`.

The common heavy marginal equals `1/2` iff total expected heavy count is `3/2`, i.e.

`y Z'(y)/Z(y)=3/2`.

After clearing denominators this is

`y^3+2y^2-3y-4=(y+1)(y^2+y-4)=0`,

so the positive root is

`r=(sqrt(17)-1)/2 = 1.5615528128088303...`.

Using `r^2+r=4`,

`Z(r)=4(r+1)(r+2)=36.49242250247064...`.

Thus

`C_3=Z(r) r^(-3/2)=18.701122669207603...`,

and

`G_(1/2)^*(M_L)=C_3 L^3`.

The corresponding marginals, computed directly from the weighted row-triple law, are

- heavy rows: `1/2,1/2,1/2`;
- each of the eight light rows: `3/16`.

Therefore the light inequalities are strictly inactive.

Numerical evaluations of the exact formula:

- `L=1`: `G*=18.701122669207603...`, density coefficient `6 sqrt(e) G*^(-1/6)=6.071843159192598...`;
- `L=2`: `G*=149.60898135366082...`, density coefficient `4.2934414721662355...`;
- `L=64`: `G*=4902387.100996758...`, density coefficient `0.7589803948990748...`.

## Dense target validity

The exact orthogonal matrix used is

`V=(1/15)[[14,-2,-3,-4],[-2,11,-6,-8],[-3,-6,6,-12],[-4,-8,-12,-1]]`.

Its integer numerator `N` satisfies `N N^T=225 I_4`.

For the eight light rows `U V^T`, the four distinct row patterns are

`[sqrt(2)/12,-sqrt(2)/12,-sqrt(2)/4,-5sqrt(2)/12]`,
`[17sqrt(2)/60,-11sqrt(2)/60,7sqrt(2)/20,-7sqrt(2)/60]`,
`[19sqrt(2)/60,23sqrt(2)/60,-sqrt(2)/20,sqrt(2)/60]`,
`[sqrt(2)/4,-sqrt(2)/4,-sqrt(2)/4,sqrt(2)/4]`,

each repeated twice. Every entry is nonzero. The three heavy rows `L e_i V^T` also have no zero entries.

The pure-cross matrix has eigenvalues `+/-sqrt(L^2+1)` each with multiplicity three and `+/-1` once. Adding `10^-3(J_11 direct_sum J_4)` has operator norm at most `0.011`, so for `L>=1` at least six eigenvalues retain modulus at least `sqrt(2)-0.011>1`.

## Designated partner r18 on L=1

Relative to heavy rows 1 and 2,

`(W_00,W_10,W_01,W_11)=(7,5,5,3)`.

The fleet02/B04 r18 two-carrier formula gives

`G_12=2(sqrt(21)+5)=19.165151389911678...`.

Its face probabilities are

`q_00=q_11=sqrt(21)/(2(sqrt(21)+5))=0.2391098093474000...`,
`q_10=q_01=5/(2(sqrt(21)+5))=0.2608901906526001...`.

The third heavy-row conditional inclusion probabilities on faces `00,10,01,11` are `3/7,2/5,2/5,1/3`, so

`alpha_3=0.3908910548820039...<1/2`.

Each light-row marginal is

`(2-alpha_3)/8=0.2011386181397495...<1/2`.

Thus the partner weight satisfies every Theorem-D row gate. Its full-law bound is

`6 sqrt(e) G_12^(-1/6)=6.047090231517419...`.

For comparison, at `L=2` the same two-carrier optimizer has third-heavy marginal `0.7183503419072274...>1/2`, while the new global three-carrier dual remains feasible.

## Grouped entropy cancellation

From

`log G_C=sum w log d + H(w)`,
`2 log F_C=H(w)+sum_i alpha_i log alpha_i`,

one gets identically

`G_C^(-1/(2d)) F_C^(1/d)
 = exp{-[sum w log d - sum_i alpha_i log alpha_i]/(2d)}`.

No numerical approximation enters this identity.
