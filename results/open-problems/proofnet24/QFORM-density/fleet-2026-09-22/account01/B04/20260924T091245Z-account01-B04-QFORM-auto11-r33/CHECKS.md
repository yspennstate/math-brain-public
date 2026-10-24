# Deterministic checks — account01/B04 r33

Marker: `QFORM_B04_R33_ONE_SQUARE_ONE_CROSS_CHECK_PASS`

## 1. Constants

For `p=3/2`:

- `2^(p-1)/(2-p)=sqrt(2)/(1/2)=2sqrt(2)`.
- Raising to `1/p=2/3` gives `(2sqrt(2))^(2/3)=2`.
- `p/(p-1)=3`.

Hence Theorem (2.1) becomes exactly

`||p_Q||_infinity <=6 |b|^(-1/3) M^(2/3)`.

For the one-coordinate corollary `M=1/|c|`, this is

`6 |b|^(-1/3)|c|^(-2/3)`.

For `b=3/2`, `c=2`:

`6 (3/2)^(-1/3) 2^(-2/3)
 =6 / [ (3/2)^(1/3) 2^(2/3) ]
 =6 / 6^(1/3)
 =6^(2/3)
 =3.301927248894626...`.

Partner constant:

`3 sqrt(pi)=5.317361552716548...`.

Ratio:

`3 sqrt(pi)/6^(2/3)=1.610381196162520...`.

## 2. Fractional-moment rearrangement

For density cap `M`, exponent `alpha in (0,1)`, the cap-saturating centered interval has half-width `1/(2M)` and gives

`M * 2 int_0^(1/(2M)) r^(-alpha) dr
 = 2M/(1-alpha) * (2M)^(-(1-alpha))
 = (2M)^alpha/(1-alpha)`.

With `alpha=1/p`, this is

`(2M)^(1/p) p/(p-1)`.

The `2^(-1/p)` from the scaled linear variable `2sX_j` cancels the `2^(1/p)` exactly.

## 3. Three-coordinate spectral check

`T=[[3/2,0,1/10],[0,0,2],[1/10,2,0]]`.

Take

`T0=[3/2] direct_sum [[0,2],[2,0]]`.

Then

`spec(T0)={-2,3/2,2}`.

The perturbation is

`E=[[0,0,1/10],[0,0,0],[1/10,0,0]]`,

whose nonzero eigenvalues are `+1/10,-1/10`, hence `||E||_op=1/10`.

Weyl gives sorted eigenvalue intervals

`lambda_1(T) in [-21/10,-19/10]`,
`lambda_2(T) in [14/10,16/10]`,
`lambda_3(T) in [19/10,21/10]`.

Thus all three eigenvalues have modulus at least `7/5>1`.

Floating audit only: approximately

`-2.00142850, 1.49159729, 2.00983121`.

## 4. Enlarged same-matrix partner splice

For `eps=1/100`, the cross block `eps J_(3x6)` has one singular value

`eps sqrt(3*6)=sqrt(18)/100=3sqrt(2)/100
 =0.04242640687119285...`.

The symmetric off-diagonal perturbation

`[[0,E],[E^T,0]]`

has the same operator norm.

The top block has spectral distance from zero at least `7/5=1.4`. Partner r21 proves the bottom `A_*` has every eigenvalue of modulus greater than

`2-sqrt(5)/5-1/50
 =1.532786404500042...`.

Therefore the block-diagonal base has spectral distance from zero at least `1.4`, and the coupled matrix `Ahat` has spectral distance at least

`7/5-3sqrt(2)/100
 =1.357573593128807... >1`.

Thus every eigenvalue of the 9x9 coupled stress matrix has modulus greater than one.

## 5. Structural hypotheses on Ahat

Using top coordinates `i=1,j=2,k=3`:

- `Ahat_11=3/2`;
- `Ahat_12=0`;
- `Ahat_22=0`;
- `Ahat_23=2`.

Conditioning the six bottom coordinates turns their `eps` couplings to coordinate `j` into a deterministic translation of `2 X_3`; hence the scalar coefficient source still has density cap exactly at most `1/2`.

The bottom principal triple used in account02/B04 r21 is unchanged by the new cross block, so its eigenvalues remain `2,2,997/200` and the completed principal-block estimate remains `3sqrt(pi)` after conditioning outside coordinates.

All checks pass.
